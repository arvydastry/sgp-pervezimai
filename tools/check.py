#!/usr/bin/env python3
"""SGP pervežimai v2 — built-site checker (python3 stdlib only).

  python3 tools/check.py            check every built page (repo root, v1/ docs/ src/ tools/ excluded)
  python3 tools/check.py apie-imone check only pages whose path starts with a prefix (links into other pages still resolve)

Errors (exit code 1): unresolved relative href/src/srcset/poster, missing #fragment targets, duplicate ids,
<img> without alt, tel: numbers outside the 5 allowed (and site-wide set must be exactly those 5),
<html lang> not "lt", not exactly one <h1>, empty <title>/meta description, leftover {{ }} placeholders,
ARIA/popover id references that do not exist, mis-nested tags, nested interactive elements,
Pexels media not listed in docs/media.json (src/srcset/poster, data-hd/-sd/-src/-poster/-hover-video,
og:image), root-absolute links (except /sgp-pervezimai/ on 404.html).
Warnings: media ids from the design system's "never use" list, external http:// URLs.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'.git', 'v1', 'docs', 'src', 'tools', 'assets', '.claude', 'node_modules'}
SITE_BASE = '/sgp-pervezimai/'
TEL_ALLOWED = {'+37065053161', '+353864503104', '+447566878681', '+37063828919', '+34602547929'}
NEVER_USE = {'7464393', '38404178', '12421166', '19274366', '3987777', '32313192', '15885602', '35531295',
             '11479826', '7828591', '8874803', '8828587'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
OPTIONAL_END = {'p', 'li', 'dt', 'dd', 'option', 'optgroup', 'tr', 'td', 'th', 'thead', 'tbody', 'tfoot', 'colgroup', 'caption', 'rp', 'rt'}
INTERACTIVE = {'a', 'button'}
ID_REF_ATTRS = ('aria-controls', 'aria-labelledby', 'aria-describedby', 'popovertarget', 'for', 'list')
URL_ATTRS = {('a', 'href'), ('link', 'href'), ('script', 'src'), ('img', 'src'), ('source', 'src'),
             ('video', 'src'), ('video', 'poster'), ('audio', 'src'), ('iframe', 'src'), ('form', 'action')}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.urls, self.tels, self.errors = [], [], [], []
        self.idrefs, self.frag_uses = [], []
        self.lang = None
        self.h1 = 0
        self.title, self.in_title = '', False
        self.description = None
        self.stack = []
        self.img_no_alt = 0

    def _line(self):
        return self.getpos()[0]

    def handle_starttag(self, tag, attrs):
        self._tag(tag, attrs, closing=False)

    def handle_startendtag(self, tag, attrs):
        self._tag(tag, attrs, closing=True)

    def _tag(self, tag, attrs, closing):
        a = {k: (v if v is not None else '') for k, v in attrs}
        line = self._line()
        if tag == 'html':
            self.lang = a.get('lang')
        if 'id' in a:
            self.ids.append((a['id'], line))
        if tag == 'h1':
            self.h1 += 1
        if tag == 'title':
            self.in_title = True
        if tag == 'meta' and a.get('name') == 'description':
            self.description = a.get('content', '')
        if tag == 'img' and 'alt' not in a:
            self.img_no_alt += 1
            self.errors.append(f'line {line}: <img> without alt ({a.get("src", "")[:60]})')
        for (t, attr) in URL_ATTRS:
            if tag == t and attr in a:
                self.urls.append((a[attr], line, f'{t}[{attr}]'))
        for attr in ('srcset', 'imagesrcset'):
            if attr in a:
                for part in a[attr].split(','):
                    u = part.strip().split(' ')[0]
                    if u:
                        self.urls.append((u, line, f'{tag}[{attr}]'))
        for attr in ('data-hd', 'data-sd', 'data-hover-video', 'data-src', 'data-poster'):
            if attr in a:
                self.urls.append((a[attr], line, f'{tag}[{attr}]'))
        if tag == 'meta' and (a.get('property') or a.get('name')) in ('og:image', 'twitter:image') and a.get('content'):
            self.urls.append((a['content'], line, f'meta[{a.get("property") or a.get("name")}]'))
        if tag == 'use':
            h = a.get('href') or a.get('xlink:href') or ''
            if h.startswith('#'):
                self.frag_uses.append((h[1:], line))
        if tag == 'a' and a.get('href', '').startswith('tel:'):
            self.tels.append((a['href'][4:], line))
        for attr in ID_REF_ATTRS:
            if a.get(attr):
                for ref in a[attr].split():
                    self.idrefs.append((ref, line, attr))
        if tag in INTERACTIVE and any(t in INTERACTIVE for t, _ in self.stack):
            outer = next(t for t, _ in reversed(self.stack) if t in INTERACTIVE)
            self.errors.append(f'line {line}: interactive <{tag}> nested inside <{outer}>')
        if not closing and tag not in VOID:
            self.stack.append((tag, line))

    def handle_endtag(self, tag):
        line = self._line()
        if tag == 'title':
            self.in_title = False
        if tag in VOID:
            return
        if not any(t == tag for t, _ in self.stack):
            self.errors.append(f'line {line}: stray </{tag}>')
            return
        while self.stack:
            t, l = self.stack.pop()
            if t == tag:
                break
            if t not in OPTIONAL_END:
                self.errors.append(f'line {line}: </{tag}> closes <{t}> opened on line {l} (mis-nested)')

    def handle_data(self, data):
        if self.in_title:
            self.title += data

    def close(self):
        super().close()
        for t, l in self.stack:
            if t not in OPTIONAL_END and t not in ('html', 'body', 'head'):
                self.errors.append(f'line {l}: <{t}> never closed')


def find_pages(prefixes):
    pages = []
    for dirpath, dirnames, files in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == '.':
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in files:
            if fn.endswith('.html'):
                rel = os.path.normpath(os.path.join(rel_dir, fn)).replace(os.sep, '/')
                if not prefixes or any(rel.startswith(p) for p in prefixes):
                    pages.append(rel)
    return sorted(pages)


_ids_cache = {}


def ids_of(path):
    if path not in _ids_cache:
        p = PageParser()
        with open(path, encoding='utf-8') as f:
            p.feed(f.read())
        _ids_cache[path] = {i for i, _ in p.ids}
    return _ids_cache[path]


def resolve(page_rel, url):
    """→ (abs file path or None for external/skip, fragment, error)"""
    if not url or url.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
        return None, None, None
    sp = urlsplit(url)
    if sp.scheme in ('http', 'https') or url.startswith('//'):
        return None, None, None
    path, frag = unquote(sp.path), sp.fragment
    if path == '':
        return os.path.join(ROOT, page_rel), frag, None
    if path.startswith('/'):
        if page_rel == '404.html' and path.startswith(SITE_BASE):
            path = path[len(SITE_BASE):] or './'
            target = os.path.normpath(os.path.join(ROOT, path))
        else:
            return None, None, f'root-absolute URL {url!r} (use relative paths / {{{{root}}}})'
    else:
        target = os.path.normpath(os.path.join(ROOT, os.path.dirname(page_rel), path))
    if not target.startswith(ROOT):
        return None, None, f'{url!r} points outside the site'
    if url.split('#')[0].split('?')[0].endswith('/') or os.path.isdir(target):
        target = os.path.join(target, 'index.html')
    return target, frag, None


def main(argv):
    prefixes = [a for a in argv if not a.startswith('-')]
    with open(os.path.join(ROOT, 'docs', 'media.json'), encoding='utf-8') as f:
        media = json.load(f)
    media_ids = {p['id'] for p in media['photos']} | {v['id'] for v in media['videos']}
    pages = find_pages(prefixes)
    if not pages:
        print('check: no built pages found — run python3 tools/build.py first')
        return 1
    total_err, total_warn = 0, 0
    site_tels = set()
    for rel in pages:
        path = os.path.join(ROOT, rel)
        with open(path, encoding='utf-8') as f:
            raw = f.read()
        p = PageParser()
        p.feed(raw)
        p.close()
        errs, warns = list(p.errors), []
        if p.lang != 'lt':
            errs.append(f'<html lang> is {p.lang!r}, expected "lt"')
        if p.h1 != 1:
            errs.append(f'{p.h1} <h1> elements (exactly one required)')
        if not p.title.strip():
            errs.append('empty <title>')
        if not (p.description or '').strip():
            errs.append('missing/empty meta description')
        for m in re.finditer(r'\{\{[^}]*\}\}', raw):
            errs.append(f'leftover placeholder {m.group(0)}')
        seen = {}
        for i, line in p.ids:
            if i in seen:
                errs.append(f'line {line}: duplicate id "{i}" (first on line {seen[i]})')
            else:
                seen[i] = line
        idset = set(seen)
        for ref, line, attr in p.idrefs:
            if ref not in idset:
                errs.append(f'line {line}: {attr}="{ref}" – no element with that id')
        for ref, line in p.frag_uses:
            if ref not in idset:
                errs.append(f'line {line}: <use href="#{ref}"> – icon symbol missing')
        for num, line in p.tels:
            site_tels.add(num)
            if num not in TEL_ALLOWED:
                errs.append(f'line {line}: tel:{num} is not one of the 5 company numbers')
        for url, line, where in p.urls:
            for mid in re.findall(r'pexels\.com/(?:photos|videos|video-files)/(\d+)/', url):
                if mid not in media_ids:
                    errs.append(f'line {line}: Pexels id {mid} is not in docs/media.json')
                elif mid in NEVER_USE:
                    warns.append(f'line {line}: Pexels id {mid} is on the „never used“ list (§6.0)')
            if url.startswith('http://'):
                warns.append(f'line {line}: insecure URL {url[:70]}')
            target, frag, err = resolve(rel, url)
            if err:
                errs.append(f'line {line}: {where}: {err}')
                continue
            if target is None:
                continue
            if not os.path.exists(target):
                errs.append(f'line {line}: {where} → {url} (missing {os.path.relpath(target, ROOT)})')
                continue
            if frag and target.endswith('.html'):
                ids = idset if os.path.samefile(target, path) else ids_of(target)
                if frag not in ids and frag != 'main':
                    errs.append(f'line {line}: {where} → {url} (no id "{frag}" in {os.path.relpath(target, ROOT)})')
        status = 'OK ' if not errs else 'ERR'
        print(f'{status} {rel}' + (f'  ({len(errs)} error(s))' if errs else '') + (f'  [{len(warns)} warning(s)]' if warns else ''))
        for e in errs[:40]:
            print(f'      ✗ {e}')
        if len(errs) > 40:
            print(f'      … {len(errs) - 40} more')
        for w in warns[:10]:
            print(f'      ! {w}')
        total_err += len(errs)
        total_warn += len(warns)
    if not prefixes and site_tels != TEL_ALLOWED:
        missing = TEL_ALLOWED - site_tels
        extra = site_tels - TEL_ALLOWED
        print(f'ERR site-wide tel: set – missing {sorted(missing)} extra {sorted(extra)}')
        total_err += 1
    print(f'\ncheck: {len(pages)} page(s), {total_err} error(s), {total_warn} warning(s)')
    return 1 if total_err else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
