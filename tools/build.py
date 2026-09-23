#!/usr/bin/env python3
"""SGP pervežimai v2 — static page generator (python3 stdlib only).

Usage
  python3 tools/build.py                 build every page
  python3 tools/build.py apie-imone ...  build only pages whose output path starts with a prefix

Sources
  src/pages/**/*.html        one page per file: front matter block + body HTML
  src/templates/paslauga.html + src/data/paslaugos.json   → 11 service pages
  src/templates/paslauga.py  (optional) render hook owned by the services team
  src/partials/*.html        shared chrome (head, header, footer, call bar, scripts, GS blocks)
  src/data/grafikas.json     schedule (mirrors the planned [sgp_grafikas] shortcode)
  docs/media.json            the only allowed Pexels media

Placeholders (see docs/build-notes/foundation.md for the full list)
  {{root}} {{url:key}} {{partial:name}} {{page:field}} {{grafikas:variant k=v}}
  {{paslaugos:variant}} {{img:ID|opts}} {{photo:ID|w=..}} {{poster:ID|w=..}}
  {{bgvideo:ID|opts}} {{alt:ID}} {{svc:field}} (service template only)

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
MA = ['SAUS.', 'VAS.', 'KOV.', 'BAL.', 'GEG.', 'BIRŽ.', 'LIEP.', 'RUGP.', 'RUGS.',
      'SPAL.', 'LAPKR.', 'GRUOD.']

ICON_PHONE = '<svg class="sgp-i" aria-hidden="true"><use href="#i-phone"/></svg>'
ICON_ARROW = '<svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg>'

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


def d_tile(d):
    return f'{d.day:02d} {MA[d.month - 1]}'


def d_rel(n):
    return 'šiandien' if n == 0 else 'rytoj' if n == 1 else f'po {n} d.'


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


# ---------------------------------------------------------------- schedule ([sgp_grafikas] mirror)
class Schedule:
    """Renders the markup contracts of dizaino-sistema.md §3.5 (board), §3.6 (timetable),
    §4.10 (table), §4.1 (ticker), §3.9 (stub), §4.11 (next). assets/js/sgp.js re-renders the
    same containers client-side when the visitor's date differs from render_today."""
    ORDER = ['lt-ie', 'lt-es', 'ie-lt', 'es-lt']
    ALIASES = {'ie': 'lt-ie,ie-lt', 'es': 'lt-es,es-lt', 'out': 'lt-ie,lt-es', 'in': 'ie-lt,es-lt',
               'all': 'lt-ie,lt-es,ie-lt,es-lt'}

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

    def keys(self, args):
        spec = args.get('routes') or self.ALIASES.get(args.get('kryptis', 'all'))
        if not spec:
            raise BuildError(f"grafikas: unknown kryptis={args.get('kryptis')!r}")
        keys = [k.strip() for k in spec.split(',') if k.strip()]
        for k in keys:
            if k not in self.routes:
                raise BuildError(f'grafikas: unknown route {k!r}')
        return keys

    def diff(self, d):
        return (d - self.today).days

    def soonest(self, keys):
        c = [self.routes[k] for k in keys if self.routes[k]['next']]
        return min(c, key=lambda r: (r['next'], self.ORDER.index(r['key']))) if c else None

    def aria(self, r):
        dates = join_dates(r['up']) if r['up'] else 'grafikas atnaujinamas.'
        return f"{r['name']}: {dates} Skambinti {r['tel_label']}"

    # -- variants
    def board(self, args):
        keys = self.keys(args)
        s = self.soonest(keys)
        cells = []
        for k in keys:
            r = self.routes[k]
            n = r['next']
            is_s = s is not None and r is s
            d = '<span class="sgp-dot"></span>Artimiausias' if is_s else ('Iš Lietuvos' if r['dir'] == 'out' else 'Į Lietuvą')
            flap = d_tile(n) if n else '— —'
            if n:
                bdate = f'<time datetime="{n.isoformat()}">{d_full(n, True)}</time> <span>· {d_rel(self.diff(n))}</span>'
            else:
                bdate = 'Grafikas atnaujinamas – skambinkite'
            later = r['up'][1:]
            later_html = f'\n    <p class="sgp-blater" aria-hidden="true">Vėliau: {join_dates(later)}</p>' if later else ''
            cells.append(
                f'<a class="sgp-bcell{" is-soonest" if is_s else ""}" href="tel:{r["tel"]}" aria-label="{ESC(self.aria(r))}">\n'
                f'    <p class="sgp-bcell__dir sgp-mono" aria-hidden="true">{d}</p>\n'
                f'    <p class="sgp-bcell__name" aria-hidden="true">{r["from"]} → {r["to"]} {ICON_PHONE}</p>\n'
                f'    <p class="sgp-bnext" aria-hidden="true"><span class="sgp-flap" data-flap>{flap}</span></p>\n'
                f'    <p class="sgp-bdate" aria-hidden="true">{bdate}</p>{later_html}\n'
                f'  </a>')
        return (f'<div class="sgp-board__grid" data-sched="board" data-routes="{",".join(keys)}">\n  '
                + '\n  '.join(cells) + '\n</div>')

    def tt_label(self, r, keys):
        if r['dir'] == 'in':
            return 'Iš ' + r['from_gen']
        outs = [k for k in keys if self.routes[k]['dir'] == 'out']
        return 'Į ' + r['to_acc'] if len(outs) > 1 else 'Iš Lietuvos'

    def timetable(self, args):
        keys = self.keys(args)
        rows = []
        for k in keys:
            r = self.routes[k]
            if r['up']:
                v = ''.join(f'<time datetime="{d.isoformat()}"{" class=\"is-next\"" if i == 0 else ""}>{d_full(d, True)}</time>'
                            for i, d in enumerate(r['up']))
            else:
                v = '<span>Grafikas atnaujinamas – skambinkite</span>'
            rows.append(
                f'<li><a class="sgp-tt__row" href="tel:{r["tel"]}" aria-label="{ESC(self.aria(r))}">'
                f'<span class="sgp-tt__k sgp-mono" aria-hidden="true">{self.tt_label(r, keys)}</span>'
                f'<span class="sgp-tt__v" aria-hidden="true">{v}</span>'
                f'<span class="sgp-tt__call" aria-hidden="true">{ICON_PHONE}</span></a></li>')
        return (f'<ul class="sgp-tt" data-sched="timetable" data-routes="{",".join(keys)}">\n  '
                + '\n  '.join(rows) + '\n</ul>')

    def table(self, args):
        keys = self.keys(args)
        s = self.soonest(keys)
        groups = []
        for title, direction in (('Iš Lietuvos', 'out'), ('Į Lietuvą', 'in')):
            ks = [k for k in keys if self.routes[k]['dir'] == direction]
            if not ks:
                continue
            rows = []
            for k in ks:
                r = self.routes[k]
                is_s = s is not None and r is s
                if r['up']:
                    dates = ''.join(f'<time datetime="{d.isoformat()}"{" class=\"is-next\"" if i == 0 else ""}>{d_full(d, True)}</time>'
                                    for i, d in enumerate(r['up']))
                    rel = d_rel(self.diff(r['next']))
                    st = f'<span class="sgp-dot"></span>Artimiausias · {rel}' if is_s else rel
                else:
                    dates = '<span>Grafikas atnaujinamas – skambinkite</span>'
                    st = '—'
                rows.append(
                    f'<a class="sgp-sched__row{" is-soonest" if is_s else ""}" href="tel:{r["tel"]}" aria-label="{ESC(self.aria(r))}">'
                    f'<span class="sgp-sched__name" aria-hidden="true">{r["from"]} → {r["to"]}<span class="sgp-mono sgp-flap" data-flap>{r["code"]}</span></span>'
                    f'<span class="sgp-sched__dates" aria-hidden="true">{dates}</span>'
                    f'<span class="sgp-sched__st sgp-mono" aria-hidden="true">{st}</span>'
                    f'<span class="sgp-sched__tel" aria-hidden="true">{r["tel_label"]}{ICON_PHONE}</span></a>')
            groups.append(f'<div class="sgp-sched__grp"><p class="sgp-sched__h sgp-mono">{title}</p>\n    '
                          + '\n    '.join(rows) + '\n  </div>')
        return (f'<div class="sgp-sched" data-sched="table" data-routes="{",".join(keys)}">\n  '
                + '\n  '.join(groups) + '\n</div>')

    def ticker(self, args):
        keys = self.keys(args)
        limit = int(args.get('limit', 3))
        items = sorted((self.routes[k] for k in keys if self.routes[k]['next']),
                       key=lambda r: (r['next'], self.ORDER.index(r['key'])))[:limit]
        if items:
            lis = ''.join(f'<li{" class=\"is-soon\"" if i == 0 else ""}><b>{r["from"]} → {r["to"]}</b> '
                          f'{d_full(r["next"])} · {d_rel(self.diff(r["next"]))}</li>' for i, r in enumerate(items))
        else:
            lis = '<li><b>Grafikas atnaujinamas</b> · skambinkite</li>'
        return (f'<ul class="sgp-tk__list" data-sched="ticker" data-routes="{",".join(keys)}" '
                f'data-limit="{limit}" aria-label="Artimiausi išvykimai">{lis}</ul>')

    def stub_inner(self, r):
        n = r['next']
        if n:
            date_html = f'<time datetime="{n.isoformat()}">{d_full(n, True)}</time>'
            rel = 'iš LT · ' + d_rel(self.diff(n))
        else:
            date_html, rel = 'Grafikas atnaujinamas', 'Skambinkite'
        # short label (never wraps in the 200 px stub); the direction moves to the mono meta line
        return (f'<p class="sgp-mono">Kitas išvykimas</p>'
                f'<p class="sgp-ticket__date">{date_html}</p>'
                f'<p class="sgp-ticket__rel sgp-mono">{rel}</p>'
                f'<a class="sgp-lnk" href="tel:{r["tel"]}" aria-label="Pervežimai į {r["to_acc"]} – skambinti {r["tel_label"]}">Skambinti{ICON_ARROW}</a>')

    def stub(self, args):
        k = args.get('route', 'lt-ie')
        if k not in self.routes:
            raise BuildError(f'grafikas:stub unknown route {k!r}')
        return f'<div class="sgp-ticket__stub" data-sched="stub" data-route="{k}">{self.stub_inner(self.routes[k])}</div>'

    def stubs(self, args):
        """The two ticket cards (LT ⇄ IE, LT ⇄ ES) with next-departure stubs (§3.9)."""
        ie = ('<article class="sgp-ticket" data-reveal>\n'
              '  <div class="sgp-ticket__main">\n'
              '    <p class="sgp-mono sgp-ticket__k"><span class="sgp-ticket__code">LT ⇄ IE</span>Pervežimai į Airiją</p>\n'
              f'    <a class="sgp-ticket__big" href="tel:+37065053161" aria-label="Pervežimai į Airiją – skambinti +370 650 53161">{ICON_PHONE}+370 650 53161</a>\n'
              '    <div class="sgp-ticket__more"><a href="tel:+353864503104" aria-label="Pervežimai į Airiją, Airijos numeris +353 86 450 3104"><span>IE</span>+353 86 450 3104</a>'
              '<a href="tel:+447566878681" aria-label="Pervežimai į Airiją, JK numeris +44 7566 878681"><span>UK</span>+44 7566 878681</a></div>\n'
              '  </div>\n  ' + self.stub({'route': 'lt-ie'}) + '\n</article>')
        es = ('<article class="sgp-ticket" data-reveal style="--dl:.12s">\n'
              '  <div class="sgp-ticket__main">\n'
              '    <p class="sgp-mono sgp-ticket__k"><span class="sgp-ticket__code">LT ⇄ ES</span>Pervežimai į Ispaniją</p>\n'
              f'    <a class="sgp-ticket__big" href="tel:+37063828919" aria-label="Pervežimai į Ispaniją – skambinti +370 638 28919">{ICON_PHONE}+370 638 28919</a>\n'
              '    <div class="sgp-ticket__more"><a href="tel:+34602547929" aria-label="Pervežimai į Ispaniją, Ispanijos numeris +34 602 547 929"><span>ES</span>+34 602 547 929</a></div>\n'
              '  </div>\n  ' + self.stub({'route': 'lt-es'}) + '\n</article>')
        return ie + '\n' + es

    def next_inner(self, keys):
        s = self.soonest(keys)
        if not s:
            v = 'Grafikas atnaujinamas – skambinkite'
        else:
            v = (f'<b>{s["from"]} → {s["to"]}</b> {d_full(s["next"])} '
                 f'<span class="sgp-next__rel">· {d_rel(self.diff(s["next"]))}</span>')
        return (f'<span class="sgp-next__k sgp-mono"><span class="sgp-dot"></span>Artimiausias išvykimas</span>'
                f'<span class="sgp-next__v">{v}</span>')

    def next(self, args):
        keys = self.keys(args)
        return (f'<a class="sgp-next" href="{{{{url:grafikas}}}}" data-sched="next" data-routes="{",".join(keys)}" '
                f'data-salient="[sgp_grafikas variant=&quot;next&quot;] · visible &lt;1000px only">{self.next_inner(keys)}</a>')

    def lane(self, args):
        """Lane chart (/pervezimu-grafikas/ 02 „Laiko juosta“): one lane per route on a day scale that starts
        today; rings = departures, filled red ring = soonest. Optional [sgp_grafikas variant="lane"]
        (page-owned gr- classes; label collision layout stays in assets/js/pages/grafikas.js)."""
        keys = self.keys(args)
        routes = [self.routes[k] for k in keys]
        fx = lambda x, n: str(Decimal(x).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP))  # = JS toFixed
        max_diff = max([0] + [self.diff(r['up'][-1]) for r in routes if r['up']])
        span = max(21, -(-(max_diff + 4) // 7) * 7)                     # whole weeks, ≥ 3 weeks
        X = lambda d: min(1, max(0, d / span))
        s = self.soonest(keys)
        weeks = list(range(7, span, 7))
        axis = ('<div class="gr-lane__axis sgp-mono"><span class="gr-lane__tick gr-lane__tick--0" style="--x:0">Šiandien</span>'
                + ''.join(f'<span class="gr-lane__tick" data-wk="{d}" style="--x:{fx(X(d), 4)}">po {d} d.</span>' for d in weeks)
                + '</div>')
        rows = []
        for ri, r in enumerate(routes):
            is_s = s is not None and r is s
            last = X(self.diff(r['up'][-1])) if r['up'] else 0
            wk = ''.join(f'<i class="gr-lane__wk" style="--x:{fx(X(d), 4)}"></i>' for d in weeks)
            stops = []
            for i, d in enumerate(r['up']):
                cls = (' is-next' if i == 0 else '') + (' is-soon' if is_s and i == 0 else '')
                x = X(self.diff(d))
                stops.append(f'<span class="gr-lane__stop{cls}" style="--x:{fx(x, 4)};--dl:{fx(ri * 0.12 + 0.2 + x * 1.25, 2)}s"><i class="gr-ring"></i>'
                             f'<span class="gr-lane__lbl"><span class="gr-lane__d">{d_full(d, True)}</span>'
                             f'<span class="gr-lane__r sgp-mono">{d_rel(self.diff(d))}</span></span></span>')
            empty = '' if r['up'] else '<span class="gr-lane__empty">Grafikas atnaujinamas – skambinkite</span>'
            rows.append(f'<div class="gr-lane__row{" is-soonest" if is_s else ""}" style="--r:{ri}">'
                        f'<p class="gr-lane__name">{ESC(r["from"])} → {ESC(r["to"])}<span class="sgp-mono">{ESC(r["code"])}</span></p>'
                        f'<div class="gr-lane__track">{wk}<i class="gr-lane__base"></i><i class="gr-lane__line" style="--end:{fx(last, 4)}"></i>'
                        f'<i class="gr-lane__origin"></i>{"".join(stops)}{empty}</div></div>')
        return (f'<figure class="gr-lane" data-sched="lane" data-routes="{",".join(keys)}" aria-hidden="true" '
                f'data-salient="[sgp_grafikas variant=&quot;lane&quot;] (optional) · .gr-lane: route lanes × day scale; rings = departures; red filled ring = soonest">'
                + axis + '<div class="gr-lane__rows">' + ''.join(rows) + '</div></figure>')

    def updated(self, args):
        d = d_parse(self.data['updated'])
        return f'Atnaujinta <time datetime="{d.isoformat()}">{d_full(d)}</time>'

    def note(self, args):
        return ESC(self.data['note'])

    def json(self, args):
        pub = {'render_today': self.data['render_today'], 'updated': self.data['updated'],
               'note': self.data['note'],
               'routes': [{k: r[k] for k in ('key', 'from', 'to', 'from_gen', 'to_acc', 'code', 'dir',
                                             'tel', 'tel_label', 'dates')} for r in self.data['routes']]}
        return json.dumps(pub, ensure_ascii=False, separators=(',', ':'))

    def render(self, variant, args):
        variant = {'tickets': 'stubs', 'data': 'json'}.get(variant, variant)
        fn = getattr(self, variant, None)
        if variant.startswith('_') or not callable(fn) or variant in ('render', 'keys', 'diff', 'soonest', 'aria', 'tt_label', 'stub_inner', 'next_inner'):
            raise BuildError(f'unknown grafikas variant {variant!r}')
        return fn(args)


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

    def bgvideo(self, vid, o):
        """Poster <img> (srcset, LCP-friendly, phones see only this) + lazy <video> (desktop, sgp.js)."""
        v = self.videos.get(vid)
        if not v:
            raise BuildError(f'media: video {vid} is not in docs/media.json')
        pos = o.get('pos', '50% 50%')
        srcset = ', '.join(f'{ESC(self.poster_url(vid, x))} {x}w' for x in (640, 960, 1280, 1920))
        load = 'fetchpriority="high"' if o.get('eager') else 'loading="lazy"'
        vid_id = f' id="{ESC(o["id"])}"' if o.get('id') else ''
        hd = v['sd'] if o.get('sd-only') else v['hd']
        return (f'<img class="sgp-bgvideo__poster" src="{ESC(self.poster_url(vid, 1280))}" srcset="{srcset}" sizes="100vw" '
                f'width="{v["width"]}" height="{v["height"]}" alt="" {load} decoding="async" style="object-position:{ESC(pos)}">'
                f'<video class="sgp-bgvideo__v"{vid_id} data-bgvideo muted playsinline loop preload="none" '
                f'data-hd="{ESC(hd)}" data-sd="{ESC(v["sd"])}" aria-hidden="true" tabindex="-1" style="object-position:{ESC(pos)}"></video>')

    def render(self, kind, arg):
        parts = arg.split('|')
        mid, o = parts[0].strip(), self.opts(parts[1:])
        if kind == 'img':
            return self.img(mid, o)
        if kind == 'photo':
            return ESC(self.photo_url(mid, int(o.get('w', 1920))))
        if kind == 'poster':
            return ESC(self.poster_url(mid, int(o.get('w', 1920))))
        if kind == 'bgvideo':
            return self.bgvideo(mid, o)
        if kind == 'alt':
            src = self.photos.get(mid) or self.videos.get(mid)
            if not src:
                raise BuildError(f'media: {mid} is not in docs/media.json')
            return ESC(src['alt_lt'])
        if kind == 'videourl':
            v = self.videos.get(mid)
            if not v:
                raise BuildError(f'media: video {mid} is not in docs/media.json')
            return ESC(v[o.get('q', 'sd')])
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

    def cards(self, args):
        """Home services road (§4.7): 11 cards hanging from the lane + end card is page markup."""
        n = len(self.list)
        out = []
        for s in self.list:
            hv = ''
            video = ''
            if s.get('hover_video'):
                hv = f' data-hover-video="{self.media.render("videourl", s["hover_video"] + "|q=sd")}"'
                video = '<video muted loop playsinline preload="none" aria-hidden="true" tabindex="-1"></video>'
            img = self.media.img(s['card_media'], {'w': '760', 'sizes': '(min-width:1000px) 360px, 96px',
                                                   'pos': s.get('card_crop', '50% 50%')})
            chips = ''.join(f'<li>{ESC(c)}</li>' for c in s.get('chips', []))
            out.append(
                f'<article class="sgp-svc" data-stop{hv}><span class="sgp-ring"></span><span class="sgp-svc__stem"></span>\n'
                f'  <a class="sgp-svc__a" href="{{{{url:{s["slug"]}}}}}"><figure class="sgp-svc__img sgp-grade">{img}<i class="sgp-ov"></i>{video}</figure>\n'
                f'  <div class="sgp-svc__body"><p class="sgp-svc__no sgp-mono">{s["no"]} <span>/ {n:02d}</span></p>'
                f'<h3 class="sgp-svc__t">{ESC(s["name"])}</h3><p class="sgp-svc__s">{ESC(s.get("card", ""))}</p>\n'
                f'  <div class="sgp-svc__f"><ul class="sgp-chips">{chips}</ul><span class="sgp-svc__go">{ICON_ARROW}</span></div></div></a></article>')
        return '\n'.join(out)

    def footer(self, args):
        return ''.join(f'<a href="{{{{url:{s["slug"]}}}}}"{{{{nav:{s["slug"]}}}}}>{ESC(s["name"])}</a>' for s in self.list)

    def list_(self, args):
        """GS-ServiceList: compact line list of the 11 services."""
        items = ''.join(
            f'<li><a href="{{{{url:{s["slug"]}}}}}"><span class="sgp-mono">{s["no"]}</span>'
            f'<span class="sgp-slist__t">{ESC(s["name"])}</span>{ICON_ARROW}</a></li>' for s in self.list)
        return f'<ol class="sgp-slist" data-salient="Global Section GS-ServiceList · Horizontal List Item ×11 (Border Animation)">{items}</ol>'

    def options(self, args):
        return ''.join(f'<option>{ESC(s["name"])}</option>' for s in self.list) + '<option>Kita</option>'

    def mega(self, args):
        cols = []
        for g in self.data['groups']:
            links = ''.join(f'<li><a href="{{{{url:{sl}}}}}"{{{{nav:{sl}}}}}>{ESC(self.by_slug[sl]["name"])}</a></li>' for sl in g['services'])
            cols.append(f'<div class="sgp-mega__grp"><p class="sgp-mono">{ESC(g["name"])}</p><ul>{links}</ul></div>')
        return ''.join(cols)

    @staticmethod
    def count_lt(n):
        """1 paslauga · 2–9 paslaugos · 10–20 paslaugų (Lithuanian plural)."""
        if n % 10 == 1 and n % 100 != 11:
            return f'{n} paslauga'
        if 2 <= n % 10 <= 9 and not 12 <= n % 100 <= 19:
            return f'{n} paslaugos'
        return f'{n} paslaugų'

    def group_index(self, args):
        """/pervezimo-paslaugos/ sticky group index (links to the stacked group cards, §6.3)."""
        lis = []
        for i, g in enumerate(self.data['groups']):
            on = i == 0
            lis.append(f'<li{" class=\"is-active\"" if on else ""}><a href="#{g["key"]}"{" aria-current=\"true\"" if on else ""}>'
                       f'<span class="sgp-ring"></span><span class="ps-idx__no sgp-mono">{i + 1:02d}</span>'
                       f'<span class="ps-idx__t">{ESC(g["name"])}</span><span class="ps-idx__n sgp-mono">{len(g["services"])}</span></a></li>')
        return '<ol class="ps-idx__list">\n          ' + '\n          '.join(lis) + '\n        </ol>'

    def groups(self, args):
        """/pervezimo-paslaugos/ stacked group cards (§4.8, §6.3): group image + one swap layer per service
        (card_media, or the hero photo when the card image equals the group image) + SD hover video layer."""
        total, gl = len(self.list), len(self.data['groups'])
        out = []
        for gi, g in enumerate(self.data['groups']):
            svcs = [self.by_slug[sl] for sl in g['services']]
            layers = [f'<div class="ps-grp__layer is-on" data-for="">{{{{img:{g["media"]}|w=1100|sizes=(min-width:1000px) 30vw, 92vw}}}}</div>']
            rows = []
            for s in svcs:
                mid, crop = s['card_media'], s.get('card_crop', '50% 50%')
                if mid == g['media'] and s.get('hero'):
                    mid, crop = s['hero'].get('id', mid), s['hero'].get('crop', crop)
                video = (f'<video muted loop playsinline preload="none" aria-hidden="true" tabindex="-1" '
                         f'data-src="{{{{videourl:{s["hover_video"]}|q=sd}}}}"></video>') if s.get('hover_video') else ''
                layers.append(f'<div class="ps-grp__layer" data-for="{s["slug"]}" aria-hidden="true">'
                              f'{{{{img:{mid}|w=1100|sizes=(min-width:1000px) 30vw, 100vw|decorative|pos={crop}}}}}{video}</div>')
                chips = ''.join(f'<span>{ESC(c)}</span>' for c in s.get('chips', []))
                rows.append(f'<li><a class="ps-row" href="{{{{url:{s["slug"]}}}}}" data-for="{s["slug"]}" data-cap="{s["no"]} / {total:02d}">'
                            f'<span class="ps-row__no sgp-mono">{s["no"]}</span><div class="ps-row__txt"><h4 class="ps-row__t">{ESC(s["name"])}</h4>'
                            f'<p class="ps-row__s">{ESC(s.get("card", ""))}</p><p class="ps-row__c sgp-mono">{chips}</p></div>'
                            f'<span class="ps-row__go">{ICON_ARROW}</span></a></li>')
            lead = f'\n              <p class="ps-grp__lead">{ESC(g["lead"])}</p>' if g.get('lead') else ''
            out.append(
                f'<article class="sgp-stack__item" id="{g["key"]}" aria-labelledby="grp-{g["key"]}">\n'
                f'          <div class="ps-grp" data-salient="Sticky Scroll Pinned Sections → child section „{ESC(g["name"])}“ · Inner Row: Image 5/12 (4:5, overlay; '
                f'row-hover image swap + hover video = custom JS) + Column 7/12: Text Block + Horizontal List Item ×{len(svcs)} (Border Animation, full-row link)">\n'
                f'            <div class="ps-grp__media sgp-grade">\n            ' + '\n            '.join(layers) + '\n'
                f'            <i class="sgp-ov"></i><p class="ps-grp__cap sgp-mono" aria-hidden="true" data-ps-cap></p>\n'
                f'            </div>\n'
                f'            <div class="ps-grp__body">\n'
                f'              <p class="ps-grp__no sgp-mono"><span>{gi + 1:02d}</span> / {gl:02d}</p>\n'
                f'              <h3 class="ps-grp__t" id="grp-{g["key"]}">{ESC(g["name"])}</h3>\n'
                f'              <p class="ps-grp__n sgp-mono">{self.count_lt(len(svcs))}</p>{lead}\n'
                f'              <ul class="ps-rows">\n              ' + '\n              '.join(rows) + '\n'
                f'              </ul>\n'
                f'            </div>\n'
                f'          </div>\n'
                f'        </article>')
        return '\n        '.join(out)

    def render(self, variant, args):
        fn = {'cards': self.cards, 'footer': self.footer, 'list': self.list_,
              'options': self.options, 'mega': self.mega,
              'groups': self.groups, 'group-index': self.group_index}.get(variant)
        if not fn:
            raise BuildError(f'unknown paslaugos variant {variant!r}')
        return fn(args)


# ---------------------------------------------------------------- engine
PH_RE = re.compile(r'\{\{\s*([a-z0-9_-]+)(?::([^{}]*?))?\s*\}\}')
URLS['pdf'] = PDF_URL
NAV_ANCESTORS = {'paslauga': ['tarptautiniai', 'paslaugos'], 'tarptautiniai': ['paslaugos']}
SHARED_CSS = ['tokens.css', 'base.css', 'components.css', 'motion.css']
# allowed CDN libraries per page (front matter `vendor: flickity`) — jsdelivr only, pinned versions
VENDORS = {
    'flickity': ('https://cdn.jsdelivr.net/npm/flickity@2.3.0/dist/flickity.min.css',
                 'https://cdn.jsdelivr.net/npm/flickity@2.3.0/dist/flickity.pkgd.min.js'),
    'anime': (None, 'https://cdn.jsdelivr.net/npm/animejs@3.2.2/lib/anime.min.js'),
}
SHARED_JS = ['sgp.js']


def file_version(path):
    import hashlib
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def parse_args(s):
    """'routes=lt-ie,ie-lt limit=3' → dict"""
    out = {}
    for tok in (s or '').split():
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


class Builder:
    def __init__(self):
        self.sched = Schedule(load_json(os.path.join(DATA_DIR, 'grafikas.json')))
        self.media = Media(load_json(MEDIA_JSON))
        self.services = Services(load_json(os.path.join(DATA_DIR, 'paslaugos.json')), self.media)
        self.partials = {}
        for fn in sorted(os.listdir(PARTIALS_DIR)):
            if fn.endswith('.html'):
                self.partials[fn[:-5]] = read(os.path.join(PARTIALS_DIR, fn))
        self.hook = None
        hook_path = os.path.join(TPL_DIR, 'paslauga.py')
        if os.path.exists(hook_path):
            spec = importlib.util.spec_from_file_location('sgp_paslauga_hook', hook_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            self.hook = mod

    # -- page list
    def pages(self):
        pages = []
        for dirpath, _, files in os.walk(PAGES_DIR):
            for fn in sorted(files):
                if not fn.endswith('.html'):
                    continue
                path = os.path.join(dirpath, fn)
                meta, body = parse_front_matter(read(path), os.path.relpath(path, ROOT))
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
        # default renderings for list fields (the hook may override any of them)
        ctx['chips_html'] = ''.join(f'<li>{ESC(c)}</li>' for c in s.get('chips', []))
        ctx['kv_html'] = ''.join(f'<dt>{ESC(r["k"])}</dt><dd>{ESC(r["v"])}</dd>' for r in s.get('kv', []))
        ctx['intro_html'] = ''.join(f'<p>{ESC(p)}</p>' for p in s.get('intro', []) if isinstance(p, str))
        ctx['routes_html'] = ''.join(
            f'<li><a class="sgp-chip" href="?domina={ESC(s["name"])}#uzklausa">{ESC(r)}</a></li>' for r in s.get('routes', []))
        if self.hook and hasattr(self.hook, 'blocks'):
            extra = self.hook.blocks(s, {'esc': ESC, 'media': self.media, 'services': self.services.list,
                                         'shared': self.services.data.get('shared', {}), 'groups': self.services.data.get('groups', []),
                                         'schedule': self.sched, 'icon_phone': ICON_PHONE, 'icon_arrow': ICON_ARROW})
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
                if arg not in self.partials:
                    raise BuildError(f'{page.origin}: unknown partial {arg!r}')
                return self.partials[arg]
            if name == 'page':
                return self.page_field(page, arg)
            if name == 'nav':
                return self.nav_attr(page, arg)
            if name == 'grafikas':
                variant, _, rest = arg.partition(' ')
                return self.sched.render(variant.strip(), parse_args(rest))
            if name == 'paslaugos':
                variant, _, rest = arg.partition(' ')
                return self.services.render(variant.strip(), parse_args(rest))
            if name in ('img', 'photo', 'poster', 'bgvideo', 'alt', 'videourl'):
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

    def page_field(self, page, key):
        m = page.meta
        if key == 'content':
            return page.body
        if key == 'arrival':
            return '' if m.get('arrival', 'yes').lower() in ('no', 'false', '0') else '{{partial:arrival}}'
        if key == 'css':
            links = []
            for f in SHARED_CSS + as_list(m.get('css')):
                path = os.path.join(ROOT, 'assets', 'css', f)
                if not os.path.exists(path):
                    raise BuildError(f'{page.origin}: css file assets/css/{f} does not exist')
                links.append(f'<link rel="stylesheet" href="{page.root}assets/css/{f}?v={file_version(path)}">')
            return '\n'.join(links)
        if key == 'js':
            tags = []
            for f in SHARED_JS + as_list(m.get('js')):
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
            return self.preload(m.get('hero_media'))
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

    def preload(self, hero):
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
        return f'<link rel="preload" as="image" imagesrcset="{ESC(srcset)}" imagesizes="100vw" fetchpriority="high">'

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

    def run(self, prefixes):
        pages = self.pages()
        if prefixes:
            pages = [p for p in pages if any(p.out.startswith(x) for x in prefixes)]
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
        Builder().run([a.strip('/').rstrip('/') if a.endswith('/') else a for a in argv])
    except BuildError as e:
        print(f'BUILD ERROR: {e}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
