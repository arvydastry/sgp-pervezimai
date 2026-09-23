# Direction C: „Naktinis reisas“ (Night Run)

**SGP pervežimai v2** · art direction and build spec for **Salient 18.3** (WPBakery 8.7.3, Salient Core 3.1.6)
**Style tile / home preview:** `docs/kryptys/kryptis-C.html`. It uses a relative logo path, so serve the project folder (for example `python3 -m http.server` from the repo root) and open `/docs/kryptys/kryptis-C.html`. The **Salient žymės** button (bottom left) overlays the Salient element and option behind every block.
**Content sources:** `turinys-puslapiai.md`, `turinys-paslaugos.md`. **Media:** `media.json` ids only. **Element names** follow `salient-elementai.md`.

---

## 1. Concept

**In three sentences.** The site is the journey itself. It is a night run from Lithuania to Dublin or Madrid, told in blue-hour road footage on deep ink surfaces, and the brand red appears only where a tail light would: the next departure, the active item, the thing to press. Emotional chapters happen at **night** (dark, cinematic, layered parallax), practical chapters happen by **day** (light, high-contrast timetables, rules, forms), and the page background dissolves between them with Salient's Color Change Section, the way dawn arrives on a long drive.

**Why it fits SGP's audience.** SGP's customers are Lithuanians in Ireland, the UK and Spain and their families at home. For them this road is personal: the minibus trip lasts 3–4 days and runs „tiek dieną, tiek naktį“ (source: the passenger comfort text). Night imagery of that road is familiar and emotional, which is why the direction centres on the line „Du namai, vienas kelias tarp jų“. The design still behaves like a dispatch office:
- the next departure dates and tap-to-call numbers are in the first viewport;
- every date, code and phone number is set in monospace like a departure board;
- all rules and forms sit in bright "day" chapters, where legibility beats mood.

Red means one thing only, *now / next / press*, so it never turns into decoration or "nightclub".

**How it differs from v1** (v1 = `v1/index.html`, all its signature moves are avoided):

| v1 signature | v2 · C „Naktinis reisas“ |
|---|---|
| Warm beige #EFEDE8, yellow #FFC21A accent | Blue-ink night surfaces (#0C1015) and cool concrete "dawn" (#E8ECEF). **Brand red #EF4539 is the only accent.** No yellow or amber anywhere. |
| Inter Tight, giant centred ALL-CAPS stacked slogan | Archivo variable in three "voices": condensed sentence-case display, **expanded** tiny sign labels, and IBM Plex Mono for data. Headlines are **left-aligned and bottom-anchored**, never centred and never all-caps. |
| Hero background colour morphs on scroll | A real night-motorway video hero (29374299, red tail-light streams) with a glass **departure board** and two phone buttons |
| Video card scales up under the hero | An inline-media headline plus a full-bleed panel that **opens via clip-path inset** (2.39:1 cinemascope → full width) |
| Rotating circular text badge | None. The only "live" motion is a pulsing **tail-light dot** on the nearest departure. |
| Services as full-width rows with a cursor-following image | Services as a **horizontal pinned "depot"** of 11 tall graded cards: 3D tilt, "headlights on" grade, red lane line, hover video |
| Word-by-word highlighted about statement on black | Static verbatim statement plus **Milestone** counters on lane dividers (no scroll-highlight) |
| Two tall parallax route cards | **Sticky Media, Scrolling Content**: the routes swap footage (ferry wake / Madrid dusk / German light trails) above a schematic lane map that draws itself |
| Outlined/solid giant marquee | None. The **route rail** (the header hairline doubles as a progress road) replaces the "movement" cue. |
| Four white step cards | A vertical **lane timeline** (door to door) with a sticky caption |
| Yellow rounded CTA block with pill checkboxes | A night CTA over red tail-light bokeh: numbers grouped by direction in large mono, and a **glass** form with a select |
| Giant footer wordmark | A structured dispatch footer with all 11 services, a lane rule and the Footer Reveal effect |
| Pills and 22px radii | Signage geometry: 2/4/6/10px radii and square line caps, taken from the logo's right-angled parallel lines |

---

## 2. Design tokens

### 2.1 Colour

Palette logic: **Naktis** (surfaces for story), **Diena** (surfaces for information), **Signalas** (the brand red family, used only as a signal). The target share per page is about 65% night, 30% day and 5% red at most.

| Token | Hex | Role | Contrast (WCAG 2.2) |
|---|---|---|---|
| `night-900` | `#07090C` | Footer, overlays, menu, deepest shadow | Headlight on it 18.0:1 |
| `night-800` | `#0C1015` | **Night page background** (Color Change target) | Headlight 17.3:1 · Tail 5.1:1 · Fog-400 6.4:1 |
| `night-700` | `#121820` | Cards, raised surfaces | Headlight 16.1:1 · Tail 4.7:1 (AA text) |
| `night-600` | `#19212B` | Hover surface | Tail 4.3:1: **large text or UI only** |
| `night-500` | `#243040` | Strong borders on night | Decorative |
| `fog-500` | `#6B7785` | Decorative text, placeholders | 4.2:1 on night-800: **large only** |
| `fog-400` | `#8B97A5` | Secondary and meta text on night | 6.4:1 on night-800 · 6.0:1 on night-700 |
| `fog-200` | `#C3CCD5` | Lead text, body on night | 11.7:1 |
| `headlight` | `#F2F4F1` | Primary text on night (slightly warm white) | 17.3:1 |
| `dawn-100` | `#E8ECEF` | **Day page background** (Color Change target) | Night-800 on it 16.0:1 |
| `dawn-50` | `#F5F7F8` | Cards and inputs on day | — |
| `dawn-200` | `#D5DBE0` | Hairlines on day | Decorative |
| `slate-600` | `#4A5563` | Secondary text on day | 6.4:1 on dawn-100 |
| `dusk` | `#1B2A3A` | Split-tone colour for image grading only | — |
| **`tail`** (brand) | **`#EF4539`** | Logo, lane lines, dots, route lines, focus rings in menus, red text **on night** | 5.1:1 on night-800 (AA). On dawn-100 it is only 3.2:1, so on day use it for **UI and ≥24px text only** |
| `brake` | `#D5362B` | **Filled button background** (white label) | White on it 4.8:1 (AA). *#EF4539 with white is only 3.8:1, which fails AA, hence this shade.* |
| `brake-deep` | `#B92A20` | Button hover and pressed | White 6.2:1 |
| `tail-ink` | `#B8281D` | Red **text/links on day** | 5.3:1 on dawn-100 · 5.8:1 on dawn-50 |
| `tail-soft` | `#FF7A70` | Error text on night | 7.5:1 on night-800 |
| `tail-glow` | `rgba(239,69,57,.55)` | The "bloom" shadow only | — |
| lines | `rgba(242,244,241,.12)` night · `rgba(12,16,21,.14)` day | Hairlines | — |

Salient setup: **Theme Options → Accent Color** `#EF4539`. **Extra Color 1** `#D5362B` (buttons), **Extra Color 2** `#0C1015`, **Extra Color 3** `#E8ECEF`. Colour rules:
- Red never fills a large area.
- There is at most one pulsing dot per viewport.
- Never put red text on day backgrounds below 24px; use `tail-ink` instead.

### 2.2 Typography

**Families** (Google Fonts, both with latin-ext, so ą č ę ė į š ų ū ž render natively; tested in the tile):
- **Archivo**, variable, `wdth 62–125`, `wght 100–900`. One family, three voices through the width axis.
- **IBM Plex Mono** 400/500, for dates, times, phone numbers, route codes and counters.

Loading: `https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500&display=swap`.
- Salient's Typography panel requests static weights only, so the **width axis would be lost**. Instead, self-host the variable woff2 files (latin plus latin-ext subsets) and declare `@font-face { font-family:"Archivo"; font-weight:100 900; font-stretch:62% 125%; }` in Custom CSS.
- Also select "Archivo" in each Salient typography field, so sizes and weights are still managed there.
- Self-hosting also removes the Google request (GDPR), which matches Salient's *Local Google Fonts* intent.
- Width is applied with `font-stretch` in the class snippets below.

| Role | Axes / weight | Size, fluid `clamp()` (390→1440) | Salient fields D / T / P | Line height | Tracking | Case |
|---|---|---|---|---|---|---|
| **Display / H1 home** | wdth 72 · 560 | `clamp(2.75rem, 1.35rem + 5.75vw, 6.5rem)` | 104 / 72 / 44 px | 1.02 | −0.025em | Sentence case |
| **H1 inner pages** | wdth 72 · 560 | `clamp(2.5rem, 1.5rem + 4.1vw, 5.25rem)` | 84 / 64 / 40 | 1.02 | −0.025em | Sentence |
| **H2** | wdth 75 · 540 | `clamp(2.125rem, 1.25rem + 3.6vw, 4.5rem)` | 72 / 56 / 34 | 1.04 | −0.02em | Sentence |
| **H3** | wdth 85 · 600 | `clamp(1.5rem, 1.1rem + 1.55vw, 2.25rem)` | 36 / 30 / 24 | 1.10 | −0.01em | Sentence |
| **H4 / card title** | wdth 90 · 600 | `clamp(1.25rem, 1.05rem + .8vw, 1.625rem)` | 26 / 22 / 20 | 1.15 | −0.005em | Sentence |
| **Statement** (about lead) | wdth 88 · 420 | `clamp(1.375rem, 1rem + 1.45vw, 2.375rem)` | 38 / 30 / 22 | 1.24 | −0.012em | Sentence |
| **Lead** | wdth 100 · 400 | `clamp(1.125rem, 1rem + .5vw, 1.375rem)` | 22 / 20 / 18 | 1.5 | 0 | Sentence |
| **Body** | wdth 100 · 400 | `clamp(1rem, .95rem + .2vw, 1.0625rem)` | 17 / 17 / 16 | 1.65 | 0 | max 68ch |
| **Small** | wdth 100 · 400 | 14px | 14 | 1.5 | 0 | — |
| **Sign label** (eyebrow, nav meta, field labels) | **wdth 125** · 600 | 12px (fields 11px, buttons 10.5px) | 12 | 1.3 | **+0.16em** | UPPERCASE, only at ≤13px |
| **Mono data** | Plex Mono 500 | 15px (chips 12.5, board 14) | 15 / 15 / 14 | 1.2 | 0 | Tabular |
| **Mono XL** (phones in CTA) | Plex Mono 500 | `clamp(1.25rem, 1rem + 1vw, 1.875rem)` | 30 / 26 / 22 | 1.2 | −0.01em | — |
| **Numeral** (Milestone) | wdth 62 · 250 | `clamp(4rem, 2.2rem + 7.4vw, 9rem)` | 144 / 104 / 64 | 0.9 | −0.03em | — |
| **Navigation** | wdth 100 · 500 | 15px | 15 | 1 | 0 | Sentence |
| **Button** | wdth 100 · 600 | 15px (sm 14) | 15 | 1 | +0.01em | Sentence |

Case and diacritic rules:
1. **Never** set display type in capitals. v1 did, and Lithuanian capitals with carons and ogoneks (Č Š Ž Ė above, Ą Ę Į Ų below) collide at tight leading.
2. Display line-height is never below **1.02**.
3. Any clip or mask reveal on text needs **0.12em** vertical padding so marks are not cut off.
4. Use Lithuanian quotes „…“, an en dash with spaces for routes (`Lietuva – Airija`), `→` for route codes (`LT → IE`) and `⇄` for two-way routes.
5. Wrap „3–4“ in a no-break span (`.nw`), because browsers break after the en dash.

### 2.3 Spacing

- **Scale:** 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192 px (4px base).
- **Section padding:** `clamp(4.5rem, 2.2rem + 9vw, 10rem)`, which is 72 / 125 / 160 px (P / T / D). In Salient, set Row Padding Top/Bottom per device to 160 / 112 / 72.
- **Heading → lead:** 18px. Eyebrow → heading: 28px. Section head → content: `clamp(40px, 5vw, 72px)`.
- **Card inner padding:** 22px. Glass panels: `clamp(20px, 3vw, 36px)`.

### 2.4 Grid and breakpoints

| Range | Salient device | Columns | Gutter | Outer margin |
|---|---|---|---|---|
| ≥1000px | Desktop | 12 | 24px | 48px (container max 1360 content / 1425 Salient) |
| 691–999 | Tablet | 8 | 20px | 32px |
| ≤690 | Phone | 4 | 16px | **16px** |

Extra custom-CSS breakpoints:
- **1240px:** the navigation collapses to the burger.
- **600px:** finer phone tweaks. Salient's own phone breakpoint is 690.

### 2.5 Radii, borders, shadows

- **Radii:**
  - 2px: chips and tags.
  - **4px: buttons and inputs.** Theme Options → Button Styling: *Slightly Rounded*.
  - 6px: cards and media.
  - 10px: glass panels.
  - Circles are used only for the tail-light dot. **No pills.**
- **Borders:** 1px hairlines. Night: `rgba(242,244,241,.12)`, strong `.2`. Day: `rgba(12,16,21,.14)`, strong `.24`. Glass: `rgba(242,244,241,.14)`.
- **Shadows:**
  - Elevation on night: `0 30px 80px -30px rgba(0,0,0,.85)`.
  - Elevation on day: `0 1px 0 rgba(12,16,21,.04), 0 24px 48px -32px rgba(12,16,21,.4)`.
  - **Bloom** (red hover): `0 0 0 1px rgba(239,69,57,.55), 0 10px 36px -10px rgba(239,69,57,.65)`.
- **Glass:** `background: rgba(12,16,21,.52); backdrop-filter: blur(18px) saturate(1.3)`. Salient: Inner Row / Column → Backdrop Filter Blur, Badge/Button backdrop blur, Header background blur.

### 2.6 Iconography

- **Line icons only:** 24px grid, **1.5px stroke, square caps, miter joins**. They echo the logo's right-angled parallel lines. Colour is `currentColor`.
- **Preferred:** a custom 14-icon SVG set: phone, calendar, route, box, pallet, car-on-trailer, motorcycle, seat, paw, sofa/move, shield (insured), clock, download, ✕ (prohibited). Upload it and use it through the Icon element's image option or an Image element.
- **Fallback:** Salient's bundled **Iconsmind** line set (bus, box, car, motorcycle, dog, calendar, phone). Verify the glyph names in the picker.
- **Never** use emoji, Font Awesome solid icons or flag emoji. Country identity is carried by mono codes (`LT`, `IE`, `UK`, `ES`).

### 2.7 Image treatment: "Night grade"

1. **Pre-grade before upload** (a Lightroom/Photoshop preset called `SGP Night`):
   - Exposure −0.3.
   - Blacks lifted to #0C1015 on the tone curve.
   - Saturation −20.
   - Split tone: shadows #1B2A3A at 25%, highlights neutral.
   - Red and orange luminance +10, so tail lights stay hot.
   - Clarity −5.
   - Export WebP q78.
   - Faces and people (courier, movers) get a lighter version (exposure 0) so they are not lost in the dark.
2. **In-page grade** (CSS or overlay):
   - Cards at rest: `filter: brightness(.58) saturate(.7) contrast(1.06)`.
   - Media rows: Color Overlay → Advanced.
     - Horizontal: `linear 90° #07090C 90% (0%) → 62% (38%) → 20% (70%) → 45% (100%)`.
     - Vertical: a fade to `#0C1015` over the last 45%, so the row melts into the page.
     - Salient allows one overlay; add the second fade with the custom `.sgp-fade-b::after`.
3. **Hover "Headlights on":** over 800ms `ease-io`, `brightness .58 → .84`, `saturate .7 → .95`, and scale `1 → 1.07`. The image never reaches full daylight, so the night mood holds.
4. **Duotone textures** (asphalt 4040619, wet road 9807331, tread 7019611): multiply #07090C → #243040 at 15–20% opacity. Use them only as section texture, never behind body text.
5. **Video:** the same overlay as photos. Videos are muted, loop, playsinline, always have a poster, and carry `aria-hidden`.
6. **Sourcing gap (recommend to the client):** there is no stock night footage of a *minibus* (`media.md` → „Nerasta … keleivinio mikroautobuso“).
   - The long-term hero should be a **one-night shoot of SGP's own van**: tail lights, a motorway on-ramp, a drone shot at dusk.
   - This direction is built to swap that footage straight in.

### 2.8 Motion tokens

| Token | Value | Use |
|---|---|---|
| `ease-out` | `cubic-bezier(.215,.61,.355,1)` (easeOutCubic) | Entrances. **Theme Options → Column/Image Animation Easing: easeOutCubic** |
| `ease-expo` | `cubic-bezier(.16,1,.3,1)` (easeOutExpo) | Lane lines, masks, underlines, card tilt |
| `ease-io` | `cubic-bezier(.65,0,.35,1)` (easeInOutCubic) | Colour and tone changes, crossfades |
| micro | 160ms | Colour on links |
| short | 280ms | Button background, border |
| med | 480ms | Lane line draw, arrow nudge, bloom |
| long | 900ms | Image scale on hover, clip reveals |
| enter | **1200ms** | Column entrances. **Theme Options → Column/Image Animation Timing: 1200** |
| tone | 800ms | Color Change Section |
| stagger | words 90ms · cards 120–150ms · columns 150ms · rows 80ms | Animated Text stagger and column delays |
| trigger | element top at 88% of viewport | Salient default offset |
| parallax | hero BG **Subtle** (≈0.18) · CTA BG **Medium** (≈0.15–0.22) · captions Move Y intensity 1–2 | Row → Parallax Background Media On Scroll |
| smooth scroll | Lenis, strength 50 | Theme Options → Smooth Scrolling ON |
| page transition | View Transitions API → **Fade** (through #07090C) | "Cut to black" |
| header | Hide Until Needed · Resize 88→68px · Navigation Entrance: Fade In 600ms | Theme Options → Header |

---

## 3. Signature system (unique to C)

1. **Juostos: the lane rule.** Three 1px parallel lines, 3px apart, 7px total. The top two are neutral and the bottom one is `tail`, drawn left to right. The idea comes from the logo mark's parallel right-angled strokes.
   - **Uses:**
     - section dividers;
     - the `lane-mini` 28px glyph in every eyebrow (`03 ═ GRAFIKAS`);
     - the milestone dividers (vertical, red on the top 38%);
     - the service card bottom edge (red draws in on hover);
     - text-link underline (a neutral hairline plus a red 2px line that grows);
     - the footer rule;
     - route lines in the schematic.
   - **Salient:** Divider element with the Extra Class `sgp-lane`; it draws itself through the divider's own delay. Card and link versions use the classes `sgp-card` and `sgp-link` (§9).
2. **Galinis žibintas: the tail-light dot.** An 8px red circle with bloom: `0 0 0 3px rgba(239,69,57,.18), 0 0 14px 2px rgba(239,69,57,.55)`.
   - It marks "now / next / active": the nearest departure, the active nav item, the current route chapter, form focus.
   - **Only one dot pulses per viewport**, at 2.4s `ease-io`, on the nearest departure.
   - **Salient:** Icon element (Pulsating Circle) or custom `.sgp-dot` span inside Text Block.
3. **Išvykimų lenta: the departure-board row.**
   - **Anatomy:** tail dot · route code in mono (`LT → IE`) · route name in small sans · date chips in mono (the next date outlined red) · phone in mono with a sign label · a 44px arrow square.
   - **On day chapters**, hovering **flips the row to night**: the ink fill scales up from the bottom in 500ms `ease-expo`, the text turns headlight, the dot lights up and the arrow fills brake red.
   - **Salient:** Horizontal List Item, 4 columns, Style *Bottom Border, Color Hover Effect*, hover colour `#0C1015`, CTA = `tel:`. The mini variant (glass board) uses a Global Section.
4. **Maršruto juosta: the route rail.** The header's 1px bottom hairline is the road.
   - A red gradient fills it and a red dot travels along it as the page scrolls, with 1px ticks at each chapter boundary.
   - **Salient:** custom CSS on `#header-outer::after` with a scroll-driven animation (`animation-timeline: scroll(root)`). No JavaScript. Browsers without support show a static hairline (§9).
5. **Windscreen inline media.** Small 16:9 video or photo windows inside headlines.
   - Size `1.42em × .8em`, 4px radius, with a 2px red underline.
   - They reveal through **Circle Mask Reveal**, staggered by 150ms.
   - **Salient:** Text With Inline Media, animation *Circle Mask Reveal*, roundness 4px, inherit heading typography.

**System rules:**
- Emotional content lives in *Night* chapters. Schedules, rules, tracking and forms live in *Day* chapters.
- The Color Change Section is the only transition between them; there are no hard colour cuts.

---

## 4. Component inventory

Global state rules, which apply to every component:
- **Focus-visible:** 2px outline, `headlight` on night or `night-800` on day, offset 3px. In the fullscreen menu the outline is `tail` with offset 6px.
- **Touch targets:** at least 44×44px.
- **Hover-only reveals are forbidden:** on touch devices (`hover: none`) every hover-revealed item is visible at rest.

### 4.1 Header

| State | Spec |
|---|---|
| **Transparent** (over hero) | 88px tall. `logo_light.svg` at 40px high. Nav: Archivo 500 15px `fog-200`. Top gradient `rgba(7,9,12,.62) → 0` (Salient 18: gradient background blur on the transparent header). The route rail hairline is visible. |
| **Scrolled** (>40px) | Height 68px, logo 34px. `background rgba(12,16,21,.62)` plus `backdrop-filter: blur(18px) saturate(1.4)` (Header Background Blur ON, BG opacity 62%). It **stays dark on day chapters** too, like a dashboard. |
| **Hidden** | *Hide Until Needed:* it hides after 90vh when scrolling down and returns on scroll up. It never hides while the call dropdown or the menu is open. |
| **Nav hover** | Text becomes headlight, and a 2px `tail` underline scales in from the left over 480ms `ease-expo` (Header Link Hover Effect: Animated Underline). **Active** item: a 5px tail dot 12px to its left. |
| **Right side** | [**Skambinti**] glass small button (42px) opening a **call dropdown** (below) · [**Gauti pasiūlymą**] brake-red small button (links to the CTA/form). |
| **Call dropdown** | 300px glass panel with two groups: „Airijos kryptis“ (LT +370 650 53161 · IE +353 86 450 3104 · UK +44 7566 878681) and „Ispanijos kryptis“ (LT +370 638 28919 · ES +34 602 547 929). Each row is a mono number plus a country code. On hover the row background lightens to `rgba(242,244,241,.07)` and the code turns red. **Salient:** menu item with the button style *See Through* and a sub-menu (Superfish), or a mega-menu Global Section. Closes on Esc or an outside click. |
| **≤1240px** | The nav collapses; a 44px burger appears (two lines, the second 12px long, which grows to 18px on hover). |
| **≤690px** | 64px bar: logo 32px · a **red 44px phone icon button** (opens the call options or jumps to the CTA) · burger. The primary text button is hidden, because the mobile call bar takes over. |

Nav items (new order, now **with Grafikas**, which the live site hides): Paslaugos · Kryptys · Grafikas · Siuntos sekimas · Taisyklės · Apie mus · Kontaktai.

### 4.2 Off-canvas / fullscreen menu

- **Salient:** Off Canvas Menu → **Fullscreen Inline with Dynamic BG**. Background `#07090C`.
- **Per-item background images** (set on each menu item) fade in at 60% opacity, graded and under a 90° ink gradient:
  - Paslaugos 38927007
  - Tarptautiniai pervežimai 2881400
  - Pervežimų grafikas 36383706
  - Siuntos sekimas 4487517
  - Taisyklės 6169133
  - Apie mus 7541981
  - Kontaktai 11479826
- **Links:** Archivo wdth 72, weight 540, `clamp(2.25rem, 1.2rem + 3.6vw, 4.5rem)`, colour `fog-400`, with a mono index (`01`–`07`).
  - Hover or focus: text turns headlight and the index turns red.
  - Entrance: translateY 26px → 0, staggered 60ms, over 900ms `ease-expo`.
- **Right column** (Off-canvas Global Section): phones grouped by direction in mono, and the email.
- **Behaviour:** Lenis stops while the menu is open, Esc closes it, and focus returns to the burger.

### 4.3 Buttons

| Type | Rest | Hover | Focus / active | Salient |
|---|---|---|---|---|
| **Primary „tail“** | `#D5362B` background, white 600 15px, 52px high, 22px horizontal padding, 4px radius, a 18px line arrow | Background `#B92A20` plus **bloom** shadow; arrow +4px (480ms `ease-expo`) | Outline 2px, offset 3; active translateY 1px | Button → **Arrow Animation**, colour Extra Color 1, hover background `#B92A20` |
| **Glass** (on night) | `rgba(242,244,241,.06)` background, 1px `rgba(242,244,241,.26)` border, blur 12px, headlight text | Border becomes headlight, background `.11`, and a **6px tail dot scales in** at the left edge | Same as above | Button → See Through + backdrop blur, Extra Class `sgp-glass` |
| **Ink** (secondary on day) | Transparent, 1px `rgba(12,16,21,.3)` border, night-800 text | Border night-800, background `rgba(12,16,21,.05)` | Same as above | Button → See Through (dark) |
| **Phone** | Glass, 62px high, a phone icon, two lines: a sign label (for example „Airijos kryptis“) and a mono number | As glass; the label brightens | Same as above | Button with a two-line label via Extra Class `sgp-phone` (or an Icon List item) |
| **Text link** | 600 15px with a neutral 1px underline at 30% | A red 2px underline grows to 100% (480ms), arrow +4px | Same as above | Button → **Underline** type, or global link style `.sgp-link` |
| **Icon button** (phone, ≤690) | 44px `brake` square, white icon | `brake-deep` | Same as above | Button (icon only) |

### 4.4 Service card (depot / grid)

- **Size:** portrait, `clamp(292px, 28vw, 420px)` wide, `min(62vh, 580px)` tall (at least 440px). 6px radius, 1px border `rgba(242,244,241,.1)`.
- **Layers:**
  1. Media (Night-graded photo; optional hover MP4).
  2. Gradient: 180°, ink 60% → 0 at 26% → 10% at 46% → 94% at the bottom.
  3. Top row: mono `01 / 11` and a 44px glass arrow square (the arrow rotated −45°).
  4. Body: H4 title, a one-sentence summary (`fog-200` 15px), 2 mono fact chips.
  5. Lanes: two neutral hairlines at the bottom, plus the red one that draws in.
- **Hover / focus-visible:**
  - **3D tilt** of up to ±4° X and ±5° Y following the pointer, with the media counter-shifting ±16/12px (depth).
  - Image scale 1.07 plus "headlights on" grade (900ms).
  - The red 2px lane with glow draws along the bottom (480ms `ease-expo`).
  - The arrow square fills brake red, gains bloom and rotates to →.
  - The body lifts 6px; fact chips brighten.
  - **Hover video** on 3 cards: automobiliai 34371915 SD, motociklai 34308329 SD, negabaritiniai 19552565 SD. They use `preload="none"`, load on first hover, crossfade in 600ms and pause on leave.
- **Touch:** no tilt and no video; everything is visible at rest.
- **Salient:**
  - Fancy Box → **Parallax Hover Effect** (layered tilt), background image, min height 62vh, link to the service page.
  - Extra Class `sgp-card` for grade, lanes and chips.
  - Hover video is custom JS (§9).
  - The alternative with no tilt is Fancy Box → Description on Hover (Long Zoom).

### 4.5 Route block (sticky media chapter)

- **Text side (5/12):**
  - sign `● KRYPTIS 01`;
  - H3 (wdth 75, 560, `clamp(1.75rem, 1.1rem + 2.3vw, 3rem)`), for example „Lietuva ⇄ Airija“;
  - a verbatim sentence;
  - a **phone list** with 1px rules: country sign code, mono number, and a hidden „Skambinti →“. On hover the row slides 8px right and the label fades in red;
  - a **date list** with sign labels („Iš Lietuvos“, „Į Lietuvą“) and mono dates.
- **Inactive blocks** fade to 32% opacity while the section is live (desktop only).
- **Media side (7/12):**
  - a sticky frame, top 12vh, height 76vh, 6px radius;
  - layers crossfade over 1000ms `ease-io` and scale 1.08 → 1 over 1800ms `ease-expo`;
  - a mono caption top-left with a live dot (`LT ⇄ IE`);
  - the **schematic lane map** in a glass panel bottom-left, max 500px.
- **Schematic:** LT → PL → DE, then a branch to IE (with a dashed "sea" segment and **no intermediate countries**, because the Ireland path is unconfirmed) or to ES via BE and FR.
  - The active branch draws in red via `stroke-dashoffset` (1100ms `ease-expo`, branch delayed 450ms).
  - Active nodes become filled red 10px squares.
  - The *Pakeliui* state lights up PL, DE, BE, FR and turns the lines headlight.
- **Salient:**
  - Sticky Content Sections → **Sticky Media, Scrolling Content** (media width 55%, height 76vh, Subtract Nav Height).
  - The map is an inline SVG in a Raw HTML element. Line drawing is either a Lottie with **Scroll Position Seek** or a 20-line class toggle.

### 4.6 Schedule row

See signature 3. Full-width variant grid: `minmax(150,190px) | 1fr (dates) | 172px (phone) | 44px`, 22px vertical padding, 1px rules. At ≤690 it stacks: code+name / arrow, then dates, then phone.

**Date format:** „Spalio 9 d.“ in full on the timetable and „Spal. 9 d.“ abbreviated on the board. **Never numeric**, because „10-09“ reads as 10 September for Irish-trained eyes.

The **next** date gets a red outline and a 10% red wash. The earliest departure overall also gets the pulsing dot.

### 4.7 Data / stat block (Milestone)

- **Layout:** 4 columns on lane dividers (vertical triple line, red on the top 38%); 2×2 at ≤999.
- **Content:** a sign label, a Numeral in headlight, and a 15px `fog-400` sub-line.
- **Salient:** Milestone → **Count To Value**, 1500ms, delays 0/150/300/450. „3–4“ uses **Motion Blur Slide In**.
- **Allowed numbers only:**
  - **2** kryptys;
  - **11** paslaugų;
  - **3–4** paros kelyje;
  - **4** šalys pakeliui (Lenkija, Vokietija, Belgija, Prancūzija);
  - optionally **8** reisai spalį, counted from the schedule, if the client keeps the schedule complete.

### 4.8 CTA band

- **Background:** night-900 with 7024783 (red tail-light bokeh) at 62%, Parallax **Medium**, overlay radial `120% 90% at 85% 10%` fading to ink 90%.
- **Left (6/12):** eyebrow, H2 „Paskambinkite pagal kryptį“, verbatim lead, then two **direction groups**:
  - a sign label with a dot;
  - rows of the country code, a **Mono XL** number, and a hidden „Skambinti →“. On hover the row pads left 10px and the label turns red;
  - then the email with a „Kopijuoti“ button.
- **Right (5/12):** the glass form (§4.9).
- **Salient:** Row with a background image, Parallax Medium and Color Overlay Advanced; Column Backdrop Filter Blur 20px on the form; Global Section „Užklausa“ reused site-wide, except on Kontaktai and Privatumo politika.

### 4.9 Form fields

| State | Night (CTA, menu) | Day (tracking, contacts) |
|---|---|---|
| Rest | 52px high, 4px radius, `rgba(242,244,241,.045)` background, 1px `rgba(242,244,241,.18)` border, headlight text, placeholder `fog-500` | `dawn-50` background, 1px `rgba(12,16,21,.24)` border, night-800 text, placeholder #6B7582 |
| Hover | Border `.34` | Border `rgba(12,16,21,.4)` |
| **Focus** | Border headlight, background `.08`, **inset 3px red bar on the left** (`box-shadow: inset 3px 0 0 #EF4539`); the label turns headlight | Border night-800, white background, the same red bar |
| Error | Border `tail`; message 13px `tail-soft` | Border `tail`; message `tail-ink` |
| Success | Mono line below the button: „Jūsų žinutė sėkmingai išsiųsta“ | Same |
| Label | Sign style 11px, +0.16em, above the field; **always visible**, never placeholder-only | Same |

- **Select:** custom chevron, 1.5px stroke.
- **Textarea:** minimum 118px high. The minimum length (20 characters) is enforced with an inline message.
- **Salient:** **Fluent Forms** (fully compatible since 18.0) with Theme Options → Form Styling, plus custom CSS `.sgp-form`.
- **Spam protection:** reCAPTCHA v3 or Turnstile, which is invisible and replaces the old v2 box.

### 4.10 Footer

- **Surface:** night-900, `padding-top clamp(64px, 7vw, 112px)`.
- **Columns:** 4 columns → 2 → 1:
  1. `logo_light.svg` at 44px with the slogan sentence.
  2. **Tarptautiniai pervežimai:** all 11 services, for SEO continuity with the live footer.
  3. **Įmonė:** Apie mus, Pervežimų grafikas, Siuntos sekimas, Taisyklės, Kontaktai, Privatumo politika.
  4. **Telefonai** in mono.
- **Links:** hover turns headlight and shifts 4px right (400ms `ease-expo`).
- **Bottom:** a lane rule, then „© 2026 sgp-pervezimai.lt. Visos teisės saugomos.“ plus a slot for company requisites (see §8).
- **Salient:** Global Section in the Footer location; **Footer Reveal Effect** ON with shadow. **No wordmark.**

### 4.11 Inner page hero ("tunnel") and breadcrumb

- **Row:**
  - Full width, Min Height **62svh** (min 460px). Service pages use 70svh; utility pages (schedule, tracking, rules) use 52svh.
  - Background image or video with Parallax **Subtle**.
  - Background Layer Animation **Slight Zoom Out Reveal**.
  - Overlay Advanced: the same horizontal gradient as the hero, plus the custom bottom fade.
- **Content** (bottom-left):
  - **Breadcrumb:** Plex Mono 12px `fog-400`, with `/` separators on neutral hairlines and the current item in headlight. **Salient:** Text Block with `[rank_math_breadcrumb]` or `[wpseo_breadcrumb]`.
  - **H1:** Animated Text → **Word Blur**, stagger 90ms.
  - **Lead:** verbatim summary, Column Fade In From Bottom, 600ms delay.
- **Right** (desktop, 4/12): a **glass mini card**, either „Artimiausi pervežimai“ filtered to the relevant direction or phone buttons.
- **Bottom edge:** lane rule.
- **Scroll:** content Column Scroll Position Advanced translateY 0 → −60px.

### 4.12 Smaller components

- **Chip:** Plex Mono 12.5px, 7×9px padding, 2px radius, 1px border. The *next* variant has a red border and a 10% red background.
- **Callout** (fines, important notes): day surface `dawn-50`, 1px `tail-ink` border, 6px radius. A mono label such as `Taisyklių 4.5 p.` and a large figure. Used for „1200 EUR“, with Milestone Motion Blur Slide In.
- **Prohibited-items list:** a chip grid with a ✕ line icon, 2–3 columns. **Salient:** Fancy Unordered List (icon list, staggered entrance).
- **PDF card:** a file icon, „Sutartis su siuntėju“, `PDF · 72 KB` in mono, and a „Atsisiųsti“ button (See Through). Hover: lane draws and the icon lifts 2px.
- **Toggle panels** (rules, FAQ-like blocks): Toggle Panels → **Minimal Shadow**, deep-linkable.
- **Reviews placeholder:** a dashed 1px `rgba(242,244,241,.28)` box with the sign „Atsiliepimai“, „Čia bus tikri klientų atsiliepimai“ and the note „Vieta rezervuota – laukiame kliento pateiktų atsiliepimų. Išgalvotų atsiliepimų nenaudojame.“. Later it becomes Testimonial Slider → Multiple Visible Minimal.
- **Mobile call bar** (≤690, appears after 70% of the first viewport):
  - A glass bar pinned to the bottom (10px inset, safe-area aware) with three 50px buttons: **Airija** (+370 650 53161, brake) · **Ispanija** (+370 638 28919, brake) · **Grafikas** (glass).
  - **Salient:** Global Section with Row → **Sticky Row: Bottom of Window**, *stay on mobile*, visible on phones only. Verify Sticky Row behaviour inside a Global Section; the fallback is 15 lines of `position:fixed` CSS.
- **Hero video pause:** a small mono glass button bottom-right, „Pauzė“ / „Tęsti“. It is required by WCAG 2.2.2 for looping background video (custom JS, §9).
- **Cookie banner:** a bottom-left glass card (max 420px) with the verbatim H4 and text and the buttons „Sutinku“ (primary) and „Plačiau“ (link). Use a consent plugin (Complianz or CookieYes) restyled to these tokens, and add a reject option (see §8).

---

## 5. Page blueprints

Legend used in every row:
- **Salient** = element → option.
- **FX** = effect, with trigger and values.
- „…“ = verbatim from the turinys files.
- *(N)* = new text, listed in §8.
- Media numbers are `media.json` ids.

### 5.0 Global building blocks (build these first)

| Global Section | Content | Used on |
|---|---|---|
| **GS-Header / menu** | Theme Options (§4.1–4.2) plus an off-canvas Global Section (phones, email) | All |
| **GS „Artimiausi pervežimai“** (Day table) | H2 „Artimiausi pervežimai“, 4 schedule rows, the duration footnote *(N)* | Home, Grafikas, Taisyklės, Tarptautiniai, service template, Siuntos sekimas |
| **GS „Artimiausi pervežimai – mini“** (glass board) | The same dates, compact | Home hero, inner hero cards |
| **GS „Paslaugų tinklelis“** | 11 service cards (§4.4) as a grid: 3 columns desktop, 2 tablet, Flickity 1.15 on phone | Paslaugos overview, Tarptautiniai, Apie, 404 (compact 4) |
| **GS „Užklausa“** | CTA band (§4.8) | All except Kontaktai and Privatumo politika |
| **GS „Skambučių juosta“** | Mobile call bar | All (phone only) |
| **GS-Footer** | §4.10 | All |

**Schedule data.** The dates change twice a month.
- **Recommended:** an ACF Options page „Grafikas“ with 4 routes, each holding a repeater of full dates *(the year is stored, which solves „metai nenurodyti“)*, plus a ~60-line shortcode `[sgp_grafikas variant="table|board|mini" kryptis="ie|es|all"]` placed in Text Blocks.
  - It auto-hides past dates.
  - It marks the nearest date as *next*.
  - It prints an „Atnaujinta“ stamp.
  - It feeds both Global Sections from one source.
- **Zero-code fallback:** edit the two Global Sections by hand.

### 5.1 Home (showpiece)

The home page has 11 content sections plus header, footer and call bar.

**Colour chapters:** Night `#0C1015` (S1–S3) → **Day** `#E8ECEF` (S4) → Night (S5–S6) → **Day** (S7–S8) → Night (S9–S11) → footer `#07090C`. Every content row sets **Color Change Section** to its chapter colour and Text Color Light or Dark.

**S1 · Hero „Naktinis reisas“**
- **Purpose:** say what and where within 3 seconds, show the next departures, offer two tap-to-call options.
- **Layout:** Row Full Width Content, **Full Height** (100svh, min 680px), content at the Bottom. 12 columns: copy in columns 1–7, board in columns 8–12.
- **Content:**
  - eyebrow with the pulsing dot: „Saugiai · greitai · patikimai“ (the slogan);
  - **H1** *(N)* „Pervežimai tarp Lietuvos, Airijos ir Ispanijos“, with a lane underline on *Airijos* and *Ispanijos*;
  - lead *(N, derived)* „Keleiviai, siuntos, automobiliai, augintiniai ir perkraustymas – nuo durų iki durų. Kelionė trunka apie 3–4 paras nuo paėmimo dienos.“;
  - buttons: „Gauti pasiūlymą“ (the modal button label), phone „Airijos kryptis +370 650 53161“, phone „Ispanijos kryptis +370 638 28919“;
  - board: „Artimiausi pervežimai“ with 4 rows (LT→IE Spal. 9, 23 · LT→ES Spal. 9, 23 · IE→LT Rugs. 28, Spal. 15, 28 · ES→LT Rugs. 27, Spal. 14, 28), then „Visas grafikas →“ and „Siuntos sekimas“.
- **Media:**
  - **Video 29374299**: a European interchange at blue hour with red tail-light streams. It literally stages the "tail light" idea.
  - Poster: 29374299 jpg at 1920w, which is the LCP image.
  - Phones: poster only.
  - Fallback photo: 11053641.
- **FX:**
  - Background: Parallax **Subtle**; Background Layer Animation **Zoom Out Slowly**.
  - Overlay: Advanced 90° gradient (§2.7) plus the bottom fade to #0C1015.
  - H1: **Animated Text → Word Blur**, stagger 90ms, delay 150ms, 1200ms.
  - Underline: `tail` 3px scaleX 0→1, 1000ms `ease-expo`, delay 1250ms. Use **Highlighted Text → Regular Underline** (#EF4539, 3px) if Animated Text cannot hold the underline. In that case the H1 uses Highlighted Text inside a column with *Slight Fade In From Bottom*.
  - Lead and CTA: Column *Fade In From Bottom*, delays 700 and 850ms.
  - Board: Inner Row Backdrop Filter Blur 18px, *Fade In From Right*, delay 1000ms. Row hover draws a red left bar (scaleY 0→1, 450ms) and lifts the background to `.05`.
  - Scroll (desktop): copy Column **Scroll Position Advanced** translateY 0 → −110px plus opacity fade (custom); board translateY 0 → −40px.
  - Hero video pause button.

**S2 · Apie SGP + milestones**
- **Purpose:** trust in one sentence, plus the numbers that are allowed.
- **Layout:** In Container; 3/12 eyebrow, 9/12 statement; lane rule; 4-column stats.
- **Content:**
  - „„SGP“ – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu **Lietuva – Ispanija – Lietuva**, **Lietuva – Airija – Lietuva** ir kitas Europos šalis (**Vokietiją, Prancūziją**).“ The routes are in headlight and the rest in `fog-400`;
  - link „Skaityti daugiau“ → /apie-imone/;
  - stats: **2** Kryptys („Airija ir Ispanija – į abi puses“ *(N)*) · **11** Paslaugos („Nuo siuntinio iki perkraustymo“ *(N)*) · **3–4** Paros kelyje („Skaičiuojant nuo paėmimo dienos“) · **4** Šalys pakeliui („Lenkija, Vokietija, Belgija, Prancūzija“).
- **FX:**
  - Statement: *Fade In From Bottom*, 1200ms.
  - Lane: Divider draws, 1400ms `ease-expo`.
  - **Milestone Count To Value** (the „3–4“ one uses Motion Blur Slide In), delays 0/150/300/450.
- **Salient:** Text Block (class `sgp-statement`), Divider `sgp-lane`, Milestone ×4 with Column Borders plus `sgp-lane-v`.

**S3 · Ką vežame (the depot)**
- **Purpose:** all 11 services, browsable, with the richest hover.
- **Layout:** head row (eyebrow, H2 „Ką vežame“ *(N)*, lead „11 paslaugų – nuo vieno siuntinio iki viso namų turinio.“ *(N)*, counter `01 / 11`, progress lane, „Visos paslaugos“), then the card track.
- **Card order and copy** (summaries are verbatim or derived and listed in §8):

| # | Title | Summary | Chips | Media |
|---|---|---|---|---|
| 01 | Keleivių pervežimas | Atlenkiamos ir šildomos sėdynės, kondicionierius. Kelionės metu keleiviai apdrausti. | 3–4 paros · Nuo durų iki durų | 36377055 |
| 02 | Siuntų pervežimas | „Skubios siuntos pasieks gavėją labai operatyviai.“ | Skubios siuntos · Nuo durų iki durų | 6170458 |
| 03 | Siuntų pristatymas | „Siuntiniai paimami iš siuntėjų ir atiduodami gavėjams į rankas.“ | Į rankas · 3–4 paros | 13456097 |
| 04 | Automobilių pervežimas | Įsigijote automobilį svečioje šalyje? Pargabensime jį traliuku. | Traliuku · 3–4 paros | 29566910 + hover video 34371915 |
| 05 | Motociklų pervežimas | „Iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos ir Airijos.“ | 3–4 paros · Nuo durų iki durų | 4858429 + hover video 34308329 |
| 06 | Gyvūnų pervežimas | „Saugiai ir patogiai perkraustysime Jūsų augintinį į kitą šalį Europoje.“ | Narvai – mūsų · Individuali kaina | 32872983 |
| 07 | Perkraustymo paslaugos | Persikeliate gyventi į kitą šalį? Baldus ir daiktus pervešime nuo durų iki durų. | 3–4 paros · Nuo durų iki durų | 7464393 |
| 08 | Daiktų pervežimas | Langai, žoliapjovės, buitinė įranga – didesni ir mažesni daiktai. | 3–4 paros · Nuo durų iki durų | 36933446 |
| 09 | Krovinių pervežimas | „Visi mūsų gabenami kroviniai kelionės metu yra apdrausti.“ | Apdrausti · Nuo durų iki durų | 38927007 |
| 10 | Dalinių krovinių gabenimas | Dalijatės vieta transporte su kitais klientais – mokate mažiau. | Mokate mažiau · Nuo durų iki durų | 29786116 |
| 11 | Negabaritinių krovinių pervežimas | Didesni nei leidžiami matmenys – su specialiais leidimais ir išankstiniu planavimu. | Su leidimais · Iš anksto planuojama | 35332902 + hover video 19552565 |

- **FX:**
  - **Pinned horizontal scroll:** vertical scroll maps to translateX; the section height is `100vh + track overflow`; the counter and progress lane follow.
  - Card hover as in §4.4.
- **Salient:**
  - **Sticky Content Sections → Horizontal Scrolling** (desktop ≥1000, section width ~30vw, effect None, Subtract Navigation Height). Each child holds a Fancy Box (Parallax Hover) with class `sgp-card`.
  - **≤999 and reduced motion:** hide it and show a duplicate row, **Carousel → Flickity** (columns: phone 1.15, tablet 2.2; Touch & Total indicator; Mask Edges off), through device visibility and the CSS in §9.

**S4 · Artimiausi pervežimai + Siuntos sekimas (Day)**
- **Purpose:** the practical core: dates, booking by phone, tracking.
- **Layout:** head, then a grid of rows (1fr) and the tracking card (380px). The footnote sits under the rows.
- **Content:**
  - H2 „Artimiausi pervežimai“;
  - lead *(N)* „Rezervuokite vietą ar siuntos paėmimą paskambinę pagal kryptį.“;
  - 4 rows. The phone is LT for outbound routes and the destination number for inbound: IE +353 86 450 3104, ES +34 602 547 929;
  - tracking card: sign „Siuntos sekimas“, H4 *(N)* „Jau išsiuntėte?“, text *(N)* „Įveskite siuntos kodą ir pamatysite, kur ji dabar.“, field placeholder „Siuntos kodas...“, button „Siuntos lokacija“, error „Neįvestas siuntos kodas!“;
  - footnote *(N)* „Kelionė trunka apie 3–4 paras nuo paėmimo dienos. Taisyklių 3.4 p.: siunta pristatoma per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.“
- **FX:**
  - Row **Color Change Section** → #E8ECEF (800ms `ease-io`).
  - Rows: *Fade In From Bottom* as a group.
  - Row hover **flips to night** (§3.3).
  - Earliest departure (ES→LT Rugsėjo 27 d.) has the pulsing dot.
- **Salient:**
  - GS „Artimiausi pervežimai“ (Horizontal List Item ×4, *Bottom Border, Color Hover Effect*, hover #0C1015).
  - Tracking: Raw HTML `<form action="https://siuntos.sgp-pervezimai.lt/sekimas.php" method="get" target="_blank">` with hidden `embed=1` and `kodas`, or better, submit to `/siuntos-sekimas/?kodas=…`, which loads the iframe prefilled.

**S5 · Dvi kryptys (Night)**
- **Purpose:** explain both corridors and give the direction phones.
- **Layout:** head (H2 *(N)* „Dvi kryptys. Keturios šalys pakeliui.“); then 5/12 scrolling blocks with a 7/12 sticky media frame.
- **Blocks:**
  1. **Kryptis 01 · „Lietuva ⇄ Airija“:** „Vežame keleivius, gabename siuntas ir automobilius iš Lietuvos į Airiją ir atgal.“ (from „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais: … iš Lietuvos į Airiją ir atgal“). Phones LT/IE/UK. Dates: Iš Lietuvos „Spalio 9, 23 d.“; Į Lietuvą „Rugsėjo 28 · Spalio 15, 28 d.“. Media: **video 19274366** (ferry wake, SD 2.2 MB) with poster.
  2. **Kryptis 02 · „Lietuva ⇄ Ispanija“:** the same sentence with Ispaniją. Phones LT/ES. Dates: Rugsėjo 27 · Spalio 14, 28. Media: **27868340** (Madrid highway at dusk).
  3. **Pakeliui · „Lenkija, Vokietija, Belgija, Prancūzija“:** „Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija, todėl nedvejokite, jei norite perduoti siuntą jose gyvenantiems artimiesiems, draugams ar verslo partneriams, taip pat jei norite šias šalis aplankyti ir patys.“ Media: **1225126** (light trails, Germany).
- **FX:**
  - Media swap: crossfade plus scale 1.08→1.
  - Schematic states `ie` / `es` / `transit` draw in (§4.5).
  - Inactive text blocks at 32% opacity.
  - Mono caption with a live dot.
- **Salient:** **Sticky Content Sections → Sticky Media, Scrolling Content** (media 55%, 76vh, alignment right); schematic as Raw HTML SVG or Lottie *Scroll Position Seek*. **≤999:** media stacks above each block (native Salient behaviour), and the schematic follows block 3.

**S6 · „Du namai, vienas kelias tarp jų.“ (Night → dawn)**
- **Purpose:** the emotional beat for the diaspora and the chapter hinge.
- **Layout:** H2 with inline media, then a full-bleed panel with a caption.
- **Content:**
  - eyebrow „Kelionė“ *(N)*;
  - H2 *(N)* „Du namai [11479826 Vilnius winter evening] [2881400 Dublin at night], vienas kelias [video 13707149 SD, headlights in fog] tarp jų.“. On desktop the line breaks after the comma;
  - panel caption: sign „Apie mus“, verbatim „Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.“, link „Skaityti daugiau“;
  - stamp (mono, decorative) `LT → … → IE / ES`.
- **Media:** panel **video 12421166** (a truck on a winding road in foggy sunrise, HD 2.6 MB). Sunrise is deliberate: the night ends here and the next chapter is Day.
- **FX:**
  - Inline windows: **Circle Mask Reveal**, 1100ms `ease-expo`, stagger 150ms.
  - Panel: **clip-path inset** from `9% 11%` (2.39:1 cinemascope with 6px radius) to 0 as it enters. Scrub between viewport bottom and 15% from the top; media scale 1.14 → 1.
  - Layered depth: caption Move Y +0.06, stamp −0.08.
- **Salient:**
  - **Text With Inline Media** (2 images + 1 MP4, Circle Mask Reveal, roundness 4, inherit H2).
  - Row Full Width with Video Background plus **Background Layer Animation → Clip Path Inset → Scroll Position** (applies to the background), Parallax Subtle, Min Height 42vw (phone: aspect 4/5 via min height 110vw).
  - Caption Column Scroll Position Animation, Move Y intensity 2.

**S7 · Nuo durų iki durų (Day)**
- **Purpose:** how it works, in four honest steps.
- **Layout:** left 5/12 **sticky** caption (H2 „Nuo durų iki durų“, verbatim phrase); right 7/12 vertical lane timeline with 4 waypoints. Each waypoint has a tail-dot marker on the line, a mono number, an H4, text, and a 240×150 thumbnail.
- **Steps** (*N*, each derived from source facts):
  1. „Paskambinkite pagal kryptį“ – „Airijos ir Ispanijos kryptys turi atskirus telefonus.“ Thumbnail 6169133.
  2. „Suderinkite paėmimą“ – „Paimame iš Jums patogios vietos.“ (from „keleiviai paimami iš jiems patogios vietos“). Thumbnail 6720534.
  3. „Kelyje apie 3–4 paras“ – „Vairuotojai visada laikosi privalomo darbo ir poilsio režimo.“ Thumbnail 7541981.
  4. „Pristatome į rankas“ – „Gavėjas turi laukti sutartu laiku – pakartotinis atvykimas apmokestinamas papildomai.“ Thumbnail 13456097.
- **FX:**
  - Row Color Change → #E8ECEF.
  - Vertical red lane line **draws with scroll** (CSS `animation-timeline: view()`, fallback: static).
  - Waypoints: Column *Fade In From Right*, stagger 150ms. The marker dot lights up when the step crosses the viewport centre.
  - Thumbnails: Inner Column **Mask Reveal** (Straight, from left, 900ms) plus Image hover **Zoom In Crop**.
- **Salient:** Column **Sticky Content** (CSS, Top, offset 120px); Inner Rows with Column Borders (left); Image with Mask Reveal; class `sgp-lane-v`.

**S8 · Prieš siųsdami – patikrinkite (Day)**
- **Purpose:** clarity on what is allowed, which heads off problems before they happen.
- **Layout:** 7/12 prohibited chip grid, 5/12 callout with packing plus links.
- **Content:**
  - H2 *(N)* „Prieš siųsdami – patikrinkite“;
  - sign „Nepriimame“ followed by the chips from rules 4.2: „tabako gaminiai · alkoholiniai gėrimai · pinigai ir vertybiniai popieriai · taurieji metalai · juvelyriniai gaminiai · vaistai ir maisto papildai · ginklai · meno kūriniai ir antikvariniai daiktai · cheminiai kroviniai ir degios prekės · greitai gendantys maisto produktai“;
  - callout: `Taisyklių 4.5 p.` · **1200 EUR** · „bauda už kiekvieną rastą draudžiamą daiktą“ *(N, summary of 4.5)*;
  - packing (verbatim, from krovinių pervežimas): „naujos, standžios, nepažeistos dėžės“ · „užpildas tuščioms ertmėms“ · „lipni juosta per visą perimetrą“ · „adresas matomoje vietoje“;
  - buttons: „Visos taisyklės“ (Ink/Arrow) and „Sutartis su siuntėju (PDF, 72 KB)“ (See Through with a download icon).
- **FX:**
  - Chips: Fancy Unordered List with staggered entrance, 60ms.
  - Callout: Milestone **Motion Blur Slide In**.
  - PDF card hover: lane draws.
- **Salient:** Fancy Unordered List; Column border 1px `#B8281D`; Milestone; Button ×2.

**S9 · Keleiviams (Night)**
- **Purpose:** the passenger service is a Google Ads landing theme, so it gets a comfort showcase.
- **Layout:** 7/12 **Image With Hotspots** on the interior; 5/12 five principle rows.
- **Content:**
  - H2 *(N)* „Keleiviams – patogiai dieną ir naktį“, from „patogiai Jūsų kelionei tiek dieną, tiek naktį“;
  - hotspots *(N, derived)*:
    1. „Atlenkiamos sėdynės – patogu ir dieną, ir naktį“
    2. „Šildomos sėdynės – šilta ir žiemą“
    3. „Oro kondicionierius – vėsu ir vasarą“
    4. „Kelionės metu visi keleiviai yra apdrausti.“ (verbatim)
  - principles (verbatim headings): **Saugumas · Operatyvumas · Profesionalumas · Komfortas · Patogumas**, each with a one-line excerpt from the keleivių page (without „2017–2018“ and without „DVD“);
  - link → /…/keleiviu-pervezimas/.
- **Media:** 36377055 (black leather minibus interior).
- **FX:**
  - Color Change → #0C1015.
  - Image: Scroll movement Move Y intensity −2.
  - Hotspots: plus-sign markers in `tail` with a pulse, tooltip on hover (tap on touch).
  - Rows: Horizontal List Item **Border Animation** (the rule draws in).
- **Salient:** Image With Hotspots (plus-sign markers, tooltip on hover, colour #EF4539); Horizontal List Item ×5.

**S10 · Atsiliepimai (placeholder)**
- **Layout:** the dashed placeholder box (§4.12), clearly labelled as a placeholder.
- **Salient:** Row with Column border dashed. Swap it for Testimonial Slider → Multiple Visible Minimal once the client supplies real reviews, for example exported Google reviews with names and dates.

**S11 · Užklausa (Night)**
- **Content** (§4.8):
  - H2 *(N)* „Paskambinkite pagal kryptį“;
  - lead „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“;
  - group „Pervežimai į Airiją“: LT +370 650 53161, IE +353 86 450 3104, UK +44 7566 878681;
  - group „Pervežimai į Ispaniją“: LT +370 638 28919, ES +34 602 547 929;
  - „El. paštas: saugiai.greitai.patikimai@gmail.com“ with „Kopijuoti“ *(N)*;
  - form „Susisiekite“: „Jūsų vardas“ · „Telefono numeris“ · „El. pašto adresas“ · „Kas Jus domina?“ (a select of the 11 services plus „Kita“ *(N)*) · „Žinutė“ (placeholder *(N)* „Iš kur, į kur ir kada?“, minimum 20 characters);
  - „Formoje pateikti duomenys naudojami susisiekimui su klientu“ · button „Gauti pasiūlymą“.
- **Media:** 7024783 (red tail-light bokeh).
- **FX:**
  - Background Parallax Medium.
  - Groups: *Fade In From Bottom*, delays 200/280ms.
  - Phone row hover slides 10px and reveals „Skambinti →“.
  - Footer Reveal below.
- **Salient:** GS „Užklausa“.

Then the Footer (§4.10) and the mobile call bar.

### 5.2 /apie-imone/ · Apie įmonę

1. **Tunnel hero** (62svh):
   - H1 „Apie įmonę“;
   - lead „„SGP“ – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu Lietuva – Ispanija – Lietuva, Lietuva – Airija – Lietuva ir kitas Europos šalis (Vokietiją, Prancūziją).“;
   - breadcrumb Pradžia / Apie įmonę;
   - media **7541981** (driver in the cab at night), Parallax Subtle;
   - FX: Word Blur H1; Slight Zoom Out Reveal.
2. **Editorial (Night):**
   - left sticky: H2 „Saugiai greitai patikimai“ (the page's H3) and „SGP – visos pervežimo paslaugos“;
   - right: „Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.“ and „Mes visada pasiruošę teikti kokybiškas transporto paslaugas už Jums prieinamą kainą!“, followed by **Cascading Images**: three layers, 21041157 / 6720534 / 31570314, offsets ±40px, rotation 0, **parallax between layers**, Grow In Reveal stagger 150ms;
   - Salient: Column Sticky Content (CSS, Top) plus Cascading Images.
3. **Penki principai (Day):**
   - Horizontal List Item ×5 (Border Animation): mono index | principle name | one verbatim sentence from the keleivių page (Saugumas: „itin preciziškai rūpinamės savo mikroautobusais“ · Operatyvumas: „Maršrutui renkamės tik geriausius kelius“ · Profesionalumas: „Mūsų komandoje – tik patyrę ir atsakingi vairuotojai“ · Komfortas: „Patogiai jausitės keliaudami bet kuriuo metų laiku.“ · Patogumas: „keleiviai paimami iš jiems patogios vietos ir pristatomi į jų kelionės tikslą“);
   - Color Change #E8ECEF.
4. **Milestones (Night):** the same four as home S2.
5. **Gallery:**
   - Image Gallery → **Flickity** with image parallax, Mask Edges, fancyBox lightbox, 3 visible desktop and 1.2 on phones;
   - **use the client's own 5 photos** from the current iGallery #39 (real vehicles build more trust than stock). Placeholders: 2449454, 8858566, 21041157, 6720534, 31570314.
6. **GS Paslaugų tinklelis** (compact 6-card Flickity with „Visos paslaugos“) → **GS Užklausa**.

### 5.3 /pervezimo-paslaugos/ · Pervežimo paslaugos (overview)

1. **Tunnel hero:**
   - H1 „Pervežimo paslaugos“;
   - lead „Mūsų paslaugų sąraše: automobilių, gyvūnų, daiktų ir krovinių gabenimas bei keleivių pervežimo paslaugos.“;
   - media **36383706** (highway at dusk with snow);
   - right glass card: GS mini board.
2. **Services by group (Night):**
   - four groups, each a left **sticky sign label** (Column Sticky Content) with its cards on the right (the §4.4 card in grid mode: 3 columns desktop, 2 tablet, 1 phone):
     - „Žmonės ir augintiniai“ *(N)*: Keleiviai, Gyvūnai;
     - „Siuntos ir daiktai“ *(N)*: Siuntų pervežimas, Siuntų pristatymas, Daiktų pervežimas, Perkraustymas;
     - „Transporto priemonės“ *(N)*: Automobiliai, Motociklai;
     - „Kroviniai“ *(N)*: Krovinių, Dalinių, Negabaritinių;
   - FX: cards *Fade In From Bottom*, stagger 120ms; hover as in §4.4, without the tilt when the grid is 3 columns (use Description on Hover to save motion budget).
3. **Kryptys ir trukmė (Day):**
   - three fact tiles: „Kryptys: į / iš Airiją, Ispaniją, Vokietiją, Prancūziją“ · „Trukmė: apie 3–4 paras, skaičiuojant nuo paėmimo dienos“ · „Mikroautobusai: techniškai tvarkingi, patogūs“ (verbatim words, re-cut);
   - then H2 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ with the verbatim paragraph („Komandoje turime subūrę savo srities profesionalus…“) beside Image 31570314 (Mask Reveal Straight, Scroll Move Y 1).
4. **Two portal tiles:** „Tarptautiniai pervežimai“ (bg 1225126) and „Siuntos sekimas“ (bg 8858566), each 50% wide and 60vh high, Fancy Box → **Parallax Hover Effect** with the lane drawing on hover.
5. **GS Artimiausi pervežimai** → **GS Užklausa**.

### 5.4 /pervezimo-paslaugos/tarptautiniai-pervezimai/ · Tarptautiniai pervežimai (routes)

1. **Hero (70svh):**
   - **video 4685871** (forest highway, graded to dusk; HD 3.8 MB, SD on tablet, poster on phone);
   - H1 „Tarptautiniai pervežimai“;
   - lead „SGP pervežimai – komanda savo srities profesionalų, turinčių vieningą tikslą – užtikrinti, kad siuntiniai ir keleiviai į Ispaniją ir Airiją keliautų saugiai, greitai, patikimai ir komfortiškai.“;
   - FX: Parallax Subtle, Word Blur.
2. **Maršrutų schema (Night):**
   - H2 „Tarptautiniai pervežimai Europoje – tai mūsų veiklos pagrindas.“, sub „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais“;
   - the full-width schematic (the §4.5 SVG at 100% width) with **Image With Hotspots**: numbered markers on PL, DE, BE, FR; the tooltip *(N)* reads „Tranzito šalis – galite perduoti siuntą čia gyvenantiems artimiesiems.“;
   - FX: Lottie Scroll Position Seek draws LT→ES and LT→IE as the row passes.
3. **Dvi kryptys:**
   - Tabs → **Toggle Button** style („Airija“ | „Ispanija“);
   - each tab: media on the left (Airija **video 2386447**, Irish cliffs, SD 3.3 MB; Ispanija **27868340**), and on the right the phones, GS mini board filtered to the direction, and a CTA;
   - tab change animation: fade 400ms.
4. **„Kodėl verta pasitikėti mumis?“:**
   - left: sticky **Cascading Images** (27383867 / 36377055 / 31570314, parallax);
   - right: Fancy Unordered List with lane-dot bullets holding the 9 verbatim bullets. Two edits need approval: drop „DVD“ and replace „naujausiais“ with „techniškai tvarkingais“ (§7).
5. **„Krovinių pervežimas tarptautiniais maršrutais: ko negalima siųsti?“ (Day):**
   - the verbatim list of 8 as a ✕ chip grid;
   - callouts „Už siuntinio turinį atsakingas siuntėjas.“ and „Už valstybinių institucijų konfiskuotas siuntas mes atsakomybės neprisiimame.“.
6. **„Tarptautiniai pervežimai: ką dar turite žinoti?“ (Day):**
   - 4 info cards from the four verbatim paragraphs, with icons clock, box, map-pin and crane:
     - „apie 3–4 paras nuo paėmimo datos“;
     - pakavimas – siuntėjo atsakomybė;
     - tikslūs adresai, and „pakartotinis mūsų atvykimas apmokestinamas“;
     - iškrovimu turi pasirūpinti siuntos gavėjas;
   - Salient: Column background hover colour #FFFFFF plus a 1px border; Icon element; *Fade In From Bottom*, stagger 120ms.
7. **GS Paslaugų tinklelis** (11) → **GS Artimiausi pervežimai** → **GS Užklausa**.

### 5.5 Service detail template (×11)

Build the page once as a WPBakery template („SGP – paslauga“) and fill it per page. Shared blocks are Global Sections.

| # | Section | Layout / content rule | FX | Salient |
|---|---|---|---|---|
| T1 | **Tunnel hero** (70svh) | H1 = service name · lead = the verbatim „Santrauka“ · breadcrumb `Pradžia / Pervežimo paslaugos / Tarptautiniai pervežimai / <name>` · right glass card with the direction phones plus the mini board | Parallax Subtle · Slight Zoom Out Reveal · Word Blur H1 · content Scroll Adv. Y 0→−60 | Row + Animated Text + GS mini |
| T2 | **Faktai** strip | 3–4 fact tiles (sign label + value) from „Savybės / sąlygos“; numbers use Milestone | Fade In From Bottom, stagger 120 | Inner Row, 4 columns, Column Borders `sgp-lane-v` |
| T3 | **Įžanga** | First verbatim paragraph (68ch) plus the secondary image with Mask Reveal (Straight, left) and Scroll Move Y 1 | — | Text Block + Image |
| T4 | **„Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“** | Left: sticky H2. Right: verbatim paragraphs | Column Sticky Content | — |
| T5 | **Service-specific block** | See the table below | — | — |
| T6 | **„Kliento atsakomybės: ką reikia žinoti?“ (Day)** | 2×2 checklist cards (Pakavimas / Draudžiami daiktai / Gavėjas sutartu laiku / Iškrovimas) from the verbatim text; long text sits in Toggle Panels (Minimal Shadow) | Color Change #E8ECEF | Toggle Panels / Columns |
| T7 | **Uždarymo sakinys (Night)** | The verbatim closing line („… su „SGP pervežimai“ – …“) at H2 size, with Highlighted Text *Regular Underline* on 2 words; background texture 9807331 at 18% | Parallax Subtle | Highlighted Text |
| T8 | **Kryptys** chips | The service's child-page names (for example „Krovinių pervežimas į Airiją“) as chips linking to `#uzklausa?domina=<name>`. Fluent Forms pre-fills „Kas Jus domina?“ from `{get.domina}`. The live child URLs get 301s (§7) | Chip hover: border red | Button (Underline) ×n |
| T9 | **Susijusios paslaugos** | 3 cards (§4.4) | Stagger 150 | GS Paslaugų tinklelis subset |
| T10 | GS Artimiausi pervežimai → GS Užklausa | — | — | — |

**Per-service mapping.** Hero media is listed first and the secondary image second. Facts are verbatim or derived from `turinys-paslaugos.md`.

| Slug | Hero media / secondary | T2 facts | T5 special block |
|---|---|---|---|
| `kroviniu-pervezimas` | 38927007 / 31570314 | Nuo durų iki durų · Kroviniai apdrausti · Airija, Ispanija, Vokietija, Prancūzija · Iškrauname be specialios technikos | **„Esminės krovinių pakavimo taisyklės“**: the 4 verbatim rules as a numbered lane list, plus the prohibited-items chips and „Šis sąrašas nėra baigtinis.“ |
| `negabaritiniu-kroviniu-pervezimas` | **video 19552565** (poster) / 35332902, 38095094 | Specialūs leidimai · Išankstinis planavimas · Nuo durų iki durų · Lietuva, Prancūzija, Ispanija, Airija | **Definition callout:** „Negabaritiniai kroviniai yra tokie kroviniai, kurių matmenys yra didesni negu didžiausi leidžiami tose šalyse, per kurias tie kroviniai keliauja.“ Plus the note: special unloading equipment is „kliento atsakomybė“ |
| `daliniu-kroviniu-gabenimas` | 29786116 / 34585120, 12418936 | Mokate mažiau · Nuo durų iki durų · Vokietija, Prancūzija, Ispanija, Airija | **„Kaip veikia dalinis krovinys“**: an SVG van split into 3 shares, with the verbatim definition („kuris neužima visos transporto priemonėje kroviniams skirtos erdvės…“) |
| `daiktu-pervezimas` | 36933446 / 9185835 | Apie 3–4 paros · Nuo durų iki durų · Be perdavimo keliems vežėjams | Example chips: „Langai · Žoliapjovės · Buitinė įranga“, plus packing guidance |
| `automobiliu-pervezimas` | **video 34371915** (B/W, heavy overlay) / 29566910, 1606957, 35531295 | Gabename traliuku · Apie 3–4 paros · Vokietija, Airija, Ispanija, Lietuva | **„Traliuku“ media block:** Self Hosted Video (autoplay in view, muted) plus „Automobilis pristatomas sutartu laiku į nurodytą paėmimo vietą. Jei gavėjo nerandame, pakartotinis atvažiavimas apmokestinamas papildomai.“ |
| `motociklu-pervezimas` | **video 34308329** / 2177200, 4858429 | 3–4 paros · Nuo durų iki durų · Iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos, Airijos | Origins as mono chips, plus the video block (motorcycle loaded onto the trailer) |
| `keleiviu-pervezimas` | 36377055 / 27383867, 160483 | 3–4 paros · Nuo durų iki durų · Keleiviai apdrausti · Darbo ir poilsio režimas | **Showcase:** Image With Hotspots (as home S9), then **Sticky Content Sections → Sticky Scroll Pinned Sections → Stacking** with 5 cards (Saugumas 27383867 · Operatyvumas 36383706 · Profesionalumas 7541981 · Komfortas 36377055 · Patogumas 160483), each carrying its verbatim paragraph without „2017–2018“ and „DVD“ |
| `gyvunu-pervezimas` | 32872983 / 21767483, 3868901 | Narvus turime mes · Kaina individuali · Ispanija, Prancūzija, Vokietija, Airija · Nuo durų iki durų | **„Prieš kelionę“ checklist** (Toggle Panels → Animated Circle): paskiepyti nuo pasiutligės ~mėnesį prieš · kraujo tyrimas · veterinaro dokumentas · dokumentai ir identifikacija · „Svarbu: … vaistų nuo helmintų …“. Plus 3 price-factor tiles (narvo dydis · priežiūros sudėtingumas · atstumas) |
| `siuntu-pervezimas` | 4487517 / 6170458, 6407553 | Skubios siuntos · Nuo durų iki durų · Vokietija, Ispanija, Airija, Prancūzija | **Pakavimo gidas:** SVG box with the „5 cm“ gap, plus „Netinka: plėvelė, popierius, laikraščiai, medžiaginės pakuotės“ |
| `siuntu-pristatymas` | 13456097 (light grade) / 4440774 | Į rankas gavėjui · Apie 3–4 paros · Vokietija, Prancūzija, Ispanija, Airija | A 3-step lane: „Paimame iš siuntėjo → Kelyje apie 3–4 paras → Į rankas gavėjui“ *(N)* |
| `perkraustymo-paslaugos` | 7464393 / 4246238, 7464731 | Apie 3–4 paros · Nuo durų iki durų · Pakrovimas ir iškrovimas – kliento · Augintiniai – atskirai | **Red-outline callout:** „į kurias neįeina pakrovimo ir iškrovimo darbai“. Packing tips (5 cm, burbulinė plėvelė, trapūs po vieną). A link to Gyvūnų pervežimas |

### 5.6 /pervezimu-grafikas/ · Pervežimų grafikas

1. **Short hero (52svh):**
   - H1 „Pervežimų grafikas“;
   - lead *(N)* „Artimiausios išvykimo datos abiem kryptimis.“;
   - mono stamp „Atnaujinta: <data>“ with a live dot;
   - media **35497082** (light trails at dusk).
2. **Board (Day):**
   - GS „Artimiausi pervežimai“ at full size;
   - above it, Tabs → **Toggle Button** („Iš Lietuvos“ | „Į Lietuvą“) *(N)*, filtering through the shortcode;
   - optional derived stat „8 reisai spalį“, counted automatically, never typed in.
3. **Kaip rezervuoti:** 3-step lane *(N)*: „Paskambinkite pagal kryptį → Suderinkite paėmimo vietą → Kelionė apie 3–4 paras“.
4. **Direction phones:** the §4.8 groups, on night.
5. **Duration note:** the footnote (§7).
6. **GS Užklausa.**

This page also has to be in the **main nav**; today it is only reachable through a hero tile.

### 5.7 /siuntos-sekimas/ · Siuntos sekimas

1. **Short hero:**
   - **H1 „Siuntos sekimas“**, which fixes the live page's wrong banner „Pervežimo paslaugos“;
   - media **8858566** (yard at night in fog).
2. **Tracking panel (Day):**
   - a large field („Siuntos kodas...“) and the button „Siuntos lokacija“;
   - `<form method="get" action="https://siuntos.sgp-pervezimai.lt/sekimas.php" target="sgp-sekimas">` with hidden `embed=1`;
   - the result loads in `<iframe name="sgp-sekimas" src="…/sekimas.php?embed=1" height="520">`, framed in a 6px panel with a lane rule on top;
   - the verbatim error messages come from the iframe;
   - read `?kodas=` from the URL to pre-fill the field (small JS).
3. **Help:** *(N)* „Neradote siuntos? Paskambinkite pagal kryptį.“ plus both phone groups, plus the duration note.
4. **GS Artimiausi pervežimai** → **GS Užklausa**.

### 5.8 /taisykles/ · Siuntų siuntimo taisyklės

1. **Short hero:** H1 „Siuntų siuntimo taisyklės“; media **6169133** (waybills, „Handle with care“).
2. **Page Submenu (sticky):** 1 Tikrinimas · 2 Siuntėjo garantija · 3 Vežėjo atsakomybė · 4 Draudžiami daiktai · 5 Pretenzijos · 6 Atsakomybės ribos *(N, short labels)*.
3. **Legal text (Day):**
   - verbatim, 68ch, 17/1.65;
   - left sticky index on desktop;
   - sections are H2 („1. Siuntų tikrinimas“ …) with clause numbers in mono;
   - Salient: Column Sticky Content plus Text Blocks.
4. **Section 4 enhancements:**
   - 4.2 as a ✕ chip grid (12 items, verbatim);
   - 4.5 as a **fines table**, a derived layout of the verbatim text: Alkoholinis gėrimas – 1200 EUR / vnt. · Vaistai – 1200 EUR / vnt. (ampulė, tabletė) · Cigaretės – 1200 EUR / blokas (200 vnt.), ir už mažesnį kiekį · Tabakas – 1200 EUR / 200 g, ir už mažesnį kiekį · Kiti 4.2 p. daiktai – 1200 EUR;
   - the table sits in a red-outline callout.
5. **PDF card:** „sgp_sutartis-su-siunteju.pdf“ · PDF · 72 KB. Re-host it in WordPress media and 301 the old download URL.
6. **GS Artimiausi pervežimai** (the live page shows it too) → **GS Užklausa**.

### 5.9 /kontaktai/ · Kontaktai

1. **Hero (Night, 56svh):**
   - H1 „Kontaktai“;
   - lead „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“;
   - media **11479826** (Vilnius old town, winter evening).
2. **Two direction panels** (50/50, min 64vh, Night):
   - „Pervežimai į Airiją“ (bg **2881400**) and „Pervežimai į Ispaniją“ (bg **27868340**);
   - each shows country-coded Mono XL numbers as tap targets;
   - panel hover gives the "headlights on" grade and draws the lane;
   - Salient: Row with 2 Columns, background image plus Column background hover opacity, class `sgp-dir-panel`.
3. **Email row:** „El. paštas: saugiai.greitai.patikimai@gmail.com“ plus „Kopijuoti“.
4. **Form (Day):**
   - verbatim fields: „Jūsų vardas“, „El. pašto adresas“, „Žinutės tema“, „Žinutė“; button „Siųsti“;
   - recommend adding „Telefono numeris“, since the audience is phone-first; it exists in the live modal form;
   - microcopy „Formoje pateikti duomenys naudojami susisiekimui su klientu“.
5. **No map, address or opening hours:** they do not exist (see §8). **No GS Užklausa** on this page; footer only.

### 5.10 /privatumo-politika/ · Privatumo politika

1. **Minimal hero:** 40svh, solid night-900, H1 „Privatumo politika“, lane rule. No media.
2. **„Informacija“:** the live text is only „Informacija ruošiama...“. **Flag:** the client (or their lawyer) must supply GDPR text. The layout reserves a 68ch Day section.
3. **„Slapukai (Cookies)“:**
   - the verbatim table styled as data (cookie names in mono, 1px rules);
   - at ≤690 each row stacks into a card.
4. **Report link** (verbatim): „Norėdami pasitikrinti, kokius duomenis … – spauskite čia.“
5. **No CTA.** 301 from `/privatumo-politika/policies`.

### 5.11 404

- **Layout:** full height, Night.
- **Media:** **video 13707149** (headlights in fog; SD 0.4 MB) under a heavy overlay; poster on phones.
- **Content:**
  - H1 *(N)* „Šio kelio žemėlapyje nėra.“;
  - sub *(N)* „Puslapis nerastas. Grįžkite į pradžią arba pasirinkite kryptį.“;
  - buttons „Į pradžią“ (primary), „Pervežimų grafikas“ (glass), and the two phone buttons;
  - a lane rule that **ends in a short red "dead-end" bar**, a signature variant.
- **FX:** Word Blur H1; Parallax Subtle.
- **Salient:** a Global Section with a display condition on the 404 page (verify in 18.3), or Theme Options → 404 Page settings plus a Global Section element.

---

## 6. Mobile, reduced motion, performance, accessibility

### 6.1 ≤1000px (Salient tablet ≤999)

- Nav collapses at 1240px. The fullscreen menu becomes a single column with the links at the bottom.
- **Hero:** the copy takes 12 columns and the board drops below it (8 columns on tablet, 12 on phone). The hero can grow past 100svh, and there is **no content fade on scroll** outside desktop.
- **Depot:** the horizontal pin is replaced by a Flickity/snap swipe carousel (cards 82vw on phone, 2.2 on tablet) with a live `03 / 11` counter.
- **Routes:** no sticky frame. Each block shows its own 16:10 image and the schematic follows block 3. Inactive-block dimming is off.
- **Stats** become 2×2. The CTA stacks with the form under the phones. The footer uses 2 columns.
- **Parallax:** Theme Options → *Disable Parallax Backgrounds On Mobile* **ON**. Scroll-driven column transforms are off below 1000.

### 6.2 ≤600px (Salient phone ≤690, plus the 600 tweaks)

- **Header** 64px with the red phone icon button. The **mobile call bar** (Airija / Ispanija / Grafikas) appears after 70% of the first viewport and the footer gets 84px bottom padding.
- **Background video off:** *Disable Video Backgrounds On Mobile* **ON**. Phones see graded posters, which suits an audience often on roaming data.
- Hero phone buttons sit 2-up with shorter tracking. The primary button runs full width.
- **Timetable rows stack:** code+name / arrow, then dates (wrapping), then phone. Chips stay at least 32px high.
- The break panel uses a 4:5 aspect. Forms are one column with 52px inputs, 16px font (no iOS zoom) and correct `autocomplete`/`inputmode`.
- **Entrance animations:** Theme Options → *Page Builder Element Animations On Mobile Devices* **OFF**. On phones, content is visible immediately.

### 6.3 prefers-reduced-motion

Salient has no reduced-motion switch. Add a class through Custom JS: `if (matchMedia('(prefers-reduced-motion: reduce)').matches) document.documentElement.classList.add('sgp-rm')`. Under `.sgp-rm`:
- Animated Text and column entrances render in their final state (`opacity:1; transform:none; filter:none`).
- Inline media and clip-path panels start open.
- Milestones show their final value.
- The pulsing dot is static. Card tilt and hover video are off.
- **Background videos are not loaded;** posters show instead.
- The Horizontal Scrolling row is hidden and the Flickity row is shown (CSS only).
- Color Change still happens, but instantly.
- **Smooth scroll:** verify whether Salient's Lenis honours reduced motion. If it does not, disable Smooth Scrolling for everyone; the design does not depend on it.

The tile implements all of this. Emulate "reduce" in DevTools to see it.

### 6.4 Performance budget

| Asset | Where | Size (source → target) | Loading |
|---|---|---|---|
| Hero video **29374299** | Home S1 | 1280×720 H.264 **4.9 MB** → **re-encode**: trim to a 10s loop, CRF 28, no audio → **≈2.5 MB MP4 + ≈1.8 MB WebM** | Desktop and tablet only; `preload="none"`, starts after the poster paints |
| Hero poster (LCP) | S1 | 1920w WebP **≤160 KB**, `fetchpriority="high"` plus preload | Immediate |
| Ferry **19274366** SD | S5 | 2.2 MB | On block entry; desktop only |
| Panel **12421166** HD | S6 | 2.6 MB | IntersectionObserver ±10%; paused when out of view |
| Inline **13707149** SD | S6 | 0.4 MB | On section entry |
| Hover videos 34371915 / 34308329 / 19552565 SD | S3 cards | 1.4 / 1.3 / 2.6 MB | **Only on first hover**, pointer-fine devices |
| Tarptautiniai hero **4685871** | 5.4 | 3.8 MB HD / 0.6 MB SD | SD on tablet; poster on phone |
| Airija tab **2386447** SD | 5.4 | 3.3 MB | Only when the tab is active |
| Images | All | Full-bleed 1920w ≤250 KB · half 1200w ≤140 KB · cards 900w ≤90 KB · inline 400w ≤25 KB · WebP/AVIF, srcset | Salient lazy load ON (not the hero) |
| Fonts | All | Archivo variable latin+latin-ext ≈2×70 KB · Plex Mono 400/500 latin-ext ≈4×16 KB · `font-display: swap` · preload the latin Archivo file | Self-hosted |
| JS | All | Salient core + Lenis + Flickity + **≤5 KB custom** | *Delay JavaScript Execution* ON, but exclude the files needed above the fold (Animated Text, header) |

**Targets** (Moto G-class device on 4G):
- initial transfer ≤1.5 MB excluding video, and ≤4 MB with the hero video on desktop;
- LCP ≤2.5s, CLS ≤0.05, INP ≤200ms;
- if every video on home plays, about 12 MB in total, and only on interaction or scroll.

### 6.5 Accessibility

- WCAG 2.2 AA contrast (§2.1).
- Visible focus on everything.
- Skip link „Pereiti prie turinio“ *(N)*.
- `lang="lt"`.
- **One H1 per page:** the page title. This fixes the live site's logo H1 „Pervežimas“.
- Decorative video is `aria-hidden`. **Looping hero video has a pause control**, as does any autoplaying video longer than 5 seconds.
- Schedule rows carry full `aria-label`s („Lietuva – Airija: spalio 9 ir 23 d. Skambinti +370 650 53161“).
- Forms: visible labels and error text linked with `aria-describedby`.
- Menu dialog: focus management, Esc to close.
- Tap targets at least 44px.

---

## 7. Content handling, conflicts and SEO continuity

| Issue | Handling in this direction |
|---|---|
| **Duration:** „apie 3–4 paras“ (service pages) vs Taisyklių **3.4** „per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos“ (and an old meta „2–3 paros“) | Marketing surfaces use **„apie 3–4 paras nuo paėmimo dienos“** (the typical trip). The schedule, tracking and service footnote add *(N)* „Taisyklių 3.4 p.: siunta pristatoma per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.“, which separates the typical duration from the legal commitment. The old „2–3 paros“ is never used. **The client must confirm.** |
| **Schedule dates have no year** | Stored as full dates (ACF); shown as „Spalio 9 d.“; the year appears only across a year boundary; past dates auto-hide; „Atnaujinta“ stamp. Weekdays only after the year is confirmed. |
| **„nauji (2017–2018 metų) mikroautobusai“** | The years are **never shown**. New UI copy says „techniškai tvarkingi“ (verbatim wording). Long verbatim paragraphs drop the parenthesis and should be approved. |
| **„DVD“** in the comfort lists | Omitted as outdated (approval needed). The comfort list keeps: atlenkiamos sėdynės, šildomos sėdynės, oro kondicionierius. |
| Negabaritiniai „tik naujais mikroautobusais“ | Unlikely for oversize cargo; **the vehicle claim is not shown** on that page. Ask the client. |
| Ireland route path unknown (a UK number exists) | The schematic shows no intermediate countries for IE: a trunk LT–PL–DE (geographically unavoidable), then a dashed sea segment. The client should confirm whether the route goes via the UK or France. |
| Phone formats inconsistent | Display is normalised (**+353 86 450 3104**, **+44 7566 878681**, **+34 602 547 929**). `tel:` values are unchanged. Approval needed. |
| Domain „sgppervezimai.lt“ in the copyright and rules 6.2 | The footer uses **sgp-pervezimai.lt**. Legal text 6.2 changes only with client approval. |
| Verbatim spelling errors („užtiktiname“, „sklandžia kelionę“, „šaunamiejii“ …) | Fix them in the new build and send the client a diff list (`turinys-*` Pastabos). |
| „Veiklą orientuojame į šias tris šalis“ (four are listed) | Change to „šias šalis“ (approval needed). |
| **URLs / SEO** | All sitemap URLs stay as WordPress Pages with parent slugs. 301s: `/pervezimo-paslaugos/siuntos-sekimas` → `/siuntos-sekimas/` · `/privatumo-politika/policies` → `/privatumo-politika/` · the 27 child route pages (for example `/…/kroviniu-pervezimas/kroviniu-pervezimas-i-airija`) → their parent service page (or rebuild them later from the template) · the old PDF download URL → the new media URL. Fix the canonicals (the double domain today), set **an H1 per page**, write a unique meta description per page with diacritics, strip `gclid` parameters from `og:url`, and create a new OG image (graded hero poster plus logo, 1200×630). |
| Grafikas missing from the nav | Added to the main nav, the footer and the mobile call bar. |

---

## 8. Naujas tekstas – reikia kliento patvirtinimo

New or re-cut Lithuanian copy used in this direction (the spec and the tile). Everything else is verbatim.

**Global / navigation**
1. Nav labels „Kryptys“ (for „Tarptautiniai pervežimai“) and „Grafikas“; the header button „Skambinti“; call dropdown groups „Airijos kryptis“, „Ispanijos kryptis“.
2. Mobile call bar: „Airija“, „Ispanija“, „Grafikas“ / „artimiausi“.
3. Section eyebrows „Apie SGP“, „Paslaugos“, „Grafikas“, „Kryptys“, „Kelionė“, „Užklausa“ (with mono indexes 01–06). Skip link „Pereiti prie turinio“; video control „Pauzė“ / „Tęsti“; „Kopijuoti“ (email); link „Visas grafikas“, „Visos paslaugos“, „Skambinti →“.
4. Footer: „Saugiai, greitai, patikimai. Keleivių, siuntų ir automobilių pervežimas Lietuva – Airija – Lietuva ir Lietuva – Ispanija – Lietuva.“; „© 2026 sgp-pervezimai.lt. Visos teisės saugomos.“; column „Telefonai“; slot for company requisites *(the client must provide the name, company code and address: likely required for a service website under LT law; confirm with the client)*.
5. Cookie banner: add a reject option (for example „Atsisakyti“) to the verbatim „Sutinku“ / „Plačiau“.

**Home**

6. H1 „Pervežimai tarp Lietuvos, Airijos ir Ispanijos“.
7. Hero lead „Keleiviai, siuntos, automobiliai, augintiniai ir perkraustymas – nuo durų iki durų. Kelionė trunka apie 3–4 paras nuo paėmimo dienos.“
8. Stat sub-lines „Airija ir Ispanija – į abi puses“, „Nuo siuntinio iki perkraustymo“, „Skaičiuojant nuo paėmimo dienos“; labels „Kryptys“, „Paslaugos“, „Paros kelyje“, „Šalys pakeliui“.
9. „Ką vežame“; „11 paslaugų – nuo vieno siuntinio iki viso namų turinio.“
10. Card summaries (re-cut): „Atlenkiamos ir šildomos sėdynės, kondicionierius. Kelionės metu keleiviai apdrausti.“ · „Įsigijote automobilį svečioje šalyje? Pargabensime jį traliuku.“ · „Persikeliate gyventi į kitą šalį? Baldus ir daiktus pervešime nuo durų iki durų.“ · „Langai, žoliapjovės, buitinė įranga – didesni ir mažesni daiktai.“ · „Dalijatės vieta transporte su kitais klientais – mokate mažiau.“ · „Didesni nei leidžiami matmenys – su specialiais leidimais ir išankstiniu planavimu.“; chips „Traliuku“, „Į rankas“, „Narvai – mūsų“, „Individuali kaina“, „Mokate mažiau“, „Su leidimais“, „Iš anksto planuojama“, „Skubios siuntos“, „Apdrausti“.
11. „Rezervuokite vietą ar siuntos paėmimą paskambinę pagal kryptį.“; phone labels in the schedule rows „Airijos kryptis“, „Ispanijos kryptis“, „Airijoje“, „Ispanijoje“; board range „rugs. – spal.“ and the abbreviated dates („Spal. 9 d.“).
12. Tracking: „Jau išsiuntėte?“; „Įveskite siuntos kodą ir pamatysite, kur ji dabar.“; label „Siuntos kodas“.
13. Duration footnote: „Kelionė trunka apie 3–4 paras nuo paėmimo dienos. Taisyklių 3.4 p.: siunta pristatoma per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.“
14. „Dvi kryptys. Keturios šalys pakeliui.“; „Kryptis 01 / 02“, „Pakeliui“, „Iš Lietuvos“, „Į Lietuvą“; route sentences „Vežame keleivius, gabename siuntas ir automobilius iš Lietuvos į Airiją (Ispaniją) ir atgal.“; schematic „Maršrutų schema“, legend „kelias“, „jūra“.
15. „Kelionė“ (eyebrow); **„Du namai, vienas kelias tarp jų.“**
16. „Nuo durų iki durų“ steps: „Paskambinkite pagal kryptį – Airijos ir Ispanijos kryptys turi atskirus telefonus.“ · „Suderinkite paėmimą – Paimame iš Jums patogios vietos.“ · „Kelyje apie 3–4 paras“ · „Pristatome į rankas – Gavėjas turi laukti sutartu laiku – pakartotinis atvykimas apmokestinamas papildomai.“
17. „Prieš siųsdami – patikrinkite“; „Nepriimame“; „bauda už kiekvieną rastą draudžiamą daiktą“; „Sutartis su siuntėju (PDF, 72 KB)“; „Visos taisyklės“.
18. „Keleiviams – patogiai dieną ir naktį“; hotspots „Atlenkiamos sėdynės – patogu ir dieną, ir naktį“, „Šildomos sėdynės – šilta ir žiemą“, „Oro kondicionierius – vėsu ir vasarą“.
19. Reviews placeholder: „Atsiliepimai“, „Čia bus tikri klientų atsiliepimai“, „Vieta rezervuota – laukiame kliento pateiktų atsiliepimų. Išgalvotų atsiliepimų nenaudojame.“
20. CTA: „Paskambinkite pagal kryptį“; „Užklausa“; select option „Kita“; placeholder „Iš kur, į kur ir kada?“; error „Žinutė turi būti bent 20 simbolių.“

**Inner pages**

21. Overview groups: „Žmonės ir augintiniai“, „Siuntos ir daiktai“, „Transporto priemonės“, „Kroviniai“.
22. Tarptautiniai: hotspot tooltip „Tranzito šalis – galite perduoti siuntą čia gyvenantiems artimiesiems.“; tab labels „Airija“, „Ispanija“.
23. Service template: fact labels („Trukmė“, „Pristatymas“, „Kryptys“, „Draudimas“ …) and the 3-step lane „Paimame iš siuntėjo → Kelyje apie 3–4 paras → Į rankas gavėjui“; „Kaip veikia dalinis krovinys“; „Pakavimo gidas“; „Prieš kelionę“; „Netinka: …“.
24. Grafikas: „Artimiausios išvykimo datos abiem kryptimis.“; „Atnaujinta:“; tabs „Iš Lietuvos“ / „Į Lietuvą“; „Kaip rezervuoti“ steps.
25. Siuntos sekimas: „Neradote siuntos? Paskambinkite pagal kryptį.“
26. Taisyklės sub-menu labels: „Tikrinimas“, „Siuntėjo garantija“, „Vežėjo atsakomybė“, „Draudžiami daiktai“, „Pretenzijos“, „Atsakomybės ribos“; the fines-table layout of 4.5.
27. 404: „Šio kelio žemėlapyje nėra.“; „Puslapis nerastas. Grįžkite į pradžią arba pasirinkite kryptį.“; „Į pradžią“.
28. Content edits needing approval: drop „2017–2018“ and „DVD“; „naujausiais“ → „techniškai tvarkingais“; „šias tris šalis“ → „šias šalis“; normalised phone display; spelling fixes.

---

## 9. Custom code inventory (everything that is not a native Salient option)

All code goes in Theme Options → Custom CSS / Custom JS, and hooks onto *Extra Class Names*. The total is about 4 KB of CSS and 3 KB of JS.

```css
/* 1 · Lane rule (Divider → class sgp-lane) */
.sgp-lane{height:7px;background:
  linear-gradient(rgba(242,244,241,.12),rgba(242,244,241,.12)) 0 0/100% 1px no-repeat,
  linear-gradient(rgba(242,244,241,.12),rgba(242,244,241,.12)) 0 3px/100% 1px no-repeat,
  linear-gradient(#EF4539,#EF4539) 0 6px/100% 1px no-repeat}

/* 2 · Tail-light dot */
.sgp-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#EF4539;
  box-shadow:0 0 0 3px rgba(239,69,57,.18),0 0 14px 2px rgba(239,69,57,.55)}
.sgp-dot--live{animation:sgp-tail 2.4s cubic-bezier(.65,0,.35,1) infinite}
@keyframes sgp-tail{50%{box-shadow:0 0 0 7px rgba(239,69,57,.06),0 0 24px 5px rgba(239,69,57,.75)}}

/* 3 · Route rail: header hairline = scroll progress, no JS */
#header-outer::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;
  background:linear-gradient(90deg,rgba(239,69,57,0),#EF4539);transform-origin:left;transform:scaleX(0)}
@supports (animation-timeline: scroll()){
  #header-outer::after{animation:sgp-rail linear both;animation-timeline:scroll(root)}
  @keyframes sgp-rail{to{transform:scaleX(1)}}
}

/* 4 · Service card grade + lane (Fancy Box class sgp-card; verify bg selector, e.g. .box-bg) */
.sgp-card .box-bg{filter:brightness(.58) saturate(.7) contrast(1.06);transition:filter .8s cubic-bezier(.65,0,.35,1),transform 1s cubic-bezier(.215,.61,.355,1)}
.sgp-card:hover .box-bg{filter:brightness(.84) saturate(.95);transform:scale(1.07)}
.sgp-card::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:#EF4539;
  box-shadow:0 0 18px 1px rgba(239,69,57,.8);transform:scaleX(0);transform-origin:left;transition:transform .48s cubic-bezier(.16,1,.3,1)}
.sgp-card:hover::after{transform:scaleX(1)}

/* 5 · Width axis for the three type voices */
h1,.sgp-display{font-stretch:72%} h2{font-stretch:75%} h3{font-stretch:85%} h4{font-stretch:90%}
.sgp-sign,.nectar-button .sgp-sign{font-stretch:125%;letter-spacing:.16em;text-transform:uppercase;font-size:12px;font-weight:600}
.sgp-mono,.sgp-mono *{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums}

/* 6 · Reduced motion swap for the depot */
.sgp-hscroll-alt{display:none}
@media (max-width:999px){.sgp-hscroll{display:none}.sgp-hscroll-alt{display:block}}
@media (prefers-reduced-motion:reduce){.sgp-hscroll{display:none!important}.sgp-hscroll-alt{display:block!important}}
```

```js
// 7 · Reduced-motion flag + hero video pause + card hover video (≈40 lines total)
const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (rm) document.documentElement.classList.add('sgp-rm');
document.querySelectorAll('.sgp-card[data-video]').forEach(c => {
  if (rm || !matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  let v; c.addEventListener('pointerenter', () => { if (!v) { v = Object.assign(document.createElement('video'),
    { muted: true, loop: true, playsInline: true, src: c.dataset.video }); v.className = 'sgp-card__video'; c.prepend(v); }
    v.play().catch(() => {}); c.classList.add('is-playing'); });
  c.addEventListener('pointerleave', () => { v && v.pause(); c.classList.remove('is-playing'); });
});
// Hero pause button: toggles the Salient row video (.nectar-video-wrap video); label „Pauzė“/„Tęsti“, aria-pressed.
```

Also needed:
- **8** · the schematic SVG plus a 20-line state toggle, if the dev skips Lottie;
- **9** · `[sgp_grafikas]` shortcode with ACF (§5.0), a small plugin;
- **10** · tracking-form pre-fill from `?kodas=`;
- **11** · Fluent Forms pre-fill `{get.domina}` (native Fluent feature, no code).

---

## 10. Open questions for the client

1. Can we shoot **one night of SGP's own minibus** (tail lights, loading, the driver)? The concept is designed for it, and stock has no minibus at night.
2. Confirm the **duration wording** (3–4 paros vs 5 darbo dienos) and the **Ireland route** (via the UK?).
3. Who updates the **schedule**, and how often? This decides between ACF and editing the Global Section by hand.
4. Real **reviews** (for example Google)? Until then, the placeholder stays.
5. **Company requisites** for the footer, and the **privacy policy** text.
6. Approve the new copy in §8, the phone display format and the spelling fixes.
7. Keep or retire the 27 child route pages (they currently return HTTP 200 and may carry Google Ads traffic)?
