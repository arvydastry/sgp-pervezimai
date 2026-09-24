#!/usr/bin/env python3
"""SGP v2 — native-coverage report for the built site (python3 stdlib only).

  python3 tools/coverage.py           summary (blocks by verdict, labels by element, custom layer size)
  python3 tools/coverage.py --md      the same as Markdown tables (for docs/salient-atitikimas-rezultatas.md)

Blocks = row-level WPBakery units: every Section / Row / Global Section that is a direct child of <main>, plus the
chrome Global Sections (header ticker, mega menu, off-canvas, footer, call bar) counted once as „_global“.
Unique blocks are de-duplicated by their data-salient label (the same recipe on several pages = one block).
Verdicts (same scale as docs/salient-auditas.md):
  CUSTOM      the block contains code that no Salient element produces (<script>, Raw HTML markers, inline <svg>
              other than the kit's line icons, sgp-* classes outside the six allowed Extra Classes)
  NATIVE+CSS  native elements + a numbered group of assets/css/sgp-custom.css (C-4 call bar, C-5 schedule rows,
              C-6 Fluent Forms, C-7 hotspots, C-8 Page Submenu, C-9 Complianz, C-12 ticker, C-14 pause button)
  NATIVE      only element options and Design Options (global C-2 reduced motion, C-3 typography, C-11 focus are
              site-wide and not counted per block)
  WRONG-MAPPING  an option that does not exist in 18.2.1 — tools/check.py refuses those, so this stays 0
"""
import collections
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from check import find_pages  # noqa: E402

ALLOWED_SGP = {'sgp-dark', 'sgp-num', 'sgp-callbar', 'sgp-grafikas', 'sgp-ticker', 'sgp-motion-toggle'}
CSS_GROUPS = [('C-4', lambda c: 'sgp-callbar' in c), ('C-5', lambda c: 'sgp-grafikas' in c), ('C-6', lambda c: 'fluentform' in c),
              ('C-7', lambda c: 'nectar_image_with_hotspots' in c), ('C-8', lambda c: 'page-submenu' in c),
              ('C-9', lambda c: any(x.startswith('cmplz-') for x in c)), ('C-12', lambda c: 'sgp-ticker' in c),
              ('C-14', lambda c: 'sgp-motion-toggle' in c)]
ICON_SVG = {'nectar-inline-icon', 'nectar-cta__icon'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'path', 'circle', 'rect', 'use'}


def element_name(label):
    head = re.split(r'\s(?:→|·)\s|\s\(', label, maxsplit=1)[0].strip()
    head = re.sub(r'\s+(?:\d+/\d+|[¼½¾⅓⅔]).*$', '', head)            # Column 7/12, Column ¼ → Column
    head = re.sub(r'^Row \d+$', 'Row', head)
    head = re.sub(r'\s+(?:[0-9]{5,}|„.*|".*)$', '', head)          # Image 4440774 / Global Section „GS-…“
    head = re.sub(r'\s+×\s*\d+$', '', head)
    return head or '?'


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth, self.in_main, self.cur, self.blocks, self.labels, self.chrome = 0, False, None, [], [], []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get('class') or '').split()
        if a.get('data-salient'):
            self.labels.append(a['data-salient'])
        top = None
        if tag == 'main':
            self.in_main = True
            self.main_depth = len(self.stack)
        elif self.cur is None and ('vc_section' in cls or 'wpb_row' in cls or 'nectar-global-section' in cls):
            parent_is_main = self.in_main and len(self.stack) == self.main_depth + 1
            if parent_is_main or not self.in_main:
                top = {'label': a.get('data-salient', ''), 'groups': set(), 'custom': [], 'chrome': not self.in_main,
                       'depth': len(self.stack)}
                self.cur = top
        if self.cur is not None:
            for g, test in CSS_GROUPS:
                if test(cls):
                    self.cur['groups'].add(g)
            bad = [c for c in cls if c.startswith('sgp-') and c not in ALLOWED_SGP]
            if bad:
                self.cur['custom'].append('class ' + bad[0])
            if tag == 'script':
                self.cur['custom'].append('<script>')
            if tag == 'svg' and not ICON_SVG & set(cls):
                self.cur['custom'].append('inline <svg>')
        if tag not in VOID and not tag.endswith('/'):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            t = self.stack.pop()
            if t == tag:
                break
        if tag == 'main':
            self.in_main = False
        if self.cur is not None and len(self.stack) <= self.cur['depth']:
            (self.chrome if self.cur['chrome'] else self.blocks).append(self.cur)
            self.cur = None


def verdict(b):
    if b['custom']:
        return 'CUSTOM'
    return 'NATIVE+CSS' if b['groups'] else 'NATIVE'


def main(argv):
    md = '--md' in argv
    pages = [p for p in find_pages([]) if not p.startswith('docs/')]
    per_page, uniq, chrome, labels = {}, {}, {}, collections.Counter()
    for rel in pages:
        p = Blocks()
        p.feed(open(os.path.join(ROOT, rel), encoding='utf-8').read())
        per_page[rel] = p.blocks
        for b in p.blocks:
            uniq.setdefault(b['label'] or f'(unlabelled {rel})', b)
        for b in p.chrome:
            chrome.setdefault(b['label'], b)
        for lb in p.labels:
            labels[element_name(lb)] += 1
    allb = list(uniq.values()) + list(chrome.values())
    cnt = collections.Counter(verdict(b) for b in allb)
    n = len(allb)
    css = os.path.join(ROOT, 'assets', 'css', 'sgp-custom.css')
    js = os.path.join(ROOT, 'assets', 'js', 'sgp-custom.js')
    css_n = sum(1 for ln in open(css, encoding='utf-8') if ln.strip())
    js_n = len(open(js, encoding='utf-8').read().rstrip('\n').split('\n'))
    page_css = os.path.join(ROOT, 'assets', 'css', 'pages')
    page_css_n = sum(sum(1 for ln in open(os.path.join(page_css, f), encoding='utf-8') if ln.strip())
                     for f in os.listdir(page_css)) if os.path.isdir(page_css) else 0
    groups = collections.Counter(g for b in allb for g in b['groups'])
    total_labels = sum(labels.values())
    if md:
        print('| Verdiktas | Blokų | Dalis |\n|---|---:|---:|')
        for k in ('NATIVE', 'NATIVE+CSS', 'CUSTOM', 'WRONG-MAPPING'):
            print(f'| {k} | {cnt.get(k, 0)} | {100 * cnt.get(k, 0) / n:.0f} % |')
        print(f'| **Iš viso (unikalūs blokai)** | **{n}** | |')
        print('\n| Elementas (data-salient) | Žymių |\n|---|---:|')
        for k, v in labels.most_common(40):
            print(f'| {k} | {v} |')
        print(f'| **Iš viso žymių (21 psl.)** | **{total_labels}** |')
    else:
        print(f'pages: {len(pages)} · row-level blocks on pages: {sum(len(v) for v in per_page.values())} · unique blocks: {len(uniq)} + chrome GS {len(chrome)} = {n}')
        for k in ('NATIVE', 'NATIVE+CSS', 'CUSTOM', 'WRONG-MAPPING'):
            print(f'  {k:<13} {cnt.get(k, 0):>4}  {100 * cnt.get(k, 0) / n:5.1f} %')
        print('  sgp-custom.css groups used by blocks: ' + ', '.join(f'{g}×{c}' for g, c in sorted(groups.items())))
        for b in allb:
            if verdict(b) == 'CUSTOM':
                print(f'  CUSTOM: {b["label"][:80]} ← {b["custom"][:3]}')
        print(f'data-salient labels: {total_labels} across {len(labels)} element types')
        for k, v in labels.most_common(60):
            print(f'  {v:>5}  {k}')
        print(f'custom layer: sgp-custom.css {css_n} non-blank lines · sgp-custom.js {js_n} lines · page CSS {page_css_n} lines')
        for rel in pages:
            c = collections.Counter(verdict(b) for b in per_page[rel])
            print(f'  {rel:<80} blocks {len(per_page[rel]):>3} · ' + ' · '.join(f'{k} {c[k]}' for k in ('NATIVE', 'NATIVE+CSS', 'CUSTOM') if c[k]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
