"""SGP v2 — service template hook (owned by the services team: pages-service-template).

tools/build.py calls blocks(svc, ctx) once per service in src/data/paslaugos.json; every returned key becomes
{{svc:<key>}} in src/templates/paslauga.html (keys ending in _html are inserted raw). The returned HTML may contain
the usual build placeholders ({{img:…}}, {{url:…}}, {{bgvideo:…}}, {{partial:…}}) — they are expanded afterwards.

Rows (dizaino-sistema.md §6.5): T2 Faktai · T3 01 Apie paslaugą (+ „Kaip tai vyksta“ stations + specials placed
„apie“) · T4 Privalumai (sticky media) or a special placed „why“ · special rows („row“) · T6 Kliento atsakomybės
(+ „aside“ / „atsak-end“ specials) · T7 Draudžiami daiktai · statement (gyvūnai) · T9 closing + related services.
stdlib only; deterministic output.
"""
import re
from urllib.parse import quote

SUBMENU_IDS = {
    'Apie paslaugą': 'apie-paslauga', 'Privalumai': 'privalumai', 'Kliento atsakomybės': 'atsakomybes',
    'Draudžiami daiktai': 'draudziami', 'Užklausa': 'uzklausa', 'Principai': 'principai', 'Patogumai': 'patogumai',
    'Prieš kelionę': 'pries-kelione', 'Kaina': 'kaina'}
WHY_H2 = 'Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?'
RESP_H2 = 'Kliento atsakomybės: ką reikia žinoti?'


def icon(name, cls='sgp-i'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


ARROW = icon('arrow')


class R:
    """Renderer for one service."""

    def __init__(self, svc, ctx):
        self.s, self.ctx, self.esc = svc, ctx, ctx['esc']
        self.by_slug = {x['slug']: x for x in ctx['services']}
        self.n = 0                      # waypoint counter (numbers continue down the page)
        self.specials = svc.get('specials') or []

    # ---------- small helpers
    def no(self):
        self.n += 1
        return f'{self.n:02d}'

    def wp(self, label, meta=''):
        m = f'<span class="sgp-mono sgp-wp__meta">{meta}</span>' if meta else ''
        return (f'<div class="sgp-wp"><span class="sgp-ring"></span><span class="sgp-mono sgp-wp__no">{self.no()}</span>'
                f'<span class="sgp-mono">{label}</span><span class="sgp-wp__rule"></span>{m}</div>')

    def sp(self, place):
        return [x for x in self.specials if x.get('place') == place]

    @staticmethod
    def img(mid, **o):
        opts = '|'.join(f'{k.replace("_", "-")}={v}' if v is not True else k for k, v in o.items())
        return '{{img:' + mid + ('|' + opts if opts else '') + '}}'

    def paras(self, items, cls=''):
        c = f' class="{cls}"' if cls else ''
        return ''.join(f'<p{c}>{t}</p>' for t in items)

    # ---------- submenu (T1b)
    def submenu(self):
        lis = ''.join(f'<li><a href="#{SUBMENU_IDS[l]}">{self.esc(l)}</a></li>' for l in self.s.get('submenu', []))
        return (f'<nav class="sgp-submenu sv-sub" aria-label="Puslapio skyriai" data-spy '
                f'data-salient="T1b Page Submenu (Sticky, below the header) · links = submenu labels · active = signal-ink + 2 px underline (M83)">'
                f'<div class="sgp-wrap"><ul class="sgp-mono">{lis}</ul></div></nav>')

    # ---------- T2 Faktai (spec sheet)
    def facts(self):
        s, e = self.s, self.esc
        kv = ''.join(f'<dt data-reveal>{e(r["k"])}</dt><dd data-reveal>{e(r["v"])}</dd>' for r in s.get('kv', []))
        routes = s.get('routes') or []
        chips = ''
        if routes:
            q = quote(s['name'])
            chips = ('<p class="sgp-mono sv-k">Kryptys ir paslaugos</p><ul class="sgp-chips sv-facts__chips" data-stagger="60">'
                     + ''.join(f'<li data-reveal><a class="sgp-chip" href="?domina={q}#uzklausa">{e(r)}</a></li>' for r in routes)
                     + '</ul>')
        return (
            f'<section class="sgp-sec sgp-sec--tight sv-facts on-light paper" id="faktai" data-theme="light" '
            f'data-salient="T2 Faktai · Row paper (sgp-light sgp-graticule) · Inner Row 7/12 Text Block .sgp-kv (rows fade up, 60 ms) + 5/12 Buttons (link chips → ?domina=…#uzklausa)">'
            f'<div class="sgp-wrap sgp-wrap--zone sv-facts__in">'
            f'<div class="sv-facts__kv"><p class="sgp-mono sv-k">Faktai</p><dl class="sgp-kv" data-stagger="60">{kv}</dl></div>'
            f'<div class="sv-facts__side">{chips}'
            f'<a class="sgp-lnk" href="#uzklausa">Gauti pasiūlymą{ARROW}</a></div>'
            f'</div></section>')

    # ---------- T3 01 Apie paslaugą
    def apie(self):
        s = self.s
        intro = s.get('intro') or []
        first = f'<p class="sv-apie__first" data-reveal>{intro[0]}</p>' if intro else ''
        rest = ''.join(f'<p data-reveal style="--dl:.08s">{t}</p>' for t in intro[1:])
        specials = ''.join(self.special(x) for x in self.sp('apie'))
        return (
            f'<section class="sgp-sec sv-apie on-light paper sgp-has-rail" id="apie-paslauga" data-theme="light" '
            f'data-salient="T3 Apie paslaugą · Row paper + sgp-has-rail · Column 4/12 Sticky Content (CSS, top 120) H2 + Column 8/12 Text Block (68ch, verbatim)">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp("Apie paslaugą")}'
            f'<div class="sv-apie__grid"><div class="sv-apie__side"><div class="sgp-sticky">'
            f'<h2 class="sgp-d2" data-split>Apie paslaugą</h2>'
            f'<p class="sgp-mono sv-apie__meta">{self.esc(s["no"])} / {len(self.ctx["services"]):02d} · {self.esc(s["name"])}</p>'
            f'</div></div><div class="sv-apie__txt sgp-prose">{first}{rest}</div></div>'
            f'{specials}{self.steps()}</div></section>')

    def steps(self):
        st = self.s.get('steps') or []
        if not st:
            return ''
        e, out = self.esc, []
        for i, x in enumerate(st):
            im = (f'<figure class="sgp-station__img">{self.img(x["img"], w=240, sizes="80px")}</figure>' if x.get('img') else '')
            link = ''
            if x.get('link'):
                link = f'<a class="sgp-lnk" href="{{{{url:{x["link"]["url"]}}}}}">{e(x["link"]["label"])}{ARROW}</a>'
            out.append(f'<li class="sgp-station" style="--i:{i}"><span class="sgp-ring"></span>{im}'
                       f'<p class="sgp-mono sgp-station__no">{i + 1:02d}</p><h3>{e(x["t"])}</h3><p>{e(x["d"])}</p>{link}</li>')
        title = self.s.get('steps_title') or 'Kaip tai vyksta'
        return (f'<div class="sv-steps" data-salient="„Kaip tai vyksta“ · Divider (2 px accent, line animation) as lane + {len(st)} Columns '
                f'(Fade In From Bottom 0/120/240) · Image Mask Circle (M55, M56)">'
                f'<p class="sgp-mono sv-k sv-steps__k">{e(title)}</p>'
                f'<ol class="sgp-stations sv-steps__lane" style="--n:{len(st)}"><li class="sgp-stations__lane" aria-hidden="true"></li>'
                f'{"".join(out)}</ol></div>')

    # ---------- T4 Privalumai — Sticky Media, Scrolling Content (M64)
    def why(self):
        s, e = self.s, self.esc
        blocks = s.get('why') or []
        if not blocks:
            return ''
        wm = s.get('why_media') or []
        ids, mids = [], []                           # unique media in order of use / media per block
        for b in blocks:
            mid = b.get('img') or wm[b.get('m', 0) % len(wm)]
            mids.append(mid)
            if mid not in ids:
                ids.append(mid)
        stack = ''.join(
            f'<figure class="sgp-grade sv-why__img{" is-active" if i == 0 else ""}" data-why-m="{i}">'
            f'{self.img(mid, w=1100, sizes="(min-width:1000px) 40vw, 1px", decorative=True)}<i class="sgp-ov"></i></figure>'
            for i, mid in enumerate(ids))
        items = []
        for i, b in enumerate(blocks):
            flag = f' data-salient="{e(b["flag"])}"' if b.get('flag') else ''
            rest = f' {b["t"]}' if b.get('t') else ''
            items.append(
                f'<article class="sv-why__b" data-why-i="{i}" data-why-m="{ids.index(mids[i])}"{flag}>'
                f'<figure class="sgp-grade sgp-ratio sv-why__inline" style="--ratio:16/10">'
                f'{self.img(mids[i], w=760, sizes="(max-width:999px) 92vw, 1px")}<i class="sgp-ov"></i></figure>'
                f'<p class="sgp-mono sv-why__no">{i + 1:02d} <span>/ {len(blocks):02d}</span></p>'
                f'<p class="sv-why__t" data-reveal><b>{b["b"]}</b>{rest}</p></article>')
        return (
            f'<section class="sgp-sec sv-why on-dark sgp-has-rail" id="privalumai" data-theme="dark" '
            f'data-salient="T4 Privalumai · Sticky Content Sections → Sticky Media, Scrolling Content (media 45 %, 80vh; crossfade + scale 1.06 → 1) · Text Blocks, first sentence bold · H2 Animated Text Word Reveal">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp("Privalumai", "Nuo durų iki durų")}'
            f'<div class="sv-why__grid"><div class="sv-why__media" aria-hidden="true"><div class="sv-why__stick">'
            f'<div class="sv-why__frame">{stack}</div>'
            f'<p class="sgp-mono sv-why__count"><span data-why-count>01</span> / {len(blocks):02d}</p></div></div>'
            f'<div class="sv-why__list"><h2 class="sgp-d2 sv-why__h" data-split>{e(s.get("why_h2") or WHY_H2)}</h2>'
            f'{"".join(items)}</div></div></div></section>')

    # ---------- specials
    def special(self, x):
        fn = getattr(self, 'sp_' + x['type'], None)
        if not fn:
            raise ValueError(f'{self.s["slug"]}: unknown special type {x["type"]!r}')
        return fn(x)

    def vctl(self, vid):
        return (f'<button class="sgp-vctl sgp-mono" type="button" data-video-toggle="{vid}" aria-pressed="false" '
                f'data-salient="Raw HTML video pause button (WCAG 2.2.2)">{icon("pause")}<span>Pauzė</span></button>')

    def sp_define(self, x):
        e = self.esc
        return (
            f'<div class="sv-define" data-salient="Special · Inner Row 5/7: Text Block (dark callout) + Self Hosted Video '
            f'(autoplay in view, muted, loop, no controls; desktop only, poster on phones) + pause button">'
            f'<div class="sv-define__card on-dark" data-reveal><p class="sgp-mono sv-define__k"><span class="sgp-ring sgp-ring--sm"></span>{e(x["k"])}</p>'
            f'<p class="sv-define__t">{e(x["text"])}</p></div>'
            f'<div class="sv-vid"><figure class="sgp-grade sgp-ratio sv-vid__fig" style="--ratio:16/10" data-mask>'
            f'{{{{bgvideo:{x["video"]}|id=svVideo|sd-only}}}}<i class="sgp-ov"></i></figure>'
            f'<div class="sv-vid__bar"><span class="sv-vid__cap">{{{{alt:{x["video"]}}}}}</span>{self.vctl("svVideo")}</div></div></div>')

    def sp_video(self, x):
        e = self.esc
        body = ''
        if x.get('quote'):
            body = f'<p class="sv-cine__q" data-split="blur">{e(x["quote"])}</p>'
        if x.get('chips'):
            body += ('<ul class="sgp-chips sgp-chips--lg sv-cine__chips" data-stagger="80">'
                     + ''.join(f'<li data-reveal>{e(c)}</li>' for c in x['chips']) + '</ul>')
        bw = ' sv-cine--bw' if x.get('bw') else ''
        return (
            f'<div class="sv-cine on-dark{bw}" data-salient="Special · Inner Row (dark, Full Width Content) · Self Hosted Video {x["video"]} '
            f'(autoplay in view, muted, loop; desktop only, poster on phones) · Parallax (Subtle) · overlay gradient · Text Color Light">'
            f'<div class="sv-cine__media" data-parallax="0.08" aria-hidden="true">{{{{bgvideo:{x["video"]}|id=svVideo|sd-only}}}}</div>'
            f'<div class="sv-cine__in"><p class="sgp-mono sv-cine__k"><span class="sgp-ring sgp-ring--sm"></span>{e(x["k"])}</p>{body}</div>'
            f'<div class="sv-cine__bar"><span class="sv-vid__cap">{{{{alt:{x["video"]}}}}}</span>{self.vctl("svVideo")}</div></div>')

    def sp_tags(self, x):
        e = self.esc
        return (f'<div class="sv-tags" data-salient="Special · Text Block label + Buttons (outline, large) = .sgp-chips--lg">'
                f'<p class="sgp-mono sv-k">{e(x["k"])}</p><ul class="sgp-chips sgp-chips--lg" data-stagger="90">'
                + ''.join(f'<li data-reveal>{e(t)}</li>' for t in x['items']) + '</ul></div>')

    def sp_bays(self, x):
        e = self.esc
        yours, others = x['legend']
        bays = ''.join(
            f'<g class="sv-bay{" sv-bay--you" if i == 1 else ""}" style="--i:{i}">'
            f'<rect x="{58 + i * 124}" y="58" width="112" height="112" rx="2"/>'
            + (f'<rect class="sv-bay__fill" x="{58 + i * 124}" y="58" width="112" height="112" fill="url(#sv-hatch)"/>' if i == 1 else
               ''.join(f'<rect class="sv-bay__box" x="{70 + i * 124 + bx}" y="{by}" width="{bw}" height="{bh}"/>'
                       for bx, by, bw, bh in ((0, 118, 44, 40), (48, 130, 40, 28), (8, 84, 32, 32))))
            + '</g>' for i in range(3))
        svg = (
            '<svg class="sv-van" viewBox="0 0 620 250" role="img" aria-labelledby="sv-van-t">'
            f'<title id="sv-van-t">{e(x["caption"])}</title>'
            '<defs><pattern id="sv-hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<line x1="0" y1="0" x2="0" y2="10" class="sv-hatch"/></pattern></defs>'
            '<path class="sv-van__road" d="M8 228 H612"/>'
            '<path class="sv-van__body" pathLength="1" d="M40 186 V44 a4 4 0 0 1 4 -4 H440 V186 Z"/>'
            '<path class="sv-van__cab" pathLength="1" d="M440 64 H520 L574 124 a8 8 0 0 1 2 6 V186 H440"/>'
            '<path class="sv-van__win" pathLength="1" d="M456 80 H512 L548 122 H456 Z"/>'
            f'{bays}'
            '<g class="sv-van__wheels"><circle cx="130" cy="200" r="24"/><circle cx="130" cy="200" r="8"/>'
            '<circle cx="492" cy="200" r="24"/><circle cx="492" cy="200" r="8"/></g>'
            '<g class="sv-van__tag"><path d="M238 58 V34"/><circle cx="238" cy="30" r="5"/></g>'
            '</svg>')
        return (
            f'<figure class="sv-bays" data-draw data-salient="Special „{e(x["title"])}“ · Raw HTML inline SVG (or Image) · CSS draw on enter · caption verbatim">'
            f'<div class="sv-bays__fig">{svg}</div>'
            f'<figcaption class="sv-bays__cap"><p class="sgp-mono sv-k">{e(x["title"])}</p><p class="sv-bays__t">{e(x["caption"])}</p>'
            f'<ul class="sv-bays__lg"><li><i class="sv-sw sv-sw--you"></i>{e(yours)}</li><li><i class="sv-sw"></i>{e(others)}</li></ul>'
            f'</figcaption></figure>')

    def sp_box(self, x):
        e = self.esc
        a, b, c = x['labels']
        svg = (
            f'<svg class="sv-box" viewBox="0 0 360 300" role="img" aria-labelledby="sv-box-t"><title id="sv-box-t">{e(x["caption"][0])}</title>'
            '<defs><pattern id="sv-fill" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.4" class="sv-dot"/>'
            '<circle cx="9" cy="9" r="1.4" class="sv-dot"/></pattern></defs>'
            # labels are 16 viewBox units (CSS) so they render >= 12 px (§2.3) down to a 360 px screen (svg ~297 px wide);
            # the box sits further left so the longest label („UŽPILDAS“) still ends inside the viewBox
            '<rect class="sv-box__gap" x="14" y="40" width="224" height="220" fill="url(#sv-fill)"/>'
            '<rect class="sv-box__outer" pathLength="1" x="14" y="40" width="224" height="220"/>'
            '<rect class="sv-box__inner" x="64" y="90" width="124" height="120"/>'
            '<g class="sv-box__dim"><path d="M14 150 H64"/><path d="M20 145 L14 150 L20 155 M58 145 L64 150 L58 155"/>'
            f'<text x="39" y="140" text-anchor="middle">{e(x["dim"])}</text></g>'
            f'<g class="sv-box__lbl"><path d="M238 60 H250"/><text x="255" y="66">{e(a)}</text>'
            f'<path d="M188 150 H250"/><text x="255" y="156">{e(b)}</text>'
            f'<path d="M213 240 H250"/><text x="255" y="246">{e(c)}</text></g>'
            '</svg>')
        return (
            f'<figure class="sv-guide" data-draw data-salient="Special „{e(x["title"])}“ · Raw HTML inline SVG (box section, 5 cm dimension line in red) · caption verbatim">'
            f'<p class="sgp-mono sv-k">{e(x["title"])}</p><div class="sv-guide__fig">{svg}</div>'
            f'<figcaption>{"".join(f"<p>{e(t)}</p>" for t in x["caption"])}</figcaption></figure>')

    def sp_callout(self, x):
        return (f'<p class="sgp-callout sgp-callout--line sv-callout" data-reveal data-salient="Special · Text Block + Extra Class .sgp-callout--line (red outline)">'
                f'<span class="sgp-callout__k sgp-mono">{self.esc(x["k"])}</span>{self.esc(x["text"])}</p>')

    def sp_note(self, x):
        e, l = self.esc, x['link']
        return (f'<div class="sv-note" data-reveal data-salient="Text Block + Button Underline → {e(l["label"])}">'
                f'<p class="sgp-mono sv-note__k">{icon("paw")}{e(x["k"])}</p><p>{e(x["text"])}</p>'
                f'<a class="sgp-lnk" href="{{{{url:{l["url"]}}}}}">{e(l["label"])}{ARROW}</a></div>')

    # ---------- special rows
    def row_head(self, x, lead=''):
        e = self.esc
        ld = f'<p class="sgp-lead" data-reveal>{lead}</p>' if lead else ''
        return f'<div class="sgp-head"><h2 class="sgp-d2" data-split>{e(x["h2"])}</h2>{ld}</div>'

    def sp_pack(self, x):
        e = self.esc
        glyphs = [
            '<path d="M8 16 L24 8 L40 16 V34 L24 42 L8 34 Z M8 16 L24 24 L40 16 M24 24 V42"/>',
            '<path d="M8 12 H40 V40 H8 Z"/><circle cx="16" cy="20" r="2"/><circle cx="26" cy="18" r="2"/><circle cx="33" cy="26" r="2"/><circle cx="18" cy="31" r="2"/><circle cx="29" cy="34" r="2"/>',
            '<path d="M8 14 H40 V38 H8 Z"/><path d="M8 22 H40 M8 30 H40" class="sv-g-red"/>',
            '<path d="M8 12 H40 V40 H8 Z"/><path d="M14 20 H30 M14 26 H34 M14 32 H24" class="sv-g-red"/>']
        items = ''.join(
            f'<li class="sgp-station" style="--i:{i}"><span class="sgp-ring"></span>'
            f'<svg class="sv-pack__g" viewBox="0 0 48 48" aria-hidden="true">{glyphs[i % 4]}</svg>'
            f'<p class="sgp-mono sgp-station__no">{i + 1:02d}</p><h3>{e(t["t"])}</h3><p>{e(t["d"])}</p></li>'
            for i, t in enumerate(x['items']))
        meta = str(len(x['items'])) + ' taisyklės'
        return (
            f'<section class="sgp-sec sv-pack on-light alt sgp-has-rail" id="{x["id"]}" data-theme="light" '
            f'data-salient="Special row „{e(x["h2"])}“ · Row paper-100 + sgp-has-rail · Divider lane + {len(x["items"])} Columns (numbered stops, Fade In 0/120/240/360) = .sgp-stations">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp(e(x["label"]), meta)}'
            f'{self.row_head(x, e(x["lead"]))}'
            f'<ol class="sgp-stations sv-pack__lane" style="--n:{len(x["items"])}"><li class="sgp-stations__lane" aria-hidden="true"></li>{items}</ol>'
            f'</div></section>')

    @staticmethod
    def _pcard_prog(i, n):
        # progress lane through the principles: rings filled up to this card (as .ab-card__prog on Apie įmonę)
        seg = lambda k: '<span class="sv-pcard__seg is-on"></span>' if k < i else '<span class="sv-pcard__seg"></span>'
        ring = lambda k: f'<span class="sgp-ring{" is-on" if k <= i else ""}"></span>'
        return ''.join(ring(k) + (seg(k) if k < n - 1 else '') for k in range(n))

    def sp_principles(self, x):
        e, n = self.esc, len(x['cards'])
        cards = ''.join(
            f'<article class="sgp-stack__item"><div class="sv-pcard">'
            f'<div class="sv-pcard__txt"><p class="sv-pcard__top" data-draw aria-hidden="true"><span class="sgp-ring"></span>'
            f'<span class="sgp-mono sv-pcard__no">{i + 1:02d}</span><span class="sv-pcard__rule"></span>'
            f'<span class="sgp-mono sv-pcard__of">{i + 1:02d} / {n:02d}</span></p>'
            f'<h3 class="sgp-h3">{e(c["t"])}</h3><p class="sv-pcard__p">{e(c["text"])}</p>'
            f'<p class="sv-pcard__prog" aria-hidden="true">{self._pcard_prog(i, n)}</p></div>'
            f'<figure class="sgp-grade sv-pcard__img">{self.img(c["img"], w=760, sizes="(min-width:1000px) 30vw, 92vw")}<i class="sgp-ov"></i></figure>'
            f'</div></article>' for i, c in enumerate(x['cards']))
        return (
            f'<section class="sgp-sec sv-princ on-dark sgp-has-rail" id="{x["id"]}" data-theme="dark" '
            f'data-salient="Special „{e(x["label"])}“ (replaces T4) · Sticky Content Sections → Sticky Scroll Pinned Sections, effect Stacking, Section Navigation off, off on tablet/phone (M63) · cards: index row (ring · mono no · hairline · n / 5) + H3 + verbatim paragraph + 5-ring progress lane (as Apie įmonę) + image 4:5 (45 %)">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp(e(x["label"]), f"{n} principai")}'
            f'{self.row_head(x, e(x["lead"]))}<div class="sgp-stack sv-princ__stack" data-stack>{cards}</div>'
            f'</div></section>')

    def sp_hotspots(self, x):
        e = self.esc
        marks, lis = [], []
        for i, h in enumerate(x['spots'], 1):
            marks.append(
                f'<button class="sv-hs__m" type="button" style="--x:{h["x"]}%;--y:{h["y"]}%" data-hs="{i}" aria-expanded="false" '
                f'aria-controls="sv-hs-tip-{i}" aria-label="{i} – {e(h["t"])}"><span aria-hidden="true">{i}</span></button>'
                f'<div class="sv-hs__tip" id="sv-hs-tip-{i}" role="tooltip" style="--x:{h["x"]}%;--y:{h["y"]}%" data-hs-tip="{i}">'
                f'<b>{e(h["t"])}</b> – {e(h["d"])}</div>')
            lis.append(f'<li data-hs-item="{i}" data-reveal><span class="sv-hs__n" aria-hidden="true">{i}</span>'
                       f'<span class="sv-hs__i">{icon(h["i"])}</span><span><b>{e(h["t"])}</b>{e(h["d"])}</span></li>')
        return (
            f'<section class="sgp-sec sv-hs on-light alt sgp-has-rail" id="{x["id"]}" data-theme="light" '
            f'data-salient="Special „{e(x["label"])}“ · Image With Hotspots (§4.26): image {x["img"]} 16:10 / 4:5 phone, 4 numbered markers (28 px, red, Nectar pulse ×2), tooltip hover/tap · list = Icon List">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp(e(x["label"]), "Salone")}'
            f'<div class="sv-hs__grid"><div class="sv-hs__side"><h2 class="sgp-d2" data-split>{e(x["h2"])}</h2>'
            f'<ol class="sv-hs__list" data-stagger="90">{"".join(lis)}</ol></div>'
            f'<figure class="sv-hs__fig"><div class="sv-hs__stage"><div class="sgp-grade sv-hs__img" data-mask>'
            f'{self.img(x["img"], w=1100, sizes="(min-width:1000px) 60vw, 92vw")}<i class="sgp-ov"></i></div>{"".join(marks)}</div>'
            f'<figcaption class="sgp-mono sv-hs__cap">{e(x["caption"])}</figcaption></figure></div>'
            f'</div></section>')

    def sp_kvrow(self, x):
        e = self.esc
        kv = ''.join(f'<dt data-reveal>{e(r["k"])}</dt><dd data-reveal>{e(r["v"])}</dd>' for r in x['kv'])
        return (
            f'<section class="sgp-sec sv-kvrow on-light paper sgp-has-rail" id="{x["id"]}" data-theme="light" '
            f'data-salient="Special „{e(x["h2"])}“ (replaces T6) · Row paper + sgp-has-rail · Column 5/12 Sticky H2 + Column 7/12 Text Block .sgp-kv (keys NEW, values verbatim)">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp(e(x["label"]))}'
            f'<div class="sv-split"><div class="sv-split__side"><div class="sgp-sticky"><h2 class="sgp-d2" data-split>{e(x["h2"])}</h2></div></div>'
            f'<div class="sv-split__main"><dl class="sgp-kv sv-kvbig" data-stagger="70">{kv}</dl></div></div>'
            f'</div></section>')

    def sp_checklist(self, x):
        e, n = self.esc, len(x['items'])
        items = []
        for i, it in enumerate(x['items']):
            iid = f'sv-chk-{i + 1}'
            items.append(
                f'<div class="sgp-acc__item sv-chk__item{" is-open" if i == 0 else ""}" id="{iid}">'
                f'<h3><button class="sgp-acc__btn" type="button" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="{iid}-p">'
                f'<span class="sgp-acc__no sgp-mono">{i + 1:02d}</span><span class="sgp-acc__t">{e(it["t"])}</span>'
                f'<span class="sgp-ring"></span></button></h3>'
                f'<label class="sv-chk__tick"><input type="checkbox" data-chk="{i + 1}">'
                f'<svg class="sv-chk__svg" viewBox="0 0 28 28" aria-hidden="true"><circle cx="14" cy="14" r="12" pathLength="1"/><path d="M8.5 14.5 L12.5 18.5 L19.5 10.5" pathLength="1"/></svg>'
                f'<span class="sgp-sr">Pažymėti kaip paruoštą: {e(it["t"])}</span></label>'
                f'<div class="sgp-acc__panel" id="{iid}-p"><div><div class="sgp-acc__body"><p>{it["text"]}</p></div></div></div></div>')
        c = x.get('callout')
        callout = (f'<p class="sgp-callout sv-chk__callout" data-reveal><span class="sgp-callout__k sgp-mono">{e(c["k"])}</span>{e(c["text"])}</p>'
                   if c else '')
        return (
            f'<section class="sgp-sec sv-chk on-light paper sgp-has-rail" id="{x["id"]}" data-theme="light" '
            f'data-salient="Special „{e(x["h2"])}“ · Toggle Panels → Animated Circle (multi-open), titles NEW, texts verbatim · demo checklist ticks = custom JS (localStorage, per visitor) · Callout .sgp-callout">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp(e(x["label"]), f"{n} žingsniai")}'
            f'<div class="sv-split"><div class="sv-split__side"><div class="sgp-sticky">'
            f'<h2 class="sgp-d2" data-split>{e(x["h2"])}</h2><p class="sgp-lead sv-chk__lead" data-reveal>{x["lead"]}</p>'
            f'<div class="sv-chk__meter" data-chk-meter><p class="sgp-mono"><span>Pasiruošta</span> <b data-chk-count>0</b> / {n}</p>'
            f'<span class="sv-chk__bar"><i data-chk-bar></i></span><span class="sgp-sr" role="status" data-chk-status></span></div>'
            f'{callout}</div></div>'
            f'<div class="sv-split__main"><div class="sgp-acc sv-chk__acc" data-acc="multi">{"".join(items)}</div></div></div>'
            f'</div></section>')

    def sp_price(self, x):
        e = self.esc
        ics = ['box', 'paw', 'route']
        tiles = ''.join(
            f'<li class="sv-price__tile" data-reveal><span class="sv-price__i">{icon(ics[i % 3])}</span>'
            f'<p class="sgp-mono sv-price__no">{i + 1:02d}</p><h3 class="sgp-h4">{e(t["t"])}</h3><p>{e(t["d"])}</p></li>'
            for i, t in enumerate(x['tiles']))
        return (
            f'<section class="sgp-sec sv-price on-dark sgp-has-rail" id="{x["id"]}" data-theme="dark" '
            f'data-salient="Special „{e(x["h2"])}“ · Row dark + sgp-has-rail · Text Block (verbatim) + 3 Columns (Fancy Box minimal: icon + NEW label + fragment) · Button Underline → #uzklausa">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp(e(x["label"]), "Individuali")}'
            f'{self.row_head(x, e(x["lead"]))}'
            f'<p class="sv-price__t" data-reveal>{e(x["text"])}</p>'
            f'<ul class="sv-price__tiles" data-stagger="120">{tiles}</ul>'
            f'<div class="sgp-btns sv-price__btns"><a class="sgp-btn sgp-btn--signal" href="#uzklausa"><span class="sgp-btn__l">Gauti pasiūlymą</span>'
            f'<span class="sgp-btn__a">{ARROW}</span></a><button class="sgp-a" type="button" popovertarget="sgp-call">Skambinti</button></div>'
            f'</div></section>')

    # ---------- T6 Kliento atsakomybės
    def resp(self):
        s, e = self.s, self.esc
        rs = s.get('responsibilities') or []
        aside = ''.join(self.special(x) for x in self.sp('aside'))
        end = ''.join(self.special(x) for x in self.sp('atsak-end'))
        if not rs and not aside:
            return ''
        lead = ''.join(f'<p class="sv-resp__lead" data-reveal>{t}</p>' for t in (s.get('resp_lead') or []))
        if len(rs) == 1:
            r = rs[0]
            main = (f'<div class="sgp-callout sv-resp__one" data-reveal data-salient="Text Block + Extra Class .sgp-callout (one responsibility → callout)">'
                    f'<span class="sgp-callout__k sgp-mono">{e(r["title"])}</span>{"".join(f"<p>{t}</p>" for t in r["text"])}</div>')
        else:
            items = []
            for i, r in enumerate(rs):
                iid = f'atsakomybe-{i + 1}'
                op = i == 0
                items.append(
                    f'<div class="sgp-acc__item{" is-open" if op else ""}" id="{iid}"><h3><button class="sgp-acc__btn" type="button" '
                    f'aria-expanded="{"true" if op else "false"}" aria-controls="{iid}-p"><span class="sgp-acc__no sgp-mono">{i + 1:02d}</span>'
                    f'<span class="sgp-acc__t">{e(r["title"])}</span><span class="sgp-ring"></span></button></h3>'
                    f'<div class="sgp-acc__panel" id="{iid}-p"><div><div class="sgp-acc__body">{"".join(f"<p>{t}</p>" for t in r["text"])}</div></div></div></div>')
            main = (f'<div class="sgp-acc sv-resp__acc" data-acc data-salient="Toggle Panels → Minimal Shadow (accordion, deep links #atsakomybe-N) · titles NEW, texts verbatim (M60)">'
                    f'{"".join(items)}</div>')
        return (
            f'<section class="sgp-sec sv-resp on-light paper sgp-has-rail" id="atsakomybes" data-theme="light" '
            f'data-salient="T6 Kliento atsakomybės · Row paper + sgp-has-rail · Column 5/12 Sticky Content (H2 + lead + special) + Column 7/12 Toggle Panels / callout">'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp("Kliento atsakomybės")}'
            f'<div class="sv-split"><div class="sv-split__side"><div class="sgp-sticky">'
            f'<h2 class="sgp-d2 sv-resp__h" data-split>{e(RESP_H2)}</h2>{lead}{aside}</div></div>'
            f'<div class="sv-split__main">{main}{end}</div></div></div></section>')

    # ---------- T7 Draudžiami daiktai
    def ban(self, shared):
        s, e = self.s, self.esc
        pr = s.get('prohibited')
        if not pr:
            return ''
        P = shared.get('prohibited_p') or {}
        if pr == 'P':
            pr = {'lead': [], 'items': 'P'}
        lead = ''.join(f'<p data-reveal>{t}</p>' for t in pr.get('lead') or [])
        items, is_p = pr.get('items'), False
        if items == 'P':
            is_p, items = True, P['items']
        plead = f'<p class="sv-ban__plead" data-reveal>{e(P["lead"])}</p>' if is_p else ''
        tail = f'<p class="sv-ban__tail sgp-mono">{e(pr["tail"])}</p>' if pr.get('tail') else ''
        note = ''.join(f'<p class="sv-ban__note" data-reveal>{t}</p>' for t in pr.get('note') or [])
        if is_p and P.get('note'):
            note += (f'<p class="sgp-callout sv-ban__resp" data-reveal><span class="sgp-callout__k sgp-mono">Svarbu</span>{e(P["note"])}</p>')
        xl = ''.join(f'<li data-reveal>{e(t)}</li>' for t in items)
        src = 'Tarptautiniai pervežimai: 8 bullets (shared.prohibited_p)' if is_p else 'service text, list split from the verbatim sentence'
        return (
            f'<section class="sgp-sec sv-ban on-dark sgp-has-rail sgp-has-media" id="draudziami" data-theme="dark" '
            f'data-salient="T7 Draudžiami daiktai · Row dark: bg image 4040619 + overlay 90 % + Parallax Subtle · Column 5/12 H2 + Text Block + fines teaser + Button · Column 7/12 Fancy Unordered List (✕, {src}; M62)">'
            f'<div class="sgp-bgmedia sv-ban__tex" data-parallax="0.14" aria-hidden="true">{self.img("4040619", w=1600, sizes="100vw", decorative=True)}</div>'
            f'<div class="sgp-wrap sgp-wrap--zone">{self.wp("Draudžiami daiktai", "Taisyklių 4.5 p.")}'
            f'<div class="sv-split"><div class="sv-split__side"><div class="sgp-sticky">'
            f'<h2 class="sgp-d2" data-split>Draudžiami daiktai</h2><div class="sv-ban__lead">{lead}</div>'
            f'<p class="sgp-callout sgp-callout--line sv-ban__fine" data-reveal><span class="sgp-callout__k sgp-mono">Baudos</span>'
            f'Radus draudžiamų daiktų – <strong>1200 EUR</strong> bauda (Taisyklių 4.5 p.)</p>'
            f'<div class="sgp-btns"><a class="sgp-btn sgp-btn--line sgp-btn--sm" href="{{{{url:taisykles}}}}"><span class="sgp-btn__l">Visos taisyklės</span>'
            f'<span class="sgp-btn__a">{ARROW}</span></a></div></div></div>'
            f'<div class="sv-split__main">{plead}<ul class="sgp-xlist sv-ban__list" data-stagger="40">{xl}</ul>{tail}{note}</div></div>'
            f'</div></section>')

    # ---------- statement before the board (gyvūnai)
    def statement(self):
        st = self.s.get('statement')
        if not st:
            return ''
        m = re.match(r'(.+?[.!?])\s+(.*)', st)
        first, rest = (m.group(1), m.group(2)) if m else (st, '')
        return (
            f'<section class="sgp-sec sgp-sec--tight sv-state on-light alt" data-theme="light" '
            f'data-salient="Row paper-100 · Text Block (statement, verbatim) + Button (opens the switchboard popover)">'
            f'<div class="sgp-wrap sgp-wrap--zone sv-state__in"><p class="sgp-statement sv-state__t" data-split>{self.esc(first)}</p>'
            f'<div class="sv-state__r"><p data-reveal>{self.esc(rest)}</p>'
            f'<button class="sgp-btn sgp-btn--signal" type="button" popovertarget="sgp-call" data-reveal style="--dl:.1s">'
            f'<span class="sgp-btn__l">{icon("phone")}Skambinti</span></button></div></div></section>')

    # ---------- T9 closing + call + related services
    def closing(self):
        s, e = self.s, self.esc
        txt = s.get('closing') or ''
        for ph in s.get('closing_marks') or []:
            txt = txt.replace(ph, f'<mark class="sgp-mark">{ph}</mark>', 1)
        more = f'<p class="sv-close__more" data-reveal style="--dl:.15s">{e(s["closing_more"])}</p>' if s.get('closing_more') else ''
        cards = []
        for i, sl in enumerate(s.get('related') or []):
            r = self.by_slug[sl]
            hv, video = '', ''
            if r.get('hover_video'):
                hv = f' data-hover-video="{{{{videourl:{r["hover_video"]}|q=sd}}}}"'
                video = '<video muted loop playsinline preload="none" aria-hidden="true" tabindex="-1"></video>'
            cards.append(
                f'<a class="sgp-card sv-rel__card" href="{{{{url:{sl}}}}}"{hv} data-reveal>'
                f'<figure class="sgp-card__img sgp-grade">{self.img(r["card_media"], w=760, sizes="(min-width:1000px) 28vw, (min-width:691px) 45vw, 92vw", pos=r.get("card_crop", "50% 50%"))}'
                f'<i class="sgp-ov"></i>{video}</figure>'
                f'<div class="sgp-card__body"><p class="sgp-card__no sgp-mono">{r["no"]} / {len(self.ctx["services"]):02d}</p>'
                f'<h3 class="sgp-card__t">{e(r["name"])}</h3><p class="sgp-card__s">{e(r.get("card", ""))}</p>'
                f'<span class="sgp-card__go">{ARROW}</span></div></a>')
        rel = ''
        if cards:
            rel = (f'<div class="sv-rel" data-salient="Inner Row · 3 × Column Link cards (image 16:11 + index + H3 + summary; hover M32, hover video M33)">'
                   f'<div class="sv-rel__head"><h2 class="sgp-mono sv-rel__h">Susijusios paslaugos</h2>'
                   f'<a class="sgp-lnk" href="{{{{url:paslaugos}}}}">Visos paslaugos{ARROW}</a></div>'
                   f'<div class="sgp-cols sv-rel__grid" style="--cols:3" data-stagger="120">{"".join(cards)}</div></div>')
        return (
            f'<section class="sgp-sec sv-close on-light paper" data-theme="light" '
            f'data-salient="T9 Uždarymas · Row paper · Highlighted Text (Regular Underline #EF4539 3 px, 2 phrases, M23) + 2 × Button .sgp-callbtn · related services">'
            f'<div class="sgp-wrap sgp-wrap--zone"><div class="sv-close__in"><div class="sv-close__txt">'
            f'<p class="sgp-statement sv-close__t" data-reveal>{txt}</p>{more}</div>'
            f'<div class="sv-close__calls">{{{{partial:phero-calls}}}}'
            f'<p class="sv-close__links"><a class="sgp-lnk" href="{{{{url:grafikas}}}}">Pervežimų grafikas{ARROW}</a>'
            f'<a class="sgp-lnk" href="{{{{url:kontaktai}}}}">Kontaktai{ARROW}</a></p></div></div>{rel}</div></section>')

    # ---------- assemble
    def body(self, shared):
        rows = [self.apie()]
        whyrow = self.sp('why')
        rows.append(''.join(self.special(x) for x in whyrow) if whyrow else self.why())
        rows += [self.special(x) for x in self.sp('row')]
        rows += [self.resp(), self.ban(shared), self.statement()]
        return '\n'.join(r for r in rows if r)


def blocks(svc, ctx):
    shared = ctx.get('shared') or {}   # tools/build.py passes paslaugos.json → shared in ctx
    r = R(svc, ctx)
    body = r.body(shared)
    return {
        'submenu_html': r.submenu(),
        'facts_html': r.facts(),
        'body_html': body,
        'closing_html': r.closing(),
    }
