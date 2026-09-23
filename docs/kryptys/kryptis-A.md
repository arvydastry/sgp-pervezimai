# Kryptis A — „Maršruto linija“ (Route Line)

SGP pervežimai · v2 redesign demo · build target: WordPress + Salient 18.3 (Salient Core 3.1.6, WPBakery 8.7.3)
Companion style tile: `docs/kryptys/kryptis-A.html` (real hero, header, 4 signature sections, specimen). Every section there carries a `data-salient="…"` attribute with the element/option that rebuilds it.
Sources used: `turinys-puslapiai.md`, `turinys-paslaugos.md`, `salient-elementai.md`, `media.json`. Media IDs below are Pexels IDs from `media.json` only.

---

## 1. Concept

**In three sentences.** The site is one trip from Lithuania to Ireland or Spain and back: a continuous red route line (a "lane" of one 2 px centre stroke and two 1 px side rails, drawn from the parallel lines of the SGP logo mark) runs down the left margin, draws itself as you scroll and stops at a waypoint ring for every chapter: Išvykimas (departure) → Apie mus → Paslaugos → Maršrutai → Kelionėje → Kelionės eiga → Prieš siunčiant → Siuntos sekimas → Atvykimas (arrival = contact). The information side reads like a departure hall: split-flap boards and monospaced timetables give the next departure date, the direction and the phone number to call, while the chapters in between are cinematic dusk and blue-hour road footage graded cold so the red line is the only warm thing on screen. Cartographic devices (a hairline graticule on "map paper" sections, coordinates, print crop marks, a schematic route diagram) make the company look precise and accountable rather than flashy.

**Why it fits SGP's audience.** Lithuanians in Ireland, the UK and Spain and their families at home ask three questions: *when is the next run, can I call a real person now, and what am I allowed to send?* This direction answers all three above the fold: the departure board sits in the hero, two direct-dial buttons (one per direction) sit under the headline, a sticky call bar stays on phones, and the rules get a full chapter. The route metaphor is also literal (the vans really drive LT → PL → DE → BE → FR → ES, and to IE), so the effects explain the service instead of decorating it. Condensed sign-style type fits long Lithuanian words („Negabaritinių krovinių pervežimas“) on a 390 px phone.

**How it differs from v1** (every v1 signature is replaced, not recoloured):

| v1 (banned) | v2 „Maršruto linija“ |
|---|---|
| Warm beige `#EFEDE8` + yellow `#FFC21A` | Cold asphalt `#0F1417` / map-paper `#F5F7F6` with a hairline graticule; brand red `#EF4539` is the only accent; no yellow anywhere |
| Inter Tight 800, all caps | Barlow Condensed 600 in sentence case (road-sign lineage) + Barlow + IBM Plex Mono for data; caps only in mono labels |
| Giant centred stacked „SAUGIAI / GREITAI / PATIKIMAI“ | Left-aligned H1 that is itself a route: „Lietuva ●—● Airija. / Lietuva ●—● Ispanija. / Ir atgal.“ The dashes are drawn red lines with rings. Slogan appears only in running text. |
| Hero background colour morph | Hero keeps its video; the only scroll-linked thing is the route line |
| Video card scaling up under hero | Departure board docked inside the hero (glass strip) |
| Rotating circular text badge | None. Waypoint rings with a single halo pulse when the line reaches them |
| Full-width service rows + cursor-following image | Horizontal pinned "route": 11 service cards hanging from a red line, the line fills as you travel (Sticky Content Sections → Horizontal Scrolling) |
| Word-by-word lit "about" statement on black | About on light map paper; route names underlined by a drawn red line; odometer stats |
| Two tall parallax route cards | Schematic route map on a graticule + Airija / Ispanija toggle + timetable panel |
| Outlined/solid giant marquee | No marquees on desktop. The only ticker is a 34 px mono departures strip in the header |
| Four white step cards | D0 → D3–4 timetable line (stations on the line, not cards) |
| Yellow rounded CTA + pill checkboxes | "Arrival" terminus with two ticket-stub contact cards (perforation + notches) and boxed mono-label fields |
| Giant footer wordmark | Footer with the 11 services drawn as a line of stops; no wordmark |
| Pills (99px radius), rounded 22px cards | 2 px radii, hairlines, square icon cells |

---

## 2. Design tokens

### 2.1 Colour

| Token | Hex | Role | Contrast (WCAG 2.2) |
|---|---|---|---|
| `asphalt-950` | `#0B0E10` | Footer, off-canvas menu, ticker, mobile call bar | Snow 18.5:1 |
| `asphalt-900` | `#0F1417` | Default dark surface: hero overlay, dark sections, text on red buttons | Snow 16.8:1 · Fog 7.4:1 · Signal 4.9:1 |
| `asphalt-800` | `#161D21` | Cards, board rows, ticket body, form fields on dark | Fog 6.8:1 · Signal 4.5:1 |
| `asphalt-700` | `#222B30` | Hover surface, strong dividers on dark | Snow 13:1 |
| `asphalt-600` | `#2E383E` | Footer line-list rail, disabled borders | decorative |
| `paper-50` | `#F5F7F6` | Default light surface ("map paper"), page background | Ink 15.7:1 |
| `paper-100` | `#EAEEED` | Alternate light band (tracking, rules on light) | Ink-2 6.7:1 |
| `paper-200` | `#D9DFDE` | Light borders, map frame | decorative |
| `paper-300` | `#C3CBCB` | Planned (inactive) route on the map | decorative |
| `ink` | `#1C1D1D` | Body text and headings on light (brand near-black) | 15.7:1 on paper-50 |
| `ink-2` | `#4A5358` | Secondary text on light, mono labels | 7.3:1 on paper-50 |
| `snow` | `#F2F4F3` | Text on dark | 16.8:1 on asphalt-900 |
| `fog` | `#9AA6AB` | Secondary text on dark, mono captions | 7.4:1 on asphalt-900 |
| `signal` | `#EF4539` | Brand red. Route line, rings, primary button fill, active states, red text on dark | 4.9:1 on asphalt-900 (AA body text OK on dark) · 3.5:1 on paper-50 (large text/UI only) |
| `signal-ink` | `#C4301E` | Small red text on light (next date in timetable, link hover on light) | 5.2:1 on paper-50 |
| `signal-soft` | `rgba(239,69,57,.14)` | Halos, selection | — |
| `sea` | `#5B7C8A` | Ferry/sea segment on the map, dashed only | 4.2:1 (non-text) |
| Hairline dark | `rgba(242,244,243,.12)` | Borders on dark | — |
| Hairline light | `rgba(28,29,29,.12)` | Borders on light | — |
| Graticule | `rgba(28,29,29,.055)` | 112 px grid on paper sections | — |

Rules:
- Red is never a background for body text. The primary button is red with **asphalt-900 text** (4.9:1). White on red is 3.76:1, so it is allowed only at ≥ 19 px bold or ≥ 24 px regular.
- On light surfaces red is used for lines, rings, large numerals and 3 px underlines. Small red text on light uses `signal-ink`.
- No gradients except image overlays. No yellow, no purple, no glow.
- Salient mapping: Theme Options → Styling → Accent Color `#EF4539`; Extra Color 1 `#0F1417`; Extra Color 2 `#F5F7F6`; Extra Color 3 `#5B7C8A`; Overall background `#F5F7F6`; body text `#1C1D1D`. Row "Text Color: Light/Dark" must be set on every row, because it drives the Permanent Transparent header.

### 2.2 Typography

Google Fonts (all three include the **latin-ext** subset, so ą č ę ė į š ų ū ž and „“ render natively). Load locally through Theme Options → Typography → "Local Google Fonts".

```
https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=Barlow:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap
```

| Role | Family / weight | Size (fluid, 360 → 1440 px) | Line-height | Letter-spacing | Case |
|---|---|---|---|---|---|
| D1 hero H1 | Barlow Condensed 600 | `clamp(2.55rem, 1.2rem + 5vw, 6.25rem)` (41 → 100 px) | .94 | -0.012em | Sentence |
| D2 section H2 | Barlow Condensed 600 | `clamp(2.25rem, 1.45rem + 3vw, 4.5rem)` (36 → 72 px) | .98 | -0.008em | Sentence |
| Statement | Barlow Condensed 500 | `clamp(1.85rem, 1.2rem + 2.2vw, 3.25rem)` | 1.08 | -0.004em | Sentence |
| H3 card / panel | Barlow Condensed 600 | `clamp(1.5rem, 1.25rem + 1vw, 2.25rem)` | 1.02 | 0 | Sentence |
| Stat numeral | Barlow Condensed 500, tabular | `clamp(3.4rem, 2.4rem + 4.2vw, 7rem)` | .9 | -0.01em | — |
| Phone number (big) | Barlow Condensed 600 | `clamp(2rem, 1.5rem + 1.6vw, 2.9rem)` | 1 | .005em | — |
| Lead | Barlow 400 | `clamp(1.0625rem, 1rem + .35vw, 1.3125rem)` | 1.5 | 0 | Sentence |
| Body | Barlow 400 | 1.0625rem (17 px), 16 px ≤ 600 px | 1.62 | 0 | Sentence |
| Button | Barlow 600 | 1rem (15 px small) | 1 | .01em | Sentence |
| Nav | Barlow 500 | .9375rem | 1 | 0 | Sentence |
| Mono label | IBM Plex Mono 500 | .75rem (12 px), .6875rem in dense UI | 1.4 | .12em | UPPERCASE |
| Board / timetable | IBM Plex Mono 500 | 1–1.25rem tiles; .9375rem light timetable | 1–1.3 | .02–.06em | UPPERCASE on dark boards, sentence case on light timetables („09 spal.“) |

Rules: headings never all caps (Lithuanian caps with Ė, Ų, Ž crowd the line and long words overflow). Only mono labels, board tiles and waypoint names are uppercase. `lang="lt"` on `<html>`; `hyphens: manual` (no auto-hyphenation of Lithuanian). Minimum line-height .94 on display sizes so diacritics above caps (Ą, Ž) do not collide with the line above. Salient: Theme Options → Typography → Fluid Typography ON; Heading 1–3 = Barlow Condensed 600; Body = Barlow 400; "Italic / Label" style slots → IBM Plex Mono 500 via Extra Class `.sgp-mono`.

### 2.3 Spacing, grid

- Base unit 4 px. Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 168.
- Section padding: `clamp(88px, 10vw, 168px)` top and bottom (Row padding: desktop 168, tablet 112, phone 88).
- Gutter `--g`: `clamp(16px, 4vw, 56px)`. Container max 1320 px (Salient container max width 1320, Extended Responsive ON).
- 12-column grid, 24 px column gap (16 px ≤ 600 px).
- **Rail zone:** on ≥ 1000 px every content row has 72 px left padding (the "map margin"); the route line runs 27 px inside it. Row → Column padding-left 72 px desktop / 0 tablet & phone.
- Vertical rhythm inside sections: waypoint → 56 px → H2 → 22 px → lead → 56 px → content.

### 2.4 Radii, borders, shadows

- Radii: 0 on media; 2 px on buttons, inputs, chips, cards; 50% only on rings. No pills.
- Borders: 1 px hairlines (`rgba(242,244,243,.12)` on dark, `rgba(28,29,29,.12)` on light); 1 px solid ink for section rules (stat tops, timetable top); 1 px dashed for ticket perforation and "planned route".
- Shadows: almost none. `lift`: `0 30px 60px -28px rgba(11,14,16,.55)` (front image in the cascade, raised tickets); `panel`: `0 30px 70px -30px rgba(0,0,0,.7)` (call switchboard dropdown). Dark UI uses border colour changes, not shadows.

### 2.5 Iconography

- Line icons on a 24 px grid, 1.6 px stroke, round caps and joins, `currentColor`. Set used in the tile: phone, route, calendar, box, paw, reclining seat, heated seat, air (A/C), shield-check (insured), clock (rest regime), mail, arrow, menu, close, pause/play.
- Salient: **Icon** element with the Linea or Iconsmind line sets (closest match), colour accent, size 22 px, inside a 44 px square outlined cell (Column border 1 px). Where Iconsmind lacks a glyph (heated seat, reclining seat), upload the SVG from the style tile as an Image (SVG) — the sprite is in `kryptis-A.html`.
- Never emoji, never filled "flaticon" glyphs from the old site.

### 2.6 Image treatment

- **Grade (all photos/video):** `filter: saturate(.8) contrast(1.06) brightness(.92)`; hover/active lifts to `filter: none`. This pulls warm-dusk and bright stock shots toward the cold blue-hour set so the red line stays the only warm accent.
- **Hero overlay:** Advanced gradient: left→right `#0F1417` 86% → 55% at 42% → 10% at 78%; top→bottom 60% → 0 at 26% → 10% at 62% → 90% at 100%.
- **Cinematic rows:** top and bottom fade to `#0F1417` (0% and 100%), 30–35% in the middle, plus left 75% → 10%.
- **Texture backgrounds** (asphalt macro 4040619, wet road 9807331): duotone by overlaying `#0F1417` at 86–90%; never full strength.
- **Crop marks:** two L-shaped 14 px corner ticks (top-left, bottom-right) on framed images in light sections, 1 px ink at 55%.
- Aspect ratios fixed per slot (4:5 portrait, 16:11 cards, 16:10 panels, 16:9 cinematic) to avoid layout shift.

### 2.7 Motion tokens

| Token | Value | Use | Salient setting |
|---|---|---|---|
| `ease-route` | `cubic-bezier(.65,0,.35,1)` | Line and map drawing, H1 dashes, underline draws | easeInOutCubic (per-column custom easing) |
| `ease-arrive` | `cubic-bezier(.16,1,.3,1)` | Entrances, mask reveals, word reveals, ticket lift | Global Column/Image easing **easeOutExpo**, timing **1300 ms** |
| `ease-hover` | `cubic-bezier(.3,.7,.4,1)` | Buttons, rows, cards | Button hover colours (CSS transition 320 ms) |
| Durations | micro 160 ms · hover 320 ms · reveal 900 ms · section 1300 ms · map trunk 1000 ms + branch 900 ms | | |
| Stagger | words 60–90 ms · list rows 90 ms · cards 120 ms · flap characters 42 ms | | Column delay 0/120/240/360 |
| Entrance trigger | element top at 88% of viewport | | Salient default (Waypoints) |
| Parallax | hero 0.18 (Subtle) · cinematic 0.35 (Medium) · cascade front layer 0.14 | | Parallax Background Media On Scroll |
| Smooth scroll | Lenis 1.1.13, lerp 0.1 | | Smooth Scrolling ON, strength 50 |
| Page transition | Horizontal Gradient Wipe (asphalt), off on mobile | | View Transitions API |

---

## 3. Signature system

Five recurring elements. Together they are the brand language of v2; any new page must use at least the rail + waypoint.

1. **Kelio juosta — the route line.** 14 px wide "lane": 2 px `#EF4539` centre stroke, 1 px `rgba(239,69,57,.42)` side rails 6 px either side (the logo's parallel-line motif). Behind it a 1 px dashed ghost line (4 on / 6 off, 28% of text colour) shows the *planned* route; the red lane is the *travelled* route and scales from 0 to 1 as the section scrolls (progress = `(0.72·vh − sectionTop) / sectionHeight`). Desktop (≥ 1000 px): vertical in the left rail zone of every chapter, bends 90° into a horizontal line in the services chapter, ends in the terminus ring in "Atvykimas". Mobile: appears only locally (service list, map list, comfort list, timeline, menu, footer lists). **Build:** Raw HTML `<span class="sgp-rail"><i></i></span>` as the first element of each row (Extra Class on the row `sgp-has-rail`) + ~40 lines of custom JS (see §11). Native fallback: **Divider** element (2 px, accent, line animation "draws in") at the left of each row; or a Lottie with **Scroll Position Seek** for the one curved piece.
2. **Stotelė — the waypoint ring.** 16 px circle, 2 px red border, section-coloured fill; on reach: fills red + a single 1 px halo that scales 0.5 → 1.7 and fades in 1300 ms. It prefixes every chapter label: `● 01 · APIE MUS ———————— LT · 55,2° Š` (mono number in red, name, a hairline rule to the right edge, a meta tag on the right). Terminus variant: 22 px, 3 px border, always filled. Build: Icon/Raw HTML + custom CSS class `.sgp-wp`; the reached state is toggled by the same rail script.
3. **Išvykimų lenta — departure board & timetable.** Dark board: mono characters on split-flap tiles (`#1A2227` tile, 1 px black split line, 2 px radius). On entering the viewport each tile cycles 4–7 random characters at 55 ms and settles, staggered 42 ms left to right. Soonest departure: red tiles, red 2 px top edge on the cell, pulsing dot + „Artimiausias“. Light timetable: mono rows with a 1 px ink top rule, next date in `signal-ink` with an 8 px red dot, past dates struck through at 60%. Build: Horizontal List Item / columns for structure + `.sgp-flap` custom JS (fallback: Animated Text → Single letter from bottom: Reveal, which gives a similar mechanical cadence).
4. **Kartografinis tinklelis — map paper.** Light sections carry a 112 px hairline graticule (`rgba(28,29,29,.055)`), coordinates in mono (Lithuanian notation: „55,2° Š · 23,9° R“, „53,4° Š · 8,2° V“), crop marks on images and a "legend" style for small print. Build: Row Extra Class `.sgp-graticule` (2 lines of CSS background-image).
5. **Bilietas — the ticket stub.** Contact cards and the next-departure stub: main body + 190 px stub separated by a dashed perforation with two 11 px semicircular notches (CSS mask). Hover: lifts 4 px, perforation turns red, stub "Skambinti" link draws its underline. ≤ 600 px: stub moves under the body, perforation becomes horizontal, notches removed. Build: two columns in an Inner Row with Extra Class `.sgp-ticket` (mask CSS in §11), Column border dashed on the stub.

Plus two minor devices: the **H1 route dash** (a 1.05 em cased line with an origin ring and a filled destination ring, drawn after the words rise) and the **odometer numerals** (Milestone "Motion Blur Slide In").

**Custom code budget (total):** CSS ≈ 5 KB, JS ≈ 6 KB unminified, no dependencies (Lenis is Salient's own). Theme Options → Custom CSS / Custom JS (footer). Exclude the JS from "Delay JavaScript Execution" or initialise it on first interaction.

---

## 4. Component inventory

### 4.1 Header (Global)
- **Ticker bar** (34 px, `asphalt-950`, mono 11 px): red live dot + „Artimiausi išvykimai“, then the next departure of each direction sorted by date („Ispanija → Lietuva · 27 rugs. · po 4 d.“), right: „Visas grafikas →“. Right edge fades out. Hides once scrolled (height 34 → 0, 400 ms). Salient: Global Section in location **In Navigation Top (Before Scrolling)**; desktop static text, phone = **Scrolling Text** (Slowest, Mask Edges) showing all items.
- **Transparent state** (over hero): logo_light.svg 112 × 46, nav centred (Barlow 500 15 px, snow), right: primary button „Skambinti“ (small, 42 px, phone icon). Height 84 px.
- **Scrolled state:** 64 px, background `rgba(15,20,23,.74)` + blur 14 px + 1 px bottom hairline; over light rows `rgba(245,247,246,.84)`, ink text and logo.svg (dark). Hides on scroll down after 360 px, returns on scroll up.
- **Hover/focus:** nav links get a 2 px red underline that grows from the left (450 ms `ease-arrive`), shrinks to the right on leave; `:focus-visible` 2 px red outline, 3 px offset.
- **Call switchboard** (dropdown under „Skambinti“, 340 px, `asphalt-950`, 2 px red top): two groups „Pervežimai į Airiją“ (LT +370 650 53161, IE +353 86 450 3104, UK +44 7566 878681) and „Pervežimai į Ispaniją“ (LT +370 638 28919, ES +34 602 547 929), each row Barlow Condensed 20 px with a mono country code; hover: row text red, 6 px indent, arrow slides in. Email under the rows. Salient: menu item styled as button + **Mega Menu** built from a Global Section.
- **Mobile (< 1000 px):** logo, red 44 px phone button (opens the same switchboard as a bottom sheet) and a 44 px outlined burger. Nav hidden from 1179 px down.
- Salient: Header layout **Centered Menu**; **Header Permanent Transparent** ON; **Hide Until Needed** ON; **Resize On Scroll** 84 → 64; header BG blur ON; Header Link Hover Effect **Animated Underline** (accent); Header Navigation Entrance Animation **Fade In** 200 ms delay.

### 4.2 Off-canvas menu
Salient **Off Canvas → Fullscreen Split**. Left: the menu as a line diagram — 2 px red vertical line draws top → bottom (900 ms `ease-route`), each item is a stop with a ring, mono number („00“–„07“) and Barlow Condensed 600 at `clamp(2rem, 1.4rem + 2.6vw, 3.6rem)`; items rise 14 px with 60 ms stagger; hover: red text, 8 px nudge, ring fills. Last item „Kontaktai“ has a filled ring (terminus). Right (`asphalt-900`, Global Section content): both phone groups, email. Phone: single column, scrolls as one sheet, Lenis paused while open. Items: Pradžia · Apie mus · Pervežimo paslaugos · Tarptautiniai pervežimai · Pervežimų grafikas · Siuntos sekimas · Taisyklės · Kontaktai (the schedule page is added to the menu; it was missing on the live site).

### 4.3 Buttons
| Type | Default | Hover | Focus / active | Salient |
|---|---|---|---|---|
| **Signal** (primary) | `#EF4539` fill, `#0F1417` text, 52 px high (42 small), 2 px radius, label cell + 52 px arrow cell split by a 22% hairline | On dark: fill → snow; on light: fill → asphalt-900, text → snow; arrow exits right and re-enters from the left (550 ms) | 2 px red outline (snow outline on red fill), active: translateY(1 px) | Button → **Arrow Animation**, colours: bg accent / text Extra 1, hover bg `#F2F4F3` or Extra 1 |
| **Line** (secondary) | Transparent, 1 px border currentColor 38%, same geometry | Border → red, fill currentColor 7% | same | Button → **See Through**, hover border accent |
| **Text link** | Mono 13 px uppercase, 1 px underline at 30% | Red 2 px underline grows from the left, arrow +4 px | outline | Button → **Underline** |
| **Call button** | 64 px, `rgba(15,20,23,.55)` + blur 10 px, 1 px hairline, 64 px red icon cell, mono label („Pervežimai į Airiją“) over a Barlow Condensed 24 px number | Whole button fills red, text asphalt, icon cell turns asphalt with red icon | outline | Button Basic + custom class `.sgp-callbtn` (backdrop blur on Button is native) |
| Disabled | 40% opacity, no hover | — | — | — |

### 4.4 Service card (home, horizontal route)
Width `clamp(290px, 24vw, 368px)`, hangs from the line: ring on the line, 22 px stem, card below. Card: `asphalt-800`, 1 px hairline; image 16:11 (max 27vh), graded, inner parallax ±13 px horizontally as the track moves; body: mono „01 / 11“ (number red), H3, one-sentence summary (fog, 15 px), two mono chips, 42 px square arrow cell. **Hover:** card lifts 6 px, border → red 55%, bg `#1A2227`, image to full colour + scale 1.10 → 1.14, H3 underline draws (600 ms), arrow cell fills red, ring fills; cards 02, 05, 06 fade in a muted SD video over the photo (loaded on first hover, fine pointers only). **Reached** (line passed it): stem turns red, ring filled. **Mobile row:** 96 px thumbnail left, number with a trailing arrow, H3 24 px, summary; chips and arrow cell hidden; the whole row is the link.

### 4.5 Route card / route panel
Tab toggle „Airija IE | Ispanija ES“ (1 px ink outline, 3 px inner padding, selected = ink fill, paper text). Panel: 16:10 photo with crop marks (hover zoom 1.06 → 1.10, grade lifts), H3 „Lietuva – Airija – Lietuva“, light timetable rows (Iš Lietuvos / Iš Airijos / Kelionė), phone group with mono country codes, Signal button „Skambinti dėl Airijos“. Panel swap: fade + 14 px rise, 600 ms. Salient: **Tabs → Toggle Button** (2 tabs, content animation fade), inside each tab an Image (Mask Reveal, straight, bottom) + Horizontal List Items + Button.

### 4.6 Schedule row
- **Dark board cell:** direction label (mono, fog) + index or „● Artimiausias“, route code tiles („LT → IE“), human name („Lietuva – Airija“, verbatim H3), next date tiles („09 SPAL.“) with status („po 16 d.“), „Vėliau: 23 spal.“. Hover: cell background +3% white. Soonest: red tiles, 2 px red top edge.
- **Light timetable row:** 118 px mono key + mono values; hover: 3.5% ink tint + 8 px indent (400 ms). Salient: **Horizontal List Item** (Style: Border Animation; 2–4 columns).
- Status logic (JS, from the dates only): future → „po N d.“ / „rytoj“ / „šiandien“; soonest across all → „Artimiausias“; past → struck through / removed from the board. If every date is past → „Grafikas atnaujinamas“. No year is shown (the site gives none).

### 4.7 Data / stat block
Four cells, each with a 1 px ink top rule and a 28 × 3 px red "kilometre marker" on the left end; mono label; Barlow Condensed numeral rolling like an odometer (digits slide with a 3 px motion blur, 1600 ms); caption. Only derivable numbers: **2** kryptys, **11** paslaugų, **3–4** paros kelionėje, **4** šalys pakeliui (Lenkija, Vokietija, Belgija, Prancūzija). Salient: **Milestone** ×4, Animation Effect **Motion Blur Slide In**, delays 0/150/300/450 ms (the „3–4“ cell: Milestone "None" + Animated Text).

### 4.8 CTA band „Atvykimas“ (Global Section, before footer)
Terminus ring on the rail, H2 (verbatim) „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“, two ticket cards (7 columns), email row, form (4 columns). Ticket: mono code „LT ⇄ IE“ + „Pervežimai į Airiją“, big number with phone icon, secondary numbers in mono; stub „Kitas išvykimas iš Lietuvos“ + flap date + „Skambinti“. Hidden on /kontaktai/ and /privatumo-politika/ (display conditions), like the live site.

### 4.9 Form fields
Boxed fields on `asphalt-800` (on light pages `#FFFFFF` with ink hairline): 1 px border, 2 px radius, mono 10 px uppercase label pinned inside top-left, input text Barlow 500 16 px. Hover: border 26% snow. **Focus:** border red, a 3 px red "lane" bar grows on the left edge (scaleY, 400 ms), label turns red, field bg `#1A2227`. **Error:** red border and label, mono 11 px message under the value („Patikrinkite el. pašto adresą“), `aria-invalid`. Select uses a two-triangle chevron. Consent note verbatim: „Formoje pateikti duomenys naudojami susisiekimui su klientu“. Submit = Signal button „Gauti pasiūlymą“. Salient: **Fluent Forms** (Salient-styled) + Extra Class `.sgp-field`; reCAPTCHA/Turnstile kept.

Fields (verbatim from the live modal): „Jūsų vardas“, „El. pašto adresas“, „Telefono numeris“, „Kas Jus domina?“ (proposed as a select of the 11 services instead of free text), „Žinutė“ (min. 20 simbolių). Success/error texts verbatim: „Jūsų žinutė sėkmingai išsiųsta“, „Oi kažkas ne taip! Bandykite dar kartą.“, „Įveskite teisingą apsaugos kodą.“

### 4.10 Footer (Global Section → Footer)
`asphalt-950`, 5 columns: logo_light + one-line description; „Pervežimai į Airiją“ numbers; „Pervežimai į Ispaniją“ numbers; „Tarptautiniai pervežimai“ = the 11 services as a vertical line of stops (1 px `asphalt-600` line, 9 px rings; hover: ring fills red, link +3 px); „Informacija“ (Apie mus, Pervežimų grafikas, Siuntos sekimas, Taisyklės, Kontaktai, Privatumo politika). Bottom bar: „© 2026 SGP pervežimai. Visos teisės saugomos.“ and „↑ Į pradžią“. No wordmark. Phone: 1 column.

### 4.11 Inner page hero „Maršruto antraštė“ + breadcrumb
Row, full width, min-height 62vh desktop / 52svh phone, graded photo with **Parallax Subtle** and **Background Layer Animation → Slight Zoom Out Reveal**, overlay gradient as hero. Content bottom-left: breadcrumb as a route — „Pradžia ●— Pervežimo paslaugos ●— Tarptautiniai pervežimai ●— **Krovinių pervežimas** ● Jūs čia“ (mono 12 px; separators are 24 px line segments; last ring filled red). H1 (Barlow Condensed 600, D2 size + 10%, Animated Text **Word Reveal**, 90 ms stagger), lead (verbatim summary), fact chips. Right column (≥ 1000 px): compact call ticket (both LT numbers). Breadcrumb source: Rank Math / Yoast breadcrumb shortcode in a Text Block, Extra Class `.sgp-crumbs` (CSS turns separators into line + ring). One H1 per page (the logo no longer carries an H1).

### 4.12 Other components
- **Mobile call bar** (< 1000 px): fixed bottom, 58 px + safe area: red „Į Airiją · Skambinti“ (tel:+37065053161), dark „Į Ispaniją · Skambinti“ (tel:+37063828919), calendar icon → /pervezimu-grafikas/. Salient: Row → **Sticky Row: Bottom of Window**, device visibility tablet + phone, inside a Global Section on all pages.
- **Toggle panels** (rules, requirements): Salient **Toggle Panels → Minimal Shadow** restyled: 1 px hairline rows, mono index, "+" becomes a 12 px ring that fills when open; accordion mode; deep links.
- **Chips:** mono 11 px uppercase, 1 px hairline, 2 px radius, no fill.
- **„Kita stotelė“ (next stop) band** on service pages: full-width Column Link, mono „Kita stotelė · 02“, H2 name of the next service, arrow; background image of that service at opacity 0 → 0.35 on hover (Column BG Image + **Hover Opacity**), the lane line draws across the band on hover (custom CSS, 900 ms).
- **Testimonials placeholder:** Testimonial Slider (Minimal) with one slide reading „Čia bus tikri klientų atsiliepimai“ inside a dashed 1 px frame, row disabled until real reviews exist.
- **Cookie bar:** existing text verbatim, bottom-left ticket shape, buttons „Sutinku“ (Signal small) / „Plačiau“ (text link); plugin (Complianz / CookieYes) styled via CSS; non-essential cookies off by default.

---

## 5. Page blueprints

Legend per section: **Purpose · Layout · Content (source) · Media · Effects (trigger → values) · Salient.**
Content sources: [P] = `turinys-puslapiai.md`, [S] = `turinys-paslaugos.md`. „NEW“ = new copy listed in §10.

### 5.0 Global Sections (built once, reused)
| Global Section | Location / display | Contents |
|---|---|---|
| GS-Ticker | In Navigation Top (Before Scrolling), all pages | §4.1 ticker |
| GS-Call | Mega menu panel on „Skambinti“ + mobile bottom sheet | §4.1 switchboard |
| GS-Menu | Off-canvas content (Fullscreen Split, right side) | phones, email |
| GS-Board „Artimiausi pervežimai“ | Global Section element inside rows (home hero, schedule page, rules, service pages) | 4 routes; the only place where dates are edited |
| GS-Arrival „Atvykimas“ | Before Footer; hidden on /kontaktai/, /privatumo-politika/, 404 | §4.8 |
| GS-Footer | Footer | §4.10 |
| GS-CallBar | Sticky Row, tablet + phone, all pages | §4.12 |

Schedule editing: dates are typed into GS-Board as text in the live site's style („Spalio 9 d.“); the custom JS reads a `data-date="2026-10-09"` attribute added through the Horizontal List Item's Extra Class field or a hidden span, so status labels stay correct. (Later upgrade: ACF Options repeater → shortcode; not required for launch.)

---

### 5.1 Home `/` (the showpiece — 12 sections + header)

**S0 · Header + ticker** — see §4.1. Row Text Color of S1 = Light, so the header starts transparent with the light logo.

**S1 · Išvykimas (hero with docked departure board)**
- Purpose: in one screen, where we go, a real person to call, and the next date.
- Layout: full-height row (min 100svh). Top 70%: 8-column copy block left, coordinates legend top-right (3 cols). Bottom: glass departure board spanning the container (4 cells). Rail origin ring sits on the board's left edge; the route line starts here.
- Content: eyebrow „Tarptautiniai pervežimai mikroautobusais“ (adapted from the page title „Tarptautiniai pervežimai Europoje (mikroautobusais)“ [P]); H1 NEW „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“ (built on the verbatim routes „Lietuva – Airija – Lietuva“, „Lietuva – Ispanija – Lietuva“ [P]); lead NEW built from „Visos pervežimo paslaugos“ + „saugiai greitai patikimai“ [P] + service list; call buttons „Pervežimai į Airiją +370 650 53161“, „Pervežimai į Ispaniją +370 638 28919“ [P]; link „Visas pervežimų grafikas“. Coordinates legend: LT 55,2° Š · 23,9° R / IE 53,4° Š · 8,2° V / ES 40,2° Š · 3,6° V (country centroids, decorative). Board: H2 „Artimiausi pervežimai“ and the four routes with dates exactly as [P] („Lietuva - Airija: Spalio 09d.; 23d.“ etc.), note NEW „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu“.
- Media: video **12421166** (truck on a winding road at sunset, drone; HD 1920 2.6 MB, SD 960 0.8 MB, 8 s loop), poster from the same ID; fallback photo **11053641**. Alternative if the client wants a van rather than a truck: video **15602514** (white van, forest road; SD 3.7 MB — heavier).
- Effects:
  - Video: **Parallax Background Media On Scroll → Subtle** (≈ translateY 0.18 × scroll); overlay per §2.6.
  - H1: words rise from a mask (translateY 108% → 0), 1150 ms `ease-arrive`, 90 ms stagger, start 100 ms after load; each dash: origin ring scales in (500 ms, +550 ms), lane draws left→right (900 ms `ease-route`, +700 ms), destination ring fills (+1450 ms).
  - Lead / buttons: Fade In From Bottom 26 px, 900 ms, delays 700 / 850 ms.
  - Board: split-flap run 700 ms after load, 42 ms per character; soonest cell pulses its dot every 2.4 s.
  - Call button hover: §4.3. "Pauzė" video toggle (mono, bottom-right above the board) — required for WCAG 2.2.2.
- Salient: Row → Full Height Row (Responsive Height: svh) · Content Position Bottom · Video Background MP4 + preview image · Parallax Subtle · Color Overlay Advanced · Text Color Light. Column → Inner Row 1 (copy): Animated Text (Word Reveal, stagger) with Extra Class `.sgp-h1-route` for the dashes, Text Block, 2 × Button (`.sgp-callbtn`), Button Underline. Inner Row 2 (board): **Minimum Width 100%**, **Backdrop filter blur 16 px**, bg `rgba(11,14,16,.74)`, Global Section element GS-Board.

**S2 · 01 Apie mus** (paper + graticule, Text Color Dark)
- Purpose: who SGP is, in their own words, plus the four honest numbers.
- Layout: waypoint row; 7 cols statement + body + link | 4 cols cascading images (offset 1 col); stats row of 4.
- Content (verbatim [P]): „„SGP“ – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu Lietuva – Ispanija – Lietuva, Lietuva – Airija – Lietuva ir kitas Europos šalis (Vokietiją, Prancūziją).“ + „Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.“ + link „Skaityti daugiau“ → /apie-imone/. Stats §4.7 (NEW captions).
- Media: **7541981** (driver at night, 4:5, back layer), **6169133** (waybills on a "Handle with care" box, 4:3, front layer). Vertical mono tag „Saugiai · Greitai · Patikimai“.
- Effects: statement Fade In From Bottom; the two route names get a 3 px red underline drawn left→right 1400 ms `ease-route` (second +500 ms); images: Mask Reveal from bottom (clip-path inset 100% → 0, 1300 ms `ease-arrive`), front layer +250 ms and parallax 0.14; hover on the cascade lifts the grade and scales 1.03; stats odometer 1600 ms with 150 ms stagger; rail draws, ring pulses when it reaches „01“.
- Salient: Row bg `#F5F7F6` + Extra Class `.sgp-graticule sgp-has-rail`; **Highlighted Text → Regular Underline** (accent, 3 px); **Cascading Images** (2 layers, parallax, layer animations Grow In Reveal / Fade In From Bottom); Button Underline; **Milestone ×4 Motion Blur Slide In**.

**S3 · 02 Paslaugos — horizontal route** (dark)
- Purpose: all 11 services at a glance, as stops on one road.
- Layout (≥ 1000 px): section pinned for (11 cards + end card) of horizontal travel ≈ 3.2 viewport widths. Top: waypoint, H2 left, counter „04 / 11“ + „Slinkite →“ right. The vertical rail comes down from S2, turns 90° into a static horizontal lane at card-ring height; cards travel left under it; the red fill advances from the first ring to the right edge with scroll progress; each ring fills as the fill passes it. Left edge of the track fades out behind the rail (mask 30 → 60 px). Last cell: „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“ + Signal button.
- Content: H2 „Visos pervežimo paslaugos“ [P hero]; lead verbatim „Platus paslaugų spektras suteikia universalumo, nes savo klientams galime pasiūlyti kur kas daugiau sprendimų.“ [P]. Card titles verbatim [S]; one-line summaries condensed from each page's „Santrauka“ (NEW where condensed, §10); chips from facts in [S].

| # | Card | Summary (source) | Chips | Photo | Hover video (SD) |
|---|---|---|---|---|---|
| 01 | Krovinių pervežimas | „Į Airiją, Ispaniją, Vokietiją bei Prancūziją ir atgal – saugiai, greitai, patikimai.“ [S verbatim] | Nuo durų iki durų · Kroviniai apdrausti | 38927007 | — |
| 02 | Negabaritinių krovinių pervežimas | Condensed definition [S] | Išankstinis planavimas · Nuo durų iki durų | 35332902 | 19552565 (2.6 MB) |
| 03 | Dalinių krovinių gabenimas | „Dalinių krovinių gabenimas yra puikus būdas klientams sutaupyti.“ [S verbatim] | Mokate mažiau · Nuo durų iki durų | 29786116 | — |
| 04 | Daiktų pervežimas | „Langai, žoliapjovės, buitinė įranga…“ [S condensed] | Apie 3–4 paros · Nuo durų iki durų | 36933446 | — |
| 05 | Automobilių pervežimas | „Automobilius gabename traliuku…“ [S condensed] | Traliuku · Apie 3–4 paros | 29566910 | 34371915 (1.4 MB, b/w) |
| 06 | Motociklų pervežimas | Countries list [S] | 3–4 paros · Nuo durų iki durų | 4858429 | 34308329 (1.3 MB) |
| 07 | Keleivių pervežimas | Comfort + insurance [S condensed] | Keleiviai apdrausti · 3–4 paros | 36377055 | — |
| 08 | Gyvūnų pervežimas | „Saugiai ir patogiai perkraustysime Jūsų augintinį į kitą šalį Europoje.“ [S verbatim] | Narvus turime mes · Nuo durų iki durų | 32872983 | — |
| 09 | Siuntų pervežimas | „Skubios siuntos pasieks gavėją labai operatyviai.“ [S verbatim] | Skubios siuntos · Nuo durų iki durų | 6170458 | — |
| 10 | Siuntų pristatymas | „Siuntiniai paimami iš siuntėjų ir atiduodami gavėjams į rankas.“ [S verbatim] | Į rankas gavėjui · Apie 3–4 paros | 13456097 | — |
| 11 | Perkraustymo paslaugos | NEW question-form summary | Apie 3–4 paros · Nuo durų iki durų | 4246238 (packed boxes — not 7464393, which shows movers carrying a sofa although loading/unloading is **not** included [S]) | — |

- Effects: pin + translateX linked to scroll; card image inner parallax ±13 px; hover per §4.4; counter updates to the number of reached rings; H2 Word Reveal.
- Salient: **Sticky Content Sections → Horizontal Scrolling** (section width 26vw, effect None, Subtract Navigation Height ON, desktop only); each child section = Column Link → card (Column bg `#161D21`, hover bg `#1A2227`, border 1 px, Image with hover **Zoom In Crop**, Text, chips as Text Block, Button Arrow). Static lane + ring states: custom JS `.sgp-hroute` (reads the Salient track's transform). Mobile: Salient stacks the children → custom CSS turns them into rows (§6).

**S4 · 03 Maršrutai — map + timetable** (paper + graticule)
- Purpose: show the actual road, the transit countries, and the dates/phones per direction.
- Layout: waypoint; H2 (7 cols) | verbatim paragraph + toggle (4 cols); 7-col framed map | 4-col route panel.
- Content: H2 NEW „Dvi kryptys. Keturios šalys pakeliui.“; paragraph (verbatim, trimmed) „Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija – nedvejokite, jei norite perduoti siuntą jose gyvenantiems artimiesiems.“ [P]; map labels LIETUVA (išvykimas), LENKIJA, VOKIETIJA, BELGIJA, PRANCŪZIJA, ISPANIJA, AIRIJA, „Keltas“; panel content: dates [P], „Kelionė: apie 3–4 paros“ [P], phones [P].
- Map: inline SVG, 700 × 520 viewBox, equirectangular positions (LT 624/64 → PL 542/140 → DE 376/161 → BE 267/175; ES branch → FR 227/270 → ES 116/416; IE branch = dashed sea line BE → IE 37/111). Graticule every 5° with Lithuanian labels („10° V … 25° R“, „40° Š … 55° Š“). Cased red trunk (12 px 45% red / 9 px paper / 2.6 px red), inactive branch `paper-300`, sea segment dashed `sea` → red dashed when active. Origin ring pulses (2.6 s). Caption „Maršrutų schema · ne mastelis“. Legend: Maršrutas / Keltas / Šalis pakeliui. **The exact Ireland route (via the UK or a direct ferry from France) must be confirmed — the diagram only shows direction (§10).**
- Media: IE panel **2881400** (Dublin, night), ES panel **27868340** (Madrid highway at dusk).
- Effects: map draws when 12% in view: trunk 1000 ms `ease-route`, branch 900 ms after 850 ms; tab switch redraws; terminus fills red after the branch; panel swap fade + 14 px rise 600 ms; panel image Mask Reveal; timetable rows hover indent; rail continues.
- Salient: Row paper + `.sgp-graticule`; **Tabs → Toggle Button** (two tabs; each tab holds the panel); map = Raw HTML (inline SVG) + JS listening to the tab change; native fallback: the same SVG exported static as an **Image With Hotspots** (numbered markers on each country with tooltips, e.g. „Belgija – pakeliui“, „Airija – +353 86 450 3104“).

**S5 · 04 Kelionėje — cinematic parallax** (dark)
- Purpose: the emotional middle of the trip and the passenger comfort facts.
- Layout: 118vh row, video background; waypoint; H2 (max 17ch); horizontal line with 5 comfort stops; footnote strip with link.
- Content: H2 NEW „Kelionė trunka apie 3–4 paras. Pasirūpinsime, kad laikas neprailgtų.“ (from „trunka apie 3–4 paras“ [P] + „pasirūpinsime, kad laikas neprailgtų“ [P]); stops (verbatim [P]/[S]): „Atlenkiamos sėdynės – patogiai Jūsų kelionei tiek dieną, tiek naktį“; „Šildomos sėdynės – komfortui net žvarbiausiomis žiemos dienomis“; „Kondicionierius – kad oras autobuse visada būtų šviežias“; „Keleiviai apdrausti – Kelionės metu visi keleiviai yra apdrausti“; „Poilsio režimas – Vairuotojai visada laikosi privalomo darbo ir poilsio režimo“. (DVD is deliberately left out — outdated.) Footnote NEW wording of the 3–4 days vs 5 working days conflict (§9). Link „Keleivių pervežimas“.
- Media: video **4685871** (forest highway at dusk, drone; HD 3.8 MB, SD 0.6 MB, 27 s), poster same ID. Load within 300 px of the viewport, pause when out.
- Effects: **Parallax Medium** (≈ 0.35; ±11% of section height); BG Layer **Zoom Out Slowly**; H2 **Word Blur** (blur 10 px → 0, 70 ms stagger, 1100 ms); comfort lane draws left→right with scroll (0 → 1 over 45% of the viewport), each icon cell turns red when reached.
- Salient: Row Video BG + Parallax Medium + overlay + Text Color Light; **Animated Text → Word: Blur**; **Fancy Unordered List / Icon List** (5 items, icons, staggered entrance) with Extra Class `.sgp-stops` for the lane; Text Block (mono) + Button Underline.

**S6 · 05 Kelionės eiga — D0 → D3–4 timeline** (paper)
- Purpose: what happens after the call, in timetable language.
- Layout: waypoint; H2 NEW „Nuo skambučio iki durų“; horizontal lane with 4 stations (desktop), vertical on mobile; each station: time code in Barlow Condensed 64 px red („Prieš“, „D0“, „D1–D3“, „D3–D4“), title, text, circular thumbnail (80 px, circle mask).
- Content (verbatim fragments): Prieš — „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“ [P]; D0 Paėmimas — „Paimame krovinį iš sutartos vietos“ [S gyvūnai] + „nuo durų iki durų“; D1–D3 Kelyje — NEW „Siuntos vietą galite pasitikrinti pagal siuntos kodą.“ + link „Siuntos sekimas“ (the tracking tool is real [P]); D3–D4 Pristatymas — „…ir pristatome gavėjui į rankas.“ [S] + „Jei sutartu laiku gavėjas … negali … paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.“ [P]. Footnote (mono): „Kelionė trunka apie 3–4 paras nuo paėmimo dienos. Siuntų pristatymo įsipareigojimas pagal taisykles – per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.“ (§9).
- Media: D0 **6407553** (open van full of boxes), D1–D3 **35531295** (cars and trucks on a ferry deck), D3–D4 **4440774** (hands passing boxes).
- Effects: lane draws with scroll; stations: ring fill + time code **Single letter from bottom: Reveal**; thumbnails **Mask Reveal circle** 900 ms `cubic-bezier(.2,.8,.2,1)`; hover on a station: thumbnail scale 1 → 1.08, grade lifts.
- Salient: 4 columns (Column delay 0/120/240/360, Fade In From Bottom); **Divider** (2 px accent, line animation "draws in", delay 200 ms) as the native lane, custom CSS for the cased look; Image with **Mask → Circle** + Column **Mask Reveal (Circle)**; Animated Text for time codes.

**S7 · 06 Prieš siunčiant — rules at a glance** (dark, textured)
- Purpose: what is allowed, what is not, packing, the recipient's duty — before people call.
- Layout: 5 cols sticky title + warning callout | 7 cols toggle panels.
- Content: H2 (verbatim H5 [P]) „Krovinių pervežimas tarptautiniais maršrutais: ko negalima siųsti?“; callout verbatim „Už siuntinio turinį atsakingas siuntėjas.“; panels: „Draudžiami daiktai“ (rules 4.2 list verbatim, 12 items, two-column mono list with ✕ rings) · „Pakavimas“ (4 packing rules verbatim [S krovinių] + „rekomenduojamas tarpas yra 5 centimetrai“ [S siuntų]) · „Gavėjas ir pristatymas“ (verbatim [P] „Labai svarbu nurodyti tikslius siuntinio paėmimo ir pristatymo adresus…“, „…iškrovimu turi pasirūpinti siuntos gavėjas“) · „Baudos“ (verbatim 4.5: „…taikoma 1200 EUR bauda…“, shortened with „Plačiau taisyklėse“). Buttons: „Visos taisyklės“ (Line) → /taisykles/; „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“ (Underline, download icon).
- Media: texture **4040619** (asphalt macro) duotone at 10%.
- Effects: BG parallax Subtle; left column sticky (CSS, top 120 px); toggles open 450 ms `ease-arrive`, ring fills; ✕ markers stagger 40 ms when a panel opens.
- Salient: Row bg image + overlay `#0F1417` 90% + Parallax Subtle; Column **Sticky Content** (CSS, Top); **Toggle Panels → Minimal Shadow** (accordion, deep linking) with `.sgp-toggle`; Buttons.

**S8 · 07 Siuntos sekimas — tracking strip** (paper-100)
- Purpose: a working tracking input on the home page.
- Layout: one band: H2 left, mono input + button right, helper line under.
- Content: H2 „Siuntos sekimas“ [P]; input placeholder „Siuntos kodas...“; button „Siuntos lokacija“ (both verbatim from the tool [P]); helper NEW „Neradote siuntos kodo? Paskambinkite – pasakysime, kur Jūsų siunta.“
- Behaviour: `GET` to `/siuntos-sekimas/?kodas=…`, which passes `kodas` into the iframe `https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=…`.
- Media: none. Effects: input focus lane (§4.9); button Arrow Animation.
- Salient: Raw HTML form with Salient's `nectar-inline-subscribe-form` styling + `.sgp-field`.

**S9 · Atsiliepimai (placeholder)** — Testimonial Slider Minimal, one slide „Čia bus tikri klientų atsiliepimai“, dashed frame; row set to **Disable row** until real reviews arrive. No invented quotes, stars or names.

**S10 · Atvykimas** — GS-Arrival (§4.8). Background texture **7024783** (red tail-light bokeh) at 12% + Parallax Subtle (optional). Rail ends in the terminus ring; tickets Fade In From Bottom (120 ms stagger); stub flaps run on entry.

**S11 · Footer** — GS-Footer (§4.10).

**S12 · Mobile call bar** — GS-CallBar (§4.12).

---

### 5.2 Apie įmonę `/apie-imone/`
1. **Route header** — H1 „Apie įmonę“ (menu label stays „Apie mus“); breadcrumb Pradžia › Apie įmonę; eyebrow verbatim „Saugiai greitai patikimai“; lead verbatim „SGP – visos pervežimo paslaugos“. Media **9989463** (white van, mountain road). Parallax Subtle + Slight Zoom Out Reveal; H1 Word Reveal. Salient per §4.11.
2. **01 Įmonė** (paper) — the three verbatim paragraphs [P] (the third: „Mes visada pasiruošę teikti kokybiškas transporto paslaugas už Jums prieinamą kainą!“), route names underlined (Highlighted Text). Right: Milestone stats (§4.7). Rail + waypoint.
3. **02 Principai** (dark) — verbatim lead „Saugumas, operatyvumas, profesionalumas, komfortas ir patogumas – tai esminiai kriterijai, kuriais grindžiama mūsų įmonės veikla…“ [S keleivių]; five stacking cards (mono „01“–„05“, title, verbatim paragraph — Saugumas without „(2017–2018 metų)“, Komfortas without DVD). Media per card: **7541981**, **6720534**, **31570314**, **17455631**, **27383867**. Effect: **Sticky Content Sections → Sticky Scroll Pinned Sections, effect Stacking** (cards stack with scale 1 → .94 of the previous one), Section Navigation dots off; mobile: plain stack.
4. **03 Kelyje** (paper) — gallery. Media **2449454**, **8858566**, **31570314**, **21041157**, **6169133**. **Image Gallery → Flickity**, Touch & Total indicator („03 / 05“ in mono), image parallax, Mask Edges; crop marks on the active slide. Note: replace with the client's own five photos from the old „Apie įmonę“ gallery once high-res files are supplied.
5. **04 Kodėl verta pasitikėti mumis?** (dark) — verbatim list [P, 9 bullets] as numbered timetable rows (Horizontal List Item, Border Animation: mono „01“, bold lead phrase, text). Edit per §10: bullet about „naujausiais mikroautobusais… DVD“ loses the DVD mention.
6. **GS-Board** (dark) and **GS-Arrival**.

### 5.3 Pervežimo paslaugos `/pervezimo-paslaugos/`
1. **Route header** — H1 „Pervežimo paslaugos“; lead verbatim first two sentences of the category text [P] („Pervežimo paslaugų poreikis Europoje nuolat auga…“). Media **36383706** (trucks and cars on a highway at dusk, light snow). Parallax Subtle.
2. **Three route tickets** (paper) — „Tarptautiniai pervežimai“ (verbatim tile), „Pervežimų grafikas“, „Siuntos sekimas“ (verbatim tile) as ticket-shaped Column Links with a mono meta line (e.g. „11 paslaugų · 2 kryptys“ / next date flap / „Siuntos kodas“). Hover: lift 4 px, perforation red, arrow cell fills. Column delay 0/120/240.
3. **01 Visos paslaugos — line index** (dark) — the 11 services as a vertical line list: ring on a 2 px lane, mono number, Barlow Condensed 44 px title, chips right; hover reveals that service's featured image in a fixed 4:5 frame to the right (desktop) and nudges the row 12 px. Salient: **Post Loop Builder → Vertical List**, hover effect **reveal featured image** + nudge, query: Pages, parent = Tarptautiniai pervežimai, order = menu order (if Pages are not offered in the query UI, register a `paslauga` CPT with rewrite slug `pervezimo-paslaugos/tarptautiniai-pervezimai` so URLs stay identical). Mobile: rows with 72 px thumbnails.
4. **02 Kryptys ir transportas** (paper) — verbatim paragraphs 2–3 [P] („…į / iš Airiją, į / iš Ispaniją, į / iš Vokietiją, į / iš Prancūziją…“ — grammar fix listed in §10), left sticky waypoint + H2 verbatim „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“, right text; inline image **32821932** (truck on a coastal road) with Column **Scroll Position Advanced** scale 0.88 → 1 and translateY 40 → 0 px.
5. **GS-Board**, **GS-Arrival**.

### 5.4 Tarptautiniai pervežimai `/pervezimo-paslaugos/tarptautiniai-pervezimai/`
1. **Route header (video)** — H1 „Tarptautiniai pervežimai“; lead verbatim „SGP pervežimai – komanda savo srities profesionalų, turinčių vieningą tikslą – užtikrinti, kad siuntiniai ir keleiviai į Ispaniją ir Airiją keliautų saugiai, greitai, patikimai ir komfortiškai.“ Media video **29374299** (highway interchange at dusk; 1280 px 4.9 MB, SD 2.6 MB), poster same. Parallax Subtle.
2. **01 Dviem maršrutais** (paper) — H2 verbatim „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais“; the full map (§5.1 S4) larger (9 cols), with hotspots on every stop; the two bullets verbatim („iš Lietuvos į Ispaniją ir atgal; iš Lietuvos į Airiją ir atgal“ — case fix per §10).
3. **02 Airija / 03 Ispanija** (two pinned chapters) — **Sticky Scroll Pinned Sections → Overlapping**; each chapter full-bleed:
   - Airija: bg video **2386447** (Irish cliffs, SD 3.3 MB, desktop only; phone uses photo **13568682**); inset photos **2881400**, **15885602** (ferry, Dublin Bay), **3220828**; dates (GS-Board filtered to IE rows), phones LT/IE/UK; small inset ferry clip **19274366** (SD 2.2 MB) in a 16:9 frame with the label „Keltas“ (Self Hosted Video, autoplay when in view, muted, no controls, lazy).
   - Ispanija: bg photo **22033738** (Málaga at sunset) graded; insets **27868340**, **32821932**; dates, phones LT/ES.
   Effects: headline Word Reveal; insets Mask Reveal with 120 ms stagger; the rail becomes a horizontal lane across the chapter header.
4. **04 Pakeliui** (paper) — verbatim paragraph „Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija, todėl nedvejokite…“; four stop cards (LENKIJA, VOKIETIJA, BELGIJA, PRANCŪZIJA) on a horizontal lane — mono names, ring, no invented facts. Horizontal List Item ×4 (Border Animation). Background accent photo **1225126** (light trails near Niederdorla, Germany) in the Vokietija card (Column bg, hover opacity 0 → .5).
5. **05 Kodėl verta pasitikėti mumis?** (dark) — 9 verbatim bullets as numbered rows (edit per §10).
6. **06 Ko negalima siųsti?** (dark, continues) — verbatim H5 + 8 bullets as a two-column ✕ list; the two paragraphs about responsibility and confiscation verbatim in a red-bar callout.
7. **07 Ką dar turite žinoti?** (paper) — four verbatim paragraphs as four notice cards (1 px ink top rule, mono index); the first card („…pristatymas truks apie 3–4 paras nuo paėmimo datos“) carries the rules footnote (§9).
8. **08 Paslaugos** — compact line list of the 11 services (Global Section reused from 5.3/3).
9. **GS-Arrival**.

### 5.5 Service detail template (one template → 11 pages)
Saved as WPBakery template „SGP – paslauga“; shared rows come from Global Sections. Pages live at `/pervezimo-paslaugos/tarptautiniai-pervezimai/<slug>/`.

| # | Section | Layout / content | Effects | Salient |
|---|---|---|---|---|
| T1 | Route header | Breadcrumb route, H1 = page H1 [S], lead = „Santrauka“ [S] verbatim, 2–3 fact chips, compact call ticket | Parallax Subtle, Slight Zoom Out Reveal, H1 Word Reveal | §4.11 |
| T2 | Faktų lenta (fact strip) | Dark board, 4 cells: **Kryptys** · **Trukmė** · **Pristatymas** · **Kaina / Svarbu** (values per table below, mono) | Flap on entry | 4 Columns, `.sgp-flap` |
| T3 | 01 Apie paslaugą | Paper; left: waypoint + child-route chips (from „Vaikiniai puslapiai“ [S], e.g. „Krovinių pervežimas į Airiją“) linking to /pervezimu-grafikas/; right: first 1–2 verbatim paragraphs | Fade In From Bottom, rail | Column Sticky Content |
| T4 | 02 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ (verbatim H5 → H2) | Dark; 3–5 blocks from the verbatim paragraphs, each with a bold lead phrase; sticky media swaps per block (service media set) | Media crossfade + scale 1.06 → 1 per block (Salient native) | **Sticky Content Sections → Sticky Media, Scrolling Content** (media 45% width, 80vh) |
| T5 | 03 „Kliento atsakomybės: ką reikia žinoti?“ (verbatim H5 → H2) | Paper; left sticky title; right toggles: Pakavimas · Draudžiami daiktai · Gavėjas sutartu laiku · (service-specific panel) | Toggle open 450 ms | **Toggle Panels → Minimal Shadow** |
| T6 | Artimiausi pervežimai | GS-Board | Flap | Global Section element |
| T7 | Closing line | Verbatim closing sentence („Krovinių pervežimas su „SGP pervežimai“ – …“) in Barlow Condensed 500 statement size, key words underlined red | Highlighted Text underline draw | Highlighted Text |
| T8 | Kita stotelė | Next service in order (11 → 01) | Hover image reveal + lane draw | §4.12 |
| T9 | Atvykimas | GS-Arrival | — | Global Section |

Per-service data (facts only from [S]; years „2017–2018“ and „DVD“ removed):

| Slug | T1 chips | T2: Kryptys / Trukmė / Pristatymas / Kaina–Svarbu | T5 special panel | Hero media | T4 sticky media | Video |
|---|---|---|---|---|---|---|
| kroviniu-pervezimas | Nuo durų iki durų · Kroviniai apdrausti | Airija, Ispanija, Vokietija, Prancūzija ir atgal / apie 3–4 paros [P] / nuo durų iki durų / „Iškrauname, jei nereikia specialios technikos“ | Tranzito šalių teisės aktai (verbatim consultation paragraph) | 38927007 | 38404178, 31570314, 2449454 | — |
| negabaritiniu-kroviniu-pervezimas | Išankstinis planavimas · Nuo durų iki durų | Lietuva, Prancūzija, Ispanija, Airija / planuojama iš anksto / nuo durų iki durų / „Iškrovimo technika – kliento atsakomybė“ | Leidimai ir iškrovimas | 35332902 | 38095094, 31570314, 35332902 | 19552565 (header, SD, desktop) |
| daliniu-kroviniu-gabenimas | Mokate mažiau · Nuo durų iki durų | Vokietija, Prancūzija, Ispanija, Airija (į / iš) / apie 3–4 paros [P] / nuo durų iki durų / „Papildomas atvežimas apmokestinamas“ | Tikslūs adresai | 29786116 | 34585120, 12418936, 6169133 | — |
| daiktu-pervezimas | Apie 3–4 paros · Nuo durų iki durų | Vokietija, Prancūzija, Ispanija, Airija / apie 3–4 paros / nuo durų iki durų / „Pakavimas – kliento atsakomybė“ | Pakavimas | 36933446 | 9185835, 160483, 6170458 | — |
| automobiliu-pervezimas | Traliuku · Apie 3–4 paros | Vokietija, Lietuva, Airija, Ispanija / apie 3–4 paros / traliuku, sutartu laiku / „Pakartotinis atvažiavimas apmokestinamas“ | Pristatymas sutartu laiku | 29566910 | 1606957, 35531295, 29566910 | 34371915 (header, b/w + dark overlay) |
| motociklu-pervezimas | 3–4 paros · Nuo durų iki durų | Ispanija, Prancūzija, Vokietija, Lenkija, Airija / 3–4 paros / nuo durų iki durų / — | — | 4858429 | 2177200, 5713164, 4858429 | 34308329 |
| keleiviu-pervezimas | Keleiviai apdrausti · 3–4 paros | Ispanija, Vokietija, Prancūzija, Airija / 3–4 paros / nuo durų iki durų / „Vairuotojai laikosi darbo ir poilsio režimo“ | T4 = the 5 principles (Saugumas … Patogumas); T5 replaced by comfort icon list (S5 home) | 36377055 | 27383867, 17455631, 7541981 | 15602514 (optional, white van) |
| gyvunu-pervezimas | Narvus turime mes · Nuo durų iki durų | Ispanija, Prancūzija, Vokietija, Airija / — / į rankas gavėjui / „Kaina individuali“ (verbatim reasons) | „Sveikata ir dokumentai“: pasiutligės skiepai ~mėnuo iki kelionės, kraujo tyrimas, veterinaro dokumentas, identifikacija, vaistai nuo helmintų pažymėti pase (verbatim, callout „Svarbu“) | 32872983 | 3868901, 21767483, 32872983 | — |
| siuntu-pervezimas | Skubios siuntos · Nuo durų iki durų | Vokietija, Ispanija, Airija, Prancūzija / — / nuo durų iki durų / „Pakuotė – 5 cm tarpas“ | Pakuotė (plėvelė, popierius, laikraščiai netinka) | 6170458 | 4487517, 6407553, 4440774 | — |
| siuntu-pristatymas | Į rankas gavėjui · Apie 3–4 paros | Vokietija, Prancūzija, Ispanija, Airija / apie 3–4 paros / į rankas / — | — | 13456097 | 4440774, 6407553, 7464731 | — |
| perkraustymo-paslaugos | Apie 3–4 paros · Nuo durų iki durų | Vokietija, Ispanija, Prancūzija, Airija / apie 3–4 paros / nuo durų iki durų / **„Pakrovimas ir iškrovimas neįeina“** | Pakavimas (5 cm, burbulinė plėvelė); Augintiniai – atskirai, narvuose | 4246238 | 7464731, 9185835, 4246238 | — |

SEO note: the 27 live child pages (e.g. `/kroviniu-pervezimas/kroviniu-pervezimas-i-airija`) are not in the new sitemap → 301 to their parent service page; their names survive as chips in T3.

### 5.6 Pervežimų grafikas `/pervezimu-grafikas/`
1. **Compact header** (dark, 44vh) — H1 „Pervežimų grafikas“, breadcrumb; bg texture **9807331** (wet road at night, b/w) at 18% + Parallax Subtle. No photo hero: the board is the hero.
2. **01 Lenta** (dark) — full departure board: filter tabs „Visi · Airija · Ispanija“ (Tabs → Minimal); two groups „Iš Lietuvos“ / „Į Lietuvą“; one row per date: Kryptis tiles | Data tiles („09 SPAL.“) | Būsena („Artimiausias“ / „po N d.“ / hidden when past) | „Skambinti“ (the LT number of that direction). Row hover: +3% white, red 2 px left lane grows. All dates exactly as [P]; no times, places or years invented.
3. **02 Kalendorius** (paper, optional enhancement) — a horizontal day ruler for the months in the data (rugsėjis–spalis): 1 px tick per day, mono day numbers every 5 days, departure days marked with rings (red = iš Lietuvos, ink = į Lietuvą), hover tooltip „Spalio 9 d. · Lietuva → Airija, Ispanija“. Generated from the same data by the custom JS (Raw HTML container). Mobile: vertical list instead.
4. **03 Ką verta žinoti** (paper) — NEW „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“ + verbatim „…trunka apie 3–4 paras, skaičiuojant nuo paėmimo dienos“ + rules footnote; both phone groups as tickets.
5. **GS-Arrival**.

### 5.7 Siuntos sekimas `/siuntos-sekimas/`
1. **Compact header** — H1 „Siuntos sekimas“ (fixes the live page, whose band said „Pervežimo paslaugos“); bg **35497082** (light trails, Craigavon) + Parallax Subtle.
2. **01 Paieška** (paper + graticule) — large mono input „Siuntos kodas...“ + Signal button „Siuntos lokacija“ (verbatim); the form targets the iframe below (`sekimas.php?embed=1&kodas=`); reads `?kodas=` from the URL (home strip).
3. **02 Rezultatas** — the iframe (min-height 520 px) inside a map frame with crop marks and graticule; messages from the tool stay verbatim („Neįvestas siuntos kodas!“, „Toks siuntos kodas neegzistuoja!“).
4. **03 Pagalba** — three small cards: NEW „Neradote siuntos kodo?“ → phones; „Siuntų pristatymas“ → service page; „Taisyklės“ → /taisykles/.
5. **GS-Arrival**. Meta description must be written (live value is „<b>test</b>“).
Salient: Raw HTML form + iframe; Columns; Buttons.

### 5.8 Taisyklės `/taisykles/`
1. **Route header** — H1 „Siuntų siuntimo taisyklės“; lead (live meta text) „Paslaugos Mokėtojai (užsakovai) privalo susipažinti su šiomis taisyklėmis ir vadovautis jomis ruošiant siuntas ir užsakant paslaugas.“; media **6169133** (waybills); Parallax Subtle.
2. **01–06 Taisyklės** (paper) — **Tabs → Vertical Sticky Scrolling** with six tabs = the six numbered sections verbatim [P] („1. Siuntų tikrinimas“ … „6. Atvejai, kuriais įmonė neprisiima atsakomybės“). The tab list is styled as a vertical lane with six stops; the active stop fills red (custom CSS on the Salient tab list). 4.2 → two-column ✕ list (12 items); 4.5 fines → red-bar callout „Svarbu“ with „1200 EUR“ in bold; 3.4 shown verbatim.
3. **PDF** — Button Underline with download icon „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“ → existing file `sgp_sutartis-su-siunteju.pdf`.
4. **GS-Board**, **GS-Arrival**.

### 5.9 Kontaktai `/kontaktai/`
1. **Header (no photo)** — dark, 40vh: H1 „Kontaktai“; lead verbatim „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“; rail terminus ring (this page *is* the arrival).
2. **01 Skambinkite** — two large tickets „Pervežimai į Airiją“ (LT, IE, UK) and „Pervežimai į Ispaniją“ (LT, ES): each number is a full-width 64 px tap target; stub = next departure from Lithuania (flap). Email row verbatim.
3. **02 Parašykite** — form fields verbatim (contact form 217 [P]): „Jūsų vardas“, „El. pašto adresas“, „Žinutės tema“, „Žinutė“ (min. 20), button „Siųsti“, consent note verbatim.
4. **03 Kur važiuojame** — mini route map (the map Global Section, static, both branches active).
No address, map pin, opening hours, company code or social links — the site has none (§9). GS-Arrival hidden on this page.

### 5.10 Privatumo politika `/privatumo-politika/`
1. **Compact header** — H1 „Privatumo politika“, no image.
2. **Document** (paper) — left sticky mini-TOC (2 stops: Informacija, Slapukai (Cookies)); right: „Informacija ruošiama...“ (verbatim; flagged: the client must supply a real GDPR policy before launch); cookie table verbatim, restyled as timetable rows (mono), link verbatim „Norėdami pasitikrinti … spauskite čia.“ (target must be replaced; the old Joomla URL will not exist).
No GS-Arrival (as on the live site). Salient: Columns + Column Sticky Content + Text Blocks + `.sgp-table`.

### 5.11 404
- Full-height dark row; bg **160483** (person with a suitcase on a foggy road), graded, overlay 80%.
- Board tiles „404“ (flap), H1 NEW „Maršrutas nerastas“, text NEW „Šio puslapio nėra – bet mūsų mikroautobusai kursuoja toliau.“; buttons „Į pradžią“ (Signal) and „Pervežimų grafikas“ (Line); both LT phone numbers.
- The rail comes down, breaks into a dashed segment and stops at a ring with a „?“.
- Salient: Theme Options → 404 page built from a Global Section (or a Page assigned as 404 via Salient's option), Row Full Height, bg image, Animated Text.

---

## 6. Mobile behaviour

Salient breakpoints are ≤ 690 phone / 691–999 tablet / ≥ 1000 desktop; the spec's "≤ 1000" = tablet + phone, "≤ 600" = phone.

**≤ 1000 px (tablet and phone)**
- Global rail hidden; lanes appear only inside lists (services, map list, comfort, timeline, menu, footer).
- Header 68 px: logo, red phone button (bottom sheet with all 5 numbers), burger; nav hidden from 1179 px. Ticker shows only the soonest departure (Scrolling Text on phone).
- Hero: height = content (not 100svh); H1 41–56 px; call buttons full width, stacked; the board detaches under the hero as a solid `asphalt-950` block, 2 × 2 cells (tablet).
- Services: Salient stacks Horizontal Scrolling children → custom CSS renders rows: 96 px thumbnail, number + arrow, 24 px title, summary; chips and arrow cells hidden; vertical lane with rings fills with scroll.
- Map (≤ 699 px): SVG replaced by a vertical route list for the active tab (LIETUVA → LENKIJA → VOKIETIJA → BELGIJA → [KELTAS dashed] → AIRIJA, or → PRANCŪZIJA → ISPANIJA).
- Cinematic rows: Salient "Disable Parallax Backgrounds On Mobile" ON; video backgrounds replaced by posters ("Disable Video Backgrounds On Mobile" ON) except where the client explicitly wants the 0.8 MB hero clip.
- Comfort stops and timelines become vertical lists with the lane on the left.
- Pinned sections (Apie → Principai, Tarptautiniai → Airija/Ispanija) have their effect switched off per device (Salient per-device toggle) and stack.
- Mobile call bar fixed at the bottom; body gets 58 px + safe-area bottom padding. Tap targets ≥ 44 px.
- Entrance animations: Salient default is off on mobile — keep it off except the H1 word reveal (element-level "animate on mobile").

**≤ 600 px (phone)**
- Gutter 16 px; body 16 px; D1 41 px, D2 36 px.
- Board: single column; each cell = code + name left, date tiles + status right.
- Tickets: stub below the body, horizontal dashed perforation, no notches.
- Stats 2 × 2; footer single column; forms full width.
- Specimen/tables scroll horizontally inside their own container; the page never scrolls sideways (`overflow-x: clip` on `html, body`).

---

## 7. Reduced motion (`prefers-reduced-motion: reduce`)
Salient has no global switch, so ship this CSS/JS block:
- Lenis not initialised (native scrolling).
- Background videos do not autoplay: poster image + visible „Leisti“ toggle; parallax transforms not applied.
- Rails, lanes, H1 dashes, map (active branch) and underlines render fully drawn; rings static (no halo).
- Split-flap shows the final text immediately; odometer shows the final numeral.
- Pinned horizontal services → a normal horizontal scroll container with scroll-snap on desktop; list on mobile.
- Animated Text / column entrances: `transition-duration: .001ms` and `transform: none; opacity: 1` for `.nectar-split-heading *`, `[data-animation]` columns and images.
- Ticker static; blinking live dot static.
- View transitions off.
The style tile implements all of the above.

---

## 8. Performance budget

| Item | Budget |
|---|---|
| LCP (4G, mid-range phone) | ≤ 2.5 s; LCP element = H1 text (fonts preloaded) or hero poster |
| Fonts | 3 families, 7 weights total, woff2 latin + latin-ext, self-hosted: ≤ 190 KB; preload Barlow Condensed 600 |
| Custom CSS + JS | ≤ 5 KB + 6 KB (gzip ≈ 2 + 2.5 KB) |
| Hero video | HD 2.6 MB (desktop, after poster); SD 0.8 MB (phone, optional); poster ≤ 200 KB |
| Other videos | Only lazy (IntersectionObserver, 300 px margin), paused off-screen, desktop only: 4685871 HD 3.8 MB; hover clips 1.3–2.6 MB SD on first hover, fine pointers only; 2386447 and 3987777 **never HD** (11.2 MB) — SD only |
| Photos | Re-host in the WP media library as WebP/AVIF (don't hotlink Pexels in production); srcset 480 / 760 / 1100 / 1600 / 1920; cards 760 px ≈ 60–90 KB; lazy below the fold; fixed aspect ratios (CLS < 0.05) |
| Home transfer | Phone first view ≤ 1.2 MB (poster instead of video); full scroll ≤ 3 MB. Desktop first view ≤ 3.5 MB incl. hero video; full scroll ≤ 9 MB with all videos |
| JS behaviour | One rAF-throttled scroll handler; no layout reads in loops except the 11 service cards while pinned; exclude the custom JS from Salient "Delay JavaScript Execution" or bootstrap it on first interaction |
| Third parties | reCAPTCHA only on pages with forms (or Cloudflare Turnstile); GA4 via GTM (UA is dead) |

---

## 9. Content handling (conflicts and gaps)

- **Delivery time:** marketing copy says „apie 3–4 paras“ from pickup; rules 3.4 say „per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos“. v2 uses „apie 3–4 paros“ as the typical trip and adds, in mono small print wherever duration appears next to parcels: „Siuntų pristatymo įsipareigojimas pagal taisykles – per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.“ The old meta text „nuo 2 iki 3 parų“ is dropped.
- **Dates without a year:** shown exactly as published („09 spal.“), never with a year or weekday; statuses are relative („po 16 d.“). Past dates disappear from boards and are struck through in light timetables; if nothing is upcoming the board says „Grafikas atnaujinamas“.
- **„Nauji (2017–2018 metų) mikroautobusai“:** years removed everywhere; wording kept as „techniškai tvarkingi, prižiūrimi mikroautobusai“ / verbatim „naujais, techniškai tvarkingais“ where it already appears without years (client to confirm). DVD removed from comfort lists.
- **Countries:** transit list uses only the verbatim four (Lenkija, Vokietija, Belgija, Prancūzija). The UK appears only as a phone country code. The Ireland branch on the map shows direction + sea crossing, not a specific port.
- **No invented data:** no fleet size, years in business, client counts, reviews, awards, partner logos, address, company code, opening hours, prices. The only euro figure on the site (1200 EUR fines) stays inside the rules.
- **Phone numbers:** same numbers, normalised spacing (+353 86 450 3104, +44 7566 878681, +34 602 547 929); `tel:` links unchanged.
- **SEO fixes to carry into WordPress:** one H1 per page; canonical URLs fixed (the live ones double the domain); 301s for the 27 child pages and the duplicate `/pervezimo-paslaugos/siuntos-sekimas`; real meta descriptions (tracking page is „<b>test</b>“); domain spelled „sgp-pervezimai.lt“.

---

## 10. Naujas tekstas — reikia kliento patvirtinimo

Headlines and UI copy
1. Hero H1: „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“
2. Hero eyebrow: „Tarptautiniai pervežimai mikroautobusais“
3. Hero lead: „Visos pervežimo paslaugos – saugiai, greitai, patikimai. Keleiviai, siuntos, automobiliai, motociklai, gyvūnai ir perkraustymas nuo durų iki durų.“
4. Board note: „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“
5. Board / ticker states: „Artimiausi išvykimai“, „Artimiausias“, „po N d.“, „rytoj“, „šiandien“, „Vėliau: …“, „Kitos datos – netrukus“, „Grafikas atnaujinamas“, „Visas grafikas“, „Visas pervežimų grafikas“, „Kitas išvykimas iš Lietuvos“
6. Stats labels and captions: „Kryptys – Airija ir Ispanija – iš Lietuvos ir atgal“, „Paslaugos – tarptautinių pervežimo paslaugų“, „Kelionėje – paros nuo paėmimo dienos“, „Pakeliui – šalys: Lenkija, Vokietija, Belgija, Prancūzija“
7. Services chapter: „Slinkite“, „11 stotelių“, „Plačiau“, end card „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“
8. Condensed card summaries: Negabaritiniai „Kroviniai, kurių matmenys didesni, nei leidžiama šalyse, per kurias jie keliauja.“; Daiktai „Langai, žoliapjovės, buitinė įranga ir kiti didesni ar mažesni daiktai.“; Automobiliai „Automobilius gabename traliuku – iš Airijos, Ispanijos, Vokietijos ir į jas.“; Motociklai „Iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos bei Airijos – nuo durų iki durų.“; Keleiviai „Atlenkiamos ir šildomos sėdynės, kondicionierius. Kelionės metu visi keleiviai apdrausti.“; Perkraustymas „Persikeliate gyventi į kitą šalį Europoje? Daiktus pervešime nuo durų iki durų.“
9. Chips: „Kroviniai apdrausti“, „Išankstinis planavimas“, „Mokate mažiau“, „Traliuku“, „Keleiviai apdrausti“, „Narvus turime mes“, „Skubios siuntos“, „Į rankas gavėjui“, „Apie 3–4 paros“, „Nuo durų iki durų“
10. Routes H2: „Dvi kryptys. Keturios šalys pakeliui.“; map labels „išvykimas“, „atvykimas“, „Keltas“, „Maršrutų schema · ne mastelis“, „Maršruto taškai“ + coordinates in Lithuanian notation
11. Route panel buttons: „Skambinti dėl Airijos“, „Skambinti dėl Ispanijos“; tab labels „Airija“, „Ispanija“; row labels „Iš Lietuvos“, „Iš Airijos“, „Iš Ispanijos“, „Į Lietuvą“, „Kelionė“
12. Cinematic H2: „Kelionė trunka apie 3–4 paras. Pasirūpinsime, kad laikas neprailgtų.“; stop titles „Kondicionierius“, „Keleiviai apdrausti“, „Poilsio režimas“
13. Delivery footnote: „Siuntoms: kelionė trunka apie 3–4 paras nuo paėmimo dienos; pagal taisykles įsipareigojame siuntą pristatyti per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.“
14. Timeline: H2 „Nuo skambučio iki durų“; station codes „Prieš“, „D0“, „D1–D3“, „D3–D4“; titles „Skambutis arba užklausa“, „Paėmimas nuo durų“, „Kelyje“, „Pristatymas į rankas“; text „Siuntos vietą galite pasitikrinti pagal siuntos kodą.“
15. Rules chapter: panel titles „Draudžiami daiktai“, „Pakavimas“, „Gavėjas ir pristatymas“, „Baudos“; button „Visos taisyklės“, „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“; callout label „Svarbu“
16. Tracking helper: „Neradote siuntos kodo? Paskambinkite – pasakysime, kur Jūsų siunta.“; help cards „Neradote siuntos kodo?“
17. Testimonials placeholder: „Čia bus tikri klientų atsiliepimai“
18. Form: title „Gauti pasiūlymą“ (button text is verbatim), select placeholder „Pasirinkite paslaugą“, placeholder „Iš kur, į kur ir kada?“, errors „Įrašykite vardą“, „Įrašykite telefono numerį“, „Patikrinkite el. pašto adresą“, „Pasirinkite paslaugą“, „Žinutė – bent 20 simbolių“. Proposal: „Kas Jus domina?“ becomes a select of the 11 services.
19. Navigation and system: „Skambinti“, „Į Airiją / Į Ispaniją“ (call bar), „Pauzė / Leisti“ (video), „Pereiti prie turinio“, menu numbering „00–07“, waypoint names („Apie mus“, „Paslaugos“, „Maršrutai“, „Kelionėje“, „Kelionės eiga“, „Prieš siunčiant“, „Siuntos sekimas“, „Atvykimas“), „Jūs čia“, „Kita stotelė“, „↑ Į pradžią“, footer line „Visos pervežimo paslaugos: Lietuva – Airija – Lietuva, Lietuva – Ispanija – Lietuva. Saugiai, greitai, patikimai.“
20. Service fact strip labels: „Kryptys“, „Trukmė“, „Pristatymas“, „Kaina“, value „Pasiūlysime telefonu“, „Planuojama iš anksto“
21. Schedule page: filters „Visi / Airija / Ispanija“, calendar tooltip format „Spalio 9 d. · Lietuva → Airija, Ispanija“
22. 404: „Maršrutas nerastas“, „Šio puslapio nėra – bet mūsų mikroautobusai kursuoja toliau.“, „Į pradžią“

Edits to existing text (need a yes/no)
23. Remove „(2017–2018 metų)“ and „DVD“ from all service and trust texts.
24. Fix the typos listed in the content notes (e.g. „sako žmogiškųjų“, „užtiktiname“, „sklandžia kelionę“, „daržo režimo“, „šaunamiejii“, „cigarecių“, „baikotai“, „maišrai“, „tiks geriausius“, „Klejonė“, „teisiai į rankas“, „šias tris šalis“ → keturias) and the case errors „į / iš Airiją“ → „į Airiją / iš Airijos“.
25. Phone number spacing normalised (numbers unchanged).
26. Map assumption: the Ireland branch leaves the shared trunk after Belgium and crosses by ferry — confirm the real route (via the UK or a direct ferry from France) and whether France is also on the Ireland route.
27. Copyright line „© 2026 SGP pervežimai. Visos teisės saugomos.“ (live: „© 2026 sgppervezimai.lt …“, wrong domain spelling).
28. Page title/H1 alignment: „Apie įmonę“ (H1) vs menu „Apie mus“; „Siuntos sekimas“ header instead of „Pervežimo paslaugos“; „Pervežimų grafikas“ added to the main menu.

---

## 11. Build appendix — the unavoidable custom code

The style tile implements the same pieces under short class names (`.rail`, `.ring`, `.wp`, `.flap`, `.ticket`, `.paper`, `.svc__hline`); in WordPress prefix them `sgp-` as below. The complete working code is in `kryptis-A.html`.

```css
/* Route line (Raw HTML <span class="sgp-rail"><i></i></span> as the row's first element) */
.sgp-has-rail{position:relative}
.sgp-rail{position:absolute;top:0;bottom:0;width:14px;left:calc((100% - min(100% - 2*var(--g),1320px))/2 + 20px);pointer-events:none}
.sgp-rail::before{content:"";position:absolute;left:6.5px;top:0;bottom:0;width:1px;opacity:.28;
  background:repeating-linear-gradient(to bottom,currentColor 0 4px,transparent 4px 10px)}      /* planned route */
.sgp-rail i{position:absolute;inset:0;transform:scaleY(var(--p,0));transform-origin:top;
  border-left:1px solid rgba(239,69,57,.42);border-right:1px solid rgba(239,69,57,.42)}          /* travelled lane */
.sgp-rail i::after{content:"";position:absolute;left:5px;width:2px;top:0;bottom:0;background:#EF4539}
@media (max-width:999px){.sgp-rail{display:none}}

/* Map paper */
.sgp-graticule{background-image:linear-gradient(rgba(28,29,29,.055) 1px,transparent 1px),
  linear-gradient(90deg,rgba(28,29,29,.055) 1px,transparent 1px);background-size:112px 112px}

/* Ticket stub: two half masks leave 11px notches at the perforation */
.sgp-ticket{--stub:190px;--n:11px;
  mask:radial-gradient(circle var(--n) at calc(100% - var(--stub)) 0,#0000 98%,#000) top/100% 51% no-repeat,
       radial-gradient(circle var(--n) at calc(100% - var(--stub)) 100%,#0000 98%,#000) bottom/100% 51% no-repeat}
@media (max-width:600px){.sgp-ticket{mask:none}}
```

```js
// sgp-route.js (outline, ≈ 6 KB; full version in kryptis-A.html)
// 1. rails:    for each .sgp-has-rail → p = clamp((0.72*vh - top) / height) → --p on .sgp-rail i;
//              .sgp-wp gets .is-reached when its top < 0.72*vh.
// 2. flap:     .sgp-flap → split into tiles, on first intersection cycle 4–7 random chars
//              (A–Ž, 0–9) every 55 ms, 42 ms stagger; sr-only copy of the text for screen readers.
// 3. schedule: read data-date (YYYY-MM-DD) from GS-Board rows → next/soonest/past classes,
//              „po N d.“ labels, ticker items.
// 4. hroute:   inside Salient Horizontal Scrolling, read the track's translateX each frame,
//              fill the static lane from ring 1 to the right edge, toggle .is-reached on cards.
// 5. map:      on Tabs change / first intersection → restart stroke-dashoffset (pathLength=1).
// All steps: one rAF-throttled scroll listener; skipped entirely under prefers-reduced-motion.
```

Salient global settings summary: Material skin · Accent `#EF4539` · Header Centered Menu, Permanent Transparent, Hide Until Needed, Resize on Scroll, BG blur, Animated Underline hover · Off Canvas Fullscreen Split (Global Section content) · Smooth Scrolling Lenis, strength 50 · Column/Image easing easeOutExpo 1300 ms · View Transitions: Horizontal Gradient Wipe (desktop only) · Lightbox fancyBox3 · Fluid Typography ON, local Google Fonts · Disable Parallax Backgrounds on Mobile ON · Disable Video Backgrounds on Mobile ON (hero exception optional) · Back To Top OFF (the call bar replaces it) · Footer = Global Section, reveal effect OFF.
