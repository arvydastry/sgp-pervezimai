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

Salient kit rules (plan §5.4; pages built with `kit: salient`, detected by <body data-kit="salient">):
  every section.vc_section / .wpb_row / .vc_row.inner_row / .nectar-global-section has data-salient (element roots
  without it are counted), no removed v2 constructs (flap, rail, ring, graticule, crop, ticket, board, switchboard
  popover, SD/HD video, relative „po N d.“ …), every tel: link has an aria-label, no <video autoplay>, background
  videos and Scrolling Text loops only with a .sgp-motion-toggle on the page, page CSS ≤ 15 lines.
Repository rules: sgp-custom.css ≤ 260 non-blank lines (plan budget 250), sgp-custom.js ≤ 40 lines (budget 30),
  no border-radius above 4px in assets/css/emul/*, sgp-custom.css, demo.css (50 % circles and lines marked
  „radius-ok“ excepted), no text under 12 px in the kit CSS.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {'.git', 'v1', 'docs', 'src', 'tools', 'assets', '.claude', 'node_modules'}
SKIP_FILES = {'salient-gidas.html'}  # standalone Lithuanian Salient guide, not a built page
SITE_BASE = '/sgp-pervezimai/'
TEL_ALLOWED = {'+37065053161', '+353864503104', '+447566878681', '+37063828919', '+34602547929'}
NEVER_USE = {'7464393', '38404178', '12421166', '19274366', '3987777', '32313192', '15885602', '35531295',
             '11479826', '7828591', '8874803', '8828587'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
OPTIONAL_END = {'p', 'li', 'dt', 'dd', 'option', 'optgroup', 'tr', 'td', 'th', 'thead', 'tbody', 'tfoot', 'colgroup', 'caption', 'rp', 'rt'}
INTERACTIVE = {'a', 'button'}
ID_REF_ATTRS = ('aria-controls', 'aria-labelledby', 'aria-describedby', 'popovertarget', 'for', 'list')
KIT_STRUCT = ('vc_section', 'wpb_row', 'inner_row', 'nectar-global-section')
KIT_ELEMENTS = {'nectar-split-heading', 'nectar-highlighted-text', 'nectar-scrolling-text', 'nectar-badge', 'nectar-cta',
                'nectar-button', 'nectar-fancy-box', 'nectar-milestone', 'toggles', 'tabbed', 'page-submenu',
                'nectar-sticky-media-sections', 'nectar-hor-list-item', 'nectar-icon-list', 'nectar-fancy-ul',
                'nectar_image_with_hotspots', 'img-with-aniamtion-wrap', 'nectar_cascading_images', 'divider-wrap',
                'nectar-video-box', 'nectar-flickity', 'nectar-content-trail', 'nectar_icon_wrap', 'nectar-responsive-text',
                'nectar-price-typography'}
BANNED_CLASS = re.compile(r'(^|[-_])(flap|rail|ring|graticule|crop|ticket|board|switchboard|callpanel|stub|lane)([-_]|$)')
BANNED_TEXT = [(re.compile(p, re.I), why) for p, why in (
    (r'\bpopover(target)?\b', 'popover (switchboard) — use GS-Telefonai'),
    (r'data-(sd|hd)=', 'SD/HD video switching'),
    (r'\bpo \d+ d\.', 'relative „po N d.“ status'),
    (r'sgp_grafikas', '[sgp_grafikas] shortcode concept'),
    (r'Raw HTML', 'Raw HTML construct'),
    (r'Inter Tight', 'Inter Tight (rejected Harbor tile)'),
    (r'\bsgp-mono\b', '.sgp-mono (labels come from the Label typography slot)'),
    (r'Fullscreen Split(?! Cover)', '„Fullscreen Split“ (18.2.1: Fullscreen Cover Split)'),
    (r'Centered Menu', 'Centered Menu header (plan: Default Layout)'),
    (r'Before Footer', '„Before Footer“ location does not exist in 18.2.1'),
    (r'Pinned[^"<]{0,40}Stacking|Stacking[^"<]{0,40}Pinned', 'Stacking is not a Pinned Sections effect'),
    (r'\(Line\)|Button \(Regular', 'legacy v2 button naming'),
    (r'Fancy Box[^"<]{0,10}minimal', 'Fancy Box has no „minimal“ style'),
    (r'\b18\.3\b', '18.3 option (owner has 18.2.1)'))]
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
        self.kit = False
        self.kit_errs, self.kit_missing_el = [], 0
        self.tel_no_label, self.videos_bg, self.videos_autoplay, self.motion_toggle, self.loops = [], 0, [], False, 0

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
        if tag == 'body' and a.get('data-kit') == 'salient':
            self.kit = True
        cls = a.get('class', '').split()
        if self.kit:
            if any(c in KIT_STRUCT for c in cls) and 'data-salient' not in a:
                self.kit_errs.append(f'line {line}: <{tag} class="{a.get("class")}"> has no data-salient')
            elif any(c in KIT_ELEMENTS for c in cls) and 'data-salient' not in a:
                self.kit_missing_el += 1
            for c in cls:
                if BANNED_CLASS.search(c) and not c.startswith(('lines-', 'nectar-')):
                    self.kit_errs.append(f'line {line}: removed v2 class "{c}"')
            if 'sgp-motion-toggle' in cls:
                self.motion_toggle = True
            if 'nectar-scrolling-text' in cls:
                self.loops += 1
            if tag == 'a' and a.get('href', '').startswith('tel:') and not a.get('aria-label'):
                self.tel_no_label.append(line)
            if tag == 'video':
                if 'autoplay' in a:
                    self.videos_autoplay.append(line)
                if any(t == 'div' for t, _ in self.stack):
                    self.videos_bg += 1
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


def count_lines(path):
    with open(path, encoding='utf-8') as f:
        return sum(1 for ln in f if ln.strip())


def repo_rules():
    """Budgets + CSS rules for the Salient kit files. Returns (errors, info lines)."""
    errs, info = [], []
    css = os.path.join(ROOT, 'assets', 'css')
    custom_css, custom_js = os.path.join(css, 'sgp-custom.css'), os.path.join(ROOT, 'assets', 'js', 'sgp-custom.js')
    if os.path.exists(custom_css):
        n = count_lines(custom_css)
        info.append(f'sgp-custom.css: {n} non-blank lines (limit 260, plan budget 250)')
        if n > 260:
            errs.append(f'sgp-custom.css has {n} non-blank lines (> 260)')
    if os.path.exists(custom_js):
        with open(custom_js, encoding='utf-8') as f:
            n = len(f.read().rstrip('\n').split('\n'))
        info.append(f'sgp-custom.js: {n} lines (limit 40, plan budget 30)')
        if n > 40:
            errs.append(f'sgp-custom.js has {n} lines (> 40)')
    files = [os.path.join(css, 'emul', f) for f in sorted(os.listdir(os.path.join(css, 'emul')))] if os.path.isdir(os.path.join(css, 'emul')) else []
    files += [custom_css, os.path.join(css, 'demo.css'), os.path.join(css, 'theme-options.css')]
    rad = re.compile(r'border-radius\s*:\s*([^;}]+)')
    small = re.compile(r'font(?:-size)?\s*:\s*(?:[^;}]*\s)?(?:[0-9]|1[01])(?:\.\d+)?px')
    for f in files:
        if not os.path.exists(f):
            continue
        rel = os.path.relpath(f, ROOT)
        with open(f, encoding='utf-8') as fh:
            for i, line in enumerate(fh, 1):
                if 'radius-ok' not in line:
                    for m in rad.finditer(line):
                        for v in re.findall(r'(\d+(?:\.\d+)?)px', m.group(1)):
                            if float(v) > 4:
                                errs.append(f'{rel}:{i}: border-radius {m.group(1).strip()[:30]} > 4px (no pills; circles use 50 %)')
                                break
                for m in small.finditer(line):
                    if 'letter-spacing' not in m.group(0):
                        errs.append(f'{rel}:{i}: text under 12px ({m.group(0)[:40]})')
    return errs, info


def find_pages(prefixes):
    pages = []
    for dirpath, dirnames, files in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == '.':
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in files:
            if fn.endswith('.html') and not (rel_dir == '.' and fn in SKIP_FILES):
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
        if p.kit:
            errs += p.kit_errs[:40]
            for m in re.finditer('|'.join(f'(?:{r.pattern})' for r, _ in BANNED_TEXT), raw, re.I):
                why = next(w for r, w in BANNED_TEXT if r.search(m.group(0)))
                errs.append(f'line {raw.count(chr(10), 0, m.start()) + 1}: banned „{m.group(0)[:40]}“ — {why}')
            for line in p.tel_no_label:
                errs.append(f'line {line}: tel: link without aria-label')
            for line in p.videos_autoplay:
                errs.append(f'line {line}: <video autoplay> — background videos are started by the theme (emul.js)')
            if (p.videos_bg or p.loops) and not p.motion_toggle:
                errs.append('background video / Scrolling Text loop without a .sgp-motion-toggle pause button on the page (WCAG 2.2.2)')
            for css in re.findall(r'assets/css/(pages/[\w.-]+\.css)', raw):
                n = count_lines(os.path.join(ROOT, 'assets', 'css', css))
                if n > 15:
                    errs.append(f'page CSS {css} has {n} non-blank lines (≤ 15 on kit pages — move needs into sgp-custom.css)')
            if p.kit_missing_el:
                warns.append(f'{p.kit_missing_el} element root(s) without data-salient (sections/rows are all tagged)')
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
    rerrs, rinfo = repo_rules()
    kit_pages = sum(1 for rel in pages if 'data-kit="salient"' in open(os.path.join(ROOT, rel), encoding='utf-8').read(20000))
    print(f'\nkit: {kit_pages} of {len(pages)} page(s) on the Salient kit')
    if kit_pages != len(pages):
        print('ERR every page must be built with `kit: salient` (the legacy v2 stack was removed in Wave 3)')
        total_err += 1
    if os.path.isdir(os.path.join(ROOT, '_kit')):
        print('ERR _kit/ exists — the Kit API specimen is not part of the public build (python3 tools/build.py --kit → docs/kit.html)')
        total_err += 1
    for line in rinfo:
        print(f'kit: {line}')
    for e in rerrs:
        print(f'ERR {e}')
    total_err += len(rerrs)
    print(f'\ncheck: {len(pages)} page(s), {total_err} error(s), {total_warn} warning(s)')
    return 1 if total_err else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
