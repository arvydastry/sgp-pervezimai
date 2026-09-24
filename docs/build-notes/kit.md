# Salient kit — Kit API for the page teams (Wave 1, team „shared“)

**Direction:** „SGP v2 identity, built the Salient way“ (`docs/salient-atitikimo-planas.md` §1). Every block is markup for the **Salient 18.2.1 emulation kit**: our own CSS/JS that reproduces Salient's visible behaviour and real numbers (`docs/salient-18-2-1-parinktys.md` §3). In WordPress the emulation disappears — Salient draws it natively.
**Living style tile:** `docs/kit.html` — source `src/pages/_kit.html`, built only with `python3 tools/build.py --kit` (Wave 3 decision: the specimen is **not part of the public site build**; sources whose name starts with `_` are skipped, `check.py` fails if a `_kit/` folder reappears). Every component below is on that page in asphalt (A) and paper (P) tones with its `data-salient` label — copy from it. Toggle **„Salient žymės“** (bottom left) to see the admin option names.

## 0. How a page switches to the kit

```
---
title: … | SGP pervežimai
description: …
out: apie-imone/index.html
kit: salient              # required — the page gets the kit stack and the kit partials
nav: apie
hero_media: 9989463       # optional LCP preload
css: pages/apie.css       # optional, ≤ 15 non-blank lines, demo-only spacing (see §6)
vendor: flickity          # only if the page has an Image Gallery (Flickity Style)
salient: Page „Apie įmonę“ · A1 inner head → A2 clip-path band → …
---
```

- `kit: salient` is **required** (build error otherwise). Pages get: `theme-options.css → emul/*.css → sgp-custom.css → page CSS → demo.css`, `sgp-custom.js` in `<head>` (production: *Custom JS (Head)*), Lenis 1.1.13 + `emul.js` + `demo.js` (defer). **`js:` is a build error** — page teams own no JS. Since Wave 3 no page has page CSS (`assets/css/pages/` was deleted).
- The chrome is automatic: GS-Išvykimai ticker + header + Fullscreen Cover Split off-canvas (`src/partials/header.html`), GS-Poraštė footer, GS-Skambučių juosta call bar, Back To Top button (desktop), Complianz-style cookie card, the „Salient žymės“ button.
- **Every page starts dark** (hero Section or the inner head) — the header is transparent at the top.
- **Inner head recipe (Wave 3 harmonisation):** Row Full Width Background, Text Light, Column Alignment Bottom, Padding **184 px / 48 px** (tablet top 168 px, phone 128 px / 32 px; 72 / 48 px bottom when there is no glass band), Parallax Subtle + Slight Zoom Out Reveal on a photo/video, Column 8/12: Yoast breadcrumbs → Label → **Animated Text H1 `--fs:6.4vw;--fs-min:44px;--fs-max:104px;--lh:.92`** → Road line → Intro; glass band links read „Visas grafikas →“. Only the home hero and the Tarptautiniai Section keep the 3-line 5.6vw H1.

## 1. Conventions

| Thing | Rule |
|---|---|
| Class | the Salient base / DOM class (`wpb_row`, `nectar-cta`, `toggles`, `img-with-aniamtion-wrap` — Salient's own spelling) |
| Element options | `data-*` attributes carrying Salient's **saved values** (`data-style="arrow-circle-animation"`, `data-parallax-speed="medium_fast"`) |
| Design Options (per instance) | inline CSS variables on the element they belong to (§3) |
| `data-salient` | **required** on every `section.vc_section`, `.wpb_row`, `.vc_row.inner_row`, `.nectar-global-section`; recommended on every element root. Format `Element → Option: value · Option: value` with the exact 18.2.1 admin names. `tools/check.py` fails a kit page when a section/row lacks it. |
| Tone | `data-text-color="light"` (asphalt chapters, photos) / `"dark"` (paper). Elements follow it through tone variables (`--tone-fg`, `--tone-muted`, `--tone-hair`, `--tone-label` …) like Salient's `.light` scope. Add Extra Class `sgp-dark` to asphalt rows (scopes C-6/C-11). |
| Utilities (only these) | Extra Classes `sgp-dark`, `sgp-num`, `sgp-callbar`, `sgp-grafikas`, `sgp-ticker`, `sgp-motion-toggle`, theme classes `nectar-inherit-label`, `screen-reader-text`; attributes `data-text-align(-t/-m)="left|center|right"`, `data-hide="desktop tablet phone"`. No other helper classes. |
| Breakpoints | desktop ≥ 1000 · tablet 691–999 · phone ≤ 690 (header breakpoint 1000). Check at 1440×900, 1024×768, 390×844. |
| Radii | 3 px (buttons, columns, cards, toggles, dropdown, sticky sections, badges), 0 (images, rows). `check.py` rejects any radius > 4 px in the kit CSS except 50 % circles. |
| Red | signal only (calls, arrows, active states, hotspots, road lines). Text on red is always `#0F1417`. Small red text on paper `#C4301E`. Never a section background. |

## 2. Structure

```html
<!-- Section (vc_section): heroes, 404. Only the Section has „Parallax Fade“ and the Flexbox layout. -->
<section class="vc_section sgp-dark" id="pradzia" data-type="full_width_background" data-text-color="light"
  data-layout="flex" data-justify="flex-end" data-parallax="parallax_fade" data-parallax-speed="medium"
  style="--bg:#0B0E10;--min-h:100svh;--min-h-m:90svh;--pt:190px;--pb:40px;--pt-m:124px"
  data-salient="Section → Min Height 100svh · Flexbox column, flex-end · Background Video 29374299 · Parallax Background Media On Scroll ✓ → Scroll Effect: Parallax Fade · Speed: Medium · Color Overlay: v2 hero grade · Text Color: Light">
  {{bgvideo:29374299|eager|phone=36383706|overlay=HERO_GRADE}}
  <div class="wpb_row" data-type="full_width_background" data-salient="Row"> … </div>
</section>

<!-- Chapter row (Row = vc_row) -->
<div class="wpb_row" id="apie" data-type="full_width_background" data-text-color="dark" data-padding="chapter"
  data-color-change style="--bg:#F5F7F6" data-salient="Row → Chapter row P · Padding 8 % / 8 % (phones 80px) · Color Change Section ✓ · Row ID apie">
  <div class="row_col_wrap_12">
    <div class="wpb_column vc_col-sm-7" data-animation="slight-fade-in-from-bottom" data-salient="Column 7/12 → Animation: Slight Fade In From Bottom">
      <div class="vc_column-inner"> …elements… </div>
    </div>
    <div class="wpb_column vc_col-sm-4 vc_col-sm-offset-1" data-delay="120" data-animation="slight-fade-in-from-bottom" data-salient="Column 4/12 (offset 1)">
      <div class="vc_column-inner"> … </div>
    </div>
  </div>
</div>

<!-- Inner Row (vc_row_inner) inside a column -->
<div class="vc_row inner_row" data-backdrop-blur="16" style="--bg:rgba(11,14,16,.55);--border:1px solid rgba(242,244,243,.12);--r:3px;--pt:24px;--pb:24px;--pl:32px;--pr:32px" data-salient="Inner Row → Backdrop Filter: Blur 16 · …">
  <div class="row_col_wrap_12_inner">
    <div class="wpb_column vc_col-sm-5" data-salient="Inner Column 5/12"><div class="vc_column-inner"> … </div></div>
  </div>
</div>
```

**Row** — `data-type="in_container | full_width_background | full_width_content"` · `data-padding="chapter"` (= Padding 8 % / 8 %, phones 80 px; otherwise `--pt/--pb`) · `data-full-height` (+ `data-column-position="bottom"`) · `data-equal-height` · `data-column-align="middle|bottom"` · `data-content-align="middle|bottom"` (with Equal Height) · `data-column-margin="none|5px|10px|20px|40px|60px|90px"` · `data-color-change` (Color Change Section: page colours switch at ≥ 40 % visibility, 0.8 s; **the text of every color-change row follows the active section's tone** like Salient's `--nectar-page-text-color` — rows with their own background media keep theirs) · `data-hide` · `data-sticky="bottom" data-sticky-mobile` (Sticky Row) · Row ID = `id`.
**Row background** — Background Image/Video via `{{bgimg:…}}` / `{{bgvideo:…}}` (§5) as the first child · `data-parallax-speed="fast|medium_fast|medium|slow|fixed"` (Subtle .20 / Regular .28 / Medium .40 / High .60 / Fixed In Place; off below 1000 px = *Disable Parallax Backgrounds On Mobile*) · `data-bg-animation="fade-in|zoom-out|zoom-out-slow|zoom-out-reveal|slight-zoom-out-reveal|clip-path"` (+ `data-bg-delay` ms).
**Clip Path Inset** — `data-bg-animation="clip-path" data-clip-type="scroll|once" data-clip-applies="bg|row" data-clip-start="0 6% 0 6%" data-clip-end="0 0 0 0" data-clip-round="3,0" data-clip-offset="0,50" data-clip-addon="zoom-fade-in|fade-in"` (Scroll Position = interpolated over the Viewport Trigger Offset; once = 1.3 s first row / 2 s others).
**Column / Inner Column** — widths `vc_col-sm-1…12`, relative offsets `vc_col-sm-offset-1…4` · tablet/phone widths `data-t-w="3|4|6|8|12"`, `data-m-w="6"` (default: full width below 1000) · `data-animation` (§4) + `data-delay` (ms) · `data-sticky="top|middle"` (+ `data-sticky-mobile`) · `data-layout="flex"` + `data-flex-dir="row"` `data-justify="center|flex-end|space-between"` `data-align="flex-start|center|flex-end"` + `--gap` · `data-el-space="50px|40px|30px|10px|5px|none"` (Column Element Spacing; default 20 px) · `data-text-align` · `data-shadow="small_depth|medium_depth|large_depth|x_large_depth"` · `data-backdrop-blur="8|12|16|20"` · `data-border-animation` (+ `data-border-delay`) · `data-bg-parallax="minimum|very_subtle|subtle|regular|medium|high"` · `data-bg-animation="mask-reveal|ro-reveal-from-bottom|zoom-out-slow"` (+ `data-mask-direction`) · Column Link = last child `<a class="column-link" href aria-label></a>` (covers the column; put no buttons in a linked column).
**Scroll Position Advanced** — `data-animation-type="scroll_pos_advanced" data-scroll-start="ty:60;s:.92;o:1" data-scroll-end="ty:0;s:1;o:1" data-scroll-offset="0,100"` (keys `tx ty s o`; desktop only unless `data-scroll-mobile`). *Scroll Position* (simple): `data-animation-type="parallax" data-movement="20" data-axis="y|x"`.
**Global Section wrapper** — `<div class="nectar-global-section" data-gs="GS-…" data-location="nav-top-before-scroll|mega-menu|off-canvas-meta|footer|after-content|inline|404" data-salient="Global Section „GS-…“ → Location: …">` (use the partials, §7).

## 3. Design Options (per instance)

Set them inline on the element they belong to; the kit resets them at the next structural level, so a nested row/column never inherits them.

| Variable | Meaning | Devices |
|---|---|---|
| `--pt --pr --pb --pl` | padding (px, %, vh) | `-t` tablet, `-m` phone (e.g. `--pt-m:80px`) |
| `--mt` | top margin of an element/column (overrides column element spacing; `--mt:auto` pushes to the bottom in flex/equal-height columns) | — |
| `--mb` | bottom margin of an element (Design Options margin-bottom, e.g. space before a `--mt:auto` button) | — |
| `--h` | Divider Custom Height (the line sits in its middle) | `--h-t`, `--h-m` (e.g. the road above Stations: `--h-m:64px`, so the line clears the stacked phone list) |
| `--bg` `--bg-hover` | background colour / Background Color Hover (columns: .45 s) | — |
| `--fg` | font colour | — |
| `--r` | border radius (keep 3px) | — |
| `--border` / `--border-top …-left` | Border Simple / Advanced (`1px solid rgba(28,29,29,.12)`) | — |
| `--min-h` | Min Height | `-t`, `-m` |
| `--max-w` | Max Width (Animated Text: measured in the heading's own size, e.g. `20em`) | — |
| `--gap` | Flexbox gap | — |
| `--col-gap` `--row-gap` | inline on `.row_col_wrap_12(_inner)` when Column Margin presets are not enough | — |
| `--fs --fs-t --fs-m --fs-min --fs-max --lh` | Font sizing group (Animated Text, Responsive Text, Highlighted Text, Scrolling Text, Button, Badge) | tablet/phone |

**Copy-paste values.** Chapter A: `data-text-color="light" style="--bg:#0F1417"` + class `sgp-dark` · Chapter P: `data-text-color="dark" style="--bg:#F5F7F6"` · P-alt `#EAEEED` · Card P: `--bg:#FFFFFF;--bg-hover:#EAEEED;--r:3px;--border:1px solid rgba(28,29,29,.12);--pt:40px;--pb:40px;--pl:36px;--pr:36px` · Card A: `--bg:#161D21;--bg-hover:#1A2227` · Callout: `--bg:#EAEEED;--r:3px;--border-left:2px solid #EF4539;--pt:32px;--pb:32px;--pl:32px;--pr:32px` (A: `--bg:#161D21`) · Glass band: Inner Row `data-backdrop-blur="16" style="--bg:rgba(11,14,16,.55);--border:1px solid rgba(242,244,243,.12);--r:3px"`.
**v2 hero grade overlay** (Color Overlay Advanced): `linear-gradient(0deg,rgba(15,20,23,.92) 0%,rgba(15,20,23,0) 46%),linear-gradient(90deg,rgba(15,20,23,.88) 0%,rgba(15,20,23,.6) 42%,rgba(15,20,23,.14) 80%)` · cinematic video row: `linear-gradient(180deg,rgba(15,20,23,.92) 0%,rgba(15,20,23,.32) 32%,rgba(15,20,23,.32) 62%,rgba(15,20,23,.94) 100%)` · Heavy (0.8): `rgba(11,14,16,.8)`.

## 4. Motion (Theme Options easeOutExpo · 1300 ms; real 18.2.1 values)

| Where | Attribute | Values → behaviour |
|---|---|---|
| Column / Inner Column | `data-animation` | `fade-in` · `fade-in-from-bottom` (100 px) · `slight-fade-in-from-bottom` (50 px) · `fade-in-from-left/right` (∓45 px) · `grow-in` (.75) · `zoom-out` (1.2) · `slight-twist` · `flip-in` · `flip-in-vertical` · `reveal-from-bottom/top/left/right` (inner slides behind the column mask, trigger 70 %) · `mask-reveal` (**Inner Column only**) + `data-mask-direction="top|right|bottom|left|middle"` `data-mask-shape="straight|circle"` (clip-path 1.3 s). Trigger 88 %, transform 1300 ms `(.19,1,.22,1)`, opacity 500 ms, `data-delay` ms (siblings 0/120/240/360). |
| Image | on `.img-with-aniamtion-wrap` | `data-animation="fade-in|fade-in-from-bottom|fade-in-from-left|fade-in-from-right|grow-in|slide-up|ro-reveal-from-bottom|ro-reveal-from-left|ro-reveal-from-right"` (Reveal Rotate 2.3 s `(.2,.65,.3,1)`) · `data-hover-animation="zoom-in|zoom-in-crop|color-overlay"` (.65 s `(.05,.2,.1,1)`) |
| Animated Text | `data-text-effect` | `default` (Word Reveal) · `blur-bottom` · `fade-bottom` · `twist-bottom` · `letter-reveal-bottom|letter-blur-bottom|letter-fade-bottom` · `scroll-opacity-reveal` · `none`; `data-stagger="true"`, `data-delay` — 1.2 s `(.25,1,.5,1)`, 15–50 ms per word |
| Row BG | `data-bg-animation` | Zoom Out Slowly 1.35 → 1 in 8 s · Slight Zoom Out Reveal .92/1.15 → 1 in 1.3 s · Clip Path Inset (§2) |
| Reduced motion | automatic | `sgp-custom.css` C-2 + `sgp-custom.js` J-1 show every end state, stop Lenis, loops and videos; sticky sections stack; the pause button starts „Paleisti judesį“. Nothing to do per page. |

## 5. Elements — copy-paste

```html
<!-- Label (Badge → Minimal Line, Label typography). Colour: #C4301E on P (default), #EF4539 on A (default), #F2F4F3 on photos -->
<span class="nectar-badge" data-badge-style="line" data-salient="Badge → Badge Style: Minimal Line · Inherit Typography From: Label">02 · Paslaugos</span>
<!-- Chip (Badge → Default, border) · on photos add data-backdrop-blur="12" style="--bg:rgba(11,14,16,.4)" -->
<span class="nectar-badge" data-badge-style="default" data-display="inline" data-padding="small" style="--border:1px solid rgba(28,29,29,.26);--r:3px">Nuo durų iki durų</span>

<!-- Animated Text (H1/H2; lines split with <br>) -->
<div class="nectar-split-heading" data-text-effect="default" data-stagger="true" style="--fs:5.6vw;--fs-min:40px;--fs-max:92px;--lh:.94" data-salient="Animated Text → Text Element: H1 · Word Animations: Reveal · Stagger ✓"><h1>Lietuva – Airija.<br>Lietuva – Ispanija.<br>Ir atgal.</h1></div>
<!-- Statement: data-text-effect="default" style="--fs:48px;--fs-t:40px;--fs-m:30px;--lh:1.05;--max-w:20em" with <h2> -->

<!-- Road line (Divider → Small Line, Accent, Animate Line) · full width: data-line-type="full-width" style="--h:1px" -->
<div class="divider-wrap" data-line-type="small" data-animate style="--line-w:96px;--thickness:2px;--h:14px"><span class="divider-border"></span></div>

<!-- Intro (Responsive Text inherit H5, muted) · other fonts: data-inherit="h1…h6|small" -->
<p class="nectar-responsive-text" data-inherit="h5" style="--fg:var(--tone-muted);--max-w:56ch">…</p>

<!-- Highlighted Text → Regular Underline (the <em> phrase gets the red line; em is not italic) -->
<div class="nectar-highlighted-text" data-style="regular_underline" data-underline-thickness="3px" style="--hl:#EF4539;--fs:40px;--fs-m:26px;--lh:1.15"><h3>„SGP“ – … <em>keleivių, siuntų ir automobilių pervežimu</em> …</h3></div>

<!-- Price Typography -->
<div class="nectar-price-typography"><span class="price">3–4</span><span class="after-text">paros kelyje</span></div>

<!-- Scrolling Text (outline marquee). Speeds: slower = Slowest 45 s · slowest = Slower 30 s · slow 14 · medium 7 · fast 4 · static -->
<div class="nectar-scrolling-text" data-s-speed="slower" data-repeat="3" data-divider="✦" data-divider-size="half" data-mask-edges data-move-on-scroll
  data-outline="thin" data-outline-divider data-spin-divider style="--fs:8vw;--fs-m:16vw;--space:.35em;--divider-color:#EF4539;--outline-color:#1C1D1D">
  <h2 class="nectar-responsive-text" data-inherit="h2" aria-label="Lietuva, Lenkija, …">Lietuva ✦ Lenkija ✦ …</h2></div>
```

**Buttons** (`a.nectar-cta` > `span.link_text` > `span.text`; the arrow circle / wave letters are injected by the kit):

| Recipe | Markup |
|---|---|
| **Call (red)** | `<a class="nectar-cta" data-style="arrow-circle-animation" data-color="accent-color" href="tel:+37065053161" aria-label="Pervežimai į Airiją – skambinti +370 650 53161">…` (+ `data-alignment="stretch"` in bands) |
| Button (ink on P) / (paper on A) | same with `data-color="extra-color-1"` / `"extra-color-2"` |
| Button (glass) | `data-style="see-through" data-backdrop-blur="12" style="--btn-border:rgba(242,244,243,.6);--btn-bg-h:#F2F4F3;--btn-fg-h:#0F1417"` |
| Route chip | `data-style="see-through" data-preset="sm"` |
| Link | `data-style="underline"` (icon: put `{{icon:download|class=nectar-cta__icon}}` before `.text`) |
| Link list | `data-style="text-reveal-wave" data-display="block"` |
| Basic | `data-style="basic" data-color="extra-color-1"` |
| Next Section | `<a class="nectar-cta" data-style="next-section" href="#next-row-id" aria-label="Į kitą skyrių"><span class="link_text"></span></a>` |
| **Lift button** (Legacy Button, P only) | `<a class="nectar-button regular large" data-color="extra-color-1" href="…"><span>Visos taisyklės</span><i class="icon-default-style"></i></a>` |
| Pause (C-14) | `<a class="nectar-cta sgp-motion-toggle" data-style="basic" href="#" style="--btn-bg:rgba(242,244,243,.1);--btn-bg-h:rgba(242,244,243,.2);--btn-fg:#F2F4F3"><span class="link_text"><span class="text">Sustabdyti judesį</span></span></a>` — **required on every page with a background video** (check.py) |

Colour vars for one-offs: `--btn-bg --btn-bg-h --btn-fg --btn-fg-h --btn-border --btn-border-h`, font `--fs`.

**Lists**
```html
<!-- KV rows (HLI 30|70, no hover, lines draw — Border Animation needs a hex Border Color: #C3CBCB on paper, #3E464A on asphalt) -->
<div class="nectar-hor-list-item" data-columns="2" data-column-layout="30-70" data-hover-effect="none" data-border-animation data-border-color="#C3CBCB">
  <div class="nectar-list-item"><p class="nectar-inherit-h6">Kelyje</p></div><div class="nectar-list-item"><p>apie 3–4 paros nuo paėmimo dienos</p></div></div>
<!-- Link rows (HLI 20|80, Hover Color: extra-color-1 on P (text turns #fff) / white on A (text turns #000), full link, typed arrow) -->
<div class="nectar-hor-list-item" data-columns="2" data-column-layout="20-80" data-hover-effect="default" data-color="extra-color-1" data-border-animation data-border-color="#C3CBCB" data-font-family="h4">
  <div class="nectar-list-item"><p class="muted sgp-num">01</p></div><div class="nectar-list-item"><p>Krovinių pervežimas <span aria-hidden="true">→</span></p></div>
  <a class="full-link" href="{{url:kroviniu-pervezimas}}" aria-label="Krovinių pervežimas"></a></div>
<!-- Column layouts: 20-80 25-75 30-70 40-60 60-40 25-50-25 20-40-40 15-35-35-15 auto · below 1000 px 2 columns keep their ratio, 3 / 4 columns stack; data-mobile="multiple" = Responsive Display: Multiple Columns (50 / 50) -->

<!-- Stations (Icon List, horizontal, numbers) — put a full-width animated Divider above as the road -->
<div class="nectar-icon-list" data-direction="horizontal" data-columns="3" data-icon-size="medium" data-icon-style="border" data-animate>
  <div class="nectar-icon-list-item" data-icon-type="numerical"><div class="list-icon-holder" aria-hidden="true"><span>1</span></div>
    <div class="content"><h4>Paėmimas</h4><p>…</p></div></div> …</div>
<!-- comfort list: data-icon-style="no-border" data-icon-size="small" data-columns="5", holder = {{icon:seat}} -->

<!-- Fancy Unordered List: data-list-icon="dash|dot|check|fa-times|none", data-spacing="5px|10px|15px|20px", data-animation -->
<ul class="nectar-fancy-ul" data-list-icon="fa-times" data-animation data-spacing="10px"><li>…</li></ul>
```

**Cards & data**
```html
<!-- Photo card (Column BG image + overlay .72 → .42 on hover + Column Link) -->
<div class="wpb_column vc_col-sm-4" data-text-color="light" data-layout="flex" data-justify="flex-end" data-bg-parallax="very_subtle" style="--r:3px;--min-h:360px;--pt:32px;--pb:32px;--pl:32px;--pr:32px">
  {{colbg:36383706|w=900|o=.72|oh=.42}}
  <div class="vc_column-inner"><span class="nectar-badge" data-badge-style="line" style="--fg:#F2F4F3">11 paslaugų</span><h3>Tarptautiniai pervežimai</h3></div>
  <a class="column-link" href="{{url:tarptautiniai}}" aria-label="Tarptautiniai pervežimai"></a></div>

<!-- Fancy Box → Image Above Text 3:2 (or {{paslaugos:related|slug=…}}) -->
<a class="nectar-fancy-box" data-style="image_above_text_underline" data-aspect="3-2" href="…"><div class="box-image">{{img:ID|w=760|decorative}}</div>
  <div class="meta-wrap"><h4><span class="fb-title">Title</span></h4><p>…</p></div></a>
<!-- Fancy Box → Description on Hover -->
<div class="nectar-fancy-box" data-style="hover_desc" data-hover-color="extra-color-1" data-bg-animation="short_zoom" style="--o:.55;--o-h:.8;--min-h:420px">
  <div class="box-bg">{{img:ID|w=760|decorative}}</div><div class="box-overlay"></div>
  <div class="inner"><h3>Title</h3><div class="hover-content"><div><p>…</p></div></div></div><a class="box-link" href="…" aria-label="Title"></a></div>
<!-- also data-style="parallax_hover" (.parallax-layer > img + content) and "color_box_hover" -->

<!-- Milestone: data-effect="motion_blur|count|none", data-symbol-pos="after|before", data-symbol-alignment="superscript" -->
<div class="nectar-milestone" data-effect="motion_blur" data-delay="150" data-inherit="h2" style="--fs:96px;--fs-m:72px"><div class="number"><span class="num">3</span><span class="symbol">–4</span></div><div class="subject">paros kelyje</div></div>

<!-- Icon (Linea-style line draw, Border W/ Hover Animation) -->
<div class="nectar_icon_wrap" data-style="border-animation" data-draw style="--ic-size:44px">{{icon:cage}}</div>
```

**Media**
```html
<div class="img-with-aniamtion-wrap" data-animation="ro-reveal-from-bottom" data-hover-animation="zoom-in" data-aspect="16-10"><div class="hover-wrap">{{img:ID|w=900|sizes=…|decorative}}</div></div>
<!-- data-aspect 16-10 | 4-5 | 3-2 | 1-1 | 16-9 | 4-3 · data-fit (Fit to Container) · data-shadow="large_depth" -->

<div class="nectar_cascading_images" data-aspect="4-5">
  <div class="cascading-image" data-animation="grow-in-reveal" data-parallax="subtle" style="--w:78%;--h:74%"><div class="bg-layer">{{img:7541981|w=900|decorative}}</div></div>
  <div class="cascading-image" data-animation="fade-in-from-bottom" data-parallax="medium" data-shadow="large_depth" style="--x:34%;--y:40%;--z:2"><div class="bg-layer">{{img:6169133|w=760|decorative}}</div></div></div>

<!-- Image With Hotspots on the static map; coordinates are listed in assets/img/marsrutai.svg -->
<div class="nectar_image_with_hotspots" data-hotspot-icon="numerical" data-tooltip-func="hover" data-tooltip-shadow="medium_depth" data-color="accent-color" data-animation>
  <img src="{{root}}assets/img/marsrutai.svg" alt="…" width="1100" height="720" loading="lazy">
  <div class="nectar_hotspot_wrap" style="left:72.7%;top:34.7%" data-tooltip-position="top|bottom|left|right">
    <button class="nectar_hotspot" type="button" aria-label="Lenkija"><span>2</span></button><div class="nttip" role="tooltip"><h5>Lenkija</h5><p>Pakeliui – …</p></div></div></div>

<a class="nectar-video-box" data-link-style="play_button_mouse_follow" data-mouse-style="see-through-contrast" data-hover="zoom_bg_image" href="{{videourl:ID}}" aria-label="Paleisti vaizdo įrašą „…“">
  <div class="nectar-video-box__media">{{img:POSTER|w=1100|decorative}}</div><span class="nectar-video-box__label" aria-hidden="true">…</span></a>

<!-- Image Gallery → Flickity Style (front matter vendor: flickity) -->
<div class="nectar-flickity" data-controls="touch_total" data-image-parallax data-mask-edges data-drag-scale style="--fl-cols:2"><div class="cell">{{img:ID|w=1100|decorative}}</div> …</div>

<!-- Content Trail (inside a Row, after .row_col_wrap_12) -->
<div class="nectar-content-trail" data-type="text" data-items="Airija|Ispanija|Siunta" data-colors="#EF4539/#0F1417,#F5F7F6/#0F1417" data-frequency="85" data-duration="1.2" data-randomize aria-hidden="true"></div>
```

**Interactive**
```html
<!-- Toggle Panels: data-style="animated_circle|minimal_shadow|default", data-accordion, data-first-open; deep link ?toggle=N (N counts all toggles on the page) -->
<div class="toggles" data-style="animated_circle" data-accordion data-first-open data-circle-position="right" data-circle-size="40" data-divider style="--r:3px">
  <div class="toggle"><h3 class="toggle-title">Draudžiama siųsti (12)</h3><div class="inner-toggle-wrap"><div class="toggle-content"> … </div></div></div></div>

<!-- Tabs: data-style="minimal|toggle_button|vertical_scrolling", data-animation="fade"; panel ids must be unique; deep link ?tab=<id without "tab-"> -->
<div class="tabbed" data-style="minimal" data-animation="fade">
  <ul class="wpb_tabs_nav"><li><a href="#tab-airija">Airija</a></li><li><a href="#tab-ispanija">Ispanija</a></li></ul>
  <div class="wpb_tab" id="tab-airija">{{partial:gs-grafikas-ie|tone=A}}</div><div class="wpb_tab" id="tab-ispanija">{{partial:gs-grafikas-es|tone=A}}</div></div>
<!-- Vertical Sticky Scrolling — two option sets (salient-core 3.1.5 tabbed_section.php):
     Sticky Aspect „Tab Links“:   data-sticky-aspect="default" data-nav-width="regular|wide|narrow" data-nav-spacing="15px…45px"
                                  data-m-display="hidden|visible" data-tab-spacing="5%…20%|10px|20px" (+ CTA: <li class="vs-cta"> with a Button)
                                  → 1 px track + 3 px indicator, links .45 → 1, nav hidden < 1000 px (used on /taisykles/, /privatumo-politika/)
     Sticky Aspect „Tab Content“: data-sticky-aspect="content" data-content-animation="fade" data-link-animation="opacity|outline_fill" data-nav-width="25|30|40"
     Tab Content Animation / Tab Link Animation do NOT exist for Tab Links. -->

<!-- Page Submenu (becomes fixed under the header; scrollspy sets .current-menu-item, C-8 draws the red line) -->
<div class="wpb_row" data-type="full_width_content" data-salient="Row → Page Submenu"><div class="row_col_wrap_12"><div class="wpb_column vc_col-sm-12"><div class="vc_column-inner">
  <nav class="page-submenu" data-sticky data-alignment="left" style="--bg:#0F1417;--link:#F2F4F3" aria-label="Puslapio skyriai">
    <div class="container"><ul><li><a href="#faktai">Faktai</a></li> …</ul></div></nav></div></div></div></div>
```

**Sticky Content Sections** (`data-enabled="desktop tablet"` default; excluded devices and reduced motion stack the sections):

| Type | Container attributes | Child `.nectar-sticky-media-section` |
|---|---|---|
| Sticky Media, Scrolling Content | `data-type="default" data-content-position="right|left" data-media-width="40|45|50" data-media-height="60vh|70vh|80vh" data-content-spacing="20vh|30vh|40vh"` | `data-section-type="image"` > `.nsms-bg` (the media, cloned into the sticky column) + `.nectar-sticky-media-section__inner` (text) |
| Sticky Scroll Pinned Sections | `data-type="scroll-pinned-sections" data-effect="none|overlapping|scale|scale_blur|fade_scale" data-stacked data-nav data-overlap="50" data-section-height="70vh|80vh|85vh|90vh" data-subtract-nav data-content-alignment="middle|stretch|top|bottom"` (Content Alignment: the section is a flex column; Stretch fills it with the Inner Row) | `data-section-type="color" style="--bg:#161D21" data-text-color="light" id="…" data-title="…"` (or `image` with `.nsms-bg`) |
| Horizontal Scrolling | `data-type="horizontal-scrolling" data-section-width="35|45|60|75" data-gap="8|16|24" data-subtract-nav` | + optional Link: last child `<a class="nsms-link" href aria-label>` and `data-indicator-text="Plačiau"` (Link Mouse Indicator) — `{{paslaugos:hscroll}}` renders the home H3 set |
| Layered Card Reveal | `data-type="layered-card-reveal"` | basic emulation only (H9 is disabled) |

**Forms** — Fluent Forms markup (`form.fluentform` > `.ff-el-group` > `.ff-el-input--label > label` + `.ff-el-form-control` + `.error.text-danger`), `data-demo-form` (never sends; shows `.ff-message-success`). Use `{{partial:gs-uzklausa|id=…|media=…}}`; the tracking form uses `data-demo-form="tracking"` (redirects to `?kodas=`), results in `[data-demo-result]` with `[data-demo-result-ok]` / `[data-demo-result-none]` / `[data-demo-code]` (demo.js).

## 6. Page CSS and the custom budget

- **Page CSS is discouraged** (Wave 3: no page uses it; `assets/css/pages/` is gone). A kit page may have `css: pages/x.css` with **≤ 15 non-blank lines of demo-only spacing** (`check.py` fails above that). If you cannot name the Salient option that produces an effect, it either becomes a numbered group in `assets/css/sgp-custom.css` (shared implements it on request — write component, attribute, expected behaviour in your hand-off note) or it does not ship.
- **What counts toward the budget:** only `assets/css/sgp-custom.css` (limit 250 non-blank lines incl. comments, `check.py` hard stop 260; now **178** after Wave 3: C-2 tab fade, C-5 selector fix, C-7 phone markers) and `assets/js/sgp-custom.js` (limit 30, hard stop 40; now **28**). They are pasted verbatim into *Theme Options → Custom CSS / Custom JS (Head)*.
- **What does not count:** `theme-options.css` (Theme Options fields), `emul/*.css` + `emul.js` (Salient itself), `demo.css` + `demo.js` (demo-only: „Salient žymės“, demo forms, cookie memory), inline Design-Options variables and `data-*` options (element settings).
- Current groups: C-1 tokens · C-2 reduced motion · C-3 Lithuanian typography · C-4 call bar · C-5 schedule rows · C-6 Fluent Forms · C-7 hotspots · C-8 Page Submenu · C-9 Complianz · C-10 header call button · C-11 focus · C-12 ticker · C-13 pause state · C-14 pause button; J-1 reduced motion, J-2 motion pause.

## 7. Build placeholders (`tools/build.py` + `tools/kitlib.py`)

| Placeholder | Output |
|---|---|
| `{{partial:name\|k=v\|k2=v2}}` | partial; inside it `{{param:k=default}}`, `{{#if:k=v}}…{{/if}}`; `tone=A\|P` also sets `tone_text` (light/dark), `tone_bg`, `tone_hover`, `tone_class` (sgp-dark), `tone_label` (#EF4539/#C4301E). **No spaces in values.** |
| GS partials | `gs-isvykimai` (in the header) · `gs-artimiausi` (hero glass band) · `gs-telefonai` (mega menu + off-canvas) · `gs-paslaugu-meniu` · `gs-grafikas-ie` / `gs-grafikas-es` (`tone`) · `gs-marsrutai` (`cols=2\|3`, `tone`, `pt`, `pb`, `pbm`) · `gs-paslaugos` (`tone`) · `gs-pasitikejimas` (`id=kodel-mes`, `cc=1` adds Color Change Section) · `gs-kvietimas` · `gs-uzklausa` (`id=uzklausa`, `media=36377055`) · `gs-skambuciu-juosta` (automatic) · `gs-poraste` (automatic) · `gs-404` |
| `{{grafikas:ticker}}` · `{{grafikas:next\|dir=ie\|es}}` (+ `\|back` for the inbound date, or `route=lt-ie`) · `{{grafikas:rows\|routes=lt-ie,ie-lt\|tone=A\|P}}` · `{{grafikas:updated}}` · `{{grafikas:note}}` | the text an editor types monthly (snapshot at `render_today` in `src/data/grafikas.json`): full dates („spalio 9 d.“), never relative words, no client-side recompute |
| `{{paslaugos:menu}}` · `{{paslaugos:rows\|tone=A\|P}}` · `{{paslaugos:hscroll}}` · `{{paslaugos:pinned}}` · `{{paslaugos:related\|slug=…}}` · `{{paslaugos:footer\|slugs=a,b}}` · `{{paslaugos:options}}` | mega-menu columns · Link rows ×11 · home H3 horizontal sections · P3 pinned groups (group key = section id) · 3 Fancy Box columns · footer link list · form `<option>`s |
| `{{bgimg:ID\|w=1920\|pos=50% 50%\|phone=ID\|phone-pos=…\|eager\|overlay=CSS}}` | Row/Section background: `.row-bg-wrap > .inner-wrap > .row-bg-layer > img` (+ phone image ≤ 690 px) + `.row-bg-overlay` |
| `{{bgvideo:ID\|eager\|phone=PHOTO_ID\|overlay=CSS}}` | poster image (phones, reduced motion, before play) + lazy MP4 (desktop only, `data-src`, started by emul.js, paused by the pause button) — one HD file, no SD/HD |
| `{{colbg:ID\|w=\|sizes=\|pos=\|overlay=#0B0E10\|o=.72\|oh=.42}}` | Column background image + Color Overlay (Opacity → Opacity Hover) |
| `{{img:ID\|w=\|sizes=\|pos=\|eager\|decorative\|alt=\|class=}}` · `{{videourl:ID}}` · `{{poster:ID}}` · `{{alt:ID}}` · `{{icon:name\|class=}}` | responsive image · lightbox MP4 (HD) · poster · alt · own line icons (`phone arrow arrow-up-right arrow-down download play pause times dash mail calendar seat heat air shield rest box route paw heart cage search pin tag truck check menu close`) |
| Refused on kit pages | `{{grafikas:board\|stub(s)\|tickets\|lane\|timetable\|table\|data}}`, `{{partial:board*\|map-*\|phero-calls\|arrival\|sprite}}`, `sd-only` / `q=sd`, front matter `js:` |

## 8. Legacy stack — deleted in Wave 3

All 21 pages are on the kit, so the v2 compatibility layer was removed: `src/partials/legacy/*`, `assets/css/legacy/*`, `assets/js/legacy/sgp.js`, `assets/js/pages/*.js`, `assets/css/pages/*.css` and the legacy schedule/services renderers in `tools/build.py`. `kit: salient` is now mandatory; old hand-off notes moved to `docs/build-notes/v2-archyvas/`.

## 9. `tools/check.py` rules for kit pages

Existing link / id / alt / `tel:` set / one H1 / title / description checks + on kit pages: `data-salient` on every Section/Row/Inner Row/Global Section (element roots without it are counted as a warning), no removed v2 constructs (class tokens flap/rail/ring/graticule/crop/ticket/board/stub/lane/switchboard/callpanel; `popover`, `data-sd/-hd`, „po N d.“, `sgp_grafikas`, `Raw HTML`, `Inter Tight`, `sgp-mono`, „Fullscreen Split“ without Cover, `Centered Menu`, `Before Footer`, Pinned + „Stacking“, `(Line)`, `Fancy Box … minimal`, `18.3`), every `tel:` link has an `aria-label`, no `<video autoplay>`, background video ⇒ a `.sgp-motion-toggle` on the page, page CSS ≤ 15 lines. Repository: sgp-custom.css ≤ 260 (reported), sgp-custom.js ≤ 40, no radius > 4 px (except 50 % circles and lines marked `radius-ok`) and no text under 12 px in the kit CSS.

## 10. Known gaps of the emulation (flag, don't work around)

- Emulation ≠ theme DOM: class names follow Salient, the inner markup is simplified (e.g. `a.nectar-cta` instead of `div.nectar-cta > span.link_wrap > a.link_text`). C-2/C-5/C-7/C-8/C-10 selectors must be verified on staging.
- Header Mega Menu GS *Mobile* is not used (18.2.1: incompatible with fullscreen off-canvas) — phones use the off-canvas meta area + call bar.
- Layered Card Reveal and Fancy Box Parallax Hover are basic emulations; Flickity needs `vendor: flickity`.
- Map labels inside `marsrutai.svg` use a system condensed stack (web fonts do not load in an `<img>` SVG).
- Color Change Section: while a chapter is below 40 % visibility its text sits on the previous chapter's colour (Salient behaves the same) — keep chapters tall enough.
- Scroll-linked effects (parallax, clip path, pinned/horizontal sections) run on desktop/tablet; phones get the static stack (Theme Options *Disable Parallax Backgrounds On Mobile*).
- **Don't nest entrance animations inside a Mask Reveal column** (Image/Icon animations inside an Inner Column with Background Layer Animation Mask Reveal) — the mask *is* the entrance; the nested one waits for the clip and starts ~2 s late.
- A Pinned Section taller than `100vh − header` never shows its bottom while stuck (Salient behaves the same) — keep sections within ≈ 600 px at 1366×768; no automatic guard in the emulation.
- Back To Top: Theme Options → Functionality → Back To Top Button ✓, Keep On Mobile ✗ (the call bar owns the bottom of phones).
