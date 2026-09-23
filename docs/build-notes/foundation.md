# SGP v2 — Foundation: conventions for page teams

Owner: Foundation agent. Source of truth for design: `docs/dizaino-sistema.md` (this file explains **how the demo code works**; when they disagree on design, the design system wins; when they disagree on code conventions, this file wins).

---

## 0. TL;DR for a page team

```bash
# from the repo root (…/sgp-pervezimai)
python3 tools/build.py apie-imone          # build ONLY your pages (prefix of the output path)
python3 tools/check.py apie-imone          # check ONLY your pages (links into other pages still resolve)
python3 -m http.server 8765 --bind 127.0.0.1   # preview: http://127.0.0.1:8765/apie-imone/
python3 tools/build.py && python3 tools/check.py   # full build + check before you hand off (must print 0 errors)
```

1. Edit **only** your files: `src/pages/<your-page>.html`, `assets/css/pages/<your-page>.css`, `assets/js/pages/<your-page>.js` (+ services team: `src/templates/paslauga.html`, `src/templates/paslauga.py`, the content fields of `src/data/paslaugos.json`).
2. **Never edit** shared files: `tools/*`, `src/partials/*`, `src/data/grafikas.json`, `assets/css/{tokens,base,components,motion}.css`, `assets/js/sgp.js`, `assets/img/*`, `src/pages/index.html` (home). Need a change? Write a **REQUEST** in `docs/build-notes/<team>.md` (what, why, where, proposed code).
3. Never edit the generated `*.html` at the repo root or in page folders — they are overwritten by the build.
4. Use the shared components/data attributes below before writing new CSS/JS. Page-owned classes get a page prefix (§8).
5. Copy: verbatim from `docs/turinys-*.md` / the blueprint in `dizaino-sistema.md §6`. Fix obvious typos only, and list every fix + every NEW string in your build notes.

---

## 1. Directory map

| Path | What | Owner |
|---|---|---|
| `tools/build.py` | stdlib static generator (front matter → partials → placeholders → files) | Foundation |
| `tools/check.py` | built-site checker (links, ids, alt, tel, lang, h1, meta, placeholders, nesting, Pexels ids) | Foundation |
| `src/partials/*.html` | layout, head, sprite, header (ticker + nav + mega + switchboard + menu), footer, callbar (+ cookie + dev toggle), scripts, arrival (GS-Arrival), board / board-inner (GS-Board), phero-calls, map-ie / map-es / map-both | Foundation |
| `src/data/grafikas.json` | schedule: 4 routes × ISO dates, phones per direction, `render_today` | Foundation (client data) |
| `src/data/paslaugos.json` | 11 services + 6 groups. Foundation filled ids/titles/meta/lead/cards/media; **services team fills the content fields** | shared (see §6) |
| `src/pages/*.html` | one source file per page (front matter + body) | page teams |
| `src/templates/paslauga.html` (+ optional `paslauga.py`) | the one template → 11 service pages | services team |
| `assets/css/tokens.css` | §2.1 tokens verbatim + surfaces | Foundation |
| `assets/css/base.css` | reset, type roles, layout, grade/media | Foundation |
| `assets/css/components.css` | every shared component (§4 below) | Foundation |
| `assets/css/motion.css` | data-attribute motion states, view transition, reduced motion | Foundation |
| `assets/css/pages/<page>.css` | page-owned CSS | page teams |
| `assets/js/sgp.js` | shared runtime (one IIFE, `window.SGP`) | Foundation |
| `assets/js/pages/<page>.js` | page-owned JS (loaded after sgp.js) | page teams |
| `assets/img/logo.svg`, `logo_light.svg`, `favicon.svg` | brand | Foundation |

Output paths (all relative links; GitHub Pages serves the repo root at `https://arvydastry.github.io/sgp-pervezimai/`):

| Source | Output | `nav` key | url key |
|---|---|---|---|
| `src/pages/index.html` | `index.html` | `pradzia` | `pradzia` |
| `src/pages/apie-imone.html` | `apie-imone/index.html` | `apie` | `apie` |
| `src/pages/pervezimo-paslaugos.html` | `pervezimo-paslaugos/index.html` | `paslaugos` | `paslaugos` |
| `src/pages/tarptautiniai-pervezimai.html` | `pervezimo-paslaugos/tarptautiniai-pervezimai/index.html` | `tarptautiniai` | `tarptautiniai` |
| `src/templates/paslauga.html` × 11 | `pervezimo-paslaugos/tarptautiniai-pervezimai/<slug>/index.html` | `paslauga` | `<slug>` |
| `src/pages/pervezimu-grafikas.html` | `pervezimu-grafikas/index.html` | `grafikas` | `grafikas` |
| `src/pages/siuntos-sekimas.html` | `siuntos-sekimas/index.html` | `sekimas` | `sekimas` |
| `src/pages/taisykles.html` | `taisykles/index.html` | `taisykles` | `taisykles` |
| `src/pages/kontaktai.html` | `kontaktai/index.html` | `kontaktai` | `kontaktai` |
| `src/pages/privatumo-politika.html` | `privatumo-politika/index.html` | `privatumas` | `privatumas` |
| `src/pages/404.html` | `404.html` | `none` | `404` |

Extra url keys: `v1` (old demo), `pdf` (the live „sutartis su siuntėju“ PDF, absolute URL). Service slugs: `kroviniu-pervezimas`, `negabaritiniu-kroviniu-pervezimas`, `daliniu-kroviniu-gabenimas`, `daiktu-pervezimas`, `automobiliu-pervezimas`, `motociklu-pervezimas`, `keleiviu-pervezimas`, `gyvunu-pervezimas`, `siuntu-pervezimas`, `siuntu-pristatymas`, `perkraustymo-paslaugos`.

---

## 2. Page source format

```html
---
title: Apie įmonę | sgp-pervezimai.lt
description: „SGP“ – esame įmonė įsikūrusi Lietuvoje, … (plain text, no quotes needed)
out: apie-imone/index.html
body_class: page-apie
nav: apie
og_image: 9989463
hero_media: 9989463
css: pages/apie.css
js: pages/apie.js
arrival: yes
salient: Page „Apie įmonę“ (§6.2) · short note for the WP developer
---
<section class="sgp-phero on-dark" …>…</section>
<section class="sgp-sec on-light paper sgp-has-rail" …>…</section>
```

| Key | Required | Meaning |
|---|---|---|
| `title` | yes | `<title>` (§6.12). `og:title` = the part before ` | `. |
| `description` | yes | meta description (§6.12). |
| `out` | yes | output path relative to repo root (table above). |
| `body_class` | no | classes on `<body>` (use `page-<name>`). |
| `nav` | no | active menu key → `aria-current="page"` on that item; parents get `aria-current="true"` (`paslauga` → `tarptautiniai` + `paslaugos`; `tarptautiniai` → `paslaugos`). |
| `og_image` | no | a media id from `docs/media.json` (photo or video → poster), 1200 w. Default = hero poster 29374299. |
| `hero_media` | no | media id of the above-the-fold image/poster → `<link rel="preload" imagesrcset …>` (LCP). Omit for texture/plain heroes. |
| `css`, `js` | no | page files, relative to `assets/css/` / `assets/js/`. Comma list or `[a, b]`. They load **after** the shared files. The build fails if a file is missing. Links get `?v=<content hash>` automatically. |
| `arrival` | no | `no` hides GS-Arrival (the „Atvykimas“ CTA before the footer, id `uzklausa`). Default yes. Hidden on kontaktai, privatumo-politika, 404. |
| `salient` | no | emitted as an HTML comment at the top of `<main>`. |
| `vendor` | no | `flickity` and/or `anime` → pinned jsdelivr files (see §7). |
| `root` | 404 only | `/sgp-pervezimai/` — absolute links for GitHub Pages' 404 (see §10). |

The build wraps your body with: `<head>` (meta, fonts, Lenis css, shared + page css) → sprite → skip link + header (ticker, nav, mega menu, switchboard popover `#sgp-call`, off-canvas menu `#sgp-menu`) → `<main id="main">` your body + GS-Arrival → footer → call bar + cookie bar + „Salient žymės“ button → `window.SGP_SCHEDULE` + Lenis + `sgp.js` + your js.

**One `<h1>` per page, `lang="lt"`, no ids that collide with shared ids** (`sgp-hdr`, `sgp-call`, `sgp-menu`, `sgp-cookie`, `sgp-tagbtn`, `main`, `uzklausa`, `mie-t/mie-d`, `mes-t/mes-d`, `mboth-t/mboth-d`). Top-level rows go directly inside `<main>` as `<section>` (the header recolours by probing `main > section`).

---

## 3. Placeholders (expanded by `tools/build.py`, recursive, any order)

| Placeholder (`\|` in the raw file = a pipe) | Output |
|---|---|
| `{{root}}` | relative prefix for the page depth: `./`, `../`, `../../`, `../../../` (404: `/sgp-pervezimai/`). Use for assets: `{{root}}assets/img/logo.svg`. |
| `{{url:<key>}}` | link to a page (keys in §1), e.g. `{{url:grafikas}}` → `../pervezimu-grafikas/`, `{{url:keleiviu-pervezimas}}`. Append fragments/queries after it: `{{url:taisykles}}#baudos`, `{{url:pradzia}}#uzklausa`. **Never hard-code relative paths.** |
| `{{partial:<name>}}` | include `src/partials/<name>.html`. Useful ones for pages: `board` (GS-Board section), `board-inner` (board without the section), `phero-calls` (hero call ticket), `map-ie`, `map-es`, `map-both`, `arrival` (auto-added; don't include manually). |
| `{{grafikas:<variant> [args]}}` | schedule markup = the planned `[sgp_grafikas]` shortcode (see §5). |
| `{{paslaugos:<variant>}}` | `cards` (home road), `list` (GS-ServiceList), `footer`, `options` (form `<option>`s + „Kita“), `mega`, `groups` + `group-index` (/pervezimo-paslaugos/ stacked group cards + sticky index, from `groups[]` incl. `lead`). Mega/footer links of the current service get `aria-current="page"`. |
| `{{img:<id>\|opt\|opt…}}` | `<img>` from `docs/media.json` with `srcset` (480/760/1100/1600/1920 ≤ 2×w), `sizes`, `width`/`height`, `alt_lt`, `loading="lazy"`, `decoding="async"`. Options: `w=760` (default 1100), `sizes=(min-width:1000px) 33vw, 100vw`, `pos=50% 60%` (object-position = crop), `eager` (above the fold), `decorative` (alt=""), `alt=…` (override), `class=…`, `id=…`, `data-parallax=0.06`. |
| `{{bgvideo:<id>\|id=myVideo\|pos=50% 50%\|eager\|sd-only}}` | background video pair: poster `<img srcset>` (phones see only this) + lazy `<video data-bgvideo>` (desktop ≥1000, loads when near, fades in over the poster, pauses off-screen). Give it an `id` and add a pause control (§4.20). Put it inside `.sgp-bgmedia`. |
| `{{photo:<id>\|w=1600}}` / `{{poster:<id>\|w=1280}}` / `{{videourl:<id>\|q=sd}}` / `{{alt:<id>}}` | bare URL / alt text (escaped for attributes). |
| `{{svc:<field>}}` | service template only (§6). |
| `{{page:…}}`, `{{nav:…}}` | used by partials; pages don't need them. |

An unknown key, a media id not in `docs/media.json`, or any leftover `{{ }}` fails the build/check.

---

## 4. Layout & components (all in the shared CSS; copy the snippets)

### 4.1 Rows, surfaces, container, rail
```html
<section class="sgp-sec on-light paper sgp-has-rail" id="imone" data-salient="Row · Extra Class sgp-light sgp-graticule sgp-has-rail · Text Color Dark">
  <div class="sgp-wrap sgp-wrap--zone">
    <div class="sgp-wp"><span class="sgp-ring"></span><span class="sgp-mono sgp-wp__no">01</span><span class="sgp-mono">Įmonė</span><span class="sgp-wp__rule"></span><span class="sgp-mono sgp-wp__meta">LT ⇄ IE · LT ⇄ ES</span></div>
    <div class="sgp-head">
      <h2 class="sgp-d2" data-split>Heading, sentence case</h2>
      <p class="sgp-lead" data-reveal>Lead paragraph (right column ≥1000, below on phones).</p>
    </div>
    …content…
  </div>
</section>
```
- Surfaces: `on-dark` (asphalt-900) / `on-light` (paper-50) + modifiers `on-light alt` (paper-100), `on-dark deep` (asphalt-950), `paper` (graticule; on dark it becomes 4 % white). They set `--bg --fg --fg-2 --hair --hair-2 --ghost --red-text --card --card-h` — **use these variables in page CSS, not raw colours**. Alternate dark/light rows. Red ≤ ~5 % of a viewport; small red text = `var(--red-text)`.
- Always add `data-theme="dark|light"` or rely on the `on-dark/on-light` class — the header recolours from it.
- `sgp-sec` = section padding (`--section-y`); `sgp-sec--tight` smaller. `sgp-wrap` = 1320 container with gutter; `sgp-wrap--zone` adds the 72 px rail zone (≥1000). Grids: `sgp-grid` (12 cols) or `<div class="sgp-cols" style="--cols:3">` (auto 2 → 1 on smaller screens). `sgp-sticky` = sticky column (top 120, static <1000).
- **Rail:** add `sgp-has-rail` to a row → the lane draws itself on scroll (CSS only). The rail **owns `::before` of that row — never put an overlay/pseudo on `::before` of a rail row** (use `::after` or a child). Waypoint rings sit on the rail automatically. `sgp-rail-end` + `data-rail-end` on the terminus waypoint stops the lane (used by GS-Arrival).
- Waypoint (`sgp-wp`): number + short label (mono, ≤ 4 words) + optional meta (short fact only; hidden ≤560 px). Terminus variant: `sgp-wp sgp-wp--end`.
- Rows with background media: add `sgp-has-media` (isolation + clip) and a child `<div class="sgp-bgmedia" data-parallax="0.14" aria-hidden="true">{{img:4040619|w=1600|sizes=100vw|decorative}}</div>`; set the image opacity/overlay in your page CSS (texture rows: `.x .sgp-bgmedia img{opacity:.1}`).

### 4.2 Type roles (§2.3)
`sgp-d2` chapter H2 · `sgp-statement` · `sgp-h3` · `sgp-h4` · `sgp-lead` · `sgp-body` · `sgp-small` · `sgp-mono` (12 px mono label, ≤4 words, UPPERCASE via CSS) · `sgp-fg2` (secondary colour) · `sgp-red` · `sgp-prose` (68ch paragraphs with spacing, underlined links) · `sgp-a` (inline underline link/button) · `sgp-sr` (screen-reader only). Nothing below 12 px. Inner-page H1 = `sgp-phero__h1`.

### 4.3 Inner page hero „Maršruto antraštė“ (§4.17)
```html
<section class="sgp-phero on-dark" data-theme="dark" data-salient="Row Full Width · Route header · BG photo + Parallax Subtle + Slight Zoom Out Reveal · overlay · Text Color Light">
  <div class="sgp-bgmedia" data-parallax="0.12" aria-hidden="true">{{img:9989463|w=1920|sizes=100vw|eager|decorative|pos=50% 60%}}</div>
  <div class="sgp-wrap sgp-wrap--zone sgp-phero__in">
    <div class="sgp-phero__copy">
      <nav class="sgp-crumbs" aria-label="Kelias"><ol><li><a href="{{url:pradzia}}">Pradžia</a></li><li aria-current="page">Apie įmonę</li></ol></nav>
      <p class="sgp-phero__eyebrow sgp-mono"><span class="sgp-ring"></span>Saugiai greitai patikimai</p>
      <h1 class="sgp-phero__h1" data-split>Apie įmonę</h1>
      <p class="sgp-phero__lead sgp-lead" data-reveal style="--dl:.3s">SGP – visos pervežimo paslaugos</p>
      <ul class="sgp-chips" data-reveal style="--dl:.4s"><li>Chip</li></ul>   <!-- optional -->
      {{grafikas:next}}                                                     <!-- phones only (<1000) -->
    </div>
    {{partial:phero-calls}}                                                 <!-- both LT call buttons (right column ≥1000) -->
  </div>
</section>
```
Variants (add to `sgp-phero`): `sgp-phero--compact` (44svh), `sgp-phero--texture` (image at 18 % — use with `--compact`), `sgp-phero--plain paper` (no media, graticule; drop the `sgp-bgmedia` div). Video variant: `<div class="sgp-bgmedia" data-parallax="0.12" aria-hidden="true">{{bgvideo:13707149|id=pheroVideo|eager}}</div>` + control `<div class="sgp-wrap sgp-phero__vc"><button class="sgp-vctl sgp-mono" type="button" data-video-toggle="pheroVideo" aria-pressed="false"><svg class="sgp-i" aria-hidden="true"><use href="#i-pause"/></svg><span>Pauzė</span></button></div>` as the last child of the section. Stamp line (grafikas): `<p class="sgp-stamp sgp-mono">{{grafikas:updated}}</p>`. Don't add `sgp-has-rail` to a hero (its overlay uses `::before`).

### 4.4 Buttons & links (§4.4)
```html
<a class="sgp-btn sgp-btn--signal" href="{{url:grafikas}}"><span class="sgp-btn__l">Pervežimų grafikas</span><span class="sgp-btn__a"><svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg></span></a>
<a class="sgp-btn sgp-btn--line sgp-btn--sm" href="…"><span class="sgp-btn__l">Visos taisyklės</span></a>
<a class="sgp-lnk" href="{{url:apie}}">Skaityti daugiau<svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg></a>
<a class="sgp-lnk sgp-lnk--plain" href="{{url:pdf}}" rel="noopener">Atsisiųsti sutartį su siuntėju (PDF, 72 KB)<svg class="sgp-i" aria-hidden="true"><use href="#i-dl"/></svg></a>
<div class="sgp-btns">…buttons in a wrapping row…</div>
<button class="sgp-ico" type="button" aria-label="…"><svg class="sgp-i" aria-hidden="true"><use href="#i-close"/></svg></button>
```
Call buttons (phone first):
```html
<a class="sgp-callbtn" href="tel:+37065053161" aria-label="Pervežimai į Airiją – skambinti +370 650 53161"><span class="sgp-callbtn__i"><svg class="sgp-i" aria-hidden="true"><use href="#i-phone"/></svg></span><span class="sgp-callbtn__t"><span class="sgp-mono">Pervežimai į Airiją</span><span class="sgp-callbtn__n">+370 650 53161</span></span></a>
```
`sgp-callbtn--sm` = 56 px. Open the switchboard (all 5 numbers) from anywhere: `<button class="sgp-a" type="button" popovertarget="sgp-call">Skambinti</button>` (or a link `href="#sgp-call"`).
Icons (sprite, `<svg class="sgp-i" aria-hidden="true"><use href="#i-NAME"/></svg>`): `phone arrow menu close pause play mail copy cal seat heat air shield rest box route paw dl search x`.

**The only allowed tel: hrefs** (check.py enforces): `+37065053161` (LT, Airija), `+353864503104` (IE), `+447566878681` (UK), `+37063828919` (LT, Ispanija), `+34602547929` (ES). Display format: `+370 650 53161`, `+353 86 450 3104`, `+44 7566 878681`, `+370 638 28919`, `+34 602 547 929`. Every tel link gets a full `aria-label` naming the direction. Phone lists: `<div class="sgp-phl"><a href="tel:…" aria-label="…"><span class="sgp-cc">LT</span>+370 650 53161</a>…</div>`.

### 4.5 Chips, datasheet, fines, lists, callouts, clauses
```html
<ul class="sgp-chips"><li>Nuo durų iki durų</li><li>Kroviniai apdrausti</li></ul>
<ul class="sgp-chips"><li><a class="sgp-chip" href="?domina=Krovinių%20pervežimas#uzklausa">Krovinių pervežimas į Airiją</a></li></ul>   <!-- link chips, 44 px -->
<ul class="sgp-chips sgp-chips--lg"><li>Langai</li><li>Žoliapjovės</li></ul>                                                    <!-- big outline tags -->
<dl class="sgp-kv" data-reveal><dt>Kelyje</dt><dd>apie 3–4 paros nuo paėmimo dienos</dd><dt>Įsipareigojimas siuntoms</dt><dd>per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklių 3.4 p.)</dd></dl>
<dl class="sgp-kv sgp-kv--fines"><dt class="sgp-kv__hd">Radus siuntoje ar krovinyje</dt><dd class="sgp-kv__hd sgp-mono">Bauda</dd>
  <dt>Alkoholinių gėrimų</dt><dd><strong>1200 EUR</strong>už kiekvieną alkoholinio gėrimo vienetą</dd></dl>
<ul class="sgp-xlist"><li>bet kokie tabako gaminiai</li>…</ul>          <!-- ✕ list, 2 cols ≥691; sgp-xlist--1 one col; sgp-xlist--num numbered 01… -->
<ul class="sgp-list"><li>ring-bullet list item</li></ul>
<p class="sgp-callout"><span class="sgp-callout__k sgp-mono">Svarbu</span>Už siuntinio turinį atsakingas siuntėjas.</p>   <!-- sgp-callout--line = red outline variant -->
<div class="sgp-clause"><span class="sgp-clause__no">3.4.</span><p class="sgp-clause__t">Vežėjas įsipareigoja …</p></div>
<div class="sgp-clause"><span class="sgp-clause__no">6.1.</span><div class="sgp-clause__t"><p>…</p><ol>…</ol></div></div>   <!-- multi-paragraph clause; number above the text ≤560 px -->
```
Delivery facts (always the pair, §4.12) = the `sgp-kv` above. Crop marks: wrap the image frame — `<div class="sgp-crop"><figure class="sgp-grade">{{img:…}}<i class="sgp-ov"></i></figure></div>` (never on the same element as `sgp-grade`, which clips). Only the two slots listed in §2.8 get crop marks.

### 4.6 Images
`<figure class="sgp-grade sgp-grade--hover sgp-ratio" style="--ratio:4/5">{{img:…}}<i class="sgp-ov"></i></figure>` = graded image, fixed ratio (no CLS), hover zoom + overlay fade (M44). Card image ratio 16:11, panels 16:10, portraits 4:5, insets 4:3, circles 80 px (`sgp-station__img`). Alt comes from media.json; textures `decorative`.

### 4.7 Schedule blocks (data from `grafikas.json`, never type dates by hand)
```html
{{partial:board}}                                   <!-- GS-Board: dark row + „Artimiausi pervežimai“ head + 4 tap-to-call cells + split-flap -->
{{grafikas:timetable kryptis=ie}}                   <!-- outputs its own <ul class="sgp-tt">: light timetable rows (lt-ie + ie-lt) -->
{{grafikas:timetable}}                              <!-- all 4 routes (labels „Į Airiją“/„Į Ispaniją“/„Iš Airijos“/„Iš Ispanijos“) -->
{{grafikas:table}}                                  <!-- /pervezimu-grafikas/ table grouped „Iš Lietuvos“ / „Į Lietuvą“ -->
{{grafikas:table kryptis=es}}                       <!-- filtered (Tabs „Visi · Airija · Ispanija“) -->
<div class="sgp-tickets">{{grafikas:stubs}}</div>   <!-- the two ticket cards LT ⇄ IE / LT ⇄ ES with next-departure stubs (§3.9) -->
{{grafikas:next}}                                   <!-- phone-only „Artimiausias išvykimas“ line (links to the schedule) -->
<p class="sgp-stamp sgp-mono">{{grafikas:updated}}</p>   <!-- „Atnaujinta rugsėjo 23 d.“ -->
{{grafikas:note}}                                   <!-- „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“ -->
```
Details in §5. `{{grafikas:table}}` route codes are split-flap tiles (`data-flap`, M14: desktop, once, when the row first comes into view — also inside tab panels).

### 4.8 Cards (generic link card)
```html
<div class="sgp-cols" style="--cols:3" data-stagger="120">
  <a class="sgp-card" href="{{url:grafikas}}" data-reveal>
    <figure class="sgp-card__img sgp-grade">{{img:36383706|w=760|sizes=(min-width:1000px) 30vw, 100vw}}<i class="sgp-ov"></i></figure>
    <div class="sgp-card__body"><p class="sgp-card__no sgp-mono">01</p><h3 class="sgp-card__t">Pervežimų grafikas</h3><p class="sgp-card__s">One-line summary.</p><span class="sgp-card__go"><svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg></span></div>
  </a>
</div>
```
Uses `--card/--card-h/--hair` so it works on dark and light rows. Ratio via `style="--ratio:4/3"` on `sgp-card__img`. Tilt (M67), group stacks (§4.8 of the design) etc. are page-owned styling on top.

### 4.9 Stations lane (process / 3–4 stop lanes, M55–M56; vertical below 1000)
```html
<ol class="sgp-stations" style="--n:3">
  <li class="sgp-stations__lane" aria-hidden="true"></li>
  <li class="sgp-station" style="--i:0"><span class="sgp-ring"></span><figure class="sgp-station__img">{{img:6407553|w=240|sizes=80px}}</figure><p class="sgp-mono sgp-station__no">01</p><h3>Paėmimas</h3><p>…</p></li>
  <li class="sgp-station" style="--i:1"><span class="sgp-ring"></span><p class="sgp-mono sgp-station__no">02</p><h3>…</h3><p>…</p></li>
</ol>
```
Draws when it enters (no attribute needed). The circle image is optional. `--n` = number of stations.

### 4.10 Accordion = Toggle Panels (M60, M62; deep links)
```html
<div class="sgp-acc" data-acc>                                   <!-- data-acc="multi" = several open -->
  <div class="sgp-acc__item is-open" id="draudziama-siusti">    <!-- item id = deep link (#draudziama-siusti opens it) -->
    <h3><button class="sgp-acc__btn" type="button" aria-expanded="true" aria-controls="acc-draudziama"><span class="sgp-acc__no sgp-mono">01</span><span class="sgp-acc__t">Draudžiama siųsti <small>(12)</small></span><span class="sgp-ring"></span></button></h3>
    <div class="sgp-acc__panel" id="acc-draudziama"><div><div class="sgp-acc__body">
      <ul class="sgp-xlist"><li>…</li></ul>
    </div></div></div>
  </div>
</div>
```
Keep the three nested divs inside `sgp-acc__panel` (the height animation needs them). Links to `#<item id>` anywhere on the page open and scroll to the panel. Collapsed panels get `inert` (sgp.js) + `visibility:hidden` after the collapse (CSS) — their links leave the Tab order; do not add `aria-hidden` yourself.

### 4.11 Tabs (Salient Tabs emulation, M40)
```html
<div data-tabs>
  <div class="sgp-seg" role="tablist" aria-label="Kryptis">        <!-- or class="sgp-tabs" = Minimal underline tabs -->
    <button type="button" role="tab" id="tab-ie" aria-selected="true" aria-controls="panel-ie" data-hash="airija">Airija <span class="sgp-mono">IE</span></button>
    <button type="button" role="tab" id="tab-es" aria-selected="false" aria-controls="panel-es" data-hash="ispanija" tabindex="-1">Ispanija <span class="sgp-mono">ES</span></button>
  </div>
  <div id="panel-ie" role="tabpanel" aria-labelledby="tab-ie" tabindex="0">…</div>
  <div id="panel-es" role="tabpanel" aria-labelledby="tab-es" tabindex="0" hidden>…</div>
</div>
```
Arrow keys/Home/End switch; `data-hash` = deep link (`…/#ispanija` opens that tab) and is written to the URL on click. Panels re-run CSS animations when shown (the map branch redraws). The container dispatches `sgp:tab` (`e.detail.tab`). Tab ids must be unique on the page (home uses `tab-ie/tab-es/rt-ie/rt-es` — only an issue if you include home markup).

### 4.12 Page submenu + scroll spy (M83, M61, M63 index, M64 media swap)
```html
<nav class="sgp-submenu" aria-label="Puslapio skyriai" data-spy data-salient="Page Submenu (Sticky)">
  <div class="sgp-wrap"><ul class="sgp-mono"><li><a href="#apie-paslauga">Apie paslaugą</a></li><li><a href="#privalumai">Privalumai</a></li></ul></div>
</nav>
```
`data-spy` on any container with `a[href="#id"]` links: the link of the section crossing the middle band gets `aria-current="true"` + its `li.is-active`; earlier links get `li.is-past` (rings in a sticky index fill via `.is-active>.sgp-ring`). Nothing is active while the first target is still below the band (visitor back at the hero). `data-spy="scroll"` = "last target whose top is above the viewport middle", computed in the rAF loop — use it for sticky/stacked targets (the IO band never re-fires for a stuck element). `[data-spy-count]` inside the container shows the 01-based active index. Elements anywhere with `data-spy-for="<section id>"` (of this spy's targets) get `.is-active` too (use for sticky-media swaps: stack the media absolutely and fade `.is-active` in your page CSS).

### 4.13 Stacking cards (Sticky Scroll Pinned Sections → Stacking, M63)
```html
<div class="sgp-stack" data-stack>
  <article class="sgp-stack__item"><div class="your-card">…</div></article>
  <article class="sgp-stack__item"><div class="your-card">…</div></article>
</div>
```
Each item is sticky (offset 14 px per index) **only ≥1000 px wide and ≥700 px tall**; while item i+1 slides over, item i's **first child** scales 1 → .94 and darkens under an opaque asphalt veil (its `::after`, opacity `--sp × .6`; `--sp` 0 → 1 written by sgp.js) — never translucent, so no text shows through. Plain stack <1000 px, on short desktops and under reduced motion (un-pinned). Give the child an opaque background and leave its `::after` to the veil. Override `top` only inside `@media (min-width:1000px) and (min-height:700px)`. Anchor links to a stacked card land on its natural (un-stuck) position (sgp.js §20).

### 4.14 „Kita stotelė“ band and CTA band
```html
<a class="sgp-nextstop" href="{{url:gyvunu-pervezimas}}" data-salient="Column Link „Kita stotelė“ (§4.19)">
  <span class="sgp-nextstop__bg" aria-hidden="true">{{img:32872983|w=1600|sizes=100vw|decorative}}</span>
  <span class="sgp-wrap sgp-wrap--zone sgp-nextstop__in"><span><span class="sgp-nextstop__k sgp-mono">Kita stotelė · 08</span><span class="sgp-nextstop__t">Gyvūnų pervežimas</span></span>
    <span class="sgp-nextstop__go"><svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg></span></span>
  <span class="sgp-nextstop__lane" aria-hidden="true"></span>
</a>

<section class="sgp-ctaband on-dark" data-theme="dark"><div class="sgp-wrap sgp-wrap--zone sgp-ctaband__in">
  <p class="sgp-ctaband__t">Statement line (verbatim or NEW – list it)</p>
  <div class="sgp-ctaband__calls">{{partial:phero-calls}}</div>
</div></section>
```

### 4.15 Forms (demo only — never sends anything)
The quote form lives in GS-Arrival (auto on every page with `arrival: yes`; pre-selects the service from `?domina=<exact service name>`). Contact form for /kontaktai/:
```html
<form class="sgp-form" action="#" method="post" novalidate data-demo-form data-salient="Fluent Forms · contact form">
  <p class="sgp-form__t">Parašykite</p>
  <label class="sgp-field"><span class="sgp-field__l">Jūsų vardas</span><input name="vardas" required autocomplete="name" placeholder="Vardas"><em class="sgp-field__err">Įrašykite vardą</em></label>
  <label class="sgp-field"><span class="sgp-field__l">El. pašto adresas</span><input name="el_pastas" type="email" required autocomplete="email" placeholder="vardas@pastas.lt"><em class="sgp-field__err">Patikrinkite el. pašto adresą</em></label>
  <label class="sgp-field"><span class="sgp-field__l">Žinutės tema</span><input name="tema" required><em class="sgp-field__err">…NEW error text – list it…</em></label>
  <label class="sgp-field"><span class="sgp-field__l">Žinutė</span><textarea name="zinute" rows="4" required minlength="20"></textarea><em class="sgp-field__err">Žinutė – bent 20 simbolių</em></label>
  <p class="sgp-form__note">Formoje pateikti duomenys naudojami susisiekimui su klientu.</p>
  <button class="sgp-btn sgp-btn--signal" type="submit"><span class="sgp-btn__l">Siųsti</span><span class="sgp-btn__a"><svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg></span></button>
  <p class="sgp-form__ok" role="status" aria-live="polite" tabindex="-1">Jūsų žinutė sėkmingai išsiųsta<small>Demonstracinė versija – duomenys niekur nesiunčiami.</small></p>
</form>
```
`data-demo-form`: submit is always prevented; native constraints (`required`, `type=email`, `minlength`) are checked per field, invalid fields get `.is-err` + `aria-invalid`, the first gets focus, errors clear on input, success box shows and receives focus; the form fires `sgp:sent`. Error `<em>` ids + `aria-describedby` are wired automatically. `<select data-domina>` = pre-fill from `?domina=`. Copy button: `<button class="sgp-copy" type="button" data-copy="saugiai.greitai.patikimai@gmail.com"><svg class="sgp-i" aria-hidden="true"><use href="#i-copy"/></svg><span>Kopijuoti</span></button><span class="sgp-sr" role="status" data-copy-status></span>` (status span must be a sibling). E-mail row: `sgp-mailrow`.

Tracking field (§4.15):
```html
<form class="sgp-track" action="{{url:sekimas}}" method="get" novalidate data-track>
  <label class="sgp-field"><span class="sgp-field__l">Siuntos kodas</span><input name="kodas" required autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="Siuntos kodas..."><em class="sgp-field__err">Neįvestas siuntos kodas!</em></label>
  <button class="sgp-btn sgp-btn--signal" type="submit"><span class="sgp-btn__l"><svg class="sgp-i" aria-hidden="true"><use href="#i-search"/></svg>Siuntos lokacija</span></button>
</form>
```
`data-track`: empty submit → the verbatim tool error; otherwise a normal GET to our own `/siuntos-sekimas/?kodas=…`. Every submit dispatches a cancelable `sgp:track` event (`detail.code`) on the form — the tracking page cancels it and runs its demo lookup; `SGP.track.error(form, msg)` / `SGP.track.clear(form)` set/clear the field error (msg omitted = the verbatim empty-code text). (the tracking page reads `SGP`-independent `new URLSearchParams(location.search).get('kodas')`). **Never call `siuntos.sgp-pervezimai.lt`** — the tracking page shows a demo result and the note „Demonstracinė versija – paieška veikia tik tikroje svetainėje.“

### 4.16 Maps, service list, reserved slot, video control
- `{{partial:map-ie}}`, `{{partial:map-es}}` (tabbed home maps), `{{partial:map-both}}` (static, both routes, IE leg dashed „maršrutas tikslinamas“) — SVG ≥700 px, ordered list below. Use each at most once per page (they carry ids). The SVG labels are 15 units: give the figure **≥ ~600 px** of width (≥ 12 px labels) and stack it in narrower columns. `map-both` wraps its SVG in `.sgp-map__stage` (position:relative, exactly the SVG box) — put overlays (hotspot layers) inside it and position them in % only.
- `{{paslaugos:list}}` = GS-ServiceList (11 services, 2 columns ≥691).
- Placeholder for future real content: `<div class="sgp-reserved"><p class="sgp-mono">Atsiliepimai</p><p class="sgp-reserved__t">…</p><p class="sgp-reserved__s">…</p></div>`.
- Every autoplaying video needs a control (WCAG 2.2.2): `<button class="sgp-vctl sgp-mono" type="button" data-video-toggle="<video id>" aria-pressed="false"><svg class="sgp-i" aria-hidden="true"><use href="#i-pause"/></svg><span>Pauzė</span></button>` (hidden <1000, where videos are posters). Self-hosted inline videos (service specials): `<figure class="sgp-grade sgp-ratio" style="--ratio:16/9">{{bgvideo:19552565|id=negabVideo|sd-only}}</figure>` + control.

---

## 5. Schedule placeholders = `[sgp_grafikas]` (§6.0)

Data: `src/data/grafikas.json` (4 routes, ISO dates, `render_today`, `updated`, `note`). Outbound rows dial the LT line; inbound rows dial the destination-country line (IE → LT `+353864503104`, ES → LT `+34602547929`). Past dates are dropped, the soonest route is marked, dates are words („Spalio 9 d.“, tiles „09 SPAL.“ only on the dark board), relative labels „šiandien / rytoj / po N d.“, empty route → „Grafikas atnaujinamas – skambinkite“ (row still dials).

| Placeholder | Output container (keeps `data-sched` for the client re-render) |
|---|---|
| `{{grafikas:board}}` | `<div class="sgp-board__grid" data-sched="board">` 4 cells (use via `{{partial:board}}` / `{{partial:board-inner}}`) |
| `{{grafikas:timetable kryptis=ie}}` | `<ul class="sgp-tt" data-sched="timetable">` tap-to-call rows |
| `{{grafikas:table}}` | `<div class="sgp-sched" data-sched="table">` grouped rows (name + code, all dates, status, number) |
| `{{grafikas:ticker limit=3}}` | header ticker `<ul class="sgp-tk__list">` (in the header partial) |
| `{{grafikas:next}}` | `<a class="sgp-next" data-sched="next">` phone-only next-departure line |
| `{{grafikas:stub route=lt-ie}}` | one ticket stub `<div class="sgp-ticket__stub" data-sched="stub">` |
| `{{grafikas:stubs}}` (alias `tickets`) | both ticket `<article class="sgp-ticket">` cards (each `data-reveal`) |
| `{{grafikas:lane}}` | `<figure class="gr-lane" data-sched="lane">` optional lane chart (/pervezimu-grafikas/ 02; page-owned `gr-` CSS, label layout in `pages/grafikas.js`) |
| `{{grafikas:updated}}` / `{{grafikas:note}}` | „Atnaujinta <time>rugsėjo 23 d.</time>“ / the board note |

Route selection args: `kryptis=ie` (lt-ie,ie-lt) · `kryptis=es` (lt-es,es-lt) · `kryptis=out` · `kryptis=in` · `kryptis=all` (default) · or explicit `routes=lt-ie,es-lt`. `limit=N` (ticker). `route=lt-es` (stub).

Build-time "today" = `render_today` (deterministic). In the browser `sgp.js` computes today in Europe/Vilnius (or `?siandien=YYYY-MM-DD` for presentations) and, if it differs, re-renders every `[data-sched]` container with the same markup (verified identical to the Python output). So: **do not post-process schedule markup in page JS; style it with the shared classes.** Test with `?siandien=2026-10-15` or `?siandien=2026-11-30` (empty state).

---

## 6. Service template (services team)

`src/templates/paslauga.html` is rendered once per entry of `src/data/paslaugos.json` → `pervezimo-paslaugos/tarptautiniai-pervezimai/<slug>/index.html`. It has the same front-matter format as a page; `{{svc:<field>}}` is substituted first (also inside front matter and inside other placeholders, e.g. `{{img:{{svc:hero_id}}|w=1920|pos={{svc:hero_crop}}}}`). Build only the services: `python3 tools/build.py pervezimo-paslaugos/tarptautiniai-pervezimai/`.

Fields available as `{{svc:…}}` (plain strings are HTML-escaped; keys ending in `_html` are inserted raw):
- From JSON (Foundation-filled): `slug no name h1 title meta card card_media card_crop hover_video lead` (+ `chips`, `submenu`, `hero{type,id,crop}`, `why_media[3]`, `next` as data).
- To fill (services team, per §6.5 data schema): `kv [{k,v}]`, `routes [..]`, `intro [..]`, `why [..]`, `special {…}`, `responsibilities [{title,text}]`, `prohibited`, `closing`. Add any extra fields you need.
- Computed: `url`, `total` („11“), `next_slug next_name next_no next_url next_media`, `hero_id hero_crop hero_type`.
- Default HTML renderings: `chips_html` (`<li>`s), `kv_html` (`<dt>/<dd>`s), `intro_html` (`<p>`s), `routes_html` (link chips to `?domina=<name>#uzklausa`).

Lists/objects cannot be printed directly — render them in the **optional hook** `src/templates/paslauga.py` (owned by the services team; stdlib only):
```python
def blocks(svc, ctx):
    """Return {name: html}; each becomes {{svc:name}}. ctx = esc, media, services, schedule, icon_phone, icon_arrow."""
    esc = ctx['esc']
    why = ''.join(f'<div class="sv-why__b" id="why-{i}"><p><b>{esc(w["lead"])}</b> {esc(w["text"])}</p></div>' for i, w in enumerate(svc.get('why', [])))
    media = ''.join(ctx['media'].img(mid, {'w': '1100', 'sizes': '45vw'}) for mid in svc.get('why_media', []))
    return {'why_html': why, 'why_media_html': media}
```
`ctx['media'].img(id, opts)` is the same helper as `{{img:…}}`. Keep copy verbatim (see §6.5 refs); record typo fixes.

---

## 7. Motion via data attributes (all implemented in `sgp.js` + `motion.css`; every effect has a reduced-motion state)

| Attribute | Effect (design id) | Notes |
|---|---|---|
| `data-reveal` | fade up 26 px (M13/M27) | values: (empty) up · `fade` · `left`. Delay: `style="--dl:.12s"`. Off ≤690 px (Salient mobile default). Anything already in the first viewport enters on load. |
| `data-stagger="120"` (parent) | assigns `--dl` = i × 120 ms to child/grandchild `[data-reveal]` | cards 120 ms, rows 60–90 ms. |
| `data-mask` | clip reveal bottom → top (M24) | also `data-mask="circle"`, `data-mask="left"`. Observed through the **parent**. |
| `data-split` | word reveal (M22; H1/H2) | JS wraps words, sets `aria-label`. Plain text only inside. `&nbsp;` keeps two words together; a lone dash („ – “) always stays with the previous word. |
| `data-split="blur"` | word blur-in (M52) | |
| `data-reel="11"` | odometer digits (M26) | any string; digits roll, other chars static; exposes `role=img` + label. |
| `data-draw` | only adds `.in` when visible (no hidden state) | use to trigger your own CSS (`.x.in …`), `<mark class="sgp-mark">` underlines (M23) draw inside any `.in` element. |
| `data-parallax="0.12"` | translateY = −(parent centre − viewport centre) × speed (M10/M25/M50) | ≥1000 px only, one shared rAF loop; negative values move against the scroll. Put it on a layer that has bleed (`.sgp-bgmedia` has `--bleed:12%`) or on an image scaled with the CSS `scale` property (never `transform`, JS owns it). |
| `data-scroll-scale` | scale .88 → 1 + y 40 → 0 while the parent enters (M66) | ≥1000 px. |
| `data-stack` | stacking cards (M63) | §4.13. |
| `data-stops` + `data-stop` (+ `data-stop-count`) | rail stops: each stop gets `.is-reached` in the left/top 70 % of the viewport (M31, M34) | style `.is-reached::after` lane segments, rings fill automatically (`.is-reached>.sgp-ring`). |
| `data-hover-video="<sd url>"` | muted video over the image on first hover (M33) | element must contain a `<video muted loop playsinline preload="none">`; add `.playing` styles. Fine pointers, desktop, no saveData. |
| `data-flap` | split-flap tiles (M14) | text only, never phone numbers; animates once on desktop; in a `[data-hero]` section it runs 700 ms after load. |
| `data-hero` | marks the first-screen hero section | |
| `data-tabs`, `data-hash` | tabs (M40) | §4.11 |
| `data-acc` | accordion (M60/M62) | §4.10 |
| `data-spy`, `data-spy-for` | scroll spy (M83/M64) | §4.12 |
| `data-demo-form`, `data-domina`, `data-track`, `data-copy`, `data-copy-status` | forms | §4.15 |
| `data-bgvideo`, `data-video-toggle="<id>"` | lazy background video + pause control (M16) | from `{{bgvideo:…}}` |
| `data-rail-end` | terminus waypoint in a `.sgp-rail-end` row | |
| `data-salient="Element → option · option"` | **required on every row, inner row, component and custom block** — the „Salient žymės“ toggle prints it for the WP developer | |

CSS-only effects you get for free: rail draw + waypoint rings (`sgp-has-rail`, M20/M21), map draw (M41/42), stations lane, breadcrumb draw (M81), inner-hero zoom-out (M80), hover states (M32/M44/M45/M70/M84–M87), page transition (M09, desktop). Scroll-driven CSS uses `animation-timeline: view()` and falls back to the finished state.

Rules: no GSAP or other libraries. Lenis 1.1.13 is loaded globally. Flickity 2.3.0 (apie-imone gallery, M68) / anime.js 3.2.2: add `vendor: flickity` (or `vendor: anime`) to your front matter — the build inserts the pinned jsdelivr CSS/JS before `sgp.js` and your page JS. CDN URLs are not allowed in `css:`/`js:`. Only `transform`/`opacity`/`clip-path` animations. Every looping pulse stops within ~5 s. Always check your page with macOS "Reduce motion" or `prefers-reduced-motion: reduce` emulation.

---

## 8. Page JS/CSS conventions

**Class prefixes (page-owned):** home `h-` (Foundation) · apie-imone `ab-` · pervezimo-paslaugos `ps-` · tarptautiniai `tp-` · service template `sv-` · pervezimu-grafikas `gr-` · siuntos-sekimas `sk-` · taisykles `tr-` · kontaktai `kt-` · privatumo-politika `pp-` · 404 `e4-`. Shared = `sgp-*` (production custom-CSS names; the WP developer copies them). Don't restyle `sgp-*` globally in a page file — scope it: `.page-apie .sgp-kv{…}` or your own wrapper class.

**Page CSS:** use tokens only (`var(--c-…)`, `var(--fs-…)`, `var(--sp-…)`, `var(--e-arrive)`, surface vars `--fg/--fg-2/--hair/--card/--red-text`). Breakpoints: 1280 · 1000 (desktop/tablet) · 691–999 (tablet) · 690 (phone) · 480. Mobile-first quality at 390, no horizontal overflow, tap targets ≥44 px, nothing <12 px, 2 px radii, no pills/gradients/glow/yellow. Put reduced-motion overrides for your own animations in `@media (prefers-reduced-motion:reduce)`.

**Page JS** (`assets/js/pages/<page>.js`, deferred, runs after `sgp.js`; wrap in an IIFE, guard with `if (!window.SGP) return;`):
```js
(function () {
  'use strict';
  const S = window.SGP; if (!S) return;
  const el = S.$('#my-thing'); if (!el) return;
  S.onFrame(y => { /* ONE rAF scroll loop: do your reads here and RETURN a function with your writes —
                     it runs after every hook has read (shared reads → hooks → shared writes → returned writes) */
    const top = el.getBoundingClientRect().top;
    return () => el.style.setProperty('--p', S.clamp(-top / S.vh()).toFixed(3));
  });
  S.onResize(() => { /* debounced resize, fonts ready, 1000px breakpoint change */ });
  S.io(S.$$('.x'), (entry, observer) => { if (entry.isIntersecting) entry.target.classList.add('in'); }, { rootMargin: '0px 0px -12% 0px' });
})();
```
`window.SGP`: `$`, `$$`, `clamp`, `reduce` (bool), `fine` (fine pointer), `saveData`, `desk()` (≥1000), `vh()`, `vw()`, `onFrame(fn)`, `onResize(fn)`, `io(els, cb, opts)`, `lenis` (instance or null — use `SGP.lenis ? SGP.lenis.scrollTo(target,{offset:-80}) : scrollTo(...)`), `refresh()` (re-measure after you change layout), `reveal(scope)` (observe newly inserted `[data-reveal]…`), `flap.flapify(el)/flap.run(el)`, `schedule` (`today`, `routes`, `full`, `rel`, `joinDates`, `render`), `menu.open/close/isOpen`, `header.update()`, `track.error(form,msg)/track.clear(form)`, `cookie.open()` (re-open the cookie bar, e.g. „Keisti slapukų nustatymus“). Never add another `scroll` listener; never import libraries other than the `vendor:` ones.

---

## 9. Hand-off checklist (per team)

- [ ] `python3 tools/build.py && python3 tools/check.py` → **0 errors** (don't break other pages).
- [ ] 390×844 and 1440×900 (plus 768 and 1366×657): no horizontal scroll (`document.documentElement.scrollWidth - innerWidth === 0`), text ≥12 px (Appendix D snippet 2), phone CTAs visible.
- [ ] Only the 5 tel numbers, each with a full `aria-label`; only `docs/media.json` media; alt texts from media.json; decorative textures `alt=""`.
- [ ] One `<h1>`; H2 per chapter; `data-salient` on every row/component; waypoint numbers continue across the page.
- [ ] Reduced-motion pass; keyboard pass (tabs, accordions, forms, menu).
- [ ] Copy verbatim; every typo fix and every NEW string listed in `docs/build-notes/<team>.md` (for client approval, §8 of the design system). Taisyklės: every point complete.
- [ ] Forms prevent submit (`data-demo-form`), tracking never calls the real endpoint.
- [ ] Shared-file changes only as **REQUESTS** in your notes: `REQUEST: <file> — <what> — <why> — <proposed code>`.

---

## 10. Foundation build notes

### 10.1 Files created
`tools/build.py`, `tools/check.py` · `src/partials/{layout,head,sprite,header,footer,callbar,scripts,arrival,board,board-inner,phero-calls,map-ie,map-es,map-both}.html` · `src/data/grafikas.json`, `src/data/paslaugos.json` · `src/pages/{index,apie-imone,pervezimo-paslaugos,tarptautiniai-pervezimai,pervezimu-grafikas,siuntos-sekimas,taisykles,kontaktai,privatumo-politika,404}.html` (all but index and 404 are placeholders: inner hero + „Puslapis kuriamas“) · `src/templates/paslauga.html` (placeholder: hero + „Kita stotelė“) · `assets/css/{tokens,base,components,motion}.css`, `assets/css/pages/home.css` · `assets/js/sgp.js`, `assets/js/pages/home.js` · `assets/img/favicon.svg` (logo mark on asphalt) · generated: `index.html`, `404.html`, 8 inner pages, 11 service pages. OG image: hero poster 29374299 at 1200 w (Pexels URL; production needs the 1200×630 graded file, §6.12).

### 10.2 Typo / formatting corrections (verbatim otherwise)
- Taisyklių 4.2 list (home „Prieš siunčiant“): „šaunamiejii“ → „šaunamieji“; item 12 lower-cased („Visos kitos…“ → „visos kitos…“, list style) and shown in full.
- Taisyklių 4.5 fines table (home): „cigarecių“ → „cigarečių“, „ampolę“ → „ampulę“, „1200EUR“ → „1200 EUR“, „(200vnt.)“ → „(200 vnt.)“, „200g“ → „200 g“ (keys adapted per §6.8).
- Phone number display unified (§8.2 #5): +353 86 450 3104, +44 7566 878681, +34 602 547 929.
- Copyright „© 2026 sgppervezimai.lt Visos teisės saugomos.“ → „© 2026 SGP pervežimai. Visos teisės saugomos.“ (§8.2 #6 / §4.21).
- Service `<title>`: „Gyvunų“ → „Gyvūnų“ (§6.12). Service meta descriptions (seeded in paslaugos.json): krovinių double space removed; daiktų „Paslaugos vykdomos: . iš/į Vokietiją, Prancūziją,  Ispaniją“ → „Paslaugos vykdomos iš/į Vokietiją, Prancūziją, Ispaniją“; gyvūnų „Mums yra svarbūs Jūsų gyvūnų saugumas“ → „svarbus“. Other live metas kept verbatim (they still contain „iš/į“ case issues — services team/client may rewrite).
- Service leads seeded from §6.5 already include approved fixes („tam tikrų“, „gera kaina“).

### 10.3 NEW copy introduced by Foundation (beyond the §8.1 list, for client approval)
- Home waypoint meta „Taisyklių 4.2 · 4.5 p.“ (06 Prieš siunčiant) and panel reference label „Taisyklių 4.2 p.“.
- Timetable row labels „Į Airiją“ / „Į Ispaniją“ when a timetable lists both outbound routes (reuses the call-bar labels).
- Arrival waypoint meta „LT ⇄ IE · LT ⇄ ES“ (reused from the about chapter).
- Service template eyebrow „07 / 11 · Tarptautiniai pervežimai“; placeholder copy „Puslapis kuriamas“, waypoint „Demo“ (demo-only, replaced by teams).
- 404 `<title>` „Maršrutas nerastas | sgp-pervezimai.lt“; 404 waypoint „11 · Paslaugos“.
- Footer demo line „Ankstesnė demo versija (v1)“ · „Demo · nuotraukos ir video — Pexels“ (demo-only, as briefed).
- Accessibility strings: „Uždaryti“, „Uždaryti meniu“, „Meniu“, „Skambinti – telefono numeriai“, „Telefonai“, „Kelias“ (breadcrumb landmark), „Greitas skambutis“, „Kryptis“ (tab list), „Tarptautinės pervežimo paslaugos“ (footer nav), empty-schedule aria „… grafikas atnaujinamas.“; dev-only tooltip on „Salient žymės“.

### 10.4 Deviations from the design system (and why)
1. **404 uses an absolute root (`/sgp-pervezimai/`) instead of `<base href>`.** A base URL makes `#fragment` links and SVG `<use href="#i-…">` icons resolve against the site root (broken icons, skip link jumps home). Links are otherwise identical; `check.py` resolves `/sgp-pervezimai/…` for 404.html only. Local preview of 404 needs the repo served under `/sgp-pervezimai/`.
2. **Demo class names are the production `sgp-` names** (the tile used unprefixed names). Surfaces keep `.on-dark/.on-light/.paper` from §2.1 and are aliased to `.sgp-dark/.sgp-light/.sgp-graticule`.
3. **File layout:** output at repo root (brief) instead of `v2/`; shared CSS split into tokens/base/components/motion instead of one `sgp.css`; schedule data is build-time JSON inlined as `window.SGP_SCHEDULE` instead of `sgp-data.js`.
4. **Schedule rendered at build time (like the PHP shortcode) and re-rendered by `sgp.js` only when the visitor's date differs from `render_today`** (the tile rendered everything client-side). Markup is identical in both paths (verified).
5. **Parallax runs in one JS rAF loop (`data-parallax`)** instead of CSS scroll timelines, so Firefox/older Safari get it too; the rail, rings, map draw and comfort lane stay CSS scroll-driven as specified. Parallax/scroll-scale are off <1000 px and under reduced motion (Salient "Disable Parallax On Mobile").
6. **Background videos:** a responsive poster `<img srcset>` (LCP, phones only ever see this) + a `<video>` that fades in over it on desktop, instead of the `poster` attribute. HD at ≥1280, SD 1000–1279.
7. **Cookie bar appears after the visitor scrolls half a viewport** (demo), so the hero board is not covered on the first presentation screen. Remembered in localStorage (try/catch).
8. **Overlay bug from the tile fixed:** in rail rows the rail owns `::before`, so the cinematic overlay moved to `::after` (the tile's overlay collapsed into a 14 px strip).
9. **Entrance reveals:** off ≤690 px (Salient mobile default); anything already in the first viewport reveals on load (the −12 % IO margin otherwise hid bottom-of-screen content until scroll).
10. **Breadcrumbs ≤690 px** hide earlier items (parent + current remain) without the „…“ link. **Mega menu** opens on hover/focus-within (CSS), no extra toggle button.
11. **`<meta name="robots" content="noindex, nofollow">`** on every demo page (the demo must not compete with the live site); canonical/og:url point to the GitHub Pages URL.
12. **Crop marks** must wrap the graded frame (`.sgp-crop > .sgp-grade`) — on the same element (tile) `overflow:hidden` clipped them.
13. **Rules digest „Pakavimas (4)“** shows the 5 cm recommendation as the full verbatim sentence from Siuntų pervežimas („Svarbu, kad siuntos turinys prie pakuotės sienelių nesiliestų – rekomenduojamas tarpas yra 5 centimetrai.“) rather than the fragment.
14. The 404 page is complete (not a placeholder) because it is small; teams may refine it.

---

## 11. Integration pass (after all page teams)

All page-team REQUESTS were reviewed; the shared files now provide what the pages had worked around locally, and the local workarounds were removed:

| Request (team) | Shared change | Page workaround removed |
|---|---|---|
| Stacking: un-pin under reduced motion (about-contact 1, service-template 1) | `motion.css` reduce block: `.sgp-stack__item{position:relative;top:auto}` + no veil | `apie.css`, `paslauga.css` |
| Stacking: opaque veil instead of opacity (about-contact 2, services-routes 1) | `components.css` `.sgp-stack__item>*::after` veil (`--sp × .6`) | `.ab-card::after`, `.sv-pcard::after`, `.ps-grp::after` + `opacity:1` overrides |
| Stacking on short desktops / `top` only while sticky (services-routes 3, service-template 4) | sticky only `@media (min-width:1000px) and (min-height:700px)` | `paslaugos.css` / `paslauga.css` max-height rules |
| Ticket stub on phones (about-contact 3) | `.sgp-ticket__stub>.sgp-mono:first-child{flex-basis:100%}` | — |
| Hero preload widths (about-contact 4) | `build.py` preload `imagesrcset` = 480/760/1100/1600/1920 (same as `{{img}}`) | — |
| `SGP.cookie.open()` (about-contact 5) | `sgp.js` §16 | `privatumo-politika.js` localStorage handling |
| `.sgp-e404*` to page CSS (about-contact 6) | moved to `pages/404.css` (`__code` rule dropped — `.e4-code` overrides it) | — |
| Lane chart as a variant (schedule 1) | `Schedule.lane()` (build) + `V.lane` (sgp.js), `{{grafikas:lane}}`, markup verified identical for 4 dates | `grafikas.js` rendering; no-JS hiding rule |
| Flap-ready table route codes (schedule 2) | `table` variant outputs `data-flap`; tile styles in `components.css` | `grafikas.js` flapify/run, `grafikas.css` tile rules |
| Tracking hook (schedule 3) | cancelable `sgp:track` + `SGP.track.error/clear` | `sekimas.js` listener-order dependency and `<em>` text swapping |
| Odometer gap (schedule 4) | `[data-reel]`/`.sgp-reel` tabular figures, centred digits | `taisykles.css` −.19em hack |
| Multi-paragraph clauses, ≤560 stacking (schedule 5) | `components.css` `.sgp-clause` | `taisykles.css` |
| Map width note (schedule 6) | §4.16 above | — |
| Spy: nothing active above chapter 1 (service-template 2) | `sgp.js` §13 (frame-loop check; IO alone misses jumps to the top) | `paslauga.js` §5 |
| Hook gets shared JSON (service-template 3) | `ctx['shared']`, `ctx['groups']` | `paslauga.py` file re-read |
| Overview groups from data (services-routes 2) | `{{paslaugos:groups}}` + `{{paslaugos:group-index}}`, group `lead` in `paslaugos.json` (output identical to the pasted markup) | ~150 lines of pasted markup |
| `data-split` keeps `&nbsp;` (services-routes 4) | `sgp.js` §3 (+ lone dashes join the previous word) | `data-reveal` fallback on the two chapter H2s |
| Spy/anchors for sticky targets (services-routes 5) | `data-spy="scroll"`, `data-spy-count`, `li.is-past`; anchor handler lands stacked cards at their natural position | `paslaugos.js` §3 |
| Ticker CSS scoped (services-routes 6) | `.sgp-tk .sgp-tk__list …` + `fitTicker` scoped | `.ps-tk__m--sched` layout resets |
| Hover video on another element (services-routes 7) | **not adopted** — the overview's loader is part of its layer cross-fade; a generic `data-hover-video-target` would not remove it | — |
| Map stage wrapper (services-routes 8) | `map-both` → `.sgp-map__stage` | `tarptautiniai.js` SVG measuring on resize |

Harmonisation: `data-hero` on every inner hero; hero chips 20 px below (shared) and plain header = 44svh (shared) — page overrides removed; button-label icons 18 px site-wide; submenu links fill the 52 px bar (text centred, 52 px tap target — was 16 px); off-canvas menu marks ancestors (`aria-current="true"`) with an outline ring; mega-menu + footer links of the current page/service get `aria-current`; „Visos paslaugos“ always → /pervezimo-paslaugos/; cross-links added: schedule → routes/services/contacts, contacts → routes/services/schedule, routes → services/schedule/contacts, every service → schedule + contacts.

---

## 12. Review fixes (shared layer + home, 2026-09-24)

| Finding | Fix (files) |
|---|---|
| Lenis on phones; stopped Lenis blocked touch/wheel in the open menu | Lenis starts only on fine pointers (`sgp.js` §20: `!fine` gate); `data-lenis-prevent` on `#sgp-menu` (`header.html`). Phones scroll natively, no non-passive touch listeners. |
| Collapsed accordion links reachable with Tab | `set()` → `panel.inert = !open` (no `aria-hidden`); CSS fallback `visibility:hidden` after the .45 s collapse (`components.css`). |
| `data-split` on `<p>` silent for screen readers | Text kept once in a `.sgp-sr` span, word spans `aria-hidden`; no `aria-label` (`sgp.js` §3). Works on any element. |
| Cookie card / „Salient žymės“ above the open menu | `.menu-open .sgp-cookie, .menu-open .sgp-tagbtn, .menu-open .sgp-stags{visibility:hidden}`. |
| Error `<em>` announced before any error / read twice | Inputs get `aria-labelledby` → their `.sgp-field__l`; `aria-describedby` → the error only while the field is in error (`fieldError()` in `sgp.js` §14, used by demo forms and `SGP.track.error/clear`). |
| Menu scroll lock without Lenis made body a scroll container (sticky submenu broke) | Lock on the root: `html.menu-open{overflow:hidden}` (class toggled on `<html>` and `<body>`). |
| Mega menu not dismissible with Esc (WCAG 1.4.13) | Esc on `.sgp-nav__mm` → `.is-closed` (hidden at once), focus to „Pervežimo paslaugos“; cleared on pointerleave / focus leaving the item. |
| Switchboard popover had no role | `role="dialog"` on `#sgp-call`. |
| No print stylesheet | `motion.css @media print`: reveal end states, accordions open, chrome/overlays/background media/forms hidden, dark rows print dark-on-white, tel: number printed after board cells, timetable rows and „Skambinti“; `sgp.js` adds `.in` to every reveal target on `beforeprint` (covers page-owned start states). |
| `viewport-fit=cover` without side safe areas | `--gutter:max(clamp(16px,4vw,56px),env(safe-area-inset-left),env(safe-area-inset-right))` (`tokens.css`; deviates from §2.1 by the `max()` only); cookie and dev chip `left:max(…,env(safe-area-inset-left))`. |
| Render-blocking `lenis.css` | The five rules inlined in `base.css`; `<link>` removed; `preconnect` to cdn.jsdelivr.net (no `crossorigin` — the deferred Lenis/Flickity files are plain no-cors requests, a CORS preconnect would not be reused). |
| Background videos observed through their section | IO observes the `<video>` box itself (250 px margin); no video starts before `window.load` (poster/fonts/LCP first). |
| Read/write interleaving in the frame loop | `readHeader/writeHeader` (header `data-on` written only on change), `motionRead`, `spyRead`, `tagsRead` return their writes; order = shared reads → page hooks → shared writes → writes returned by hooks. Existing page hooks still work unchanged (they may adopt the return-a-writer form, §8). |
| `check.py` skipped `data-src` and og:image | Checks `data-src`, `data-poster`, `og:image`/`twitter:image` against `docs/media.json`. |
| Route schematic finished drawing after the map centre | trunk `entry 0% → cover 28%`, branch `cover 18% → cover 38%` (map centre = cover 50 %): verified fully drawn at 1440×900 and 1280×800 with the map centred. |
| Dev tags clipped / squeezed / overlapping | Tags render in one fixed layer `body > .sgp-stags`, placed from `getBoundingClientRect()` in the frame loop (+ every 400 ms while on), clamped to the viewport, `min-width:min(240px,80vw)`, tall elements' tags stick to the top while on screen, collisions move a tag below the earlier one. |
| Dev toggle covered content | 32×32 tag chip (`#i-tag`) bottom-left, label slides out on hover/focus/while on (label = accessible name); moves beside the cookie card while that is shown; still hidden ≤699 px. |
| Ticket stub label wrapped | „Kitas išvykimas“ + mono meta „iš LT · po N d.“ (`build.py` `stub_inner`, `sgp.js` `V.stub`; design system §3.9 / §8.1 p. 15 updated). |
| Home: „dėžės“ | „dėžes“ in „Pakavimas (4)“ (turinio-pataisos #69, same as #29). |
| Home/Kontaktai: trimmed Maršrutai sentence not listed | turinio-pataisos #70 (Pradžia) and #71 (Kontaktai). |
| Home hero video 5.1 MB HD | `{{bgvideo:29374299|…|sd-only}}` (960×540, 2.6 MB) + first play after `load`. |
| Home: inline „Skambinti“ inflated the line | `.h-track__call{min-height:0;padding:12px 2px;margin:-12px 0}` — 48 px hit area, 24 px line box. |
| Home: static „01 / 11“ on phones | `.h-svc__count b{display:none}` < 1000 px (the link stays). |
| Home: reviews placeholder looked orphaned | Chapter waypoint (ring · „Atsiliepimai“ · rule · „Vieta rezervuota“), `sgp-has-rail`, full-width dashed box, title 7/12 + note 5/12. |

New copy for approval: „Kitas išvykimas“ + „iš LT · po N d.“ (replaces „Kitas išvykimas iš Lietuvos“); home reviews waypoint meta „Vieta rezervuota“ (reuses the placeholder note).

