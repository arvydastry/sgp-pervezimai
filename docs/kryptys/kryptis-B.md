# Kryptis B — „Inžinerinis tikslumas“ (Industrial Precision)

**Project:** SGP pervežimai, v2 redesign demo · **Target build:** WordPress + Salient 18.3 (Salient WPBakery 8.7.3, Salient Core 3.1.6)
**Files:** this spec · style tile / mini home preview → `docs/kryptys/kryptis-B.html` (open via the local server so `../../assets/img/logo*.svg` resolve)
**Date:** 2026-09-23 · **Status:** concept for client selection (one of three directions)

Notation used in this document:
- **Content sources:** `[P: …]` = `turinys-puslapiai.md`, `[S: slug]` = `turinys-paslaugos.md`. Quoted Lithuanian in „…“ is verbatim. Anything new is marked **NEW** and repeated in § 13.
- **Media:** `#id` = Pexels id from `media.json`. `v#id` = a video.
- **Effects:** written as *trigger → property from→to, duration, easing, delay/stagger*. Easing names are the Salient/jQuery names from § 1.8.
- **Salient:** `Element › option: value`, using the v18 names from `salient-elementai.md`. **Custom** means a class plus a snippet from § 14.

---

## 0. The direction in one page

**Concept (3 sentences).** SGP is a scheduled operator with two fixed lines, Lithuania ⇄ Ireland and Lithuania ⇄ Spain, so B presents the company the way a well-run European transport operator documents itself: a visible drafting grid, timetable rows, a route schematic and key–value spec sheets. Type is a tall, condensed grotesk on cool steel-grey paper, graphite does the structural work and SGP red is reserved for signals. The logo's parallel red strokes become the connective system: three "lane lines" draw every route, underline every link and physically connect „Lietuva“ to „Airija“ and „Ispanija“ in the hero headline.

**Why it fits SGP's audience.**
- The audience is Lithuanians in Ireland, the UK and Spain and their families at home. They come for four things: can I trust them, when is the next departure, who do I call, and what am I allowed to send.
- B answers these in that order, above the fold on every device:
  - the departure board sits in the hero;
  - the two phone "lines" (Airija / Ispanija) are the primary CTAs;
  - rules and prohibited items are scannable spec lists, not walls of text.
- The engineered look signals "serious operator" without a single invented number. Every figure on the page is derived from SGP's own content:
  - 2 lines;
  - 4 transit countries;
  - 11 services;
  - 3–4 days on the road;
  - the dates in the schedule.

**How B differs from v1 (the banned signature moves):**

| v1 did | B does instead |
|---|---|
| Warm beige `#EFEDE8` + yellow `#FFC21A`, Inter Tight | Cool steel paper `#EDEFF1` + graphite `#16181A`, with SGP red `#EF4539` as the only accent. Type is Sofia Sans Extra Condensed, Sofia Sans and JetBrains Mono. |
| Giant centred all-caps stacked slogan filling the hero; hero colour morph | The hero is a dark full-bleed drone video under a hairline grid. The headline is left-aligned, sentence case, on a 2-row grid: „Lietuva“ connects through red lane lines to „Airija“ / „Ispanija“. A glass departure board sits on the right. No colour morph. |
| Video card scaling up under the hero; rotating circular badge | No scaling media cards and no badges. Photography sits inside square frames with viewfinder corner ticks and moves in parallax *within* the frame. |
| Services as full-width rows with a cursor-following image | Services are 6 sticky **stacking spec sheets** (Sticky Content Sections › Stacking) with a sticky index column. No cursor-following media anywhere. |
| Word-by-word highlighted "about" statement on black | The about statement is a light spec sheet: word-mask reveal once, plus a key–value company datasheet. No scroll-lit words. |
| Two tall parallax route cards | A route schematic (transit-map style, drawn on scroll) plus a 2-way toggle datasheet. |
| Outlined/solid giant marquee | No marquee. The only repeating band is the thin mono utility bar. |
| 4 white "step" cards | Process = Sticky Media, Scrolling Content (the media swaps while numbered procedure steps scroll). |
| Yellow rounded CTA with pill checkboxes; giant footer wordmark | Graphite CTA with phone "lines" and a boxed, labelled form (select, not pills). The footer is a quiet 12-column index with no wordmark. |

---

## 1. Design tokens

### 1.1 Colour

| Token | Hex | Role | Contrast / usage notes (WCAG 2.2) |
|---|---|---|---|
| `--paper` | `#EDEFF1` | Base light background (cool, never beige) | `--ink` on it **14.7:1**, `--steel` **5.1:1** |
| `--paper-2` | `#E2E5E8` | Alternate light section (services), zebra rows | ink 13.4:1, steel 4.6:1 (AA body OK) |
| `--sheet` | `#F7F8F9` | Cards, spec sheets, light form fields | steel 5.5:1, red-ink 5.0:1 |
| `--mist` | `#C9CED3` | Field borders, blueprint (dashed) paths, disabled | Non-text only |
| `--hair` | `rgba(22,24,26,.12)` | Hairlines on light; `--hair-2` .22 for component borders | — |
| `--steel` | `#5E666E` | Secondary text and captions on light, placeholders | ≥ 4.6:1 on every light surface |
| `--steel-2` | `#8A929A` | Inactive route branch; secondary text **on dark** | 5.6:1 on graphite; never as text on light (2.7:1) |
| `--ink` | `#1C1D1D` | SGP near-black: primary text, 1px section rules | — |
| `--graphite` | `#16181A` | Dark sections, primary-button hover fill, **text on red** | On red **4.73:1** ✓ |
| `--graphite-2` | `#222528` | Dark cards, dark form fields | paper on it 13.4:1 |
| `--graphite-3` | `#2E3236` | Borders on dark | Non-text |
| `--graphite-0` | `#0F1011` | Footer | fog on it 8.7:1 |
| `--fog` | `#A9B0B7` | Secondary text on dark | 8.1:1 on graphite |
| `--red` | `#EF4539` | Brand signal: primary CTA fill, lane lines, route, markers, active states, large display accents | Red on graphite **4.73:1** ✓ (small text allowed on dark). Red on paper **3.26:1**: only large text (≥ 24px, or 18.7px bold) and UI graphics (≥ 3:1). **White on red is 3.76:1, so it is never used**: text on red is always graphite. |
| `--red-ink` | `#C8321F` | Small red text on light: route codes, clause numbers, link hover | 4.63:1 on paper, 5.0:1 on sheet ✓ |
| `--ok` | `#2F7D5B` | Form success border (text inside is `#CFE9DC`, 12:1) | Border only |

**Rules**
- Red covers at most ~5% of any viewport. It never fills a section and never appears as body text on light surfaces.
- Surface rhythm on Home, dark→light→dark:
  - hero `graphite`/video
  - tracking `graphite-2`
  - about `paper`
  - routes `paper`
  - services `paper-2` (cards alternate `sheet` / `graphite`)
  - band photo+graphite
  - process `paper`
  - rules `sheet`
  - testimonials placeholder `paper-2`
  - contact `graphite`
  - footer `graphite-0`
- Inner pages start **light**, with the page hero on `paper`. The contact band and footer are always dark.
- Focus ring: `2px solid var(--red)` with a 3px offset. It is 3.26:1 on paper and 4.7:1 on graphite, so it passes the 3:1 non-text rule on both.
- Salient colour slots:
  - Accent `#EF4539`
  - Extra Color 1 `#16181A`
  - Extra Color 2 `#C8321F`
  - Extra Color 3 `#EDEFF1`
  - Overall BG `#EDEFF1`
  - Body text `#1C1D1D`

### 1.2 Typography

Three Google families. Each ships the **latin-ext** subset, which covers ą č ę ė į š ų ū ž, and all were checked rendering Lithuanian caps and lowercase.

| Role | Family | Weights | Why |
|---|---|---|---|
| Display (H1–H3, numerals, route names, phone numbers) | **Sofia Sans Extra Condensed** | 700, 800 | Tall, rational, engineered condensed grotesk; tabular-looking figures; very good ogonek/caron design. Native family, so Salient can select it directly (no width-axis hacks). |
| Text & UI (body, nav, buttons, forms) | **Sofia Sans** | 400, 500, 600 | Same superfamily; calm at 16–21px; good Lithuanian diacritics. |
| Technical labels (section §, route codes, captions, table keys) | **JetBrains Mono** | 400, 500 | Crisp at 10–12px uppercase; the "spec-sheet" voice. |

Google Fonts URL (as used in the tile):
`https://fonts.googleapis.com/css2?family=Sofia+Sans+Extra+Condensed:wght@700;800&family=Sofia+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap`

**Salient setup** (Theme Options › Typography, Local Google Fonts ON):
- **Body:** Sofia Sans 400, 17px / 1.6 (desktop), 16px (phone).
- **Navigation:** Sofia Sans 500, 15px.
- **H1–H3:** Sofia Sans Extra Condensed 800, letter-spacing −0.005em, line-height 0.92–0.95.
- **H4–H6:** Sofia Sans 600.
- **JetBrains Mono:** Salient only enqueues fonts that are assigned to a typography slot. Assign JetBrains Mono 500 to an unused slot (e.g. "Portfolio filters" or "Sidebar/Carousel header"), or enqueue it in the child theme. It is then applied through the custom class `.sgp-label` (§ 14).
- **Fluid Typography** [CL 18.0]: ON, with the clamps below.

**Type scale (fluid):**

| Style | Family / weight | Size (clamp) | px at 390 → 1440 | Line-height | Tracking | Case |
|---|---|---|---|---|---|---|
| Hero H1 | SSXC 800 | `clamp(3.2rem, 14.4cqi, 8.5rem)`: sized to its 8-column container, so it never overflows. Phone: `min(20cqi, 4.8rem)` | ~72 → ~128 | 0.92 | −0.006em | Sentence |
| Display D1 (inner page H1) | SSXC 800 | `clamp(3rem, 1.5rem + 5vw, 7rem)` | 48 → 96 | 0.92 | −0.005em | Sentence |
| H2 | SSXC 800 | `clamp(2.6rem, 1.4rem + 3.9vw, 5.75rem)` | 42 → 79 (max 92) | 0.92 | −0.004em | Sentence, `text-wrap: balance` |
| H3 / card title | SSXC 800 | `clamp(2rem, 1.3rem + 2vw, 3.5rem)` | 32 → 50 | 0.95 | 0 | Sentence |
| Statement (band) | SSXC 800 | `clamp(2.6rem, 1rem + 4.6vw, 6.25rem)` | 42 → 82 | 0.94 | 0 | Sentence |
| Data numeral | SSXC 800 | `clamp(3rem, 2rem + 3vw, 5rem)` | 48 → 75 | 0.8 | 0 | Figures |
| Sub-display (phone numbers, route names) | SSXC 700 | 21–26px | — | 1.05 | +0.01em | As written |
| H4 | Sofia Sans 600 | `clamp(1.25rem, 1.1rem + .5vw, 1.625rem)` | 20 → 25 | 1.2 | 0 | Sentence |
| Lead | Sofia Sans 400 | `clamp(1.0625rem, 1rem + .35vw, 1.3125rem)` | 17 → 21 | 1.5 | 0 | — |
| Body | Sofia Sans 400 | `clamp(1rem, .95rem + .15vw, 1.0625rem)` | 16 → 17 | 1.6 | 0 | — |
| Small / captions | Sofia Sans 400 | 14px | — | 1.4 | 0 | — |
| Label | JetBrains Mono 500 | 11px (`.lbl`), 12px (`.lbl-m`) | — | 1.35 | +0.08–0.09em | UPPERCASE |
| Button | Sofia Sans 600 | 15px (14px in header) | — | 1.1 | +0.005em | Sentence |

**Case rules**
- Headlines are always sentence case, never all caps. This is a deliberate break from v1.
- Uppercase is reserved for mono labels.
- Numbers keep Lithuanian formatting: „3–4 paros“, „spal. 09“.
- Phone numbers are grouped for reading: +370 650 53161 · +353 86 450 3104 · +44 7566 878681 · +34 602 547 929.
- Measure: body 60–70ch, lead ≤ 34em.

**Diacritics safety:** word-mask reveals use `padding: .2em 0 .08em; margin: -.2em 0 -.08em` on the clipping span, so carons on capitals (Š, Ž) and ogoneks (Į, Ą) are never cut at line-height 0.92.

### 1.3 Spacing

4px base: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 160`.
- **Section padding (vertical):** `clamp(88px, 9vw, 152px)`. Section head → content: `clamp(44px, 5vw, 80px)`.
- **Components:**
  - Card padding: `clamp(22px, 2.4vw, 34px)`.
  - Buttons: 54px tall, padding `0 18 0 22`.
  - Phone lines: 62px tall, with a 54px icon cell.
  - Fields: 54px tall.
  - Table rows: 15px vertical padding.
- **Stack gaps:** 8 (dense lists), 16 (form), 22 (cards), 28 (hero blocks).

### 1.4 Grid & layout

| | Desktop ≥ 1000 | Tablet 691–999 | Phone ≤ 690 (fine-tune ≤ 600) |
|---|---|---|---|
| Columns | 12 | 8 | 4 |
| Gutter | 24px | 16px | 12px |
| Side margin | `clamp(16px, 3.4vw, 48px)` | same | 16px |
| Max content width | 1440px | — | — |

- **Hairline grid (signature S1):** vertical 1px lines at the centre of every gutter, plus the outer edges (so text sits `gutter/2` off the line).
  - Colour `rgba(22,24,26,.075)` on light, `rgba(255,255,255,.075)` on dark.
  - Registration crosses (9px "+") sit on lines 1 and 7 at each section's top edge.
- **Section head pattern:** mono label `§ 0X  Name` in columns 1–3, the H2 in columns 4–12 and the intro in columns 4–9. On tablet and phone everything stacks.
- **Salient:**
  - Theme Options › Max Container Width 1440, Extended Responsive ON.
  - Rows: Column Margin **custom 24px**.
  - Rows that show the grid get the Extra Class `sgp-grid`, plus `sgp-grid--x` for the registration crosses (§ 14-A). The grid is drawn by a pseudo-element, so no extra markup is needed.

### 1.5 Radii, borders, shadows

- **Radius:**
  - 2px on buttons, fields, cards, the board and the segmented control.
  - 0 on images and sections.
  - No pills and no circles, except the transit-stop marker.
- **Borders:**
  - Structure: 1px `--hair` / `--hair-2`.
  - Section/table heads: 1px `--ink` rule on light, 1px `--hair-d2` on dark.
  - Field focus: `inset 3px 0 0 var(--red)` plus the border turning ink.
- **Shadows** are used once only, on the stacking service cards: `0 1px 0 rgba(22,24,26,.04), 0 30px 60px -40px rgba(22,24,26,.35)`. Elsewhere, depth comes from the grid, the overlays and parallax. No glows and no blurred colour blobs.
- **Glass:** only on the hero departure board and the hero phone lines: `backdrop-filter: blur(16px) saturate(1.15)` over `rgba(18,19,21,.56)`, with a 1px border at 12% white. Salient: Inner Row › Backdrop filter [CL 18.0].

### 1.6 Iconography

- **Style:**
  - Custom inline SVG line icons on a 24px grid.
  - **1.5px stroke, butt caps, miter joins**, `currentColor`.
  - Drawn as engineering pictograms, not playful ones.
- **Set needed (15):** phone, arrow-right, arrow-up-right, close, menu, pause, play, search/track (crosshair), download, box, pallet, car-on-trailer, motorcycle, seat, pet-carrier, home-move, check, prohibited (circle-slash).
- Arrows in buttons use the **double-arrow swap**: the outgoing arrow slides right while the incoming one slides in from the left, 450ms easeInOutCubic.
- **Salient:** upload the SVGs and use them through the Icon element (image option) or inline in Raw HTML. Fallback: Iconsmind line icons, stroke-matched via CSS.
- **Never:** emoji, filled glyph icons, Flaticon mixed styles or Font Awesome solid.

### 1.7 Image treatment

- **Grade ("cool operator"):** saturation −20%, contrast +5%, a slight cool white balance (−200K), blacks lifted to `#0F1011`. Bake the grade into the exported WebP; the CSS fallback in the tile is `filter: saturate(.8) contrast(1.05)`.
- **Overlays on dark media:**
  - Hero: three stacked gradients:
    - top `rgba(15,16,17,.72)→0` over 26%;
    - bottom `rgba(15,16,17,.92)→.35` at 34% `→0` at 60%;
    - left `rgba(15,16,17,.78)→.38` at 46% `→.05` at 78%.
  - Band: bottom `.95→.55` at 45% `→.35`, plus left `.6→0`.
- **Framing:**
  - Photos always sit in square-cornered frames with **viewfinder corner ticks** (12px, 1px; signature S5).
  - A mono caption sits under or inside the frame: „Pav. 0X — Airija“.
  - Inner parallax: the image is 120% tall and translates at 0.07–0.08 of the scroll.
- **Hover:** scale 1.02→1.07 over 1400ms easeOutExpo; the corner ticks move inward 6px over 450ms.
- **Honesty rule:** stock photos are mood, not claims. Captions never say „mūsų vairuotojas“ or „mūsų autoparkas“. When SGP provides real photos of its minibuses and drivers, they replace #6720534, #7541981 and #27383867 first.

### 1.8 Motion tokens

| Token | Value | Salient mapping | Used for |
|---|---|---|---|
| `--e-out` | `cubic-bezier(.19,1,.22,1)` | Column/Image Animation Easing **easeOutExpo** | Reveals, masks, word reveals, line draws |
| `--e-io` | `cubic-bezier(.645,.045,.355,1)` | easeInOutCubic (custom per column [CL 15.0]) | Hover wipes, button fills, row fills |
| `--e-q` | `cubic-bezier(.165,.84,.44,1)` | easeOutQuart | Small nudges (4px shifts) |
| `--d1` | 180ms | — | Colour changes |
| `--d2` | 320ms | — | Hover transforms, row fills |
| `--d3` | 450ms | — | Wipes, underline draws, arrow swaps |
| `--d4` | 900ms | — | Image zoom out on reveal |
| `--d5` | 1200ms | Column/Image Animation Timing **1200** | Section entrances |
| Stagger | 45ms grid lines · 60ms lane lines · 70ms words · 120ms columns/cards | Column Delay 0/120/240/360; Animated Text Stagger | |
| Trigger | Element top at 88% of the viewport (IO `rootMargin: 0 0 -12% 0`) | Salient default waypoint offset | |
| Parallax | Hero bg 0.22 (Subtle) · band 0.30 (Medium) · in-frame images 0.07–0.08 (Image › Scroll movement Move Y, intensity 2) · labels −0.05 (optional) | Row › Parallax Background Media On Scroll | |
| Smooth scroll | Lenis 1.1.13, lerp 0.1 | Theme Options › Smooth Scrolling ON, strength 60 | |

**Never animated:**
- body text after it has appeared;
- phone numbers (no scrambling or typing);
- the prices and dates in the timetable;
- any looping ornament. Nothing spins and nothing pulses forever.

---

## 2. Signature system (unique to B)

**S1 — Drafting grid + column ruler + registration crosses**
- **What:** visible 12-column hairlines, plus a mono ruler „01 … 12“ under the header on hero-type rows. 9px "+" crosses sit on the section top edges (lines 1 and 7).
- **Motion:** on page load the hero lines draw top→bottom (scaleY 0→1, 1400ms easeOutExpo, stagger 45ms, right edge last at +600ms). The ruler digits fade in with a 40ms stagger. The lines of the other sections are static.
- **Salient:** Row Extra Class `sgp-grid` (static gradient version) or `sgp-grid sgp-grid--draw` (13 spans injected by 15 lines of JS). The ruler is a Raw HTML element. See § 14-A.

**S2 — Lane lines (from the logo mark)**
- **What:** three parallel 2px red strokes with 3px gaps (the logo's nested-line motif). Uses:
  - the prefix glyph of every section label;
  - the hero connector;
  - the route trunk;
  - hover markers (the left bar on rows, the underline on phone lines);
  - card-link markers.
- **Motion:** each stroke scaleX 0→1 in 700ms easeOutExpo, stagger 60ms, when entering the viewport.
- **Salient:** inline `<span class="sgp-lanes"><i></i><i></i><i></i></span>` inside Text blocks. Route lines are SVG. See § 14-B.

**S3 — Route schematic with waypoint markers**
- **What:** a transit-map diagram: LT → PL → DE → BE → FR, then branching to IE and ES.
  - Origin and destinations use **concentric squares**, echoing the nested logo: 28px red / 16px paper / 6px red.
  - Transit stops are 10px paper circles with a 2.5px ink stroke.
  - Each segment is a triple-lane path with rounded 90° corners.
  - A dashed `--mist` blueprint path shows beneath before drawing.
  - A mono note reads „Schema, ne mastelis“.
- **Motion (scroll-scrubbed):** the trunk draws over the first 60% of progress (stroke-dashoffset L→0). Both branches draw from 45% to 95%. The active branch is red and the inactive one `--steel-2`; the inactive terminus drops to 35% opacity. Toggling a route recolours in 500ms easeInOutCubic.
- **Salient:** preferred is **Lottie Animations › Trigger: Scroll Position Seek**, with the SVG exported to Lottie (frames 0→100 = draw), a desktop JSON (1344×320) and a vertical phone JSON (360×690) switched with device visibility. The alternative is Raw HTML SVG plus a custom scrub script (§ 14-E).

**S4 — Timetable rows + date chips**
- **What:** departure-board rows, with columns `code (mono, red) | destination (SSXC 700) | date chips | →`.
  - A **date chip** is a 40px-wide box: the day number in SSXC 800 (21px) over the month abbreviation in mono 8.5px („spal.“, „rugs.“).
- **Hover, dark variant (hero board):** background 6% white plus a 3px left red bar growing scaleY 0→1 from the bottom, 320ms easeInOutCubic.
- **Hover, light variant (grafikas page):** a graphite fill rises from the bottom (scaleY 0→1, 380ms easeInOutCubic). Text turns paper, the codes turn `--red` and the left red bar widens 4→10px.
- **Salient:** Horizontal List Item › Style "Bottom Border, Color Hover Effect" (native fill flip), colour set to graphite. The chips are HTML inside the column text (`.sgp-date`, § 14-C). Rows are fed from one **Global Section „Grafikas“** so the dates are edited in one place.

**S5 — Spec sheets**
- **What:** key–value datasheets.
  - Key in `--steel`, value in ink 500, 15px rows with 1px hairlines.
  - A heading bar with a 1px ink rule and a mono reference („Maršrutas 01“).
  - § section labels and „Pav. 0X“ figure captions.
  - **Viewfinder corner ticks** on photos and on the board/form panels.
- **Motion:** sheets fade up 28px in 1000ms. Tabbed sheets swap with opacity 0→1 and translateY 12→0 in 600ms easeOutExpo.
- **Salient:** Text block with `<dl class="sgp-kv">` (§ 14-D), Column/Image Extra Class `sgp-ticks`.

---

## 3. Component inventory (all states)

### 3.1 Header (Global: Theme Options › Header Navigation)

- **Structure (desktop):**
  - **Utility bar**, 36px (Secondary Header Bar), mono 11px uppercase:
    - left: „SGP — saugiai · greitai · patikimai“;
    - right: `IE +370 650 53161` · `ES +370 638 28919` · `Siuntos sekimas →`. The route codes are in red.
  - **Main bar**, 76px:
    - logo, 132px wide;
    - the nav centred;
    - a primary button on the right.
- **Nav items:** Apie mus · Paslaugos (mega) · Kryptys · Grafikas · Taisyklės · Kontaktai. Each has a mono index superscript 01–06 at 55% opacity.
- **States:**
  - **Transparent (on a dark hero):** paper text, `logo_light.svg`, utility border 12% white.
  - **Transparent (on a light inner hero):** ink text and `logo.svg`, via *Header Inherit Row Color* from the first row's Text Color: Dark.
  - **Scrolled (> 60px):** the utility bar slides away (translateY −36px); the bar gets `rgba(237,239,241,.86)` + blur 14px + a 1px `--hair` bottom border; ink text and the dark logo.
  - **Hidden (scrolling down > 420px):** the header translates up by its full height in 600ms easeOutExpo. It comes back on any upward scroll (*Hide Until Needed*).
- **Link hover:** Salient *Header Link Hover Effect: Text Reveal*. The label rolls up and a red duplicate rolls in (450ms easeInOutCubic).
- **Active page:** a 2px red lane under the label (custom class `current-menu-item`).
- **Focus:** red ring.
- **Mobile (≤ 1000):** 64px bar with the logo, an icon button „Skambinti“ (tel: the Ireland line) and a burger. The utility bar is hidden.
- **Salient:**
  - Header Layout **Centered Menu**; Transparent Header ON; Header Inherit Row Color ON.
  - Background blur ON; Hide Until Needed ON; Resize On Scroll OFF.
  - Header Navigation Entrance Animation: Fade In, 300ms delay.
  - The header button is a menu item with the button class `sgp-btn`.
  - Mega menu „Paslaugos“: a Global Section with 6 groups × links (mono indices), plus a mini spec line „Kelyje apie 3–4 paros · Nuo durų iki durų“.

### 3.2 Off-canvas menu

- **Salient:** Off Canvas Menu **Slide Out From Side** (right), width 440px (100% on phone), bg `--paper`, ink text, overlay `rgba(15,16,17,.5)`.
- **Content:**
  - a list of 7 links, each a row: `mono index | SSXC 800 34px label | →`, with hairlines;
  - a Global Section "phone dock" with 2 phone lines („Pervežimai į Airiją“, „Pervežimai į Ispaniją“).
- **Motion:** the panel slides in 700ms easeOutExpo. Links fade up with a 40ms stagger.
- **Hover:** the label turns red-ink.
- **Accessibility:** Esc closes, focus moves to the close button, and focus returns to the burger on close.
- This differs from v1's dark full-screen overlay.

### 3.3 Buttons

| Variant | Default | Hover / focus-visible | Active | Disabled |
|---|---|---|---|---|
| **Primary** `.sgp-btn` | Red fill, graphite text, 2px radius, 54px tall, double-arrow icon | A graphite fill wipes in from the left (scaleX 0→1, 450ms easeInOutCubic); text turns paper; the arrows swap. **On dark:** the fill is paper and the text graphite. | translateY 1px | 40% opacity, no wipe |
| **Ghost** `.sgp-btn--ghost` | Transparent, 1px `--hair-2` inset border, text currentColor | An ink fill (paper on dark) wipes in from the left; text inverts; the border disappears | same | same |
| **Text link** `.sgp-tlink` | Weight 600; 1px underline at 30% | A 2px red underline draws left→right (450ms); the arrow swaps | — | — |
| **Phone line** `.sgp-line` | 62px; a 54px icon cell (5% tint) + a mono label + the number (SSXC 700, 25px); 1px border | The icon cell fills red (icon graphite); the number moves right 4px (320ms easeOutQuart); a 2px red underline draws under the text cell; the border turns ink/paper | — | — |
| **Icon button** | 46px square, 1px border | The border turns currentColor | — | — |

- **Salient:**
  - **Primary and ghost:** Button element, type *Arrow Animation*.
    - Primary colours: bg `#EF4539`, text `#16181A`, hover bg `#16181A`, hover text `#EDEFF1`.
    - The left-to-right wipe is the custom class `sgp-btn` (§ 14-F). Without it, Salient's native hover colour fade is an acceptable fallback.
  - **Text link:** Button type *Underline*.
  - **Phone line:** Button (Basic) with the custom class `sgp-line` and a `tel:` link.

### 3.4 Service spec card (stacking)

- **Anatomy:**
  - Top bar, mono: „**02** / 06 — Kroviniai“ on the left (red-ink index), „3 paslaugos“ on the right.
  - Body grid: 54% text, 46% image.
  - **Text column:**
    - H3 (SSXC);
    - verbatim lead in steel;
    - a `mini` key–value list (3 rows, mono keys);
    - the links list pinned to the bottom: each service is a row with a 1px ink top rule and hairlines between.
  - **Image column:** full-height photo with inner parallax (0.07), corner ticks 14px inset, a caption „Pav. 03 / Kroviniai“ inside at the bottom.
- **Variants:** light (`--sheet`) and dark (`--graphite`), alternating.
- **States:**
  - Card hover: the image scales 1.02→1.07 (1400ms easeOutExpo) and the ticks tighten to 8px.
  - Link row hover: padding-left 0→24px, a red 14px bar scales in, the arrow swaps.
  - Stacked (covered by the next card): the card scales 1→0.95 and a graphite overlay rises 0→0.28, driven by scroll.
  - Focus: red ring on each link.
- **Salient:**
  - **Sticky Content Sections › Sticky Scroll Pinned Sections**, Effect **Stacking**, Stacked Appearance ON, Section Navigation OFF (the index column replaces it). Effect OFF on phone.
  - Each child section: Inner Row with 2 columns.
  - Image element: Scroll movement Move Y 2, Hover *Zoom In*.
  - Links: Horizontal List Item (Style *Border Animation*) or a Text block with `.sgp-cardlinks`.

### 3.5 Route datasheet (the "route card")

- **Anatomy:**
  - Heading bar: „Lietuva **⇄** Airija“ (SSXC 800, 64px; the ⇄ is red) plus the mono ref „Maršrutas 01“, above a 1px ink rule.
  - `dl.sgp-kv` rows: Tranzitas · Išvykimai iš Lietuvos (chips) · Išvykimai iš Airijos (chips) · Kelionės trukmė · Vežame · Linija (tel links).
  - CTA row: primary „Skambinti +370 650 53161“ + ghost „Gauti pasiūlymą“.
- **Paired figure:** a 4:5 frame with corner ticks and inner parallax. On toggle the image cross-fades (700ms).
- **States:**
  - Toggle: the panel swaps with opacity 0→1 and translateY 12→0 (600ms).
  - Tel links: the underline turns red and the text red-ink.
- **Salient:** Tabs › **Toggle Button** (2 tabs, deep-linkable `#airija` / `#ispanija`) containing the Text block with `sgp-kv` + Buttons. The figure is an Image in an Inner Column with *Reveal From Left*.

### 3.6 Timetable row (S4)

- **Dark (hero board)** and **light (Grafikas page)** variants, with hover as in S4.
- **Mobile:** chips wrap under the destination; the arrow is hidden.
- **Empty or past date:** the row is hidden automatically (see § 11).
- **Salient:** as S4. Rows link to `tel:` for that route's line.

### 3.7 Data / stat block

- **Anatomy:** a mono label row („01 — Kryptys“ … a right-aligned mono detail „LT ⇄ IE · ES“), an SSXC 800 numeral (48→75px) and a 14px caption beside it.
- **Allowed values only:**
  - **2** kryptys;
  - **4** tranzito šalys;
  - **11** paslaugų;
  - **3–4** paros kelyje;
  - **7** šalys maršrutuose;
  - **5** telefono linijos;
  - **2** išvykimai per mėnesį kiekviena kryptimi: derived from the October schedule, and must be re-checked when the schedule changes.
- **Motion:** Milestone *Count To Value*, 1400ms. Delays 0/120/240/360 (plus 900ms in the hero after load). For „3–4“, count to 4 with the symbol „3–“ before it.
- **Salient:** Milestone (Count To Value, symbol before/after), with the label as a Text block above.

### 3.8 Section head

- Mono label with the lane glyph and „§ 0X“ in ink, then the name in steel (columns 1–3). The H2 is an Animated Text › Word Reveal, stagger 70ms (columns 4–12). The intro in steel sits in columns 4–9.
- On tablet and phone the three stack.

### 3.9 CTA / contact band (Global Section „CTA — Kontaktai“)

- Graphite band with the grid and registration crosses.
- **H2** (verbatim [P: Kontaktai H6]): „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“
- **Left (columns 1–6):** two groups.
  - „Pervežimai į Airiją“ (mono, with the right-aligned codes „LT · IE · UK“) and 3 phone lines labelled Lietuva / Airija / Jungtinė Karalystė.
  - „Pervežimai į Ispaniją“ with 2 lines.
  - The email as a text link.
- **Right (columns 8–12):** the form panel (`--graphite-2`, corner ticks).
- **Motion:** the groups fade up with a 120ms stagger.
- Omitted on /kontaktai/ and /privatumo-politika/, matching the old site.

### 3.10 Form fields (Fluent Forms, styled by § 14-G)

| State | Light | Dark |
|---|---|---|
| Default | bg `--sheet`, 1px `--mist`, 2px radius, 54px; label is mono 11px uppercase **above** the field (never placeholder-only) | bg `--graphite-2`, 1px `--graphite-3`, paper text |
| Hover | border `--steel-2` | border `#4A5057` |
| Focus | border ink, bg `#fff`, **inset 3px left red bar** | border fog, bg `#262a2d`, red bar |
| Invalid | border `--red-ink`; mono 11px message below in red-ink (on dark: red) | same |
| Disabled | 50% opacity, no hover | same |
| Success | panel message with an `--ok` border: „Jūsų žinutė sėkmingai išsiųsta“ [P] | same |
| Error (server) | „Oi kažkas ne taip! Bandykite dar kartą.“ [P] | same |

- **Select:** a custom chevron made of 2 CSS gradients; `appearance: none`.
- **Textarea:** min-height 120px; the placeholder uses steel (5.5:1).
- **Privacy line** (verbatim): „Formoje pateikti duomenys naudojami susisiekimui su klientu.“
- **reCAPTCHA:** v3/invisible preferred, to avoid a v2 box inside the design. The client must confirm.

### 3.11 Tracking console

- **Parts:**
  - a mono label „Siuntos sekimas“ with the lane glyph;
  - a field with the placeholder „Siuntos kodas...“;
  - the primary button „Siuntos lokacija“.
  All three are verbatim [P].
- **Behaviour:** GET → `/siuntos-sekimas/?kodas=XXXX`. That page loads the iframe `https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=XXXX`.
- **Salient:** a Raw HTML form, or Fluent Forms with a redirect to URL + query. Style `nectar-inline-subscribe-form`.

### 3.12 Inner page hero + breadcrumb

- **Surface:** light `--paper` with the grid, ruler and crosses; header in its dark variant.
- **Breadcrumb:** mono 11px uppercase „Pradžia / Pervežimo paslaugos / Tarptautiniai pervežimai / …“. The separator is „/“ in steel; the current page is ink. Salient: Text block with Yoast breadcrumbs, class `sgp-crumbs`.
- **H1:** SSXC D1 in columns 1–8, then the lead in columns 1–6.
- **Optional figure:** columns 8–12 (aspect 4:5, corner ticks). Entrance: Column Animation **Mask Reveal**, Straight, direction left, 1300ms easeOutExpo, delay 200ms. Inner parallax 0.08.
- **Spec strip:** full width, 4 cells of 3 columns each, as in 3.7, but text values instead of counters where needed.
- **Height:** auto, min 62svh desktop, padding-top = header height + 80px.
- **Dark variant:** used on Tarptautiniai pervežimai (video) and 404.

### 3.13 Sticky submenu (service pages)

- **Salient:** Page Submenu, **Sticky**. Mono 12px uppercase links, active = red-ink with a 2px red underline. Background `rgba(237,239,241,.9)` + blur.
- Anchors: Apie paslaugą · Privalumai · Kliento atsakomybės · Draudžiami daiktai · Kryptys · Užklausa.

### 3.14 Footer (Global Section, Footer location)

- **Background:** `--graphite-0`, grid lines, 12 columns.
- **Columns:**
  - **Brand (1–3):** `logo_light.svg` at 150px, „SGP – visos pervežimo paslaugos“ (verbatim [P: Apie, sidebar]) in SSXC 22px, and the mono slogan.
  - **„Tarptautiniai pervežimai“ (5–8):** all 11 service links in 2 sub-columns (verbatim [P: footer]).
  - **„Informacija“ (9–10):** Apie mus, Pervežimų grafikas, Siuntos sekimas, Taisyklės, Kontaktai.
  - **„Kontaktai“ (11–12):** a mono „Airija“ label + 3 numbers, then a mono „Ispanija“ label + 2 numbers.
- **Bottom bar**, mono 11px:
  - left: „© 2026 SGP pervežimai. Visos teisės saugomos.“;
  - right: „Privatumo politika · Į viršų ↑“.
- **Hover:** links fog→paper; phone numbers → red.
- No wordmark and no reveal effect (Footer Reveal OFF).

### 3.15 Mobile call bar (Global Section)

- Fixed to the bottom on ≤ 1000px. Three buttons: `IE Airija` (tel:+37065053161), `ES Ispanija` (tel:+37063828919), `Užklausa` (primary red, anchor to the form).
- Dark glass: `rgba(15,16,17,.94)` + blur 12px, with a safe-area inset.
- Slides up (600ms easeOutExpo) after 55% of the first viewport has been scrolled. Body padding-bottom 66px.
- **Salient:** Row › **Sticky Row: Bottom of Window**, keep on mobile, device visibility tablet + phone.

### 3.16 Testimonials placeholder

- **Label:** a `--paper-2` row with a 1px dashed `--mist` sheet and the mono label „ČIA BUS TIKRI KLIENTŲ ATSILIEPIMAI“. **NEW (required wording)**.
- **Grey stand-in:** 3 grey skeleton quote blocks (no names, no stars).
- **Production:** the row is hidden (device visibility: none) until the client supplies at least 3 real, attributable reviews. It then becomes a Testimonial Slider › **Multiple Visible Minimal** with a shadow on the active item.

### 3.17 Cookie bar

- **Layout:** a bottom-left sheet, 420px wide (full width on phone, sitting above the call bar), `--sheet` with corner ticks.
- **Content:** a mono title, then the verbatim H4 and text [P: slapukų juosta]. Buttons: primary „Sutinku“ and ghost „Plačiau“.
- **Recommendation:** add a ghost „Atmesti“ (**NEW**, a GDPR requirement for a real reject option).

### 3.18 Rules clause block (Taisyklės, Toggle Panels)

- **Clauses:** each clause number (2.1, 4.2 …) in mono red-ink, then 17px text with max-width 68ch, 1px hairlines between clauses.
- **Numbered prohibited items:** a 2-column Icon List (numbered), numbers in mono red-ink.
- **Fines:** a data table with key/value rows; „1200 EUR“ in SSXC 800 red (large-text contrast OK).

---

## 4. Global Sections (single sources of truth)

| Global Section | Used on | Notes |
|---|---|---|
| **Grafikas — kompaktiškas** (4 timetable rows, dark) | Home hero board | Dates edited once |
| **Grafikas — pilnas** (chronological light rows) | /pervezimu-grafikas/, /taisykles/, service pages (collapsed to the next 4) | Ideally fed by an ACF repeater `išvykimai[] {data (YYYY-MM-DD), kryptis (LT→IE…)}`; past rows hidden by a small PHP filter. Manual fallback. |
| **Siuntos sekimas — juosta** | Home H2, /pervezimo-paslaugos/, 404 | |
| **CTA — Kontaktai** | All pages except /kontaktai/ and /privatumo-politika/ | Fluent Form #1 (fields of the old modal 213) |
| **Maršruto schema** (Lottie desktop + phone) | Home, Tarptautiniai, Grafikas (mini), Kontaktai | |
| **Mobile call bar** | Site-wide | Sticky Row |
| **Off-canvas phone dock** | Off-canvas | |
| **Footer** | Site-wide | |

---

## 5. Page blueprints

Every page uses the same shell: Header → content → CTA — Kontaktai (unless noted) → Footer. The mobile call bar sits on top.

### 5.1 Home `/` — showpiece (12 sections)

The tile `kryptis-B.html` renders H1, H4 (with H2 folded in at its end), H5, H6, H10 and H11 exactly. H3, H7, H8 and H9 are specified here only.

**H0 · Header:** see 3.1. It starts transparent over the dark hero.

**H1 · Hero — "Dvi linijos"**
- **Purpose:** in 5 seconds, show what SGP does, where it goes, when it next leaves and whom to call.
- **Layout (desktop):** Row, Full Height (min 760px / 100svh), Full Width Background, Text Color Light.
  - Ruler under the header.
  - Left block in columns 1–8, bottom-aligned: eyebrow row → H1 → lead → CTAs.
  - Right block in columns 9–12: the departure board.
  - Bottom: a 4-cell data strip across 12 columns.
  - ≤ 1200px: the board moves under the CTAs (columns 1–7). ≤ 1000px: full width.
- **Content:**
  - Eyebrow (verbatim fragment [P: Apie įmonę]): „Keleivių, siuntų ir automobilių pervežimas“.
  - H1:
    - screen-reader text: „Keleivių, siuntų ir automobilių pervežimas: Lietuva – Airija ir Lietuva – Ispanija“;
    - visual: „Lietuva“ ⟶ lane connector ⟶ „Airija“ / „Ispanija“ (**NEW composition**; the route names come from [P]).
  - Lead (**NEW**, assembled from [P: Tarptautiniai] + [S]): „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais – nuo durų iki durų, apie 3–4 paras kelyje.“
  - CTAs: phone line „Airijos linija +370 650 53161“, phone line „Ispanijos linija +370 638 28919“, text link „Gauti pasiūlymą“ → #uzklausa.
  - Board: „Artimiausi pervežimai“ (verbatim H2 [P]); a range label „Rugsėjis – spalis“ (**NEW**, derived). The groups „Iš Lietuvos“ / „Į Lietuvą“ (**NEW**) hold the rows:
    - LT → IE, LT → ES: 09 · 23 spal.;
    - IE → LT: 28 rugs. · 15 · 28 spal.;
    - ES → LT: 27 rugs. · 14 · 28 spal.

    Footer line: „Vietą rezervuokite telefonu“ (**NEW**) + „Visas grafikas →“.
  - Data strip: 2 Kryptys („Airija ir Ispanija, abiem kryptimis“) · 4 Tranzitas („Lenkija, Vokietija, Belgija, Prancūzija“) · 11 Paslaugos („Nuo siuntų iki perkraustymo“) · 3–4 Kelyje („paros nuo paėmimo dienos“). The captions are **NEW**; the facts come from [P]/[S].
- **Media:** `v29374299` (highway interchange at dusk, drone).
  - Desktop HD 1280×720, 4.9 MB (re-encode target ≤ 3 MB).
  - Tablet SD 960, 2.6 MB.
  - Phone: poster only (poster = the media.json `poster`, w=1920/1280).
  - Fallback still: #36383706.
- **Effects:**
  - Video bg parallax: scroll → translateY at 0.22 of scroll (Subtle).
  - Load → grid lines draw (S1).
  - Load → H1 words: mask translateY 112%→0, 1200ms easeOutExpo, stagger 120ms. The connector strokes draw (dashoffset L→0, 1300ms easeOutExpo; the branch starts 350ms later).
  - Lead and CTAs: fade-up 22px, 1000/1200ms, delays 700/850ms.
  - Board: clip-path `inset(0 0 0 100%)→inset(-8px)`, 1300ms easeOutExpo, delay 500ms.
  - Data strip: fade-up with delays 900–1200ms, then counters.
  - Hovers: phone line (3.3), board rows (S4).
  - A „Sustabdyti vaizdą“ pause toggle sits in the eyebrow row (WCAG 2.2.2).
- **Salient:**
  - Row: Full Height Row (Responsive Height min 760), Video Background MP4 + preview image, Parallax Background Media On Scroll **Subtle**, Color Overlay **Advanced gradient** (3 stops, § 1.7), Extra Class `sgp-grid sgp-grid--draw sgp-grid--x`.
  - Raw HTML: ruler + H1 (§ 14-B).
  - Text: lead, Column Animation *Fade In From Bottom*, delay 700.
  - Button ×2 `sgp-line` + Button *Underline*.
  - Inner Row with Backdrop filter blur 16, Column Animation *Reveal From Right*, delay 500, containing Global Section „Grafikas — kompaktiškas“.
  - Inner Row 4 × Milestone (Count To Value).
  - Custom JS `sgp-video-toggle`.

**H2 · Siuntos sekimas strip**
- **Purpose:** gives returning senders a one-step tracking path.
- **Layout:** Row `--graphite-2`, 104px. Label in columns 1–3, form in columns 4–12 (field + button).
- **Content:** verbatim [P: Siuntos sekimas] (field „Siuntos kodas...“, button „Siuntos lokacija“).
- **Effects:** lane glyph draws on view; no other motion.
- **Salient:** Global Section „Siuntos sekimas — juosta“; Row Full Width BG `#222528`; Raw HTML GET form.

**H3 · Apie mus — company datasheet**
- **Purpose:** establishes trust and who SGP is.
- **Layout:** paper background. Section head (§ 01 Apie mus). Columns 1–5: figure. Columns 7–12: statement + datasheet + button.
- **Content:**
  - H2: „Saugiai. Greitai. Patikimai.“ (the slogan [P: Apie, H3 „Saugiai greitai patikimai“] with full stops added → **NEW punctuation**).
  - Text (verbatim [P: Apie]): „„SGP“ – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu Lietuva – Ispanija – Lietuva, Lietuva – Airija – Lietuva ir kitas Europos šalis (Vokietiją, Prancūziją).“ and „Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.“
  - Datasheet `sgp-kv` (keys **NEW**, values from [P]/[S]):
    - Veikla — Keleivių, siuntų ir automobilių pervežimas;
    - Kryptys — Lietuva ⇄ Airija, Lietuva ⇄ Ispanija;
    - Taip pat — Vokietija, Prancūzija;
    - Principas — Nuo durų iki durų;
    - Draudimas — Kroviniai ir keleiviai kelionės metu apdrausti;
    - Vairuotojai — Laikosi darbo ir poilsio režimo.
  - Button „Skaityti daugiau“ (verbatim [P]) → /apie-imone/.
- **Media:** #6720534 (driver reviewing a checklist). Caption „Pav. — Kontrolinis sąrašas“ (**NEW**).
- **Effects:**
  - Figure: Column Animation **Reveal From Left** (clip `inset(0 100% 0 0)→0`, 1300ms easeOutExpo); image scale 1.14→1 over 1800ms; inner parallax 0.08.
  - H2: Animated Text › Word Reveal, stagger 70ms.
  - Datasheet rows: Fade In From Bottom, 60ms stagger.
- **Salient:** Row paper `sgp-grid`; Column 5/12 with Image (Scroll movement Move Y 2, Mask none) inside an Inner Column *Reveal From Left*; Animated Text; Text block `sgp-kv`; Button Underline.

**H4 · Kryptys — route schematic + toggle datasheet** (in the tile)
- **Purpose:** makes the two lines and the transit countries tangible, and gives the numbers per line.
- **Layout:**
  - Section head (§ 02 Kryptys).
  - A bar with the Toggle (columns 1–5) and the legend (columns 7–12).
  - The diagram (12 columns) framed by hairlines.
  - A note row („Schema, ne mastelis“ · „LT → PL → DE → BE → FR → IE / ES“).
  - The datasheet: figure in columns 1–4, sheet in columns 6–12.
- **Content:**
  - H2 **NEW**: „Du maršrutai, keturios tranzito šalys“.
  - Intro, adapted from [P: Tarptautiniai]: „Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija – siuntą galite perduoti ir ten gyvenantiems artimiesiems, draugams ar verslo partneriams.“ (the second clause is shortened → **NEW**).
  - Datasheets: see 3.5. Values from [P: grafikas, kontaktai]; the „Vežame“ row **NEW**: „Keleivius, siuntas, automobilius, gyvūnus ir kt.“
- **Media:** Airija #2881400 (Dublin bridge at night), Ispanija #27868340 (Madrid highway at dusk). Alternates: #3220828, #32821932.
- **Effects:**
  - Diagram: scroll-scrubbed draw (S3).
  - Toggle: branch recolour 500ms; datasheet swap 600ms; figure cross-fade 700ms.
  - Figure: Reveal From Left + inner parallax 0.08.
  - Datasheet: fade-up.
  - Tel links: hover underline red.
- **Salient:** Tabs › Toggle Button; Lottie (Scroll Position Seek) ×2 with device visibility; Inner Column *Reveal From Left*; Text `sgp-kv`; Buttons.

**H5 · Paslaugos — sticky stacking spec sheets** (in the tile)
- **Purpose:** covers all 11 services, scannable, with a direct link to each.
- **Layout:**
  - Columns 1–4 sticky: label (§ 03), H2, a count block „11 paslaugų / 6 grupėse“ (**NEW**), the intro and the index 01–06 (the active item gets a red 28px lane).
  - Columns 5–12: 6 stacking cards, sticky top = header + 24px + i×14px.
- **Content** (group names **NEW**; leads verbatim [S]):

| # | Card (light/dark) | Lead (verbatim) | Mini spec (condensed from [S] → NEW wording) | Links | Image |
|---|---|---|---|---|---|
| 01 | Siuntos ir daiktai (light) | „Skubus siuntų pristatymas į namus – paslauga, garantuojanti didžiausią patogumą ir siuntėjui, ir gavėjui.“ | Principas: Nuo durų iki durų · Kelyje: Apie 3–4 paros nuo paėmimo · Pakuotė: Nauja, tvirta, ~5 cm tarpas iki sienelių | Siuntų pervežimas · Siuntų pristatymas · Daiktų pervežimas | #6170458 |
| 02 | Kroviniai (dark) | „Krovinių pervežimas į Airiją, Ispaniją, Vokietiją bei Prancūziją ir atgal – saugiai, greitai, patikimai.“ | Draudimas: Visi kroviniai kelionės metu apdrausti · Iškrovimas: Iškrauname, jei nereikia specialios technikos · Daliniai: Erdvę dalijatės su kitais – mokate mažiau | Krovinių pervežimas · Dalinių krovinių gabenimas · Negabaritinių krovinių pervežimas | #12418936 |
| 03 | Automobiliai ir motociklai (light) | „Automobilių gabenimas – paprastai ir greitai.“ + adapted [S] „Vežame traliuku – patikimomis, techniškai tvarkingomis transporto priemonėmis.“ („naujomis“ dropped) | Transportas: Traliukas (priekaba) · Kelyje: Apie 3–4 paros · Dažniausiai: Automobiliai iš / į Vokietiją | Automobilių pervežimas · Motociklų pervežimas | #29566910 |
| 04 | Keleiviai (dark) | „…keleiviai paimami iš jiems patogios vietos ir pristatomi į jų kelionės tikslą.“ (trimmed) | Salonas: Atlenkiamos, šildomos sėdynės, kondicionierius · Draudimas: Kelionės metu visi keleiviai apdrausti · Vairuotojai: Laikosi darbo ir poilsio režimo | Keleivių pervežimas | #36377055 |
| 05 | Gyvūnai (light) | „Saugiai ir patogiai perkraustysime Jūsų augintinį į kitą šalį Europoje.“ | Narvai: Narvus gyvūnams pervežti turime mes · Dokumentai: Skiepai nuo pasiutligės, veterinaro pažyma · Kaina: Individuali: narvas, priežiūra, atstumas | Gyvūnų pervežimas | #32872983 |
| 06 | Perkraustymas (dark) | „…jei nusprendėte persikelti gyventi į kitą šalį Europoje, mūsų nebrangios perkraustymo paslaugos bus būtent tai, ko Jums reikia.“ | Svarbu: Pakrovimas ir iškrovimas į paslaugą neįeina · Pakavimas: Tvirtos dėžės, trapūs daiktai po vieną · Augintiniai: Vežami atskirai, narvuose | Perkraustymo paslaugos | #7464393 |

- **Effects:**
  - Stacking: the previous card scales 1→0.95 and its dim overlay goes 0→0.28 as the next card arrives.
  - Card images: inner parallax 0.07 and hover zoom.
  - Link rows: hover (3.4).
  - Index: the active item follows the card at the sticky top (red lane width 0→28px, 450ms).
  - H2: Word Reveal.
  - Count: Milestone 0→11.
- **Salient:** Row paper-2 `sgp-grid`. Left column: **Column › Sticky Content (CSS, Top)**. Right: **Sticky Content Sections › Sticky Scroll Pinned Sections › Stacking**, effect off on phone. The index is anchor links, with an optional 10-line JS for the active state (§ 14-E).

**H6 · Nuo durų iki durų — parallax statement band** (in the tile)
- **Purpose:** an emotional beat, and the graceful handling of the delivery-time conflict.
- **Layout:** Row full-bleed, min-height 100svh (700px floor). Label top-left. Statement in columns 1–10, bottom third. A 3-cell strip (columns 1–4 / 5–8 / 9–12) with a top hairline.
- **Content:**
  - Statement, verbatim [S: siuntu-pristatymas]: „Siuntiniai paimami iš siuntėjų ir atiduodami gavėjams **į rankas.**“ („į rankas.“ in red).
  - Cells (**NEW** microcopy, facts from [S]/[P]):
    - „01 — Paėmimas / Sutartu adresu / Paimame iš Jums patogios vietos. Gavėjas turi būti vietoje sutartu laiku – pakartotinis atvykimas apmokestinamas.“
    - „02 — Kelyje / Apie 3–4 paros / Skaičiuojama nuo paėmimo dienos, nepriklausomai nuo maršruto.“
    - „03 — Įsipareigojimas / Iki 5 darbo dienų / Siuntą pristatome per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklės, 3.4 p.).“
- **Media:** #31570314 (securing cargo with chains at night). Alternate: #8858566.
- **Effects:**
  - Background parallax at 0.30 (Medium).
  - Statement: Word Reveal, stagger 70ms, 1100ms easeOutExpo.
  - Strip: fade-up with 0/120/240 delays.
  - The grid lines in white 7.5% cross the photo, with crosses on the top edge.
- **Salient:** Row Full Width BG image, **Parallax Background Media On Scroll: Medium**, Color Overlay Advanced gradient, `sgp-grid sgp-grid--x`; Animated Text (Word: Reveal); Inner Row 3 columns (Fade In From Bottom, delays 0/120/240).

**H7 · Kaip vyksta — sticky media procedure**
- **Purpose:** shows the process step by step and answers "what do I have to do?".
- **Layout:**
  - Section head.
  - Sticky media on the left (columns 1–6, 80vh, corner ticks, mono caption „P-0X / 05“).
  - Steps scrolling on the right (columns 8–12). Each step has a code, an SSXC 44px title and 2–3 lines of body.
  - A thin vertical 3-lane rail beside the steps fills as they pass.
- **Content** (titles and bodies **NEW**, facts from [S]):
  - **P-01 Susisiekite:** „Paskambinkite į Airijos ar Ispanijos liniją arba užpildykite užklausą – suderinsime datą, adresus ir kainą.“ → media #6169133.
  - **P-02 Supakuokite:** „Naujos, standžios dėžės, užpildas tuščioms ertmėms, lipni juosta per visą perimetrą, adresas matomoje vietoje.“ (condensed [S: kroviniu]) → #7464731.
  - **P-03 Paimame:** „Paimame krovinį iš sutartos vietos“ (verbatim [S: gyvunu]) + „nuo durų iki durų.“ → #13456097.
  - **P-04 Kelyje:** „Apie 3–4 paros. Vairuotojai laikosi privalomo darbo ir poilsio režimo.“ ([S]) → `v13707149` SD (0.4 MB, fog, night).
  - **P-05 Pristatome:** „…ir pristatome gavėjui į rankas.“ ([S]) + „Gavėjas turi laukti sutartu laiku – kitu atveju pakartotinis atvykimas apmokestinamas papildomai.“ ([S]) → #4440774.
- **Effects:**
  - Media swap: cross-fade + clip `inset(0 0 100% 0)→0` from the bottom, 900ms easeOutExpo.
  - Steps: fade-up.
  - Rail: fill scaleY driven by progress (custom, progressive enhancement: `animation-timeline: view()`, with static rails as the fallback).
- **Salient:** **Sticky Content Sections › Sticky Media, Scrolling Content** (media width 50%, height 80vh). Phone: stacks, with the media above each step.

**H8 · Prieš siunčiant — rules digest**
- **Purpose:** makes "what's allowed" unmissable and reduces bad parcels and calls.
- **Layout:** `--sheet` row. Section head. Tabs Minimal (3 tabs) in columns 4–12. A penalty callout block in columns 1–3 (sticky).
- **Content:**
  - H2 **NEW**: „Ką galima siųsti, o ko – ne“.
  - Tab „Draudžiama siųsti (12)“: the verbatim list from [P: Taisyklės 4.2] as 12 numbered items:
    1. „bet kokie tabako gaminiai“
    2. „bet kokie alkoholiniai gėrimai“
    3. „pinigai ir vertybiniai popieriai“
    4. „taurieji metalai“
    5. „juvelyriniai gaminiai“
    6. „vaistai ir maisto papildai“
    7. „šaunamieji ir kiti ginklai“ (typo fixed, needs approval)
    8. „meno kūriniai ir antikvariniai daiktai“
    9. „cheminiai kroviniai ir degios prekės“
    10. „greitai gendantys maisto produktai“
    11. „daiktai, kurių pervežimui reikalingos specialios temperatūros, oro, drėgmės ir kitos papildomos sąlygos“
    12. „visos kitos prekės, kurias vežti draudžiama įstatymais…“
  - Tab „Pakavimas (4)“: the 4 packing rules, verbatim [S: kroviniu], plus „rekomenduojamas tarpas yra 5 centimetrai“ [S: siuntu].
  - Tab „Pretenzijos“: [P: 5.1] verbatim.
  - Callout: „1200 EUR“ (SSXC red) + verbatim „Radus siuntoje ar krovinyje alkoholinių gėrimų, taikoma 1200 EUR bauda už kiekvieną alkoholinio gėrimo vienetą“ + a link to the full rules.
  - Buttons: „Visos taisyklės →“, „Atsisiųsti sutartį (PDF, 72 KB)“ (**NEW** label; file [P]).
- **Effects:**
  - Tab change: content fade + 12px slide (Tabs content animation).
  - List items: stagger 60ms.
  - Each prohibited item gets a red „×“ line icon that draws (Vivus-style) on view.
- **Salient:** Tabs **Minimal**; Icon List (numbered, 2 columns via `columns: 2` custom); Column Sticky Content; Buttons.

**H9 · Atsiliepimai placeholder:** see 3.16. Hidden in production until real reviews exist.

**H10 · CTA — Kontaktai** (in the tile): see 3.9. Form = the fields of the old modal: Jūsų vardas · Telefono numeris · El. pašto adresas · Kas Jus domina? (a select of the 11 services) · Žinutė (min. 20) → „Gauti pasiūlymą“. The placeholder „Iš kur, į kur, kada ir ką vežame?“ is **NEW**; the form header „Užklausa“ / „Visi laukai privalomi“ is **NEW**.
- **Effects:** H2 Word Reveal; the groups fade up (0/120ms); phone-line hovers; field focus.
- **Salient:** Global Section, Row `#16181A` `sgp-grid sgp-grid--x`, Fluent Forms (Salient form styling + § 14-G), Column BG `#222528` + `sgp-ticks`.

**H11 · Footer:** see 3.14.

### 5.2 Apie mus `/apie-imone/`

| # | Section | Content (source) | Media | Effects | Salient |
|---|---|---|---|---|---|
| 1 | Page hero (light) | Breadcrumb „Pradžia / Apie įmonę“; H1 „Apie mus“ (menu label [P]); lead = the first „„SGP“ – esame įmonė…“ sentence [P]; spec strip 2 · 4 · 11 · 3–4 | #7541981 (driver at night) | Figure Mask Reveal, straight, left, 1300ms; inner parallax 0.08; counters | Row paper `sgp-grid`, Column Mask Reveal, Milestones |
| 2 | Statement (light) | „Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.“ [P] in SSXC, columns 4–12 | — | Word Reveal once (never scroll-lit) | Animated Text › Word Reveal, stagger 60 |
| 3 | Saugiai / Greitai / Patikimai | 3 columns, each with a lane marker + SSXC title + 2 spec rows. **Saugiai:** „Visi mūsų gabenami kroviniai kelionės metu yra apdrausti.“ / „Kelionės metu visi keleiviai yra apdrausti.“ [S]. **Greitai:** „apie 3–4 paras“ + „Artimiausi pervežimai →“. **Patikimai:** „Vairuotojai visada laikosi privalomo darbo ir poilsio režimo.“ [S] + „nuo durų iki durų“ | — | Animated Column Borders draw in [DOM]; hover: column bg → sheet, lanes extend 22→44px | Row 3 columns, Column Borders + animated, Column bg hover |
| 4 | Parallax quote band | „Mes visada pasiruošę teikti kokybiškas transporto paslaugas už Jums prieinamą kainą!“ [P] | #9989463 (white van, mountain road) | Parallax Medium 0.30; Word Reveal | Row image bg Parallax Medium + gradient |
| 5 | Figures (replaces the old 5-photo iGallery) | Captions **NEW**, neutral: „Pav. 01 — Pakrovimas“, „Pav. 02 — Tvirtinimas“, „Pav. 03 — Dokumentai“, „Pav. 04 — Kelyje naktį“ | #2449454, #31570314, #6169133, #8858566 | Flickity drag with Subtle Item Scale When Dragging; Touch & Total indicator; mask edges | Carousel › Flickity › *Fixed Text Content Fullwidth* (text: „Kaip dirbame“ **NEW**) |
| 6 | Paslaugos link tiles | „Pervežimo paslaugos“ (H2 [P]) + tiles → Tarptautiniai pervežimai, Pervežimo paslaugos, Pervežimų grafikas | — | Fancy Box *Bottom Color Bar Hover Effect* (red bar) | Fancy Box ×3 |
| 7 | CTA + Footer | Global | | | |

Note: replace the stock photos with SGP's own as soon as they are available (§ 1.7).

### 5.3 Pervežimo paslaugos `/pervezimo-paslaugos/`

| # | Section | Content | Media | Effects | Salient |
|---|---|---|---|---|---|
| 1 | Page hero (light) | H1 „Pervežimo paslaugos“; lead „Mūsų paslaugų sąraše: automobilių, gyvūnų, daiktų ir krovinių gabenimas bei keleivių pervežimo paslaugos.“ [P]; spec strip: 11 paslaugų · 2 kryptys · 3–4 paros · „Nuo durų iki durų“ | #36383706 (highway at dusk, snow) | Mask Reveal left; counters | Row + Column Mask Reveal |
| 2 | Services index (grid of 11 spec cards) | Per card: index 01–11, name, a one-line verbatim santrauka (trimmed at a sentence end), country chips (IE ES DE FR…), arrow. Group filter chips: Visos · Siuntos ir daiktai · Kroviniai · Automobiliai ir motociklai · Keleiviai · Gyvūnai · Perkraustymas (**NEW** group names) | Featured images per slug (§ 5.5 table) | Entrance: *Zoom out reveal*, stagger 90ms. Hover: image Slow BG Zoom, corner ticks tighten, arrow swap, title underline (Animated Underline) | **Post Loop Builder** (CPT „Paslaugos“) › Grid 3/2/1 columns, item style *Content Under Featured Image*, filters ON, hover *Slow BG Zoom* + Animated Underline |
| 3 | Text (SEO body) | Verbatim [P] paragraphs 1–3 (drop „naujais“ if not confirmed, § 11) + H4 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ + paragraph | — | Fade-up | Row 2 columns: label column Sticky Content, Text block columns 4–10 |
| 4 | Maršruto schema (mini) | Global Section | — | S3 | Lottie |
| 5 | Siuntos sekimas strip | Global | | | |
| 6 | CTA + Footer | | | | |

### 5.4 Tarptautiniai pervežimai `/pervezimo-paslaugos/tarptautiniai-pervezimai/`

| # | Section | Content | Media | Effects | Salient |
|---|---|---|---|---|---|
| 1 | Page hero (**dark video**) | Breadcrumb; H1 „Tarptautiniai pervežimai“; lead „SGP pervežimai – komanda savo srities profesionalų, turinčių vieningą tikslą – užtikrinti, kad siuntiniai ir keleiviai į Ispaniją ir Airiją keliautų saugiai, greitai, patikimai ir komfortiškai.“ [P]; 2 phone lines | `v4685871` (forest highway at dusk; HD 3.8 MB / SD 0.6 MB; phone poster) | Parallax Subtle 0.22; grid draw; H1 Word Reveal | Row video bg + Parallax Subtle + gradient + `sgp-grid--draw` |
| 2 | Route schematic, full | Both route datasheets **side by side** (no toggle): „Lietuva ⇄ Airija“ / „Lietuva ⇄ Ispanija“ with phones, dates, transit, duration | #3220828 (Irish coastal road), #32821932 (coastal road, truck) | S3 scrub; datasheets fade-up 0/120 | Lottie + 2 columns `sgp-kv` |
| 3 | Coverage map | 7 markers: LT, PL, DE, BE, FR, IE, ES (country centroids, no cities); legend „Schema“ | — | Nectar Animated (pulsing) markers in red; greyscale | **Interactive Map** (Leaflet), Greyscale, Ultra Flat, no scroll-zoom, custom marker colour `#EF4539` |
| 4 | Kodėl verta pasitikėti mumis? | H4 verbatim + the 9 bullets [P] as indexed spec rows 01–09 (the key phrase bolded; drop the „DVD“ clause, § 11) | — | Rows: Border Animation (the rule draws in), 60ms stagger | Horizontal List Item › *Border Animation* |
| 5 | Visos paslaugos | The same 11-card grid (Global Post Loop) | per slug | as 5.3 | Post Loop Builder |
| 6 | Ko negalima siųsti? | H4 verbatim „Krovinių pervežimas tarptautiniais maršrutais: ko negalima siųsti?“ + the 8 items [P] + the responsibility paragraphs + „Už valstybinių institucijų konfiskuotas siuntas mes atsakomybės neprisiimame.“ | — | List stagger; red × icons draw | Icon List (numbered) |
| 7 | Ką dar turite žinoti? | H4 verbatim + 4 accordion items (**NEW** item titles: „Trukmė“, „Pakavimas“, „Adresai“, „Iškrovimas“), bodies verbatim [P] | — | Accordion open 450ms easeInOutCubic | **Toggle Panels › Minimal**, accordion ON |
| 8 | Grafikas (full, next 4) | Global | | S4 | Global Section |
| 9 | CTA + Footer | | | | |

### 5.5 Service detail template `/pervezimo-paslaugos/tarptautiniai-pervezimai/<slug>/` (×11)

**Template sections**

| # | Section | Content | Effects | Salient |
|---|---|---|---|---|
| 1 | Page hero (light) | Breadcrumb „Pradžia / Pervežimo paslaugos / Tarptautiniai pervežimai / {H1}“; **H1 = {title}** (fixes the site-wide „Pervežimas“ H1 bug); lead = {santrauka, verbatim}; CTAs: phone line IE + phone line ES + „Gauti pasiūlymą“; figure {hero} columns 8–12; spec strip: **Kryptys** {chips} · **Kelyje** {trukmė} · **Principas** „Nuo durų iki durų“ · **Svarbu** {svarbu} | Figure Mask Reveal (straight, left) 1300ms + inner parallax 0.08; H1 Word Reveal; strip fade-up 0/120/240/360 | Row paper `sgp-grid`; Column Mask Reveal; Animated Text; Buttons |
| 2 | Sticky submenu | 3.13 | Sticky | Page Submenu (Sticky) |
| 3 | Apie paslaugą | Verbatim intro paragraphs [S] (columns 4–10), sticky label (columns 1–3). The closing sentence „… su „SGP pervežimai“ – …“ (present on every page [S]) becomes a pull-quote in SSXC 40px with a red lane glyph | Pull-quote Word Reveal | Column Sticky Content; Text; Animated Text |
| 4 | Privalumai | H4 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ (verbatim [S]) → 3–5 spec rows (`sgp-kv`) from the „Savybės / sąlygos“ block; below, a toggle „Skaityti visą tekstą“ (**NEW**) holding the full verbatim paragraphs | Rows fade-up 60ms | Text `sgp-kv`; Toggle Panels › Minimal |
| 5 | Media band | {band media} full-bleed with the {band statement, verbatim} in SSXC | Parallax Medium 0.30 (photo) or video bg (SD, lazy, autoplay in view); Word Reveal | Row image/video bg, Parallax Medium, gradient, `sgp-grid--x` |
| 6 | Kliento atsakomybės | H4 „Kliento atsakomybės: ką reikia žinoti?“ (verbatim [S], where present) → a numbered checklist (packing, exact addresses, recipient on time → repeat visit charged, prohibited items summary) + a link „Visos taisyklės →“. **Keleivių** page: replaced by the „Keleiviams“ comfort spec (seats, heating, A/C, insurance, rest regime) | List stagger 60ms; the prohibited list uses red × icons | Icon List (numbered) + Button Underline |
| 7 | Kryptys | Country chips + the legacy child pages as rows, e.g. „Krovinių pervežimas į Airiją →“ (anchors; see § 12 for 301s) | Row hover: graphite fill rises, text inverts | Horizontal List Item › *Bottom Border, Color Hover Effect* |
| 8 | Susijusios paslaugos | 3 cards, same group first | as 5.3 | Post Loop Builder (3 items, related by taxonomy) |
| 9 | Grafikas (next 4) + CTA + Footer | Global | | |

**Per-slug variables** (lead = verbatim santrauka [S]; band statement verbatim [S]; spec values condensed from [S], marked NEW in § 13)

| Slug | H1 | Hero img | Band media | Band statement (verbatim) | Kryptys chips | Kelyje | Svarbu (spec strip) | Legacy child rows |
|---|---|---|---|---|---|---|---|---|
| kroviniu-pervezimas | Krovinių pervežimas | #38927007 | #1225126 (light trails, DE) | „Visi mūsų gabenami kroviniai kelionės metu yra apdrausti.“ | IE · ES · DE · FR | Apie 3–4 paros | Iškrauname, jei nereikia specialios technikos | į / iš Airijos, į / iš Ispanijos, į / iš Vokietijos (6) |
| negabaritiniu-kroviniu-pervezimas | Negabaritinių krovinių pervežimas | #35332902 | `v19552565` SD 2.6 MB | „Negabaritiniai kroviniai yra tokie kroviniai, kurių matmenys yra didesni negu didžiausi leidžiami tose šalyse, per kurias tie kroviniai keliauja.“ | LT · FR · ES · IE | Apie 3–4 paros* | Reikia leidimų ir išankstinio planavimo; iškrovimo techniką užtikrina klientas | Pavojingų krovinių pervežimas; Didelių krovinių pervežimas |
| daliniu-kroviniu-gabenimas | Dalinių krovinių gabenimas | #34585120 | #29786116 | „Dalinių krovinių gabenimas yra puikus būdas klientams sutaupyti.“ | DE · FR · ES · IE | Apie 3–4 paros* | Tiksliai nurodykite siuntėjo ir gavėjo adresus | Smulkių krovinių pervežimas |
| daiktu-pervezimas | Daiktų pervežimas | #36933446 | #160483 | „Daiktų pervežimas į užsienį kelių transportu trunka apie 3–4 paras (skaičiuojama nuo siuntos paėmimo dienos).“ | DE · FR · ES · IE | Apie 3–4 paros | Pakavimas – kliento atsakomybė | Daiktų pervežimas į Airiją |
| automobiliu-pervezimas | Automobilių pervežimas | #29566910 | `v34371915` SD 1.4 MB (B/W) | „Automobilių pervežimas Europoje traliuku trunka apie 3–4 paras.“ | DE · LT · IE · ES | Apie 3–4 paros | Vežame traliuku; nesant gavėjo – pakartotinis atvažiavimas apmokestinamas | iš Airijos; iš Ispanijos; iš Vokietijos |
| motociklu-pervezimas | Motociklų pervežimas | #4858429 | `v34308329` SD 1.3 MB | „Nuo durų iki durų – tai principas, kuriuo vadovaujantis vykdomas motociklų gabenimas Europoje.“ | ES · FR · DE · PL · IE | 3–4 paros | Važiuojame tik geriausiais keliais | — |
| keleiviu-pervezimas | Keleivių pervežimas | #36377055 | #27383867 | „Kelionės metu visi keleiviai yra apdrausti.“ | ES · DE · FR · IE | 3–4 paros | Atlenkiamos, šildomos sėdynės, kondicionierius | vežimas į Airiją; į Ispaniją; į Vokietiją; į Prancūziją |
| gyvunu-pervezimas | Gyvūnų pervežimas | #32872983 | #21767483 | „Narvus gyvūnams pervežti turime mes.“ | ES · FR · DE · IE | Apie 3–4 paros* | Skiepai nuo pasiutligės (~mėn. iki kelionės), veterinaro dokumentas, vaistai nuo helmintų | į Airiją; į Ispaniją; į Vokietiją; į Prancūziją; Šunų pervežimas |
| siuntu-pervezimas | Siuntų pervežimas | #6170458 | #4487517 | „Skubios siuntos pasieks gavėją labai operatyviai.“ | DE · ES · IE · FR | Apie 3–4 paros* | ~5 cm tarpas iki pakuotės sienelių | Siuntos į Airiją; į Ispaniją; į Vokietiją |
| siuntu-pristatymas | Siuntų pristatymas | #13456097 | #4440774 | „Siuntiniai paimami iš siuntėjų ir atiduodami gavėjams į rankas.“ | DE · FR · ES · IE | Apie 3–4 paros | Klientas atsako už turinį ir pakavimą | Nuo durų iki durų |
| perkraustymo-paslaugos | Perkraustymo paslaugos | #7464393 | #4246238 | „Nuo durų iki durų – tai principas, kuriuo remiantis teikiamos perkraustymo paslaugos į užsienį.“ | DE · ES · FR · IE | Apie 3–4 paros | Pakrovimas ir iškrovimas į paslaugą neįeina | Perkraustymo paslaugos kaina |

\* This service page has no duration of its own. It uses the general statement from [P: Tarptautiniai]: „…pristatymas truks apie 3–4 paras nuo paėmimo datos.“ The client must confirm it (§ 11).

The **Keleivių** page adds a „Penki principai“ row block: Saugumas · Operatyvumas · Profesionalumas · Komfortas · Patogumas (verbatim bold leads [S]). It is rendered as 5 indexed spec columns, and the „(2017–2018 metų)“ and „DVD“ fragments are dropped (§ 11).

### 5.6 Pervežimų grafikas `/pervezimu-grafikas/` (now in the main nav)

| # | Section | Content | Effects | Salient |
|---|---|---|---|---|
| 1 | Page hero (graphite, grid, ruler) | H1 „Pervežimų grafikas“; lead **NEW** „Artimiausi išvykimai iš Lietuvos ir grįžimai į Lietuvą. Vietą rezervuokite telefonu.“; 2 phone lines. Background texture #9807331 (wet road, B/W) at 18% | Grid draw; Word Reveal | Row graphite + image bg 18% + `sgp-grid--draw` |
| 2 | Departure board (light) | Filter toggle „Visi · Airija · Ispanija“ (**NEW**). Chronological rows (from [P]): Rugs. 27 ES → LT · Rugs. 28 IE → LT · Spal. 09 LT → IE · Spal. 09 LT → ES · Spal. 14 ES → LT · Spal. 15 IE → LT · Spal. 23 LT → IE · Spal. 23 LT → ES · Spal. 28 IE → LT · Spal. 28 ES → LT. Columns: date chip · code · „Lietuva – Airija“ · tranzitas „PL · DE · BE · FR“ · linija (tel) · → | Rows fade-up, 40ms stagger; hover S4 light | Global Section „Grafikas — pilnas“: Horizontal List Items, or a Post Loop from an ACF/CPT „Išvykimai“ |
| 3 | Notes (spec) | „Kelyje: apie 3–4 paros nuo paėmimo“ · „Išvykimo laiką ir vietą suderiname telefonu“ (**NEW**) · „Siuntų įsipareigojimas: per 5 darbo dienas nuo išvykimo iš Lietuvos (Taisyklės, 3.4 p.)“ | Fade-up | Text `sgp-kv` |
| 4 | Maršruto schema (mini) | Global | S3 | Lottie |
| 5 | CTA + Footer | | | |

### 5.7 Siuntos sekimas `/siuntos-sekimas/`

| # | Section | Content | Effects | Salient |
|---|---|---|---|---|
| 1 | Page hero (light, compact) | H1 „Siuntos sekimas“ (verbatim); a large tracking console (3.11) prefilled from `?kodas=` | Field focus red bar | Raw HTML form |
| 2 | Result sheet | A framed sheet (corner ticks, mono header „Rezultatas“) holding the `<iframe src="https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=…" height="500">`. The iframe's own messages („Neįvestas siuntos kodas!“, „Toks siuntos kodas neegzistuoja!“) cannot be styled from the site; ask the GP Soft system for a `#1C1D1D`/`#EF4539` theme | — | Raw HTML (iframe), `sgp-ticks` |
| 3 | Help strip | **NEW** „Kodo neturite ar kyla klausimų? Paskambinkite:“ + 2 phone lines | Hover lines | Buttons `sgp-line` |
| 4 | Grafikas (next 4) + Footer | | | |

Also fix the meta description, which is currently „<b>test</b>“. Redirect `/pervezimo-paslaugos/siuntos-sekimas` here with a 301.

### 5.8 Taisyklės `/taisykles/`

| # | Section | Content | Effects | Salient |
|---|---|---|---|---|
| 1 | Page hero (light) | Breadcrumb „Pradžia / Taisyklės“; H1 „Siuntų siuntimo taisyklės“ (the old banner title [P]); lead: „Paslaugos Mokėtojai (užsakovai) privalo susipažinti su šiomis taisyklėmis ir vadovautis jomis ruošiant siuntas ir užsakant paslaugas.“ (from the old meta description [P], so it needs approval); primary button „Atsisiųsti sutartį (PDF, 72 KB)“ → `sgp_sutartis-su-siunteju.pdf` | Word Reveal | Row + Button (download attr) |
| 2 | Rules document | Left: sticky TOC of the 6 section titles (verbatim: „1. Siuntų tikrinimas“ … „6. Atvejai, kuriais įmonė neprisiima atsakomybės“), with the active item marked by a red lane. Right: clauses per 3.18, all text verbatim [P] (typos fixed only with approval, § 11) | Active TOC follows scroll; clauses fade-up | **Tabs › Vertical Sticky Scrolling** (native sticky TOC) |
| 3 | 4.2 list + 4.5 fines table | 12 numbered items. Fines table (values verbatim [P 4.5]): Alkoholis — 1200 EUR / vnt. · Vaistai — 1200 EUR / vnt. (ampulė, tabletė) · Cigaretės — 1200 EUR / blokas (200 vnt.), ta pati bauda ir už mažesnį kiekį · Tabakas — 1200 EUR / 200 g · Kiti draudžiami daiktai (4.2 p.) — 1200 EUR | Rows stagger | Icon List + Text table `sgp-kv` |
| 4 | Grafikas (the old page shows it under the rules) + CTA + Footer | Global | | |

### 5.9 Kontaktai `/kontaktai/`

| # | Section | Content | Effects | Salient |
|---|---|---|---|---|
| 1 | Page hero (light) | H1 „Kontaktai“; H2-sized lead „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“ [P] | Word Reveal | Animated Text |
| 2 | Linijos + forma | Left: „Pervežimai į Airiją“ (3 lines: Lietuva, Airija, Jungtinė Karalystė) and „Pervežimai į Ispaniją“ (2 lines), plus the email „saugiai.greitai.patikimai@gmail.com“. Right: the contact form, verbatim [P]: Jūsų vardas · El. pašto adresas · Žinutės tema · Žinutė (min. 20) → „Siųsti“ + the privacy line | Groups fade-up; line hovers | Buttons `sgp-line`; Fluent Form #2 |
| 3 | Maršruto schema (mini) instead of a map | The site has **no address**, so there is no map. The honest visual is the route network | S3 | Lottie |
| 4 | Footer (no CTA band on this page) | | | |

The page hero image is optional: #1696742 (road through a pine forest). **Do not** use the Vilnius photos, because the site never states a city.

### 5.10 Privatumo politika `/privatumo-politika/`

| # | Section | Content | Salient |
|---|---|---|---|
| 1 | Page hero (light, compact) | H1 „Privatumo politika“ | Row |
| 2 | Informacija | „Informacija ruošiama...“ [P]. **Client must supply the actual policy (GDPR)**; the design reserves a 68ch document column with mono clause numbers | Text |
| 3 | Slapukai (Cookies) | H3 + H5 verbatim; the 5-row cookie table as a spec table (mono keys, hairlines; it scrolls horizontally inside its own box on phone); the link „Norėdami pasitikrinti, … – spauskite čia.“ [P] | Text `sgp-table` |
| 4 | Footer (no CTA band) | | |

Redirect the old `/privatumo-politika/policies` URL with a 301.

### 5.11 404

- **Layout:** full-height graphite row with the grid and ruler.
  - An SSXC „404“ at 22vw in `--graphite-3` (a solid tone, not outlined).
  - Over it, a fragment of the route schematic: the triple lane runs from the left and ends in a dashed `--mist` segment with a red concentric-square marker labelled mono „Maršrutas nerastas“ (**NEW**).
- **Copy (NEW):** H1 „Tokio puslapio nėra“ · lead „Grįžkite į pradžią arba paskambinkite – padėsime.“
- **Buttons:** primary „Į pradžią“, ghost „Pervežimų grafikas“, plus 2 phone lines. The tracking strip sits below.
- **Media:** texture #4040619 (asphalt macro) at 12% under the grid.
- **Effects:** grid draw; the lane draws and stops (1300ms); Word Reveal.
- **Salient:** a Salient 404 template through a Global Section, Row `sgp-grid--draw`.

---

## 6. Salient Theme Options checklist

- **General / skin:** Material skin. Button Styling: *Default* (square), plus radius 2px via `.sgp-btn`.
- **Colours:** see § 1.1.
- **Typography:** see § 1.2 (Local Google Fonts ON, Fluid Typography ON).
- **Header:**
  - Layout Centered Menu, height 76.
  - Transparent Header ON; starting logo `logo_light.svg`; dark logo `logo.svg` (height 54).
  - Header Inherit Row Color ON; background blur ON (BG `rgba(237,239,241,.86)`).
  - Hide Until Needed ON; Resize On Scroll OFF.
  - Header Link Hover/Active Effect: **Text Reveal**; Entrance: Fade In.
  - Secondary Header Bar ON on desktop, hidden on mobile.
- **Off Canvas:** Slide Out From Side; custom colours; Global Section content (phone dock).
- **Animation:**
  - Column/Image Animation Easing **easeOutExpo**, Timing **1200**.
  - Page Builder Element Animations On Mobile Devices **ON** (entrances are short, masks are cheap).
  - Parallax on mobile **OFF**; video backgrounds on mobile **OFF** (poster).
- **Smooth Scrolling:** ON (Lenis), strength 60, with the reduced-motion guard in § 8.
- **Page transitions:** View Transitions API › **Fade** (restrained). Keep it OFF on mobile if there are performance issues.
- **Lightbox:** fancyBox3.
- **Footer:** Global Section; Footer Reveal OFF.
- **Back to top:** OFF (the footer link and the call bar cover it).
- **Forms:** Fluent Forms + § 14-G.
- **Performance:** Delay JavaScript Execution ON (exclude the Lenis init and the `sgp-*` scripts that affect first paint); lazy load images ON.
- **Anchor scroll:** One Page Scroll Support ON (offset 80).

---

## 7. Responsive behaviour

**≤ 1200px**
- The hero board drops under the CTAs (columns 1–7, max 560px).
- H1 sizing is container-based, so it never overflows.

**≤ 1000px (Salient tablet + phone)**
- **Header:** 64px; the utility bar and desktop nav are hidden; icon buttons for call and menu; off-canvas panel.
- **Mobile call bar:** appears after 55% of the first viewport has been scrolled.
- **Grid:** 8 columns, 16px gutter; the ruler shows 01–08.
- **Hero:** stacks as eyebrow row → H1 → lead → phone lines (side by side) → board (full width) → data strip (2 × 2).
- **Section heads:** stack (label → H2 → intro).
- **Routes:** the toggle is full width and the legend wraps left. The desktop diagram still fits; figure and sheet split 3/5 columns.
- **Services:** the left column is no longer sticky and the index list is hidden. Cards still stack down to 760px.
- **Process:** Sticky Media stacks (Salient default).
- **Contact:** single column (lines, then form).
- **Footer:** 2 columns.

**≤ 760px**
- **Service cards:** stacking is off and cards flow normally. Each card is image (16:10) → text → links; scale and dim are disabled.

**≤ 600px (fine-tune inside Salient's ≤ 690 phone band)**
- **H1:** switches to the 3-row "tree" composition: „Lietuva“ over a vertical lane that branches to „Airija“ and „Ispanija“. Size `min(20cqi, 4.8rem)`, about 72px at 390px.
- **Phone lines:** full width and stacked. The text link „Gauti pasiūlymą“ is centred under them.
- **Board:** 52px code column; chips 36px.
- **Diagram:** the vertical phone SVG/Lottie (LT at the top, the trunk down through PL/DE/BE/FR, branches to IE and ES at the bottom).
- **Datasheet:** key over value (1 column). Tel links don't break inside a number.
- **Forms:** single column; the tracking form stacks (field above button).
- **Grid:** 4 columns, 12px gutter.
- **Tap targets:** ≥ 48px (buttons 54, lines 62, call bar 50).
- **Hover-only information is never used:** every hover effect is decorative.

---

## 8. prefers-reduced-motion

When `prefers-reduced-motion: reduce` is set:
- No Lenis: guard the init, or set `nectarOptions.smooth_scroll='false'` early in the head. **Verify on staging**; if it is not honoured, turn Smooth Scrolling OFF globally.
- No parallax (all `transform` reset).
- No video autoplay: poster only. The pause control is hidden because nothing plays.
- All entrances appear instantly: masks, word reveals, fade-ups, counters (final values shown) and grid/lane/route draws (fully drawn).
- Stacking cards keep sticky positioning but lose scale and dim.
- Hover transitions shrink to 1ms, so states still change and remain visible.
- Page transitions: none.

The tile implements all of this (CSS `@media (prefers-reduced-motion: reduce)` plus a JS `RM` flag). For Salient, add the CSS block in § 14-H, plus `data-m-animate`-style overrides.

---

## 9. Performance budget

| Item | Budget | Notes |
|---|---|---|
| LCP (home, 4G mobile) | < 2.5 s | The LCP element is the hero poster (w=1280 on ≤ 1440, w=1920 above, WebP ≤ 220 KB). Preload it. Fonts preloaded: SSXC 800 + Sofia Sans 400 (latin + latin-ext woff2). |
| CLS / INP | < 0.05 / < 200 ms | Aspect-ratio boxes on every media item; the board has a fixed row height; fonts use `display: swap` with metric-compatible fallbacks (`Arial Narrow` for SSXC). |
| Hero video | Desktop ≤ 3 MB target (the source HD is 4.9 MB at 1280×720), tablet SD 2.6 MB, phone 0 | Load only after `load` and only when the viewport is ≥ 601px. Re-encode: `ffmpeg -i in.mp4 -an -vf scale=1280:-2 -c:v libx264 -crf 28 -preset slow -movflags +faststart hero.mp4` plus a WebM VP9 CRF 38. Loop ≤ 12 s. |
| Other video | ≤ 1 per page after the hero; SD versions only (0.4–2.6 MB); lazy; autoplay in view, pause out of view | Process step P-04 `v13707149` SD 0.4 MB; service bands use SD. |
| Images | Home ≤ 2.8 MB desktop / ≤ 1.4 MB phone (after WebP) | Full-bleed w=1920 (band) / 1280; cards and figures w=900; `loading="lazy"` below the fold; `decoding="async"`; responsive `srcset` 480/800/1200/1920. |
| Fonts | ≤ 230 KB woff2 total | SSXC 700/800, Sofia Sans 400/500/600, JetBrains Mono 500 (400 only if needed); latin + latin-ext subsets only; self-hosted via Local Google Fonts. |
| JS (custom) | ≤ 8 KB gzip | Grid draw, route scrub (if not Lottie), video toggle, stack index. No GSAP. Lottie route files ≤ 60 KB each. |
| Total transfer (home) | Before video ≤ 1.6 MB; after idle ≤ 6 MB desktop, ≤ 2 MB phone | |

---

## 10. Accessibility

- **One real H1 per page:** the page title, removing the logo `<h1>Pervežimas</h1>`. The hero's visual H1 is `aria-hidden`, with the full H1 text in an sr-only span.
- **Contrast:** all pairs are in § 1.1. Red on light is used only for large text and graphics; small red text on light uses `--red-ink`.
- **Keyboard:** visible focus ring everywhere. Tabs have roving arrow keys (Salient Tabs + the tile). The off-canvas traps focus with Esc to close. The skip link reads „Pereiti prie turinio“ (**NEW**).
- **Motion:** § 8, plus a pause control for the looping hero video (WCAG 2.2.2).
- **Forms:** visible labels; required state announced; errors in text, not colour only; the success message uses `role="status"`.
- **Route information** is never colour-only: codes (LT → IE) and names always accompany the red/grey branch states.
- **Language:** `lang="lt"`. Tel links are in international format.
- **Iframe (tracking):** `title="Siuntos sekimas"`.

---

## 11. Content conflicts & data rules (how the design handles them)

1. **Delivery time:**
   - Where it appears: „apie 3–4 paras“ ([P] Paslaugos, Tarptautiniai; most [S]) against „per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos“ ([P] Taisyklės 3.4). The old meta also says „nuo 2 iki 3 parų“.
   - B treats these as two different quantities:
     - **„Kelyje: apie 3–4 paros nuo paėmimo“** is the typical duration, used on service pages and the hero strip;
     - **„Įsipareigojimas: iki 5 darbo dienų nuo išvykimo iš Lietuvos (Taisyklės, 3.4 p.)“** is the contractual maximum, used only in the home band, on Grafikas and on Taisyklės.
   - „2–3 paros“ is never shown.
   - The client confirms both labels.
2. **Schedule dates have no year:**
   - The CMS stores full ISO dates. The front end shows the day plus the Lithuanian month abbreviation („09 spal.“).
   - The range label („Rugsėjis – spalis“) is computed.
   - Past rows auto-hide.
   - If no future dates exist, the board shows **NEW** „Artimiausias datas sužinokite telefonu“ plus the 2 lines, and never stale dates.
   - The „2 išvykimai per mėnesį“ stat must be recomputed or removed when the rhythm changes.
3. **„nauji (2017–2018 metų) mikroautobusai“:**
   - The years are never repeated.
   - Copy uses „techniškai tvarkingi mikroautobusai“, which also appears verbatim in [S].
   - „Nauji / naujausi“ is kept only if the client confirms it is still true.
   - The **„DVD“** comfort item is dropped as outdated.
4. **Phone formats:**
   - Display is normalised: +353 86 450 3104, +44 7566 878681, +34 602 547 929.
   - `tel:` values are unchanged.
   - The UK number is shown under „Pervežimai į Airiją“ as in [P]. Whether the Ireland line physically routes via the UK or by ferry is **not stated**, so the schematic shows only the countries named in [P] and carries „Schema, ne mastelis“. A ferry/UK segment is added only after client confirmation (and `v19274366` / #15885602 become usable then).
5. **Country lists differ:** some pages name DE/FR as destinations, while [P: Tarptautiniai] names PL/DE/BE/FR as transit. B shows PL, DE, BE and FR as transit on the schematic and lists DE and FR as „Taip pat“ destinations in the about datasheet. Per-service chips follow each service's own text.
6. **Illogical or incorrect claims to confirm:**
   - „Negabaritiniai… tik naujais mikroautobusais“: confirm the vehicle type.
   - „šias tris šalis“ (4 are listed) → „šias šalis“.
   - The domain in rules 6.2 „http://sgppervezimai.lt“ → sgp-pervezimai.lt.
7. **Typos in the source** (listed in [P]/[S] notes: „šaunamiejii“, „cigarecių“, „baikotai“, „daržo režimo“, …) are corrected in v2 only with client approval, because legal texts may need to stay verbatim.

---

## 12. SEO continuity (design-relevant)

- **URLs:** kept as `folder/index.html` → WP permalinks, identical to the live paths.
- **301 redirects:**
  - `/pervezimo-paslaugos/siuntos-sekimas` → `/siuntos-sekimas/`;
  - `/privatumo-politika/policies` → `/privatumo-politika/`;
  - the 27 legacy child pages (e.g. `/…/kroviniu-pervezimas/kroviniu-pervezimas-i-airija`) → the parent service `#kryptys` (their titles become the „Kryptys“ rows, so the keywords stay on the page), **or** keep them if the client wants route landing pages. That is a decision for phase 2.
- **Titles and meta:** H1 = the page title; fix the broken canonicals (double domain); write new meta descriptions with diacritics (**NEW**, the client approves each).
- **Schema:** Organization + ContactPoint (5 phones, `areaServed` LT/IE/GB/ES) + Service per slug. There is no LocalBusiness address, because none exists.

---

## 13. Naujas tekstas — reikia kliento patvirtinimo

All strings below are new or edited microcopy. Verbatim content from the turinys files is not listed.

**Navigacija / bendri**
- Meniu punktai: „Kryptys“, „Grafikas“ (naujas punktas meniu), meniu indeksai „01–06“
- Viršutinė juosta: „SGP — saugiai · greitai · patikimai“ (šūkis su taškais), „Siuntos sekimas →“
- Telefono linijų pavadinimai: „Airijos linija“, „Ispanijos linija“; kontaktuose – „Lietuva“, „Airija“, „Jungtinė Karalystė“, „Ispanija“
- Mobilioji juosta: „Airija“, „Ispanija“, „Užklausa“; ikonos etiketė „Skambinti“
- „Pereiti prie turinio“ (skip link); „Sustabdyti vaizdą“ / „Paleisti vaizdą“
- Poraštė: stulpelio pavadinimas „Informacija“, „Į viršų ↑“
- Slapukų juosta: papildomas mygtukas „Atmesti“

**Pradžia**
- H1 kompozicija: „Lietuva — Airija / Ispanija“ (su linijų jungtimi); pilnas H1 tekstas: „Keleivių, siuntų ir automobilių pervežimas: Lietuva – Airija ir Lietuva – Ispanija“
- Hero įžanga: „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais – nuo durų iki durų, apie 3–4 paras kelyje.“
- Grafiko lentelė: „Iš Lietuvos“, „Į Lietuvą“, „Rugsėjis – spalis“, „Vietą rezervuokite telefonu“, „Visas grafikas“
- Skaičių juosta: „Kryptys / Tranzitas / Paslaugos / Kelyje“, „Airija ir Ispanija, abiem kryptimis“, „Nuo siuntų iki perkraustymo“, „paros nuo paėmimo dienos“
- Apie: H2 „Saugiai. Greitai. Patikimai.“; duomenų lapo raktai „Veikla, Kryptys, Taip pat, Principas, Draudimas, Vairuotojai“; paveikslėlio parašas „Pav. — Kontrolinis sąrašas“
- Kryptys: H2 „Du maršrutai, keturios tranzito šalys“; sutrumpinta įžangos pabaiga „– siuntą galite perduoti ir ten gyvenantiems artimiesiems, draugams ar verslo partneriams.“; „Schema, ne mastelis“; „Maršrutas 01 / 02“; raktai „Tranzitas, Išvykimai iš Lietuvos, Išvykimai iš Airijos / Ispanijos, Kelionės trukmė, Vežame, Linija“; „Keleivius, siuntas, automobilius, gyvūnus ir kt.“; mygtukas „Skambinti +370 …“
- Paslaugos: „11 paslaugų / 6 grupėse“; grupės „Siuntos ir daiktai“, „Kroviniai“, „Automobiliai ir motociklai“ (kortelės viršuje „Transporto priemonės“), „Keleiviai“, „Gyvūnai“, „Perkraustymas“; kortelių eilutės: „Nuo durų iki durų“, „Apie 3–4 paros nuo paėmimo“, „Nauja, tvirta, ~5 cm tarpas iki sienelių“, „Visi kroviniai kelionės metu apdrausti“, „Iškrauname, jei nereikia specialios technikos“, „Erdvę dalijatės su kitais – mokate mažiau“, „Vežame traliuku – patikimomis, techniškai tvarkingomis transporto priemonėmis.“, „Traliukas (priekaba)“, „Automobiliai iš / į Vokietiją“, „Atlenkiamos, šildomos sėdynės, kondicionierius“, „Kelionės metu visi keleiviai apdrausti“, „Laikosi darbo ir poilsio režimo“, „Skiepai nuo pasiutligės, veterinaro pažyma“, „Individuali: narvas, priežiūra, atstumas“, „Pakrovimas ir iškrovimas į paslaugą neįeina“, „Tvirtos dėžės, trapūs daiktai po vieną“, „Vežami atskirai, narvuose“; paveikslėlių parašai „Pav. 02–07“
- Juosta: „Paėmimas — Sutartu adresu — Paimame iš Jums patogios vietos. Gavėjas turi būti vietoje sutartu laiku – pakartotinis atvykimas apmokestinamas.“; „Kelyje — Apie 3–4 paros — Skaičiuojama nuo paėmimo dienos, nepriklausomai nuo maršruto.“; „Įsipareigojimas — Iki 5 darbo dienų — Siuntą pristatome per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklės, 3.4 p.).“
- Kaip vyksta: žingsniai „P-01 Susisiekite“ … „P-05 Pristatome“ ir jų tekstai (§ 5.1 H7)
- Taisyklių santrauka: H2 „Ką galima siųsti, o ko – ne“; skirtukai „Draudžiama siųsti (12)“, „Pakavimas (4)“, „Pretenzijos“; „Visos taisyklės“, „Atsisiųsti sutartį (PDF, 72 KB)“
- Atsiliepimai: „Čia bus tikri klientų atsiliepimai“ (privaloma formuluotė)
- Forma: „Užklausa“, „Visi laukai privalomi“, „Pasirinkite paslaugą“, „Iš kur, į kur, kada ir ką vežame?“, demo pastaba „(demo — forma nesiunčiama)“

**Vidiniai puslapiai**
- Apie: „Kaip dirbame“, parašai „Pav. 01 — Pakrovimas“, „Pav. 02 — Tvirtinimas“, „Pav. 03 — Dokumentai“, „Pav. 04 — Kelyje naktį“
- Paslaugų apžvalga: filtrų pavadinimai „Visos“ + 6 grupės
- Tarptautiniai: akordeono pavadinimai „Trukmė“, „Pakavimas“, „Adresai“, „Iškrovimas“; „Schema“
- Paslaugos šablonas: „Skaityti visą tekstą“; „Penki principai“ (Keleivių); poskyrių meniu „Apie paslaugą · Privalumai · Kliento atsakomybės · Draudžiami daiktai · Kryptys · Užklausa“; spec. juostos reikšmės iš § 5.5 lentelės stulpelio „Svarbu“
- Grafikas: „Artimiausi išvykimai iš Lietuvos ir grįžimai į Lietuvą. Vietą rezervuokite telefonu.“; filtras „Visi · Airija · Ispanija“; „Išvykimo laiką ir vietą suderiname telefonu“; atsarginis tekstas „Artimiausias datas sužinokite telefonu“
- Siuntos sekimas: „Kodo neturite ar kyla klausimų? Paskambinkite:“; antraštė „Rezultatas“
- Taisyklės: įžanga paimta iš seno meta aprašymo (reikia patvirtinti, ar ji vis dar galioja)
- 404: „Tokio puslapio nėra“, „Grįžkite į pradžią arba paskambinkite – padėsime.“, „Maršrutas nerastas“, „Į pradžią“
- Visų puslapių nauji meta aprašymai (su lietuviškomis raidėmis)
- Telefonų numerių rodymo formatas (+353 86 450 3104, +44 7566 878681, +34 602 547 929)
- Rašybos klaidų taisymai taisyklėse ir paslaugų tekstuose

---

## 14. Custom CSS/JS appendix (for Salient › Theme Options › Custom CSS/JS)

These are the only non-native parts. Each snippet is small and hangs off Extra Class Names.

**A — Hairline grid (`sgp-grid`, `sgp-grid--x`, `sgp-grid--draw`)**
```css
:root{--sgp-m:clamp(16px,3.4vw,48px);--sgp-gut:24px;--sgp-cols:12;--sgp-max:1440px;--sgp-gl:rgba(22,24,26,.075)}
@media(max-width:999px){:root{--sgp-gut:16px;--sgp-cols:8}} @media(max-width:690px){:root{--sgp-gut:12px;--sgp-cols:4}}
.sgp-grid{position:relative}
.sgp-grid.light-text,.sgp-grid[data-midnight="light"]{--sgp-gl:rgba(255,255,255,.075)} /* verify the light-row hook on staging; else add class sgp-grid--dark */
.sgp-grid::before{content:"";position:absolute;inset:0 auto 0 50%;z-index:1;pointer-events:none;transform:translateX(-50%);
  width:calc(min(100% - 2*var(--sgp-m),var(--sgp-max)) + var(--sgp-gut));
  background:linear-gradient(90deg,var(--sgp-gl) 1px,transparent 1px) 0 0/calc(100%/var(--sgp-cols)) 100%;
  border-right:1px solid var(--sgp-gl)}
.sgp-grid > .row-bg-wrap{z-index:0}.sgp-grid > .col.span_12{position:relative;z-index:2}
```
`--draw` replaces the gradient with 13 `<i>` spans that JS injects: `transform: scaleY(0)` → `1`, 1400ms easeOutExpo, stagger 45ms. `--x` adds two 9px crosses at the top edge (tile: `.gl.x`).

**B — Lane lines + hero connector:** `.sgp-lanes{display:inline-grid;gap:3px;width:22px}.sgp-lanes i{height:2px;background:#EF4539;transform-origin:left}`. The hero H1 markup, the connector SVG paths (desktop 150×184 and phone 95×184 viewBoxes) and their CSS are exactly as in `kryptis-B.html` (`.h1v`, `.h1-link`), and can be copied into a Raw HTML element.

**C — Date chip:** `.sgp-date{display:inline-grid;justify-items:center;min-width:40px;padding:5px 4px 4px;border:1px solid currentColor}` with `b` in SSXC 800 21px and `i` in mono 8.5px uppercase, 70% opacity. The border colour is `--hair-d` on dark and `--hair-2` on light.

**D — Spec sheet:** `.sgp-kv{display:grid;grid-template-columns:minmax(150px,2fr) 5fr}.sgp-kv dt,.sgp-kv dd{margin:0;padding:15px 0;border-bottom:1px solid var(--hair)}.sgp-kv dt{color:#5E666E}`. At ≤ 600px it becomes a single column.

**E — Route scrub (fallback when Lottie is not used) and stack index:**
- For each `.sgp-route path`, set `strokeDasharray = L` and compute the progress `p = clamp((0.9vh − top) / (height + 0.35vh))`.
- The trunk uses `p/0.6`; the branches use `(p − 0.45)/0.5`.
- For the stack index, mark as active the last card whose top ≤ its sticky top. About 25 lines in total (see the tile script).

**F — Primary button wipe:** `.sgp-btn a{position:relative;overflow:hidden;isolation:isolate}.sgp-btn a::before{content:"";position:absolute;inset:0;background:#16181A;transform:scaleX(0);transform-origin:right;transition:transform .45s cubic-bezier(.645,.045,.355,1);z-index:-1}.sgp-btn a:hover::before{transform:scaleX(1);transform-origin:left}`

**G — Fields (Fluent Forms):** see tile `.in-f`: 54px, 2px radius, `--sheet`/`--graphite-2` background, focus `inset 3px 0 0 #EF4539`, labels in mono 11px uppercase.

**H — Reduced motion:** copy the tile's `@media (prefers-reduced-motion: reduce)` block. Add `.nectar-split-heading .line, [data-animation] {transform:none!important;opacity:1!important}` and guard the Lenis init.

**I — Video pause (WCAG):** a button `.sgp-video-toggle` that finds the row's `video` element and toggles `play()`/`pause()`, `aria-pressed` and its label.

---

## 15. Media map (ids used by B)

| Where | Id(s) |
|---|---|
| Home hero | `v29374299` (poster from media.json); fallback #36383706 |
| Home about | #6720534 |
| Home routes | #2881400 (IE), #27868340 (ES) |
| Home services | #6170458, #12418936, #29566910, #36377055, #32872983, #7464393 |
| Home band | #31570314 (alt #8858566) |
| Home process | #6169133, #7464731, #13456097, `v13707149` SD, #4440774 |
| Apie mus | #7541981, #9989463, #2449454, #31570314, #6169133, #8858566 |
| Pervežimo paslaugos | #36383706 + per-slug featured images |
| Tarptautiniai | `v4685871`, #3220828, #32821932 |
| Service pages | § 5.5 table (hero + band per slug) |
| Grafikas | #9807331 (texture) |
| Kontaktai | #1696742 (optional) |
| 404 | #4040619 |
| Held for phase 2 (only if the ferry/UK routing is confirmed) | `v19274366`, `v3987777`, #15885602, #35531295, #35497082 |

None of the v1 ids (12261472, 5025635, 34539243, 33384858, 39572426, 5025663, 12615250, 34369733, 7183495) are used.
