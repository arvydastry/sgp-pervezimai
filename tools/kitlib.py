"""SGP v2 — Salient kit placeholders for pages with front matter `kit: salient` (imported by tools/build.py).

Everything here renders NATIVE Salient element markup (Kit API, docs/build-notes/kit.md):
  {{grafikas:ticker|next|rows|updated|note}}   schedule as typed into the Global Sections (full dates, no relative words)
  {{paslaugos:menu|rows|hscroll|pinned|related|footer|options}}
  {{bgimg:ID|…}} {{bgvideo:ID|…}} {{colbg:ID|…}} {{videourl:ID}} {{icon:name}}
(The v2 legacy variants were deleted in Wave 3.)
"""
import html

ESC = lambda s: html.escape(str(s), quote=True)

# ---------------------------------------------------------------- own line icons (24 × 24, stroke = currentColor)
ICONS = {
    'phone': 'M5.5 3.5h3l1.6 4.2-2.1 1.5a11.5 11.5 0 0 0 6.8 6.8l1.5-2.1 4.2 1.6v3a2 2 0 0 1-2 2A16.5 16.5 0 0 1 3.5 5.5a2 2 0 0 1 2-2z',
    'arrow': 'M4 12h15.5M13.5 6l6 6-6 6',
    'arrow-up-right': 'M7 17 17 7M9 7h8v8',
    'arrow-down': 'M12 4v15.5M6 13.5l6 6 6-6',
    'arrow-up': 'M12 20V4.5M6 10.5l6-6 6 6',
    'download': 'M12 3.5v12M7 10.5l5 5 5-5M4.5 20h15',
    'play': 'M8 5.5l11 6.5-11 6.5z',
    'pause': 'M9 5.5v13M15 5.5v13',
    'times': 'M6 6l12 12M18 6 6 18',
    'dash': 'M5 12h14',
    'mail': 'M3.5 6h17v12h-17zM3.5 7l8.5 6 8.5-6',
    'calendar': 'M4 6h16v14H4zM4 10.5h16M8.5 3.5v5M15.5 3.5v5',
    'seat': 'M6.5 3.5l3 11h8.5M16 14.5l1.5 6M9.5 14.5l-1.5 6M4 20.5h16M9 9.5h3.5',
    'heat': 'M8 3.5c-1.2 1.3 1.2 2.4 0 3.8M12 3.5c-1.2 1.3 1.2 2.4 0 3.8M16 3.5c-1.2 1.3 1.2 2.4 0 3.8M4.5 11h15v3a5.5 5.5 0 0 1-5.5 5.5h-4A5.5 5.5 0 0 1 4.5 14z',
    'air': 'M12 3v18M4.2 7.5l15.6 9M19.8 7.5l-15.6 9M9.3 4.3 12 6.8l2.7-2.5M9.3 19.7 12 17.2l2.7 2.5',
    'shield': 'M12 3l7.5 3v5.2c0 4.8-3.1 8.4-7.5 9.8-4.4-1.4-7.5-5-7.5-9.8V6zM8.8 12.2l2.2 2.2 4.3-4.4',
    'rest': 'M12 7.5V12l3 2M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z',
    'box': 'M3.5 7.5 12 3.5l8.5 4v9L12 20.5l-8.5-4zM3.5 7.5 12 11.5l8.5-4M12 11.5v9',
    'route': 'M6 20.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5zM18 8.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5zM8.5 18h6a3.5 3.5 0 0 0 0-7h-5a3.5 3.5 0 0 1 0-7h6',
    'paw': 'M12 20.5c-3.5 0-5.5-1.7-5.5-3.7 0-2.3 2.6-5.3 5.5-5.3s5.5 3 5.5 5.3c0 2-2 3.7-5.5 3.7zM6 10.5a1.8 2.3 0 1 0 0-.1M18 10.5a1.8 2.3 0 1 0 0-.1M9.3 6.5a1.8 2.3 0 1 0 0-.1M14.7 6.5a1.8 2.3 0 1 0 0-.1',
    'heart': 'M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.3 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z',
    'cage': 'M4.5 20.5V9a7.5 5 0 0 1 15 0v11.5zM4.5 20.5h15M8.5 6v14.5M12 5v15.5M15.5 6v14.5',
    'search': 'M10.5 17.5a7 7 0 1 0 0-14 7 7 0 0 0 0 14zM15.5 15.5l5 5',
    'pin': 'M12 21s-6.5-6.2-6.5-11a6.5 6.5 0 0 1 13 0c0 4.8-6.5 11-6.5 11zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
    'tag': 'M3.5 3.5h8l9 9-8 8-9-9zM8.5 7a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z',
    'truck': 'M2.5 6.5h11v9h-11zM13.5 9.5h4l3 3v3h-7zM6.5 18.5a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM17 18.5a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
    'check': 'M5 12.5l4.5 4.5L19 7.5',
    'menu': 'M3.5 8h17M3.5 16h17',
    'close': 'M5.5 5.5l13 13M18.5 5.5l-13 13',
}


def icon(name, cls='nectar-inline-icon'):
    if name not in ICONS:
        raise KeyError(name)
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'<path d="{ICONS[name]}"/></svg>')


def wave_link(url_ph, label, nav='', extra='', salient='Button → Type: Text Reveal Wave · Display: Block'):
    """Salient Button → Text Reveal Wave used as a link-list item (mega menu, footer, card lists)."""
    return (f'<a class="nectar-cta" data-style="text-reveal-wave" data-display="block" href="{url_ph}"{nav}{extra} '
            f'data-salient="{ESC(salient)}"><span class="link_text"><span class="text">{ESC(label)}</span></span></a>')


# ---------------------------------------------------------------- schedule (the four hand-typed Global Sections)
class KitSchedule:
    """Renders what an editor types monthly into GS-Išvykimai / GS-Artimiausi / GS-Grafikas Airija / Ispanija.
    Dates are the snapshot at render_today (build-time), written in full („spalio 9 d.“) — no relative words, no JS."""
    ORDER = ['lt-ie', 'lt-es', 'ie-lt', 'es-lt']
    DIRS = {'ie': ('lt-ie', 'ie-lt'), 'es': ('lt-es', 'es-lt')}

    def __init__(self, sched, d_full, join_dates, d_parse, error):
        # dates keep their „d.“ on the number's line (no-break space): „rugsėjo 28\u00a0d.“
        nb = lambda t: t.replace(' d.', '\u00a0d.')
        self.s, self.d_full, self.join, self.d_parse, self.Err = sched, (lambda d: nb(d_full(d))), (lambda ds: nb(join_dates(ds))), d_parse, error

    def route(self, key):
        if key not in self.s.routes:
            raise self.Err(f'grafikas: unknown route {key!r} (lt-ie, lt-es, ie-lt, es-lt)')
        return self.s.routes[key]

    def ticker(self, a):
        sep = ' <span style="color:#EF4539">✦</span> '
        parts = []
        for k in self.ORDER:
            r = self.route(k)
            when = self.d_full(r['next']) if r['next'] else 'grafikas atnaujinamas'
            parts.append(f'{r["from"]} → {r["to"]}: {when}')
        return sep.join(parts) + sep + 'Visas grafikas →'

    def next(self, a):
        key = a.get('route')
        if not key:
            dr = a.get('dir', 'ie')
            if dr not in self.DIRS:
                raise self.Err(f'grafikas:next dir={dr!r} (ie | es)')
            key = self.DIRS[dr][1 if a.get('back') else 0]
        r = self.route(key)
        return self.d_full(r['next']) if r['next'] else 'grafikas atnaujinamas'

    def rows(self, a):
        keys = [k for k in (a.get('routes') or 'lt-ie,ie-lt').split(',') if k]
        dark = a.get('tone', 'P').upper() == 'A'
        color, cname, bc = ('white', 'White', '#3E464A') if dark else ('extra-color-1', 'Extra Color 1', '#C3CBCB')
        out = []
        for k in keys:
            r = self.route(k)
            dates = self.join(r['up']) if r['up'] else 'grafikas atnaujinamas – skambinkite'
            label = f'{r["from"]} → {r["to"]} {dates} {r["tel_label"]} – skambinti'
            out.append(
                f'<div class="nectar-hor-list-item" data-columns="3" data-column-layout="25-50-25" data-hover-effect="default" '
                f'data-color="{color}" data-border-animation data-border-color="{bc}" data-font-family="h4" '
                f'data-salient="Horizontal List Item → Columns: 3 · Column Layout: 25% | 50% | 25% (stacked below 1000 px) · Style: Bottom Border, Color Hover Effect · '
                f'Hover Color: {cname} · Full Item Link URL: tel:{r["tel"]} · Border Animation ✓ · Border Color {bc}">'
                f'<div class="nectar-list-item"><p>{ESC(r["from"])} → {ESC(r["to"])}</p></div>'
                f'<div class="nectar-list-item"><p class="sgp-num">{ESC(dates)}</p></div>'
                f'<div class="nectar-list-item" data-text-align="right"><p class="sgp-num">{ESC(r["tel_label"])}</p></div>'
                f'<a class="full-link" href="tel:{r["tel"]}" aria-label="{ESC(label)}"></a></div>')
        return '\n'.join(out)

    def updated(self, a):
        return f'Atnaujinta {self.d_full(self.d_parse(self.s.data["updated"]))}'

    def note(self, a):
        return ESC(self.s.data['note'])

    def render(self, variant, a):
        fn = {'ticker': self.ticker, 'next': self.next, 'rows': self.rows, 'updated': self.updated, 'note': self.note}.get(variant)
        if not fn:
            raise self.Err(f'grafikas:{variant} is not part of the Salient kit (use ticker | next | rows | updated | note)')
        return fn(a)


# ---------------------------------------------------------------- services (paslaugos.json)
FOOTER_SLUGS = ['keleiviu-pervezimas', 'siuntu-pervezimas', 'automobiliu-pervezimas', 'kroviniu-pervezimas',
                'gyvunu-pervezimas', 'perkraustymo-paslaugos']


class KitServices:
    def __init__(self, services, error):
        self.s, self.Err = services, error
        self.groups = services.data['groups']

    def svc(self, slug):
        if slug not in self.s.by_slug:
            raise self.Err(f'paslaugos: unknown service {slug!r}')
        return self.s.by_slug[slug]

    def lead(self, g):
        return g.get('lead') or self.svc(g['services'][0]).get('card', '')

    def menu(self, a):
        """GS-Paslaugų meniu: 3 Columns × 2 groups — Label (Minimal Line) + Link list (Text Reveal Wave)."""
        cols = []
        for i in range(0, len(self.groups), 2):
            parts = []
            for j, g in enumerate(self.groups[i:i + 2]):
                mt = ' style="--mt:30px"' if j else ''
                parts.append(f'<span class="nectar-badge" data-badge-style="line"{mt} data-salient="Badge → Badge Style: Minimal Line · Inherit Typography From: Label">{ESC(g["name"])}</span>')
                parts += [wave_link(f'{{{{url:{sl}}}}}', self.svc(sl)['name'], f'{{{{nav:{sl}}}}}') for sl in g['services']]
            cols.append('<div class="wpb_column vc_col-sm-3" data-el-space="10px" data-salient="Column → Column Element Spacing: 10px">'
                        '<div class="vc_column-inner">' + ''.join(parts) + '</div></div>')
        return '\n'.join(cols)

    def rows(self, a):
        """GS-Paslaugos: Link rows ×11 — Horizontal List Item 20 | 80, Color Hover Effect, Full Item Link."""
        tone = a.get('tone', 'P').upper()
        color, cname, bc = ('white', 'White', '#3E464A') if tone == 'A' else ('extra-color-1', 'Extra Color 1', '#C3CBCB')
        out = []
        for s in self.s.list:
            out.append(
                f'<div class="nectar-hor-list-item" data-columns="2" data-column-layout="20-80" data-hover-effect="default" data-color="{color}" '
                f'data-border-animation data-border-color="{bc}" data-font-family="h4" data-salient="Horizontal List Item → Columns: 2 · Column Layout: 20% | 80% · '
                f'Style: Bottom Border, Color Hover Effect · Hover Color: {cname} · Full Item Link URL · last column ends with a typed arrow · Border Animation ✓ · Border Color {bc}">'
                f'<div class="nectar-list-item"><p class="muted sgp-num">{s["no"]}</p></div>'
                f'<div class="nectar-list-item"><p>{ESC(s["name"])} <span aria-hidden="true">→</span></p></div>'
                f'<a class="full-link" href="{{{{url:{s["slug"]}}}}}" aria-label="{ESC(s["name"])}"></a></div>')
        return '\n'.join(out)

    def hscroll(self, a):
        """Home H3: 6 × Sticky Content Section (Color #161D21) for Sticky Content Sections → Horizontal Scrolling."""
        out = []
        for i, g in enumerate(self.groups):
            names = ''.join(f'<li>{ESC(self.svc(sl)["name"])}</li>' for sl in g['services'])
            out.append(
                f'<div class="nectar-sticky-media-section" data-section-type="color" style="--bg:#161D21" data-text-color="light" '
                f'data-indicator-text="Plačiau" data-salient="Sticky Content Section → Section Type: Color #161D21 · Link: /pervezimo-paslaugos/#{g["key"]} · '
                f'Link Mouse Indicator: „Plačiau“ (BG Accent, text #0F1417)">'
                f'<div class="nectar-sticky-media-section__inner"><div class="vc_row inner_row" style="--pt:28px;--pb:28px;--pl:28px;--pr:28px" data-salient="Inner Row → Padding 28px">'
                f'<div class="row_col_wrap_12_inner"><div class="wpb_column vc_col-sm-12" data-layout="flex" style="--gap:18px" '
                f'data-salient="Inner Column → Layout: Flexbox · Vertical · Gap 18px · Padding 28px"><div class="vc_column-inner">'
                f'<div class="img-with-aniamtion-wrap" data-aspect="16-10" data-hover-animation="zoom-in" data-salient="Image → Aspect 16:10 · Fit to Container · Hover Animation: Zoom In">'
                f'<div class="hover-wrap">{{{{img:{g["media"]}|w=1100|sizes=(min-width:1000px) 45vw, 92vw|decorative}}}}</div></div>'
                f'<p class="nectar-responsive-text" data-inherit="h1" style="--fs:64px;--fs-m:48px;--fg:#EF4539;--lh:1;--mt:10px" aria-hidden="true" '
                f'data-salient="Responsive Text → Font Style: H1 · Custom Font Size 64px (phone 48px) · Color #EF4539">{i + 1:02d}</p>'
                f'<h3>{ESC(g["name"])}</h3>'
                f'<p class="nectar-responsive-text" style="--fg:var(--tone-muted);--max-w:46ch" data-salient="Responsive Text → Intro">{ESC(self.lead(g))}</p>'
                f'<ul class="nectar-fancy-ul" data-list-icon="dash" data-spacing="5px" style="--icon-color:#9AA6AB" data-salient="Fancy Unordered List → Icon: Standard Dash · Color #9AA6AB">{names}</ul>'
                f'</div></div></div></div>'
                f'</div>'
                f'<a class="nsms-link" href="{{{{url:paslaugos}}}}#{g["key"]}" aria-label="{ESC(g["name"])} – plačiau"></a></div>')
        return '\n'.join(out)

    def pinned(self, a):
        """/pervezimo-paslaugos/ P3: 6 × Sticky Content Section (Color alternating #161D21 / #EAEEED), group id = anchor."""
        out = []
        for i, g in enumerate(self.groups):
            dark = i % 2 == 0
            bg, tc, color, cname = ('#161D21', 'light', 'white', 'White') if dark else ('#EAEEED', 'dark', 'extra-color-1', 'Extra Color 1')
            rows = ''.join(
                f'<div class="nectar-hor-list-item" data-columns="2" data-column-layout="20-80" data-hover-effect="default" data-color="{color}" data-font-family="h4" '
                f'data-salient="Horizontal List Item → 20% | 80% · Bottom Border, Color Hover Effect · Hover Color: {cname} · Full Item Link URL">'
                f'<div class="nectar-list-item"><p class="muted sgp-num">{s["no"]}</p></div>'
                f'<div class="nectar-list-item"><p>{ESC(s["name"])}</p><p class="muted" style="font:400 15px/22px var(--f-text)">{ESC(s.get("card", ""))}</p></div>'
                f'<a class="full-link" href="{{{{url:{s["slug"]}}}}}" aria-label="{ESC(s["name"])}"></a></div>'
                for s in (self.svc(sl) for sl in g['services']))
            out.append(
                f'<div class="nectar-sticky-media-section" id="{g["key"]}" data-title="{ESC(g["name"])}" data-section-type="color" style="--bg:{bg}" data-text-color="{tc}" '
                f'data-salient="Sticky Content Section → Section Type: Color {bg} · Section ID {g["key"]}">'
                f'<div class="nectar-sticky-media-section__inner"><div class="vc_row inner_row" style="--pt:48px;--pb:48px;--pl:48px;--pr:48px;--pt-m:28px;--pb-m:28px;--pl-m:20px;--pr-m:20px" data-salient="Inner Row → 2 × ½ · Padding 48px">'
                f'<div class="row_col_wrap_12_inner">'
                f'<div class="wpb_column vc_col-sm-6"><div class="vc_column-inner">'
                f'<p class="nectar-responsive-text" data-inherit="h1" style="--fs:64px;--fg:#EF4539;--lh:1" aria-hidden="true">{i + 1:02d}</p>'
                f'<h2>{ESC(g["name"])}</h2><p class="nectar-responsive-text" data-inherit="h5" style="--fg:var(--tone-muted)">{ESC(self.lead(g))}</p>'
                f'<div>{rows}</div></div></div>'
                f'<div class="wpb_column vc_col-sm-6"><div class="vc_column-inner">'
                f'<div class="img-with-aniamtion-wrap" data-aspect="4-5" data-hover-animation="zoom-in-crop" data-salient="Image → 4:5 · Hover Animation: Zoom In Crop">'
                f'<div class="hover-wrap">{{{{img:{g["media"]}|w=900|sizes=(min-width:1000px) 38vw, 92vw|decorative}}}}</div></div>'
                f'</div></div></div></div></div></div>')
        return '\n'.join(out)

    def related(self, a):
        """S11: 3 Columns with Fancy Box → Image Above Text 3:2 (Entrance 0 / 120 / 240)."""
        slug = a.get('slug')
        base = self.svc(slug) if slug else None
        rel = (base or {}).get('related') or [s['slug'] for s in self.s.list[:3]]
        out = []
        for i, sl in enumerate(rel[:3]):
            s = self.svc(sl)
            hid = (s.get('hero') or {}).get('id', s.get('card_media'))
            out.append(
                f'<div class="wpb_column vc_col-sm-4" data-t-w="4" data-animation="slight-fade-in-from-bottom" data-delay="{i * 120}" '
                f'data-salient="Column → Animation: Slight Fade In From Bottom · Delay {i * 120}"><div class="vc_column-inner">'
                f'<a class="nectar-fancy-box" data-style="image_above_text_underline" data-aspect="3-2" data-border-radius="none" href="{{{{url:{sl}}}}}" '
                f'data-salient="Fancy Box → Style: Image Above Text · Image Aspect Ratio: 3:2 · Border Radius: None">'
                f'<div class="box-image">{{{{img:{hid}|w=760|sizes=(min-width:1000px) 30vw, 92vw|decorative}}}}</div>'
                f'<div class="meta-wrap"><h4><span class="fb-title">{ESC(s["name"])}</span></h4><p>{ESC(s.get("card", ""))}</p></div></a>'
                f'</div></div>')
        return '\n'.join(out)

    def footer(self, a):
        slugs = [x for x in (a.get('slugs') or ','.join(FOOTER_SLUGS)).split(',') if x]
        return ''.join(wave_link(f'{{{{url:{sl}}}}}', self.svc(sl)['name'], f'{{{{nav:{sl}}}}}') for sl in slugs)

    def options(self, a):
        return ''.join(f'<option>{ESC(s["name"])}</option>' for s in self.s.list) + '<option>Kita</option>'

    def render(self, variant, a):
        fn = {'menu': self.menu, 'rows': self.rows, 'hscroll': self.hscroll, 'pinned': self.pinned,
              'related': self.related, 'footer': self.footer, 'options': self.options}.get(variant)
        if not fn:
            raise self.Err(f'paslaugos:{variant} is not part of the Salient kit (menu | rows | hscroll | pinned | related | footer | options)')
        return fn(a)


# ---------------------------------------------------------------- media (docs/media.json only)
class KitMedia:
    def __init__(self, media, error):
        self.m, self.Err = media, error

    def _overlay(self, o):
        ov = o.get('overlay')
        return f'<div class="row-bg-overlay" style="--overlay:{ESC(ov)}"></div>' if ov else ''

    def _phone_picture(self, img, o):
        """Per-device image as ONE <picture> (only the matching source is downloaded): phones ≤ 690 px get the
        portrait crop, everything else the main image. Object position per device via --pos / --pos-m."""
        if not o.get('phone'):
            return img
        pid = o['phone']
        if pid not in self.m.photos:
            raise self.Err(f'media: photo {pid} is not in docs/media.json')
        srcset = ', '.join(f'{ESC(self.m.photo_url(pid, x))} {x}w' for x in (480, 760, 1100))
        pos, ppos = ESC(o.get('pos', '50% 50%')), ESC(o.get('phone-pos', '50% 50%'))
        img = img.replace(f'style="object-position:{pos}"', f'style="--pos:{pos};--pos-m:{ppos}"', 1)
        if '--pos-m' not in img:
            img = img.replace('<img ', f'<img style="--pos:{pos};--pos-m:{ppos}" ', 1)
        return f'<picture><source media="(max-width:690px)" srcset="{srcset}" sizes="100vw">{img}</picture>'

    def bgimg(self, pid, o):
        """Row / Section Background Image (+ per-device phone image) → .row-bg-wrap > .inner-wrap > .row-bg-layer"""
        w = int(o.get('w', 1920))
        eager = 'eager' if o.get('eager') else ''
        main = self.m.img(pid, {'w': str(w), 'sizes': '100vw', 'decorative': True, 'class': 'row-bg', 'pos': o.get('pos', '50% 50%'), 'eager': eager or None})
        return (f'<div class="row-bg-wrap" aria-hidden="true"><div class="inner-wrap"><div class="row-bg-layer">{self._phone_picture(main, o)}</div></div>'
                f'{self._overlay(o)}</div>')

    def bgvideo(self, vid, o):
        """Row / Section Video Background, native 18.2.1 structure (vc_row.php): the poster image sits in .row-bg-wrap
        (Background Image; phones, reduced motion, before play), the video in the sibling .nectar-video-wrap
        (video.nectar-video-bg, lazy MP4, desktop only via emul.js) under a .video-color-overlay (Video Color Overlay)."""
        v = self.m.videos.get(vid)
        if not v:
            raise self.Err(f'media: video {vid} is not in docs/media.json')
        pos = ESC(o.get('pos', '50% 50%'))
        srcset = ', '.join(f'{ESC(self.m.poster_url(vid, x))} {x}w' for x in (640, 960, 1280, 1920))
        load = 'fetchpriority="high"' if o.get('eager') else 'loading="lazy"'
        poster = (f'<img class="row-bg" src="{ESC(self.m.poster_url(vid, 1280))}" srcset="{srcset}" sizes="100vw" width="{v["width"]}" '
                  f'height="{v["height"]}" alt="" {load} decoding="async" style="object-position:{pos}">')
        video = (f'<video class="nectar-video-bg" data-src="{ESC(v["hd"])}" muted playsinline loop preload="none" aria-hidden="true" tabindex="-1" '
                 f'style="object-position:{pos}"></video>')
        ov = o.get('overlay')
        overlay = f'<div class="video-color-overlay row-bg-layer" style="--overlay:{ESC(ov)}" aria-hidden="true"></div>' if ov else ''
        return (f'<div class="row-bg-wrap" aria-hidden="true"><div class="inner-wrap"><div class="row-bg-layer">{self._phone_picture(poster, o)}</div></div></div>'
                f'<div class="nectar-video-wrap row-bg-layer" aria-hidden="true"><div class="nectar-video-inner">{video}</div></div>{overlay}')

    def colbg(self, pid, o):
        """Column Background Image (Scale To Column) + Color Overlay (Opacity → Opacity Hover)."""
        img = self.m.img(pid, {'w': o.get('w', '1100'), 'sizes': o.get('sizes', '(min-width:1000px) 40vw, 92vw'), 'decorative': True, 'pos': o.get('pos', '50% 50%')})
        ov = (f'<div class="column-overlay-layer" style="--overlay:{ESC(o.get("overlay", "#0B0E10"))};--o:{ESC(o.get("o", ".72"))};--o-h:{ESC(o.get("oh", o.get("o", ".72")))}"></div>')
        return f'<div class="column-image-bg-wrap" aria-hidden="true"><div class="inner-wrap">{img}</div></div>{ov}'

    def videourl(self, vid, o):
        v = self.m.videos.get(vid)
        if not v:
            raise self.Err(f'media: video {vid} is not in docs/media.json')
        return ESC(v['hd'])
