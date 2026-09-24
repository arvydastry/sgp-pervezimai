#!/usr/bin/env python3
"""SGP pervežimai v2 — static page generator (python3 stdlib only).

Usage
  python3 tools/build.py                 build every page
  python3 tools/build.py apie-imone ...  build only pages whose output path starts with a prefix
  python3 tools/build.py --kit           + the Kit API specimen → docs/kit.html (not a site page)

Sources
  src/pages/**/*.html        one page per file: front matter block + body HTML
  src/templates/paslauga.html + src/data/paslaugos.json   → 11 service pages
  src/templates/paslauga.py  (optional) render hook owned by the services team
  src/partials/*.html        shared chrome (head, header, footer, call bar, scripts, GS blocks)
  src/data/grafikas.json     schedule data for the DEMO build only (renders GS-Išvykimai / GS-Artimiausi /
                             GS-Grafikas); production edits those Global Sections by hand each month,
                             there is no shortcode and no client-side recompute
  docs/media.json            the only allowed Pexels media

One stack (plan §5.1): every page has front matter `kit: salient` and uses the Salient emulation kit
(src/partials/*.html, assets/css/theme-options.css + emul/* + sgp-custom.css, assets/js/emul.js;
placeholders in tools/kitlib.py and docs/build-notes/kit.md). The v2 legacy stack was deleted in Wave 3.

Kit specimen: src/pages/_kit.html (sources whose name starts with „_“) is NOT part of the public build.
  python3 tools/build.py --kit           also writes the specimen to docs/kit.html (open /docs/kit.html)

Placeholders
  {{root}} {{url:key}} {{nav:key}} {{partial:name|k=v}} (+ {{param:k=default}} inside) {{page:field}}
  {{grafikas:variant|k=v}} {{paslaugos:variant|k=v}} {{img:ID|opts}} {{photo:ID|w=..}} {{poster:ID|w=..}}
  {{bgimg:ID|opts}} {{bgvideo:ID|opts}} {{colbg:ID|opts}} {{videourl:ID}} {{alt:ID}} {{icon:name}}
  {{svc:field}} (service template only)

The build is deterministic: "today" for the schedule comes from grafikas.json
(render_today); files are only rewritten when their content changes.
"""
import html
import importlib.util
import json
import os
import re
import sys
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

sys.dont_write_bytecode = True  # the optional src/templates/paslauga.py hook must not leave __pycache__ in the repo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kitlib  # noqa: E402  Salient kit placeholders (pages with `kit: salient`)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
PAGES_DIR = os.path.join(SRC, 'pages')
PARTIALS_DIR = os.path.join(SRC, 'partials')
DATA_DIR = os.path.join(SRC, 'data')
TPL_DIR = os.path.join(SRC, 'templates')
MEDIA_JSON = os.path.join(ROOT, 'docs', 'media.json')
SITE_URL = 'https://arvydastry.github.io/sgp-pervezimai/'

SERVICE_BASE = 'pervezimo-paslaugos/tarptautiniai-pervezimai/'

# key → output folder ('' = site root). Services are added from paslaugos.json.
URLS = {
    'pradzia': '',
    'apie': 'apie-imone/',
    'paslaugos': 'pervezimo-paslaugos/',
    'tarptautiniai': SERVICE_BASE,
    'grafikas': 'pervezimu-grafikas/',
    'sekimas': 'siuntos-sekimas/',
    'taisykles': 'taisykles/',
    'kontaktai': 'kontaktai/',
    'privatumas': 'privatumo-politika/',
    '404': '404.html',
    'v1': 'v1/',
}

# nav key → which top-level menu item is current (children light up their parent)
NAV_PARENT = {'tarptautiniai': 'paslaugos', 'paslauga': 'paslaugos'}

PDF_URL = 'https://www.sgp-pervezimai.lt/siuntu-siuntimo-taisykles/download/sgp-sutartis-su-siunteju-pdf-3'

MG = ['sausio', 'vasario', 'kovo', 'balandžio', 'gegužės', 'birželio', 'liepos',
      'rugpjūčio', 'rugsėjo', 'spalio', 'lapkričio', 'gruodžio']
ESC = lambda s: html.escape(str(s), quote=True)


class BuildError(Exception):
    pass


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# ---------------------------------------------------------------- front matter
FM_RE = re.compile(r'\A\s*---\s*\n(.*?)\n---\s*\n', re.S)


def parse_front_matter(text, origin):
    """Returns (meta dict, body). Front matter = `key: value` lines between --- fences.
    Lists: `css: [a.css, b.css]` or `css: a.css, b.css`. Lines starting with # are comments."""
    m = FM_RE.match(text)
    if not m:
        raise BuildError(f'{origin}: missing front matter block (--- ... ---)')
    meta = {}
    for raw in m.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            raise BuildError(f'{origin}: bad front matter line: {raw!r}')
        k, v = line.split(':', 1)
        meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def as_list(v):
    if not v:
        return []
    v = v.strip()
    if v.startswith('[') and v.endswith(']'):
        v = v[1:-1]
    return [x.strip() for x in v.split(',') if x.strip()]


# ---------------------------------------------------------------- dates
def d_parse(iso):
    y, m, d = (int(x) for x in iso.split('-'))
    return date(y, m, d)


def d_full(d, upper=False):
    m = MG[d.month - 1]
    return (m[0].upper() + m[1:] if upper else m) + f' {d.day} d.'


def join_dates(ds):
    """[2026-09-28, 2026-10-15, 2026-10-28] → 'rugsėjo 28 d., spalio 15 ir 28 d.'"""
    groups = []
    for d in ds:
        if groups and groups[-1][0] == d.month:
            groups[-1][1].append(d.day)
        else:
            groups.append((d.month, [d.day]))
    out = []
    for month, days in groups:
        dd = str(days[0]) if len(days) == 1 else ', '.join(map(str, days[:-1])) + ' ir ' + str(days[-1])
        out.append(f'{MG[month - 1]} {dd} d.')
    return ', '.join(out)


# ---------------------------------------------------------------- schedule data (grafikas.json)
class Schedule:
    """Parsed grafikas.json: routes with all / upcoming / next dates at render_today.
    Rendering lives in tools/kitlib.py (KitSchedule) — the text an editor types into the Global Sections."""

    def __init__(self, data):
        self.data = data
        self.today = d_parse(data['render_today'])
        self.routes = {}
        for r in data['routes']:
            r = dict(r)
            r['all'] = sorted(d_parse(x) for x in r['dates'])
            r['up'] = [d for d in r['all'] if d >= self.today]
            r['next'] = r['up'][0] if r['up'] else None
            r['name'] = f"{r['from']} – {r['to']}"
            self.routes[r['key']] = r


# ---------------------------------------------------------------- media (docs/media.json only)
class Media:
    SRCSET = [480, 760, 1100, 1600, 1920]

    def __init__(self, data):
        self.photos = {p['id']: p for p in data['photos']}
        self.videos = {v['id']: v for v in data['videos']}

    @staticmethod
    def opts(parts):
        o = {}
        for p in parts:
            p = p.strip()
            if not p:
                continue
            if '=' in p:
                k, v = p.split('=', 1)
                o[k.strip()] = v.strip()
            else:
                o[p] = True
        return o

    def photo_url(self, pid, w):
        if pid not in self.photos:
            raise BuildError(f'media: photo {pid} is not in docs/media.json')
        return f"{self.photos[pid]['url_base']}?auto=compress&cs=tinysrgb&w={w}"

    def poster_url(self, vid, w):
        if vid not in self.videos:
            raise BuildError(f'media: video {vid} is not in docs/media.json')
        return re.sub(r'w=\d+', f'w={w}', self.videos[vid]['poster'])

    def img(self, pid, o):
        """{{img:ID|w=760|sizes=...|class=..|pos=50% 60%|eager|decorative|alt=..|id=..}}"""
        p = self.photos.get(pid)
        if not p:
            raise BuildError(f'media: photo {pid} is not in docs/media.json')
        w = int(o.get('w', 1100))
        widths = sorted({x for x in self.SRCSET if x <= max(w * 2, 480)} | {w})
        srcset = ', '.join(f'{ESC(self.photo_url(pid, x))} {x}w' for x in widths)
        h = round(w * p['height'] / p['width'])
        alt = '' if o.get('decorative') else o.get('alt', p['alt_lt'])
        attrs = [f'src="{ESC(self.photo_url(pid, w))}"', f'srcset="{srcset}"',
                 f'sizes="{ESC(o.get("sizes", "100vw"))}"', f'width="{w}"', f'height="{h}"', f'alt="{ESC(alt)}"']
        if o.get('eager'):
            attrs.append('fetchpriority="high"' if o.get('eager') == 'high' else 'loading="eager"')
        else:
            attrs.append('loading="lazy"')
        attrs.append('decoding="async"')
        if o.get('class'):
            attrs.insert(0, f'class="{ESC(o["class"])}"')
        if o.get('id'):
            attrs.insert(0, f'id="{ESC(o["id"])}"')
        style = []
        if o.get('pos'):
            style.append(f'object-position:{o["pos"]}')
        if style:
            attrs.append(f'style="{ESC(";".join(style))}"')
        for k in ('data-parallax', 'data-mask'):
            if o.get(k):
                attrs.append(f'{k}="{ESC(o[k])}"' if o[k] is not True else k)
        return '<img ' + ' '.join(attrs) + '>'

    def render(self, kind, arg):
        parts = arg.split('|')
        mid, o = parts[0].strip(), self.opts(parts[1:])
        if kind == 'img':
            return self.img(mid, o)
        if kind == 'photo':
            return ESC(self.photo_url(mid, int(o.get('w', 1920))))
        if kind == 'poster':
            return ESC(self.poster_url(mid, int(o.get('w', 1920))))
        if kind == 'alt':
            src = self.photos.get(mid) or self.videos.get(mid)
            if not src:
                raise BuildError(f'media: {mid} is not in docs/media.json')
            return ESC(src['alt_lt'])
        raise BuildError(f'unknown media placeholder {kind!r}')


# ---------------------------------------------------------------- services (paslaugos.json)
class Services:
    def __init__(self, data, media):
        self.data = data
        self.media = media
        self.list = data['services']
        self.by_slug = {s['slug']: s for s in self.list}
        for s in self.list:
            URLS[s['slug']] = SERVICE_BASE + s['slug'] + '/'



# ---------------------------------------------------------------- engine
PH_RE = re.compile(r'\{\{\s*([a-z0-9_-]+)(?::([^{}]*?))?\s*\}\}')
URLS['pdf'] = PDF_URL
NAV_ANCESTORS = {'paslauga': ['tarptautiniai', 'paslaugos'], 'tarptautiniai': ['paslaugos']}
# Salient kit stack (plan §5.1): Theme Options stand-in → emulation → the one custom layer → (page) → demo
KIT_CSS = ['theme-options.css', 'emul/base.css', 'emul/grid.css', 'emul/header.css', 'emul/typography.css',
           'emul/buttons.css', 'emul/lists-cards.css', 'emul/interactive.css', 'emul/motion.css', 'emul/plugins.css',
           'sgp-custom.css']
KIT_CSS_AFTER = ['demo.css']
KIT_JS = ['emul.js', 'demo.js']           # defer, after Lenis; sgp-custom.js loads in <head> (Custom JS (Head))
# allowed CDN libraries per page (front matter `vendor: flickity`) — jsdelivr only, pinned versions
VENDORS = {
    'flickity': ('https://cdn.jsdelivr.net/npm/flickity@2.3.0/dist/flickity.min.css',
                 'https://cdn.jsdelivr.net/npm/flickity@2.3.0/dist/flickity.pkgd.min.js'),
    'anime': (None, 'https://cdn.jsdelivr.net/npm/animejs@3.2.2/lib/anime.min.js'),
}


def file_version(path):
    import hashlib
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def parse_args(s):
    """'routes=lt-ie,ie-lt limit=3' or 'routes=lt-ie|tone=A' → dict"""
    out = {}
    for tok in re.split(r'[|\s]+', (s or '').strip()):
        if not tok:
            continue
        if '=' in tok:
            k, v = tok.split('=', 1)
            out[k] = v
        else:
            out[tok] = True
    return out


class Page:
    def __init__(self, meta, body, origin, svc=None):
        self.meta, self.body, self.origin, self.svc = meta, body, origin, svc
        out = meta.get('out', '').strip()
        if not out or out.startswith('/') or '..' in out.split('/'):
            raise BuildError(f'{origin}: front matter `out` must be a relative path like "apie-imone/index.html"')
        if out.split('/')[0] in ('v1', 'docs', 'src', 'tools', 'assets', '.git'):
            raise BuildError(f'{origin}: refusing to write into {out.split("/")[0]}/')
        self.out = out
        self.depth = out.count('/')
        self.root = './' if self.depth == 0 else '../' * self.depth
        if meta.get('root'):
            # 404.html only: GitHub Pages serves it at any depth, so links must be absolute.
            # (An absolute root is used instead of <base href>, which breaks #fragment links and SVG <use>.)
            if out != '404.html' or not meta['root'].startswith('/') or not meta['root'].endswith('/'):
                raise BuildError(f'{origin}: front matter `root` is only allowed on 404.html (e.g. root: /sgp-pervezimai/)')
            self.root = meta['root']
        for req in ('title', 'description'):
            if not meta.get(req):
                raise BuildError(f'{origin}: front matter `{req}` is required')
        self.kit = meta.get('kit', '').strip().lower() == 'salient'
        if not self.kit:
            raise BuildError(f'{origin}: front matter `kit: salient` is required (the legacy v2 stack was removed)')
        if meta.get('js'):
            raise BuildError(f'{origin}: `kit: salient` pages own no JS — remove front matter `js:` (behaviour comes from assets/js/emul.js)')


class Builder:
    def __init__(self):
        self.sched = Schedule(load_json(os.path.join(DATA_DIR, 'grafikas.json')))
        self.media = Media(load_json(MEDIA_JSON))
        self.services = Services(load_json(os.path.join(DATA_DIR, 'paslaugos.json')), self.media)
        self.partials = {fn[:-5]: read(os.path.join(PARTIALS_DIR, fn))
                         for fn in sorted(os.listdir(PARTIALS_DIR)) if fn.endswith('.html')}
        self.k_sched = kitlib.KitSchedule(self.sched, d_full, join_dates, d_parse, BuildError)
        self.k_svc = kitlib.KitServices(self.services, BuildError)
        self.k_media = kitlib.KitMedia(self.media, BuildError)
        self.hook = None
        hook_path = os.path.join(TPL_DIR, 'paslauga.py')
        if os.path.exists(hook_path):
            spec = importlib.util.spec_from_file_location('sgp_paslauga_hook', hook_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            self.hook = mod

    # -- page list
    def pages(self, kit=False):
        pages = []
        for dirpath, _, files in os.walk(PAGES_DIR):
            for fn in sorted(files):
                if not fn.endswith('.html'):
                    continue
                path = os.path.join(dirpath, fn)
                meta, body = parse_front_matter(read(path), os.path.relpath(path, ROOT))
                if fn.startswith('_'):
                    # specimen (Kit API style tile): never part of the public site; --kit writes it to docs/kit.html
                    if not kit:
                        continue
                    page = Page(meta, body, os.path.relpath(path, ROOT))
                    page.out, page.depth, page.root = 'docs/kit.html', 1, '../'
                    pages.append(page)
                    continue
                pages.append(Page(meta, body, os.path.relpath(path, ROOT)))
        tpl = os.path.join(TPL_DIR, 'paslauga.html')
        if os.path.exists(tpl):
            text = read(tpl)
            for s in self.services.list:
                ctx = self.svc_context(s)
                t = PH_RE.sub(lambda m: self.svc_field(ctx, m) if m.group(1) == 'svc' else m.group(0), text)
                meta, body = parse_front_matter(t, f'src/templates/paslauga.html [{s["slug"]}]')
                pages.append(Page(meta, body, f'src/templates/paslauga.html [{s["slug"]}]', svc=s))
        outs = {}
        for p in pages:
            if p.out in outs:
                raise BuildError(f'{p.origin} and {outs[p.out]} both write {p.out}')
            outs[p.out] = p.origin
        return sorted(pages, key=lambda p: p.out)

    # -- service template fields
    def svc_context(self, s):
        idx = self.services.list.index(s)
        nxt = self.services.by_slug.get(s.get('next')) or self.services.list[(idx + 1) % len(self.services.list)]
        ctx = {k: v for k, v in s.items()}
        ctx.update({'url': '{{url:' + s['slug'] + '}}', 'total': f'{len(self.services.list):02d}',
                    'next_slug': nxt['slug'], 'next_name': nxt['name'], 'next_no': nxt['no'],
                    'next_url': '{{url:' + nxt['slug'] + '}}',
                    'next_media': (nxt.get('hero') or {}).get('id', nxt.get('card_media', ''))})
        hero = s.get('hero') or {}
        ctx['hero_id'] = hero.get('id', s.get('card_media', ''))
        ctx['hero_crop'] = hero.get('crop', s.get('card_crop', '50% 50%'))
        ctx['hero_type'] = hero.get('type', 'photo')
        # the render hook (src/templates/paslauga.py, services team) emits every *_html block of the template
        if not (self.hook and hasattr(self.hook, 'blocks')):
            raise BuildError('src/templates/paslauga.py with blocks(svc, ctx) is required for the service template')
        extra = self.hook.blocks(s, {'esc': ESC, 'media': self.media, 'services': self.services.list,
                                     'shared': self.services.data.get('shared', {}), 'groups': self.services.data.get('groups', []),
                                     'schedule': self.sched})
        ctx.update(extra or {})
        return ctx

    def svc_field(self, ctx, m):
        key = (m.group(2) or '').strip()
        if key not in ctx:
            raise BuildError(f'service template: unknown field {{{{svc:{key}}}}} for {ctx.get("slug")}')
        v = ctx[key]
        if key.endswith('_html') or key in ('url', 'next_url'):
            return str(v)
        if isinstance(v, (list, dict)):
            raise BuildError(f'service template: {{{{svc:{key}}}}} is a list/object – use {key}_html or the hook')
        return ESC('' if v is None else v)

    # -- placeholder expansion
    def expand(self, text, page, depth=0):
        def repl(m):
            name, arg = m.group(1), (m.group(2) or '').strip()
            if name == 'root':
                return page.root
            if name == 'url':
                key = arg
                if key not in URLS:
                    raise BuildError(f'{page.origin}: unknown url key {key!r}')
                u = URLS[key]
                return u if u.startswith('http') else page.root + u
            if name == 'partial':
                return self.partial(page, arg)
            if name == 'param':
                raise BuildError(f'{page.origin}: {{{{param:{arg}}}}} outside a partial')
            if name == 'page':
                return self.page_field(page, arg)
            if name == 'nav':
                return self.nav_attr(page, arg)
            if name in ('grafikas', 'paslaugos'):
                variant, rest = re.split(r'[|\s]', arg + ' ', maxsplit=1)
                args = parse_args(rest)
                if name == 'grafikas':
                    return self.k_sched.render(variant, args)
                return self.k_svc.render(variant, args)
            if name == 'icon':
                iname, _, iopt = arg.partition('|')
                io = Media.opts(iopt.split('|'))
                try:
                    return kitlib.icon(iname.strip(), io.get('class', 'nectar-inline-icon'))
                except KeyError:
                    raise BuildError(f'{page.origin}: unknown icon {arg!r} (see tools/kitlib.py ICONS)')
            if name in ('bgimg', 'colbg', 'bgvideo', 'videourl'):
                parts = arg.split('|')
                mid, o = parts[0].strip(), Media.opts(parts[1:])
                if o.get('sd-only') or o.get('q') == 'sd':
                    raise BuildError(f'{page.origin}: SD/HD video flags were removed in the Salient kit')
                return getattr(self.k_media, name)(mid, o)
            if name in ('img', 'photo', 'poster', 'alt'):
                return self.media.render(name, arg)
            if name == 'svc':
                raise BuildError(f'{page.origin}: {{{{svc:...}}}} is only available in src/templates/paslauga.html')
            raise BuildError(f'{page.origin}: unknown placeholder {{{{{name}}}}}')
        for _ in range(8):
            new = PH_RE.sub(repl, text)
            if new == text:
                break
            text = new
        return text

    def partial(self, page, arg):
        """{{partial:name|k=v|k2=v2}} — src/partials/<name>.html; {{param:k=default}} inside."""
        name, _, rest = arg.partition('|')
        key = name.strip()
        if key not in self.partials:
            raise BuildError(f'{page.origin}: unknown partial {name!r}')
        params = parse_args(rest)
        tone = str(params.get('tone', '')).upper()
        if tone in ('A', 'P'):   # tone shortcuts: A = asphalt chapter, P = paper chapter (plan §3 „Tone“)
            derived = {'A': {'tone_text': 'light', 'tone_bg': '#0F1417', 'tone_hover': 'extra-color-2', 'tone_class': 'sgp-dark', 'tone_label': '#EF4539'},
                       'P': {'tone_text': 'dark', 'tone_bg': '#F5F7F6', 'tone_hover': 'extra-color-1', 'tone_class': '', 'tone_label': '#C4301E'}}[tone]
            for k, v in derived.items():
                params.setdefault(k, v)
        text = re.sub(r'\{\{#if:([a-z0-9_-]+)=([^{}]*?)\}\}(.*?)\{\{/if\}\}',
                      lambda m: m.group(3) if str(params.get(m.group(1), '')) == m.group(2) else '', self.partials[key], flags=re.S)

        def sub(m):
            k, _, default = m.group(1).partition('=')
            k = k.strip()
            if k in params and params[k] is not True:
                return str(params[k])
            if m.group(1).find('=') >= 0:
                return default
            raise BuildError(f'{page.origin}: partial {name!r} needs parameter {k!r}')
        return re.sub(r'\{\{\s*param:([^{}|]+?)\s*\}\}', sub, text)

    def page_field(self, page, key):
        m = page.meta
        if key == 'content':
            return page.body
        if key == 'css':
            links = []
            files = KIT_CSS + as_list(m.get('css')) + KIT_CSS_AFTER
            for f in files:
                path = os.path.join(ROOT, 'assets', 'css', f)
                if not os.path.exists(path):
                    raise BuildError(f'{page.origin}: css file assets/css/{f} does not exist')
                links.append(f'<link rel="stylesheet" href="{page.root}assets/css/{f}?v={file_version(path)}">')
            return '\n'.join(links)
        if key == 'head_js':
            path = os.path.join(ROOT, 'assets', 'js', 'sgp-custom.js')
            return f'<script src="{page.root}assets/js/sgp-custom.js?v={file_version(path)}"></script>'
        if key == 'js':
            tags = []
            for f in KIT_JS:
                path = os.path.join(ROOT, 'assets', 'js', f)
                if not os.path.exists(path):
                    raise BuildError(f'{page.origin}: js file assets/js/{f} does not exist')
                tags.append(f'<script src="{page.root}assets/js/{f}?v={file_version(path)}" defer></script>')
            return '\n'.join(tags)
        if key in ('vendor_css', 'vendor_js'):
            tags = []
            for v in as_list(m.get('vendor')):
                if v not in VENDORS:
                    raise BuildError(f'{page.origin}: unknown vendor {v!r} (allowed: {", ".join(VENDORS)})')
                css, js = VENDORS[v]
                if key == 'vendor_css' and css:
                    tags.append(f'<link rel="stylesheet" href="{css}">')
                if key == 'vendor_js' and js:
                    tags.append(f'<script src="{js}" defer></script>')
            return '\n'.join(tags)
        if key == 'canonical':
            if page.out == '404.html':
                return ''
            path = page.out[:-len('index.html')] if page.out.endswith('index.html') else page.out
            return f'<link rel="canonical" href="{SITE_URL}{path}">\n<meta property="og:url" content="{SITE_URL}{path}">'
        if key == 'base':
            return f'<base href="{ESC(m["base"])}">' if m.get('base') else ''
        if key == 'og_image':
            return ESC(self.og_image(m.get('og_image') or '29374299'))
        if key == 'preload':
            return self.preload(m.get('hero_media'), m.get('hero_phone'))
        if key == 'today':
            return self.sched.data['render_today']
        if key == 'salient':
            return f'<!-- Salient: {ESC(m["salient"])} -->' if m.get('salient') else ''
        if key in ('title', 'description', 'body_class', 'nav', 'og_title'):
            v = m.get(key) or (m.get('title', '').split(' | ')[0] if key == 'og_title' else '')
            return ESC(v)
        raise BuildError(f'{page.origin}: unknown page field {key!r}')

    def og_image(self, v):
        v = v.strip()
        if v.isdigit():
            if v in self.media.photos:
                return self.media.photo_url(v, 1200)
            return self.media.poster_url(v, 1200)
        return v

    def preload(self, hero, phone=None):
        """Hero preload. With a per-device phone image (front matter hero_phone = the {{bgvideo|bgimg:…|phone=ID}}
        crop) the two preloads are split by media query, so each device fetches only the image its <picture> uses."""
        if not hero:
            return ''
        hero = hero.strip()
        if hero in self.media.videos:
            srcset = ', '.join(f'{self.media.poster_url(hero, x)} {x}w' for x in (640, 960, 1280, 1920))
        elif hero in self.media.photos:
            # same candidates as the hero {{img:…|w=1920}} srcset (incl. 480 w), so DPR-1 phones reuse the preload
            srcset = ', '.join(f'{self.media.photo_url(hero, x)} {x}w' for x in self.media.SRCSET)
        else:
            raise BuildError(f'hero_media {hero!r} is not in docs/media.json')
        if not phone:
            return f'<link rel="preload" as="image" imagesrcset="{ESC(srcset)}" imagesizes="100vw" fetchpriority="high">'
        phone = phone.strip()
        if phone not in self.media.photos:
            raise BuildError(f'hero_phone {phone!r} is not a photo in docs/media.json')
        psrc = ', '.join(f'{self.media.photo_url(phone, x)} {x}w' for x in (480, 760, 1100))
        return (f'<link rel="preload" as="image" media="(min-width:691px)" imagesrcset="{ESC(srcset)}" imagesizes="100vw" fetchpriority="high">\n'
                f'<link rel="preload" as="image" media="(max-width:690px)" imagesrcset="{ESC(psrc)}" imagesizes="100vw" fetchpriority="high">')

    def nav_attr(self, page, key):
        cur = page.meta.get('nav', '')
        if page.svc is not None and key == page.svc['slug']:
            return ' aria-current="page"'                    # mega menu + footer link of the current service
        if cur == key:
            return ' aria-current="page"'
        if key in NAV_ANCESTORS.get(cur, []):
            return ' aria-current="true"'
        return ''

    # -- build
    def render(self, page):
        layout = self.partials.get('layout')
        if not layout:
            raise BuildError('src/partials/layout.html is missing')
        out = self.expand(layout, page)
        left = re.findall(r'\{\{[^}]*\}\}', out)
        if left:
            raise BuildError(f'{page.origin}: unresolved placeholders {sorted(set(left))[:5]}')
        return out

    def run(self, prefixes, kit=False):
        pages = self.pages(kit)
        if prefixes:
            pages = [p for p in pages if any(p.out.startswith(x) for x in prefixes) or p.out == 'docs/kit.html']
            if not pages:
                raise BuildError(f'no page output matches {prefixes}')
        written = 0
        for p in pages:
            text = self.render(p)
            dest = os.path.join(ROOT, p.out)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if os.path.exists(dest) and read(dest) == text:
                continue
            with open(dest, 'w', encoding='utf-8', newline='\n') as f:
                f.write(text)
            written += 1
            print(f'  wrote {p.out}')
        print(f'build: {len(pages)} page(s), {written} changed, {len(pages) - written} unchanged')


def main(argv):
    try:
        kit = '--kit' in argv
        Builder().run([a.strip('/').rstrip('/') if a.endswith('/') else a for a in argv if not a.startswith('--')], kit)
    except BuildError as e:
        print(f'BUILD ERROR: {e}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
