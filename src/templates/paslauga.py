"""SGP v2 — service template hook, Salient kit edition (team „service-template“).

tools/build.py calls blocks(svc, ctx) once per service in src/data/paslaugos.json; every returned key becomes
{{svc:<key>}} in src/templates/paslauga.html (keys ending in _html are inserted raw). The returned HTML is Salient
18.2.1 element markup for the emulation kit (docs/build-notes/kit.md) and may contain the usual build placeholders
({{img:…}}, {{bgimg:…}}, {{colbg:…}}, {{url:…}}, {{icon:…}}, {{partial:…}}) — they are expanded afterwards.

One WPBakery template „SGP – paslauga“ (plan §3.7) → 11 pages:
  S1 hero Row (template) · S2 Page Submenu · S3 Faktai · S4 Apie paslaugą (+ specials placed „apie“ + S4b Stations)
  · specials placed „after-apie“ (own Row) · S5 Privalumai (Sticky Media) or a special placed „why“ · specials placed
  „row“ · S7 Kliento atsakomybės (+ „aside“ / „atsak-end“ specials) · S8 Draudžiami daiktai · statement (gyvūnai)
  · S9 Maršrutai + grafikas · S10 Uždarymas · S11 Susijusios paslaugos · S12 Kita paslauga · S13 GS-Užklausa.
Specials (plan §3.8): pack X1 · video X2 · tags X3 · bays X4 · checklist X5 · price X6 · statement X7 ·
principles X8 · hotspots X9 · kvrow X10 · define X11 · callout/note X12 · box X13 (· steps_title X14 · X15 callout).
stdlib only; deterministic output.
"""
import re
from urllib.parse import quote

SUBMENU_IDS = {
    'Apie paslaugą': 'apie-paslauga', 'Privalumai': 'privalumai', 'Kliento atsakomybės': 'atsakomybes',
    'Draudžiami daiktai': 'draudziami', 'Užklausa': 'uzklausa', 'Principai': 'principai', 'Patogumai': 'patogumai',
    'Prieš kelionę': 'pries-kelione', 'Kaina': 'kaina', 'Maršrutai': 'marsrutai'}
WHY_H2 = 'Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?'
RESP_H2 = 'Kliento atsakomybės: ką reikia žinoti?'
CLOSING_MEDIA = '9807331'        # S10 parallax band (wet road, b/w) — the same for all 11 pages (template-wide)
PROHIBITED_MEDIA = '4040619'     # S8 asphalt texture
# fallbacks when a service's own media are all on the page already (every photo appears once per page)
APIE_POOL = ('1696742', '11053641', '32821932', '9989463', '8858566', '5919143')
FORM_POOL = ('21041157', '6720534', '7541981', '8858566', '11053641', '32821932', '9989463')   # GS-Užklausa image
ROUTE_WORDS = ['Lietuva', 'Lenkija', 'Vokietija', 'Belgija', 'Prancūzija', 'Ispanija', 'Airija']

# tones (plan §3 „Chapter row“): P paper · P2 paper-alt · A asphalt · A0 asphalt-950
TONES = {'P': ('#F5F7F6', 'dark'), 'P2': ('#EAEEED', 'dark'), 'A': ('#0F1417', 'light'), 'A0': ('#0B0E10', 'light')}
TONE_NAME = {'P': 'Chapter row P', 'P2': 'Chapter row P-alt', 'A': 'Chapter row A', 'A0': 'Chapter row A (asphalt-950)'}
CALLS = {
    'ie': ('tel:+37065053161', 'Į Airiją · +370 650 53161 – skambinti', 'Į Airiją · +370 650 53161'),
    'es': ('tel:+37063828919', 'Į Ispaniją · +370 638 28919 – skambinti', 'Į Ispaniją · +370 638 28919')}
# S1 Color Overlay → Advanced: 3 stacked linear gradients (top strip under the transparent header + breadcrumbs,
# bottom for the glass band, left→right for the H1/intro); the 90° end stop stays ≥ .4 so bright subjects on the
# right never drop the white header links / chips under 4.5:1 (phones: + sgp-custom.css C-15 flat scrim)
HERO_GRADE = ('linear-gradient(180deg,rgba(15,20,23,.72) 0%,rgba(15,20,23,0) 30%),'
              'linear-gradient(0deg,rgba(15,20,23,.92) 0%,rgba(15,20,23,0) 50%),'
              'linear-gradient(90deg,rgba(15,20,23,.9) 0%,rgba(15,20,23,.66) 44%,rgba(15,20,23,.4) 82%)')
CARD_P = '--bg:#FFFFFF;--bg-hover:#FFFFFF;--r:3px;--border:1px solid rgba(28,29,29,.12)'
CARD_A = '--bg:#161D21;--bg-hover:#1A2227;--r:3px;--border:1px solid rgba(242,244,243,.12)'


def A(s):
    """attribute-safe text (data-salient, aria-label)"""
    return (str(s).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;'))


# ---------------------------------------------------------------- element helpers (Kit API markup)
def badge(text, fg='', mt='', salient='Badge → Badge Style: Minimal Line · Line Width 28px · Inherit Typography From: Label'):
    st = ';'.join(x for x in (f'--fg:{fg}' if fg else '', f'--mt:{mt}' if mt else '') if x)
    st = f' style="{st}"' if st else ''
    return f'<span class="nectar-badge" data-badge-style="line"{st} data-salient="{A(salient)}">{text}</span>'


def chip(text, glass=False, large=False):
    if glass:
        return (f'<span class="nectar-badge" data-badge-style="default" data-display="inline" data-padding="small" data-backdrop-blur="12" '
                f'style="--bg:rgba(11,14,16,.4);--border:1px solid rgba(242,244,243,.26);--fg:#F2F4F3;--r:3px" '
                f'data-salient="Badge → Default (Chip, glass) · BG rgba(11,14,16,.4) · Border 1px rgba(242,244,243,.26) · Padding Small · '
                f'Border Radius 3px · Display Inline · Backdrop Filter: Blur 12">{text}</span>')
    pad, fs = ('large', ';--fs:15px') if large else ('small', '')
    return (f'<span class="nectar-badge" data-badge-style="default" data-display="inline" data-padding="{pad}" '
            f'style="--border:1px solid var(--tone-hair-2);--fg:var(--tone-fg);--r:3px{fs}" '
            f'data-salient="Badge → Default (Chip) · Border 1px hairline · Padding {pad.title()} · Border Radius 3px · Display Inline'
            f'{" · Custom Font Size 15px" if large else ""}">{text}</span>')


def heading(tag, html, style='', effect='default', delay='', salient_extra=''):
    names = {'default': 'Word Animations: Reveal', 'blur-bottom': 'Word Animations: Blur', 'fade-bottom': 'Word Animations: Fade',
             'scroll-opacity-reveal': 'Scroll Position: Opacity'}
    st = f' style="{style}"' if style else ''
    dl = f' data-delay="{delay}"' if delay else ''
    stag = ' data-stagger="true"' if effect != 'scroll-opacity-reveal' else ''
    sal = f'Animated Text → Text Element: {tag.upper()} · Text Effect: {names[effect]}{" · Stagger Animation ✓" if stag else ""}{salient_extra}'
    return f'<div class="nectar-split-heading" data-text-effect="{effect}"{stag}{dl}{st} data-salient="{A(sal)}"><{tag}>{html}</{tag}></div>'


def road(delay='', mt=''):
    dl = f' data-delay="{delay}"' if delay else ''
    m = f';--mt:{mt}' if mt else ''
    return (f'<div class="divider-wrap" data-line-type="small" data-animate{dl} style="--line-w:96px;--thickness:2px;--h:14px{m}" '
            f'data-salient="Divider → Line Type: Small Line · Custom Line Width 96px · Line Thickness 2px · Accent Color · Animate Line ✓ (road line)">'
            f'<span class="divider-border"></span></div>')


def road_full(mt='36px', color='rgba(28,29,29,.26)'):
    return (f'<div class="divider-wrap" data-line-type="full-width" data-animate style="--h:1px;--mt:{mt};--line-color:{color};--h-m:64px" '
            f'data-salient="Divider → Line Type: Full Width · Line Thickness 1px · Animate Line ✓ · Custom Height (phone) 64px (the road above the Stations)">'
            f'<span class="divider-border"></span></div>')


def intro(html, fg='var(--tone-muted)', maxw='56ch', inherit='h5', mt=''):
    m = f';--mt:{mt}' if mt else ''
    return (f'<p class="nectar-responsive-text" data-inherit="{inherit}" style="--fg:{fg};--max-w:{maxw}{m}" '
            f'data-salient="Responsive Text → Font Style: {inherit.upper()} · Max Width {maxw} (Intro)">{html}</p>')


def text(paras, fg='', maxw='', mt=''):
    st = ';'.join(x for x in (f'--fg:{fg}' if fg else '', f'--max-w:{maxw}' if maxw else '', f'--mt:{mt}' if mt else '') if x)
    st = f' style="{st}"' if st else ''
    return (f'<div class="wpb_text_column"{st} data-salient="Text Block">'
            + ''.join(f'<p>{p}</p>' for p in paras) + '</div>')


def call(d, stretch=False, mt=''):
    href, label, txt = CALLS[d]
    s = ' data-alignment="stretch"' if stretch else ''
    m = f' style="--mt:{mt}"' if mt else ''
    return (f'<a class="nectar-cta" data-style="arrow-circle-animation" data-color="accent-color"{s} href="{href}" aria-label="{label}"{m} '
            f'data-salient="Button → Type: Arrow Circle Animation · Button Roundness 3 · BG Accent · BG Hover #F4604F · Text #0F1417 · '
            f'Min Icon Size 36 · Icon Gap 20{" · Alignment: Stretch" if stretch else ""} · tel: + Aria Label">'
            f'<span class="link_text"><span class="text">{txt}</span></span></a>')


def link(href, label, mt='', aria=''):
    m = f' style="--mt:{mt}"' if mt else ''
    ar = f' aria-label="{A(aria)}"' if aria else ''
    return (f'<a class="nectar-cta" data-style="underline" href="{href}"{ar}{m} data-salient="Button → Type: Underline · Underline Visibility: Default (Visible)">'
            f'<span class="link_text"><span class="text">{label}</span></span></a>')


def button(href, label, color='extra-color-1', mt='', extra='', salient=''):
    m = f' style="--mt:{mt}"' if mt else ''
    names = {'extra-color-1': 'BG Extra Color 1 · Hover #222B30 · Text #F2F4F3', 'extra-color-2': 'BG Extra Color 2 · Hover #FFFFFF · Text #0F1417'}
    return (f'<a class="nectar-cta" data-style="arrow-circle-animation" data-color="{color}" href="{href}"{m}{extra} '
            f'data-salient="{A(salient or "Button → Type: Arrow Circle Animation · Button Roundness 3 · " + names[color])}">'
            f'<span class="link_text"><span class="text">{label}</span></span></a>')


def flex_row(inner, gap='10px', mt='', justify='', salient='Inner Row → Inner Column Layout: Flexbox · Horizontal · Wrap'):
    j = f' data-justify="{justify}"' if justify else ''
    m = f' style="--mt:{mt}"' if mt else ''
    return (f'<div class="vc_row inner_row"{m} data-salient="{A(salient)}"><div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-12" data-layout="flex" data-flex-dir="row"{j} style="--gap:{gap}" '
            f'data-salient="Inner Column → Layout: Flexbox · Direction: Horizontal · Wrap · Gap {gap}"><div class="vc_column-inner">'
            f'{inner}</div></div></div></div>')


def callout(inner, tone='P', mt='', pad='32px', salient=''):
    bg = {'P': '#EAEEED', 'W': '#FFFFFF', 'A': '#161D21'}[tone]
    tc = ' data-text-color="light"' if tone == 'A' else ''
    m = f' style="--mt:{mt}"' if mt else ''
    return (f'<div class="vc_row inner_row"{m} data-salient="Inner Row → Callout"><div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-12"{tc} data-el-space="10px" style="--bg:{bg};--r:3px;--border-left:2px solid #EF4539;'
            f'--pt:{pad};--pb:{pad};--pl:{pad};--pr:{pad};--pt-m:24px;--pb-m:24px;--pl-m:22px;--pr-m:22px" '
            f'data-salient="{A(salient or f"Inner Column → Callout: Background Color {bg} · Border Radius 3px · Border Type: Advanced (left 2px Accent) · Padding {pad} · Column Element Spacing 10px")}">'
            f'<div class="vc_column-inner">{inner}</div></div></div></div>')


def row(inner, *, tone='P', rid='', cc=True, pad='chapter', cls='', attrs='', style='', label='', rtype='full_width_background', bgimg=''):
    bg, tc = TONES[tone]
    dark = tone.startswith('A')
    c = ' sgp-dark' if dark else ''
    c += f' {cls}' if cls else ''
    i = f' id="{rid}"' if rid else ''
    p = ' data-padding="chapter"' if pad == 'chapter' else ''
    cc = cc and not dark          # Color Change Section only on paper chapters: dark chapters stay solid (no snow-on-paper flash, kit §10)
    ccs = ' data-color-change' if cc else ''
    st = f'--bg:{bg}' + (f';{pad}' if pad not in ('chapter', '') else '') + (f';{style}' if style else '')
    sal = (f'Row → {TONE_NAME[tone]}: Type {rtype.replace("_", " ").title()} · BG {bg} · Text Color: {"Light" if dark else "Dark"}'
           f'{" · Padding 8 % / 8 % (phones 80px)" if pad == "chapter" else ""}{" · Color Change Section ✓" if cc else ""}'
           f'{f" · Row ID {rid}" if rid else ""}{" · Extra Class sgp-dark" if dark else ""}{f" · {label}" if label else ""}')
    return (f'<div class="wpb_row{c}"{i} data-type="{rtype}" data-text-color="{tc}"{p}{ccs}{attrs} style="{st}" data-salient="{A(sal)}">\n'
            f'{bgimg}  <div class="row_col_wrap_12">\n{inner}\n  </div>\n</div>')


def inner_col(inner, el_space='10px', salient='Inner Row → Inner Column 12/12 · Column Element Spacing 10px'):
    return (f'<div class="vc_row inner_row" data-salient="{A(salient)}"><div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-12" data-el-space="{el_space}" data-salient="Inner Column 12/12"><div class="vc_column-inner">'
            f'{inner}</div></div></div></div>')


def col(inner, span, *, off=0, attrs='', style='', salient=''):
    o = f' vc_col-sm-offset-{off}' if off else ''
    st = f' style="{style}"' if style else ''
    return (f'    <div class="wpb_column vc_col-sm-{span}{o}"{attrs}{st} data-salient="{A(salient or f"Column {span}/12")}">'
            f'<div class="vc_column-inner">\n      {inner}\n    </div></div>')


class R:
    """Renderer for one service."""

    def __init__(self, svc, ctx):
        self.s, self.ctx, self.esc = svc, ctx, ctx['esc']
        self.media = ctx['media']
        self.by_slug = {x['slug']: x for x in ctx['services']}
        self.total = f'{len(ctx["services"]):02d}'
        self.specials = svc.get('specials') or []
        self.hero_id = (svc.get('hero') or {}).get('id', svc.get('card_media'))

    def sp(self, place):
        return [x for x in self.specials if x.get('place') == place]

    def special(self, x):
        fn = getattr(self, 'sp_' + x['type'], None)
        if not fn:
            raise ValueError(f'{self.s["slug"]}: unknown special type {x["type"]!r}')
        return fn(x)

    @staticmethod
    def img(mid, **o):
        opts = '|'.join(f'{k.replace("_", "-")}={v}' if v is not True else k for k, v in o.items())
        return '{{img:' + mid + ('|' + opts if opts else '') + '}}'

    def poster(self, vid, sizes):
        """Video Lightbox preview image = the clip's own poster frame (media.json → videos[].poster)."""
        v = self.media.videos[vid]
        srcset = ', '.join(f'{self.esc(self.media.poster_url(vid, w))} {w}w' for w in (640, 960, 1280))
        return (f'<img src="{self.esc(self.media.poster_url(vid, 1280))}" srcset="{srcset}" sizes="{sizes}" width="{v["width"]}" '
                f'height="{v["height"]}" alt="" loading="lazy" decoding="async">')

    def video_box(self, vid, label, mt=''):
        m = f' style="--mt:{mt}"' if mt else ''
        return (f'<a class="nectar-video-box" data-link-style="play_button_mouse_follow" data-mouse-style="see-through-contrast" '
                f'data-hover="zoom_bg_image" href="{{{{videourl:{vid}}}}}" aria-label="Paleisti vaizdo įrašą „{A(label)}“"{m} '
                f'data-salient="Video Lightbox → Link Style: Play Button With Image - Mouse Follow · Mouse Indicator Style: See Through Contrast · '
                f'Hover Effect: Zoom BG Image · Border Radius 0 · MP4 {vid} · Image = poster frame">'
                f'<div class="nectar-video-box__media">{self.poster(vid, "(min-width:1000px) 55vw, 92vw")}</div>'
                f'<span class="nectar-video-box__label" aria-hidden="true">{self.esc(label)} · video</span></a>')

    # ---------- S1 hero pieces (the Row itself is in paslauga.html)
    def hero_chips(self):
        return flex_row(''.join(chip(self.esc(c), glass=True) for c in self.s.get('chips', [])), gap='8px', mt='18px',
                        salient='Inner Row → Inner Column Flexbox (row, wrap, gap 8px) → Chips (glass)')

    # ---------- S2 Page Submenu
    def submenu(self):
        lis = ''.join(f'<li><a href="#{SUBMENU_IDS[l]}">{self.esc(l)}</a></li>' for l in self.s.get('submenu', []))
        return (
            '<div class="wpb_row sgp-dark" data-type="full_width_content" data-text-color="light" '
            'data-salient="Row → Type: Full Width Content · Padding 0 · Page Submenu">\n'
            '  <div class="row_col_wrap_12"><div class="wpb_column vc_col-sm-12" data-salient="Column 12/12"><div class="vc_column-inner">\n'
            '    <nav class="page-submenu" data-sticky data-alignment="left" style="--bg:#0F1417;--link:#F2F4F3" aria-label="Puslapio skyriai" '
            'data-salient="Page Submenu → Link Alignment: Left · Sticky? ✓ · Menu BG Color #0F1417 · Link Color #F2F4F3 · items = Menu Link → Row IDs '
            '(C-8 draws the active underline) · Phones/tablets &lt; 1000 px: native Salient collapses the links into a centred „Menu“ toggle + '
            'vertical dropdown — this demo keeps the horizontal scrolling strip, which is custom CSS (C-8 phone rule, requested in '
            'docs/build-notes/service-template.md R4)">'
            f'<div class="container"><ul>{lis}</ul></div></nav>\n'
            '  </div></div></div>\n</div>')

    # ---------- S3 Faktai
    def facts(self):
        s, e = self.s, self.esc
        kv = ''.join(
            f'<div class="nectar-hor-list-item" data-columns="2" data-column-layout="30-70" data-hover-effect="none" data-border-animation data-border-color="#C3CBCB" '
            f'data-salient="Horizontal List Item (KV rows) → Columns 2 · Column Layout 30% | 70% · Style: Bottom Border, No Hover Effect · '
            f'Border Animation ✓ · Border Color #C3CBCB · Column 1 Text Element: Paragraph · content &lt;p class=&quot;nectar-inherit-h6&quot;&gt;">'
            f'<div class="nectar-list-item"><p class="nectar-inherit-h6">{e(r["k"])}</p></div>'
            f'<div class="nectar-list-item"><p>{e(r["v"])}</p></div></div>' for r in s.get('kv', []))
        left = col(badge('Faktai') + f'<div style="--mt:14px" data-salient="KV rows">{kv}</div>', 6,
                   attrs=' data-t-w="12" data-el-space="none" data-animation="slight-fade-in-from-bottom"',
                   salient='Column 6/12 → Label + KV rows · Animation: Slight Fade In From Bottom')
        routes = s.get('routes') or []
        q = quote(s['name'])
        right = badge('Kryptys ir paslaugos') if routes else badge('Užklausa')
        if routes:
            right += flex_row(''.join(
                f'<a class="nectar-cta" data-style="see-through" data-preset="sm" href="?domina={q}#uzklausa" '
                f'data-salient="Button → Type: See Through · Preset sm · Button Roundness 3 · Border rgba(28,29,29,.26) → hover fill ink · Display inline · '
                f'Link ?domina=…#uzklausa"><span class="link_text"><span class="text">{e(r)}</span></span></a>' for r in routes),
                gap='8px', mt='4px', salient='Inner Row → Inner Column Flexbox (row, wrap, gap 8px) → route chips')
        right += button('#uzklausa', 'Gauti pasiūlymą', mt='28px')
        right_col = col(right, 5, off=1, attrs=' data-t-w="12" data-animation="slight-fade-in-from-bottom" data-delay="120"',
                        salient='Column 5/12 (offset 1) → Label + route chips (See Through sm) + Button (ink) · Animation: Slight Fade In From Bottom · Delay 120')
        return row(left + '\n' + right_col, tone='P', rid='faktai', pad='--pt:6%;--pb:6%;--pt-m:64px;--pb-m:64px',
                   label='Padding 6 % (phones 64px)')

    # ---------- photo plan: every photo appears once per page
    def fixed_media(self):
        """photos placed by other sections: hero, S5 why images, special images (Principai cards, hotspots),
        S11 related heroes, S12 next hero, S8 / S10 textures"""
        s, wm = self.s, self.s.get('why_media') or []
        why = [b.get('img') or wm[b.get('m', 0) % len(wm)] for b in s.get('why') or []] if not self.sp('why') else []
        spec = [m for x in self.specials for m in [x.get('img')] + [c.get('img') for c in x.get('cards') or []] if m]
        rel = [(self.by_slug[r].get('hero') or {}).get('id') for r in s.get('related') or [] if r in self.by_slug]
        return [self.hero_id, *why, *spec, *rel, self.next_service().get('hero', {}).get('id'), CLOSING_MEDIA, PROHIBITED_MEDIA]

    def media_plan(self):
        """(apie Cascading Images [2], GS-Užklausa image) — explicit apie_media / form_media first, then the service's
        own photos, then the template pools; raises if the page would show a photo twice"""
        if hasattr(self, '_plan'):
            return self._plan
        s = self.s
        fixed = self.fixed_media()
        body = [m for m in fixed if m not in (CLOSING_MEDIA, PROHIBITED_MEDIA)]
        dup = sorted({m for m in body if body.count(m) > 1})
        if dup:
            raise ValueError(f'{s["slug"]}: photo(s) {dup} used twice (hero / why / specials / related / next)')
        used = set(fixed)
        steps = [st['img'] for st in s.get('steps') or [] if st.get('img')]
        apie = []
        for m in [*(s.get('apie_media') or []), *steps, *APIE_POOL]:
            if m not in used and len(apie) < 2:
                apie.append(m); used.add(m)
        if s.get('apie_media') and apie != s['apie_media']:
            raise ValueError(f'{s["slug"]}: apie_media {s["apie_media"]} repeats a photo already on the page')
        form = next(m for m in [s.get('form_media'), *(s.get('why_media') or []), *steps, *FORM_POOL] if m and m not in used)
        self._plan = (apie, form)
        return self._plan

    # ---------- S4 Apie paslaugą (+ specials „apie“ + S4b Stations)
    def apie_media(self):
        """two photos for the Cascading Images (none of them elsewhere on the page)"""
        return self.media_plan()[0]

    def apie(self):
        s, e = self.s, self.esc
        paras = s.get('intro') or []
        first = intro(paras[0], fg='var(--tone-fg)', maxw='36em') if paras else ''
        rest = text(paras[1:], maxw='68ch') if len(paras) > 1 else ''
        m = self.apie_media()
        casc = ''
        if len(m) == 2:
            casc = (
                f'<div class="nectar_cascading_images" data-aspect="3-2" style="--mt:56px" data-salient="Cascading Images → Aspect Ratio 3:2 · '
                f'Image #1 {m[0]}: CSS Animation Grow In Reveal · Enable Parallax Scrolling ✓ · Parallax Intensity Subtle · Image #2 {m[1]}: Offset X 46 % · Offset Y 34 % · '
                f'CSS Animation Fade In From Bottom · Box Shadow Large Depth · Parallax Intensity Medium · Time Between Animations 200 · Layer Border Radius 0">'
                f'<div class="cascading-image" data-animation="grow-in-reveal" data-parallax="subtle" style="--w:70%;--h:80%"><div class="bg-layer">'
                f'{self.img(m[0], w=1100, sizes="(min-width:1000px) 40vw, 70vw", decorative=True)}</div></div>'
                f'<div class="cascading-image" data-animation="fade-in-from-bottom" data-parallax="medium" data-shadow="large_depth" '
                f'style="--x:46%;--y:34%;--w:54%;--h:66%;--z:2"><div class="bg-layer">{self.img(m[1], w=760, sizes="(min-width:1000px) 30vw, 52vw", decorative=True)}'
                f'</div></div></div>')
        side = col(badge(f'{e(s["no"])} / {self.total} · {e(s["name"])}') + heading('h2', 'Apie paslaugą') + road(mt='6px'), 4,
                   attrs=' data-sticky="top" data-t-w="12"',
                   salient='Column 4/12 → Sticky Content (CSS Powered, Top) · Label + Animated Text H2 + Road line')
        inline = ''.join(self.special(x) for x in self.sp('apie') if x['type'] in ('tags',))
        main = col(first + rest + inline + casc, 7, off=1, attrs=' data-t-w="12" data-animation="slight-fade-in-from-bottom"',
                   salient='Column 7/12 (offset 1) → Responsive Text H5 (first paragraph) + Text Block (Max Width 68ch) + Cascading Images · '
                           'Animation: Slight Fade In From Bottom')
        wide = ''.join(self.special(x) for x in self.sp('apie') if x['type'] not in ('tags',))
        cols = [side, main]
        if wide:
            cols.append(col(wide, 12, attrs=' data-el-space="none"', salient='Column 12/12 → special (Inner Row)'))
        st = self.steps()
        if st:
            cols.append(col(st, 12, attrs=' data-el-space="none"', salient='Column 12/12 → Label + Divider (road) + Icon List (Stations)'))
        return row('\n'.join(cols), tone='P2', rid='apie-paslauga')

    def steps(self):
        st = self.s.get('steps') or []
        if not st:
            return ''
        e = self.esc
        items = []
        for i, x in enumerate(st):
            lk = ''
            if x.get('link'):
                lk = f'<p><a href="{{{{url:{x["link"]["url"]}}}}}">{e(x["link"]["label"])} →</a></p>'
            items.append(f'<div class="nectar-icon-list-item" data-icon-type="numerical"><div class="list-icon-holder" aria-hidden="true"><span>{i + 1}</span></div>'
                         f'<div class="content"><h4>{e(x["t"])}</h4><p>{e(x["d"])}</p>{lk}</div></div>')
        title = self.s.get('steps_title') or 'Kaip tai vyksta'
        n = len(st)
        return (badge(e(title), mt='72px') + road_full(mt='30px') +
                f'<div class="nectar-icon-list" data-direction="horizontal" data-columns="{n}" data-icon-size="medium" data-icon-style="border" data-animate '
                f'style="--mt:-24px" data-salient="Icon List → Direction: Horizontal · {n} columns · Icon Size: Medium · Icon Style: Icon Colored W/ BG · '
                f'Icon Color: Accent · Animate Element? ✓ · items: Number + Header (H4) + Text („Stations“)">{"".join(items)}</div>')

    # ---------- S5 Privalumai — Sticky Content Sections → Sticky Media, Scrolling Content
    def why(self):
        s, e = self.s, self.esc
        blocks = s.get('why') or []
        if not blocks:
            return ''
        wm = s.get('why_media') or []
        n = len(blocks)
        secs = []
        for i, b in enumerate(blocks):
            mid = b.get('img') or wm[b.get('m', 0) % len(wm)]
            flag = f' · Note for the WP developer: {b["flag"]}' if b.get('flag') else ''
            rest = intro(b['t'], maxw='40em', mt='6px') if b.get('t') else ''
            h4 = f'<h4>{b["b"]}</h4>'
            secs.append(
                f'<div class="nectar-sticky-media-section" data-section-type="image" data-salient="{A(f"Sticky Content Section → Section Type: Image {mid}{flag}")}">'
                f'<div class="nsms-bg">{self.img(mid, w=1100, sizes="(min-width:1000px) 45vw, 92vw", decorative=True)}</div>'
                f'<div class="nectar-sticky-media-section__inner">{inner_col(badge(f"{i + 1:02d} / {n:02d}") + h4 + rest)}</div></div>')
        head = col(badge('Privalumai') + heading('h2', e(s.get('why_h2') or WHY_H2), style='--max-w:15em'), 8,
                   salient='Column 8/12 → Label + Animated Text H2 (Max Width 15em)')
        tail = col(chip('Nuo durų iki durų'), 4, attrs=' data-layout="flex" data-justify="flex-end" data-align="flex-end" data-hide="phone"',
                   salient='Column 4/12 → Layout: Flexbox · Justify flex-end · Chip · Device Visibility: hidden on phone')
        box = col(
            f'<div class="nectar-sticky-media-sections" data-type="default" data-content-position="right" data-media-width="45" data-media-height="80vh" '
            f'data-content-spacing="30vh" data-radius="3" data-salient="Sticky Content Sections → Type: Sticky Media, Scrolling Content · Content Position: Right · '
            f'Media Width 45 % · Media Height 80vh · Content Spacing 30vh · Border Radius 3 · Mobile Media Aspect Ratio 4:5">{"".join(secs)}</div>', 12,
            salient='Column 12/12 → Sticky Content Sections')
        return row('\n'.join([head, tail, box]), tone='A', rid='privalumai')

    # ---------- specials placed „apie“
    def sp_tags(self, x):                                                     # X3
        e = self.esc
        return (badge(e(x['k']), mt='36px') +
                flex_row(''.join(chip(e(t), large=True) for t in x['items']), gap='10px', mt='12px',
                         salient='Inner Row → Inner Column Flexbox (row, wrap, gap 10px) → Chips (Badge Default, Padding Large, 15px)'))

    def sp_bays(self, x):                                                     # X4
        e = self.esc
        yours, others = x['legend']
        return (
            f'<div class="vc_row inner_row" data-equal-height data-column-margin="none" style="--mt:64px" '
            f'data-salient="Inner Row → Equal Height · Column Margin None (special „{A(x["title"])}“)"><div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-7" data-animation="mask-reveal" data-mask-direction="right" data-mask-shape="straight" '
            f'style="--bg:#FFFFFF;--pt:40px;--pb:32px;--pl:40px;--pr:40px;--pt-m:24px;--pb-m:20px;--pl-m:16px;--pr-m:16px" '
            f'data-salient="Inner Column 7/12 → Background Color #FFFFFF · Padding 40px · Animation: Mask Reveal · Direction: Right · Shape: Straight">'
            f'<div class="vc_column-inner"><div class="img-with-aniamtion-wrap" '
            f'data-salient="Image → assets/img/paslaugos/daliniai-skyriai.svg (static illustration) · Animation: None (the Inner Column Mask Reveal carries it) · Border Radius 0">'
            f'<div class="hover-wrap"><img src="{{{{root}}}}assets/img/paslaugos/daliniai-skyriai.svg" width="1200" height="520" loading="lazy" '
            f'alt="{A("Schema: mikroautobuso krovinių skyrius padalintas į tris dalis; viduryje – Jūsų krovinys, šalia – kitų klientų kroviniai.")}"></div></div>'
            f'</div></div>'
            f'<div class="wpb_column vc_col-sm-5" data-text-color="light" data-layout="flex" data-justify="flex-end" '
            f'style="--bg:#161D21;--pt:40px;--pb:40px;--pl:40px;--pr:40px;--pt-m:28px;--pb-m:28px;--pl-m:22px;--pr-m:22px;--gap:14px" '
            f'data-salient="Inner Column 5/12 → Background Color #161D21 · Font Color #F2F4F3 · Layout: Flexbox (column, justify end) · Padding 40px">'
            f'<div class="vc_column-inner">{badge(e(x["title"]))}'
            f'<p class="nectar-responsive-text" data-inherit="h4" data-salient="Responsive Text → Font Style: H4">{e(x["caption"])}</p>'
            + flex_row(f'<span class="nectar-badge" data-badge-style="default" data-display="inline" data-padding="small" style="--bg:#EF4539;--fg:#0F1417;--r:3px" '
                       f'data-salient="Badge → Default · BG Accent · Text #0F1417 · Radius 3px">{e(yours)}</span>'
                       + chip(e(others)), gap='8px', mt='10px', salient='Inner Row → legend (2 Badges)')
            + '</div></div></div></div>')

    def sp_define(self, x):                                                   # X11
        e = self.esc
        return (
            f'<div class="vc_row inner_row" data-equal-height style="--mt:64px" data-salient="Inner Row → Equal Height (special „{A(x["k"])}“)">'
            f'<div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-5" data-text-color="light" data-layout="flex" data-justify="space-between" data-animation="slight-fade-in-from-bottom" '
            f'style="--bg:#161D21;--r:3px;--border-left:2px solid #EF4539;--pt:40px;--pb:40px;--pl:40px;--pr:40px;--pt-m:28px;--pb-m:28px;--pl-m:22px;--pr-m:22px;--gap:24px" '
            f'data-salient="Inner Column 5/12 → Callout (A): Background Color #161D21 · Border Radius 3px · Border Type: Advanced (left 2px Accent) · Padding 40px · '
            f'Layout: Flexbox (column, space-between) · Animation: Slight Fade In From Bottom">'
            f'<div class="vc_column-inner">{badge(e(x["k"]))}'
            f'<p class="nectar-responsive-text" data-inherit="h3" style="--fs:30px;--fs-m:24px;--lh:1.18" data-salient="Responsive Text → Font Style: H3 · Custom Font Size 30px (phone 24px)">{e(x["text"])}</p>'
            f'</div></div>'
            f'<div class="wpb_column vc_col-sm-7" data-animation-type="scroll_pos_advanced" data-scroll-start="ty:70;s:.94;o:.4" data-scroll-end="ty:0;s:1;o:1" '
            f'data-scroll-offset="0,70" data-salient="Inner Column 7/12 → Column Animation Type: Scroll Position Advanced · Start: Translate Y 70, Scale .94, '
            f'Opacity .4 → End: 0, 1, 1 · Viewport Trigger Offset 0–70"><div class="vc_column-inner">'
            f'{self.video_box(x["video"], "{{alt:" + x["video"] + "}}")}</div></div>'
            f'</div></div>')

    # ---------- special placed „after-apie“ (own Row, opens the dark Privalumai chapter)
    def sp_video(self, x):                                                    # X2
        e = self.esc
        body = ''
        if x.get('quote'):
            body = heading('h3', e(x['quote']), effect='blur-bottom', style='--fs:34px;--fs-m:26px;--lh:1.15;--max-w:22em')
        if x.get('chips'):
            body += flex_row(''.join(chip(e(c), large=True) for c in x['chips']), gap='10px', mt='8px',
                             salient='Inner Row → Inner Column Flexbox (row, wrap) → Chips (Padding Large, 15px)')
        bw = ' · Poster/clip b/w' if x.get('bw') else ''
        left = col(badge(e(x['k'])) + body, 5, attrs=' data-t-w="12"', salient=f'Column 5/12 → Label + {"Animated Text H3 (Blur)" if x.get("quote") else "Chips"}')
        right = col(self.video_box(x['video'], '{{alt:' + x['video'] + '}}'), 7,
                    attrs=' data-t-w="12" data-animation-type="scroll_pos_advanced" data-scroll-start="ty:90;s:.9;o:.5" data-scroll-end="ty:0;s:1;o:1" data-scroll-offset="0,80"',
                    salient=f'Column 7/12 → Video Lightbox{bw} · Column Animation Type: Scroll Position Advanced (Translate Y 90 → 0, Scale .9 → 1, Opacity .5 → 1, offset 0–80)')
        return row(left + '\n' + right, tone='A', attrs=' data-column-align="middle"', pad='--pt:8%;--pb:0px;--pt-m:80px;--pb-m:0px',
                   label='Vertically aligned columns · Padding 8 % / 0 (the Privalumai row continues the dark chapter)')

    # ---------- specials placed „row“
    def sp_pack(self, x):                                                     # X1
        e = self.esc
        items = ''.join(
            f'<div class="nectar-icon-list-item" data-icon-type="numerical"><div class="list-icon-holder" aria-hidden="true"><span>{i + 1}</span></div>'
            f'<div class="content"><h4>{e(t["t"])}</h4><p>{e(t["d"])}</p></div></div>' for i, t in enumerate(x['items']))
        n = len(x['items'])
        head = col(badge(e(x['label'])) + heading('h2', e(x['h2']), style='--max-w:14em') + road(mt='4px') + intro(e(x['lead']), mt='10px'), 8,
                   salient='Column 8/12 → Label + Animated Text H2 + Road line + Intro')
        lst = col(road_full(mt='40px') +
                  f'<div class="nectar-icon-list" data-direction="horizontal" data-columns="{n}" data-icon-size="medium" data-icon-style="border" data-animate '
                  f'style="--mt:-24px" data-salient="Icon List → Direction: Horizontal · {n} columns (tablet 2, phone 1) · Icon Size: Medium · '
                  f'Icon Style: Icon Colored W/ BG · Icon Color: Accent · Animate Element? ✓ · items: Number 1–{n} + Header H4 + Text">{items}</div>', 12,
                  attrs=' data-el-space="none"', salient='Column 12/12 → Divider (road) + Icon List (Stations)')
        return row(head + '\n' + lst, tone='P2', rid=x['id'])

    def sp_principles(self, x):                                               # X8 (placed „why“, replaces S5)
        e, n = self.esc, len(x['cards'])
        secs = []
        for i, c in enumerate(x['cards']):
            dark = i % 2 == 0                                                 # surfaces alternate asphalt / paper-alt (as apie „Principai“)
            bg, tc, num, fg = ('#161D21', 'light', '#EF4539', '#C3CBCB') if dark else ('#EAEEED', 'dark', '#C4301E', 'var(--tone-muted)')
            secs.append(
                f'<div class="nectar-sticky-media-section" id="{x["id"]}-{i + 1}" data-title="{A(c["t"])}" data-section-type="color" style="--bg:{bg}" '
                f'data-text-color="{tc}" data-salient="Sticky Content Section → Section Type: Color {bg} · Text Color: {tc.title()} · Section ID {x["id"]}-{i + 1}">'
                f'<div class="nectar-sticky-media-section__inner"><div class="vc_row inner_row" data-equal-height '
                f'style="--pt:44px;--pb:44px;--pl:48px;--pr:48px;--pt-m:28px;--pb-m:28px;--pl-m:20px;--pr-m:20px" '
                f'data-salient="Inner Row → 2 × ½ · Equal Height · Padding 44px 48px"><div class="row_col_wrap_12_inner">'
                f'<div class="wpb_column vc_col-sm-6" data-el-space="20px" data-salient="Inner Column ½ → Column Element Spacing 20px"><div class="vc_column-inner">'
                f'<p class="nectar-responsive-text" data-inherit="h1" style="--fs:88px;--fs-m:56px;--fg:{num};--lh:1" aria-hidden="true" '
                f'data-salient="Responsive Text → Font Style: H1 · Custom Font Size 88px (phone 56px) · Color {num}">{i + 1:02d}</p>'
                f'<h3>{e(c["t"])}</h3>{intro(e(c["text"]), fg=fg, maxw="52ch", inherit="p")}</div></div>'
                f'<div class="wpb_column vc_col-sm-6" data-salient="Inner Column ½ → Image"><div class="vc_column-inner">'
                f'<div class="img-with-aniamtion-wrap" data-fit data-hover-animation="zoom-in" style="height:100%;min-height:340px" '
                f'data-salient="Image → Fit to Container · Hover Animation: Zoom In · Border Radius 0 · Min Height 340px"><div class="hover-wrap">'
                f'{self.img(c["img"], w=900, sizes="(min-width:1000px) 38vw, 92vw", decorative=True)}</div></div></div></div>'
                f'</div></div></div></div>')
        head = col(badge(e(x['label'])) + heading('h2', e(x['h2']), style='--max-w:15em') + intro(e(x['lead']), mt='8px'), 8,
                   salient='Column 8/12 → Label + Animated Text H2 + Intro')
        box = col(
            f'<div class="nectar-sticky-media-sections" data-type="scroll-pinned-sections" data-effect="scale" data-stacked data-nav data-section-height="70vh" '
            f'data-subtract-nav data-content-alignment="middle" data-enabled="desktop" data-radius="3" style="--mt:36px" data-salient="Sticky Content Sections → Type: Sticky Scroll Pinned Sections · '
            f'Effect: Scale (1 → .92) · Stacked Appearance ✓ · Section Navigation ✓ (Accent) · Section Height 70vh · Subtract Navigation Height from Section Height ✓ · '
            f'Content Alignment: Middle · '
            f'Border Radius 3 · Effect Enabled: Desktop Enabled, Tablet/Phone Disabled (stack)">{"".join(secs)}</div>', 12,
            salient='Column 12/12 → Sticky Content Sections (Pinned)')
        return row(head + '\n' + box, tone='A0', rid=x['id'])

    def sp_hotspots(self, x):                                                 # X9
        e = self.esc
        wraps, items, i = [], [], 0
        for h in x['spots']:
            if h.get('list_only'):                                            # not a physical feature → legend only, icon instead of a number
                items.append(f'<div class="nectar-icon-list-item" data-icon-type="icon"><div class="list-icon-holder" aria-hidden="true">{{{{icon:{h["i"]}}}}}</div>'
                             f'<div class="content"><h4>{e(h["t"])}</h4><p>{e(h["d"])}</p></div></div>')
                continue
            i += 1
            if h['y'] < 12:
                raise ValueError(f'{self.s["slug"]}: hotspot {i} at top {h["y"]} % hides under the sticky Page Submenu (keep y ≥ 12)')
            pos, lab = h.get('tip', 'top'), A(f'{i} – {h["t"]}')
            wraps.append(
                f'<div class="nectar_hotspot_wrap" style="left:{h["x"]}%;top:{h["y"]}%" data-tooltip-position="{pos}">'
                f'<button class="nectar_hotspot" type="button" aria-label="{lab}"><span>{i}</span></button>'
                f'<div class="nttip" role="tooltip"><p><strong>{e(h["t"])}</strong></p><p>{e(h["d"])}</p></div></div>')
            items.append(f'<div class="nectar-icon-list-item" data-icon-type="numerical"><div class="list-icon-holder" aria-hidden="true"><span>{i}</span></div>'
                         f'<div class="content"><h4>{e(h["t"])}</h4><p>{e(h["d"])}</p></div></div>')
        side = col(badge(e(x['label'])) + heading('h2', e(x['h2'])) + road(mt='4px') +
                   f'<div class="nectar-icon-list" data-direction="vertical" data-icon-size="small" data-icon-style="border" data-animate style="--mt:28px" '
                   f'data-salient="Icon List → Direction: Vertical · Icon Size: Small · Icon Style: Icon Colored W/ BG · Icon Color: Accent · Animate Element? ✓ · '
                   f'items: Number 1–{i} + Header H4 + Text (legend of the hotspots){f" · {len(items) - i} × Icon (Linea) item for features without a hotspot" if len(items) > i else ""}">{"".join(items)}</div>', 4,
                   attrs=' data-sticky="top" data-t-w="12"', salient='Column 4/12 → Sticky Content (CSS, Top) · Label + H2 + Road line + Icon List')
        fig = col(
            f'<div class="vc_row inner_row" data-salient="Inner Row"><div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-12" data-animation="mask-reveal" data-mask-direction="bottom" data-mask-shape="straight" '
            f'data-salient="Inner Column → Animation: Mask Reveal · Direction: Bottom · Shape: Straight (1.3 s)"><div class="vc_column-inner">'
            f'<div class="nectar_image_with_hotspots" data-hotspot-icon="numerical" data-tooltip-func="hover" data-tooltip-shadow="medium_depth" '
            f'data-color="accent-color" data-animation data-salient="Image With Hotspots → Image {x["img"]} · Hotspot Icon: Numerical · Tooltip Functionality: '
            f'Show On Hover · Tooltip Shadow: Medium Depth · Enable Animation ✓ · Color: Accent (C-7) · {i} hotspots, physical features only, all below the sticky Page Submenu (top ≥ 12 %)">'
            f'{self.img(x["img"], w=1100, sizes="(min-width:1000px) 58vw, 92vw")}{"".join(wraps)}</div>'
            f'<p class="nectar-responsive-text" data-inherit="small" style="--fg:var(--tone-muted);--mt:12px" data-salient="Responsive Text → small (caption)">{e(x["caption"])}</p>'
            f'</div></div></div></div>', 7, off=1, attrs=' data-t-w="12"', salient='Column 7/12 (offset 1) → Inner Row (Mask Reveal) → Image With Hotspots')
        return row(side + '\n' + fig, tone='P', rid=x['id'])

    def sp_kvrow(self, x):                                                    # X10
        e = self.esc
        kv = ''.join(
            f'<div class="nectar-hor-list-item" data-columns="2" data-column-layout="30-70" data-hover-effect="none" data-border-animation data-border-color="#C3CBCB" '
            f'data-salient="Horizontal List Item (KV rows) → 30% | 70% · Bottom Border, No Hover Effect · Border Animation ✓ · Border Color #C3CBCB · Column 1 Text Element: Heading 4">'
            f'<div class="nectar-list-item"><h4>{e(r["k"])}</h4></div><div class="nectar-list-item"><p>{e(r["v"])}</p></div></div>' for r in x['kv'])
        side = col(badge(e(x['label'])) + heading('h2', e(x['h2'])) + road(mt='4px'), 4, attrs=' data-sticky="top" data-t-w="12"',
                   salient='Column 4/12 → Sticky Content (CSS, Top) · Label + Animated Text H2 + Road line')
        main = col(kv, 7, off=1, attrs=' data-t-w="12" data-el-space="none" data-animation="slight-fade-in-from-bottom"',
                   salient='Column 7/12 (offset 1) → KV rows · Animation: Slight Fade In From Bottom')
        return row(side + '\n' + main, tone='P2', rid=x['id'])

    def sp_checklist(self, x):                                                # X5 (lead's brief: documents checklist = Icon List)
        e, n = self.esc, len(x['items'])
        items = ''.join(
            f'<div class="nectar-icon-list-item" data-icon-type="numerical"><div class="list-icon-holder" aria-hidden="true"><span>{i + 1}</span></div>'
            f'<div class="content"><h4>{e(it["t"])}</h4><p>{it["text"]}</p></div></div>' for i, it in enumerate(x['items']))
        c = x.get('callout')
        co = callout(badge(e(c['k'])) + text([e(c['text'])]), tone='W', mt='40px', pad='28px') if c else ''
        side = col(badge(e(x['label'])) + heading('h2', e(x['h2'])) + road(mt='4px') + intro(x['lead'], mt='10px', maxw='34ch') + co, 5,
                   attrs=' data-sticky="top" data-t-w="12"', salient='Column 5/12 → Sticky Content (CSS, Top) · Label + H2 + Road line + Intro + Callout')
        main = col(
            f'<div class="nectar-icon-list" data-direction="vertical" data-icon-size="medium" data-icon-style="border" data-animate '
            f'data-salient="Icon List → Direction: Vertical · Icon Size: Medium · Icon Style: Icon Colored W/ BG · Icon Color: Accent · Animate Element? ✓ · '
            f'items: Number 1–{n} + Header H4 (NEW titles) + Text (verbatim)">{items}</div>', 6, off=1,
            attrs=' data-t-w="12"', salient='Column 6/12 (offset 1) → Icon List (checklist)')
        return row(side + '\n' + main, tone='P', rid=x['id'])

    def sp_price(self, x):                                                    # X6
        e = self.esc
        ics = ['cage', 'heart', 'route']
        cards = []
        for i, t in enumerate(x['tiles']):
            cards.append(col(
                f'<div class="nectar_icon_wrap" data-style="border-animation" data-draw data-delay="{i * 120}" style="--ic-size:44px" '
                f'data-salient="Icon → Library: Linea (line draw on entry, speed Medium) · Icon Style: Border W/ Hover Animation · Color: Accent">'
                f'{{{{icon:{ics[i % 3]}}}}}</div><h4 style="--mt:28px">{e(t["t"])}</h4>{intro(e(t["d"]), inherit="p", maxw="30ch")}',
                4, attrs=f' data-t-w="4" data-animation="fade-in-from-bottom" data-delay="{i * 120}"',
                style=CARD_A + ';--pt:40px;--pb:40px;--pl:36px;--pr:36px;--pl-m:24px;--pr-m:24px',
                salient=f'Column 4/12 → Card (A): Background Color #161D21 · Background Color Hover #1A2227 · Border Radius 3px · Border Simple 1px · '
                        f'Padding 40px · Animation: Fade In From Bottom · Delay {i * 120}'))
        head = col(badge(e(x['label'])) + heading('h2', e(x['h2'])) + road(mt='4px'), 5, attrs=' data-t-w="12"',
                   salient='Column 5/12 → Label + Animated Text H2 + Road line')
        txt = col(intro(e(x['lead']), fg='var(--tone-fg)', maxw='40em') + text([e(x['text'])], maxw='62ch', fg='#C3CBCB') +
                  button('#uzklausa', 'Gauti pasiūlymą', color='extra-color-2', mt='12px'), 7,
                  attrs=' data-t-w="12" data-animation="slight-fade-in-from-bottom"',
                  salient='Column 7/12 → Responsive Text H5 (verbatim) + Text Block (verbatim) + Button (paper)')
        return row('\n'.join([head, txt] + cards), tone='A', rid=x['id'], attrs=' data-equal-height')

    # ---------- specials placed „aside“ / „atsak-end“ (inside S7)
    def sp_callout(self, x):                                                  # X12
        return callout(badge(self.esc(x['k'])) + text([self.esc(x['text'])]), tone='W', mt='36px', pad='28px',
                       salient='Inner Column → Callout: Background Color #FFFFFF · Border Radius 3px · Border Type: Advanced (left 2px Accent) · Padding 28px')

    def sp_note(self, x):                                                     # X12
        e, l = self.esc, x['link']
        return (
            f'<div class="vc_row inner_row" style="--mt:40px" data-salient="Inner Row → Card"><div class="row_col_wrap_12_inner">'
            f'<div class="wpb_column vc_col-sm-12" data-el-space="10px" style="{CARD_P};--bg-hover:#FFFFFF;--pt:32px;--pb:32px;--pl:32px;--pr:32px;--pl-m:22px;--pr-m:22px" '
            f'data-salient="Inner Column → Card: Background Color #FFFFFF · Border Radius 3px · Border Simple 1px hairline · Padding 32px"><div class="vc_column-inner">'
            f'<div class="nectar_icon_wrap" data-style="border-animation" data-draw style="--ic-size:32px" data-salient="Icon → Linea (line draw) · '
            f'Icon Style: Border W/ Hover Animation · Accent">{{{{icon:paw}}}}</div>'
            f'{badge(e(x["k"]), mt="18px")}{text([e(x["text"])])}{link("{{url:" + l["url"] + "}}", e(l["label"]) + " →", mt="8px")}'
            f'</div></div></div></div>')

    def sp_box(self, x):                                                      # X13
        e = self.esc
        return callout(
            badge(e(x['title'])) +
            f'<div class="img-with-aniamtion-wrap" data-animation="fade-in-from-bottom" style="--mt:18px;--max-w:340px" '
            f'data-salient="Image → assets/img/paslaugos/pakavimas-5cm.svg (static illustration) · Animation: Fade In From Bottom · Max Width 340px">'
            f'<div class="hover-wrap"><img src="{{{{root}}}}assets/img/paslaugos/pakavimas-5cm.svg" width="360" height="300" loading="lazy" '
            f'alt="{A("Pakavimo schema: tarp pakuotės sienelių ir turinio paliekamas 5 cm tarpas, užpildytas užpildu.")}"></div></div>'
            + text([e(t) for t in x['caption']], mt='16px'), tone='W', mt='36px', pad='28px',
            salient='Inner Column → Callout: Background Color #FFFFFF · Border Radius 3px · Border Type: Advanced (left 2px Accent) · Padding 28px')

    # ---------- S7 Kliento atsakomybės
    def resp(self):
        s, e = self.s, self.esc
        rs = s.get('responsibilities') or []
        aside = ''.join(self.special(x) for x in self.sp('aside'))
        end = ''.join(self.special(x) for x in self.sp('atsak-end'))
        if not rs and not aside:
            return ''
        lead = ''.join(intro(t, mt='12px', maxw='40ch') for t in (s.get('resp_lead') or []))
        if len(rs) == 1:                                                      # X15 one responsibility → Callout
            r = rs[0]
            main = callout(badge(e(r['title'])) + text(r['text']), tone='W', pad='36px',
                           salient='Inner Column → Callout (one responsibility): Background Color #FFFFFF · Border Radius 3px · Border Type: Advanced (left 2px Accent) · Padding 36px')
        else:
            tg = ''.join(f'<div class="toggle"><h3 class="toggle-title">{e(r["title"])}</h3><div class="inner-toggle-wrap"><div class="toggle-content">'
                         + ''.join(f'<p>{t}</p>' for t in r['text']) + '</div></div></div>' for r in rs)
            main = (f'<div class="toggles" data-style="animated_circle" data-accordion data-first-open data-circle-position="right" data-circle-size="40" '
                    f'data-divider style="--r:3px" data-salient="Toggle Panels → Style: Animated Circle · Animated Circle Position: Right · Animated Circle Size 40 · Enable Divider ✓ · '
                    f'Accordion Toggles ✓ · Starting Functionality: First Toggle Open · Border Radius 3 · titles NEW, texts verbatim · deep link ?toggle=N">{tg}</div>')
        side = col(badge('Kliento atsakomybės') + heading('h2', e(RESP_H2), style='--max-w:11em') + road(mt='4px') + lead + aside, 5,
                   attrs=' data-sticky="top" data-t-w="12"', salient='Column 5/12 → Sticky Content (CSS, Top) · Label + Animated Text H2 + Road line + Intro + specials')
        mainc = col(main + end, 6, off=1, attrs=' data-t-w="12" data-animation="slight-fade-in-from-bottom" data-delay="120"',
                    salient='Column 6/12 (offset 1) → Toggle Panels / Callout · Animation: Slight Fade In From Bottom · Delay 120')
        return row(side + '\n' + mainc, tone='P', rid='atsakomybes')

    # ---------- S8 Draudžiami daiktai
    def ban(self, shared):
        s, e = self.s, self.esc
        pr = s.get('prohibited')
        if not pr:
            return ''
        P = shared.get('prohibited_p') or {}
        if pr == 'P':
            pr = {'lead': [], 'items': 'P'}
        items, is_p = pr.get('items'), False
        if items == 'P':
            is_p, items = True, P['items']
        lead = list(pr.get('lead') or [])
        if is_p:
            lead.append(e(P['lead']))
        src = 'Tarptautiniai pervežimai: 8 bullets (shared.prohibited_p)' if is_p else 'service text, list split from the verbatim sentence'
        ul = (f'<ul class="nectar-fancy-ul" data-list-icon="fa-times" data-animation data-spacing="15px" style="--mt:28px" '
              f'data-salient="Fancy Unordered List → Icon: Font Icon fa-times · Color Accent · Spacing 15px · Enable Animation ✓ · {src}">'
              + ''.join(f'<li>{e(t)}</li>' for t in items) + '</ul>')
        tail = text([e(pr['tail'])], fg='#9AA6AB', mt='12px') if pr.get('tail') else ''
        note = text(pr.get('note'), fg='#C3CBCB', maxw='62ch', mt='28px') if pr.get('note') else ''
        left = col(badge('Draudžiami daiktai') + heading('h2', 'Draudžiami daiktai') + road(mt='4px') + text(lead, fg='#C3CBCB', maxw='62ch', mt='16px')
                   + ul + tail + note, 7, attrs=' data-t-w="12"', salient='Column 7/12 → Label + Animated Text H2 + Road line + Text Block + Fancy UL ✕')
        fine = (badge('Baudos') +
                '<div class="nectar-milestone" data-effect="count" data-inherit="h2" data-symbol-pos="after" data-symbol-alignment="superscript" '
                'style="--fs:104px;--fs-m:76px" data-salient="Milestone → Milestone Number 1200 · Milestone Number Inherit Font: H2 · Milestone Number Font Size 104px (phone 76px) · '
                'Animation Effect: Count To Value (2.2 s) · Milestone Symbol „EUR“ · Milestone Symbol Position: After · Milestone Symbol Alignment: Superscript">'
                '<div class="number"><span class="num">1200</span><span class="symbol">EUR</span></div>'
                '<div class="subject">Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)</div></div>'
                + button('{{url:taisykles}}', 'Visos taisyklės', color='extra-color-2', mt='24px'))
        if is_p and P.get('note'):
            fine += badge('Svarbu', mt='36px') + text([e(P['note'])], fg='#F2F4F3')
        right = col(callout(fine, tone='A', pad='40px'), 4, off=1, attrs=' data-sticky="top" data-t-w="12"',
                    salient='Column 4/12 (offset 1) → Sticky Content (CSS, Top) · Callout (A) with Milestone + Button (paper)')
        return row(left + '\n' + right, tone='A0', rid='draudziami', cc=False, pad='chapter',
                   attrs=' data-parallax-speed="medium_fast" data-bg-animation="fade-in"',
                   label=f'Background Image {PROHIBITED_MEDIA} · Parallax Background Media On Scroll: Regular (0.28) · Background Layer Animation: Fade In · '
                         f'Color Overlay: Heavy (0.8) #0B0E10',
                   bgimg=f'{{{{bgimg:{PROHIBITED_MEDIA}|w=1600|overlay=rgba(11,14,16,.8)}}}}')

    # ---------- X7 statement (gyvūnai)
    def statement(self):
        st = self.s.get('statement')
        if not st:
            return ''
        e = self.esc
        m = re.match(r'(.+?[.!?])\s+(.*)', st)
        first, rest = (m.group(1), m.group(2)) if m else (st, '')
        left = col(heading('h2', e(first), style='--fs:48px;--fs-t:40px;--fs-m:30px;--lh:1.05;--max-w:16em'), 7, attrs=' data-t-w="12"',
                   salient='Column 7/12 → Statement: Animated Text H2 · Custom Font Size 48px (tablet 40, phone 30) · Max Width 16em')
        right = col(text([e(rest)]) + call('ie', stretch=True, mt='16px') + call('es', stretch=True, mt='10px'), 4, off=1,
                    attrs=' data-t-w="12" data-animation="slight-fade-in-from-bottom" data-delay="120"',
                    salient='Column 4/12 (offset 1) → Text Block (verbatim) + 2 × Call (red, Stretch) · Animation: Slight Fade In From Bottom')
        return row(left + '\n' + right, tone='P2', pad='--pt:7%;--pb:7%;--pt-m:72px;--pb-m:72px', label='Padding 7 % (phones 72px)')

    # ---------- S9 Maršrutai: grafikas tabs + Scrolling Text + GS-Maršrutai
    def routes(self):
        head = col(badge('Maršrutai') + heading('h2', 'Artimiausi pervežimai', style='--max-w:10em') + road(mt='4px') +
                   link('{{url:grafikas}}', 'Visas grafikas →', mt='18px'), 4, attrs=' data-t-w="12"',
                   salient='Column 4/12 → Label + Animated Text H2 + Road line + Link')
        tabs = col(
            '<div class="tabbed" data-style="minimal_alt" data-animation="fade" data-salient="Tabs → Style: Minimal · Tab Change Animation: Fade · '
            'panels = Global Section element (GS-Grafikas Airija / Ispanija) · deep link ?tab=airija">'
            '<ul class="wpb_tabs_nav"><li><a href="#tab-airija">Airija</a></li><li><a href="#tab-ispanija">Ispanija</a></li></ul>'
            '<div class="wpb_tab" id="tab-airija">{{partial:gs-grafikas-ie|tone=P}}</div>'
            '<div class="wpb_tab" id="tab-ispanija">{{partial:gs-grafikas-es|tone=P}}</div></div>', 8,
            attrs=' data-t-w="12" data-animation="slight-fade-in-from-bottom"', salient='Column 8/12 → Tabs (Minimal)')
        words = ' ✦ '.join(ROUTE_WORDS)
        marquee = (
            '<div class="wpb_row" data-type="full_width_content" data-text-color="dark" style="--bg:#F5F7F6;--pt:5%;--pb:40px;--pt-m:48px;--pb-m:24px" '
            'data-salient="Row → Type: Full Width Content · BG #F5F7F6 · Scrolling Text (route countries)">\n  <div class="row_col_wrap_12">\n'
            + col('<div class="nectar-scrolling-text" data-s-speed="slower" data-repeat="3" data-divider="✦" data-divider-size="half" data-mask-edges '
                  'data-move-on-scroll data-outline="thin" data-outline-divider data-spin-divider '
                  'style="--fs:8vw;--fs-m:16vw;--space:.35em;--divider-color:#EF4539;--outline-color:#1C1D1D" '
                  'data-salient="Scrolling Text → Scrolling Speed: Slowest (45 s) · Number of Text Repeats 3 · Italic Style: Text Outline · Outline Thickness: Thin · '
                  'Outline Applies To: Text Content and Custom Divider · Move on Scroll ✓ · Mask Edges ✓ · Text Repeat Divider: Custom „✦“ · Custom Text Repeat Divider '
                  'Size: Half · Custom Text Repeat Divider Color: Accent · Custom Text Repeat Divider Spin on Scroll ✓ · Custom Font Size 8vw · Custom Font Size Mobile 16vw">'
                  f'<p class="nectar-responsive-text" data-inherit="h2" aria-label="{", ".join(ROUTE_WORDS)}" data-salient="Scrolling Text → Text Content (Text Element: H2 style)">{words}</p></div>', 12,
                  salient='Column 12/12')
            + '\n  </div>\n</div>')
        return '\n'.join([row(head + '\n' + tabs, tone='P', rid='marsrutai', pad='--pt:8%;--pb:2%;--pt-m:80px;--pb-m:24px',
                              label='Padding 8 % / 2 %'),
                          marquee, '{{partial:gs-marsrutai|cols=2|tone=P|pt=24px}}'])

    # ---------- S10 Uždarymas (parallax photo band)
    def closing(self):
        s, e = self.s, self.esc
        txt = s.get('closing') or ''                                          # trusted data, may contain <b> (perkraustymo)
        for ph in s.get('closing_marks') or []:
            if ph not in txt:
                raise ValueError(f'{s["slug"]}: closing_marks phrase {ph!r} not found in closing')
            txt = txt.replace(ph, f'<em>{ph}</em>', 1)
        more = intro(e(s['closing_more']), fg='#C3CBCB', maxw='52ch', mt='18px') if s.get('closing_more') else ''
        acts = flex_row(call('ie') + call('es'), gap='12px', mt='36px', salient='Inner Row → Inner Column Flexbox (row, wrap, gap 12px) → 2 × Call (red)')
        links = flex_row(link('{{url:grafikas}}', 'Pervežimų grafikas →') + link('{{url:kontaktai}}', 'Kontaktai →'), gap='28px', mt='18px',
                         salient='Inner Row → Inner Column Flexbox (row, gap 28px) → 2 × Link (Underline)')
        body = col(
            badge(e(s['name'])) +
            f'<div class="nectar-highlighted-text" data-style="regular_underline" data-underline-thickness="3px" style="--hl:#EF4539;--fs:52px;--fs-m:30px;--lh:1.12;--max-w:1000px" '
            f'data-salient="Highlighted Text → Style: Regular Underline · Color: Accent · Underline Thickness 3px · Custom Font Size 52px (phone 30px) / 1.12 · Max Width 1000px · '
            f'Text Element H3 · the italic phrases get the red line (verbatim)"><h3>{txt}</h3></div>' + more + acts + links, 10,
            attrs=' data-t-w="12"', salient='Column 10/12 → Label + Highlighted Text + Intro + Calls + Links')
        return row(body, tone='A0', cc=False, pad='--pt:12%;--pb:12%;--pt-m:104px;--pb-m:104px',
                   attrs=' data-parallax-speed="slow" data-bg-animation="zoom-out-slow"',
                   label=f'Background Image {CLOSING_MEDIA} · Parallax Background Media On Scroll: High (0.60) · Background Layer Animation: Zoom Out Slowly (8 s) · '
                         f'Color Overlay: Heavy (0.8) #0B0E10 · Padding 12 %',
                   bgimg=f'{{{{bgimg:{CLOSING_MEDIA}|w=1920|overlay=rgba(11,14,16,.8)}}}}')

    # ---------- S11 Susijusios paslaugos
    def related(self):
        if not self.s.get('related'):
            return ''
        head = col(badge('Tarptautiniai pervežimai') + heading('h2', 'Susijusios paslaugos'), 8, salient='Column 8/12 → Label + Animated Text H2')
        more = col(link('{{url:paslaugos}}', 'Visos paslaugos →'), 4, attrs=' data-layout="flex" data-justify="flex-end" data-align="flex-end"',
                   salient='Column 4/12 → Layout: Flexbox · Justify/Align flex-end · Link')
        return row(head + '\n' + more + '\n{{paslaugos:related|slug=' + self.s['slug'] + '}}', tone='P', rid='susijusios',
                   label='3 × Column + Fancy Box → Image Above Text (GS-free, paslaugos:related)')

    # ---------- S12 Kita paslauga (photo card band)
    def next_service(self):
        c = self.ctx
        nx = self.by_slug[self.s.get('next')] if self.s.get('next') in self.by_slug else None
        if not nx:
            i = [x['slug'] for x in c['services']].index(self.s['slug'])
            nx = c['services'][(i + 1) % len(c['services'])]
        return nx

    def next_band(self):
        nx = self.next_service()
        nid = (nx.get('hero') or {}).get('id', nx.get('card_media'))
        crop = (nx.get('hero') or {}).get('crop', '50% 50%')
        e = self.esc
        no, slug = nx['no'], nx['slug']
        inner = (
            f'{{{{colbg:{nid}|w=1920|sizes=100vw|pos={crop}|o=.8|oh=.52}}}}'
            f'<div class="vc_column-inner">{badge(f"Kita paslauga · {no} / {self.total}", fg="#F2F4F3")}'
            f'{heading("h2", e(nx["name"]), style="--fs:6.4vw;--fs-min:44px;--fs-max:104px;--lh:.95;--max-w:12em")}'
            f'<a class="nectar-cta" data-style="arrow-circle-animation" data-color="extra-color-2" href="{{{{url:{nx["slug"]}}}}}" tabindex="-1" aria-hidden="true" '
            f'style="--mt:28px" data-salient="Button (paper) · decorative — the Column Link carries the URL"><span class="link_text"><span class="text">Plačiau</span></span></a>'
            f'</div><a class="column-link" href="{{{{url:{nx["slug"]}}}}}" aria-label="Kita paslauga: {A(nx["name"])}"></a>')
        colh = (f'    <div class="wpb_column vc_col-sm-12" data-text-color="light" data-layout="flex" data-justify="flex-end" data-bg-parallax="very_subtle" '
                f'style="--min-h:62vh;--min-h-m:60svh;--pt:10%;--pb:6%;--pl:8%;--pr:8%;--pt-m:120px;--pb-m:48px;--pl-m:20px;--pr-m:20px" '
                f'data-salient="{A(f"Column 12/12 → Photo card: Background Image {nid} (next service hero) · Scale To Column · Color Overlay #0B0E10 Opacity .8 → Opacity Hover .52 · Background Image Parallax Scrolling: Very Subtle · Min Height 62vh · Layout: Flexbox (justify end) · Column Link → {slug}")}">'
                f'{inner}</div>')
        return (f'<div class="wpb_row sgp-dark" data-type="full_width_content" data-text-color="light" style="--bg:#0B0E10" '
                f'data-salient="Row → Type: Full Width Content · BG #0B0E10 · Padding 0 · „Kita paslauga“ (S12)">\n  <div class="row_col_wrap_12">\n{colh}\n  </div>\n</div>')

    # ---------- assemble
    def body(self, shared):
        rows = [self.apie()]
        rows += [self.special(x) for x in self.sp('after-apie')]
        whyrow = self.sp('why')
        rows.append(''.join(self.special(x) for x in whyrow) if whyrow else self.why())
        rows += [self.special(x) for x in self.sp('row')]
        rows += [self.resp(), self.ban(shared), self.statement()]
        return '\n'.join(r for r in rows if r)


def blocks(svc, ctx):
    shared = ctx.get('shared') or {}
    r = R(svc, ctx)
    return {
        'hero_chips_html': r.hero_chips(),
        'hero_grade': HERO_GRADE,
        'submenu_html': r.submenu(),
        'facts_html': r.facts(),
        'body_html': r.body(shared),
        'routes_html': r.routes(),
        'closing_html': r.closing(),
        'related_html': r.related(),
        'next_html': r.next_band(),
        'form_media': r.media_plan()[1],
    }
