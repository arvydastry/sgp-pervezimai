# SGP pervežimai v2 — dizaino sistema („Maršruto linija“, galutinė)

**Status:** final, single source of truth for the v2 static demo and the WordPress (Salient 18.3.0 · Salient WPBakery 8.7.3 · Salient Core 3.1.6) build.
**Date:** 2026-09-23 · **Winner:** Kryptis A „Maršruto linija“ (judge totals 66 / 63.5 / 68.5; two of three panels picked A), with must-fixes and grafts from B and C applied.
**Companion style tile:** `docs/kryptys/kryptis-A.html` — updated to these tokens and fixes. Every block carries `data-salient="…"`; the **Salient žymės** button (bottom-left) overlays them. Serve the repo root over http (`python3 -m http.server 8765`), open `/docs/kryptys/kryptis-A.html`. Append `?siandien=2026-09-23` to freeze "today" for presentations and `?domina=Gyvūnų%20pervežimas` to test form pre-fill.
**Sources:** `turinys-puslapiai.md` [P], `turinys-paslaugos.md` [S], `salient-elementai.md`, `media.json` (only ids listed there), `assets/img/logo.svg` + `logo_light.svg`, `v1/index.html` (what not to resemble), `kryptys/kryptis-A|B|C.md`.

**How to read this document**
- „…“ = Lithuanian copy, verbatim from [P]/[S] unless marked **NEW** (every NEW string is listed in §8.1 for client approval).
- `M##` = motion effect id (§5.2). `GS-…` = Salient Global Section (§6.0). `T#` = service-template section (§6.5).
- "Demo" = static HTML in `v2/`. "Production" = WordPress + Salient. When they differ, both are specified.
- Where this document and `kryptis-A.md` disagree, **this document wins**.

---

## 0. Decisions at a glance

### 0.1 What changed versus the winning spec (`kryptis-A.md`)

| # | Area | kryptis-A.md | Final system | Why (judge item) |
|---|---|---|---|---|
| 1 | Rail | Raw HTML span in every row + JS reading scroll | **One CSS pseudo-element per row** (`.sgp-has-rail`), progress by CSS scroll-driven animation (`view-timeline`), fully drawn where unsupported. **0 bytes JS** | must-fix: rail as progressive enhancement, no per-row Raw HTML |
| 2 | Services lane | JS reads the transform of Salient's Horizontal Scrolling track | **IntersectionObserver** marks each card "reached" when it enters the left/top 70 % of the viewport; each card draws its own lane segment (≈0.5 KB) | must-fix: fragile transform reading |
| 3 | H1 | Animated Text + inline dashes (impossible natively) | **Raw HTML H1**: sr-only keyword sentence „Tarptautiniai pervežimai: Lietuva – Airija, Lietuva – Ispanija ir atgal“ + `aria-hidden` visual rows; fallback = Animated Text Word Reveal of the plain sentence | must-fix: Salient honesty, SEO keyword |
| 4 | Hero fit | Board fell below the fold on laptops | D1 capped at `10.5svh`; ≥1280 px the two call buttons move to a right column; board cells re-structured (no wrapping); compact rules at ≤760 px height. Verified: board fully visible at 1366×657, 1366×768, 1440×800, 1024×768 | must-fix |
| 5 | Schedule data | Dates typed in 5 places, `data-date` via Extra Class (impossible) | **ACF Options repeater (ISO dates) + `[sgp_grafikas]` shortcode** feeding ticker, board, timetables, stubs, "next" line and the schedule page; ≈1 KB JS recomputes relative labels on cached pages; "Atnaujinta …" stamp | grafts C + judge 3 |
| 6 | Tap-to-call | Board/timetables were display only | **Every schedule row is a full-width `tel:` link**; outbound rows dial the LT line, inbound rows dial the destination-country line (IE→LT +353 86 450 3104, ES→LT +34 602 547 929), full `aria-label` | graft C |
| 7 | Dates | „09 spal.“ everywhere | Full dates „Spalio 9 d.“ in light timetables, stubs, ticker and next-line; **flap tiles „09 SPAL.“ only on the dark board**, with the full date under them | graft C |
| 8 | Readability | 9–11 px labels | **Nothing below 12 px** anywhere (labels, chips, form labels, map text, stub captions, call bar). Mono uppercase only for short labels | must-fix |
| 9 | Red | Red rings everywhere, `.wp__no` 3.5:1 | Unreached rings are **neutral**; red only when reached. Small red text: `signal-ink #C4301E` on light, **new `signal-lit #F4604F`** on dark cards. Rule: red ≤ ~5 % of any viewport | must-fix + graft B |
| 10 | Pseudo-precision | Coordinates, „Lygiakampė projekcija“, map degree labels, day codes D0/D1–D3 | **All removed.** Devices kept: rail + rings, board, tickets, graticule; crop marks only on 2 image slots | must-fix |
| 11 | Map | Ireland via Belgium + „Keltas“ ferry leg; JS draw | Trunk LT–PL–DE; ES branch DE–BE–FR–ES; **Ireland leg neutral dashed ink-2, labelled „maršrutas tikslinamas“**, no crossing point, no ferry imagery. **Draw is CSS-only** (scroll-scrubbed + replays on tab switch) | must-fix + graft B |
| 12 | Phone chrome | Ticker + header + call bar = 156 px on phones | **Ticker is desktop-only.** Phones get a one-line „Artimiausias išvykimas“ under the H1 (first viewport) | must-fix |
| 13 | Mobile call bar | Ireland red, Spain dark | **Both directions identical** (dark, red icon, number visible) | must-fix |
| 14 | Services end card | „Skambinti“ dialled Ireland only | Shows **both LT numbers** as two call buttons | must-fix |
| 15 | Delivery time | Mono small-print footnote | Two labelled facts (`dl.sgp-kv`): „Kelyje: apie 3–4 paros nuo paėmimo dienos“ / „Įsipareigojimas siuntoms: per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklių 3.4 p.)“ | graft B |
| 16 | Kelionėje H2 | „Kelionė trunka apie 3–4 paras…“ | H2 **„Du namai, vienas kelias tarp jų.“** (NEW, text only — no inline media) + lead „Kelionė trunka apie 3–4 paras – pasirūpinsime, kad laikas neprailgtų.“ | graft C |
| 17 | Process | D0 → D3–4 timeline, 4 stations | 3 stations **Paėmimas → Kelyje apie 3–4 paras → Pristatymas** + the two labelled facts | must-fix |
| 18 | Rules | Toggles | Panels with counts („Draudžiama siųsti (12)“, „Pakavimas (4)“) + **fines table** (4.5 p.) | graft B |
| 19 | Services overview page | Post Loop hover-image list (echoed v1) | **Sticky Scroll Pinned Sections → Stacking** with sticky index of 6 groups | graft (judge 3) |
| 20 | Service template | Flap fact strip | `dl.sgp-kv` fact sheet; **sticky Page Submenu**; Image With Hotspots (keleiviai); „Prieš kelionę“ checklist + 3 price factors (gyvūnai) | grafts B + C |
| 21 | About chapter | Statement + stats | + B's datasheet (Veikla / Kryptys / Taip pat / Principas / Draudimas / Vairuotojai) | graft B |
| 22 | Switchboard | Mega Menu + custom bottom sheet | **Native HTML `popover`** (dropdown ≥1000 px, bottom sheet below) — no JS except a 5-line hook for the Salient menu link | simplification |
| 23 | Image grade | Runtime CSS filter + filter transitions on ~20 media | **Grade baked into exported WebP/AVIF**; hover = scale + 18 % overlay fading to 0 (opacity only) | must-fix (judge 3) |
| 24 | Hero video | 12421166 (muddy under grade) | **29374299** (blue-hour interchange, red light trails). Phones: poster only | judge 2 |
| 25 | Forms | Select of 11 | + „Kita“, pre-fill from `?domina=` (Fluent Forms `{get.domina}`), „Kopijuoti“ next to the e-mail | graft C |
| 26 | Split-flap | Everywhere incl. stubs | Board only; desktop only, once, fixed tile widths (no CLS), never phone numbers, never under reduced motion, sr-only copy | must-fix |
| 27 | Pinned services | ~3.2 screens, no escape | Skip link „Praleisti paslaugų juostą“, visible „Visos paslaugos sąrašu →“, focus scrolls the track, unpinned below 620 px height, compact ≤760 px height | must-fix |
| 28 | Photos | 7464393 avoided; 35531295, 15885602, 19274366 used | Also excluded: **38404178** (third-party truck branding), all ferry media (route unconfirmed), 12421166, Vilnius media (implies an office), map-with-pins photos | honesty |
| 29 | Custom code budget | CSS 5 KB + JS 6 KB | Production **CSS ≈ 7 KB, JS ≈ 4 KB** (all enhancements; the site is complete without them) | must-fix (<6 KB JS) |
| 30 | Handoff | — | `data-salient` on every block + **Salient žymės** toggle in the demo | graft C |

### 0.2 Not adopted (and why)
- **Color Change Section** (page background morphing on scroll): echoes v1's banned hero colour morph (judge 1). Chapters change with hard edges and the rail carries continuity.
- **Text With Inline Media / images inside headlines**: v1 move.
- **Scrolling Text marquee** anywhere, including the phone ticker: v1 move and phone-chrome budget.
- **Interactive Map (Leaflet)**: a street map with pins implies depots/addresses the company does not publish. The schematic + Image With Hotspots does the job.
- **Lottie route**: not needed; the CSS-only SVG draw has no dependency and no After Effects work. Lottie Scroll Position Seek remains an optional fallback (§3.8).
- **Coordinates / projection names / day codes**: pseudo-precision the audience does not need.

---

## 1. Concept, principles, difference from v1

### 1.1 Concept
The site is one trip: **Lithuania → Ireland or Spain → and back.** A red "lane" (2 px centre stroke between two 1 px side rails — the parallel lines of the SGP logo mark) runs down the left margin of every chapter and **draws itself as you scroll**, stopping at a **waypoint ring** for each chapter (Apie mus → Paslaugos → Maršrutai → Kelionėje → Kelionės eiga → Prieš siunčiant → Siuntos sekimas → **Atvykimas** = contact). The information layer reads like a **departure hall**: a dark board with split-flap date tiles, light timetables with full dates, and ticket-stub contact cards that pair each phone line with the next departure. In between, **cinematic blue-hour road footage** is graded cold so the red lane is the only warm thing on screen. Light chapters sit on **map paper** (a hairline graticule), dark chapters on **asphalt**.

**The audience's three questions are answered on every page and every device:** *When is the next run?* (ticker/board/next-line, relative status „po 4 d.“) · *Can I call a real person now?* (two direct-dial buttons, switchboard with all 5 numbers, equal-weight mobile call bar, tap-to-call schedule rows) · *What am I allowed to send?* (rules chapter with counts, fines table, per-service prohibited lists).

### 1.2 Principles (apply to every new page or block)
1. **Phone first, literally.** A `tel:` action is never more than one tap away; both directions always have equal weight.
2. **Only true facts.** Numbers only if derivable from the content (2 kryptys, 11 paslaugų, 3–4 paros, 4 šalys pakeliui). No fleet size, years, clients, reviews, awards, logos, address, company code. Unknowns are shown as unknown („maršrutas tikslinamas“, „Grafikas atnaujinamas – skambinkite“).
3. **The lane explains, it does not decorate.** Every line is a route, a timeline or a list of stops.
4. **Red is a signal, not a fill.** ≤ ~5 % of any viewport; brand red for lines/rings/CTA fills/large type; tinted reds for small text.
5. **Readable for parents on phones.** Min 12 px text, 16 px body on phones, sentence-case headings, full dates in words.
6. **Native first.** Everything must look complete with Salient elements only; custom code is progressive enhancement (§5.4).
7. **Motion with meaning, and optional.** Every effect has a reduced-motion state (§5.5); nothing loops for more than ~5 s without a control.
8. **Lithuanian typography.** `lang="lt"`, latin-ext fonts, „…“ quotes, en dash with spaces for routes („Lietuva – Airija“), no auto-hyphenation.

### 1.3 What makes v2 different from v1 (every v1 signature replaced, not recoloured)

| v1 (banned) | v2 „Maršruto linija“ |
|---|---|
| Warm beige `#EFEDE8` + yellow `#FFC21A` | Cold asphalt `#0F1417` + map paper `#F5F7F6` with a hairline graticule; brand red `#EF4539` is the only accent; no yellow anywhere |
| Inter Tight 800, ALL CAPS | Barlow Condensed 600 sentence case + Barlow + IBM Plex Mono labels |
| Giant centred stacked „SAUGIAI / GREITAI / PATIKIMAI“ | Left-aligned route H1 „Lietuva ●—● Airija. / Lietuva ●—● Ispanija. / Ir atgal.“ docked above a departure board; slogan only in running text |
| Hero background colour morph on scroll | Hero keeps its video; the only scroll-linked device is the lane. No Color Change Section anywhere |
| Video card scaling up under the hero | Departure board docked inside the hero |
| Rotating circular text badge | None. Waypoint rings with one halo when reached |
| Full-width service rows + cursor-following image | Horizontal pinned "road" of 11 cards hanging from a lane of stops (home); pinned stacking groups (overview page) |
| Word-by-word lit "about" statement on black | About on light map paper, route names underlined by a drawn red line, datasheet, odometer stats |
| Two tall parallax route cards | Tabbed route schematic on graticule + timetable + phones |
| Outlined/solid giant marquee | No marquee anywhere; desktop ticker is static text |
| 4 white "step" cards (Užklausa → Pasiūlymas → Kelionė → Pristatymas) | 3 stations on a lane (Paėmimas → Kelyje apie 3–4 paras → Pristatymas) + labelled facts |
| Yellow rounded CTA with pill checkboxes | „Atvykimas“ terminus: two ticket-stub cards (perforation + notches) + boxed mono-label form |
| Giant footer wordmark | Footer with the 11 services as a line of stops; no wordmark |
| Pills (99 px), 22 px rounded cards | 2 px radii, hairlines, square icon cells, 50 % only on rings |

### 1.4 Signature device budget
Kept: **(1) rail + rings, (2) departure board (flap) + light timetable, (3) tickets, (4) map-paper graticule.** Minor: H1 route dash, odometer numerals, crop marks (only the about cascade back image and the route-panel image). Cut: coordinates, projection caption, degree labels, day codes, ferry leg, marquees.

---

## 2. Tokens

### 2.1 Ready-to-paste `:root` (identical in `kryptis-A.html`, `v2/assets/css/sgp.css` and Salient → Theme Options → Custom CSS)

```css
@property --sgp-p{syntax:'<percentage>';inherits:false;initial-value:100%}
:root{
  /* colour · surfaces */
  --c-asphalt-950:#0B0E10; --c-asphalt-900:#0F1417; --c-asphalt-800:#161D21; --c-asphalt-750:#1A2227;
  --c-asphalt-700:#222B30; --c-asphalt-600:#2E383E;
  --c-paper-50:#F5F7F6; --c-paper-100:#EAEEED; --c-paper-200:#D9DFDE; --c-paper-300:#C3CBCB; --c-white:#FFFFFF;
  /* colour · text */
  --c-ink:#1C1D1D; --c-ink-2:#4A5358; --c-snow:#F2F4F3; --c-fog:#9AA6AB;
  /* colour · brand signal */
  --c-signal:#EF4539; --c-signal-ink:#C4301E; --c-signal-lit:#F4604F;
  --c-signal-soft:rgba(239,69,57,.14); --c-signal-rail:rgba(239,69,57,.42);
  /* colour · lines & overlays */
  --c-hair-d:rgba(242,244,243,.12); --c-hair-d-2:rgba(242,244,243,.26);
  --c-hair-l:rgba(28,29,29,.12); --c-hair-l-2:rgba(28,29,29,.26);
  --c-ghost-d:rgba(242,244,243,.28); --c-ghost-l:rgba(28,29,29,.28);
  --c-graticule:rgba(28,29,29,.055);
  --c-glass:rgba(11,14,16,.74); --c-scrim:rgba(11,14,16,.55);
  --c-hdr-d:rgba(15,20,23,.74); --c-hdr-l:rgba(245,247,246,.86);
  --c-grade:rgba(15,20,23,.18);
  /* fonts */
  --f-display:"Barlow Condensed","Arial Narrow",sans-serif;
  --f-text:"Barlow",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  /* type scale (fluid 360 → 1440 px) */
  --fs-d1:min(clamp(2.5rem,1rem + 4.6vw,5.75rem),10.5vh);
  --fs-d2:clamp(2.125rem,1.35rem + 2.9vw,4.25rem);
  --fs-statement:clamp(1.75rem,1.15rem + 2vw,3rem);
  --fs-h3:clamp(1.5rem,1.25rem + 1vw,2.25rem);
  --fs-h4:1.375rem;
  --fs-stat:clamp(3.25rem,2.3rem + 4vw,6.5rem);
  --fs-phone:clamp(1.875rem,1.45rem + 1.5vw,2.75rem);
  --fs-lead:clamp(1.0625rem,1rem + .3vw,1.25rem);
  --fs-body:1.0625rem; --fs-small:.9375rem; --fs-label:.75rem;
  --fs-board:clamp(1rem,.92rem + .25vw,1.125rem);
  --lh-display:.94; --lh-heading:1; --lh-lead:1.5; --lh-body:1.62; --lh-label:1.35;
  --ls-display:-.012em; --ls-label:.08em;
  /* spacing (4 px base) */
  --sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-5:24px; --sp-6:32px; --sp-7:48px; --sp-8:64px; --sp-9:96px; --sp-10:128px; --sp-11:168px;
  --gutter:clamp(16px,4vw,56px); --container:1320px; --col-gap:24px;
  --section-y:clamp(80px,10vw,160px);
  --rail-zone:0px; --rail-x:27px;
  /* radii · shadows */
  --r-0:0; --r-1:2px; --r-ring:50%;
  --sh-lift:0 30px 60px -28px rgba(11,14,16,.55);
  --sh-panel:0 30px 70px -30px rgba(0,0,0,.7);
  --sh-bar:0 -12px 30px -12px rgba(0,0,0,.6);
  /* z-index */
  --z-rail:1; --z-raise:2; --z-sticky:20; --z-callbar:50; --z-scrim:55; --z-menu:58; --z-header:60; --z-devtags:90; --z-skip:200;
  /* motion */
  --e-route:cubic-bezier(.65,0,.35,1); --e-arrive:cubic-bezier(.16,1,.3,1);
  --e-hover:cubic-bezier(.3,.7,.4,1); --e-std:cubic-bezier(.215,.61,.355,1);
  --d-micro:160ms; --d-hover:320ms; --d-panel:450ms; --d-reveal:900ms; --d-draw:900ms; --d-section:1300ms; --d-odo:1600ms;
  --st-word:60ms; --st-hero:90ms; --st-row:90ms; --st-card:120ms; --st-flap:42ms;
  /* chrome heights */
  --h-ticker:0px; --h-hdr:68px; --h-hdr-s:64px; --h-callbar:58px;
}
@supports (height:1svh){:root{--fs-d1:min(clamp(2.5rem,1rem + 4.6vw,5.75rem),10.5svh)}}
@media (min-width:1000px){:root{--rail-zone:72px;--h-hdr:84px;--h-ticker:34px}}
@media (max-width:690px){:root{--fs-body:1rem;--col-gap:16px}}

/* surfaces — Salient: Row → Text Color Light (= .on-dark) / Dark (= .on-light) */
.on-dark{--bg:var(--c-asphalt-900);--fg:var(--c-snow);--fg-2:var(--c-fog);--hair:var(--c-hair-d);--hair-2:var(--c-hair-d-2);
  --ghost:var(--c-ghost-d);--red-text:var(--c-signal-lit);--card:var(--c-asphalt-800);--card-h:var(--c-asphalt-750);
  background-color:var(--bg);color:var(--fg)}
.on-light{--bg:var(--c-paper-50);--fg:var(--c-ink);--fg-2:var(--c-ink-2);--hair:var(--c-hair-l);--hair-2:var(--c-hair-l-2);
  --ghost:var(--c-ghost-l);--red-text:var(--c-signal-ink);--card:var(--c-white);--card-h:var(--c-paper-100);
  background-color:var(--bg);color:var(--fg)}
.on-light.alt{--bg:var(--c-paper-100)}
.paper{background-image:linear-gradient(var(--c-graticule) 1px,transparent 1px),linear-gradient(90deg,var(--c-graticule) 1px,transparent 1px);
  background-size:112px 112px;background-position:50% 0}
```

In WordPress the surface classes are applied as Row Extra Class `sgp-dark` / `sgp-light` (same declarations, prefixed) in addition to Salient's Row Text Color, because Salient's Text Color drives the transparent header but not our custom properties.

### 2.2 Fonts
**Exact link (demo `<head>`, after two `preconnect`s to `fonts.googleapis.com` and `fonts.gstatic.com` crossorigin):**
```html
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=Barlow:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```
The css2 API returns separate `@font-face` blocks per subset with `unicode-range`; **latin-ext is included** for all three families (verified 2026-09-23: blocks `/* latin-ext */` for Barlow 400/500/600, Barlow Condensed 500/600, IBM Plex Mono 400/500). latin-ext covers ą č ę ė į š ų ū ž (U+0100–024F); „ “ – are in the latin block (U+2000–206F).

**Production:** Theme Options → Typography → *Local Google Fonts* ON (self-hosts the same files; latin + latin-ext woff2 only). Preload only **Barlow Condensed 600 (latin)** and **Barlow 400 (latin)**; the latin-ext files load on demand through `unicode-range` as soon as a Lithuanian letter appears (they are small).

| Salient Typography slot | Family / weight | Size | LH | LS |
|---|---|---|---|---|
| Heading 1 | Barlow Condensed 600 | `var(--fs-d1)` | .94 | −.012em |
| Heading 2 | Barlow Condensed 600 | `var(--fs-d2)` | .98 | −.008em |
| Heading 3 | Barlow Condensed 600 | `var(--fs-h3)` | 1.02 | 0 |
| Heading 4 | Barlow Condensed 600 | 22 px | 1.05 | 0 |
| Heading 5/6 | Barlow 600 | 17 / 15 px | 1.3 | 0 |
| Body | Barlow 400 | 17 px (16 px ≤690) | 1.62 | 0 |
| Navigation | Barlow 500 | 15 px | 1 | 0 |
| Buttons | Barlow 600 | 16 px (15 small) | 1 | .01em |
| Mono labels | IBM Plex Mono 500 via Extra Class `.sgp-mono` (custom CSS; do not hijack a Salient slot) | 12 px | 1.35 | .08em UPPERCASE |

Fluid Typography ON. `html{hyphens:manual}`; headings never all caps; min display line-height .94 (diacritics above caps).

### 2.3 Type roles

| Role | Token / font | 360 px → 1440 px | Case | Used for |
|---|---|---|---|---|
| D1 hero | `--fs-d1` Barlow Condensed 600 | 40 → 82 px (capped at 10.5svh; 92 px max) | Sentence | Home H1 only |
| D2 section | `--fs-d2` BC 600 | 34 → 68 px | Sentence | Chapter H2, inner-page H1 uses `calc(var(--fs-d2)*1.1)` |
| Statement | `--fs-statement` BC 500 | 28 → 48 px | Sentence | About statement, closing lines |
| H3 | `--fs-h3` BC 600 | 24 → 36 px | Sentence | Cards, panels |
| Stat | `--fs-stat` BC 500, tabular | 52 → 104 px | — | Milestones |
| Phone big | `--fs-phone` BC 600 | 30 → 44 px | — | Ticket numbers |
| Lead | `--fs-lead` Barlow 400 | 17 → 20 px | Sentence | Intros |
| Body | 17 px / 16 px ≤690 | — | Sentence | Paragraphs |
| Small | 15 px | — | Sentence | Card summaries, captions, footer links |
| Label | 12 px Plex Mono 500 +.08em | — | UPPERCASE, ≤ 4 words | Waypoints, chips, field labels, board direction |
| Board tile | `--fs-board` Plex Mono 500 | 16 → 18 px | UPPERCASE | Flap tiles only |

**Floor:** no rendered text under **12 px** at any width (SVG text included: map labels are 15 px in a 700-unit viewBox, which renders ≥ 12.8 px at the smallest map width of 597 px).

### 2.4 Surfaces, contrast and the red budget

| Pair | Ratio | Allowed use |
|---|---|---|
| snow on asphalt-950 / 900 / 800 / 750 | 17.5 / 16.8 / 15.4 / 14.6 | all text |
| fog on 950 / 900 / 800 / 750 / 700 | 7.8 / 7.4 / 6.8 / 6.5 / 5.8 | secondary text, placeholders |
| ink on paper-50 / 100 / white | 15.7 / 14.4 / 16.9 | all text |
| ink-2 on paper-50 / 100 / 200 | 7.3 / 6.7 / 5.8 | secondary text, "tikslinama" line |
| **signal #EF4539** on 950 / 900 | 5.2 / 4.9 | text OK on these two only |
| signal on 800 / 750 / 700 | 4.5 / 4.3 / 3.8 | **no small text** → use signal-lit |
| **signal-lit #F4604F** on 800 / 750 / 700 | 5.4 / 5.1 / 4.6 | small red text on dark cards/tiles |
| signal on paper-50 / white | 3.5 / 3.8 | **lines, rings, ≥24 px text only** |
| **signal-ink #C4301E** on paper-50 / 100 / white | 5.2 / 4.7 / 5.5 | small red text on light |
| asphalt-900 on signal | 4.9 | text on red buttons |
| white / snow on signal | 3.8 / 3.4 | only ≥ 19 px bold / 24 px regular (avoid) |

Rules
- Sections alternate dark/light; each Salient Row sets Text Color (drives the header) **and** `sgp-dark|sgp-light`.
- Red budget: brand red covers ≤ ~5 % of any viewport (hero: two 64 px icon cells + a 2 px lane ≈ 1 %). Never a red section background, never red body text.
- No gradients except image overlays; no glow, no yellow, no purple.
- Unreached rings are neutral (`currentColor` at 45 %); red appears only for reached / active / terminus / CTA.

### 2.5 Spacing, grid, rail zone
- 4 px base; scale `--sp-1…11` = 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 168.
- Section padding `--section-y` = clamp(80, 10vw, 160) px (Salient Row padding desktop 160 / tablet 112 / phone 80).
- Container 1320 px (Salient container width 1320, Extended Responsive ON), gutter `--gutter` clamp(16, 4vw, 56) px, 12 columns, gap 24 px (16 px ≤690).
- **Rail zone:** ≥1000 px every content container has `padding-left:72px`; the lane centre is 27 px inside it. <1000 px zone = 0 (no global rail).
- Rhythm inside a chapter: waypoint → 28–56 px → H2 → 14–22 px → lead → 48–64 px → content.

### 2.6 Radii, borders, shadows, z-index
- Radii: 0 media, **2 px** buttons/inputs/chips/cards/tiles, 50 % rings only. No pills.
- Borders: 1 px hairlines (`--c-hair-d` / `--c-hair-l`); 1 px solid `--fg` for data tops (kv, timetable, stats); 1 px dashed for perforation and "tikslinama".
- Shadows: `--sh-lift` (cascade front image, raised ticket), `--sh-panel` (switchboard), `--sh-bar` (mobile call bar). Dark UI otherwise uses border changes.
- Z: rail 1 · raised 2 · sticky submenu 20 · call bar 50 · scrim 55 · menu 58 · header 60 · dev tags 90 · skip link 200. The switchboard is a `popover` (top layer, above everything).

### 2.7 Iconography
Line icons, 24 px grid, 1.6 px stroke, round caps/joins, `currentColor`. Set (SVG sprite in the tile): phone, arrow, menu, close, pause, play, mail, copy, calendar, reclining seat, heated seat, air (A/C), shield-check, clock (rest), box, route, paw, download. Salient: **Icon** element (Iconsmind/Linea closest glyph) in a 44 px square outlined cell; where no glyph exists (heated/reclining seat) upload the sprite's SVG as an Image. No emoji, no filled flaticons.

### 2.8 Image treatment
- **Production grade is baked** into the exported files (Lightroom/Photoshop preset "SGP cold": saturation −20, contrast +6, exposure −0.1 EV, highlights cool +4). Export WebP (AVIF optional) at 480/760/1100/1600/1920 w; photos ≤ 180 KB at 1600 w.
- **Demo:** Pexels URLs with a static CSS filter stand-in `filter:saturate(.8) contrast(1.06) brightness(.92)` (no filter transitions).
- **Hover** (both): image `scale(1.08 → 1.13)` 1100 ms `--e-arrive` + an 18 % asphalt overlay (`<i class="ov">` / Column overlay) fading to 0 in 900 ms. Opacity/transform only.
- Overlays: hero = left→right `#0F1417` 88 % → 60 % @42 % → 14 % @80 %, plus top→bottom 60 % → 0 @24 % → 12 % @60 % → 92 % @100 %. Cinematic rows = top/bottom fade to `#0F1417`, 30–35 % middle, left 75 % → 10 %. Textures = `#0F1417` at 86–90 %.
- Fixed aspect ratios per slot (4:5 portrait, 4:3 inset, 16:11 card, 16:10 panel, 16:9 cinematic, 1:1 circle 80 px).
- Crop marks only on: about cascade back image, route-panel image.

### 2.9 Salient global settings (Theme Options)
Material skin · Accent `#EF4539`; Extra Color 1 `#0F1417`, Extra 2 `#F5F7F6`, Extra 3 `#C4301E` · Overall background `#F5F7F6`, body text `#1C1D1D` · Button Styling: Slightly Rounded (2 px) · Header: **Centered Menu**, Permanent Transparent, Hide Until Needed, Resize On Scroll (84 → 64), Header BG blur, Link Hover **Animated Underline** (accent), Navigation Entrance Fade In 200 ms · Off Canvas **Fullscreen Split** with Global Section content · **Smooth Scrolling ON (Lenis), strength 50** · Column/Image Animation Easing **easeOutExpo**, Timing **1300 ms** · Page Builder Element Animations On Mobile: **OFF** (element-level exceptions noted) · **View Transitions: Horizontal Gradient Wipe**, disabled on mobile · Lightbox fancyBox3 · Fluid Typography ON, Local Google Fonts ON · Disable Parallax Backgrounds On Mobile ON · Disable Video Backgrounds On Mobile ON · Back To Top OFF (call bar replaces it) · Footer = Global Section, Footer Reveal OFF · Delay JavaScript Execution ON **with `sgp-*.js` excluded**.

---

## 3. Signature graphic system (how to draw each element)

All code below is production CSS/JS (Theme Options → Custom CSS / Custom JS, or `sgp.css`/`sgp.js` enqueued by a 20-line mu-plugin). Class names are `sgp-` prefixed in WordPress; the tile uses the unprefixed equivalents (`has-rail` = `sgp-has-rail`, etc.).

### 3.1 Kelio juosta — the rail (CSS only)
Geometry: 14 px wide lane = 1 px side rail (`--c-signal-rail`) at x 0 and x 13, 2 px centre stroke (`--c-signal`) at x 6, dashed ghost (1 px, 4 on / 6 off, `--ghost`) at x 6.5 showing the *planned* route. Travelled part = 0 → 100 % of the row height, from **row top at 72 % of the viewport** to **row bottom at 72 %**.

```css
/* Row → Extra Class: sgp-has-rail · Row Type: Full Width Background (row box = viewport width) */
.sgp-has-rail{position:relative;view-timeline:--sgp-rail block}
.sgp-has-rail::before{content:"";position:absolute;top:0;bottom:0;width:14px;z-index:1;pointer-events:none;display:none;
  left:calc(max(var(--gutter),(100% - var(--container)) / 2) + var(--rail-x) - 7px);
  background:
    linear-gradient(var(--c-signal),var(--c-signal)) 6px 0/2px var(--sgp-p) no-repeat,
    linear-gradient(var(--c-signal-rail),var(--c-signal-rail)) 0 0/1px var(--sgp-p) no-repeat,
    linear-gradient(var(--c-signal-rail),var(--c-signal-rail)) 13px 0/1px var(--sgp-p) no-repeat,
    repeating-linear-gradient(to bottom,var(--ghost) 0 4px,transparent 4px 10px) 6.5px 0/1px 100% no-repeat}
.sgp-has-rail > .row_col_wrap_12{padding-left:var(--rail-zone)}      /* content moves out of the rail zone */
.sgp-has-rail.sgp-rail-end::before{bottom:auto;height:var(--rail-end,170px)} /* Atvykimas: stops at the terminus */
@media (min-width:1000px){.sgp-has-rail::before{display:block}}
@supports (animation-timeline:view()){
  .sgp-has-rail::before{animation:sgp-rail linear both;animation-timeline:--sgp-rail;
    animation-range:entry-crossing 28vh entry-crossing calc(100% + 28vh)}
}
@keyframes sgp-rail{from{--sgp-p:0%}to{--sgp-p:100%}}
@media (prefers-reduced-motion:reduce){.sgp-has-rail::before{animation:none;--sgp-p:100%}}
```
- `--sgp-p` is a registered property with initial value 100 %, so **unsupported browsers (Firefox today) show the lane fully drawn**. Chrome/Edge 115+ and Safari 26+ scrub it.
- `--rail-end` for GS-Arrival is set once on load/resize by 2 lines of JS (distance from row top to the terminus ring centre); without JS the lane stops at 170 px.
- **Staging check (required):** confirm `.wpb_row::before` is not used by Salient on these rows (inspect computed styles). If it is, move the rule to `.sgp-has-rail > .row-bg-wrap::after` (same declarations; `.row-bg-wrap` is full-bleed and sits under the content).
- The pinned services row does **not** carry the rail; its waypoint ring sits in the rail zone and its lane of stops continues horizontally (§3.4).

### 3.2 Stotelė — the ring
16 px circle, 2 px border. States: **laukia** (border `currentColor` 45 %, fill = section bg) · **aktyvi** (border red, no fill) · **pasiekta** (fill + border red, one 1 px halo scaling .5 → 1.7 and fading .9 → 0) · **galas/terminus** (22 px, 3 px border, filled when reached).
```css
.sgp-ring{--s:16px;width:var(--s);height:var(--s);border-radius:50%;border:2px solid color-mix(in srgb,currentColor 45%,transparent);
  background:var(--bg);position:relative;display:inline-block;flex:none;transition:background-color .45s var(--e-arrive),border-color .45s var(--e-arrive)}
.sgp-ring::after{content:"";position:absolute;inset:-7px;border-radius:50%;border:1px solid var(--c-signal);opacity:0;transform:scale(.5)}
.sgp-ring--fill,.is-reached>.sgp-ring{border-color:var(--c-signal);background:var(--c-signal)}
.sgp-ring--term{--s:22px;border-width:3px;border-color:var(--c-signal)}
/* waypoint rings fill when they cross 72 % of the viewport (CSS only) */
@supports (animation-timeline:view()){
  .sgp-wp .sgp-ring{view-timeline:--wp block;animation:sgp-reach linear both;animation-timeline:--wp;animation-range:cover 28vh cover calc(28vh + 1px)}
  .sgp-wp .sgp-ring::after{animation:sgp-halo linear both;animation-timeline:--wp;animation-range:cover 28vh cover calc(28vh + 180px)}
}
@supports not (animation-timeline:view()){.sgp-wp .sgp-ring{border-color:var(--c-signal);background:var(--c-signal)}}
@keyframes sgp-reach{from{border-color:color-mix(in srgb,currentColor 45%,transparent);background:var(--bg)}to{border-color:var(--c-signal);background:var(--c-signal)}}
@keyframes sgp-halo{from{opacity:.9;transform:scale(.5)}to{opacity:0;transform:scale(1.7)}}
```

### 3.3 Waypoint label (chapter head)
Markup (Salient Text Block, Extra Class `sgp-wp-block`):
```html
<p class="sgp-wp"><span class="sgp-ring"></span><span class="sgp-mono sgp-wp__no">01</span><span class="sgp-mono">Apie mus</span><span class="sgp-wp__rule"></span><span class="sgp-mono sgp-wp__meta">LT ⇄ IE · LT ⇄ ES</span></p>
```
`display:flex; gap:14px; align-items:center`; number in `var(--red-text)` (signal-ink on light, signal-lit on dark — fixes the 3.5:1 failure); rule `flex:1; height:1px; opacity:.16`; meta in `--fg-2`. ≥1000 px the ring is absolutely placed on the rail: `left: calc(-1 * var(--rail-zone) + var(--rail-x) - 8px)` (terminus −11 px). Meta values are short facts only (e.g. „11 paslaugų“, „2 kryptys“, „Apie 3–4 paros“) — never coordinates.

### 3.4 Horizontal stops (services lane)
Each card (Horizontal Scrolling child, Extra Class `sgp-stop`) has a 30 px top zone holding: ring at (22, 0), 14 px stem (hairline → red when reached), and a lane segment from its ring to the next card's ring.
```css
.sgp-stop{--gap:28px;position:relative;padding-top:30px}
.sgp-stop::before,.sgp-stop::after{content:"";position:absolute;left:38px;top:2px;height:12px;width:calc(100% + var(--gap) - 16px);pointer-events:none}
.sgp-stop::before{background:repeating-linear-gradient(90deg,var(--c-ghost-d) 0 4px,transparent 4px 10px) 0 5.5px/100% 1px no-repeat}
.sgp-stop::after{border-top:1px solid var(--c-signal-rail);border-bottom:1px solid var(--c-signal-rail);
  background:linear-gradient(var(--c-signal),var(--c-signal)) 0 4px/100% 2px no-repeat;transform:scaleX(0);transform-origin:left;transition:transform .6s var(--e-route)}
.sgp-stop.is-reached::after{transform:scaleX(1)}
@media (max-width:999px){ /* Salient stacks the children: the lane turns vertical on the left */
  .sgp-stop::before,.sgp-stop::after{left:-32px;top:40px;width:12px;height:calc(100% - 16px)}
  .sgp-stop::before{background:repeating-linear-gradient(to bottom,var(--c-ghost-d) 0 4px,transparent 4px 10px) 5.5px 0/1px 100% no-repeat}
  .sgp-stop::after{border:0;border-left:1px solid var(--c-signal-rail);border-right:1px solid var(--c-signal-rail);
    background:linear-gradient(var(--c-signal),var(--c-signal)) 4px 0/2px 100% no-repeat;transform:scaleY(0);transform-origin:top}
  .sgp-stop.is-reached::after{transform:scaleY(1)}
}
```
JS (production, ≈0.5 KB) — no reading of Salient internals:
```js
(()=>{const s=[...document.querySelectorAll('.sgp-stop')];if(!s.length)return;const n=document.querySelector('[data-sgp-count]');
const io=new IntersectionObserver(es=>{es.forEach(e=>{const r=e.boundingClientRect,R=e.rootBounds||{left:0,top:0};
  e.target.classList.toggle('is-reached',e.isIntersecting||r.right<R.left||r.bottom<R.top)});
  if(n)n.textContent=String(Math.max(1,s.filter(x=>x.classList.contains('is-reached')).length)).padStart(2,'0')},{rootMargin:'0px -30% -30% 0px'});
s.forEach(x=>io.observe(x))})();
```
Reduced motion: `.sgp-stop::after{transform:none}` (all drawn). **Prototype on real Salient 18.3 Horizontal Scrolling markup on staging before sign-off** (IO sees transformed positions; verify on Chrome, Safari, Firefox).

### 3.5 Išvykimų lenta — dark board + split-flap
Board = Inner Row (`Backdrop filter blur 16px`, bg `--c-glass`, top hairline) holding GS-Board. Head: title „Artimiausi pervežimai“ (BC 600 24 px) · note „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“ (15 px fog) · link „Visas grafikas →“. Grid of 4 cells (2×2 at 691–999, 1 column ≤480).

**Cell markup contract** (shortcode output; the whole cell is a `tel:` link):
```html
<a class="sgp-bcell is-soonest" href="tel:+34602547929" aria-label="Ispanija – Lietuva: rugsėjo 27 d., spalio 14 ir 28 d. Skambinti +34 602 547 929">
  <p class="sgp-bcell__dir sgp-mono" aria-hidden="true"><span class="sgp-dot"></span>Artimiausias</p>   <!-- otherwise „Iš Lietuvos“ / „Į Lietuvą“ -->
  <p class="sgp-bcell__name" aria-hidden="true">Ispanija → Lietuva <svg class="sgp-i">…phone…</svg></p>
  <p class="sgp-bnext" aria-hidden="true"><span class="sgp-flap">27 RUGS.</span></p>
  <p class="sgp-bdate" aria-hidden="true"><time datetime="2026-09-27">Rugsėjo 27 d.</time> <span>· po 4 d.</span></p>
  <p class="sgp-blater" aria-hidden="true">Vėliau: spalio 14 ir 28 d.</p>
</a>
```
Cell styles: padding 13/20/15 px; name BC 600 20 px; date line Barlow 500 15 px; later line 14 px fog (hidden ≤760 px height); soonest = 2 px red top edge, flap digits in signal-lit, dot pulses 2 cycles (M15). Hover: bg +3.5 % white, phone icon → red (M45).

**Flap tiles:** each character is a fixed-width tile `width:.9em;height:1.42em;background:var(--c-asphalt-750);border-radius:2px` with a 1 px black split line at 50 %; spaces are `.4em` transparent. Fixed widths = no layout shift.
```js
/* sgp-flap.js ≈0.8 KB — desktop only, once, never under reduced motion, never on phone numbers */
(()=>{if(matchMedia('(prefers-reduced-motion: reduce)').matches||!matchMedia('(min-width:1000px)').matches)return;
const CH='ABCDEFGHIJKLMNOPRSTUVZĄČĘĖĮŠŲŪŽ0123456789';
document.querySelectorAll('.sgp-flap').forEach(el=>{const t=el.textContent.trim();el.textContent='';
  const sr=document.createElement('span');sr.className='sgp-sr';sr.textContent=t;el.append(sr);
  [...t].forEach(c=>{const s=document.createElement('span');s.setAttribute('aria-hidden','true');s.className=c===' '?'sgp-fc sp':'sgp-fc';s.textContent=c;s.dataset.c=c;el.append(s)});
  new IntersectionObserver(([e],o)=>{if(!e.isIntersecting)return;o.disconnect();
    el.querySelectorAll('.sgp-fc:not(.sp)').forEach((s,i)=>{let n=4+Math.floor(Math.random()*4);
      setTimeout(function k(){if(n-->0){s.textContent=CH[Math.random()*CH.length|0];setTimeout(k,55)}else s.textContent=s.dataset.c},i*42)})}).observe(el)})})();
```
Native fallback (no JS): plain text in the same tiles style is not possible without JS → the plain text is shown in Plex Mono with a 1 px bottom hairline (still reads as a board). Alternative native: Animated Text → *Single letter from bottom: Reveal*.

### 3.6 Light timetable row (tap-to-call)
```html
<li><a class="sgp-tt__row" href="tel:+37065053161" aria-label="Lietuva – Airija: spalio 9 ir 23 d. Skambinti +370 650 53161">
  <span class="sgp-tt__k sgp-mono" aria-hidden="true">Iš Lietuvos</span>
  <span class="sgp-tt__v" aria-hidden="true"><time datetime="2026-10-09" class="is-next">Spalio 9 d.</time><time datetime="2026-10-23">Spalio 23 d.</time></span>
  <span class="sgp-tt__call" aria-hidden="true">…phone icon…</span></a></li>
```
Grid `112px 1fr 20px`, min-height 48 px, 1 px ink top rule on the list, hairline between rows. Next date: signal-ink, 600, 8 px red dot before it. Past dates are removed (not struck). Hover/focus: bg ink 4 % + 8 px indent (400 ms `--e-arrive`), icon → signal-ink. Inbound row labels: „Iš Airijos“ / „Iš Ispanijos“; inbound rows dial +353 86 450 3104 / +34 602 547 929.

### 3.7 Map paper and crop marks
```css
.sgp-graticule{background-image:linear-gradient(var(--c-graticule) 1px,transparent 1px),linear-gradient(90deg,var(--c-graticule) 1px,transparent 1px);background-size:112px 112px;background-position:50% 0}
.sgp-crop{position:relative}
.sgp-crop::before,.sgp-crop::after{content:"";position:absolute;width:14px;height:14px;border:1px solid currentColor;opacity:.55;z-index:3;pointer-events:none}
.sgp-crop::before{top:-8px;left:-8px;border-right:0;border-bottom:0}
.sgp-crop::after{bottom:-8px;right:-8px;border-left:0;border-top:0}
```
Graticule on light chapters only (never on forms or the dense stacked lists). Crop marks only on the two slots listed in §2.8.

### 3.8 Route schematic (SVG, CSS-only draw)
`viewBox="0 0 700 500"`, placed inside a framed `<figure class="sgp-map">` (1 px `--c-hair-l`, bg paper 70 %, padding 18 px, `view-timeline:--map block`). One SVG **per tab** (Airija, Ispanija), because Salient Tabs toggle `display` and CSS animations restart on display — that is how the branch redraws on tab switch with no JS.

| Node | x, y | Label (15 px Plex Mono 500, +.08em) |
|---|---|---|
| Lietuva (origin) | 624, 64 | „LIETUVA“ + „išvykimas“ (x 604 end-anchored) |
| Lenkija | 542, 140 | „LENKIJA“ |
| Vokietija | 376, 161 | „VOKIETIJA“ |
| Belgija | 267, 175 | „BELGIJA“ |
| Prancūzija | 227, 270 | „PRANCŪZIJA“ |
| Ispanija (terminus) | 116, 416 | „ISPANIJA“ + „atvykimas“ |
| Airija (terminus) | 37, 111 | „AIRIJA“ + „atvykimas“ |

Paths: **trunk** `M624 64 L542 140 L376 161` (both tabs) · **ES branch** `M376 161 L267 175 L227 270 L116 416` · **IE leg** `M376 161 L37 111` drawn as `stroke: var(--c-ink-2); stroke-width:1.6; stroke-dasharray:6 7` (neutral, never red), with label „maršrutas tikslinamas“ at (118, 112) rotated 8.4°. Cased red line = three stacked strokes: 12 px `rgba(239,69,57,.45)`, 9 px paper, 2.6 px red, each `pathLength="1"`. Inactive branch/terminus at 35 % opacity; inactive base path `--c-paper-300` 2.5 px. Stops: 5.5 r, paper fill, 2 px ink stroke. Termini 8.5 r, 2.6 px red stroke, filled red on the active tab. Origin: 9 r red + 14 r pulse ring (2 iterations). Graticule lines every 92/118 units, **no degree labels**. Caption „Maršrutų schema · ne mastelis“; legend „Maršrutas“ (red line) · „Tikslinama“ (dashed) · „Šalis pakeliui“ (ring).
```css
.sgp-map .live path{fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1 1;stroke-dashoffset:0}
@supports (animation-timeline:view()){
  .sgp-map .live.trunk path{animation:sgp-draw linear both,sgp-draw .9s var(--e-route) backwards;animation-timeline:--map,auto;animation-range:entry 10% cover 40%,normal}
  .sgp-map .live.branch path{animation:sgp-draw linear both,sgp-draw .9s var(--e-route) .35s backwards;animation-timeline:--map,auto;animation-range:cover 32% cover 52%,normal}
}
@keyframes sgp-draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
```
<700 px the SVG is hidden and an ordered list replaces it (vertical red line, rings): Airija = „Lietuva (išvykimas) · Lenkija · Vokietija · Maršrutas tikslinamas (dashed segment) · Airija (atvykimas)“; Ispanija = „Lietuva · Lenkija · Vokietija · Belgija · Prancūzija · Ispanija“. SVG has `role="img"`, `<title>` and `<desc>` („Iš Lietuvos per Lenkiją ir Vokietiją; tolesnė maršruto dalis iki Airijos tikslinama.“ / „Iš Lietuvos per Lenkiją, Vokietiją, Belgiją ir Prancūziją į Ispaniją.“).
**Staging check:** if Salient 18.3 hides inactive tabs without `display:none`, add a 5-line listener on `.tabbed > ul a` that re-adds a `sgp-redraw` class. **Optional fallback:** Lottie element, trigger *Scroll Position Seek*, separate desktop and phone JSON. **Static fallback** (and /tarptautiniai-pervezimai/ primary): the same drawing exported as SVG image inside **Image With Hotspots**.

### 3.9 Bilietas — ticket stub
Two-column card (`1fr 200px`), bg `--c-asphalt-800`, dashed 1 px perforation (22 % snow) between body and stub, two 11 px semicircular notches cut by mask:
```css
.sgp-ticket{--stub:200px;--n:11px;display:grid;grid-template-columns:1fr var(--stub);background:var(--c-asphalt-800);
  -webkit-mask:radial-gradient(circle var(--n) at calc(100% - var(--stub)) 0,#0000 98%,#000) top/100% 51% no-repeat,radial-gradient(circle var(--n) at calc(100% - var(--stub)) 100%,#0000 98%,#000) bottom/100% 51% no-repeat;
          mask:radial-gradient(circle var(--n) at calc(100% - var(--stub)) 0,#0000 98%,#000) top/100% 51% no-repeat,radial-gradient(circle var(--n) at calc(100% - var(--stub)) 100%,#0000 98%,#000) bottom/100% 51% no-repeat}
@media (max-width:699px){.sgp-ticket{--stub:0px;grid-template-columns:1fr;-webkit-mask:none;mask:none}}
```
Body: mono code „LT ⇄ IE“ (signal-lit) + label „Pervežimai į Airiją“; big number (`--fs-phone`, phone icon red); secondary numbers (16 px Barlow with 12 px mono country code), each ≥44 px tall. Stub: label „Kitas išvykimas“ (short, never wraps in the 200 px stub), **full date** („Spalio 9 d.“, BC 600 28 px), direction + relative („iš LT · po 16 d.“, 12 px mono fog), link „Skambinti →“. ≤699 px the stub goes under the body with a horizontal dashed perforation, notches removed. Salient: Inner Row with 2 Columns (Extra Class `sgp-ticket`), stub Column border-left dashed.

### 3.10 H1 route dash (Raw HTML)
```html
<h1 class="sgp-h1-route">
  <span class="sgp-sr">Tarptautiniai pervežimai: Lietuva – Airija, Lietuva – Ispanija ir atgal</span>
  <span class="row" aria-hidden="true"><span class="w"><span style="--i:0">Lietuva</span></span><span class="dash" style="--i:1"><i></i></span><span class="w"><span style="--i:2">Airija.</span></span></span>
  <span class="row" aria-hidden="true"><span class="w"><span style="--i:3">Lietuva</span></span><span class="dash" style="--i:4"><i></i></span><span class="w"><span style="--i:5">Ispanija.</span></span></span>
  <span class="row row--back" aria-hidden="true"><span class="w"><span style="--i:6">Ir</span></span><span class="w"><span style="--i:7">atgal.</span></span></span>
</h1>
```
Dash = `.9em × .6em` box: origin ring (left, 2 px red border, bg asphalt) → lane (`clamp(8px,.12em,12px)` high, 1 px rails + 2 px centre) → destination ring (right, filled red). Row 3 in fog. The complete CSS is in the tile (`.h1`, `.dash` rules). Native fallback: Animated Text *Word Reveal* of „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“ with the keyword sentence in the page title/meta.

### 3.11 Odometer numerals
Salient **Milestone**, Animation Effect *Motion Blur Slide In*, delays 0/150/300/450 ms, 4 cells with 1 px `--fg` top rule and a 28×3 px red "kilometre marker". „3–4“ = Milestone "None" + Animated Text. Demo: digit reels (`translateY(-n em)` 1600 ms `--e-arrive` + blur 3 px → 0).

### 3.12 Datasheet (`dl.sgp-kv`)
```css
.sgp-kv{display:grid;grid-template-columns:minmax(120px,11rem) 1fr;border-top:1px solid var(--fg)}
.sgp-kv dt,.sgp-kv dd{margin:0;padding:12px 0;border-bottom:1px solid var(--hair)}
.sgp-kv dt{font:500 .75rem/1.5 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--fg-2);padding-top:14px}
.sgp-kv dd{font-size:.9375rem;line-height:1.45}
@media (max-width:480px){.sgp-kv{grid-template-columns:1fr}.sgp-kv dt{border-bottom:0;padding-bottom:0}}
```
Salient: Text Block containing the `<dl>` (Extra Class on the Text Block). Rows fade up with 60 ms stagger (M27).

---

## 4. Components (exact states)

State columns: **D** default · **H** hover (fine pointers) · **F** `:focus-visible` (always 2 px `--c-signal` outline, 3 px offset unless noted) · **A** active/pressed · **X** disabled.

### 4.1 Header (Global)
| Part | Spec |
|---|---|
| Ticker (≥1000 px only) | 34 px, asphalt-950, bottom hairline. Left: red dot + „Artimiausi išvykimai“ (12 px mono, signal-lit). Items (Barlow 500 14 px, fog; route bold snow): „**Ispanija → Lietuva** rugsėjo 27 d. · po 4 d.“ — max 3, sorted by date, first in signal-lit; items that do not fit are hidden (never truncated). Right: „Visas grafikas →“. Collapses to 0 when scrolled (M05). Salient: GS-Ticker in *In Navigation Top (Before Scrolling)*, content `[sgp_grafikas variant="ticker" limit="3"]`. |
| Transparent state | Height 84 px (68 px <1000). logo_light.svg 112×46 (alt „SGP pervežimai“). Nav centred: Apie mus · Pervežimo paslaugos (mega menu) · Pervežimų grafikas · Siuntos sekimas · Taisyklės · Kontaktai (Barlow 500 15 px). Right: Signal button small „Skambinti“ (phone icon). |
| Scrolled (y > 40) | 64 px, `--c-hdr-d` + blur 14 px + bottom hairline; over light rows `--c-hdr-l`, ink text, logo.svg (M02, M04). |
| Hide until needed | Hides on scroll-down after 360 px; returns on scroll-up; never hides while the switchboard or menu is open (M03). |
| Nav link | D: snow/ink · H/F: 2 px red underline grows from left 450 ms `--e-arrive`, shrinks to the right on leave · current page: underline stays (`aria-current="page"`). |
| Mega menu „Pervežimo paslaugos“ | Salient Mega Menu, 3 columns, asphalt-950, 2 px red top: 6 group headings (12 px mono fog) with their services (Barlow 15 px; H: red-lit + 3 px nudge). Groups = §6.3. Last row: „Tarptautiniai pervežimai →“, „Visos paslaugos →“. |
| <1180 px | Nav hidden; burger (44 px outlined) visible. |
| <1000 px | Logo · red 44 px phone button (opens the switchboard sheet) · burger. No ticker. |
| Salient | Header layout Centered Menu; Permanent Transparent; Hide Until Needed; Resize On Scroll; BG blur; Animated Underline; every Row sets Text Color. One H1 per page (the logo carries none). |

### 4.2 Switchboard „Skambinti“ (native popover)
- Markup lives once, site-wide, in GS-CallBar as Raw HTML: `<div id="sgp-call" class="sgp-callpanel" popover aria-label="Telefono numeriai">…</div>`.
- Content: group „Pervežimai į Airiją“ → rows LT +370 650 53161 · IE +353 86 450 3104 · UK +44 7566 878681; group „Pervežimai į Ispaniją“ → LT +370 638 28919 · ES +34 602 547 929; e-mail saugiai.greitai.patikimai@gmail.com. Each row `min-height:44px`, BC 600 21 px, 12 px mono country code, full `aria-label` („Pervežimai į Airiją, Lietuvos numeris +370 650 53161“).
- ≥1000 px: 360 px dropdown under the header's right edge (`top` = header bottom + 8 px), asphalt-950, 2 px red top, `--sh-panel`; open: opacity 0→1 + translateY −6→0, 350 ms (M07). <1000 px: full-width **bottom sheet** (translateY 100 % → 0), scrim `--c-scrim`, close button (44 px), safe-area padding.
- Row states: D snow · H/F signal-lit + 6 px indent + arrow slides in · A: native call.
- Triggers: `<button popovertarget="sgp-call">` in the demo. In Salient the "Skambinti" menu item (Menu Item Button Style, URL `#sgp-call`) + 5-line JS: `document.querySelectorAll('a[href="#sgp-call"]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();document.getElementById('sgp-call').togglePopover()}))`. Esc and outside click close natively; focus returns to the trigger.
- Mobile header phone button: Salient menu item button with *show on mobile* if available in 18.3; otherwise the same item exposed in the mobile header by 6 lines of CSS (verify on staging).

### 4.3 Off-canvas menu (Salient Off Canvas → Fullscreen Split)
Left (1.2 fr, asphalt-950): ordered list as a line diagram — 2 px red vertical lane draws top→bottom 900 ms `--e-route` (M08); items: ring + 12 px mono number + BC 600 `clamp(2rem,1.4rem+2.6vw,3.4rem)`: 00 Pradžia · 01 Apie mus · 02 Pervežimo paslaugos · 03 Tarptautiniai pervežimai · 04 Pervežimų grafikas · 05 Siuntos sekimas · 06 Taisyklės · 07 Kontaktai (terminus ring filled). Items rise 14 px, 60 ms stagger. H/F: signal-lit, +8 px, ring fills. Right (asphalt-900, GS-Menu): both phone groups + e-mail. <1000 px single column, scrolls as one sheet; Lenis paused while open; focus moves to the first item; Esc closes and returns focus to the burger.

### 4.4 Buttons
| Type | D | H | F | A | X | Salient |
|---|---|---|---|---|---|---|
| **Signal** (primary) | 52 px (small 44), red fill, asphalt-900 text, 2 px radius; label cell + 52 px arrow cell split by a 22 % hairline | on dark → snow fill; on light → asphalt-900 fill + snow text; arrow exits right and re-enters (550 ms) | outline in `--fg` (not red on red) | translateY(1px) | 40 % opacity, no pointer | Button → Arrow Animation; bg Accent; text Extra 1; hover bg custom |
| **Line** | transparent, 1 px border currentColor 38 % | border red, fill currentColor 7 % | red outline | 1 px down | 40 % | Button → See Through |
| **Text link** („Skaityti daugiau“) | 13 px mono uppercase, 1 px underline 30 %, 44 px tall hit area | 2 px red underline grows left→right 500 ms, arrow +4 px | outline + underline shown | — | 40 % | Button → Underline |
| **Call button** | 64 px: 64 px red icon cell + mono label („Pervežimai į Airiją“) over BC 600 24 px number; glass bg (blur 10) + hairline | whole button red, text asphalt, icon cell asphalt with red icon (320 ms) | outline | native call | — | Button Basic + `.sgp-callbtn` (backdrop blur native) |
| **Call button small** | 56 px variant, number 21 px | same | same | — | — | same |
| **Icon button** | 44×44, 1 px border currentColor 30 %; red variant filled | border red (red variant → snow fill) | outline | — | — | Header/menu buttons |
| **Copy** („Kopijuoti“) | 44 px, 1 px border 26 %, 12 px mono + copy icon | border red | outline | label → „Nukopijuota“ (signal-lit) for 2.4 s, `role=status` announces „El. pašto adresas nukopijuotas“ | — | Raw HTML + 8-line JS |

### 4.5 Links in text
Inline links: underline 1 px at 40 % (`text-underline-offset:3px`), H: underline 2 px signal (dark) / signal-ink (light), text unchanged. Visited = same. `tel:` and `mailto:` links always show the full number/address as text.

### 4.6 Chips
12 px mono uppercase, +.06em, 7×9 px padding, 1 px `--hair`, 2 px radius, `--fg-2`. Link chips (service child routes): H border red + text `--fg`; F outline.

### 4.7 Service card (home horizontal route)
Width `clamp(290px,24vw,360px)`, 28 px gap, hangs from the lane (§3.4). Card: asphalt-800, 1 px hairline; image 16:11 (max `min(27vh,250px)`, 20vh at ≤760 px height); body 20/22 px: mono „01 / 11“ (number signal-lit), H3, one-line summary (15 px fog), 2 chips, 44 px square arrow cell. Whole card = one link (Column Link).
- H: card translateY −6 px (550 ms), border red 55 %, bg asphalt-750, image scale 1.13 + overlay 0, H3 1 px underline draws (600 ms), arrow cell fills red, ring fills. Cards 02, 05, 06: muted SD video fades in over the photo (M33).
- F: same as hover + 4 px outline offset. Reached (IO): ring red + stem red + lane segment drawn.
- <1000 px list row: 96 px thumbnail left, „01 / 11 →“, H3 23 px, summary; chips/arrow cell hidden; no lift; vertical lane.
- End card: „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“ (NEW) + two small call buttons „Į Airiją +370 650 53161“ / „Į Ispaniją +370 638 28919“.
- Salient: Sticky Content Sections → **Horizontal Scrolling** (section width 26vw, effect None, Subtract Navigation Height ON, desktop only); child = Column Link (bg `#161D21`, hover bg `#1A2227`, border 1 px) + Image (hover Zoom In Crop) + Text Block + chips + Icon.

### 4.8 Group stack card (/pervezimo-paslaugos/)
Full-width card (min-height 70vh desktop), 5/7 split: image (4:5, overlay) | content: mono index „01 / 06“, group H2 (NEW group name), list of its services as rows (H3 24 px + one-line summary + arrow; each row a link, H: row bg 4 %, arrow slides, title signal-ink/lit). Stacking: previous card scales 1 → .94 and dims to 60 % (M63). Left sticky index (≥1000 px) lists the 6 groups; active group ring filled; click = anchor.

### 4.9 Route tabs + route panel
Tabs = Salient **Tabs → Toggle Button** (2 tabs, deep links `#airija` / `#ispanija`), styled: 1 px ink outline, 3 px inner padding, 44 px buttons „Airija IE“ / „Ispanija ES“; selected = ink fill, paper text; unselected H = ink 7 %. Keyboard ← → switches (native in Salient; demo emulates). Tab content (Inner Row): map 7/12 + info 5/12 (≥1280); map 12/12 + info in 2 columns (1000–1279); stacked below. Info: 16:10 image with crop marks (H: scale 1.04, overlay 0), H3 „Lietuva – Airija – Lietuva“, timetable (§3.6, 2 rows), kv „Kelyje — apie 3–4 paros nuo paėmimo dienos“, phone group list. Panel switch: fade + 14 px rise 600 ms (M40); branch redraw (M42).

### 4.10 Schedule rows (three variants, one data source)
| Variant | Where | Layout | States |
|---|---|---|---|
| `board` | Home hero, GS-Board (Paslaugos, Taisyklės, service pages) | §3.5 | H bg +3.5 %, icon red; F outline; A native call |
| `timetable` | Route panels, Kontaktai | §3.6 | H bg 4 % + indent 8 px; F outline |
| `table` | /pervezimu-grafikas/ | full-width rows grouped „Iš Lietuvos“ / „Į Lietuvą“: col 1 route name BC 600 28 px + code (mono); col 2 all upcoming full dates as a wrapping list (next = signal-ink + dot); col 3 status „po N d.“ (mono; soonest „● Artimiausias“); col 4 number + phone icon (right). ≤690 px stacks: name/icon, dates, number | H: bg 4 %, 2 px red left lane grows (scaleY, 400 ms); F outline; A call |
Empty state (no future dates for a route): row text „Grafikas atnaujinamas – skambinkite“, row still dials. All past → the board shows 4 such rows; the ticker shows „Grafikas atnaujinamas · skambinkite“.

### 4.11 Next-departure line (phones)
Only <1000 px, placed under the H1 on home and under the lead on inner heroes: box with 1 px `--c-hair-d-2` border, 3 px red left edge, glass bg; row 1 = 12 px mono „● Artimiausias išvykimas“; row 2 = Barlow 500 16 px „**Ispanija → Lietuva** rugsėjo 27 d. · po 4 d.“ (relative in signal-lit). Whole box links to /pervezimu-grafikas/. Source: `[sgp_grafikas variant="next"]`.

### 4.12 Data blocks
- **Stats** (§3.11): only 2 · 11 · 3–4 · 4 with captions (NEW): „Airija ir Ispanija – iš Lietuvos ir atgal“, „tarptautinių pervežimo paslaugų“, „paros nuo paėmimo dienos“, „šalys: Lenkija, Vokietija, Belgija, Prancūzija“. Labels: „Kryptys“, „Paslaugos“, „Kelyje“, „Pakeliui“.
- **Datasheet** (§3.12). **Delivery facts** (always this pair where parcel delivery time is mentioned): `Kelyje — apie 3–4 paros nuo paėmimo dienos` / `Įsipareigojimas siuntoms — per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklių 3.4 p.)`.

### 4.13 Rules components
- **Toggle panels** (Salient Toggle Panels → Minimal Shadow, restyled): 1 px hairline rows, 12 px mono index, title BC 600 22 px with count in fog („Draudžiama siųsti (12)“), "+" replaced by a 12 px ring that fills when open; accordion; deep links; open 450 ms `--e-arrive` (M60).
- **✕ list** (prohibited items): 2 columns ≥691 px, each item = 12 px ✕ ring (1 px `--fg-2`) + text 15 px; stagger 40 ms when the panel opens (M62).
- **Fines table** (Taisyklių 4.5 p.): `dl.sgp-kv` 5 rows, value „1200 EUR“ in BC 600 24 px signal (large-text rule) + qualifier 15 px. Rows in §6.8.
- **Callout „Svarbu“**: 3 px red left bar, `--card` bg, 12 px mono label „Svarbu“, 17 px text.
- **Clause** (Taisyklės page): number („3.4.“) 12 px mono red-text, text 17 px max 68ch, hairline between clauses.

### 4.14 Forms (Fluent Forms; demo = no submission)
Field: `--card`-coloured box (asphalt-800 on dark; white on light with 1 px `--c-hair-l-2`), 1 px border, 2 px radius, min-height 58 px (textarea 110 px). Label **inside the box, always visible**, 12 px mono uppercase at (14, 10); input Barlow 500 16 px; placeholder in fog (≥ 4.5:1).
| State | Spec |
|---|---|
| D | border `--hair` |
| H | border `--hair-2` |
| F (`:focus-within`) | border red, 3 px red lane grows on the left edge (scaleY 0→1, 400 ms), label signal-lit/ink, bg asphalt-750 (dark) / white (light) |
| Error | border red, label red-text, message 13 px under the value (`aria-invalid="true"`, `aria-describedby`) |
| X | 45 % opacity, no pointer |
| Success | form stays; a status box (3 px red left bar) appears under the button: „Jūsų žinutė sėkmingai išsiųsta“ + demo note „Demonstracinė versija – duomenys niekur nesiunčiami.“ (NEW); it receives focus and is announced (`role="status"`, `aria-live="polite"`) |
Quote form (GS-Arrival): „Jūsų vardas“ · „Telefono numeris“ · „El. pašto adresas“ · „Kas Jus domina?“ (select: „Pasirinkite paslaugą“ + 11 services + „Kita“; default from `?domina=` → Fluent `{get.domina}`) · „Žinutė“ (min 20; placeholder „Iš kur, į kur ir kada?“) · consent note „Formoje pateikti duomenys naudojami susisiekimui su klientu.“ · Signal button „Gauti pasiūlymą“. Errors (NEW): „Įrašykite vardą“, „Įrašykite telefono numerį“, „Patikrinkite el. pašto adresą“, „Pasirinkite paslaugą“, „Žinutė – bent 20 simbolių“. Live fail/captcha messages verbatim: „Oi kažkas ne taip! Bandykite dar kartą.“, „Įveskite teisingą apsaugos kodą.“ Production spam protection: Cloudflare Turnstile (invisible) instead of reCAPTCHA v2.
Contact form (/kontaktai/): „Jūsų vardas“ · „El. pašto adresas“ · „Žinutės tema“ · „Žinutė“ (min 20) · button „Siųsti“.
Demo JS: `checkValidity()` per field on submit, first invalid gets focus, errors clear on input, success box on valid. Nothing is sent anywhere.

### 4.15 Tracking field
Inline form: one field (label „Siuntos kodas“, placeholder „Siuntos kodas...“, Plex Mono 18 px, 58 px) + Signal button „Siuntos lokacija“. Home strip submits `GET /siuntos-sekimas/?kodas=…`; the tracking page sets the iframe `src="https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=<urlencoded>"`. Empty submit → field error „Neįvestas siuntos kodas!“ (verbatim from the tool).

### 4.16 Breadcrumbs
```html
<nav class="sgp-crumbs" aria-label="Kelias"><ol>
  <li><a href="/">Pradžia</a></li><li><a href="/pervezimo-paslaugos/">Pervežimo paslaugos</a></li>
  <li><a href="/pervezimo-paslaugos/tarptautiniai-pervezimai/">Tarptautiniai pervežimai</a></li>
  <li aria-current="page">Krovinių pervežimas</li></ol></nav>
```
13 px Barlow 500 (not mono — long Lithuanian names), fog/ink-2; separators = CSS `::before` 24 px lane segment (1 px, 45 %) + 7 px ring; current item snow/ink with a filled red ring. H: link underline. ≤690 px shows only the parent + current (earlier items collapse to „…“ link to the root). Salient: Rank Math breadcrumb shortcode in a Text Block, Extra Class `sgp-crumbs` (Rank Math → breadcrumbs separator empty).

### 4.17 Inner page hero („Maršruto antraštė“)
Row Full Width, min-height 62svh (≥1000) / auto (≤999: content + 120 px top), content bottom-left: breadcrumb → H1 (D2 × 1.1, Animated Text Word Reveal, 90 ms stagger) → lead (max 60ch) → chips → next-line (<1000). Right column ≥1000: compact call ticket (both LT numbers as small call buttons, or the service's direction numbers). Background: graded photo or video, **Parallax Subtle** + **Slight Zoom Out Reveal** (M80), overlay as hero. Text Color Light. Variants: *photo* (default), *video* (tarptautiniai), *texture* (grafikas: 9807331 at 18 %), *plain* (kontaktai, privatumo: asphalt-900 + graticule at 4 % white).

### 4.18 Page Submenu (service pages)
Salient **Page Submenu**, Sticky, below the header (top 64 px), bg `--c-hdr-l` + blur 12 px, bottom hairline, height 52 px; links 12 px mono uppercase: „Apie paslaugą · Privalumai · Kliento atsakomybės · Draudžiami daiktai · Užklausa“ (per-service labels in §6.5). Active: signal-ink + 2 px red underline. Horizontal scroll on phones (no wrap), current link scrolled into view.

### 4.19 „Kita stotelė“ band
Full-width Column Link, asphalt-900, 18vh min: mono „Kita stotelė · 02“ (NEW label) → H2 next service name → arrow cell. Column BG image = next service hero at opacity 0 → .35 on hover (Column BG *Hover Opacity*), a 2 px lane draws across the band (scaleX 0→1, 900 ms `--e-route`) (M82). F: outline inset.

### 4.20 „Atvykimas“ CTA (GS-Arrival)
Terminus waypoint („Atvykimas“) → H2 „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“ → 7/12 two tickets (§3.9) + e-mail row (label „El. paštas“, address, „Kopijuoti“) | 4/12 quote form (§4.14). Tickets fade up 0/120 ms; H: lift −4 px, bg asphalt-750, perforation turns red (M70). Background texture 7024783 at 12 % + Parallax Subtle. Hidden on /kontaktai/, /privatumo-politika/, 404.

### 4.21 Footer (GS-Footer)
asphalt-950, 5 columns (1.3 / 1 / 1 / 1.2 / 1), padding-top clamp(64,7vw,104):
1. logo_light.svg 128×52 + „Visos pervežimo paslaugos: Lietuva – Airija – Lietuva, Lietuva – Ispanija – Lietuva. Saugiai, greitai, patikimai.“ (NEW composite) + „El. paštas“ saugiai.greitai.patikimai@gmail.com.
2. „Pervežimai į Airiją“: LT +370 650 53161 · IE +353 86 450 3104 · UK +44 7566 878681.
3. „Pervežimai į Ispaniją“: LT +370 638 28919 · ES +34 602 547 929.
4. „Tarptautiniai pervežimai“: the 11 services as a line of stops (1 px asphalt-600 line, 9 px rings; H/F ring fills red, link +3 px, text snow).
5. „Informacija“: Apie mus · Pervežimų grafikas · Siuntos sekimas · Taisyklės · Kontaktai · Privatumo politika.
Bottom bar (hairline): „© 2026 SGP pervežimai. Visos teisės saugomos.“ · „↑ Į pradžią“. No wordmark, no social links (none exist), no address/company code. Phone numbers are `tel:` with the display format above; `href` values: `+37065053161`, `+353864503104`, `+447566878681`, `+37063828919`, `+34602547929`. ≤999 px 2 columns (brand full width), ≤699 px 1 column.

### 4.22 Mobile call bar (GS-CallBar, <1000 px)
Fixed bottom, 58 px + safe area, `--sh-bar`, grid `1fr 1fr 58px`, 1 px gaps: [phone icon red] „Į AIRIJĄ“ (12 px mono fog) over „+370 650 53161“ (BC 600 15 px) · same for „Į ISPANIJĄ“ „+370 638 28919“ · calendar icon → /pervezimu-grafikas/ (`aria-label="Pervežimų grafikas"`). **Both call cells identical** (asphalt-950, red icon). A: bg asphalt-800. Visible from load; body gets `padding-bottom: 58px + safe-area`. Salient: Row → Sticky Row: Bottom of Window, device visibility tablet + phone, inside GS-CallBar (verify Sticky Row inside a Global Section on staging; fallback = 12 lines `position:fixed` CSS).

### 4.23 Testimonials placeholder
Dashed 1 px `--hair-2` frame, 12 px mono „Atsiliepimai“, text „Čia bus tikri klientų atsiliepimai“ + „Vieta rezervuota – išgalvotų atsiliepimų nenaudojame.“ (both NEW). Demo: visible on home only. Production: Row **disabled** until real reviews; then Testimonial Slider → Minimal. No stars, names or quotes invented.

### 4.24 Cookie bar
Consent plugin (Complianz or CookieYes) restyled: bottom-left card, max 420 px (above the call bar on phones), asphalt-950, 2 px red top. Title verbatim „Informuojame, kad šioje svetainėje naudojami slapukai (angl. cookies)“; text **NEW** (the verbatim "naršykite toliau" implied consent is not GDPR-valid) „Būtini slapukai reikalingi svetainei veikti. Analitikos slapukus naudosime tik gavę Jūsų sutikimą.“; buttons „Sutinku“ (Signal small), „Atmesti“ (Line small), „Plačiau“ (text link → /privatumo-politika/). Non-essential cookies off until consent; GA4 via GTM Consent Mode v2. Demo: shown once, remembered in `localStorage` (wrapped in try/catch).

### 4.25 Video control
Mono 12 px button with pause/play icon, 44 px tall: „Pauzė“ ↔ „Leisti“ (`aria-pressed`). Hero: bottom-right above the board. Cinematic rows: in the chapter footer. Hidden <1000 px (videos are posters there). Required by WCAG 2.2.2.

### 4.26 Image With Hotspots (Keleivių pervežimas)
Image 36377055 (16:10 desktop, 4:5 phone), 4 numbered markers (28 px, red fill, asphalt number, Nectar pulse), tooltip on hover/tap (asphalt-950, 1 px hairline, 15 px): 1 „Atlenkiamos sėdynės – patogiai Jūsų kelionei tiek dieną, tiek naktį“ · 2 „Šildomos sėdynės – komfortui net žvarbiausiomis žiemos dienomis“ · 3 „Kondicionierius – kad oras autobuse visada būtų šviežias“ · 4 „Keleiviai apdrausti – Kelionės metu visi keleiviai yra apdrausti.“. Caption (12 px mono): „Iliustracinė nuotrauka“ (NEW) — replace with the client's own interior photo before launch; markers positioned on seats (1, 2), ceiling vent area (3), centre (4).

### 4.27 Developer overlay „Salient žymės“ (demo only)
Fixed bottom-left button (above the call bar <1000 px, hidden ≤690 px), 12 px mono; toggles `aria-pressed` and appends a label with each element's `data-salient` value (asphalt tag, red border, 12 px mono). Every Row, Inner Row, component and custom block in the demo carries `data-salient="Element → option · option"`.

---

## 5. Motion system

### 5.1 Rules
- Easing: `--e-arrive` for anything entering, `--e-route` for anything drawing (lanes, maps, underlines), `--e-hover` for hover colour/position. Durations: micro 160 · hover 320 · panel 450 · reveal 900 · draw 900 · section 1300 · odometer 1600 ms.
- Entrance trigger: element top at 88 % of viewport (Salient default); demo uses IntersectionObserver `rootMargin:0 0 -12% 0`.
- Scroll-linked effects use the **72 % line** (row/ring crosses 72 % of the viewport height).
- Phones: Salient entrance animations off by default; exceptions noted (H1 word reveal, lanes).
- No infinite loops > ~5 s except background videos (which have a pause control): every pulse stops within ~5 s (2 cycles).

### 5.2 Effect catalogue
| Id | Effect | Trigger | From → to | Duration / easing / stagger | Salient mapping | Demo implementation | Reduced motion |
|---|---|---|---|---|---|---|---|
| M01 | Smooth scroll | wheel | native → lerp .1 | continuous | Theme Options → Smooth Scrolling (Lenis), strength 50 | Lenis 1.1.13 `new Lenis({lerp:.1,smoothWheel:true})` + rAF | not initialised |
| M02 | Header resize + glass | scrollY > 40 | 84 → 64 px, bg transparent → `--c-hdr-d/l` + blur 14 | 400 ms `--e-arrive` | Resize On Scroll + BG blur | rAF scroll loop toggles `.is-scrolled` | instant |
| M03 | Header hide/show | scroll down > 360 px / up | translateY 0 ↔ −100 % | 500 ms `--e-arrive` | Hide Until Needed | same loop (5 px threshold) | instant |
| M04 | Header recolour | row under header changes | light ↔ dark logo/text | 350 ms | Permanent Transparent (Row Text Color) | probe row at y 32/60 px | instant |
| M05 | Ticker collapse | scrollY > 40 | 34 → 0 px, opacity 1 → 0 | 400 ms | GS In Navigation Top (native) | class toggle | instant |
| M06 | Nav underline | hover/focus | scaleX 0 → 1 (origin left), leave to right | 450 ms `--e-arrive` | Header Link Hover: Animated Underline | CSS | colour only |
| M07 | Switchboard | click | opacity 0→1, y −6→0 (desktop) / y 100 %→0 (sheet) | 350 ms `--e-arrive` | Raw HTML popover | `popover` + `@starting-style` | instant |
| M08 | Menu open | burger | fade 0→1; lane scaleY 0→1; items y 14→0 | 350 / 900 `--e-route` / 700 ms, stagger 60 ms | Off Canvas Fullscreen Split (+ custom CSS lane) | class toggle | instant |
| M09 | Page transition | navigation | horizontal gradient wipe (asphalt) | 600 ms | View Transitions: Horizontal Gradient Wipe, off on mobile | `@view-transition{navigation:auto}` + `::view-transition-new(root){animation:clip-path inset(0 100% 0 0)→inset(0)}` | none |
| M10 | Hero video parallax | scroll | translateY 0 → 18vh over 0 → 100vh scroll (≈ .18×) | linear | Row Parallax BG: **Subtle** | CSS `animation-timeline:scroll(root)` | static |
| M11 | H1 word rise | load | translateY 108 % → 0 (masked) | 1150 ms `--e-arrive`, stagger 90 ms, start 100 ms | Raw HTML H1 (custom CSS); fallback Animated Text Word Reveal | `.ready` class after 2 rAF | static |
| M12 | H1 dash draw | load | origin ring scale 0→1 (+550 ms); lane scaleX 0→1 (+700 ms); destination ring 0→1 (+1450 ms) | 500 / 900 `--e-route` / 500 ms | custom CSS | CSS transitions | drawn |
| M13 | Fade up | enter viewport | opacity 0→1, y 26→0 | 900/1100 ms `--e-arrive`; hero lead +700, calls +850 ms | Column/element Animation: Fade In From Bottom | IO adds `.in` | visible |
| M14 | Split-flap | board enters (hero: +700 ms after load) | 4–7 random chars at 55 ms, settle | stagger 42 ms/char; once; desktop only | custom `sgp-flap.js`; fallback Animated Text Single letter Reveal | same script | final text |
| M15 | Live dot | load | opacity 1 → .25 → 1 | 2.4 s × 2 cycles | custom CSS | CSS | static |
| M16 | Background video | row within 200–300 px of viewport | load + play; pause when out | — | Row Video BG (lazy); Disable Video BG on mobile | IO; `<1000px` poster only; saveData = poster | poster + „Leisti“ |
| M20 | Rail draw | scroll | lane 0 → 100 % of row height (row top@72 % → bottom@72 %) | scrubbed | custom CSS `.sgp-has-rail` (view-timeline) | same CSS | drawn |
| M21 | Waypoint reach | ring crosses 72 % | ring fill neutral → red; halo scale .5→1.7, opacity .9→0 over 180 px | scrubbed | custom CSS | same CSS | filled, no halo |
| M22 | Heading word reveal | enter | words y 105 % → 0 (masked) | 1000 ms `--e-arrive`, stagger 60 ms | Animated Text → Word Reveal | JS splits words + IO | static |
| M23 | Underline draw | enter | background-size 0 → 100 % × 3 px | 1400 ms `--e-route`, 2nd +500 ms | Highlighted Text → Regular Underline | CSS on `.in` | drawn |
| M24 | Mask reveal image | enter | clip-path inset(100% 0 0 0) → inset(0) | 1300 ms `--e-arrive`; 2nd layer +250 ms | Column Animation: Mask Reveal (straight, bottom) / Cascading Images Grow In Reveal | IO on the parent | visible |
| M25 | Cascade parallax | scroll | front layer y +14 % → −14 % across the view | scrubbed | Cascading Images → parallax | CSS view-timeline | static |
| M26 | Odometer | enter | digit reels y 0 → −n em; blur 3 px → 0 | 1600 ms `--e-arrive`, stagger 150 ms | Milestone → Motion Blur Slide In | IO + CSS | final number |
| M27 | Staggered cards/rows | enter | fade up 26 px | 900 ms, stagger 120 ms (cards) / 60–90 ms (rows) | Column delays 0/120/240/360 | IO + `--dl` | visible |
| M30 | Pinned horizontal track | scroll through section | translateX 0 → −overflow | scrubbed | Sticky Content Sections → Horizontal Scrolling (desktop) | sticky + rAF translateX (demo emulation only); off <1000 px width or <620 px height | horizontal scroll-snap list |
| M31 | Stop reached | card enters left/top 70 % | segment scaleX/Y 0→1; ring + stem red | 600 ms `--e-route` | custom IO (§3.4) | same | all drawn |
| M32 | Service card hover | pointer | y 0→−6; border → red 55 %; image 1.08→1.13; overlay → 0; H3 underline; arrow cell red | 550 / 1100 / 600 / 350 ms | Column Link bg hover + Image Zoom In Crop + custom CSS | CSS | colour only |
| M33 | Hover video | first pointerenter (fine pointer) | video opacity 0→1 | 500 ms | custom 12-line JS | same | never |
| M34 | Services counter | stops reached | „01“ → „11“ | instant | custom (same IO) | same | final |
| M40 | Tab switch | click / ← → | panel opacity 0→1, y 14→0 | 600 ms `--e-arrive` | Tabs → Toggle Button, content animation Fade | ARIA tabs emulation | instant |
| M41 | Map trunk draw | map scroll (entry 10 % → cover 40 %) | stroke-dashoffset 1 → 0 | scrubbed | Raw HTML SVG + CSS | same CSS | drawn |
| M42 | Branch redraw | tab shown (display toggle) | dashoffset 1 → 0 | 900 ms `--e-route`, +350 ms | same CSS (animation restarts on display) | same | drawn |
| M43 | Origin pulse | load | ring scale .6→2.2, opacity .9→0 | 2.6 s × 2 | CSS | CSS | static |
| M44 | Image hover | pointer | scale +4–5 %, overlay 18 %→0 | 1100 / 900 ms | Image hover Zoom In Crop | CSS | none |
| M45 | Row hover | pointer/focus | bg 3.5–4 %, indent 0→8 px, icon → red | 400 ms `--e-arrive` | Horizontal List Item (Border Animation) + custom CSS | CSS | colour only |
| M50 | Cinematic parallax | scroll | video y −11 % → +11 % (media box 128 %) | scrubbed | Row Parallax BG: **Medium** | CSS view-timeline | static |
| M51 | BG slow zoom | row enters | scale 1.12 → 1 | 12 s linear | Row BG Layer Animation: Zoom Out Slowly | CSS | static |
| M52 | Word blur heading | enter | blur 10→0, opacity 0→1, y 10→0 | 1100 ms, stagger 70 ms | Animated Text → Word: Blur | JS split + IO | static |
| M53 | Comfort lane | scroll (cover 22 % → 48 %; phones per item 72 %) | lane scaleX 0→1; stop i activates at 22 % + i × 6.5 % | scrubbed | Icon List + custom CSS `.sgp-stops` | CSS view-timeline | drawn/active |
| M55 | Process lane | enter | Divider draws 0 → 100 %; rings fill 400 ms + i × 350 ms | 1200 ms `--e-route`, delay 200 ms | Divider (line animation) + Column delays | IO + CSS | drawn |
| M56 | Circle reveal | enter | clip-path circle(0) → circle(50 %) | 900 ms cubic-bezier(.2,.8,.2,1), stagger 120 ms | Image Mask Circle + Column Mask Reveal (circle) | IO + CSS | visible |
| M60 | Toggle open | click | height 0 → auto; ring fill | 450 ms `--e-arrive` | Toggle Panels → Minimal Shadow | `<details>`-style JS | instant |
| M61 | Sticky column | scroll | CSS sticky top 120 px | — | Column → Sticky Content (CSS, Top) | `position:sticky` | same |
| M62 | ✕ stagger | panel opens | opacity 0→1, x −6→0 | 300 ms, 40 ms stagger | custom CSS nth-child delays | CSS | visible |
| M63 | Stacking cards | scroll | previous card scale 1→.94, opacity 1→.6 | scrubbed | Sticky Scroll Pinned Sections → **Stacking** | sticky + CSS view-timeline | plain stack |
| M64 | Sticky media swap | text block enters | media crossfade + scale 1.06→1 | 700 ms | Sticky Content Sections → Sticky Media, Scrolling Content | IO swaps `.is-active` | crossfade only |
| M65 | Overlapping chapters | scroll | next chapter slides over the pinned one | scrubbed | Sticky Scroll Pinned Sections → **Overlapping** | sticky stacking | plain stack |
| M66 | Scroll scale image | scroll | scale .88→1, y 40→0 px | scrubbed | Column → Scroll Position Advanced | CSS view-timeline | static |
| M67 | Tilt card | pointer | rotateX/Y ±8°, layered | follows pointer | Fancy Box → Parallax Hover Effect | vanilla-tilt-like 25 lines | none |
| M68 | Gallery | drag | Flickity drag, image parallax, Touch & Total | — | Image Gallery → Flickity | Flickity 2.3 (jsdelivr) | no parallax |
| M69 | Hotspot pulse | load | marker ring pulse | 2 s × 2 | Image With Hotspots (Nectar Animated) | CSS | static |
| M70 | Ticket hover | pointer | y 0→−4, bg asphalt-750, perforation red | 500 ms `--e-arrive` | custom CSS | CSS | colour only |
| M71 | Field focus lane | focus | left bar scaleY 0→1, border/label red | 400 ms `--e-arrive` | Fluent Forms + `.sgp-field` | CSS | instant |
| M72 | Form success | valid submit | status box opacity 0→1 | 400 ms | Fluent Forms message | JS | instant |
| M73 | Copy feedback | click | label swap for 2.4 s | — | custom | JS | same |
| M80 | Inner hero | load/scroll | BG scale 1.08→1 (1600 ms); parallax Subtle | `--e-arrive` | Row BG Layer Animation: Slight Zoom Out Reveal + Parallax Subtle | CSS | static |
| M81 | Breadcrumb draw | load | separator lanes scaleX 0→1 | 600 ms, stagger 80 ms | custom CSS | CSS | drawn |
| M82 | Kita stotelė hover | pointer | BG image opacity 0→.35; lane scaleX 0→1 | 500 / 900 ms `--e-route` | Column BG Hover Opacity + custom CSS | CSS | opacity only |
| M83 | Submenu | scroll past | sticky; active link underline | 300 ms | Page Submenu (Sticky) | IO sets `aria-current` | instant |
| M84 | Button hover | pointer | fill swap; arrow pass-through | 320 / 550 ms | Button → Arrow Animation | CSS | colour only |
| M85 | Text link | pointer/focus | red underline scaleX 0→1 | 500 ms `--e-arrive` | Button → Underline | CSS | colour only |
| M86 | Call button | pointer | whole button red, icon cell inverts | 320 ms `--e-hover` | Button Basic + `.sgp-callbtn` | CSS | same |
| M87 | Footer stops | pointer/focus | ring fills red, link x +3 | 350 ms | custom CSS `.sgp-line-list` | CSS | colour only |

### 5.3 Static demo implementation (v2/)
- **Files:** `v2/assets/css/sgp.css` (tokens §2.1 + components; one file), `v2/assets/js/sgp-data.js` (`window.SGP_SCHEDULE`, `window.SGP_SERVICES` — §6.0/§6.5), `v2/assets/js/sgp.js` (runtime, one IIFE), `v2/assets/img/logo.svg` + `logo_light.svg` (copies of `/assets/img/`). External: Lenis `https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js` + `…/dist/lenis.css`; Flickity (only /apie-imone/) `https://cdn.jsdelivr.net/npm/flickity@2.3.0/dist/flickity.pkgd.min.js` + `…/dist/flickity.min.css`. **No GSAP, no other libraries.** anime.js is allowed but not needed.
- **Runtime modules** (all in `sgp.js`, guarded by feature checks; ~22 KB unminified is fine for the demo):
  1. `schedule` — renders every `[data-sched]` container from `SGP_SCHEDULE` exactly in the shortcode markup contract (§6.0); computes today in Europe/Vilnius (`Intl.DateTimeFormat('en-CA',{timeZone:'Europe/Vilnius'})`), `?siandien=YYYY-MM-DD` override.
  2. `flap` (§3.5), 3. `reveal` — one IntersectionObserver (`rootMargin:'0px 0px -12% 0px'`) adding `.in`; masks observe their parent (clip-path hides the element itself); split-word headings; odometer reels.
  4. `video` — lazy src (HD ≥1000 px, none below), IO play/pause, pause buttons.
  5. `header` — **one rAF-throttled passive scroll listener** (header state + services translateX only); no other scroll handlers. Everything else scroll-linked is CSS (`animation-timeline`).
  6. `switchboard` — `popover`; `beforetoggle` sets `top` under the header; fallback toggles `display` if `popover` is unsupported.
  7. `menu` — open/close, Lenis stop/start, focus handling, Esc.
  8. `hscroll` — **demo emulation of Salient Horizontal Scrolling** (pin height = vh + overflow; translateX by progress; off <1000 px, <620 px height or reduced motion; focusin scrolls the card into view) + the production IO stops (§3.4) + hover videos.
  9. `tabs` — ARIA tablist emulation of Salient Tabs (role=tab, aria-selected, arrow keys, `hidden` on panels).
  10. `stack` (overview page, M63) and `stickymedia` (service T4, M64) — CSS sticky + IO `.is-active`.
  11. `form` — validation + success box; `?domina=` pre-select; `copy` e-mail.
  12. `lenis` — init unless reduced motion; anchor links use `lenis.scrollTo(target,{offset:-72})` and move focus.
  13. `devtags` — Salient žymės overlay.
- **Cross-document view transitions** (M09) in CSS only: `@view-transition{navigation:auto}` inside `@media (min-width:1000px) and (prefers-reduced-motion:no-preference)`.
- **Links** are relative (`../../`), pages are `folder/index.html`; serve over http (directory index). 404 = `v2/404.html`.
- **Parallax** in the demo uses CSS scroll timelines with the same distances as Salient Subtle/Medium; Firefox shows static images (acceptable, same as production fallback).

### 5.4 Production custom code inventory (everything that is not a Salient option)
| # | Piece | Type | Size (unminified) | Without it |
|---|---|---|---|---|
| 1 | Tokens + surfaces + `sgp-*` component CSS (rail, ring, wp, stop, board, tt, kv, ticket, crumbs, fields, call bar tweaks, reduced motion) | CSS | ≈ 7 KB | Salient defaults (still complete) |
| 2 | `sgp-grafikas` shortcode + ACF options | PHP mu-plugin | ≈ 3 KB | GS-Board edited by hand (zero-code fallback) |
| 3 | `sgp-sched.js` — relative labels, hide past dates, soonest, ticker fit | JS | ≈ 1.1 KB | server-rendered labels (may be stale by ≤ cache TTL) |
| 4 | `sgp-flap.js` | JS | ≈ 0.8 KB | plain mono text |
| 5 | Stops IO (§3.4) | JS | ≈ 0.5 KB | lanes shown drawn |
| 6 | Hover video | JS | ≈ 0.5 KB | photo only |
| 7 | Video pause control | JS | ≈ 0.4 KB | Salient video without control (**not WCAG-compliant — keep**) |
| 8 | Switchboard hook + copy e-mail + `--rail-end` + tracking `?kodas` | JS | ≈ 0.6 KB | numbers still in footer/call bar |
| **Σ JS** | | | **≈ 3.9 KB** (≈ 1.7 KB gzip) | |
All JS is excluded from Salient's *Delay JavaScript Execution* and loaded `defer` in the footer; no dependencies (Lenis is Salient's own).

### 5.5 Reduced motion (`prefers-reduced-motion: reduce`)
Global CSS: `*,*::before,*::after{animation-duration:.001ms!important;animation-iteration-count:1!important;transition-duration:.001ms!important;transition-delay:0s!important;scroll-behavior:auto!important}` plus the explicit end states: rails/lanes/map drawn, rings filled (no halo), H1 words and dashes in place, masks open, odometer final, split words visible, parallax transforms none, flap final text, videos not autoplayed (poster + „Leisti“), Lenis not initialised, pinned sections (horizontal, stacking, overlapping) become plain stacks / a horizontal scroll-snap list, ticker static, pulses off, view transitions off. Salient has no global switch → this CSS/JS ships in Custom CSS/JS; per-device animation toggles are set as in §7.1.

---

## 6. Page blueprints

Legend per section: **Layout · Content** („…“ verbatim; **NEW** → §8.1) **· Media** (`media.json` ids; crop = object-position) **· Motion** (M ids) **· Salient.**

### 6.0 Global building blocks, schedule data, demo file map

**Global Sections**
| GS | Location / display | Contents |
|---|---|---|
| GS-Ticker | In Navigation Top (Before Scrolling); desktop only | `[sgp_grafikas variant="ticker" limit="3"]` |
| GS-Menu | Off Canvas content (Fullscreen Split, right) | phone groups, e-mail |
| GS-Board „Artimiausi pervežimai“ | Global Section element inside rows (home hero, Paslaugos, Tarptautiniai, service T8, Taisyklės) | board head + `[sgp_grafikas variant="board"]` |
| GS-Arrival „Atvykimas“ | Before Footer; hidden on /kontaktai/, /privatumo-politika/, 404 | §4.20 |
| GS-Footer | Footer | §4.21 |
| GS-CallBar | site-wide; Sticky Row bottom, tablet + phone | call bar §4.22 + Raw HTML switchboard popover §4.2 |
| GS-Trust „Kodėl verta pasitikėti mumis?“ | element on /apie-imone/ and /tarptautiniai-pervezimai/ | 9 numbered rows (§6.2) |
| GS-ServiceList | element on /tarptautiniai-pervezimai/, 404 | 11 services as a compact line list |

**Schedule data — ACF Options page „Pervežimų grafikas“ (menu slug `sgp-grafikas`)**
| Field | Type | Notes |
|---|---|---|
| `routes` | Repeater (4 fixed rows, order lt-ie, lt-es, ie-lt, es-lt) | |
| ↳ `key` | Select `lt-ie` / `lt-es` / `ie-lt` / `es-lt` (disabled after creation) | labels, codes and phones are constants in the plugin |
| ↳ `dates` | Repeater → `date` (Date Picker, return `Y-m-d`) | full ISO dates → solves "no year" and year wrap |
| `note` | Text | default „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“ |
| `updated` | auto (`acf/save_post` sets today) | printed as „Atnaujinta rugsėjo 23 d.“ |

Route constants: `lt-ie` Lietuva → Airija, code „LT → IE“, out, `tel:+37065053161` („+370 650 53161“) · `lt-es` Lietuva → Ispanija, „LT → ES“, out, `tel:+37063828919` · `ie-lt` Airija → Lietuva, „IE → LT“, in, `tel:+353864503104` („+353 86 450 3104“) · `es-lt` Ispanija → Lietuva, „ES → LT“, in, `tel:+34602547929` („+34 602 547 929“).
Current data (from [P], year assigned from the 2026-09-23 crawl — **client to confirm**): lt-ie 2026-10-09, 2026-10-23 · lt-es 2026-10-09, 2026-10-23 · ie-lt 2026-09-28, 2026-10-15, 2026-10-28 · es-lt 2026-09-27, 2026-10-14, 2026-10-28.

**Shortcode** `[sgp_grafikas variant="board|timetable|table|ticker|stub|next" routes="lt-ie,ie-lt" limit="3"]` (routes default = all four in constant order). Server: today = Europe/Vilnius; drop dates < today; next = first ≥ today; soonest = min next across the requested routes; output exactly the markup contracts in §3.5 (board), §3.6 (timetable), §4.10 (table), §4.1 (ticker), §3.9 (stub: date + relative), §4.11 (next). Every date is `<time datetime="YYYY-MM-DD">` in the words format; relative labels „šiandien“ / „rytoj“ / „po N d.“; grouped lists „rugsėjo 28 d., spalio 15 ir 28 d.“. Empty → „Grafikas atnaujinamas – skambinkite“. Page cache: purge on options save (or TTL ≤ 12 h); `sgp-sched.js` recomputes relative labels client-side.

Date words: months (genitive) sausio, vasario, kovo, balandžio, gegužės, birželio, liepos, rugpjūčio, rugsėjo, spalio, lapkričio, gruodžio; tile abbreviations SAUS., VAS., KOV., BAL., GEG., BIRŽ., LIEP., RUGP., RUGS., SPAL., LAPKR., GRUOD.; tile format `DD MMM.` („09 SPAL.“); full format „Spalio 9 d.“ (capitalised when it starts a line/cell), „spalio 9 d.“ inside sentences. **Never numeric (10-09), never weekday, never year** (the year is only stored).

**Demo file map** (`sgp-pervezimai/v2/`, relative links):
```
v2/index.html                                   Pradžia
v2/apie-imone/index.html
v2/pervezimo-paslaugos/index.html
v2/pervezimo-paslaugos/tarptautiniai-pervezimai/index.html
v2/pervezimo-paslaugos/tarptautiniai-pervezimai/{kroviniu-pervezimas|negabaritiniu-kroviniu-pervezimas|daliniu-kroviniu-gabenimas|daiktu-pervezimas|automobiliu-pervezimas|motociklu-pervezimas|keleiviu-pervezimas|gyvunu-pervezimas|siuntu-pervezimas|siuntu-pristatymas|perkraustymo-paslaugos}/index.html
v2/pervezimu-grafikas/index.html
v2/siuntos-sekimas/index.html
v2/taisykles/index.html
v2/kontaktai/index.html
v2/privatumo-politika/index.html
v2/404.html
v2/assets/{css/sgp.css, js/sgp.js, js/sgp-data.js, img/logo.svg, img/logo_light.svg}
```
Header, menu, switchboard, footer, call bar and GS-Arrival markup must be byte-identical across pages (generate from partials with a small script or copy carefully). Service pages are generated from one template + `SGP_SERVICES` (§6.5). Every page: `<html lang="lt">`, one H1, skip link „Pereiti prie turinio“, `<title>` and meta description per §6.12, `data-salient` on every block, the Salient žymės toggle.

**Photos in the demo:** `url_base + '?auto=compress&cs=tinysrgb&w=<w>'` with `srcset` 480/760/1100/1600/1920 and `sizes`; `loading="lazy"` below the fold; `width`/`height` attributes; `alt` = `alt_lt` from media.json (decorative textures `alt=""`). Videos: HD/SD URLs from media.json, poster from media.json.

**Media never used:** 7464393 (movers carrying a sofa — loading is not included), 38404178 (third-party truck branding), 12421166 (muddy under grade), all ferry media 19274366 / 3987777 / 32313192 / 15885602 / 35531295 (Ireland route unconfirmed — may be added after confirmation), 11479826 / 7828591 (Vilnius — implies an office), 8874803 / 8828587 (pins on Ireland/UK imply a route), 3847797, 15602514, 34497909 only where listed, v1 ids (media.json `excluded_ids`).

### 6.1 Home `/`
Row order and surfaces: S0 header → S1 dark hero → S2 paper → S3 dark → S4 paper → S5 dark video → S6 paper → S7 dark texture → S8 paper-100 → S9 paper (placeholder) → S10 dark → footer. Chapter numbers 01–07 in waypoints.

**S1 · Išvykimas (hero + docked board)** — Row Full Height (min 100svh, content bottom), dark.
- Layout: ≥1280: copy 8 cols (eyebrow, H1, lead) | call column 4 cols (two call buttons stacked + „Visas pervežimų grafikas →“), bottom-aligned; below, the full-width glass board. 1000–1279: calls in a row under the lead. <1000: eyebrow, H1, **next-line**, lead, stacked full-width call buttons, link; the board detaches below the hero as a solid asphalt-950 block (2×2 ≥481, 1 column ≤480).
- Content: eyebrow „Tarptautiniai pervežimai mikroautobusais“ (NEW, adapted from the page title „Tarptautiniai pervežimai Europoje (mikroautobusais)“); H1 per §3.10 (visual „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“ NEW; sr-only „Tarptautiniai pervežimai: Lietuva – Airija, Lietuva – Ispanija ir atgal“ NEW); lead „Visos pervežimo paslaugos – saugiai, greitai, patikimai. Keleiviai, siuntos, automobiliai, motociklai, gyvūnai ir perkraustymas nuo durų iki durų.“ (NEW, from [P] hero text + service list); call buttons „Pervežimai į Airiją +370 650 53161“, „Pervežimai į Ispaniją +370 638 28919“; board head „Artimiausi pervežimai“ [P] + note (NEW) + link „Visas grafikas“.
- Media: video **29374299** (HD `12654527_1280_720_30fps.mp4` 4.9 MB, desktop only after poster; production re-encode ≤ 2.5 MB H.264 + WebM), poster from media.json; phones poster only, `object-position:58% 55%`. Alt/aria: decorative (`aria-hidden`).
- Motion: M10, M11, M12, M13 (lead +700, calls +850), M14 (+700 ms), M15, M16, M86.
- Salient: Row Full Height (Responsive Height svh, content Bottom) · Video BG MP4 + preview image · Parallax Subtle · Color Overlay Advanced (§2.8) · Text Color Light · Inner Row 1: Raw HTML H1 + Text Block + 2 × Button `.sgp-callbtn` + Button Underline · Inner Row 2 (Minimum Width 100 %, Backdrop blur 16 px, bg `rgba(11,14,16,.74)`): Global Section GS-Board · Raw HTML video pause button.
- Fit rule (tested): board fully visible at 1024×768, 1366×657, 1366×768, 1440×800; at ≤760 px height the board note and „Vėliau“ lines hide.

**S2 · 01 Apie mus** — paper + graticule, rail.
- Layout: waypoint („01 · Apie mus“, meta „LT ⇄ IE · LT ⇄ ES“); 7 cols copy | 4 cols cascade (offset 1); stats row of 4.
- Content: statement „„SGP“ – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu Lietuva – Ispanija – Lietuva, Lietuva – Airija – Lietuva ir kitas Europos šalis (Vokietiją, Prancūziją).“ [P] (the two routes underlined); body „Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.“ [P]; datasheet (keys NEW, values from [P]/[S]): Veikla — Keleivių, siuntų ir automobilių pervežimas · Kryptys — Lietuva – Airija – Lietuva · Lietuva – Ispanija – Lietuva · Taip pat — Vokietija, Prancūzija · Principas — Nuo durų iki durų · Draudimas — Kroviniai ir keleiviai kelionės metu apdrausti · Vairuotojai — Laikosi privalomo darbo ir poilsio režimo; link „Skaityti daugiau“ [P] → /apie-imone/; stats §4.12.
- Media: back **7541981** (4:5, crop 60% 40%, crop marks), front **6169133** (4:3).
- Motion: M20, M21, M13, M23, M24, M25, M26, M27, M44.
- Salient: Row bg `#F5F7F6` + `sgp-light sgp-graticule sgp-has-rail`; Highlighted Text (Regular Underline, accent, 3 px); Text Block `.sgp-kv`; Cascading Images (2 layers, parallax, Grow In Reveal / Fade In From Bottom); Button Underline; Milestone ×4.

**S3 · 02 Paslaugos — horizontal road** — dark.
- Layout: skip link (focus-visible only) „Praleisti paslaugų juostą“ → #marsrutai; waypoint (meta „11 paslaugų“); H2 left + lead; right: counter „01 / 11“ (mono 40–54 px) + link „Visos paslaugos sąrašu →“ (/pervezimo-paslaugos/); track of 11 cards + end card (§4.7).
- Content: H2 „Visos pervežimo paslaugos“ [P hero]; lead „Platus paslaugų spektras suteikia universalumo, nes savo klientams galime pasiūlyti kur kas daugiau sprendimų.“ [P]. Cards:

| # | Title [S] | Summary | Chips (NEW) | Photo (16:11) | Hover video (SD) |
|---|---|---|---|---|---|
| 01 | Krovinių pervežimas | „Į Airiją, Ispaniją, Vokietiją bei Prancūziją ir atgal – saugiai, greitai, patikimai.“ [S] | Nuo durų iki durų · Kroviniai apdrausti | 38927007 (50% 60%) | — |
| 02 | Negabaritinių krovinių pervežimas | „Kroviniai, kurių matmenys didesni, nei leidžiama šalyse, per kurias jie keliauja.“ NEW (condensed [S]) | Išankstinis planavimas · Nuo durų iki durų | 35332902 | 19552565 (2.6 MB) |
| 03 | Dalinių krovinių gabenimas | „Dalinių krovinių gabenimas yra puikus būdas klientams sutaupyti.“ [S] | Mokate mažiau · Nuo durų iki durų | 29786116 | — |
| 04 | Daiktų pervežimas | „Langai, žoliapjovės, buitinė įranga ir kiti didesni ar mažesni daiktai.“ NEW | Apie 3–4 paros · Nuo durų iki durų | 36933446 | — |
| 05 | Automobilių pervežimas | „Automobilius gabename traliuku – iš Airijos, Ispanijos, Vokietijos ir į jas.“ NEW | Traliuku · Apie 3–4 paros | 29566910 | 34371915 (1.4 MB, b/w) |
| 06 | Motociklų pervežimas | „Iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos bei Airijos – nuo durų iki durų.“ NEW | 3–4 paros · Nuo durų iki durų | 4858429 | 34308329 (1.3 MB) |
| 07 | Keleivių pervežimas | „Atlenkiamos ir šildomos sėdynės, kondicionierius. Kelionės metu visi keleiviai apdrausti.“ NEW | Keleiviai apdrausti · 3–4 paros | 36377055 | — |
| 08 | Gyvūnų pervežimas | „Saugiai ir patogiai perkraustysime Jūsų augintinį į kitą šalį Europoje.“ [S] | Narvus turime mes · Nuo durų iki durų | 32872983 | — |
| 09 | Siuntų pervežimas | „Skubios siuntos pasieks gavėją labai operatyviai.“ [S] | Skubios siuntos · Nuo durų iki durų | 6170458 | — |
| 10 | Siuntų pristatymas | „Siuntiniai paimami iš siuntėjų ir atiduodami gavėjams į rankas.“ [S] | Į rankas gavėjui · Apie 3–4 paros | 13456097 | — |
| 11 | Perkraustymo paslaugos | „Persikeliate gyventi į kitą šalį Europoje? Daiktus pervešime nuo durų iki durų.“ NEW | Apie 3–4 paros · Nuo durų iki durų | 4246238 | — |

- Motion: M30, M31, M32, M33, M34, M22.
- Salient: §4.7. Counter `[data-sgp-count]` in a Text Block.

**S4 · 03 Maršrutai** — paper + graticule, rail.
- Layout: waypoint (meta „2 kryptys“); H2 7 cols | paragraph + tabs 5 cols; tab content per §4.9.
- Content: H2 „Dvi kryptys. Keturios šalys pakeliui.“ NEW; paragraph (verbatim, trimmed) „Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija – nedvejokite, jei norite perduoti siuntą jose gyvenantiems artimiesiems.“ [P]; tabs „Airija IE“ / „Ispanija ES“; panel H3 „Lietuva – Airija – Lietuva“ / „Lietuva – Ispanija – Lietuva“ [P]; timetable (`routes="lt-ie,ie-lt"` / `"lt-es,es-lt"`); kv „Kelyje — apie 3–4 paros nuo paėmimo dienos“; phone lists (IE panel LT/IE/UK; ES panel LT/ES) under the label „Pervežimai į Airiją“ / „Pervežimai į Ispaniją“.
- Media: IE **2881400** (16:10, crop 50% 60%); ES **27868340** (16:10). Map §3.8.
- Motion: M20, M21, M22, M40, M41, M42, M43, M44, M45.
- Salient: Tabs → Toggle Button; each tab = Inner Row (Raw HTML SVG map 7/12 + Column 5/12 with Image, Text Block, shortcode, Text Block `.sgp-kv`, phone list).

**S5 · 04 Kelionėje (cinematic)** — dark, video, rail.
- Layout: min-height 112vh (auto <1000); waypoint (meta „Apie 3–4 paros“); H2 (max 16ch) + lead; 5 comfort stops on a horizontal lane (vertical <1000); footer row: link + pause button.
- Content: H2 **„Du namai, vienas kelias tarp jų.“** NEW; lead „Kelionė trunka apie 3–4 paras – pasirūpinsime, kad laikas neprailgtų.“ NEW (from „trunka apie 3–4 paras“ + „pasirūpinsime, kad laikas neprailgtų“ [P]); stops (titles NEW where not verbatim, texts verbatim [P]/[S]): „Atlenkiamos sėdynės“ — „Patogiai Jūsų kelionei tiek dieną, tiek naktį.“ · „Šildomos sėdynės“ — „Komfortui net žvarbiausiomis žiemos dienomis.“ · „Kondicionierius“ — „Kad oras autobuse visada būtų šviežias.“ · „Keleiviai apdrausti“ — „Kelionės metu visi keleiviai yra apdrausti.“ · „Poilsio režimas“ — „Vairuotojai visada laikosi privalomo darbo ir poilsio režimo.“ (DVD omitted); link „Keleivių pervežimas →“.
- Media: video **4685871** (HD 3.8 MB desktop / poster phones).
- Motion: M16, M50, M51, M52, M53, M20.
- Salient: Row Video BG + Parallax Medium + BG Layer Zoom Out Slowly + overlay + Text Color Light; Animated Text Word Blur; Icon List (5) + `.sgp-stops` custom CSS; Button Underline; Raw HTML pause.

**S6 · 05 Kelionės eiga** — paper, rail.
- Layout: waypoint; H2; 3 stations on a lane (vertical <1000); kv facts (7 cols).
- Content: H2 „Nuo durų iki durų“ [S]; stations: „01 Paėmimas“ — „Krovinys paimamas iš siuntėjo nurodytos, jam patogiausios, vietos.“ [S perkraustymo] · „02 Kelyje apie 3–4 paras“ (title NEW) — „Siuntos vietą galite pasitikrinti pagal siuntos kodą.“ NEW + link „Siuntos sekimas“ · „03 Pristatymas“ — „Pristatome gavėjui tiesiai į rankas. Jei sutartu laiku gavėjas negali paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.“ (NEW condensation of [S perkraustymo] „…pristatomas gavėjui teisiai [sic] į rankas“ + [P] „Jei sutartu laiku gavėjas arba siuntos adresatas negali atiduoti / paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.“); delivery facts (§4.12).
- Media: **6407553**, **1696742**, **4440774** (80 px circles, centre crop).
- Motion: M55, M56, M27.
- Salient: Divider (2 px accent, line animation) + 3 Columns (delays 0/120/240) + Image Mask Circle + Column Mask Reveal (circle) + Text Block `.sgp-kv`.

**S7 · 06 Prieš siunčiant (rules digest)** — dark, texture, rail.
- Layout: 5 cols sticky (H2 + callout „Svarbu“ + buttons) | 7 cols toggle panels.
- Content: H2 „Krovinių pervežimas tarptautiniais maršrutais: ko negalima siųsti?“ [P H5]; callout „Už siuntinio turinį atsakingas siuntėjas.“ [P]; panels (titles NEW, content verbatim):
  1. „Draudžiama siųsti (12)“ — Taisyklių 4.2 list, 12 items: „bet kokie tabako gaminiai“, „bet kokie alkoholiniai gėrimai“, „pinigai ir vertybiniai popieriai“, „taurieji metalai“, „juvelyriniai gaminiai“, „vaistai ir maisto papildai“, „šaunamieji ir kiti ginklai“ (typo fixed, approval), „meno kūriniai ir antikvariniai daiktai“, „cheminiai kroviniai ir degios prekės“, „greitai gendantys maisto produktai“, „daiktai, kurių pervežimui reikalingos specialios temperatūros, oro, drėgmės ir kitos papildomos sąlygos“, „visos kitos prekės, kurias vežti draudžiama įstatymais…“ (✕ list).
  2. „Pakavimas (4)“ — the 4 rules [S kroviniu] („pakuotei naudokite tik naujas, standžias, nepažeistas dėžės ar kitas pakuotes;“ … „pasirūpinkite, kad adresas būtų užrašytas matomoje vietoje, ten, kur nekyla rizika nusitrinti, nuplyšti.“) + „rekomenduojamas tarpas yra 5 centimetrai“ [S siuntu].
  3. „Gavėjas ir pristatymas“ — „Labai svarbu nurodyti tikslius siuntinio paėmimo ir pristatymo adresus Europoje. Jei sutartu laiku gavėjas arba siuntos adresatas negali atiduoti / paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.“ + „Neretai siunčiami didesni, sunkesni daiktai, kurių iškrovimui reikalinga speciali technika. Tokiu atveju iškrovimu turi pasirūpinti siuntos gavėjas.“ [P].
  4. „Baudos“ — fines table (§6.8) + „Plačiau taisyklėse →“.
  Buttons: „Visos taisyklės“ (Line) → /taisykles/; „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“ (text link + download icon) → `https://www.sgp-pervezimai.lt/siuntu-siuntimo-taisykles/download/sgp-sutartis-su-siunteju-pdf-3` (production: re-hosted file).
- Media: texture **4040619**, overlay `#0F1417` 90 %, Parallax Subtle.
- Motion: M60, M61, M62, Row Parallax Subtle (as M10), M20.
- Salient: Row bg image + overlay + Parallax Subtle + `sgp-dark sgp-has-rail`; Column Sticky Content (CSS, Top 120); Toggle Panels → Minimal Shadow (accordion, deep linking) `.sgp-toggle`; Text Block `.sgp-kv`; Buttons.

**S8 · 07 Siuntos sekimas (strip)** — paper-100, rail.
- Content: H2 „Siuntos sekimas“ [P]; tracking field (§4.15); helper „Neradote siuntos kodo? Paskambinkite – pasakysime, kur Jūsų siunta.“ NEW.
- Salient: Raw HTML form (`nectar-inline-subscribe-form` styling + `.sgp-field`).

**S9 · Atsiliepimai (placeholder)** — §4.23 (production: row disabled).

**S10 · Atvykimas** — GS-Arrival (§4.20); rail ends in the terminus ring. **S11** GS-Footer. **S12** GS-CallBar.

### 6.2 Apie įmonę `/apie-imone/`
1. **Route header** (photo) — breadcrumb „Pradžia › Apie įmonę“; eyebrow „Saugiai greitai patikimai“ [P H3]; H1 „Apie įmonę“ (menu label stays „Apie mus“); lead „SGP – visos pervežimo paslaugos“ [P]. Media **9989463** (crop 50% 60%). M80, M22, M81.
2. **01 Įmonė** (paper, rail) — the three verbatim paragraphs [P] (routes underlined, M23): „„SGP“ – esame įmonė…“, „Nuo pirmos darbo dienos…“, „Mes visada pasiruošę teikti kokybiškas transporto paslaugas už Jums prieinamą kainą!“; right: datasheet (§6.1 S2); stats row.
3. **02 Principai** (dark) — lead „Saugumas, operatyvumas, profesionalumas, komfortas ir patogumas – tai esminiai kriterijai, kuriais grindžiama mūsų įmonės veikla ir profesionalios keleivių vežimo paslaugos.“ [S keleiviu]; five stacking cards (mono „01“–„05“, title, verbatim paragraph; edits: Saugumas drops „Mūsų transporto priemonių parke – tik nauji (2017–2018 metų) mikroautobusai.“; Komfortas drops the DVD sentence and „Klejonė yra puikus būdas…“; typo „puiki žino“ → „puikiai žino“ with approval). Media: Saugumas **31570314**, Operatyvumas **17720190**, Profesionalumas **6720534**, Komfortas **17455631**, Patogumas **27383867** (each 4:5 right, 45 % width). Sticky Content Sections → Sticky Scroll Pinned Sections, effect **Stacking**, Section Navigation off; effect off on tablet/phone (plain stack). M63.
4. **03 Kelyje** (paper) — gallery (Image Gallery → Flickity; Touch & Total indicator „03 / 05“ in mono; image parallax; Mask Edges): **11053641**, **2449454**, **8858566**, **21041157**, **1606957**; caption none. Replace with the client's own 5 photos when high-res files arrive. M68.
5. **04 Kodėl verta pasitikėti mumis?** (dark) — GS-Trust: the 9 bullets [P Tarptautiniai] as numbered rows (Horizontal List Item, Border Animation; mono „01“–„09“; first clause bold). Edits (approval): bullet 3 „sako“ → „savo“; bullet 4 drops „DVD – kad kelionė neprailgtų.“ and „naujausiais“ → „techniškai tvarkingais“ (client to confirm); bullet 6 „užtiktiname“ → „užtikriname“. M27, M45.
6. **GS-Board**, **GS-Arrival**.
Meta: title „Apie įmonę | sgp-pervezimai.lt“.

### 6.3 Pervežimo paslaugos `/pervezimo-paslaugos/`
1. **Route header** — H1 „Pervežimo paslaugos“; lead „Pervežimo paslaugų poreikis Europoje nuolat auga. Tai – puikus būdas komunikuoti, keistis apčiuopiama informacija, prekėmis ir kitais daiktais tarp fizinių asmenų bei verslo subjektų skirtingose šalyse.“ [P]. Media **36383706** (crop 50% 55%). M80.
2. **Three route tickets** (paper) — ticket-shaped **Fancy Box → Parallax Hover Effect** tiles (Extra Class `sgp-ticket-tilt`, M67): „Tarptautiniai pervežimai“ [P tile] (meta „11 paslaugų · 2 kryptys“ NEW) → /…/tarptautiniai-pervezimai/ · „Pervežimų grafikas“ [P tile] (meta = `[sgp_grafikas variant="next"]` compact) → /pervezimu-grafikas/ · „Siuntos sekimas“ [P tile] (meta „Pagal siuntos kodą“ NEW) → /siuntos-sekimas/. Column delays 0/120/240.
3. **01 Visos paslaugos — stacked groups** (dark) — left sticky index of 6 groups (≥1000); right Sticky Scroll Pinned Sections → **Stacking**, one card per group (§4.8). Groups (names NEW) → services (title [S], summary = the home card summary) → image:
   1. „Kroviniai“ → Krovinių pervežimas, Negabaritinių krovinių pervežimas, Dalinių krovinių gabenimas → **34585120**
   2. „Daiktai ir perkraustymas“ → Daiktų pervežimas, Perkraustymo paslaugos → **7464731**
   3. „Automobiliai ir motociklai“ → Automobilių pervežimas, Motociklų pervežimas → **29566910**
   4. „Keleiviai“ → Keleivių pervežimas → **36377055**
   5. „Gyvūnai“ → Gyvūnų pervežimas → **3868901**
   6. „Siuntos“ → Siuntų pervežimas, Siuntų pristatymas → **4487517**
   Mobile: plain stack of 6 cards, index hidden. M63, M45, M44.
4. **02 Kryptys ir transportas** (paper, rail) — left sticky waypoint + H2 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ [P H5]; right: paragraphs 2–3 of the category text [P] („Pervežimo paslaugos patrauklia kaina vykdomos tokiomis kryptimis Europoje: …“ with the case fix „į Airiją ir iš Airijos, į Ispaniją ir iš Ispanijos, į Vokietiją ir iš Vokietijos, į Prancūziją ir iš Prancūzijos“ — approval; „…vykdomos naujais, techniškai tvarkingais, patogiais mikroautobusais…“) + the H5 paragraph („Komandoje turime subūrę…“, typo „sklandžia“ → „sklandžią“); delivery facts kv; inline image **32821932** with Column → Scroll Position Advanced (scale .88 → 1, y 40 → 0) (M66).
5. **GS-Board**, **GS-Arrival**.

### 6.4 Tarptautiniai pervežimai `/pervezimo-paslaugos/tarptautiniai-pervezimai/`
1. **Route header (video)** — H1 „Tarptautiniai pervežimai“; lead „SGP pervežimai – komanda savo srities profesionalų, turinčių vieningą tikslą – užtikrinti, kad siuntiniai ir keleiviai į Ispaniją ir Airiją keliautų saugiai, greitai, patikimai ir komfortiškai.“ [P]. Media: video **13707149** (HD 1.5 MB desktop; SD 0.4 MB tablet), poster phones; overlay lighter (left 80 %). M80, M16.
2. **01 Dviem maršrutais** (paper + graticule, rail) — H2 „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais“ [P bold]; bullets „iš Lietuvos į Ispaniją ir atgal;“ („Ispanija“ → „Ispaniją“, approval) / „iš Lietuvos į Airiją ir atgal.“ [P]; **Image With Hotspots** on the static both-routes schematic (IE leg dashed „maršrutas tikslinamas“, ES solid), numbered markers on PL, DE, BE, FR with tooltip „Pakeliui – galite perduoti siuntą čia gyvenantiems artimiesiems.“ (NEW, from [P]); markers on IE/ES with the direction numbers („Airija · +353 86 450 3104“, „Ispanija · +34 602 547 929“). M69.
3. **02 Airija / 03 Ispanija** — Sticky Scroll Pinned Sections → **Overlapping** (M65), each chapter full-bleed dark:
   - *Airija*: bg video **2386447** SD (3.3 MB, desktop only; never HD), phone photo **13568682**; H2 „Lietuva – Airija – Lietuva“; insets **2881400**, **3220828** (Mask Reveal, 120 ms stagger); `[sgp_grafikas variant="timetable" routes="lt-ie,ie-lt"]`; phones LT/IE/UK; delivery facts. No ferry media.
   - *Ispanija*: bg **22033738** (crop 50% 60%); H2 „Lietuva – Ispanija – Lietuva“; insets **27868340**, **34497909**; timetable `routes="lt-es,es-lt"`; phones LT/ES.
   Mobile: effect off, plain stack.
4. **04 Pakeliui** (paper, rail) — verbatim paragraph „Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija, todėl nedvejokite, jei norite perduoti siuntą jose gyvenantiems artimiesiems, draugams ar verslo partneriams, taip pat jei norite šias šalis aplankyti ir patys.“ [P]; four stop tiles on a horizontal lane (Horizontal List Item ×4, Border Animation): LENKIJA · VOKIETIJA · BELGIJA · PRANCŪZIJA (mono names + ring; no photos, no invented facts). M45, M31-style lane (CSS on enter).
5. **05 Kodėl verta pasitikėti mumis?** — GS-Trust (§6.2).
6. **06 Ko negalima siųsti?** (dark) — H2 verbatim H5; 8 bullets [P] as ✕ list (typo „visus daiktai“ → „visi daiktai“, approval); callout with the two paragraphs „Už siuntinio turinį atsakingas siuntėjas. …“ and „Už valstybinių institucijų konfiskuotas siuntas mes atsakomybės neprisiimame.“ [P].
7. **07 Ką dar turite žinoti?** (paper) — H2 „Tarptautiniai pervežimai: ką dar turite žinoti?“ [P H5]; four notice cards (1 px ink top rule, mono index): card 1 = delivery facts kv (replaces „…truks apie 3–4 paras nuo paėmimo datos“ + adds the 3.4 commitment); cards 2–4 = the three verbatim paragraphs (pakavimas, adresai, iškrovimas).
8. **08 Paslaugos** — GS-ServiceList.
9. **GS-Arrival**.

### 6.5 Service detail template (one template → 11 pages)
URL `/pervezimo-paslaugos/tarptautiniai-pervezimai/<slug>/`; WPBakery template „SGP – paslauga“ (Salient Templates); shared rows are Global Sections. Demo: one HTML template filled from `SGP_SERVICES[slug]`.

| # | Section (id) | Surface | Layout / content rule | Motion | Salient |
|---|---|---|---|---|---|
| T1 | Route header | dark photo/video | breadcrumb (4 levels) · H1 = `h1` · lead = `lead` (Santrauka, verbatim) · `chips` · next-line (<1000) · right: compact call ticket with both LT numbers | M80, M22, M81 | §4.17 |
| T1b | Page Submenu | light glass, sticky | links = `submenu` | M83 | Page Submenu (Sticky) |
| T2 | Faktai (`#faktai`) | paper | `dl.sgp-kv` with rows `kv` (Kryptys · Kelyje · Pristatymas · Įsipareigojimas (parcels only) · Svarbu), 7 cols + child-route chips 5 cols („Kryptys ir paslaugos“ NEW label) | M27 | Text Block `.sgp-kv` + Buttons (chips) |
| T3 | 01 Apie paslaugą (`#apie-paslauga`) | paper, rail | left sticky waypoint; right `intro` paragraphs (verbatim, 68ch) | M13, M20 | Column Sticky Content |
| T4 | 02 Privalumai (`#privalumai`) | dark | H2 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ [S H5]; `why` blocks (each = verbatim paragraph, first sentence bold) with `why_media` swapping | M64, M22 | Sticky Content Sections → Sticky Media, Scrolling Content (media 45 %, 80vh) |
| T5 | Special block | varies | `special` (per service) | varies | varies |
| T6 | 03 Kliento atsakomybės (`#atsakomybes`) | paper, rail | H2 „Kliento atsakomybės: ką reikia žinoti?“ [S H5]; `responsibilities` as Toggle Panels (≥2) or one callout (1) | M60 | Toggle Panels → Minimal Shadow |
| T7 | 04 Draudžiami daiktai (`#draudziami`) | dark | `prohibited` (✕ list, verbatim) + „Šis sąrašas nėra baigtinis…“ where present + link „Visos taisyklės →“ + fines teaser „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“ (NEW summary) | M62 | Fancy Unordered List + Button |
| T8 | Artimiausi pervežimai | dark | GS-Board | M14 | Global Section |
| T9 | Uždarymas | paper | `closing` (verbatim) in statement size, 2 key phrases underlined | M23 | Highlighted Text |
| T10 | Kita stotelė | dark | next service (`next`) | M82 | §4.19 |
| T11 | 05 Užklausa (`#uzklausa`) | dark | GS-Arrival; form `domina` pre-selected = this service | M70, M71 | Global Section |

Keleivių and Gyvūnų pages drop T7 (not applicable); their submenus differ (see data). If `responsibilities` has one item, T6 renders a callout; if none, T6 is omitted.

**Data schema (`SGP_SERVICES[slug]`)**
| Field | Type | Rule |
|---|---|---|
| `slug`, `no` | string, "01"–"11" | order = [P] tile order |
| `h1` | string | [S] H1 |
| `title` | string | `<title>` (live, typo fixes §6.12) |
| `meta` | string | meta description (§6.12) |
| `card` | string | home/overview one-liner (§6.1 S3) |
| `lead` | string | [S] Santrauka verbatim |
| `chips` | [2] | NEW chip labels (§6.1) |
| `kv` | [{k, v}] | keys: Kryptys, Kelyje, Pristatymas, Įsipareigojimas (parcels), Svarbu |
| `routes` | [string] | [S] child-page names → chips linking to `?domina=<h1>#uzklausa` |
| `intro` | [ref] | paragraph refs by first words |
| `why` | [ref] | 2–3 paragraph refs (bold first sentence) |
| `why_media` | [id×3] | media ids |
| `special` | {type, …} | see per-service |
| `responsibilities` | [{title, ref}] | titles NEW where not verbatim |
| `prohibited` | ref / "P" | own list or „P“ = [P Tarptautiniai] 8 bullets |
| `closing` | string | verbatim |
| `hero` | {type: photo/video, id, poster, crop} | |
| `submenu` | [labels] | default „Apie paslaugą · Privalumai · Kliento atsakomybės · Draudžiami daiktai · Užklausa“ |
| `next` | slug | 01→02 … 11→01 |

Paragraph references use the first words of the paragraph in [S] „Tekstas (pažodžiui)“; copy the whole paragraph verbatim, applying only the approved fixes in §8.2.

**Per-service data** — „Įsipareigojimas — (3.4 p.)“ below always means the full row „Įsipareigojimas siuntoms — per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklių 3.4 p.)“ (§4.12).

**01 `kroviniu-pervezimas`** — h1 „Krovinių pervežimas“ · lead „Krovinių pervežimas į Airiją, Ispaniją, Vokietiją bei Prancūziją ir atgal – saugiai, greitai, patikimai.“ · kv: Kryptys — Airija, Ispanija, Vokietija, Prancūzija – ir atgal · Kelyje — apie 3–4 paros nuo paėmimo dienos [P] · Pristatymas — nuo durų iki durų · Įsipareigojimas — per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklių 3.4 p.) · Svarbu — „Krovinius iškrauname, jei tam nereikalinga speciali technika.“ · routes: Krovinių pervežimas į Airiją · iš Airijos · iš Ispanijos · į Ispaniją · į Vokietiją · iš Vokietijos · intro: „Jei norite į kitą šalį Europoje išsiųsti krovinį…“, „Mūsų įmonės įkainiai rinkoje labai patrauklūs…“ · why: „Užtikriname, kad krovinių pervežimas Europoje bus sklandus…“ split into two blocks (block 1 ends „…naujomis transporto priemonėmis.“, block 2 starts „Tikriausiai nė nereikia sakyti…“), „Svarbu žinoti, kad krovinių pervežimas vyksta nuo durų iki durų…“ · why_media 17720190, 31570314, 2449454 · special: **„Esminės krovinių pakavimo taisyklės“** [S bold] — the 4 bullets as a numbered 4-stop lane (paper) · responsibilities: „Atsakomybė už pakuotę“ — „Jei dėl netinkamos krovinio pakuotės jos turinys yra apgadinamas arba apgadinami kiti kroviniai, atsakomybė už tai tenka klientui.“; „Iškrovimas“ — „Krovinius iškrauname, jei tam nereikalinga speciali technika. Jei tokia reikalinga, tuo turi pasirūpinti klientas.“; „Tranzito šalių teisės aktai“ — „Labai svarbu atsižvelgti ir į šalyse, per kurias keliaus krovinys, galiojančius teisės aktus bei draudžiamus į jas įvežti daiktus. Jei kyla abejonių, nes nežinote tų šalių teisės aktų, susisiekite su mumis – pakonsultuosime.“ · prohibited: own list (lead „Būtinai paskaitykite draudžiamų siųsti daiktų sąrašą. Į jį įeina:“ + 4 bullets + „Šis sąrašas nėra baigtinis. …“) · closing „Visi mūsų gabenami kroviniai kelionės metu yra apdrausti.“ · hero photo **38927007** (50% 60%) · next 02.

**02 `negabaritiniu-kroviniu-pervezimas`** — h1 „Negabaritinių krovinių pervežimas“ · lead „Negabaritinių krovinių pervežimas – išskirtinė krovinių pervežimo paslauga, reikalaujanti specialių žinių, atitinkamos technikos, išankstinio planavimo, tam tikrų leidimų.“ („tiktų“ → „tikrų“, approval) · kv: Kryptys — Lietuva, Prancūzija, Ispanija, Airija · Kelyje — reikia išankstinio planavimo · Pristatymas — nuo durų iki durų · Svarbu — „Iškrovimo technika – kliento atsakomybė“ (NEW condensation) · routes: Pavojingų krovinių pervežimas · Didelių krovinių pervežimas · intro: „Negabaritinių krovinių pervežimas – išskirtinė…“ · why: „Ilgametė patirtis, sukauptos žinios…“, „Negabaritinius krovinius transportuojame į Lietuvą…“, „Negabaritiniai kroviniai pristatomi vadovaujantis principu nuo durų iki durų…“ (the „tik naujais mikroautobusais“ paragraph is not shown — vehicle claim to confirm) · why_media 38095094, 31570314, 12418936 · special: **definition callout** (dark) „Negabaritiniai kroviniai yra tokie kroviniai, kurių matmenys yra didesni negu didžiausi leidžiami tose šalyse, per kurias tie kroviniai keliauja.“ beside Self Hosted Video **19552565** SD (autoplay in view, muted, loop, no controls + pause button, desktop only; poster phones) · responsibilities: „Gavėjas sutartu laiku“ — „Tiesa, labai svarbu, kad krovinio gavėjas sutartu laiku būtų atsiėmimo vietoje – kitu atveju pakartotinis krovinio pristatymas bus apmokestinamas papildomai.“; „Iškrovimas“ — „Paprastai negabaritinių krovinių pervežimas, taip pat ir pavojingų krovinių vežimas reikalauja specialios technikos kroviniui iškrauti. Tai – kliento atsakomybė.“ · prohibited „P“ · closing „Žinome visus niuansus, todėl drąsiai priimame šiuos iššūkius ir sėkmingai juos įgyvendiname.“ · hero photo **35332902** (50% 50%) · next 03.

**03 `daliniu-kroviniu-gabenimas`** — h1 „Dalinių krovinių gabenimas“ · lead „Dalinių krovinių gabenimas yra puikus būdas klientams sutaupyti.“ · kv: Kryptys — Vokietija, Prancūzija, Ispanija, Airija – į ir iš · Kelyje — apie 3–4 paros nuo paėmimo dienos [P] · Pristatymas — nuo durų iki durų · Įsipareigojimas — (3.4 p.) · Svarbu — „Papildomas krovinio atvežimas bus apmokestinamas.“ · routes: Smulkių krovinių pervežimas · intro: „Dalinių krovinių gabenimas yra puikus būdas…“, „Kai vykdomas dalinių krovinių gabenimas…“ · why: „Dalinių krovinių gabenimas Europoje vykdomas tose šalyse…“, „Dalinių krovinių gabenimas vykdomas tik naujais, techniškai tvarkingais…“, „Dalinių krovinių pervežimas Europoje – nuo durų iki durų…“ · why_media 34585120, 12418936, 6169133 · special: **„Kaip veikia dalinis krovinys“** (NEW title) — static SVG (Raw HTML or Image): van outline split into 3 bays, one bay in signal-ink hatching, others ink outlines; caption „Dalinis krovinys yra toks krovinys, kuris neužima visos transporto priemonėje kroviniams skirtos erdvės.“ [S] · responsibilities: „Pakavimas ir adresai“ — „Dalinių krovinių gabenimas bus sklandus, jei prie šio proceso prisidės ir klientas. …“; „Gavėjas sutartu laiku“ — „Atsiėmimo vietoje sutartu laiku turi būti gavėjas. Papildomas krovinio atvežimas bus apmokestinamas.“ · prohibited: „Įsitikinkite, kad nesiunčiate draudžiamų siųsti daiktų. …“ · closing „Dalinių krovinių pervežimas Europoje su „SGP pervežimai“ – profesionalios gabenimo paslaugos naujais, techniškai tvarkingais mikroautobusais, su atsakingu vairuotoju, geriausia kaina, patikimai ir saugiai.“ · hero **29786116** · next 04.

**04 `daiktu-pervezimas`** — h1 „Daiktų pervežimas“ · lead „Jei į kitą šalį norite gabenti didesnį ar mažesnį daiktą, siūlome susisiekti su mumis – pasiūlysime optimaliausią variantą.“ · kv: Kryptys — Vokietija, Prancūzija, Ispanija, Airija – į ir iš · Kelyje — apie 3–4 paros (skaičiuojama nuo siuntos paėmimo dienos) · Pristatymas — nuo durų iki durų, be perdavimo keliems vežėjams · Įsipareigojimas — (3.4 p.) · Svarbu — „Daiktų supakavimas yra kliento atsakomybė.“ · routes: Daiktų pervežimas į Airiją · intro: „Įvairiausi daiktai siuntose keliauja…“ (case fixes) · why: „Daiktų pervežimo paslaugos apima itin platų spektrą…“, „Buitinės įrangos pervežimas, perkraustymas ir smulkios siuntos…“, „Daiktų pervežimas į užsienį kelių transportu trunka apie 3–4 paras…“ · why_media 9185835, 6407553, 7464731 · special: **example tags** (NEW nominatives from [S]) „Langai · Žoliapjovės · Buitinė įranga · Smulkios siuntos“ as large outline chips on paper · responsibilities: „Pakavimas“ — „Daiktų pervežimas – procesas, kurio sėkmė priklauso ir nuo paties kliento. …“ (single → callout) · prohibited: „Kitas aspektas – draudžiami siųsti daiktai. …“ · closing „Daiktų pervežimas į užsienį kelių transportu su „SGP pervežimai“ – tvarkingais ir patikimais mikroautobusais, geriausia kaina, operatyviai ir saugiai.“ · hero **36933446** · next 05.

**05 `automobiliu-pervezimas`** — h1 „Automobilių pervežimas“ · lead „Jei įsigijote automobilį svečioje šalyje ir norite jį atsigabenti namo arba patys pardavėte automobilį ir turite jį pristatyti pirkėjui į kitą šalį, siūlome savo paslaugas ir garantuojame saugų bei kokybišką automobilio pervežimą.“ · kv: Kryptys — Vokietija, Airija, Ispanija, Lietuva – į ir iš · Kelyje — traliuku apie 3–4 paros · Pristatymas — sutartu laiku į nurodytą vietą · Svarbu — „Jei gavėjo nerandame, pakartotinis atvažiavimas apmokestinamas papildomai.“ · routes: Automobilių pervežimas iš Airijos · iš Ispanijos · iš Vokietijos · intro: „Automobilių pervežimas Europoje – labai populiari paslauga…“, „Vežame automobilius iš / į Vokietijos…“ (case fix, approval) · why: „Automobilių pervežimas Europoje – gabename traliuku…“, „Operatyvumas – vienas esminių mūsų veiklos kriterijų…“, „Automobilių gabenimas – viena iš mūsų veiklos sričių…“ · why_media 29566910, 1606957, 1696742 · special: **„Traliuku“** media block — Self Hosted Video **34371915** (b/w, dark overlay, desktop only; poster 29566910 on phones) + „Tai nėra įprastinis krovinys – automobiliams pervežti reikalingas specialus transportas (dažniausiai naudojamės traliuku), teisės aktų bei kelių eismo taisyklių šalyse, kuriomis automobilis gabenamas, išmanymas.“ [S] · responsibilities: „Pristatymas sutartu laiku“ — „Automobilis pristatomas sutartu laiku į nurodytą paėmimo vietą. Jei gavėjo nerandame, pakartotinis atvažiavimas apmokestinamas papildomai.“ (callout) · prohibited „P“ · closing „Automobilių pervežimas su „SGP pervežimai“ – tik techniškai tvarkingu, specialiu transportu, su atsakingais ir važiavimo tarptautiniais maršrutais ypatumus žinančiais vairuotojais, geriausia kaina, operatyviai ir saugiai.“ · hero photo **29566910** (+ desktop header video 34371915 optional: off) · next 06.

**06 `motociklu-pervezimas`** — h1 „Motociklų pervežimas“ · lead „Jei užsienyje įsigijote motociklą ir svarstote, kaip operatyviai ir gera kaina jį pargabenti į kitą norimą šalį, siūlome savo pagalbą – pasirūpinsime, kad Jūsų motociklas reikiamą vietą pasiektų operatyviai, saugiai ir patrauklia kaina.“ („gera kainą“ → „gera kaina“, approval) · kv: Kryptys — iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos ir Airijos · Kelyje — 3–4 paros nuo krovinio paėmimo dienos · Pristatymas — nuo durų iki durų · routes: none (chips hidden) · intro: „Šiandieninės galimybės leidžia…“, „Orientuojamės į veiklą keliose Europos šalyse…“ · why: „Mūsų komandos teikiamos profesionalios paslaugos…“, „Nuo durų iki durų – tai principas…“, „Motociklo transportavimas trunka 3–4 paras…“ · why_media 2177200, 5713164, 4858429 · special: **origins + video** — chips „Ispanija · Prancūzija · Vokietija · Lenkija · Airija“ + Self Hosted Video **34308329** (motorcycle loaded onto a trailer; desktop autoplay in view; poster phones) · responsibilities: „Adresai ir gavėjas“ — „Labai svarbu nurodyti tikslius siuntinio paėmimo ir pristatymo adresus Europoje. Jei sutartu laiku gavėjas arba siuntos adresatas negali atiduoti / paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.“ [P] (callout) · prohibited „P“ · closing „Motociklų pervežimas kelių transportu su „SGP pervežimai“ – tik techniškai tvarkingomis transporto priemonėmis, vairuojant atsakingiems ir ilgametę patirtį turintiems vairuotojams, itin gera kaina, operatyviai, patikimai ir saugiai.“ · hero **4858429** (40% 60%) · next 07.

**07 `keleiviu-pervezimas`** (Google Ads landing — highest craft) — h1 „Keleivių pervežimas“ · lead „Jei Jums aktualus keleivių pervežimas iš Ispanijos, iš Vokietijos, iš Prancūzijos ir iš Airijos, taip pat jei prioritetą teikiate komfortui ir saugumui, siūlome savo paslaugas.“ · kv: Kryptys — Ispanija, Vokietija, Prancūzija, Airija – į ir iš · Kelyje — 3–4 paros · Pristatymas — nuo durų iki durų: keleiviai paimami iš jiems patogios vietos · Svarbu — „Kelionės metu visi keleiviai yra apdrausti.“ · routes: Keleivių vežimas į Airiją · į Ispaniją · į Vokietiją · į Prancūziją · submenu „Apie paslaugą · Principai · Patogumai · Privalumai · Užklausa“ · intro: „Kalbant apie pervežimo paslaugas Europoje…“ · **T4 replaced by „Principai“**: lead „Saugumas, operatyvumas, profesionalumas, komfortas ir patogumas – tai esminiai kriterijai…“ + 5 stacking cards as on /apie-imone/ (same edits; media 6720534, 36383706, 7541981, 17455631, 160483) · special **„Patogumai“**: Image With Hotspots (§4.26) on **36377055** · T6 replaced by **„Kokie dar privalumai?“** [S H5] as kv: Kaina — „Patraukli kaina – tai dar vienas aspektas, kurį galime paminėti prie mūsų paslaugos privalumų. …“; Pažintys — „Būtina paminėti ir tai, kad kelionė mikroautobusu dažnai tampa naujų pažinčių ir draugysčių pradžios tašku. …“; Draudimas — „Kelionės metu visi keleiviai yra apdrausti.“; Poilsio režimas — „Vairuotojai visada laikosi privalomo darbo ir poilsio režimo.“ (keys NEW) · T7 omitted · closing „Keleivių pervežimas su „SGP pervežimai“ – tik techniškai tvarkingais, naujais mikroautobusais, su atsakingais ir patyrusiais vairuotojais, labai gera kaina, visada patikimai ir operatyviai.“ · hero photo **27383867** (50% 65%) · next 08.

**08 `gyvunu-pervezimas`** — h1 „Gyvūnų pervežimas“ · lead „Saugiai ir patogiai perkraustysime Jūsų augintinį į kitą šalį Europoje.“ · kv: Kryptys — Ispanija, Prancūzija, Vokietija, Airija · Kelyje — apie 3–4 paros [P] · Pristatymas — „Paimame krovinį iš sutartos vietos ir pristatome gavėjui į rankas.“ · Svarbu — „Narvus gyvūnams pervežti turime mes.“ · routes: Gyvūnų pervežimas į Airiją · į Ispaniją · į Vokietiją · į Prancūziją · Šunų pervežimas · submenu „Apie paslaugą · Privalumai · Prieš kelionę · Kaina · Užklausa“ · intro: „Planuojate išvykti pasisvečiuoti…“, „Paslaugą teikiame keliose Europos šalyse…“, „Mikro autobusu pervežame visus naminius gyvūnus…“ („Mikro autobusu“ → „Mikroautobusu“, approval) · why: „Gyvūnų pervežimas nėra kiekvieno vežėjo paslaugų sąraše…“, „Mūsų komandoje – tik solidžią patirtį…“ („tiks“ → „tik“), „Gyvūnų gabenimas vykdomas vadovaujantis principu nuo durų iki durų…“ · why_media 3868901, 21767483, 1696742 · special **„Prieš kelionę“** (NEW title): Toggle Panels → **Animated Circle**, 5 items (titles NEW, texts verbatim): „Skiepai nuo pasiutligės“ — „Itin svarbus aspektas – gabenti perduoti gyvūnai turi būti sveiki, paskiepyti nuo pasiutligės. Tai būtina atlikti likus maždaug mėnesiui iki kelionės, kadangi praėjus mėnesiui po vakcinos reikia padaryti kraujo tyrimą.“ · „Veterinaro dokumentas“ — „Gyvūno šeimininkai privalo pateikti veterinaro išduotą dokumentą, jog gyvūnas yra sveikas ir gali keliauti iki numatytos vietos.“ · „Dokumentai ir identifikacija“ — „Negana to, visi gabenti perduoti gyvūnai privalo turėti dokumentus ir turi būti identifikuoti.“ · „Vaistai nuo helmintų“ — „Svarbu: prieš kelionę veterinaras turi duoti Jūsų gyvūnui vaistų nuo helmintų ir tai pažymėti augintinio pase.“ · „Maistas ir vedžiojimo priemonės“ — „Užtikrindami visa, ko reikia jų augintiniui, kelionės metu, pavyzdžiui, maistą, gėrimus. Narvus gyvūnams pervežti turime mes. Taip pat pridėkite ir priemones, reikalingas Jūsų gyvūnų vedžiojimui.“; plus **„Kaina“** (NEW title): 3 tiles „Narvo dydis“ · „Priežiūros sudėtingumas“ · „Atstumas“ (NEW labels) under „Gyvūnų gabenimo kaina yra individuali kiekvienu atveju ir ji paprastai priklauso nuo narvo dydžio, t. y. kiek gyvūnas užima vietos transporte, taip pat įtakos kainai turi gyvūno priežiūros sudėtingumas kelionės metu ir žinoma, atstumas, kurį nuvažiuojame.“ [S] · responsibilities: „Gavėjas sutartu laiku“ — „Sutartu laiku atvykus į gyvūno atidavimo vietą gavėjas turėtų mūsų laukti. Kitu atveju pakartotinis atvykimas apmokestinamas papildomai.“ (callout) · T7 omitted; before T8 a statement: „Mūsų patirtis rodo, jog šeimininkams kyla daug klausimų ir nerimo, planuojant augintinio pervežimą. …“ [S] · closing „Gyvūnų pervežimas su „SGP pervežimai“ – tik techniškai tvarkingais, naujais ir prižiūrimais mikroautobusais, vairuojant profesionaliems vairuotojams, visada patikimai ir operatyviai.“ · hero **32872983** (50% 45%) · next 09.

**09 `siuntu-pervezimas`** — h1 „Siuntų pervežimas“ · lead „Jei ir Jums aktualus siuntų pervežimas į Vokietiją, Ispaniją, Airiją ar Prancūziją, taip pat ir iš šių šalių, siūlome savo transportavimo paslaugas.“ · kv: Kryptys — Vokietija, Ispanija, Airija, Prancūzija – į ir iš · Kelyje — apie 3–4 paros nuo paėmimo [P] · Pristatymas — nuo durų iki durų · Įsipareigojimas — (3.4 p.) · Svarbu — „rekomenduojamas tarpas yra 5 centimetrai“ · routes: Siuntos į Airiją · į Ispaniją · į Vokietiją · intro: „Milžiniški siuntų srautai…“ · why: „Profesionali komanda yra esminis įrankis…“ („sklandžia“ → „sklandžią“), „Reikalingas skubios siuntos gabenimas? …“, „Siuntų pervežimas į užsienį vykdomas tik naujais, tvarkingais mikroautobusais…“ · why_media 4487517, 6407553, 4440774 · special **„Pakavimo gidas“** (NEW title): static SVG box section with a 5 cm dimension line between content and wall (ink lines, red dimension) + „Siuntai pakuoti netinka paprasta plėvelė, popierius, laikraščiai, medžiaginės pakuotės.“ [S] · responsibilities: „Turinys“ — „Siuntų siuntimas bus sėkmingas, jei pasitikėsime mūsų komanda…“; „Pakuotė“ — „Kitas aspektas – siuntos pakuotė. …“ · prohibited: „Pirmiausia – siuntos turinys. …“ · closing „Siuntų pervežimas su „SGP pervežimai“ – tvarkingais, naujais mikroautobusais, su patikimais vairuotojais, geriausia kaina, operatyviai ir saugiai.“ · hero **6170458** · next 10.

**10 `siuntu-pristatymas`** — h1 „Siuntų pristatymas“ · lead „Skubus siuntų pristatymas į namus – paslauga, garantuojanti didžiausią patogumą ir siuntėjui, ir gavėjui.“ · kv: Kryptys — Vokietija, Prancūzija, Ispanija, Airija – į ir iš · Kelyje — apie 3–4 paros nuo siuntos paėmimo dienos · Pristatymas — „Siuntiniai paimami iš siuntėjų ir atiduodami gavėjams į rankas.“ · Įsipareigojimas — (3.4 p.) · routes: Nuo durų iki durų · intro: „Skubus siuntų pristatymas į namus…“ („šias tris šalis“ → „šias šalis“, approval) · why: „Siuntų pristatymas užsienyje visada vykdomas…“, „Komanda – kitas aspektas…“ („daržo“ → „darbo“), „Nuo durų iki durų – tai principas…“ · why_media 4440774, 6407553, 7464731 · special **3-stop lane** (NEW labels) „Paimame iš siuntėjo → Kelyje apie 3–4 paras → Į rankas gavėjui“ · responsibilities: „Turinys ir pakuotė“ — „Siuntų pristatymas į namus bus sklandus, jei mūsų ir klientų bendradarbiavimas bus abipusis. …“ (callout) · prohibited „P“ · closing „Skubus siuntų pristatymas su „SGP pervežimai“ – naujais, tvarkingais mikroautobusais, geriausia kaina, visada patikimai ir saugiai.“ · hero **13456097** (55% 45%) · next 11.

**11 `perkraustymo-paslaugos`** — h1 „Perkraustymo paslaugos“ · lead „Todėl jei nusprendėte persikelti gyventi į kitą šalį Europoje, mūsų nebrangios perkraustymo paslaugos bus būtent tai, ko Jums reikia.“ (keep verbatim; the leading „Todėl“ reads fine after the H1 — client may shorten) · kv: Kryptys — Vokietija, Ispanija, Prancūzija, Airija – į ir iš · Kelyje — apie 3–4 paros · Pristatymas — nuo durų iki durų · Įsipareigojimas — (3.4 p.) · **Svarbu — „Pakrovimas ir iškrovimas į paslaugą neįeina“** (NEW condensation) · routes: Perkraustymo paslaugos kaina · intro: „Šiandien galime džiaugtis…“ („šį / iš“ fix) · why: „Perkraustymo paslaugos patrauklia kaina vykdomos tik naujais (2017–2018 metų)…“ (years removed), „Mūsų komanda yra tai…“, „Nuo durų iki durų – tai principas…“ („teisiai“ → „tiesiai“) · why_media 7464731, 9185835, 6407553 · special: **red-outline callout** „Pirmiausia – mes teikiame pervežimo paslaugas, į kurias neįeina pakrovimo ir iškrovimo darbai. Klientas turi pasirūpinti, kad baldai ir kiti daiktai, kuriuos reikia pervežti, bus pakrauti į mūsų transporto priemones, taip pat užtikrinti, kad pristatymo vietoje jie bus iškrauti.“ + note „Svarbu ir tai, kad jei turite augintinį, jį saugiai pervešime ne su baldais ir kitais namų apyvokos daiktais, o specialiu transportu, narvuose, sklandžiai ir patikimai.“ with link „Gyvūnų pervežimas →“ · responsibilities: „Pakavimas“ — „Kitas aspektas – tinkamas daiktų pakavimas. …“; „Gavėjas sutartu laiku“ — „Svarbu, kad gavėjas nurodytoje vietoje sutartu laiku lauktų mūsų, nes pakartotinis atvykimas bus apmokestinamas papildomai.“ · prohibited: „Į pakuotes nedėkite draudžiamų siųsti daiktų. …“ · closing „Perkraustymo paslaugos į užsienį su „SGP pervežimai“ – naujais, puikios būklės mikroautobusais, geriausia kaina, visada sklandžiai, operatyviai ir saugiai.“ · hero **4246238** (packed boxes; never 7464393) · next 01.

SEO: the 27 live child pages (e.g. `/…/kroviniu-pervezimas/kroviniu-pervezimas-i-airija`) → **301** to their parent service page; their names survive as T2 chips.

### 6.6 Pervežimų grafikas `/pervezimu-grafikas/` (added to the main nav)
1. **Compact header** (dark, 44svh desktop / auto phone) — breadcrumb; H1 „Pervežimų grafikas“; lead „Artimiausios išvykimo datos abiem kryptimis.“ NEW; stamp „● Atnaujinta rugsėjo 23 d.“ (from `updated`); bg texture **9807331** at 18 % + Parallax Subtle. No photo hero — the table is the hero.
2. **01 Lenta** (dark) — Tabs → **Minimal** „Visi · Airija · Ispanija“ (NEW labels), each tab = `[sgp_grafikas variant="table" routes="…"]` (all / lt-ie,ie-lt / lt-es,es-lt); groups „Iš Lietuvos“ / „Į Lietuvą“; every row full-width tap-to-call (§4.10); board note under the table. M40, M45, M14 (route codes only).
3. **02 Ką verta žinoti** (paper, rail) — kv: „Išvykimo laikas ir vieta — Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“ (key NEW) + delivery facts; the two ticket cards (§3.9).
4. **GS-Arrival**.

### 6.7 Siuntos sekimas `/siuntos-sekimas/`
1. **Compact header** — H1 „Siuntos sekimas“ (fixes the live band that said „Pervežimo paslaugos“); bg **35497082** + Parallax Subtle.
2. **01 Paieška** (paper + graticule) — large tracking field (§4.15); reads `?kodas=` on load and submits it.
3. **02 Rezultatas** — iframe `https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=…` (min-height 520 px, title „Siuntos sekimo rezultatas“) in a framed map-paper box; tool messages stay verbatim („Neįvestas siuntos kodas!“, „Toks siuntos kodas neegzistuoja!“). Demo: if the iframe cannot load from the demo origin, show a static card with those two messages as examples and the note „Demonstracinė versija – paieška veikia tik tikroje svetainėje.“ (NEW).
4. **03 Pagalba** — three small cards: „Neradote siuntos kodo?“ (NEW) → both LT numbers · „Siuntų pristatymas“ → service page · „Taisyklės“ → /taisykles/.
5. **GS-Arrival**. Meta description must be written (live is „<b>test</b>“). 301: `/pervezimo-paslaugos/siuntos-sekimas` → `/siuntos-sekimas/`.

### 6.8 Taisyklės `/taisykles/`
1. **Route header** — H1 „Siuntų siuntimo taisyklės“; lead „Paslaugos Mokėtojai (užsakovai) privalo susipažinti su šiomis taisyklėmis ir vadovautis jomis ruošiant siuntas ir užsakant paslaugas.“ (from the live meta, approval); button „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“; media **6169133**.
2. **01–06 Taisyklės** (paper) — **Tabs → Vertical Sticky Scrolling**, six tabs = the six numbered sections verbatim [P] („1. Siuntų tikrinimas“ … „6. Atvejai, kuriais įmonė neprisiima atsakomybės“); the tab list styled as a vertical lane with six stops (active filled). Clauses per §4.13. 4.2 → numbered ✕ list (12). **4.5 → fines table** (keys adapted, values verbatim — approval):
   | Radus siuntoje ar krovinyje | Bauda |
   |---|---|
   | Alkoholinių gėrimų | 1200 EUR už kiekvieną alkoholinio gėrimo vienetą |
   | Vaistų | po 1200 EUR už kiekvieną siuntoje rastą vienetą (ampulę, tabletę) |
   | Cigarečių | po 1200 EUR už kiekvieną rastą bloką (200 vnt.); ta pati bauda taikoma ir už mažesnį kiekį |
   | Tabako ar jo gaminių | po 1200 EUR už kiekvienus rastus 200 g; ta pati bauda taikoma ir už mažesnį kiekį |
   | Kitų 4.2 punkte nurodytų draudžiamų daiktų | 1200 EUR |
   followed by the full verbatim 4.5 text in a toggle „Visas 4.5 punkto tekstas“ (NEW label). 3.4 shown verbatim with the delivery-facts kv beside it.
3. **PDF** — Button Underline with download icon (repeated at the end).
4. **GS-Board**, **GS-Arrival**.

### 6.9 Kontaktai `/kontaktai/`
1. **Header (plain)** — dark 40svh, graticule 4 %, terminus ring on the rail (this page is the arrival); H1 „Kontaktai“; lead „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“ [P].
2. **01 Skambinkite** (dark) — two large tickets „Pervežimai į Airiją“ (LT +370 650 53161 big; IE +353 86 450 3104, UK +44 7566 878681) and „Pervežimai į Ispaniją“ (LT +370 638 28919 big; ES +34 602 547 929); every number is a ≥ 64 px tap target; stub = next departure from Lithuania (full date + relative). E-mail row: „El. paštas: saugiai.greitai.patikimai@gmail.com“ + „Kopijuoti“.
3. **02 Grafikas** — `[sgp_grafikas variant="timetable"]` all four routes (tap-to-call).
4. **03 Parašykite** (paper) — contact form (§4.14: „Jūsų vardas“, „El. pašto adresas“, „Žinutės tema“, „Žinutė“, „Siųsti“) + consent note.
5. **04 Kur važiuojame** — both-routes schematic (static, no tabs; IE leg dashed).
No address, map pin, opening hours, company code, social links (none exist). GS-Arrival hidden.

### 6.10 Privatumo politika `/privatumo-politika/`
1. **Header (plain)** — H1 „Privatumo politika“.
2. **Document** (paper) — left sticky mini-TOC (two stops: „Informacija“, „Slapukai (Cookies)“ [P H3]); right: „Informacija ruošiama...“ [P] **with a visible notice box** (3 px red left bar): „Privatumo politikos tekstas bus pateiktas prieš paleidžiant svetainę.“ (NEW, demo only; the client must supply a real GDPR policy); cookie table restyled as timetable rows (mono keys) — the listed Joomla cookies (`jpanesliders_…`, `joomsef_lang`) will not exist in WordPress: replace with the consent plugin's auto-generated list at launch; link „Norėdami pasitikrinti … spauskite čia.“ removed until a real endpoint exists (flagged).
No GS-Arrival. 301 `/privatumo-politika/policies` → `/privatumo-politika/`.

### 6.11 404 (`v2/404.html`; Salient 404 via Global Section)
Full-height dark row, bg **160483** graded, overlay 80 %; board tiles „4 0 4“ (flap, desktop); H1 „Maršrutas nerastas“ NEW; text „Šio puslapio nėra – bet mūsų mikroautobusai kursuoja toliau.“ NEW; buttons „Į pradžią“ (Signal) · „Pervežimų grafikas“ (Line); both LT numbers as small call buttons; GS-ServiceList (compact). The rail comes down, breaks into a dashed segment and ends in a neutral ring.

### 6.12 Titles, meta descriptions, redirects
| Page | `<title>` | Meta description |
|---|---|---|
| / | Visos pervežimo paslaugos \| sgp-pervezimai.lt | NEW „Keleivių, siuntų, automobilių ir krovinių pervežimai Lietuva – Airija ir Lietuva – Ispanija. Nuo durų iki durų, kelionė apie 3–4 paros.“ |
| /apie-imone/ | Apie įmonę \| sgp-pervezimai.lt | live („„SGP“ – esame įmonė įsikūrusi Lietuvoje…“) |
| /pervezimo-paslaugos/ | Pervežimo paslaugos \| sgp-pervezimai.lt | live („Profesionalios keleivių, krovinių, automobilių, gyvūnų, daiktų pervežimo paslaugos mikroautobusais. Susisiekite jau dabar!“) |
| /…/tarptautiniai-pervezimai/ | Tarptautiniai pervežimai Europoje (mikroautobusais) \| sgp-pervezimai.lt | NEW „Tarptautiniai pervežimai mikroautobusais: Lietuva – Airija ir Lietuva – Ispanija, pakeliui Lenkija, Vokietija, Belgija, Prancūzija.“ |
| service pages | live titles; „Gyvunų“ → „Gyvūnų“ | live descriptions except: automobiliu NEW „Automobilių pervežimas traliuku tarp Lietuvos, Vokietijos, Airijos ir Ispanijos. Kelionė – apie 3–4 paros, pristatymas sutartu laiku.“; keleiviu NEW „Keleivių pervežimas mikroautobusais iš Airijos, Ispanijos, Vokietijos ir Prancūzijos. Nuo durų iki durų, keleiviai apdrausti.“ |
| /pervezimu-grafikas/ | Pervežimų grafikas \| sgp-pervezimai.lt | NEW „Artimiausi išvykimai: Lietuva – Airija, Lietuva – Ispanija ir atgal. Tikslų laiką ir paėmimo vietą suderinsime telefonu.“ |
| /siuntos-sekimas/ | Siuntos sekimas \| sgp-pervezimai.lt | NEW „Įveskite siuntos kodą ir sužinokite, kur yra Jūsų siunta. Neradote kodo? Paskambinkite – pasakysime.“ |
| /taisykles/ | Taisyklės \| sgp-pervezimai.lt | NEW „Siuntų siuntimo taisyklės: tikrinimas, siuntėjo garantija, vežėjo atsakomybė, draudžiami daiktai, baudos ir pretenzijos.“ |
| /kontaktai/ | Kontaktai \| sgp-pervezimai.lt | NEW „Pervežimai į Airiją: +370 650 53161. Pervežimai į Ispaniją: +370 638 28919. El. paštas saugiai.greitai.patikimai@gmail.com.“ |
| /privatumo-politika/ | Privatumo politika \| sgp-pervezimai.lt | NEW „SGP pervežimai privatumo politika ir slapukų naudojimas.“ |
Fix canonicals (live ones double the domain), strip `gclid/gbraid` from `og:url`, new OG image 1200×630 (hero poster 29374299 graded + logo), one H1 per page, no meta keywords. 301s: 27 child pages → parent; `/pervezimo-paslaugos/siuntos-sekimas` → `/siuntos-sekimas/`; `/privatumo-politika/policies` → `/privatumo-politika/`; old PDF URL → new media URL. Keep Google Ads landing URLs (krovinių, automobilių, keleivių) identical.

---

## 7. Responsive, accessibility, performance

### 7.1 Breakpoints and rules
| Range | Name | Rules |
|---|---|---|
| ≥ 1280 | Wide desktop | Hero call column right; route tab map 7 / info 5; nav visible; all pinned effects |
| 1000–1279 | Desktop | Calls in a row under the lead; map 12 cols + info 2 cols; board cells 14 px padding; nav visible ≥1180, burger below |
| 691–999 | Tablet (Salient tablet) | No global rail, no ticker; header 68 px with red phone button + burger; hero height = content; next-line under H1; board 2×2 solid; services = vertical list with lane; pinned sections off (plain stacks); map full width (SVG ≥700 px); comfort/process vertical lanes; call bar visible; videos → posters; parallax off (Salient option) |
| 481–690 | Phone (Salient phone) | Body 16 px; gutter 16 px; SVG map → ordered list (<700); tickets stub below; kv 2 columns; stats 2×2; footer 1 column; tt rows `96px 1fr 20px`; dev toggle hidden |
| ≤ 480 | Small phone | Board 1 column; kv single column (key over value); call numbers 22 px; call bar numbers 15 px (fits 360 px) |
| Height ≤ 820 (≥1000 w) | Short desktop | Pinned services hide the lead |
| Height ≤ 760 (≥1000 w) | Laptop | Board note + „Vėliau“ hidden; pinned card image 20vh, summary 2 lines |
| Height < 620 (≥1000 w) | Very short | Services not pinned (horizontal scroll-snap list). In Salient (no height condition) the compact CSS above applies; verify 1366×657 on staging |
Global: `html,body{overflow-x:clip}`; wide tables scroll inside their own container; no horizontal page scroll at any width (tile verified 375–1440). Tap targets ≥ 44×44. Salient per-element "animate on mobile" only for the H1 word reveal and lanes.

### 7.2 Accessibility (WCAG 2.2 AA)
- `lang="lt"`; skip link „Pereiti prie turinio“ first in DOM; landmarks header/nav/main/footer; one H1 per page; heading order H1 → H2 (chapters) → H3.
- Contrast per §2.4; nothing under 12 px; placeholders ≥ 4.5:1; focus visible everywhere (2 px red outline, 3 px offset; `--fg` on red buttons).
- `tel:` links carry full `aria-label`s naming the direction; board/timetable visuals are `aria-hidden` with the label on the link; flap text has an sr-only copy; odometers expose the final value (`role="img"` + `aria-label`).
- Switchboard = native popover (focus management, Esc, light dismiss); menu traps focus while open, Esc closes, focus returns.
- Tabs: `role=tablist/tab/tabpanel`, `aria-selected`, arrow keys; toggle panels are buttons with `aria-expanded`.
- Pinned horizontal services: skip link, index link, focus scrolls the track, all cards reachable by Tab.
- Map: `role="img"` + `<title>`/`<desc>`; list alternative on phones.
- Forms: visible labels, `autocomplete` (name, tel, email), inline errors with `aria-invalid` + `aria-describedby`, success `role=status`.
- Motion: reduced-motion path per §5.5; pause controls on every autoplaying video (WCAG 2.2.2); pulses stop within ~5 s.
- Images: `alt_lt` from media.json; decorative textures `alt=""`; video backgrounds `aria-hidden`.
- Language quality: typographic quotes „…“, en dash with spaces for routes, no ALL CAPS headings.

### 7.3 Performance budget
| Item | Budget |
|---|---|
| LCP (4G, mid phone) | ≤ 2.5 s; LCP = H1 text (fonts preloaded) or hero poster |
| CLS | < 0.05 (fixed aspect ratios, fixed flap tile widths, fonts `display=swap` + metric-compatible fallbacks) |
| INP | < 200 ms (one passive rAF scroll handler; no layout reads in loops) |
| Fonts | 7 files × latin/latin-ext woff2 ≤ 190 KB; preload 2 |
| Custom CSS / JS (production) | ≤ 8 KB / ≤ 5 KB unminified (current ≈ 7 / 3.9 KB) |
| Hero video | desktop only, after poster: production ≤ 2.5 MB (re-encode 29374299, 1280×720, 8–10 s loop); poster ≤ 200 KB |
| Other videos | lazy (IO 200–300 px), paused off-screen, desktop only, SD: 4685871 (HD 3.8 MB allowed), 13707149 1.5 MB, 2386447 SD 3.3 MB (never HD), hover clips 1.3–2.6 MB on first hover, fine pointers only; `saveData` → posters |
| Photos | re-hosted WebP/AVIF (never hotlink Pexels in production); srcset 480/760/1100/1600/1920; cards 760 w ≈ 60–90 KB |
| Page weight | Phone first view ≤ 1.2 MB, full home ≤ 3 MB. Desktop first view ≤ 3.5 MB incl. hero video; full home ≤ 9 MB with all videos |
| Third parties | GTM + GA4 (Consent Mode v2) after consent; Turnstile only on pages with forms; no reCAPTCHA v2 |
| Salient | Delay JavaScript Execution ON (exclude `sgp-*.js`), lazy loading ON, image preloading for the hero poster only |

### 7.4 QA checklist (before client review)
Viewports 375×812, 390×844, 768×1024, 1024×768, 1280×800, 1366×657, 1366×768, 1440×800, 1920×1080 · no horizontal overflow · board fully visible above the fold on all desktop sizes · next departure visible in the first phone viewport · red ≤ ~5 % per viewport · no text < 12 px (snippet in Appendix D) · all `tel:` links correct (5 numbers) · keyboard-only pass (menu, switchboard, tabs, pinned track, forms) · VoiceOver/NVDA read the board and flap correctly · reduced-motion pass (macOS "Reduce motion") · Chrome, Safari, Firefox (lane fallbacks) · Lighthouse mobile ≥ 90 performance / 100 accessibility on home and one service page · Salient žymės labels present on every block.

---

## 8. Klientui

### 8.1 Naujas tekstas — reikia kliento patvirtinimo
Antraštės ir pagrindiniai tekstai
1. Pagrindinio puslapio H1 (vaizdinis): „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“
2. H1 paieškos sistemoms (nematomas): „Tarptautiniai pervežimai: Lietuva – Airija, Lietuva – Ispanija ir atgal“
3. Viršutinė etiketė: „Tarptautiniai pervežimai mikroautobusais“
4. Įžanga: „Visos pervežimo paslaugos – saugiai, greitai, patikimai. Keleiviai, siuntos, automobiliai, motociklai, gyvūnai ir perkraustymas nuo durų iki durų.“
5. Maršrutų antraštė: „Dvi kryptys. Keturios šalys pakeliui.“
6. Kelionės skyrius: „Du namai, vienas kelias tarp jų.“ ir „Kelionė trunka apie 3–4 paras – pasirūpinsime, kad laikas neprailgtų.“
7. Kelionės eigos etapai: „Kelyje apie 3–4 paras“, „Siuntos vietą galite pasitikrinti pagal siuntos kodą.“, „Pristatome gavėjui tiesiai į rankas. Jei sutartu laiku gavėjas negali paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.“
8. Paslaugų juostos pabaiga: „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“
9. Sutrumpinti paslaugų aprašymai: Negabaritiniai „Kroviniai, kurių matmenys didesni, nei leidžiama šalyse, per kurias jie keliauja.“; Daiktai „Langai, žoliapjovės, buitinė įranga ir kiti didesni ar mažesni daiktai.“; Automobiliai „Automobilius gabename traliuku – iš Airijos, Ispanijos, Vokietijos ir į jas.“; Motociklai „Iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos bei Airijos – nuo durų iki durų.“; Keleiviai „Atlenkiamos ir šildomos sėdynės, kondicionierius. Kelionės metu visi keleiviai apdrausti.“; Perkraustymas „Persikeliate gyventi į kitą šalį Europoje? Daiktus pervešime nuo durų iki durų.“
10. Žymos (chips): „Kroviniai apdrausti“, „Išankstinis planavimas“, „Mokate mažiau“, „Traliuku“, „Keleiviai apdrausti“, „Narvus turime mes“, „Skubios siuntos“, „Į rankas gavėjui“, „Apie 3–4 paros“, „Nuo durų iki durų“, „Langai · Žoliapjovės · Buitinė įranga · Smulkios siuntos“
11. Paslaugų grupės: „Kroviniai“, „Daiktai ir perkraustymas“, „Automobiliai ir motociklai“, „Keleiviai“, „Gyvūnai“, „Siuntos“
12. Duomenų lapo raktai: „Veikla“, „Kryptys“, „Taip pat“, „Principas“, „Draudimas“, „Vairuotojai“, „Kelyje“, „Pristatymas“, „Įsipareigojimas siuntoms“, „Svarbu“, „Išvykimo laikas ir vieta“, „Kaina“, „Pažintys“, „Poilsio režimas“
13. Statistikos užrašai: „Kryptys – Airija ir Ispanija – iš Lietuvos ir atgal“, „Paslaugos – tarptautinių pervežimo paslaugų“, „Kelyje – paros nuo paėmimo dienos“, „Pakeliui – šalys: Lenkija, Vokietija, Belgija, Prancūzija“
14. Pristatymo trukmės formuluotė (dvi eilutės): „Kelyje: apie 3–4 paros nuo paėmimo dienos“ ir „Įsipareigojimas siuntoms: per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos (Taisyklių 3.4 p.)“
15. Grafiko būsenos: „Artimiausi išvykimai“, „Artimiausias išvykimas“, „Artimiausias“, „po N d.“, „rytoj“, „šiandien“, „Vėliau: …“, „Grafikas atnaujinamas – skambinkite“, „Atnaujinta rugsėjo 23 d.“, „Visas grafikas“, „Visas pervežimų grafikas“, „Kitas išvykimas“ + „iš LT · po N d.“, „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“, filtrai „Visi / Airija / Ispanija“, grafiko įžanga „Artimiausios išvykimo datos abiem kryptimis.“
16. Žemėlapis: „Maršrutų schema · ne mastelis“, „maršrutas tikslinamas“, „Maršrutas“, „Tikslinama“, „Šalis pakeliui“, „išvykimas“, „atvykimas“, užuomina „Pakeliui – galite perduoti siuntą čia gyvenantiems artimiesiems.“
17. Taisyklių santrauka: skydelių pavadinimai „Draudžiama siųsti (12)“, „Pakavimas (4)“, „Gavėjas ir pristatymas“, „Baudos“, „Visas 4.5 punkto tekstas“, mygtukai „Visos taisyklės“, „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“, „Plačiau taisyklėse“, žyma „Svarbu“, baudų lentelės eilutės (4.5 p. pertvarkyta į lentelę), „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“
18. Paslaugų puslapiai: meniu „Apie paslaugą · Privalumai · Kliento atsakomybės · Draudžiami daiktai · Užklausa“ (keleiviams „Principai · Patogumai“, gyvūnams „Prieš kelionę · Kaina“), „Kryptys ir paslaugos“, „Kita stotelė“, „Kaip veikia dalinis krovinys“, „Pakavimo gidas“, „Prieš kelionę“ ir jo punktai („Skiepai nuo pasiutligės“, „Veterinaro dokumentas“, „Dokumentai ir identifikacija“, „Vaistai nuo helmintų“, „Maistas ir vedžiojimo priemonės“), kainos veiksniai „Narvo dydis“, „Priežiūros sudėtingumas“, „Atstumas“, „Iliustracinė nuotrauka“, „Iškrovimo technika – kliento atsakomybė“, „Pakrovimas ir iškrovimas į paslaugą neįeina“, „Atsakomybė už pakuotę“, „Tranzito šalių teisės aktai“, „Pakavimas ir adresai“, „Adresai ir gavėjas“, „Turinys ir pakuotė“, trijų žingsnių juosta „Paimame iš siuntėjo → Kelyje apie 3–4 paras → Į rankas gavėjui“
19. Siuntos sekimas: „Neradote siuntos kodo? Paskambinkite – pasakysime, kur Jūsų siunta.“, „Neradote siuntos kodo?“, kortelės pavadinimas „Siuntos kodas“, „Pagal siuntos kodą“, „11 paslaugų · 2 kryptys“
20. Forma: pavadinimas „Gauti pasiūlymą“ (mygtuko tekstas – esamas), pasirinkimas „Pasirinkite paslaugą“ + „Kita“, vieta „Iš kur, į kur ir kada?“, klaidos „Įrašykite vardą“, „Įrašykite telefono numerį“, „Patikrinkite el. pašto adresą“, „Pasirinkite paslaugą“, „Žinutė – bent 20 simbolių“, demonstracinė pastaba „Demonstracinė versija – duomenys niekur nesiunčiami.“, „Kopijuoti“ / „Nukopijuota“ / „El. pašto adresas nukopijuotas“. Siūlymas: „Kas Jus domina?“ tampa pasirinkimu iš 11 paslaugų + „Kita“.
21. Navigacija ir sistema: „Skambinti“, „Į Airiją“ / „Į Ispaniją“ (skambučių juosta), „Pauzė“ / „Leisti“, „Pereiti prie turinio“, „Praleisti paslaugų juostą“, „Visos paslaugos sąrašu“, meniu numeracija „00–07“, skyrių pavadinimai („Apie mus“, „Paslaugos“, „Maršrutai“, „Kelionėje“, „Kelionės eiga“, „Prieš siunčiant“, „Siuntos sekimas“, „Atvykimas“), „↑ Į pradžią“, poraštės sakinys „Visos pervežimo paslaugos: Lietuva – Airija – Lietuva, Lietuva – Ispanija – Lietuva. Saugiai, greitai, patikimai.“, „© 2026 SGP pervežimai. Visos teisės saugomos.“
22. Atsiliepimų vieta: „Čia bus tikri klientų atsiliepimai“, „Vieta rezervuota – išgalvotų atsiliepimų nenaudojame.“
23. Slapukų juostos tekstas: „Būtini slapukai reikalingi svetainei veikti. Analitikos slapukus naudosime tik gavę Jūsų sutikimą.“, mygtukas „Atmesti“
24. 404: „Maršrutas nerastas“, „Šio puslapio nėra – bet mūsų mikroautobusai kursuoja toliau.“, „Į pradžią“
25. Privatumo politika (demo): „Privatumo politikos tekstas bus pateiktas prieš paleidžiant svetainę.“; siuntos sekimo demo pastaba „Demonstracinė versija – paieška veikia tik tikroje svetainėje.“
26. Meta aprašymai (§6.12, pažymėti NEW) ir naujas OG paveikslėlis.

### 8.2 Esamo teksto pataisymai (reikia „taip / ne“)
1. Išbraukti „(2017–2018 metų)“ ir „DVD“ visuose paslaugų ir „Kodėl verta pasitikėti mumis?“ tekstuose; „naujausiais / naujais mikroautobusais“ palikti tik jei tai vis dar tiesa (kitu atveju – „techniškai tvarkingais“).
2. Rašybos klaidos: „sako žmogiškųjų“ → „savo žmogiškųjų“, „užtiktiname“ → „užtikriname“, „sklandžia kelionę/siuntinio kelionę“ → „sklandžią“, „daržo režimo“ → „darbo režimo“, „šaunamiejii“ → „šaunamieji“, „cigarecių“ → „cigarečių“, „baikotai“ → „boikotai“, „maišrai“ → „maištai“, „kokos“ → „kokios“, „tiks geriausius“ → „tik geriausius“, „Klejonė“ (sakinys išbraukiamas kartu su DVD), „puiki žino“ → „puikiai žino“, „teisiai į rankas“ → „tiesiai į rankas“, „šį / iš Airiją“ → „į Airiją ir iš Airijos“, „tam tiktų leidimų“ → „tam tikrų leidimų“, „gera kainą“ → „gera kaina“, „esminiai mūsų veiklos principas“ → „esminiai mūsų veiklos principai“, „Mikro autobusu“ → „Mikroautobusu“, „Siuntėjau nedalyvaujant“ → „Siuntėjui nedalyvaujant“, „dėlto“ → „dėl to“, „grąžinamą“ → „grąžinama“, „visus daiktai“ → „visi daiktai“, „į Ispanija ir atgal“ → „į Ispaniją ir atgal“, „išsiųti pasiūlymui parengtams“ → „išsiųsti pasiūlymui parengti“, „Gyvunų“ → „Gyvūnų“, „Mes už˛ kokybę“ (meta).
3. Linksnių klaidos: „į / iš Airiją, į / iš Ispaniją …“ → „į Airiją ir iš Airijos, į Ispaniją ir iš Ispanijos, į Vokietiją ir iš Vokietijos, į Prancūziją ir iš Prancūzijos“; „iš / į Vokietijos“ → „iš Vokietijos ir į Vokietiją“.
4. „Veiklą orientuojame į šias tris šalis“ (išvardytos keturios) → „į šias šalis“.
5. Telefono numerių rašymas suvienodinamas (numeriai nesikeičia): +353 86 450 3104, +44 7566 878681, +34 602 547 929.
6. Taisyklių 6.2 p. domenas „http://sgppervezimai.lt“ → „https://www.sgp-pervezimai.lt“; autorių teisių eilutė – „SGP pervežimai“, ne „sgppervezimai.lt“.
7. Puslapių pavadinimai: H1 „Apie įmonę“ (meniu – „Apie mus“); siuntos sekimo juostoje – „Siuntos sekimas“ vietoj „Pervežimo paslaugos“; „Pervežimų grafikas“ įtraukiamas į pagrindinį meniu.
8. Taisyklių 4.5 p. baudos pateikiamos lentele (tekstas nesikeičia, tik struktūra); visas punktas lieka išskleidžiamas.
9. Taisyklių puslapio įžanga paimta iš seno meta aprašymo („Paslaugos Mokėtojai (užsakovai) privalo susipažinti…“).

### 8.3 Turinio pastabos klientui (ką verta sutvarkyti prieš paleidžiant)
1. **Pristatymo trukmė nesutampa.** Paslaugų tekstuose – „apie 3–4 paras nuo paėmimo dienos“, Taisyklių 3.4 p. – „per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos“, o seno Taisyklių meta aprašymo tekste – „nuo 2 iki 3 parų“ ir „Siuntos išdalinamos per 3 dienas nuo atvykimo į šalį“. Naujame dizaine rodome dvi atskiras eilutes (įprasta kelionė ir įsipareigojimas). Prašome patvirtinti abi formuluotes; „2–3 paros“ nebenaudojama.
2. **Grafike nėra metų.** Datos („Spalio - 09d.“) be metų; naujoje sistemoje datas saugosime pilnu formatu (2026-10-09), lankytojams rodysime „Spalio 9 d.“, praėjusios datos pasislėps automatiškai. Reikia sutarti, kas ir kaip dažnai atnaujina grafiką (dabar – rankiniu būdu); nesant naujų datų rodysime „Grafikas atnaujinamas – skambinkite“. Išvykimo laikų ir paėmimo vietų svetainėje nėra – to ir neišgalvojame.
3. **Maršrutas į Airiją nepatvirtintas.** Tekstai sako, kad maršrutai „apima“ Lenkiją, Vokietiją, Belgiją ir Prancūziją, o Airijos kontaktuose yra JK numeris. Kuriuo keliu važiuojama į Airiją (per JK ar keltu iš Prancūzijos / Belgijos / Nyderlandų)? Kol nepatvirtinta, schemoje Airijos atkarpa pažymėta „maršrutas tikslinamas“, kelto nuotraukų nenaudojame. Taip pat patvirtinkite, ar į Ispaniją važiuojama per Belgiją.
4. **Nėra įmonės rekvizitų.** Svetainėje nėra juridinio pavadinimo, įmonės kodo, PVM kodo, adreso, darbo laiko. Paslaugas teikiančiai įmonei (ir pagal BDAR) jie reikalingi – pateikite, įtrauksime į poraštę ir kontaktus. Kol negauta – nieko neišgalvojame.
5. **Privatumo politika neparengta.** Yra tik „Informacija ruošiama...“ ir seno Joomla slapukų lentelė (dalies slapukų WordPress nebeliks). Reikia tikro BDAR teksto (duomenų valdytojas, tikslai, saugojimo terminai, teisės), o nuoroda „spauskite čia“ veda į Joomla adresą, kurio nebeliks.
6. **Slapukų juosta neatitinka BDAR.** „Sutikdami, paspauskite mygtuką „Sutinku“ arba naršykite toliau“ – numanomas sutikimas negalioja; reikia mygtuko „Atmesti“ ir išankstinio analitikos išjungimo (pasiūlytas tekstas – §8.1 p. 23).
7. **Pasenusi informacija:** „nauji (2017–2018 metų) mikroautobusai“ (2026 m. – 8–9 metų), DVD patogumų sąraše, Google Analytics UA (neveikia nuo 2023 m. – reikia GA4), reCAPTCHA v2 (siūlome Cloudflare Turnstile).
8. **Negabaritiniai kroviniai „tik naujais mikroautobusais“** – mažai tikėtina; patvirtinkite, kokiu transportu vežate negabaritinius krovinius, ir ar tinka nuotrauka / vaizdo įrašas su sunkiasvore technika (35332902, 19552565). Kitaip pakeisime.
9. **Rašybos ir linksnių klaidos** – sąrašas §8.2 (dalis jų yra teisiniame taisyklių tekste, todėl be Jūsų pritarimo nekeičiame).
10. **SEO problemos:** kiekviename puslapyje H1 = „Pervežimas“ (logotipe); sugadinti canonical adresai (dvigubas domenas); siuntos sekimo meta aprašymas „<b>test</b>“; `og:url` su Google Ads parametrais; dubliuotas siuntos sekimo URL; neveikiantis OG paveikslėlis; meta raktažodžiai – atsitiktiniai žodžiai. Naujoje svetainėje visa tai sutvarkoma (§6.12).
11. **27 vaikiniai puslapiai** (pvz., „Krovinių pervežimas į Airiją“) – naujoje struktūroje jų nėra; siūlome 301 nukreipimus į pagrindinę paslaugą. Jei šie puslapiai gauna Google Ads srauto, galime vėliau sukurti juos iš to paties šablono.
12. **„Vietiniai pervežimai“** šoniniame meniu veda į neveikiančius puslapius (HTTP 404) – naujoje svetainėje jų nėra; patvirtinkite, ar tokios paslaugos teikiamos.
13. **Nuotraukos.** Demo naudoja Pexels nuotraukas; keleivių salono taškai (Image With Hotspots) ant iliustracinės nuotraukos – prieš paleidimą reikia Jūsų mikroautobuso salono nuotraukos. Labai praverstų ir kelios tikros Jūsų nuotraukos (mikroautobusai, pakrovimas, vairuotojai) vietoje senos galerijos.
14. **Atsiliepimai.** Svetainėje jų nėra; vieta rezervuota. Jei turite tikrų (pvz., „Google“ atsiliepimai), atsiųskite – išgalvotų nenaudosime.
15. **Pristatymo sąlygos „Perkraustymo paslaugose“:** pakrovimas ir iškrovimas neįeina – tai pabrėžta; patvirtinkite, kad taip ir yra.
16. **Kontaktinis el. paštas** – „Gmail“ adresas; verta apsvarstyti domeno adresą (pvz., info@sgp-pervezimai.lt) – tai didina pasitikėjimą. Socialinių tinklų ir pokalbių programėlių nuorodų nėra – jei naudojate „WhatsApp“ / „Viber“, galime pridėti.
17. **Kainos nenurodytos** (tik „geriausia kaina“) – dizainas tam paruoštas („Pasiūlysime telefonu“), bet jei norite rodyti bent orientacines kainas, jas reikėtų pateikti.

---

## Appendix A — `[sgp_grafikas]` mu-plugin outline (PHP, ≈ 3 KB)
```php
<?php /* Plugin Name: SGP grafikas */
const SGP_ROUTES=['lt-ie'=>['Lietuva','Airija','LT → IE','out','+37065053161','+370 650 53161'],
 'lt-es'=>['Lietuva','Ispanija','LT → ES','out','+37063828919','+370 638 28919'],
 'ie-lt'=>['Airija','Lietuva','IE → LT','in','+353864503104','+353 86 450 3104'],
 'es-lt'=>['Ispanija','Lietuva','ES → LT','in','+34602547929','+34 602 547 929']];
add_action('acf/init',fn()=>acf_add_options_page(['page_title'=>'Pervežimų grafikas','menu_slug'=>'sgp-grafikas','capability'=>'edit_pages']));
add_action('acf/save_post',function($id){ if($id==='options') update_field('updated',wp_date('Y-m-d'),'options'); });
add_shortcode('sgp_grafikas',function($a){
  $a=shortcode_atts(['variant'=>'board','routes'=>'lt-ie,lt-es,ie-lt,es-lt','limit'=>0],$a);
  $today=wp_date('Y-m-d',null,new DateTimeZone('Europe/Vilnius')); $rows=get_field('routes','options')?:[];
  $data=[]; foreach($rows as $r){ $d=array_filter(array_map(fn($x)=>$x['date'],$r['dates']?:[]),fn($x)=>$x>=$today); sort($d); $data[$r['key']]=$d; }
  $keys=array_filter(explode(',',$a['routes']),fn($k)=>isset(SGP_ROUTES[$k]));
  // soonest across $keys, then render the variant with the markup contracts of §3.5/§3.6/§4.1/§4.10/§4.11/§3.9
  // (template partials in /mu-plugins/sgp/views/{board,timetable,table,ticker,stub,next}.php)
  ob_start(); include __DIR__."/sgp/views/{$a['variant']}.php"; return ob_get_clean();
});
add_action('acf/save_post',fn()=>do_action('litespeed_purge_all')); // or the host's cache purge hook
```
Month/relative formatting helpers mirror the JS (`MG`, `MA`, `rel()`, `joinDates()` in the tile). Zero-code fallback: the Global Section keeps a hand-typed board in the same markup.

## Appendix B — Custom JS load order (production)
`sgp-sched.js` (relative labels, past-date hiding, soonest, ticker fit) → `sgp-flap.js` → stops IO → hover video → video pause → switchboard hook / copy / `--rail-end` / tracking `?kodas`. One file (`sgp.js`, ≈ 3.9 KB unminified), `defer`, footer, excluded from Delay JS. Each block starts with a feature/element guard and exits early.

## Appendix C — Build order (recommended)
1. Theme Options (§2.9) + Custom CSS tokens (§2.1) + fonts. 2. Global Sections (§6.0) incl. ACF + shortcode. 3. Home (§6.1) — prototype Horizontal Scrolling + stops IO and the rail on staging first (§3.1, §3.4 checks). 4. Service template (§6.5) + 11 pages. 5. Remaining pages. 6. Redirects, meta, OG, consent, GA4. 7. QA (§7.4).

## Appendix D — QA snippets (paste in the browser console)
```js
// 1 · horizontal overflow (must be 0)
document.documentElement.scrollWidth - innerWidth
// 2 · rendered text smaller than 12 px (SVG text scaled by its viewBox); must return []
(()=>{const out=[];document.querySelectorAll('body *').forEach(el=>{if(el.closest('.sgp-sr,.sr,script,style,title,desc'))return;
 if(![...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim()))return;const cs=getComputedStyle(el);if(cs.display==='none'||cs.visibility==='hidden'||!el.getClientRects().length)return;
 let fs=parseFloat(cs.fontSize);const svg=el.closest('svg');if(svg&&svg.viewBox.baseVal.width)fs*=svg.getBoundingClientRect().width/svg.viewBox.baseVal.width;
 if(fs<11.95)out.push([el.tagName,String(el.className).slice(0,40),fs.toFixed(1),el.textContent.trim().slice(0,30)])});return out})()
// 3 · every tel: link (must be exactly the 5 numbers)
[...new Set([...document.querySelectorAll('a[href^="tel:"]')].map(a=>a.getAttribute('href')))]
```
