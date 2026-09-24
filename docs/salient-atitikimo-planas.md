# SGP v2 → Salient conformance plan („SGP v2 identity, built the Salient way“, 18.2.1)

**Date:** 2026-09-24 (revision 2, after the lead's direction decision) · **Theme:** Salient **18.2.1**, Salient Core 3.1.5, Salient WPBakery 8.7.3 (the owner's licence). Every option below was checked against that code, not the 18.3 web docs.
**Status:** binding plan for the v2 rebuild. It keeps the „Maršruto linija“ identity (palette, type, dark/paper chapters, content, URLs, phone-first rules) and rebuilds **every block from native Salient 18.2.1 elements and options**, emulated in the static demo by a Salient emulation kit (§5).
**Inputs:** `salient-18-2-1-parinktys.md` (ground truth, "P§"), `salient-demo-analize.md` (Harbor / Architect / Tether), `salient-auditas.md/.json` (current state, 129 blocks), `dizaino-sistema.md` (v2 system, "DS§"), `turinys-*.md`, `turinio-pataisos.md`, `media.json`. Theme code was read in the scratchpad only; nothing from it is copied into the repo.
**Rejected alternative (reference only):** `docs/kryptys/salient-tile-harbor.html` — the Harbor-white / Inter Tight / pill style tile of revision 1. The lead rejected it as the main direction (too generic, and it drifts back to the rejected v1 demo: Inter Tight, pill buttons, giant wordmark). It stays in the repo as a comparison file; nothing in this plan may borrow its look.
**Precedence:** this plan wins over `dizaino-sistema.md` for construction (which Salient element and option builds a block), motion values and file architecture. **DS§2 stays the source of the identity** (colours, contrast table, type roles, image grade) except the parts §1.3 drops. Content, copy approvals (DS§8), titles/meta (DS§6.12), redirects and media exclusions stay as in `dizaino-sistema.md`.

---

## 1. Decision

> **Lead's decision (binding): „SGP v2 identity, built the Salient way.“**

**Base demos are pattern libraries, not skins.** No demo's Theme Options are imported. We borrow *structures* only:
- **Harbor** — the departures ticker as a Global Section above the header, the full-height hero Section with a glass band (Inner Row + Backdrop Filter), horizontally scrolling colour sections for services, the photo stats band with Scroll-Position Opacity text, the pricing-style route columns, the closing CTA row with Content Trail.
- **Architect** — the inner-page head (H1 + a column of section links), the header phone button with *Persist In Mobile Navigation Header* and *Button Shadow and Scale on Hover*, Fancy Box *Image Above Text*, outline Scrolling Text, *Slight Zoom Out Reveal* rows, two-speed parallax image columns.
- **Tether** — Toggle Panels *Minimal Shadow* for checklists and the tidy card grid built from Columns with hover colours.

**The direction in ten sentences.**
1. **Identity stays v2:** dark cinematic *asphalt* chapters (`#0B0E10` / `#0F1417` / `#161D21`) alternate with light *paper* chapters (`#F5F7F6` / `#EAEEED`), text in ink `#1C1D1D` / snow `#F2F4F3`, and brand red `#EF4539` works as a **signal** (call buttons, primary arrows, active states, hotspots, the red underline and road lines) — never as a section background; small red text on paper uses `#C4301E`.
2. **Type stays v2 and is set only in Theme Options → Typography:** Barlow Condensed 600 (H1, H3, H4) and 500 (H2, statements, numbers), Barlow 400/500/600 for text, navigation and buttons; IBM Plex Mono survives **only** as the *Form and Category Labels* slot, which Salient itself applies to Badge (*Inherit Typography From: Label*), form labels and Material tab links — so the mono labels cost **zero** custom CSS.
3. **Chapter labels** are **Badge → Badge Style: Minimal Line** (Salient draws a 1 px line before the text) in the Label typography — the old waypoint, without rings, rail or graticule.
4. **Crisp, not round:** *Button Styling* **Slightly Rounded W/ Shadow**, *Button Roundness* **3**; Button (`nectar_cta`) roundness 3; Column / Toggle / Dropdown / Sticky Sections radius **3**, badges **3** (the smallest non-zero Badge preset), images **0**; no pills, no 10–100 px radii.
5. **Header is Salient's own:** *Default Layout*, full width, transparent over every page's dark first chapter, then a solid asphalt bar (`#0F1417`, *Header BG Opacity* 90, *Header Blur Background*) that shrinks with *Header Resize On Scroll*; *Animated Underline* hover; one red element — the „Skambinti“ menu button (*Button Accent Color*, `fa-phone`, *Persist In Mobile Navigation Header*, Mega Menu → GS-Telefonai); the departures ticker is a **Scrolling Text** Global Section *In Navigation Top Before Scrolling*.
6. **Heroes are video/photo Sections** (*Parallax Fade*) with the v2 H1 as **Animated Text** and a **glass band** (Inner Row + *Backdrop Filter → Blur*) carrying the next departures as text and both per-direction call buttons.
7. **The route idea is kept only through native elements:** Animated Text line-by-line H1 („Lietuva – Airija. / Lietuva – Ispanija. / Ir atgal.“), **Divider → Animate Line** as short red road lines, **Highlighted Text → Regular Underline** in red, **Icon List** numbered stations (01 → 02 → 03), **Fancy Unordered List**, **Image With Hotspots** on a static route-map image (`assets/img/marsrutai.svg`) and **Scrolling Text** of route/country names.
8. **Structure comes from Salient's interactive elements:** Sticky Content Sections (Horizontal Scrolling, Pinned *Scale* / *Blurred Scale* / *Overlapping* with Stacked Appearance, Sticky Media), Fancy Box styles, Horizontal List Item hover rows, Milestones, Toggle Panels (*Animated Circle*, *Minimal Shadow*), Tabs (*Minimal*, *Toggle Button*, *Vertical Sticky Scrolling*), Page Submenu, Global Sections.
9. **Motion is rich and entirely native, with 18.2.1's real numbers:** row parallax at Subtle 0.20 / Regular 0.28 / Medium 0.40 / High 0.60, Background Layer Animation (*Zoom Out Slowly* 8 s, *Slight Zoom Out Reveal* 1.3 s, *Clip Path Inset* on scroll), Image *Reveal Rotate*, Inner Column *Mask Reveal* 1.3 s, Column *Scroll Position Advanced*, Cascading Images with layer parallax, **Color Change Section** (0.8 s) between dark and paper chapters, **View Transitions → Vertical Reveal** (1.3 s), **Lenis** strength 60 — plus our reduced-motion layer, because 18.2.1 has none.
10. **Result:** 99 % of blocks predicted native (81 % NATIVE + 18 % NATIVE+CSS, §3.13; planned ≥ 95 %), one production custom layer **`sgp-custom.css` ≤ 250 lines** + **`sgp-custom.js` ≤ 30 lines**, no PHP, no ACF, no shortcode; the schedule is typed monthly into **four Global Sections** by a non-developer.

### 1.1 What changes vs v2 „Maršruto linija“ (same look, native construction)

| Area | v2 now (custom) | New — Salient 18.2.1 |
|---|---|---|
| Header | *Centered Menu*, hides on scroll, JS recolouring, square red „Skambinti“ opening a popover | *Header Layout* **Default Layout** · *Full Width Header Content* · transparent → asphalt bar with blur · *Header Resize On Scroll* (84 → ≈ 70 px) · *Hide Until Needed* OFF · *Animated Underline* · „Skambinti“ = menu item *Button Accent Color* + `fa-phone` + Mega Menu **GS-Telefonai** (full values §2.4) |
| Ticker | Dark strip rendered by `[sgp_grafikas ticker]`, relative „po N d.“ | **GS-Išvykimai** → *In Navigation Top Before Scrolling* · **Scrolling Text** (*Slower* 30 s, divider „✦“ red, *Mask Edges*) · full dates typed monthly |
| Off-canvas | „Fullscreen Split“ + line-diagram menu (custom) | *Off Canvas Menu Style* **Fullscreen Cover Split** (phones/tablets) · Off Canvas Navigation Barlow Condensed 40 px · right side = **GS-Telefonai** (*Off Canvas Menu Meta Area*) |
| Typography | 3 families, mono via `.sgp-mono` custom class | same 3 families, **all through Typography slots** (H1–H6, Body, Navigation, Nectar Button, Off Canvas, *Form and Category Labels* = Plex Mono) |
| Labels | `02 · PASLAUGOS` + ring + hairline on the rail | **Badge → Minimal Line**, *Inherit Typography From: Label* („02 · Paslaugos“ rendered uppercase by the slot) |
| H1 | Raw HTML route H1 with drawn dashes | **Animated Text** (*Text Element* H1, *Word Animations: Reveal*, Stagger) + **Divider → Animate Line** (red, 2 px, 96 px) |
| Buttons | 2 px square, split icon cell, „Line“ outline | **Button** (`nectar_cta`): *Arrow Circle Animation* (primary/calls), *See Through* (on photos), *Underline* (inline), *Text Reveal Wave* (link lists) · **Legacy Button → Regular** where the −3 px shadow lift is wanted (the lift is native only for Legacy Button and submit buttons under *Slightly Rounded W/ Shadow*) |
| Surfaces | `.on-dark/.on-light` + graticule + rail zone | Row *Background Color* + *Text Color* Light/Dark + **Color Change Section**; no graticule, no rail zone |
| Cards | Tickets with notches, 16:11 cards + mono index, hover videos | **Column** (BG + *Background Color Hover* + radius 3 + *Column Link*), **photo columns** (BG image + *Color Overlay Opacity → Opacity Hover*), **Fancy Box** *Image Above Text* 3:2 / *Description on Hover* |
| Services | Horizontal „road“ of 11 cards + counter; pinned „Stacking“ | **Sticky Content Sections → Horizontal Scrolling** (6 groups, *Link Mouse Indicator*) · **Pinned Sections → Blurred Scale + Stacked Appearance + Section Navigation** |
| Schedule | Split-flap board + `[sgp_grafikas]` (8 variants, JS) | 4 hand-typed Global Sections (GS-Išvykimai, GS-Artimiausi, GS-Grafikas Airija, GS-Grafikas Ispanija) built from Scrolling Text, Badge, Responsive Text and Horizontal List Items; the demo renders them from `grafikas.json` at build time |
| Maps | Inline SVG maps + JS draw, tabs | **Image With Hotspots** (*Numerical*, *Tooltip Show On Hover*, Accent) on the static `assets/img/marsrutai.svg` |
| Indexes | Custom sticky lane indexes with filling rings | **Page Submenu** (*Sticky?* ✓) · **Tabs → Vertical Sticky Scrolling** · inner-head link columns |
| Accordions / tabs | `.sgp-acc`, custom tabs | **Toggle Panels → Animated Circle / Minimal Shadow** · **Tabs → Minimal / Toggle Button / Vertical Sticky Scrolling** |
| Motion | easeOutExpo 1300, Lenis 50, JS parallax, rail draw, odometer | *Column/Image Animation Easing* **easeOutExpo** · *Timing* **1300** · Lenis **60** · element options only (full list §2.6) · Milestone *Motion Blur Slide In* |
| Video | Autoplay BG videos + custom pause + SD/HD switch + hover videos | Section/Row **Video Background** (MP4; poster = Row *Video Preview Image* or Section *Background Image*; *Disable Video Backgrounds On Mobile* ON) + a pause Button (≈ 10 lines in `sgp-custom.js`, WCAG 2.2.2) · on-demand clips via **Video Lightbox → Play Button With Image – Mouse Follow** |
| Page transitions | Horizontal Gradient Wipe | *Transition Method* **View Transitions API (Modern)** · *Transition Effect* **Vertical Reveal** |
| Footer | GS-Footer, ring bullets | **GS-Poraštė** → *Location: Footer*, 4 columns of Text Reveal Wave links, animated hairline Divider, © line — **no giant wordmark, no animated gradient** (v1 signatures) |

### 1.2 What is kept from v2 (not negotiable)
- **Palette, contrast table and red budget** (DS§2.4): red ≤ ~5 % of any viewport; never a section background, never body text; small red text only `#C4301E` on paper or `#EF4539` on asphalt-900/950.
- **Typography roles** (DS§2.3) mapped to Salient slots (§2.3); nothing under 12 px; 17 px body (16 px on phones).
- **Dark/paper chapter rhythm**; every page starts with a dark first chapter (so the transparent header always sits on dark).
- **Video/photo hero with the next departures** and both per-direction call buttons in the first screen.
- **Phone first:** header „Skambinti“ (persists on phones), the mobile call bar (GS-Skambučių juosta), per-direction numbers everywhere (LT lines for outbound, destination lines for inbound).
- All 21 pages, URLs, `<title>`/meta, one H1 per page, the v2 H2s and chapter order, verbatim copy + approved fixes (DS§6, DS§8, `turinio-pataisos.md`), media ids and exclusions.
- Only true facts: 2 kryptys · 11 paslaugų · 3–4 paros · 4 šalys pakeliui; no reviews until real ones exist; forms are demo-only.
- The **„Salient žymės“** developer overlay (every block keeps `data-salient`).

### 1.3 What is dropped (custom-only, no Salient equivalent)
Split-flap tiles and the departures board · relative „po N d.“ statuses (stale in hand-typed Global Sections) · the continuous drafting rail, stop rings, waypoint ring labels, graticule paper and crop marks · the Raw HTML route H1 (→ Animated Text) · inline SVG maps with JS (→ Image With Hotspots on a static image) · the Popover switchboard (→ header button + GS-Telefonai mega menu / off-canvas meta area + plain anchor `/kontaktai/#skambinkite`) · custom sticky indexes and scroll-spies (→ Page Submenu / Tabs Vertical Sticky Scrolling) · lane charts (grafikas „Laiko juosta“, taisyklių terminai, 404 broken rail) · hover videos · the copy-email button · SD/HD video switching · custom accordion/tab visuals · the odometer · the `[sgp_grafikas]` shortcode concept (the schedule = hand-edited Global Sections; the demo may still render them from `src/data/grafikas.json` at build time).
**Also not used** (they belong to the rejected Harbor tile or v1): Inter Tight, pill buttons (radius ≥ 20), white Harbor canvas, „(Label)“ parentheses, the footer wordmark with Animated Gradient, fit-text giant headings.

### 1.4 Adopted Salient patterns → where they appear

| Pattern (18.2.1 element / option) | Source demo | Used in |
|---|---|---|
| Scrolling Text Global Section *In Navigation Top Before Scrolling* | Harbor | G1 (all pages) |
| Section *Parallax Fade* hero + Inner Row *Backdrop Filter → Blur* glass band | Harbor | H1, T1, S1, E1 |
| Sticky Content Sections → *Horizontal Scrolling* (+ *Link Mouse Indicator*) | Harbor | H3 |
| Pinned Sections *Scale / Blurred Scale / Overlapping* + *Stacked Appearance* | Salient core | A7, P3, T4, X8 |
| Sticky Media, Scrolling Content | Salient core | S5 |
| Animated Text *Scroll Position: Opacity* on a parallax photo band | Harbor | H5 |
| Pricing-style route columns (Border Advanced, Price Typography, Fancy UL) | Harbor | G12 |
| Content Trail on the closing CTA | Harbor | G24 |
| Inner head: H1 + section-link column | Architect | §3.3 (all inner pages) |
| Header phone button *Persist In Mobile Navigation Header* + *Button Shadow and Scale on Hover* | Architect | G4 |
| Fancy Box *Image Above Text* (+ *Description on Hover*), outline Scrolling Text, *Slight Zoom Out Reveal* | Architect | S11 / K4, H4, T6, §3.3 |
| Toggle Panels *Minimal Shadow* checklist, Column colour grid with hover | Tether | X5, X6, P2 |
| Color Change Section, Clip Path Inset (Scroll Position), View Transitions, Lenis | Salient core | G30, H5, A2, G31 |

### 1.5 Style reference
There is **no new style tile** for this revision: the reference look is the current v2 demo (`/`, served from the repo root) for identity, and §2 + §3 for construction. The shared team's Wave 1 kit page (`/kit/`, §5.2) becomes the living style tile. `docs/kryptys/salient-tile-harbor.html` is the rejected alternative.

---
## 2. Tokens and Theme Options (v2 identity × Salient 18.2.1 values)

Everything in this section is **set in Salient Theme Options** in production. The demo mirrors it in `assets/css/theme-options.css` (§2.7) — that file is *not* custom code, it is a stand-in for the Theme Options panel. Labels are the exact 18.2.1 admin labels (`options-config.php`); values in `code` are the saved values where they differ.

### 2.1 Colours

| Theme Options field | Value | Role |
|---|---|---|
| General Settings → Accent Colors → **Accent Color** | `#EF4539` | Signal red: call buttons, primary arrows, hotspots, Highlighted Text, road Dividers, ticker „✦“, Section Navigation dots, active states |
| **Extra Color 1** | `#0F1417` | Asphalt-900: dark chapters, dark buttons on paper, HLI hover fill on paper |
| **Extra Color 2** | `#F5F7F6` | Paper-50: paper chapters, light buttons on asphalt, HLI hover fill on asphalt |
| **Extra Color 3** | `#C4301E` | Red ink: small red text on paper (5.2:1), Badge labels on paper |
| **Theme Color Gradient** | `#EF4539 → #C4301E` | reserved (no gradient element is planned) |
| **Theme Color Gradient #2** | `#0B0E10 → #161D21` | reserved |
| Styling → **Primary Background Color** | `#F5F7F6` | page background (Color Change Section animates it) |
| Styling → **Primary Text Color** / **Primary Text Color (Light)** | `#1C1D1D` / `#F2F4F3` | ink / snow |

**Extended v2 palette** (used as custom colours inside element options; the palette pickers above cover the rest): asphalt-950 `#0B0E10`, asphalt-800 `#161D21`, asphalt-750 `#1A2227`, asphalt-700 `#222B30` · paper-100 `#EAEEED`, paper-200 `#D9DFDE`, paper-300 `#C3CBCB`, white `#FFFFFF` · ink-2 `#4A5358` · fog `#9AA6AB` · signal-lit `#F4604F` (button hover, small red on asphalt-800) · hairlines `rgba(28,29,29,.12)` / `.26` on paper, `rgba(242,244,243,.12)` / `.26` on asphalt · glass `rgba(11,14,16,.55)` · scrim `rgba(11,14,16,.72)`.
**Contrast rules** = DS§2.4 unchanged. Text on the red button is asphalt `#0F1417` (4.9:1); its hover is `#F4604F` with the same text (5.9:1) — never white text on red below 24 px.

### 2.2 General Settings

| Group → field | Value | Why / effect |
|---|---|---|
| Styling → *Theme Skin* | **Material** | Material skin is what makes Tabs links use the Label typography (mono) |
| Styling → **Button Styling** | **Slightly Rounded W/ Shadow** | radius from *Button Roundness*; Legacy Buttons and submit buttons lift −3 px with `0 20px 38px rgba(0,0,0,.16)` on hover |
| Styling → **Button Roundness** | **3** | crisp v2 corners (v2 had 2 px; 3 is the nearest that also reads on 44 px buttons) |
| Styling → *Column Spacing* | 30px | ≈ v2 24 px gap at the 1320 container |
| Styling → *Animated Underline Type* / *Thickness* | **Left to Right Fancy** / **1** | inline links and Button → Underline |
| Styling → *General Link Style* | Basic Underline | text links underlined (v2 §4.5) |
| Functionality → **Smooth Scrolling** / *Strength* | **On** / **60** | Lenis 1.1.13, `lerp = 0.17 × (1.5 − 0.60) = 0.153`; desktop only, never Safari/iOS/touch (theme rule) |
| Functionality → *One Page Scrolling* | On | animated anchor links (Row IDs) |
| Functionality → **Max Website Container Width** | **1430** (the field's minimum is 1425) | v2 container: 1430 − 2 × 55 = **1320** content |
| Functionality → **Container Left/Right Padding** | **55** px (step 5) · Mobile: **Pixels 20** | v2 gutter |
| Functionality → *Lightbox Script* | fancyBox3 | Video Lightbox / Image Gallery |
| Functionality → **Page Builder Element Animations On Mobile Devices** | **Enable** | phones keep entrances, Animated Text and toggles motion |
| Functionality → **Column/Image Animation Easing** / **Timing** | **easeOutExpo** / **1300** | v2's „arrive“ feel; Transit maps it to `cubic-bezier(.19,1,.22,1)`, mask reveals to easings.net `(0.19,1,0.22,1)` |
| Functionality → *Disable Parallax Backgrounds On Mobile* | On | phones: static backgrounds (performance); Parallax Fade and sticky sections degrade to static stacks |
| Functionality → *Disable Video Backgrounds On Mobile Devices* | On | phones see the *Video Preview Image* only |
| Functionality → *Back To Top Button* | Off | the call bar replaces it |
| CSS/Script Related → *Custom CSS Code* / *Custom JS (Head)* | `sgp-custom.css` / `sgp-custom.js` | the only custom layer (§4) |
| Performance | *Load Google Fonts Locally* On · *Font Display Swap* On · *Lazy Load Page Builder Element Images* On · *Delay JavaScript Execution* Off at launch (test later) | — |

### 2.3 Typography (Theme Options → Typography)

*Fluid Typography* **Off** (root stays 16 px, so the 12 px label floor is exact) · *Custom Responsive Headings* **On** with the percentages below (small desktop / tablet / phone) · families from Google Fonts with `latin-ext` (ą č ę ė į š ų ū ž).

| Slot (admin label) | Family · weight | Size / line height | Letter spacing · transform | Responsive % → px at 390 |
|---|---|---|---|---|
| **Heading 1** | Barlow Condensed **600** | 80 / 76 px | −1 px | 90 / 72 / 52 % → 42 px |
| **Heading 2** | Barlow Condensed **500** | 64 / 64 px | −0.5 px | 90 / 78 / 56 % → 36 px |
| **Heading 3** | Barlow Condensed **600** | 36 / 38 px | 0 | 92 / 86 / 74 % → 27 px |
| **Heading 4** | Barlow Condensed **600** | 24 / 26 px | 0 | 100 / 100 / 92 % → 22 px |
| **Heading 5** | Barlow **500** | 20 / 30 px | 0 | 100 / 100 / 90 % → 18 px (leads, *Intro*) |
| **Heading 6** | Barlow **600** | 15 / 20 px | 0.2 px | 100 % (small heads, ticker text) |
| **Body Font** | Barlow **400** | 17 / 27.5 px | 0 | 100 / 100 / 94 % → 16 px |
| *Italic* / *Bold* | Barlow 400 italic / 600 | — | — | — |
| **Form and Category Labels** („Label“) | **IBM Plex Mono 500** | 12 / 16 px | **1 px · uppercase** | 100 % (never below 12 px) |
| **Navigation Font** / **Navigation Dropdown Font** | Barlow 500 | 15 px | 0.2 px | — |
| **Off Canvas Navigation** | Barlow Condensed 600 | 40 / 42 px (mobile custom size 34) | 0 | — |
| Off Canvas Navigation/Dropdown Description Text | Barlow 400 | 15 px | — | — |
| **Nectar Button** | Barlow 600 | 16 px | 0.2 px | — |

Where the Label slot shows up natively: **Badge** (*Inherit Typography From: Label*), all `form label`s (Fluent Forms field labels), Tabs links under the Material skin, and any element given the theme's own Extra Class `nectar-inherit-label` (used for the Yoast breadcrumb line). Nothing else uses mono. *Statement* size (48 px) and the home hero H1 size come from the element's *Font sizing* group, not from a new slot.

### 2.4 Header Navigation (Theme Options → Header Navigation) and the call button

| Field | Value |
|---|---|
| Logo & General Styling → *Logo* / *Starting Logo* (transparent state) | `logo_light.svg` for both (every page starts on dark) · *Logo Height* **30** · *Mobile Logo Height* **26** · **Header Padding 27** (→ 84 px bar) |
| *Header Box Shadow* | None |
| **Header BG Opacity** | **90** |
| **Header Blur Background** · *Type* · *Functionality* | On · Default · „Active when "Transparent header effect" is not“ |
| **Header Button Link Style** | **Button Shadow and Scale on Hover** |
| Layout & Content → **Header Layout** | **Default Layout** (logo left, menu right) · **Full Width Header Content** On |
| Transparent Header Effect → **Use Transparent Header When Applicable** | On · *Header Starting Text Color* `#FFFFFF` · *Header Starting Text Opacity* 1.0 · *Header Permanent Transparent* **Off** · *Header Inherit Row Color* **Off** |
| Animation Effects → **Header Link Hover/Active Effect** | **Animated Underline** (`.35s cubic-bezier(.52,.01,.16,1)`, underline in the hover colour) |
| **Header Hide Until Needed** | **Off** (so *Resize On Scroll* works and Sticky Sections can subtract the bar) |
| **Header Resize On Scroll** · *Header Logo Shrink Number (in px)* | **On** · **6** (84 → ≈ 70 px) |
| Dropdown / Megamenu | *Header Dropdown Animation* **Fade In Up** · *Header Dropdown Roundness* **3** · Dropdown shadow **Large** · dropdown hover *Animated Underline* · *Megamenu Removes Transparent Header* On · *Mega Menu Width* Contained |
| Mobile Header | *Layout* Default · *Header Sticky On Mobile* On · *Mobile breakpoint* **1000** |
| Color Scheme → **Custom** | *Header Background* `#0F1417` · *Header Font* `#F2F4F3` · *Header Font Hover* `#FFFFFF` · Dropdown BG `#0F1417`, font `#F2F4F3`, hover `#FFFFFF` · Off Canvas BG `#0B0E10`, font `#F2F4F3`, close button `#F2F4F3` |
| Header menu (Appearance → Menus) | Apie mus · **Paslaugos** (mega menu, G3) · **Grafikas** · Siuntos sekimas · Taisyklės · Kontaktai · **Skambinti** (G4). „Paslaugos“ / „Grafikas“ are shortened labels (client to confirm; H1s keep the full names) |
| „Skambinti“ menu item (Salient Core menu options) | *Menu Item Link Button Style* **Button Accent Color** · *Menu Item Text Coloring* Custom, *Title Color* `#0F1417`, *Hover* `#0F1417` · *Icon* `fa-phone` · **Persist In Mobile Navigation Header** ✓ · URL `/kontaktai/#skambinkite` · **Enable Mega Menu** · *Mega Menu Width* **x2 Regular Dropdown** · *Mega Menu Alignment* **Right** · *Mega Menu Global Section* **GS-Telefonai** (Mega Menu GS *Mobile* is not used: 18.2.1 marks it incompatible with fullscreen off-canvas styles — phones get GS-Telefonai in the off-canvas meta area and the call bar) |

### 2.5 Off Canvas, Footer, Page Transitions, Forms, Global Sections

| Field | Value |
|---|---|
| Off Canvas Menu → *Off Canvas Menu* (desktop button) | **Off** (the full menu fits from 1000 px; below 1000 the off-canvas is the mobile menu) |
| **Off Canvas Menu Style** | **Fullscreen Cover Split** (`fullscreen-split`): left = menu (BC 600 40 px, items rise .85 s with 20 ms stagger), right = *Off Canvas Menu Meta Area* Global Section **GS-Telefonai** (rises from 35 px, .85 s, delay .3 s) |
| *Off Canvas Icon Button* · icon style | **Circular**, BG `#161D21`, icon `#F2F4F3` · *Icon Style* **Even Lines** |
| *Off Canvas Menu Overlay Strength* | Solid |
| Footer → *Main Footer Area* / *Copyright* | Off / Off → **GS-Poraštė** at *Location: Footer* · *Footer Reveal Effect* Off |
| Page Transitions → **Transition Method** | **View Transitions API (Modern)** |
| → **Transition Effect** | **Vertical Reveal** (`vertical-reveal`, 1.3 s `cubic-bezier(.55,0,.1,1)`); 18.2.1 has no mobile switch for this method, the reduced-motion layer turns it off |
| Form Styling | *Overall Form Style* **Minimal** · *Fancy Select* On · *Fancy Checkbox* On · *Submit Button* Nectar Button · *Input font size* **17** · border width 1 · input BG transparent · border `#C3CBCB`, border hover `#EF4539` (dark rows adjusted in `sgp-custom.css` C-6) |
| Global Sections (post type) | 14 sections: G1 GS-Išvykimai · G3 GS-Paslaugų meniu · G5 GS-Telefonai · G7 GS-Poraštė · G8 GS-Skambučių juosta · G11 GS-Grafikas Airija + GS-Grafikas Ispanija · G12 GS-Maršrutai · G18 GS-Paslaugos · G24 GS-Kvietimas · G25 GS-Užklausa · G32 GS-Artimiausi · A9 GS-Pasitikėjimas · E1 404 Content |

### 2.6 Motion values the emulation must reproduce (P§3, with SGP's Theme Options)

| What | Value |
|---|---|
| Column / Image entrances | transform **1300 ms `cubic-bezier(.19,1,.22,1)`** (easeOutExpo) · opacity **500 ms** · trigger when the element top crosses **88 %** of the viewport (*Reveal From X* 70 %, Image *Reveal Rotate* 75 %, Image *Slide Up* 99 %) · *Fade In From Bottom* 100 px · *Slight Fade In From Bottom* 50 px · *Grow In* scale .75 · *Fade In From Left/Right* ∓45 px |
| Inner Column **Mask Reveal** / Column BG *Mask Reveal* | `clip-path` **1.3 s `cubic-bezier(0.19,1,0.22,1)`** · Straight Bottom = `inset(100% 0 0 0)` → `inset(0)` · Circle = `circle(0%)` → `circle(150%)` |
| Image / Column BG **Reveal Rotate From X** | wrapper ±250 px + inner ±25° → 0 · **2.3 s `cubic-bezier(.2,.65,.3,1)`** |
| **Animated Text** | words 1.2 s `(.25,1,.5,1)`, stagger 15–50 ms · letters 20–35 ms · *Reveal* from 1.3em · *Blur* 10 px + .25em · *Scroll Position: Opacity* words .2 → 1 with scroll |
| **Highlighted Text** | `background-size` 0 → 100 % **.9 s `(.15,.75,.4,1)`** · Regular Underline 3 px |
| **Milestone** | *Count To Value* 2.2 s easeOutCubic · *Motion Blur Slide In* digits stagger 200 ms, .65 s `(0,0,.17,1)` · trigger 98 % |
| Row **Background Layer Animation** | *Fade In* .85 s · *Zoom Out* scale 1.25 → 1, 2.5 s `(.1,.55,.4,1)` · **Zoom Out Slowly** 1.35 → 1, **8 s `(.1,.2,.7,1)`** · **Slight Zoom Out Reveal** wrapper .92 / inner 1.15 → 1, **1.3 s `(.12,.75,.4,1)`** · **Clip Path Inset** once: first row 1.3 s `(.25,.1,.18,1)`, others 2 s `(.6,.06,.18,1)`; *Scroll Position*: interpolated over the *Viewport Trigger Offset* range |
| **Parallax** speeds | Subtle `fast` **0.20** · Regular `medium_fast` **0.28** · Medium `medium` **0.40** · High `slow` **0.60** · column BG Very Subtle 0.12 / Minimum 0.09 · Section *Parallax Fade*: background moves at the speed factor and fades towards the scrim as the hero leaves |
| **Color Change Section** | page BG/text colours switch to the section's when ≥ 40 % of it is visible · **0.8 s** |
| Buttons | colours **.45 s `(.25,1,.33,1)`** · *Arrow Circle Animation* **.55 s `(.12,.75,.4,1)`**, circle `max(1.4em,36px)`, `clip-path circle(50%) → circle(45%)`, arrow exits ↗ and a twin enters · *Text Reveal Wave* letters `translateY(115%)` → 0, **.5 s `(.46,.4,.56,.87)`**, 15 ms per letter · *Underline* `scaleX` .4 s `(.23,.46,.4,1)` · Legacy Button lift `translateY(-3px)` + `0 20px 38px rgba(0,0,0,.16)` · header button scale + shadow |
| Fancy Box | *Image Above Text* image scale 1.1, **.75 s `(.2,.75,.5,1)`** + title underline · *Description on Hover* card −10 px + `0 25px 55px rgba(0,0,0,.22)` **.65 s `(.05,.2,.1,1)`**, text from 20 px (delay .15 s), *Short Zoom* 1.13 .8 s |
| Image hover | *Zoom In* 1.13 · *Zoom In Crop* inner 1.15 / frame .95 · **.65 s `(.05,.2,.1,1)`** |
| Horizontal List Item | fill flips up `rotateX(90deg) → 0`, origin bottom, **.4 s `(.2,0,.15,1)`** · row padding 22 px · *Border Animation* draws the bottom line |
| Toggle Panels | *Animated Circle*: stroke draws + panel opens **.85 s `(.76,0,.24,1)`**, circle 40 px · *Minimal Shadow*: open panel gets the 5-layer soft shadow |
| Tabs | *Minimal* 4 px underline slides **.3 s `(.12,.75,.4,1)`** · *Toggle Button* 70 × 28 switch, knob **.45 s `(.23,.46,.4,1)`** · *Vertical Sticky Scrolling* active link by scroll — *Tab Links*: links .45 → 1 (.25 s), 3 px indicator .5 s `(0,0,.34,.96)`; *Tab Content*: content *Fade* |
| Sticky Content Sections | pinned *Scale* / *Blurred Scale*: previous card 1 → .92, blur 0 → 5 px, −54 px when *Stacked* · *Horizontal Scrolling* track moves with vertical scroll while pinned |
| Scrolling Text | loop Slowest 45 s · Slower 30 s · Slow 14 s · Medium 7 s · Fast 4 s · *Mask Edges* · *Move on Scroll* adds scroll offset |
| Header / off-canvas | underline .35 s `(.52,.01,.16,1)` · resize on scroll · Fullscreen Cover Split .85 s `(.2,.75,.5,1)` |
| **View Transitions → Vertical Reveal** | new page `clip-path: inset(90% 0 0 0)` + `translateY(10%)` → none, old page `translateY(-10%)` + opacity .3 · **1.3 s `(.55,0,.1,1)`** |
| Content Trail | frequency 85 px, life 1.2 s, *Scale* in / out, random rotation |
| Lenis | 1.1.13, `lerp` 0.153 |

### 2.7 `assets/css/theme-options.css` (demo stand-in for §2.1–2.6)

The shared team writes this file first; every emulation file and page reads only these variables. Names prefixed `--nectar-*` are the ones Salient itself exposes (palette, page colours used by Color Change Section, button radius, its two cubic-bezier tokens), so markup written against them keeps its meaning in WordPress.

```css
:root{
  /* Accent Colors (Theme Options → General Settings) */
  --nectar-accent-color:#EF4539;  --nectar-extra-color-1:#0F1417;
  --nectar-extra-color-2:#F5F7F6; --nectar-extra-color-3:#C4301E;
  /* Styling → Primary Background / Text (Color Change Section rewrites the --nectar-page-* pair) */
  --nectar-bg-color:#F5F7F6; --nectar-font-color:#1C1D1D; --nectar-font-color-light:#F2F4F3;
  --nectar-page-background-color:var(--nectar-bg-color); --nectar-page-text-color:var(--nectar-font-color);
  /* extended v2 palette (custom colours inside element options) */
  --sgp-asphalt-950:#0B0E10; --sgp-asphalt-900:#0F1417; --sgp-asphalt-800:#161D21; --sgp-asphalt-750:#1A2227; --sgp-asphalt-700:#222B30;
  --sgp-paper-50:#F5F7F6; --sgp-paper-100:#EAEEED; --sgp-paper-200:#D9DFDE; --sgp-paper-300:#C3CBCB; --sgp-white:#FFFFFF;
  --sgp-ink:#1C1D1D; --sgp-ink-2:#4A5358; --sgp-snow:#F2F4F3; --sgp-fog:#9AA6AB;
  --sgp-red:#EF4539; --sgp-red-ink:#C4301E; --sgp-red-lit:#F4604F;
  --sgp-hair-l:rgba(28,29,29,.12); --sgp-hair-l-2:rgba(28,29,29,.26);
  --sgp-hair-d:rgba(242,244,243,.12); --sgp-hair-d-2:rgba(242,244,243,.26);
  --sgp-glass:rgba(11,14,16,.55); --sgp-scrim:rgba(11,14,16,.72);
  /* Typography (Theme Options → Typography; Fluid Typography off) */
  --f-display:"Barlow Condensed","Arial Narrow",sans-serif;
  --f-text:"Barlow",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --f-label:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  --h1-size:80px; --h1-lh:76px; --h1-w:600; --h1-ls:-1px;
  --h2-size:64px; --h2-lh:64px; --h2-w:500; --h2-ls:-.5px;
  --h3-size:36px; --h3-lh:38px; --h3-w:600;
  --h4-size:24px; --h4-lh:26px; --h4-w:600;
  --h5-size:20px; --h5-lh:30px; --h5-w:500;
  --h6-size:15px; --h6-lh:20px; --h6-w:600; --h6-ls:.2px;
  --body-size:17px; --body-lh:27.5px;
  --label-size:12px; --label-lh:16px; --label-ls:1px;              /* uppercase, Plex Mono 500 */
  --nav-size:15px; --nav-w:500; --btn-size:16px; --btn-w:600; --btn-ls:.2px;
  --oc-nav-size:40px;                                                /* phones 34px */
  /* General Settings → Functionality / Styling */
  --container:1320px; --container-pad:55px;                          /* Max Website Container Width 1430 · padding 55 (step 5) → 1320 content · phones: 20px */
  --column-spacing:30px;
  --nectar-border-radius:3px;                                        /* Button Styling: Slightly Rounded W/ Shadow, Roundness 3 */
  --r-col:3px; --r-img:0px; --r-badge:3px; --r-toggle:3px; --r-dropdown:3px; --r-sticky:3px;
  --btn-lift:translateY(-3px); --btn-lift-shadow:0 20px 38px rgba(0,0,0,.16);
  --underline-thickness:1px;
  /* Header Navigation */
  --header-h:84px; --header-h-small:70px; --header-pad:27px; --logo-h:30px; --logo-h-m:26px;
  --header-bg:rgba(15,20,23,.9); --header-font:#F2F4F3; --header-font-hover:#FFFFFF; --header-start:#FFFFFF;
  --dropdown-bg:#0F1417; --offcanvas-bg:#0B0E10;
  /* Motion (§2.6) */
  --nectar-cubic-bezier-out:cubic-bezier(.3,1,.3,1); --nectar-cubic-bezier-in-out:cubic-bezier(.76,0,.24,1);
  --nectar-header-hover-timing:.65s; --page-color-change-section-transition-time:.8s;
  --e-entrance:cubic-bezier(.19,1,.22,1);  --d-entrance:1300ms; --d-entrance-opacity:500ms;
  --e-mask:cubic-bezier(.19,1,.22,1);      --d-mask:1.3s;
  --e-rotate:cubic-bezier(.2,.65,.3,1);    --d-rotate:2.3s;
  --e-text:cubic-bezier(.25,1,.5,1);       --d-text:1.2s;
  --e-btn:cubic-bezier(.25,1,.33,1);       --d-btn:.45s;
  --e-arrow:cubic-bezier(.12,.75,.4,1);    --d-arrow:.55s;
  --e-wave:cubic-bezier(.46,.4,.56,.87);   --d-wave:.5s; --st-wave:15ms;
  --e-underline:cubic-bezier(.23,.46,.4,1); --d-underline:.4s;
  --e-nav:cubic-bezier(.52,.01,.16,1);     --d-nav:.35s;
  --e-hover:cubic-bezier(.05,.2,.1,1);     --d-hover:.65s;           /* image zoom, Description on Hover */
  --e-card:cubic-bezier(.2,.75,.5,1);      --d-card:.75s;            /* Image Above Text; off-canvas .85s */
  --e-hli:cubic-bezier(.2,0,.15,1);        --d-hli:.4s;
  --e-highlight:cubic-bezier(.15,.75,.4,1); --d-highlight:.9s;
  --e-toggle:var(--nectar-cubic-bezier-in-out); --d-toggle:.85s;
  --e-tab:cubic-bezier(.12,.75,.4,1);      --d-tab:.3s;
  --e-zoom-slow:cubic-bezier(.1,.2,.7,1);  --d-zoom-slow:8s;
  --e-zoom-reveal:cubic-bezier(.12,.75,.4,1); --d-zoom-reveal:1.3s;
  --e-clip-first:cubic-bezier(.25,.1,.18,1); --e-clip:cubic-bezier(.6,.06,.18,1);
  --e-vt:cubic-bezier(.55,0,.1,1);         --d-vt:1.3s;
  --parallax-subtle:.2; --parallax-regular:.28; --parallax-medium:.4; --parallax-high:.6;
  --parallax-very-subtle:.12; --parallax-minimum:.09;
  --d-milestone:2.2s; --lenis-lerp:.153;
  --loop-slowest:45s; --loop-slower:30s; --loop-slow:14s; --loop-medium:7s; --loop-fast:4s;
}
@media (max-width:999px){:root{--container-pad:20px;--h1-size:57.6px;--h1-lh:55px;--h2-size:49.9px;--h2-lh:50px;--h3-size:31px;--h3-lh:33px}}
@media (max-width:690px){:root{--h1-size:41.6px;--h1-lh:40px;--h2-size:35.8px;--h2-lh:36px;--h3-size:26.6px;--h3-lh:29px;
  --h4-size:22px;--h5-size:18px;--h5-lh:27px;--body-size:16px;--body-lh:26px;--oc-nav-size:34px;--logo-h:26px}}
```
(Small-desktop percentages 90/90/92 % apply at 1000–1299 px; the kit adds that media query too.)

### 2.8 Notes that bind every team
- **Breakpoints = Salient's:** desktop ≥ 1000, tablet 691–999, phone ≤ 690; header mobile breakpoint 1000. Verify at 1440×900, 1024×768 and 390×844.
- **Row padding in %** follows WPBakery/Salient semantics (percent of the row **width**): chapters use **8 % top / 8 % bottom** on desktop (≈ 115 px at 1440, close to v2's 160 px cap), **80 px / 80 px** on phones (Row padding per device).
- **Every page starts dark** (hero Section or the inner head §3.3) — the transparent header needs it; *Disable Transparency* is never used.
- **Fonts:** `https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600&family=Barlow:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap` (Plex Mono 400 is no longer needed). Production: *Load Google Fonts Locally*.
- **Red budget:** ≤ ~5 % of any viewport; no red Row/Column backgrounds (the only red fills are buttons, the header button, hotspot markers, the „4 šalys“ badge and Highlighted Text bars).
- **Radii:** 3 px (buttons, columns, cards, toggles, dropdown, sticky sections, glass band, badges), 0 (images, rows). Nothing rounder.
- **Old tokens** (`--c-asphalt-*`, `--c-paper-*`, `--f-mono`, `--rail-*`, `--c-graticule`, `--sp-*`, `--st-*`, `--section-y`) disappear with `tokens.css` in Wave 3; pages switch to the new kit per page (front matter `kit: salient`, §5.1) so old and new CSS never mix on one page.

---

## 3. Page-by-page, section-by-section mapping

**How to read the tables.** *Now* = the v2 block (audit verdict in brackets: N = NATIVE, N+C = NATIVE+CSS, C = CUSTOM, W = WRONG-MAPPING). *New* = the exact 18.2.1 element and options (`Element → Option: value`), in the order an editor sets them. *Tone* = **A** asphalt (dark chapter) / **P** paper (light chapter) / **Ph** photo or video with scrim. *Media* = `media.json` ids. *CSS* = the `sgp-custom.css` group from §4 it needs (— = none). *Verdict* = predicted audit verdict after the change: **NATIVE**, **NATIVE+CSS**, **CUSTOM** or **DROPPED**. Copy is verbatim from DS§6 unless marked NEW. Every block's `data-salient` is rewritten to the *New* column (format §5.0).
Element decisions from revision 1 stand unless a row says otherwise; what changed is the **look** (v2 palette/type/radii instead of Harbor white/pills) and a few elements that fit the v2 identity better (Icon List stations, photo columns, Legacy Button lift, Minimal Line labels, Color Change Section).

**Recurring building blocks** (defined once, referenced by name below)

| Name | Salient build |
|---|---|
| **Label** „02 · Paslaugos“ | **Badge** → *Badge Style* **Minimal Line** · *Line Width* 28px · *Inherit Typography From* **Label** (Plex Mono 500 12 px, uppercase via the slot) · *Badge Text Color* `#C4301E` on P, `#EF4539` on A (asphalt-900/950 only), `#F2F4F3` on Ph. Home chapters carry the stop number („02 · Paslaugos“); inner pages the plain name |
| **Statement** | **Animated Text** → *Text Element* **H2** · *Text Effect* Word Animations: **Reveal** · Stagger ✓ · Font sizing: custom **48px** (tablet 40, phone 30) · line height 1.05 · Max Width 20em |
| **Intro** | **Responsive Text** → *Font Style* inherit **H5** (Barlow 500 20/30) · Max Width 56ch · colour ink-2 `#4A5358` on P, fog `#9AA6AB` on A |
| **Road line** | **Divider** → *Line Type* **Small Line** · *Custom Line Width* 96px · *Line Thickness* 2px · colour **Accent Color** · **Animate Line** ✓ (draws left → right) · height 28px — the route mark under chapter titles (max one per chapter) |
| **Call (red)** | **Button** (`nectar_cta`) → *Type* **Arrow Circle Animation** · *Button Roundness* 3 · *Background Color* **Accent Color** · *Background Color Hover* custom `#F4604F` · *Text Color* `#0F1417` · *Min Icon Size* 36 · *Icon Gap* 20 · `tel:` link + *Aria Label Text* „Skambinti į … +370 …“ |
| **Button (ink / paper)** | same *Arrow Circle Animation*, *Background Color* **Extra Color 1** + text `#F2F4F3` (on P), or **Extra Color 2** + text `#0F1417` (on A); hover `#222B30` / `#FFFFFF` |
| **Button (glass)** | **Button** → *Type* **See Through** · Preset **md** · *Button Roundness* 3 · *Border Color* `rgba(242,244,243,.6)` → hover `#F2F4F3` · *Text Color* `#F2F4F3` → hover `#0F1417` · **Backdrop Filter → Blur 12** (secondary actions on photos) |
| **Lift button** | **Legacy Button** → *Style* **Regular** · *Size* Large · Color **Extra Color 1** (white text, 17:1) · *Icon* Default Arrow — gets the native −3 px lift + shadow from *Button Styling: Slightly Rounded W/ Shadow*. Paper chapters only (never Accent: white on red is 3.8:1). Used where a solid secondary CTA sits in text („Visos taisyklės“, PDF) |
| **Link** | **Button** → *Type* **Underline** · *Underline Visibility* Default (Visible) · Display inline |
| **Link list** | **Button** → *Type* **Text Reveal Wave** · Display block (mega menu, footer, card service lists) |
| **Chip** | **Badge** → *Badge Style* Default · *Inherit Typography From* Label · BG custom transparent + **Border** 1px (`rgba(28,29,29,.26)` on P / `rgba(242,244,243,.26)` on A) · *Padding Amount* Small · *Border Radius* 3px · Display Inline. On photos: BG `rgba(11,14,16,.4)` + **Backdrop Filter → Blur 12** |
| **Callout** | Inner Column → *Background Color* `#EAEEED` (P) / `#161D21` (A) · *Border Radius* 3px · *Border Type* Advanced: left 2px **Accent** · *Padding* Advanced 32px |
| **KV rows** | **Horizontal List Item** ×n → *Columns* 2 · *Column Layout* **30% \| 70%** · *Style* **Bottom Border, No Hover Effect** · **Border Animation** ✓ · column 1 text element H6 (key), column 2 p |
| **Stations** | **Icon List** → *Direction* **Horizontal** · 3 columns (4 for packing rules) · *Icon Size* Medium · *Icon Style* **Icon Colored W/ BG** · *Icon Color* **Accent Color** · **Animate Element** ✓ · items *Number* 1/2/3 + header (H4) + text — with a full-width **Divider** (*Line Type* Full Width, 1px, *Animate Line* ✓) above it as the road. Phones: vertical |
| **Link rows** | **Horizontal List Item** ×n → *Columns* 2 · **20% \| 80%** · *Style* **Bottom Border, Color Hover Effect** · *Hover Color* **Extra Color 1** on P / **Extra Color 2** on A · *Full Item Link URL* · CTA 1 text „→“ |
| **Card** | Column/Inner Column → *Background Color* `#FFFFFF` (P) / `#161D21` (A) · **Background Color Hover** `#EAEEED` / `#1A2227` · *Border Radius* 3px · *Border* Simple 1px hairline · *Padding* 40px · optional **Column Link** |
| **Photo card** | Column → *Background Image* (media id) + *Scale Background Image To Column* ✓ + **Color Overlay** Advanced `#0B0E10` · *Opacity* **.72** → *Opacity Hover* **.42** · *Background Image Parallax Scrolling* Very Subtle · *Border Radius* 3px · **Column Link** · *Text Color* Light — the photo brightens under the text on hover (native) |
| **Entrance** | Column/Inner Column → *Animation* **Fade In From Bottom** (big blocks) or **Slight Fade In From Bottom** (text) · *Delay* 0 / 120 / 240 / 360 ms for siblings (theme timing easeOutExpo 1300 ms) |
| **Chapter row** | Row → *Type* Full Width Background · BG colour `#0F1417` (A) or `#F5F7F6` / `#EAEEED` (P) · *Text Color* Light / Dark · padding 8 % / 8 % (phones 80 px) · **Color Change Section** ✓ (home and service template chapters) · **Row ID** = the v2 anchor · *Extra Class* `sgp-dark` on A rows (scopes C-6 / C-11 only) |

### 3.1 Shared (header, menus, footer, Global Sections, site-wide components)

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| G1 | GS-Ticker, dark strip, desktop only, `[sgp_grafikas ticker]` (C) | **Global Section „GS-Išvykimai“ → Location: In Navigation Top Before Scrolling** (all pages, phones too). Row Full Width Content, padding 0 · Column BG `#0B0E10`, Border Advanced bottom 1px `rgba(242,244,243,.12)`, padding 9px 0, **Column Link** `/pervezimu-grafikas/` · **Scrolling Text** → *Scrolling Direction* Standard · *Scrolling Speed* **Slower** (`slowest`, 30 s) · *Number of Text Repeats* 3 · *Text Repeat Divider* **Custom Symbol „✦“** · *Divider Size* ½ · *Divider Color* `#EF4539` · *Text Space Amount* Custom 1.6em · **Mask Edges** ✓ · *Custom Font Size* 15px (mobile 14px) · text in an **H6** (Barlow 600), colour `#F2F4F3` | 4 routes, next date each, typed monthly: „Lietuva → Airija: spalio 9 d. ✦ Lietuva → Ispanija: spalio 9 d. ✦ Airija → Lietuva: rugsėjo 28 d. ✦ Ispanija → Lietuva: rugsėjo 27 d. ✦ Visas grafikas →“ | A | 30 s loop; hides once the page scrolls (location „Before Scrolling“); pauses with the motion toggle (C-13) | C-12 | NATIVE |
| G2 | Header #sgp-hdr (N) | Theme Options → Header Navigation per §2.4 · logo `logo_light.svg` 30 px (mobile 26) · menu Apie mus · Paslaugos · Grafikas · Siuntos sekimas · Taisyklės · Kontaktai · [Skambinti] | menu labels (2 shortened) | A (transparent → `#0F1417` 90 % + blur) | underline .35 s; bar shrinks 84 → ≈ 70 px on scroll | — | NATIVE |
| G3 | Mega menu „Pervežimo paslaugos“ (N+C) | Menu item „Paslaugos“ → **Enable Mega Menu** · *Mega Menu Width* 100% Header Width · **Mega Menu Global Section „GS-Paslaugų meniu“**: Row BG `#0F1417`, 3 Columns × 2 groups: **Label** (group name) + **Link list** (services, Text Reveal Wave) · 4th Column **Photo card** 38927007 „Visos paslaugos →“ (Column Link `/pervezimo-paslaugos/`) · *Header Dropdown Animation* Fade In Up · Roundness 3 · shadow Large | 6 groups → 11 services (`paslaugos.json`) | A · 38927007 | fade-in-up; wave on links; photo card brightens | — | NATIVE |
| G4 | Header „Skambinti“ (N) | per §2.4 (*Button Accent Color*, text `#0F1417`, `fa-phone`, **Persist In Mobile Navigation Header**, Mega Menu x2 Regular Dropdown / Right / **GS-Telefonai**, URL `/kontaktai/#skambinkite`) · *Header Button Link Style* **Button Shadow and Scale on Hover** | „Skambinti“ | red button on A | scale + shadow on hover | C-10 | NATIVE+CSS |
| G5 | Switchboard popover #sgp-call (C) | **Global Section „GS-Telefonai“** (Mega Menu GS of „Skambinti“ + **Location: Off Canvas Menu Meta Area**): Row BG `#0F1417`, Inner Row 2 × ½: **Label** „Į Airiją“ + **Link list** item at H3 size „+370 650 53161“ (`tel:`) + **Link** „Airijoje +353 86 450 3104“ + **Link** „JK +44 7566 878681“ · **Label** „Į Ispaniją“ + „+370 638 28919“ + **Link** „Ispanijoje +34 602 547 929“ · Divider · **Link** „saugiai.greitai.patikimai@gmail.com“ (`mailto:`) | all 5 numbers + e-mail, grouped by direction | A | fade-in-up; letters wave on the numbers | — | NATIVE |
| G6 | Off-canvas #sgp-menu (N+C) | per §2.5: **Fullscreen Cover Split** · Circular icon button · Even Lines · meta area = GS-Telefonai · menu items BC 600 34–40 px | menu + phones | A `#0B0E10` | items rise .85 s, 20 ms stagger; right side +.3 s | — | NATIVE |
| G7 | Footer GS, 5 dark columns, ring bullets (N+C) | **Global Section „GS-Poraštė“ → Location: Footer**. Row BG `#0B0E10`, Text Light, padding 72px 56px 32px: Row 1 = 4 Columns: ¼ logo (Image) + Responsive Text „Saugiai, greitai, patikimai.“ · ¼ **Label** „Puslapiai“ + **Link list** (Apie mus, Paslaugos, Grafikas, Siuntos sekimas, Taisyklės, Kontaktai) · ¼ **Label** „Paslaugos“ + **Link list** (6 most visited services) · ¼ **Label** „Į Airiją“ / „Į Ispaniją“ + phones as **Link list** + e-mail **Link**. Row 2: **Divider** Full Width, 1px, `rgba(242,244,243,.12)`, **Animate Line** ✓. Row 3: Responsive Text „© `[nectar_current_year]` SGP pervežimai“ + **Link** „Privatumo politika“ (flex, space-between). No wordmark, no gradient | links, numbers, © year | A | wave on links; hairline draws | — | NATIVE |
| G8 | GS-CallBar (N+C) | **Global Section „GS-Skambučių juosta“** placed as the last element of every page's content · Row → Sticky Row ✗ (cannot pin inside a Global Section) · **Device Visibility** Desktop hidden · *Extra Class* `sgp-callbar` pinned by C-4 · Inner Row → **Backdrop Filter → Blur 16** + BG `rgba(11,14,16,.86)` · 2 Columns: **Call (red)** „Į Airiją“ / „Į Ispaniją“ (LT lines, *Alignment* Stretch) | both LT lines, equal weight | A glass | arrow circle on tap/hover | C-4 | NATIVE+CSS |
| G9 | Cookie consent (N+C) | Complianz banner: bottom-left card `#161D21`, radius 3, Label-typography title, accept = red with `#0F1417` text, deny = See-Through style | verbatim banner texts | A | plugin | C-9 | NATIVE+CSS |
| G10 | GS-Board split-flap (C) + `[sgp_grafikas]` family (C) + next-strip (C) | **Dropped as a component.** Dates live in GS-Išvykimai (G1), **GS-Artimiausi** (G32) and **GS-Grafikas Airija / Ispanija** (G11) | all dates, notes, phones | — | — | — | DROPPED |
| G11 | Timetables `.sgp-tt` (C) | **GS-Grafikas Airija / GS-Grafikas Ispanija**: **Label** „Iš Lietuvos“ / „Į Lietuvą“ + **Horizontal List Item** ×2 each → *Columns* 3 · **25% \| 50% \| 25%** („Lietuva → Airija \| spalio 9 d., spalio 23 d. \| +370 650 53161“) · *Style* **Bottom Border, Color Hover Effect** · *Hover Color* Extra Color 1 (P) / **White** (A variant — native hover text is #fff on every colour except White, which gets #000) · **Border Color** `#C3CBCB` (P) / `#3E464A` (A) — Border Animation only draws with a Border Color · **Full Item Link URL** `tel:` · **Border Animation** ✓ · + Responsive Text „Tikslų išvykimo laiką ir paėmimo vietą suderinsime telefonu.“ + **Label** „Atnaujinta rugsėjo 23 d.“ | all 4 routes, full dates, phone per direction (out = LT line, in = destination line) | P or A | fill flips up .4 s; lines draw | C-5 | NATIVE+CSS |
| G12 | (new, replaces GS-Board on inner pages) | **Global Section „GS-Maršrutai“** (Harbor pricing form, v2 look): Row Full Width Content, padding 0 56px, Equal Height · 2 Columns (+ optional 3rd „Pakeliui“) with **Border Type Advanced** 1px hairline (left/top/bottom; last also right), padding 40px: **Label** „Maršrutas 01“ + H3 „Lietuva – Airija – Lietuva“ + **Road line** + **Intro** + **Price Typography** amount „3–4“, after text „paros kelyje“ (H2) + **Fancy Unordered List** (*Icon* Standard Dash, colour Accent, Enable Animation ✓): Keleiviai · Siuntos · Automobiliai · Gyvūnai + **Call (red)** stretch „Skambinti +370 650 53161“ + **Link** „Airijoje: +353 86 450 3104“ + **Link** „Visas grafikas →“. 3rd column: H3 „Pakeliui“ + verbatim paragraph + **Badge** „4 šalys“ (BG Accent, text `#0F1417`, *Border Radius* 3px) | route names, services carried, phones, delivery time (no dates → nothing to update) | P or A (inherits the row) | Entrance 0/120/240; road lines draw; arrow circles | — | NATIVE |
| G13 | Rail + waypoints (C), graticule (N), crop marks (N+C), split-flap tiles (C), hover videos (C), odometer (C) | **Dropped.** Chapters are marked by **Label** + **Road line** | — | — | — | — | DROPPED |
| G14 | Key/value `.sgp-kv` (N+C) | **KV rows** | every key/value | P/A | bottom lines draw | — | NATIVE |
| G15 | Chips `.sgp-chips` (N+C) | **Chip** (Badge) | chip labels | P/A/Ph | none | — | NATIVE |
| G16 | Callouts `.sgp-callout` (N+C) | **Callout** | callout texts | P/A | Entrance | — | NATIVE |
| G17 | ✕ lists `.sgp-xlist` (N) | **Fancy Unordered List** → *Icon* Font Icon `fa-times` · colour **Accent** · Spacing 10px · **Enable Animation** ✓ | verbatim items | P/A | items fade in, 1 by 1 | — | NATIVE |
| G18 | GS-ServiceList (N+C) | **Global Section „GS-Paslaugos“**: **Link rows** ×11 („01 \| Krovinių pervežimas“) | 11 services | P or A | fill flips up .4 s `(.2,0,.15,1)` | — | NATIVE |
| G19 | Link cards `.sgp-card` 16:11 (N+C) | **Fancy Box** → *Style* **Image Above Text** · *Image Aspect Ratio* **3:2** · *Border Radius* None · Link URL · H4 + 1 line (P) — or *Style* **Description on Hover** (A: *Hover Color* Extra Color 1, *Overlay Opacity* .55 → *Hover Overlay Opacity* .8, *Background Hover Animation* **Short Zoom**, radius None, min height 420) | titles, summaries | per card | image scale 1.1 + underline / card lifts −10 px + text rises | — | NATIVE |
| G20 | Buttons `.sgp-btn`, `.sgp-callbtn` (N+C) | **Call (red)**, **Button (ink / paper)**, **Button (glass)**, **Lift button**, **Link**, **Link list** | labels | — | .45–.55 s, lift −3 px | — | NATIVE |
| G21 | Typography & colour tokens (N) | Theme Options §2 (demo: `theme-options.css`) | — | — | — | — | NATIVE |
| G22 | Breadcrumbs (N+C) | **Text Block** `[wpseo_breadcrumb]` (Yoast SEO → Breadcrumbs on) with the theme's Extra Class **`nectar-inherit-label`** (Label typography) in every inner head (§3.3) | breadcrumb trail | A | — | — | NATIVE |
| G23 | GS-Arrival „Atvykimas“ (N+C) + call tickets (C) | Split into **GS-Kvietimas** (G24) and **GS-Užklausa** (G25); tickets dropped | H2, both calls, form | — | — | — | DROPPED |
| G24 | (Harbor CTA, v2 „Atvykimas“ mood) | **Global Section „GS-Kvietimas“ → Location: After Page/Post Content** (display conditions: all pages except Kontaktai, Privatumo politika and services — they end with GS-Užklausa). Row Full Width Background · BG image **5919143** (tail-light bokeh) · **Parallax Background Media On Scroll** Speed **Medium** · *Background Layer Animation* **Zoom Out Slowly** · Color Overlay `#0B0E10` Heavy (0.8) · Text Light · padding 12 % · Column centred, **Column Link** `/kontaktai/`: **Label** „Atvykimas“ + **Animated Text** H2 *Word Animations: Blur* „Norite užsakyti? Paskambinkite arba parašykite.“ (NEW) + 2 × **Call (red)** (both LT lines) + **Link** „Parašykite mums →“ · **Content Trail** → *Type* Text · texts „Airija · Ispanija · Siunta · Keleivis · Automobilis · Gyvūnas · Perkraustymas“ · colours `#EF4539`/text `#0F1417`, `#F5F7F6`/`#0F1417`, `#161D21`/`#F2F4F3` · *Animation In* Scale · *Out* Scale · radius 3 · **Frequency 85** · **Duration 1.2 s** · random rotation ✓ · Position Absolute (full size) | CTA sentence NEW | Ph · 5919143 | bg zooms out over 8 s + parallax 0.40; tags trail the cursor | — | NATIVE |
| G25 | Enquiry form (N+C) | **Global Section „GS-Užklausa“**: Row BG `#0F1417`, Text Light, Equal Height · Column 2/5 **Callout** (A): **Label** „Užklausa“ + **Intro** „Kaip galime padėti?“ + **Fluent Forms** „SGP užklausa“ (Vardas, Telefonas, El. paštas, „Kas Jus domina?“ select of 11 + „Kita“ with default `{get.domina}`, Žinutė, sutikimas) + submit (Nectar Button → lifts) · Column 3/5: Inner Column **Mask Reveal** (Direction Right, Straight) with **Image** (Fit to Container, height 100 %) + **KV rows** (both directions' numbers) | form labels/texts DS§4.14 | A · 36377055 or per service `why_media[0]` | image wipes in 1.3 s; submit lift | C-6 | NATIVE+CSS |
| G26 | Motion system (N) | Theme Options §2.2 + element options only | — | — | as §2.6 | — | NATIVE |
| G27 | Reduced motion + motion pause (none / C) | **Custom layer** (18.2.1 never reads `prefers-reduced-motion`): CSS end states for entrances, Animated Text, Mask/Clip reveals, parallax, Scrolling Text, Content Trail, Milestones, View Transitions; JS stops Lenis before init and wires the **pause Button** (Button → Basic, Extra Class `sgp-motion-toggle`, „Sustabdyti judesį“) that pauses BG videos and Scrolling Text (WCAG 2.2.2) | — | — | — | C-2, C-13, C-14 + JS | CUSTOM |
| G28 | BG videos + pause + SD/HD (C) | Section/Row **Video Background** (MP4; poster = Row *Video Preview Image* / Section *Background Image*; desktop only via Theme Options) on H1, H5, T1 · on-demand clips: **Video Lightbox** → *Link Style* **Play Button With Image – Mouse Follow** · *Indicator Style* See Through Contrast · *Hover Effect* Zoom BG Image · radius 0 | clip lists per page | video ids as in DS | mouse-follow play button | — | NATIVE |
| G29 | „Salient žymės“ overlay (demo only) | Kept (`assets/js/demo.js`), reads `data-salient` | — | — | — | demo | (not counted) |
| G30 | Dark/paper alternation via classes (N) | **Color Change Section** ✓ on every *Chapter row* of home, service template and Tarptautiniai — the page background eases between `#0F1417` and `#F5F7F6` (0.8 s) as each chapter reaches 40 % visibility | — | — | 0.8 s colour sweep | — | NATIVE |
| G31 | Page transitions + smooth scroll (N) | Theme Options: **View Transitions API → Vertical Reveal**; **Smooth Scrolling 60** | — | — | 1.3 s reveal; Lenis lerp .153 | — | NATIVE |
| G32 | (new) next departures in heroes | **Global Section „GS-Artimiausi“** (inserted with the Global Section element into H1, T1, S1): Inner Row 2 × ½: **Label** „Į Airiją“ + Responsive Text (H4) „spalio 9 d.“ + Responsive Text (small) „Atgal iš Airijos – rugsėjo 28 d.“ · same for Ispanija | next date per direction, typed monthly | Ph glass | — | — | NATIVE |

### 3.2 Home `/` (v2 chapter order, Salient construction)

Order (v2 anchors kept): GS-Išvykimai → **H1 #pradzia** (Ph) → **H2 #apie** (P) → **H3 #paslaugos** (A) → **H4 #marsrutai** (P) → **H5 #kelioneje** (Ph) → **H6 #eiga** (P) → **H7 #pries-siunciant** (P-alt) → **H8 #siuntos-sekimas** (A) → [H9 testimonials, disabled] → GS-Kvietimas → GS-Poraštė → GS-Skambučių juosta. H2–H8 are *Chapter rows* with **Color Change Section** ✓, so the page colour sweeps dark ↔ paper between chapters.

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| H1 | #pradzia: video row, Raw HTML route H1 (C), call tiles (N+C), docked board (C), pause button (C) | **Section** → *Type* Full Width Background · *Min Height* **100svh** (phone 90svh, so the call bar never covers the band) · *Layout* **Flexbox** column, *Justify* flex-end · Background **Video** MP4 **29374299** (*Background Video Loading* lazy) + *Background Image* = its poster (the Section has no *Video Preview Image*; the image shows until the video plays and on phones) · phone image = portrait crop of the poster · **Parallax Background Media On Scroll** ✓ → *Scroll Effect* **Parallax Fade** · *Speed* **Medium** · **Color Overlay** Advanced = the v2 hero grade (left→right `#0F1417` .88 → .60 @42 % → .14 @80 %; bottom band to .92) · *Text Color* Light. **Row 1** Column 8/12: **Label** „Tarptautiniai pervežimai mikroautobusais“ + **Animated Text** → *Text Element* **H1** · *Text Effect* **Word Animations: Reveal** · Stagger ✓ · Font sizing custom **5.6vw**, min 40px, max 92px, line height .94 · „Lietuva – Airija.⏎Lietuva – Ispanija.⏎Ir atgal.“ + **Road line** + **Intro** (snow) „Visos pervežimo paslaugos – saugiai, greitai, patikimai. Keleiviai, siuntos, automobiliai, motociklai, gyvūnai ir perkraustymas nuo durų iki durų.“ **Row 2 — glass band:** Inner Row → **Backdrop Filter → Blur 16** · Design options BG `rgba(11,14,16,.55)`, border 1px `rgba(242,244,243,.12)`, radius 3, padding 24px 32px · Inner Columns 5/12: **Label** „Artimiausi išvykimai“ + Global Section element **GS-Artimiausi** (G32) · 4/12: 2 × **Call (red)** „Į Airiją · +370 650 53161“ / „Į Ispaniją · +370 638 28919“ · 3/12 (flex column, end): **Link** „Visas grafikas →“ + pause Button (G27) + **Button → Next Section** *Minimal Arrow Alt*, *Arrow Animation* On Hover Only | H1 = v2's visible route lines (the keyword sentence stays in `<title>`/meta), lead, both calls, next departures | Ph · video 29374299 + poster; phone crop | words rise 1.2 s, 15–50 ms stagger; road line draws; band *Slight Fade In From Bottom* delay 600 ms; background fades at 0.40 while leaving | C-14 | NATIVE+CSS |
| H2 | #apie: paper + rail, statement with red underline, kv, cascade + crop marks, odometer stats (N / N+C) | *Chapter row* P `#F5F7F6`, Row ID `apie`. Row 1: Column 7/12: **Label** „01 · Apie mus“ + **Highlighted Text** → *Style* **Regular Underline** · colour **Accent** · *Underline Thickness* 3px · custom font size 40px / 1.15 (phone 26px) · italic phrase „keleivių, siuntų ir automobilių pervežimu“ gets the line · text = the verbatim company statement · Column 5/12: **Cascading Images** → *Forced Aspect Ratio* 4:5 · layer 1 **7541981** (*CSS Animation* Grow In Reveal, parallax **Subtle**) · layer 2 **6169133** (offset X 20 % Y 25 %, *Layer Padding* Auto — Salient shrinks the layer by its offset, *Fade In From Bottom*, *Box Shadow* Large, parallax **Medium**) · layer radius 0. Row 2 Inner Row: ½ Responsive Text „Nuo pirmos darbo dienos…“ + **KV rows** ×3 (Kryptys · Principas · Draudimas) + **Link** „Skaityti daugiau“ → /apie-imone/ · ½ 4 × **Milestone** (Inner Columns with Border Advanced top 1px hairline) → *Milestone Number Inherit Font* **H2** (BC 500) · *Number Font Size* 96px · *Animation Effect* **Motion Blur Slide In** · delays 0/150/300/450: „2“ kryptys · „11“ paslaugų · „3“ + *Symbol* „–4“ (*Position* After) paros kelyje · „4“ šalys pakeliui | statement, body, 3 of 6 kv rows (all 6 on /apie-imone/), 4 true stats, link | P · 7541981, 6169133 | underline grows .9 s; cascade layers drift at 0.20 / 0.40; digits blur-slide in | — | NATIVE |
| H3 | #paslaugos horizontal „road“ of 11 cards + lane + counter (C) | *Chapter row* A `#0F1417`, Row ID `paslaugos`. Row 1: **Label** „02 · Paslaugos“ + H2 „Visos pervežimo paslaugos“ + **Road line** + **Link** „Visos 11 paslaugų sąrašu →“ /pervezimo-paslaugos/. Row 2 Full Width Content: **Sticky Content Sections** → *Type* **Horizontal Scrolling** · *Effect* None · **Section Width 45** · *Section Height* 100vh · **Subtract Navigation Height** ✓ · gap 8px · *Content Alignment* Stretch · *Border Radius* 3 · *Effect Enabled* desktop ✓ tablet ✓ phone ✗ (stacks) · 6 × **Sticky Content Section** → *Section Type* **Color** `#161D21` · *Link* `/pervezimo-paslaugos/#<group-id>` + **Link Mouse Indicator** („Plačiau“, BG Accent, text `#0F1417`) · inside: numeral „01“ (Responsive Text, H1 font, 120px, `#EF4539`) + H3 group name + **Intro** group lead + **Fancy UL** (dash, fog) with its service names as text + **Image** (group media, 16:10, *Fit to Container*, *Hover Animation* Zoom In) | 6 groups (`paslaugos.json` names), their services, leads | A · 38927007, 7464731, 29566910, 36377055, 3868901, 4487517 | pinned horizontal track; mouse indicator follows the cursor; image zoom .65 s | — | NATIVE |
| H4 | #marsrutai route tabs + SVG maps (C) + timetables (C) | *Chapter row* P `#F5F7F6`, Row ID `marsrutai`. Row 1: **Label** „03 · Maršrutai“ + H2 „Dvi kryptys. Keturios šalys pakeliui.“ + **Road line**. Row 2 Full Width Content: **Scrolling Text** → *Scrolling Speed* **Slowest** (`slower`, 45 s) · *Italic Style* **Text Outline** · *Outline Thickness* Thin · *Outline Applies To* Text Content and Custom Divider · **Move on Scroll** ✓ · **Mask Edges** ✓ · divider „✦“ + **Spin on Scroll** ✓ · *Custom Font Size* 8vw (mobile 16vw) · H2 text in ink: „Lietuva ✦ Lenkija ✦ Vokietija ✦ Belgija ✦ Prancūzija ✦ Ispanija ✦ Airija“. Row 3: Column 12 (max 1100 centred) on a **Callout** surface without the red edge: **Image With Hotspots** on `assets/img/marsrutai.svg` · *Hotspot Icon* **Numerical** · *Tooltip* Show On Hover · tooltip shadow Medium Depth · **Enable Animation** ✓ · colour **Accent** · 7 hotspots (Vilnius, PL, DE, BE, FR „Pakeliui – galite perduoti siuntą čia gyvenantiems artimiesiems.“; IE „Airija · +353 86 450 3104“; ES „Ispanija · +34 602 547 929“). Row 4: **GS-Maršrutai** (G12) with the 3rd column „Pakeliui“ | H2, paragraph, route cards, phones, the map idea | P · static map image (IE leg dashed „maršrutas tikslinamas“) | outline marquee moves with scroll, ✦ spins; hotspots pop in and pulse | C-7 | NATIVE+CSS |
| H5 | #kelioneje cinematic video row + comfort stops on a lane (N+C) | Row → *Type* Full Width Background · Background **Video** MP4 **4685871** + *Video Preview Image* · **Parallax Background Media On Scroll** *Speed* **Regular** · *Background Layer Animation* **Clip Path Inset** → *Clip Path Animation Type* **Scroll Position** · *Applies To* Background Layer · *Inset Start* 0 / 6 % / 0 / 6 % · *Roundness Start* 3px → *End* 0 / 0 · *Viewport Trigger Offset* 0–50 · *Clip Path Animation Addon* Zoom Fade In · **Color Overlay** Advanced (v2 cinematic: top/bottom to `#0F1417`, 32 % middle) · *Text Color* Light · padding 12 % / 8 % · Row ID `kelioneje`. Column 8/12: **Label** „04 · Kelionėje“ + **Animated Text** H2 → *Text Effect* **Scroll Position: Opacity** „Du namai, vienas kelias tarp jų.“ + **Intro** „Kelionė trunka apie 3–4 paras – pasirūpinsime, kad laikas neprailgtų.“ Row 2: **Icon List** → *Direction* Horizontal · 5 columns (tablet 3, phone 1) · *Icon Style* Icon Colored No BG · icon colour Accent · Animate ✓ · items (Font Awesome glyphs) with the 5 comfort titles + verbatim texts („Atlenkiamos sėdynės“, „Šildomos sėdynės“, „Kondicionierius“, „Keleiviai apdrausti“, „Poilsio režimas“) · + **Video Lightbox** → Play Button With Image – Mouse Follow on **3987777** (poster) „Kelionė keltu“ (NEW label) + **Link** „Keleivių pervežimas →“ | H2 + lead (v2), 5 comfort titles + texts, link | Ph · video 4685871, 3987777 | band opens from a 6 % inset to full bleed as it scrolls in; video parallax 0.28; words brighten .2 → 1; icons fade in one by one | — | NATIVE |
| H6 | #eiga process stations on a lane (W) | *Chapter row* P, Row ID `eiga`: Column 4/12 **Sticky Content** (CSS, Top): **Label** „05 · Kelionės eiga“ + H2 „Nuo durų iki durų“ + **Road line** · Column 8/12: **Stations** (1 Paėmimas · 2 Kelyje apie 3–4 paras · 3 Pristatymas, verbatim texts) + **KV rows** ×2 (Kelyje · Įsipareigojimas siuntoms) + **Link** „Siuntos sekimas →“ + Inner Column → **Column Animation Type: Scroll Position Advanced** (Start: Translate Y 60, Scale .92 → End: 0, 1; *Viewport Trigger Offset* 0–100) holding **Image** 4440774 (16:10, radius 0) | 3 steps + 2 facts verbatim | P · 4440774 | road draws, numbers pop in; the photo rises and scales with scroll | — | NATIVE |
| H7 | #pries-siunciant rules accordion (N+C) | *Chapter row* P-alt `#EAEEED`, Row ID `pries-siunciant`: Column 5/12 **Sticky Content** (CSS, Top): **Label** „06 · Prieš siunčiant“ + H2 verbatim „Krovinių pervežimas tarptautiniais maršrutais: ko negalima siųsti?“ + **Callout** (BG `#FFFFFF`) „Už siuntinio turinį atsakingas siuntėjas.“ + **Lift button** „Visos taisyklės“ + **Link** (*Icon* download) „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“ · Column 7/12: **Toggle Panels** → *Style* **Animated Circle** · Position Right · Size 40 · **Divider** ✓ · Accordion ✓ · First Toggle Open · radius 3 · panels „Draudžiama siųsti (12)“ (Fancy UL ✕) · „Pakavimas (4)“ · „Gavėjas ir pristatymas“ · „Baudos“ (**KV rows** 40\|60 + **Link** „Plačiau taisyklėse →“) | 4 panels verbatim, callout, buttons | P-alt | circle draws + panel opens .85 s `(.76,0,.24,1)`; deep link `?toggle=1`; lift on the button | — | NATIVE |
| H8 | #siuntos-sekimas strip, Raw HTML form (C) | *Chapter row* A `#0F1417`, Row ID `siuntos-sekimas`, Equal Height: Column 6/12 **Card** (A) padding 48: **Label** „07 · Siuntos sekimas“ + H2 „Siuntos sekimas“ + Responsive Text „Neradote siuntos kodo? Paskambinkite – pasakysime, kur Jūsų siunta.“ + **Fluent Forms** „Siuntos sekimas“ (1 required field „Siuntos kodas“, submit „Ieškoti“; *Confirmation* **Redirect to URL** `/siuntos-sekimas/?kodas={inputs.kodas}`) · Column 6/12: Inner Column **Mask Reveal** (Direction Right, Straight) with **Image** 6170458 (Fit to Container) | H2, helper, field + error texts verbatim | A · 6170458 | image wipes in 1.3 s; submit lift | C-6 | NATIVE+CSS |
| H9 | Reviews placeholder (N) | Row → **Disable row** ✓; later **Sticky Content Sections → Layered Card Reveal** (4:5, radius 3) with real reviews only | — | — | — | — | NATIVE |

### 3.3 Inner-page head (Architect „About“ structure, v2 dark mood) — used by A1, P1, R1, K1, L1, C1, V1

Row → *Type* Full Width Background · BG colour `#0F1417` + *Background Image* = the page's v2 header photo (front matter `hero_media`; none on Privatumo politika) · **Parallax Background Media On Scroll** *Speed* **Subtle** (0.20) · *Background Layer Animation* **Slight Zoom Out Reveal** · Color Overlay `#0B0E10` Heavy (0.8) · *Text Color* Light · *Min Height* 56svh (phone 48svh) · padding top 168px (header 84 + ticker + air) / bottom 64px. Column **9/12**: breadcrumbs (G22, Label typography) + **Label** (page eyebrow) + **Animated Text** → *Text Element* **H1** · *Text Effect* **Word Animations: Reveal** · Stagger ✓ + **Road line** + **Intro** (lead). Column **3/12** (flex column, gap 10, bottom aligned): 3–4 × **Link** to the page's own Row IDs. Phones: the link column drops under the lead as a wrap. Verdict **NATIVE**, CSS —.

### 3.4 `/apie-imone/`

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| A1 | Photo route header + breadcrumb + chips + ticket (N+C) | **Inner head** (§3.3): Label „Saugiai, greitai, patikimai“ · H1 „Apie įmonę“ · lead „SGP – visos pervežimo paslaugos“ · links Įmonė · Principai · Kelyje · Kodėl mes | H1, lead, eyebrow | Ph · 9989463 | words rise; bg zoom-out reveal 1.3 s + parallax 0.20 | — | NATIVE |
| A2 | (the photo was the header bg) | Row Full Width Content, padding 0: BG image **38404178** (fleet of black trucks) · *Background Layer Animation* **Clip Path Inset** → *Scroll Position* · *Applies To* Background Layer · *Inset Start* 0 / 8 % / 0 / 8 %, *Roundness Start* 3px → End 0 · trigger 0–60 · **Parallax** *Speed* Regular · Divider No Line **70vh** (phone 45vh) as the height | — | Ph · 38404178 | the photo widens to full bleed while scrolling; parallax 0.28 | — | NATIVE |
| A3 | #imone statement + text + sticky kv (N) | *Chapter row* P, Row ID `imone`: **Label** „Įmonė“ + **Highlighted Text** (Regular Underline, Accent, 3px, 40px) with paragraph 1 „„SGP“ – esame įmonė…“ · Inner Row: 5/12 Responsive Text paragraphs 2–3 („Nuo pirmos darbo dienos…“, „Mes visada pasiruošę…“) + **Button (ink)** „Pervežimo paslaugos“ + **Link** „Kontaktai“ · 1/12 empty · 6/12 **KV rows** ×6 (Veikla, Kryptys, Taip pat, Principas, Draudimas, Vairuotojai) | 3 paragraphs verbatim, datasheet, 2 buttons | P | underline grows; KV lines draw | — | NATIVE |
| A4 | ab-promise mini route: ring → lane → ring (N+C) | **Dropped** (the statement carries the promise) | — | — | — | — | DROPPED |
| A5 | Buttons under the text (N) | merged into A3 | — | — | — | — | DROPPED |
| A6 | Milestones ×4 with odometer (N+C) | *Chapter row* A `#0F1417`: 4 Columns ¼ (tablet ½) with **Border Advanced** top 1px `rgba(242,244,243,.26)` + **Enable Border Animation**, padding-top 28: **Label** („Kryptys“ …) + **Milestone** (inherit H2, 96px, **Motion Blur Slide In**, delays 0/150/300/450) + caption | 2 / 11 / 3–4 / 4 | A | top lines draw; digits blur-slide in | — | NATIVE |
| A7 | #principai pinned cards, WRONG „Stacking“ + progress rings (W) | Row ID `principai`, A: **Label** „Principai“ + **Intro** (verbatim lead „Saugumas, operatyvumas…“) · **Sticky Content Sections** → *Type* **Sticky Scroll Pinned Sections** · *Effect* **Scale** · **Stacked Appearance** ✓ · *Section Navigation* ✗ · *Section Height* 80vh · *Border Radius* 3 · *Effect Enabled* tablet ✗ phone ✗ · 5 × Sticky Content Section (**Color**: `#161D21` / `#EAEEED` / `#161D21` / `#EAEEED` / `#161D21`, text Light/Dark to match): Inner Row ½ numeral „01“ (Responsive Text, H1 font, 96px, Accent) + H3 + verbatim paragraph · ½ **Image** 4:5, radius 0, *Animation* Reveal Rotate From Bottom | 5 principles verbatim (DS§6.2 edits) | A · 31570314, 17720190, 6720534, 17455631, 27383867 | previous card scales 1 → .92, −54 px when stacked; photos rotate-reveal 2.3 s | — | NATIVE |
| A8 | #kelyje Flickity gallery + custom counter (N) | *Chapter row* P, Row ID `kelyje`: **Label** „Kelyje“ + H2 „Kelyje apie 3–4 paras“ · **Image Gallery** → *Type* **Flickity Style** · *Controls* **Touch Indicator and Total Visualized** · spacing 10px · columns 2 / 1 / 1 · **Image Parallax** ✓ · **Mask Edges** ✓ · **Subtle Image Scale When Dragging** ✓ · radius 0 | same 5 photos | P · 11053641, 2449454, 8858566, 21041157, 1606957 | drag with touch indicator; parallax inside frames | — | NATIVE |
| A9 | #pasitikejimas GS-Trust: sticky heading + masked photo + 9 rows on a lane (C) | **Global Section „GS-Pasitikėjimas“** (also on Tarptautiniai): *Chapter row* A, Row ID `kodel-mes`: Column 5/12 **Sticky Content** (CSS, Top): **Label** „Kodėl mes“ + H2 „Kodėl verta pasitikėti mumis?“ + Inner Column with BG image 7541981, *Background Layer Animation* **Mask Reveal** (Bottom, Straight), height 50vh · Column 7/12: **Link rows**-style **Horizontal List Item** ×9 → 2 cols **20% \| 80%** · *Style* Bottom Border, No Hover Effect · **Border Animation** ✓ („01 \| **first clause** rest“) | 9 bullets with approved fixes | A · 7541981 | mask reveal 1.3 s; lines draw | — | NATIVE |
| A10 | GS-Trust photo mask reveal (W) | merged into A9 | — | — | — | — | DROPPED |
| A11 | GS-Board + GS-Arrival | **GS-Kvietimas** (G24) + footer | — | — | — | — | NATIVE |

### 3.5 `/pervezimo-paslaugos/`

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| P1 | Photo route header (N+C) | **Inner head**: Label „Paslaugos“ · H1 „Pervežimo paslaugos“ · lead verbatim („Pervežimo paslaugų poreikis Europoje nuolat auga…“) · links Visos paslaugos (`#visos-paslaugos`) · Kryptys ir transportas (`#kryptys`) | H1, lead | Ph · v2 header photo | words rise; zoom-out reveal | — | NATIVE |
| P2 | 3 ticket tiles with notches, tilt, hover video, live date (C) | *Chapter row* P, Equal Height, Column Margin 10px: 3 × **Photo card** (Tether-style grid, *Entrance* 0/120/240): „Tarptautiniai pervežimai“ (36383706, „11 paslaugų · 2 kryptys“) · „Pervežimų grafikas“ (1696742, „Artimiausios išvykimo datos abiem kryptimis.“) · „Siuntos sekimas“ (13456097, „Pagal siuntos kodą“); each: **Label** meta + H3 + **Button (paper)** „→“ (decorative, the Column Link carries the URL) | tile titles + metas (live date → static meta) | Ph cards on P · 36383706, 1696742, 13456097 | overlay .72 → .42 on hover (photo brightens), arrow circle | — | NATIVE |
| P3 | #visos-paslaugos pinned „Stacking“ (W) + ring index (C) + row-hover photo swap (C) | Row ID `visos-paslaugos`, A: **Label** „Visos paslaugos“ + H2 „Visos pervežimo paslaugos“ · **Sticky Content Sections** → **Sticky Scroll Pinned Sections** · *Effect* **Blurred Scale** · **Stacked Appearance** ✓ · **Section Navigation** ✓ (colour Accent) · *Section Height* 85vh · radius 3 · *Effect Enabled* tablet ✗ phone ✗ · 6 × Sticky Content Section (**Color** alternating `#161D21` / `#EAEEED`, each with the group's id as anchor): Inner Row ½: numeral + H2 group + group lead + **Link rows** (one per service; *Hover Color* Extra Color 2 on dark cards, Extra Color 1 on paper cards) · ½ **Image** 4:5 (one per group, *Hover Animation* Zoom In Crop) | 6 groups, 11 services + one-liners | A · as H3 (home) | blurred-scale stack (1 → .92, blur 5 px); dots navigate; rows flip; image zoom-crop | — | NATIVE |
| P4 | CTA „Nežinote, kurią paslaugą rinktis?“ (N+C) | *Chapter row* P, centred: **Statement** verbatim + **Road line** (centred) + 2 × **Call (red)** (both LT lines) | statement, numbers | P | words rise; arrow circles | — | NATIVE |
| P5 | #kryptys why row with scaling photo (N) | *Chapter row* P-alt, Row ID `kryptys`: Column 5/12 **Sticky Content**: **Label** „Kryptys ir transportas“ + H2 verbatim „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ · Column 7/12: Responsive Text paragraphs (approved fixes) + **KV rows** (delivery facts) + Inner Column → **Scroll Position Advanced** (Start Scale .88, Y 40 → End 1, 0; trigger 0–100) with **Image** 32821932 (*Hover Animation* **Zoom In Crop**) | paragraphs verbatim | P-alt · 32821932 | scroll-linked scale; zoom-crop .65 s | — | NATIVE |
| P6 | GS-Board + GS-Arrival | **GS-Maršrutai** (G12, 2 columns, on A) + **GS-Kvietimas** | — | — | — | — | NATIVE |

### 3.6 `/pervezimo-paslaugos/tarptautiniai-pervezimai/`

T2–T10 are *Chapter rows* with **Color Change Section** ✓.

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| T1 | Video route header + pause toggle (N) | **Section** → Full Width Background · *Min Height* **85svh** (phone 80svh) · Flexbox column, flex-end · Background **Video** MP4 **13707149** + *Background Image* = its poster (phone image: 36383706 crop) · **Parallax Fade** (Medium) · v2 hero grade overlay · Text Light: breadcrumbs + **Chip** (glass) „2 kryptys · 11 paslaugų“ + **Animated Text** H1 *Word Animations: Reveal* „Tarptautiniai pervežimai“ + **Road line** + **Intro** verbatim lead + glass band (as H1: Inner Row *Backdrop Filter → Blur 16*) with **GS-Artimiausi** + 2 × **Call (red)** + pause Button | H1, lead, chips, both calls, next departures | Ph · video 13707149, 36383706 | words rise; background fades at 0.40 | C-14 | NATIVE+CSS |
| T2 | #marsrutai H2 + bullets + 2 route rows + hotspot schematic (N+C) | *Chapter row* P, Row ID `marsrutai`: ½ **Label** „Maršrutai“ + **Animated Text** H2 verbatim „Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais“ + **Road line** + **Fancy UL** (dash) 2 bullets + **Link rows** ×2 („Lietuva – Airija – Lietuva →“ `#airija`, „Lietuva – Ispanija – Lietuva →“ `#ispanija`) · ½ **Image With Hotspots** on `assets/img/marsrutai.svg` (as H4: Numerical, Show On Hover, Enable Animation, Accent; PL/DE/BE/FR „Pakeliui – galite perduoti siuntą čia gyvenantiems artimiesiems.“, IE „Airija · +353 86 450 3104“, ES „Ispanija · +34 602 547 929“) | H2, bullets, tooltips | P · map image | hotspots pop in and pulse; rows flip | C-7 | NATIVE+CSS |
| T3 | Both-routes SVG map (C) | merged into T2 (static image) | — | — | — | — | DROPPED |
| T4 | Overlapping chapters Airija / Ispanija (N) | **Sticky Content Sections** → **Sticky Scroll Pinned Sections** · *Effect* **Overlapping** (overlap 50) · **Subtract Navigation Height** ✓ · *Section Height* 100vh · *Effect Enabled* tablet ✗ phone ✗ · 2 × **Sticky Content Section** → *Section Type* **Image** (2881400 / 22033738), IDs `airija`, `ispanija`, content per T5 | as T5 | Ph · 2881400, 22033738 | the second chapter slides over the first | — | NATIVE |
| T5 | Chapter content ×2 (N+C) + route strips (C) + timetables (C) + insets „Mask Reveal“ (W) | Inside each section: Inner Column ½ → *Background Color* `rgba(11,14,16,.72)` + **Backdrop Filter → Blur 16** · radius 3 · padding 40 · Text Light: **Label** „Airija“ + H2 „Lietuva – Airija – Lietuva“ + **GS-Grafikas Airija** (A variant) + **KV rows** (Kelyje · Įsipareigojimas) + **Call (red)** „+370 650 53161“ + **Link** „Airijoje +353 86 450 3104“ · „JK +44 7566 878681“ · Inner Column ½: **Cascading Images** (*Forced Aspect Ratio* 4:5; layer 1 *Grow In Reveal*, layer 2 offset X 20 % Y 25 % *Fade In From Bottom*; **Enable Parallax Scrolling** Subtle / Medium; radius 0). Ispanija the same with ES data | H2s, timetables, phones, facts, insets | Ph glass · insets 13568682, 3220828 / 27868340, 34497909 | grow-in reveal + layer parallax; timetable rows flip white | C-5 | NATIVE+CSS |
| T6 | #pakeliui countries on a drawing lane (C) | *Chapter row* P, Row ID `pakeliui`: **Label** „Pakeliui“ + Responsive Text verbatim paragraph · **Scrolling Text** → *Speed* **Slowest** · **Move on Scroll** ✓ · *Italic Style* Text Outline (Thin) · font 8vw · divider „✦“ + Spin on Scroll: „Lenkija ✦ Vokietija ✦ Belgija ✦ Prancūzija“ · + **Video Lightbox** (Mouse Follow) on **12421166** „Kelionė per Europą“ (NEW label) | paragraph, 4 countries | P · video 12421166 | marquee moves with scroll; play button follows the cursor | — | NATIVE |
| T7 | #kodel-mes trust list (N+C) | **GS-Pasitikėjimas** (A9) | 9 reasons | A · 7541981 | as A9 | — | NATIVE |
| T8 | #ko-negalima-siusti (N+C) | *Chapter row* A, Row ID `ko-negalima-siusti` · BG image **4040619** (asphalt texture) + Color Overlay `#0F1417` Very Heavy (.95) + **Parallax** Subtle · Text Light: Column 7/12: **Label** „Ko negalima siųsti“ + H2 verbatim + intro + **Fancy UL ✕** (8 items, Accent) · Column 5/12 **Sticky Content**: **Callout** (A) with the two verbatim paragraphs + **Button (paper)** „Visos taisyklės“ | H2, 8 bullets (fix), 2 paragraphs | A · 4040619 | items fade in one by one; texture drifts at 0.20 | — | NATIVE |
| T9 | #ka-dar-zinoti 4 cards with top rule (N+C) | *Chapter row* P: **Label** „Ką dar verta žinoti“ + H2 verbatim · 4 Columns ¼ (tablet ½) with **Border Type Advanced** top 1px ink + **Enable Border Animation**, padding-top 28, **Entrance** 0/120/240/360: **Label** „01“… + H4 („Pristatymas“, „Pakavimas“, „Adresai ir gavėjas“, „Iškrovimas“) + verbatim text (card 1 = KV rows delivery facts) | 4 cards verbatim | P | top rules draw; slight fade-up | — | NATIVE |
| T10 | #paslaugos GS-ServiceList (N) | *Chapter row* A: **Label** „Paslaugos“ + H2 „Visos pervežimo paslaugos“ + **GS-Paslaugos** (G18, hover Extra Color 2) + **Link** „Pervežimo paslaugos →“ | list | A | rows flip paper-white | — | NATIVE |
| T11 | GS-Arrival | **GS-Kvietimas** | — | — | — | — | NATIVE |

### 3.7 Service template (one WPBakery template „SGP – paslauga“ → 11 pages)

Order: S1 hero → S2 submenu → S3 Faktai → S4 Apie paslaugą (+ S4b Kaip tai vyksta where present) → S5 Privalumai → S6 special → S7 Kliento atsakomybės → S8 Draudžiami daiktai → S9 GS-Maršrutai → S10 Uždarymas → S11 Susijusios paslaugos → S12 Kita paslauga → S13 GS-Užklausa (#uzklausa) → footer. Keleivių and Gyvūnų pages keep their DS§6.5 variations (S8 omitted, own submenu). S3–S10 are *Chapter rows* with **Color Change Section** ✓.

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| S1 | T1 route header: breadcrumb, index, H1, chips, call ticket (N+C) | **Section** → Full Width Background · *Min Height* **85svh** (phone 78svh) · Flexbox column, flex-end · *Background Image* `hero` + phone crop · **Parallax Fade** (Medium) · v2 hero grade · Text Light: breadcrumbs + **Chip** (glass) „01 / 11 · Tarptautiniai pervežimai“ + **Animated Text** H1 *Word Animations: Reveal* `h1` + **Road line** + **Intro** `lead` (max 60ch) + `chips` as glass **Chips** + glass band with **GS-Artimiausi** + 2 × **Call (red)** | h1, lead, chips, calls, index, next departures | Ph · `hero` per service (DS§6.5) | words rise; background fades at 0.40 | — | NATIVE |
| S2 | T1b sticky submenu, custom scrollspy (N+C) | **Page Submenu** → *Link Alignment* **Left** · **Sticky?** ✓ · *Menu BG Color* `#0F1417` · *Link Color* `#F2F4F3` · items = **Menu Link** (`submenu` labels → Row IDs) | submenu labels | A | Salient scrollspy; active item gets a 2 px red underline (C-8) | C-8 | NATIVE+CSS |
| S3 | T2 Faktai: kv + outlined chips (N+C) | *Chapter row* P, Row ID `faktai`: Column 7/12 **KV rows** (`kv`) · Column 5/12: **Label** „Kryptys ir paslaugos“ + `routes` as **Button → See Through** · Preset **sm** · *Button Roundness* 3 · border `rgba(28,29,29,.26)` → hover fill ink · Display inline → `?domina=<h1>#uzklausa` | kv rows, route chips | P | rows draw in; chips fill on hover | — | NATIVE |
| S4 | T3 Apie paslaugą: sticky H2 + text (N) | *Chapter row* P-alt, Row ID `apie-paslauga`: Column 4/12 **Sticky Content**: **Label** „Apie paslaugą“ + **Road line** · Column 8/12 Responsive Text `intro` paragraphs (Max Width 68ch), **Entrance** | intro verbatim | P-alt | slight fade-up | — | NATIVE |
| S4b | „Kaip tai vyksta“ 3 stations on a lane (N+C) | **Stations** ×3 (as H6) | stations verbatim | P-alt | road draws; numbers pop | — | NATIVE |
| S5 | T4 Privalumai sticky media, dark (N) | *Chapter row* A, Row ID `privalumai`: **Label** „Privalumai“ + H2 verbatim „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“ · **Sticky Content Sections** → *Type* **Sticky Media, Scrolling Content** · Content **Right** · **Media Width 45%** · **Media Height 80vh** · Content Spacing 30vh · *Border Radius* 3 · mobile aspect **4:5** · children = Sticky Content Section (**Image** `why_media[i]`) with H4 (first sentence) + Responsive Text | `why` paragraphs (first sentence → H4) | A · `why_media` ×3 | media swaps as the text blocks pass (Salient's own) | — | NATIVE |
| S6 | T5 special block | see §3.8 | | | | | |
| S7 | T6 Kliento atsakomybės accordion (N+C) / single callout | *Chapter row* P, Row ID `atsakomybes`: Column 5/12 **Sticky Content**: **Label** „Kliento atsakomybės“ + H2 verbatim + intro · Column 7/12: **Toggle Panels** → **Animated Circle** (Right, 40, Divider ✓, Accordion ✓, First Toggle Open, radius 3) with `responsibilities` · one item → **Callout** | titles NEW, texts verbatim | P | circle .85 s; deep link `?toggle=N` | — | NATIVE |
| S8 | T7 Draudžiami daiktai dark texture (N+C) | *Chapter row* A, Row ID `draudziami`, BG image 4040619 + overlay .95 + Parallax Subtle (as T8): Column 7/12 **Label** „Draudžiami daiktai“ + lead + **Fancy UL ✕** (`prohibited`) + „Šis sąrašas nėra baigtinis…“ · Column 5/12 **Callout** (A): **Milestone** „1200“ *Symbol* „EUR“ · *Position* After · *Symbol Alignment* **Superscript** · *Count To Value* + Responsive Text „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“ + **Button (paper)** „Visos taisyklės“ | list verbatim, fine teaser | A · 4040619 | count 2.2 s; list fades in | — | NATIVE |
| S9 | T8 GS-Board (C) | **Label** „Maršrutai“ + **GS-Maršrutai** (G12, 2 columns, on P) | route cards | P | Entrance; road lines draw | — | NATIVE |
| S10 | T9 Uždarymas: underlined statement + tickets (N+C) | *Chapter row* P-alt: **Highlighted Text** → *Style* **Regular Underline** · colour **Accent** · 3px · custom font size 40px / 1.15 (phone 26px) · the 2 key phrases in italics get the red line · + 2 × **Call (red)** | `closing` verbatim | P-alt | line grows .9 s `(.15,.75,.4,1)` | — | NATIVE |
| S11 | Related service cards ×3 + hover video (N+C) | *Chapter row* P: **Label** „Susijusios paslaugos“ · 3 × **Fancy Box → Image Above Text** 3:2 (G19), **Entrance** 0/120/240 | 3 related services | P · their `hero` ids | image scale 1.1 + underline | — | NATIVE |
| S12 | T10 „Kita stotelė“ band with photo fade + lane (N+C) | Row Full Width Content, padding 0: **Photo card** (next service's `hero`), radius 0, *Min Height* 50vh, overlay **.85 → .55** on hover, **Column Link** `next_url`, BG parallax Very Subtle: **Label** „Kita paslauga · 02 / 11“ + **Animated Text** H2 „Negabaritinių krovinių pervežimas“ + **Button (paper)** „→“ | next service name + index („Kita stotelė“ → „Kita paslauga“) | Ph · next `hero` | photo brightens on hover (.45 s); arrow circle | — | NATIVE |
| S13 | T11 GS-Arrival form with `domina` pre-select (N+C) | **Row ID `uzklausa`** + **GS-Užklausa** (G25); Fluent Forms default value `{get.domina}` | form | A · `why_media[0]` | as G25 | C-6 | NATIVE+CSS |

### 3.8 Per-service special blocks (S6)

| # | Service · Now (v2) | New — Salient 18.2.1 | CSS | Verdict |
|---|---|---|---|---|
| X1 | kroviniu · 4 packing rules on a red lane (N+C) | **Label** „Esminės krovinių pakavimo taisyklės“ + **Stations** ×4 (Icon List, 4 columns, numbers 1–4) | — | NATIVE |
| X2 | automobiliu + motociklu · cinematic b/w video band (N) ×2 | *Chapter row* A: **Video Lightbox** → *Play Button With Image – Mouse Follow* (poster 29566910 / 4858429, video 34371915 / 34308329, 16:9, radius 0, *Hover Effect* Zoom BG Image) + Responsive Text (verbatim „Tai nėra įprastinis krovinys…“ / origins as **Chips**) | — | NATIVE |
| X3 | daiktu · large outline tag buttons (N) | **Chip** ×4, custom font size 15px, *Padding Amount* Large („Langai · Žoliapjovės · Buitinė įranga · Smulkios siuntos“) | — | NATIVE |
| X4 | daliniu · inline SVG bays diagram (C) | **Image** `assets/img/paslaugos/daliniai-skyriai.svg` (static illustration: ink lines, one red bay), *Animation* **Fade In From Bottom**, on a **Callout** + caption verbatim | — | NATIVE |
| X5 | gyvunu · „Prieš kelionę“ checklist with remembered ticks (C) | **Toggle Panels** → *Style* **Minimal Shadow** (Tether), Accordion ✗ (multi-open), radius 3, 5 items verbatim; ticks and storage dropped | — | NATIVE |
| X6 | gyvunu · „Kaina“ factors, WRONG Fancy Box „minimal“ (W) | Verbatim paragraph + 3 × **Card** (P) each with **Icon** → library **Linea** (line-draw on entrance, speed Medium) · *Icon Style* **Border W/ Hover Animation** · colour Accent + H4 „Narvo dydis“ / „Priežiūros sudėtingumas“ / „Atstumas“ | — | NATIVE |
| X7 | gyvunu · statement + call button opening the popover (N) | **Statement** verbatim + 2 × **Call (red)** | — | NATIVE |
| X8 | keleiviu · „Principai“ pinned „Stacking“ (W) | as A7 (**Pinned Sections → Scale + Stacked Appearance**) with the keleivių media set | — | NATIVE |
| X9 | keleiviu · „Patogumai“ hotspots + legend (N+C) | **Image With Hotspots** on 36377055 (Numerical, Accent, Tooltip Show On Hover, Enable Animation) + **Stations**-style **Icon List** (vertical, numbers) as the legend | C-7 | NATIVE+CSS |
| X10 | keleiviu · „Kokie dar privalumai?“ kv (N+C) | **KV rows** (Kaina · Pažintys · Draudimas · Poilsio režimas) | — | NATIVE |
| X11 | negabaritiniu · definition callout + looping video (N+C) | **Callout** (A) with the verbatim definition + **Video Lightbox** Mouse Follow (video 19552565, poster 35332902) | — | NATIVE |
| X12 | perkraustymo · red-outline callout (N+C) | **Callout** (P, red left edge) with the verbatim paragraph + note + **Link** „Gyvūnų pervežimas →“ | — | NATIVE |
| X13 | siuntu-pervezimas · SVG packing guide (C) | **Image** `assets/img/paslaugos/pakavimas-5cm.svg` (static box section with the 5 cm dimension line), on a **Callout** + caption verbatim | — | NATIVE |
| X14 | siuntu-pristatymas · 3-stop lane (N+C) | **Stations** ×3 („Paimame iš siuntėjo · Kelyje apie 3–4 paras · Į rankas gavėjui“) | — | NATIVE |
| X15 | single-responsibility callout (4 services) (N+C) | **Callout** | — | NATIVE |

### 3.9 `/pervezimu-grafikas/`

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| R1 | Compact dark header 44svh (N) | **Inner head**: Label „Grafikas“ · H1 „Pervežimų grafikas“ · lead „Artimiausios išvykimo datos abiem kryptimis.“ · links Lenta · Ką verta žinoti | H1, lead | Ph · v2 header photo | words rise | — | NATIVE |
| R2 | „Atnaujinta …“ stamp set automatically (C) | typed **Label** „Atnaujinta rugsėjo 23 d.“ inside GS-Grafikas (G11) | stamp | — | — | — | NATIVE |
| R3 | #lenta dark board with tabs + shortcode table (C) | *Chapter row* A, Row ID `lenta`: **Tabs** → *Style* **Minimal Alt** (the only tab style set in the Label typography) · *Tab Change Animation* Fade · tabs „Visi“ (GS-Grafikas Airija + GS-Grafikas Ispanija) · „Airija“ · „Ispanija“ · deep link `?tab=airija` | all rows, groups „Iš Lietuvos / Į Lietuvą“ | A | 4 px underline slides .3 s; rows flip paper-white | C-5 | NATIVE+CSS |
| R4 | Board footer button „Regular, Line“ (W) | 2 × **Call (red)** (both LT lines) under the tabs | numbers | A | arrow circle | — | NATIVE |
| R5 | #laiko-juosta lane chart (C) | **Dropped** (the tabs show the same data) | — | — | — | — | DROPPED |
| R6 | #ka-verta-zinoti facts + map (C) | *Chapter row* P, Row ID `ka-verta-zinoti`: Column 5/12 **Sticky Content**: **Label** + H2 „Laiką ir vietą suderinsime telefonu“ + **KV rows** („Išvykimo laikas ir vieta“, Kelyje, Įsipareigojimas) + 2 × **Link** · Column 7/12 **Image With Hotspots** on the map image (same hotspots as H4) | facts, links | P · map image | hotspots pop in | C-7 | NATIVE+CSS |
| R7 | GS-Arrival | **GS-Kvietimas** | — | — | — | — | NATIVE |

### 3.10 `/siuntos-sekimas/`

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| K1 | Compact photo header (N) | **Inner head**: Label „Sekimas“ · H1 „Siuntos sekimas“ · lead „Įveskite siuntos kodą ir sužinokite, kur yra Jūsų siunta.“ (from the meta) · links Paieška · Pagalba | H1 | Ph · 35497082 | words rise | — | NATIVE |
| K2 | #paieska Raw HTML tracking form (C) | *Chapter row* P, Row ID `paieska`, Equal Height: Column 2/5 **Callout** (P, padding 40): H2 „Kur keliauja Jūsų siunta?“ + **Fluent Forms** „Siuntos sekimas“ (field „Siuntos kodas“, required message „Neįvestas siuntos kodas!“, submit „Ieškoti“; *Confirmation* **Redirect to URL** `https://siuntos.sgp-pervezimai.lt/sekimas.php?kodas={inputs.kodas}`) · Column 3/5: Inner Column **Mask Reveal** (Right, Straight) with **Image** 6407553 | H2, field, messages verbatim | P · 6407553 | image wipes in; submit lift | C-6 | NATIVE+CSS |
| K3 | #rezultatas iframe on a crop-marked frame (C) | **Dropped** at launch (the tool opens in its own page via the redirect). Demo only: `?kodas=SGP-DEMO` shows a Callout result (`demo.js`) | — | — | — | — | DROPPED |
| K4 | #pagalba help + 3 link cards (N+C) | *Chapter row* A, Row ID `pagalba`: **Label** „Pagalba“ + H2 „Neradote siuntos kodo?“ + 2 × **Call (red)** · 3 × **Fancy Box → Description on Hover** (Siuntų pristatymas · Pervežimų grafikas · Taisyklės) | texts | A · 13456097, 1696742, 6169133 | cards lift −10 px, text rises, short zoom | — | NATIVE |
| K5 | GS-Arrival | **GS-Kvietimas** | — | — | — | — | NATIVE |

### 3.11 `/taisykles/`

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| L1 | Route header + PDF „Line“ button + chips (W) | **Inner head**: Label „Taisyklės“ · H1 „Siuntų siuntimo taisyklės“ · lead (approved) · link column: **Link** with *Icon* download „Atsisiųsti sutartį (PDF, 72 KB)“ + Links „Draudžiami daiktai“ (`?tab=` + tab 4 slug) · „Baudos“ · „Pretenzijos“ | H1, lead, PDF | Ph · 6169133 | words rise | — | NATIVE |
| L2 | #taisykliu-tekstas: sticky lane index with filling stops (N+C) | *Chapter row* P, Row ID `taisykliu-tekstas`: **Tabs** → *Style* **Vertical Sticky Scrolling** · *Sticky Aspect* Tab Links · *Navigation Functionality* All Links Visible · *Navigation Width* Regular · *Navigation Item Spacing* 15px · *Navigation Item Mobile Display* Hidden · *Tab Spacing* 10% · tab link element **H4** · CTA Button = the PDF (Wave 3 fix: Tab Content Animation / Tab Link Animation exist only for *Sticky Aspect* Tab Content) · 6 tabs = the 6 sections verbatim; clauses „2.1 …“ as Text Block paragraphs | all 6 sections verbatim | P | active link fills from outline; content fades | — | NATIVE |
| L3 | 4.2 banned items dark inset, numbered ✕ (N+C) | **Callout** (A) with 2 × Inner Column **Fancy UL ✕** (12 items split 6 + 6) | 12 items | A inset on P | list fades in | — | NATIVE |
| L4 | 4.5 fines (N) | **Milestone** 1200 EUR superscript *Count To Value* + **KV rows** (40\|60 „Radus siuntoje ar krovinyje \| Bauda“) + **Toggle Panels → Animated Circle** „Visas 4.5 punkto tekstas“ | table + verbatim 4.5 | P | count; circle | — | NATIVE |
| L5 | 5. deadline lane 0 → 5 → 14 d. (C) | 3 Columns with **Border Advanced** top 1px + **Enable Border Animation**: **Milestone** 0 / 5 / 14 (*Symbol* „d.“ after, **Motion Blur Slide In**) + caption verbatim | deadlines | P | rules draw, digits slide | — | NATIVE |
| L6 | PDF end card (N+C) | **Callout** (P): H4 „Sutartis su siuntėju“ + **Lift button** „Atsisiųsti (PDF, 72 KB)“ + **Link** „Turinys ↑“ (`#taisykliu-tekstas`) | labels | P | lift | — | NATIVE |
| L7 | GS-Board + GS-Arrival | **GS-Kvietimas** (GS-Board dropped) | — | — | — | — | NATIVE |

### 3.12 `/kontaktai/`, `/privatumo-politika/`, 404

| # | Now (v2) | New — Salient 18.2.1 | Content kept | Tone · Media | Motion / hover / parallax | CSS | Verdict |
|---|---|---|---|---|---|---|---|
| C1 | Plain dark header + stop-list jump links + terminus ring (C) | **Inner head**: Label „Kontaktai“ · H1 „Kontaktai“ · lead „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“ · links Skambinkite · Grafikas · Parašykite | H1, lead | Ph · 7828591 | words rise | — | NATIVE |
| C2 | #skambinkite ticket cards + e-mail copy button (C) | *Chapter row* A, Row ID `skambinkite`, Equal Height, Column Margin 10px: 2 × **Card** (A `#161D21`, *Background Color Hover* `#1A2227`, radius 3, padding 48): **Label** „Pervežimai į Airiją“ + number as **Button → Text Reveal Wave**, *Display Tag* H2, custom font size 3.4vw (min 32px), `tel:` „+370 650 53161“ + **Call (red)** „Skambinti“ + **Link** „Airijoje +353 86 450 3104“ · „JK +44 7566 878681“; Ispanija card the same · Row: **Link** `mailto:` „saugiai.greitai.patikimai@gmail.com“ (copy button dropped) | all 5 numbers, e-mail | A | letters wave on the big numbers; card BG warms | — | NATIVE |
| C3 | #grafikas timetable + „Line“ button (C / W) | *Chapter row* P, Row ID `grafikas`: Column 5/12 **Sticky Content** **Label** + H2 „Artimiausi pervežimai“ + note · Column 7/12 **Tabs** → *Style* **Toggle Button** (2 tabs „Airija“ / „Ispanija“, *Tab Change Animation* Fade) with **GS-Grafikas Airija** / **GS-Grafikas Ispanija** | all dates | P | the 70 × 28 switch knob slides .45 s `(.23,.46,.4,1)`; rows flip | C-5 | NATIVE+CSS |
| C4 | #parasykite form + quick-call highlight JS (N+C) | **Row ID `parasykite`** + **GS-Užklausa** (DS§4.14 labels; highlight JS dropped) | form | A · 36377055 | as G25 | C-6 | NATIVE+CSS |
| C5 | #kur-vaziuojame dark map (C) | *Chapter row* P-alt: ½ **Label** + H2 „Dvi kryptys. Keturios šalys pakeliui.“ + text + **KV rows** + **Link** · ½ **Image With Hotspots** (map image) | texts | P-alt · map image | hotspots | C-7 | NATIVE+CSS |
| V1 | Plain header (N) | **Inner head** without photo (BG `#0F1417`): H1 „Privatumo politika“ (no link column) | H1 | A | words rise | — | NATIVE |
| V2 | Document + reading-progress mini-TOC (C) | *Chapter row* P: Column 3/12 **Sticky Content** 2 × **Link** („Informacija“, „Slapukai (Cookies)“) · Column 9/12 Text Block + **Callout** „Privatumo politikos tekstas bus pateiktas prieš paleidžiant svetainę.“ | texts, notice | P | — | — | NATIVE |
| V3 | Cookie table styled as timetable (N+C) | Complianz `[cmplz-cookies]` in a Text Block | plugin list | P | — | C-9 | NATIVE+CSS |
| E1 | 404 full-height photo row (N) | **Global Section → Location: 404 Content**: **Section** Min Height 100svh, BG 160483 + **Parallax Fade** (Medium), overlay v2 grade, Text Light, flex end | — | Ph · 160483 | background fades | — | NATIVE |
| E2 | „4 0 4“ split-flap tiles + broken rail (C) | **Label** „Klaida 404“ + **Animated Text** H1 *Word Animations: Blur* „Maršrutas nerastas“ + **Road line** + Responsive Text „Šio puslapio nėra – bet mūsų mikroautobusai kursuoja toliau.“ (no giant fit-text numerals) | H1, text | Ph | words blur in | — | NATIVE |
| E3 | 404 buttons „Signal/Line“ (W) | **Button (paper)** „Į pradžią“ + **Button (glass)** „Pervežimų grafikas“ + 2 × **Link** (LT numbers) | labels | Ph | arrow circle; glass fill | — | NATIVE |
| E4 | GS-ServiceList (N) | **GS-Paslaugos** in an A row under the hero | list | A | flip | — | NATIVE |

### 3.13 Predicted verdicts after the change

Counted from the tables above (every row that stays on a page; DROPPED rows and the demo-only overlay excluded; the 11 service pages count once as the template, specials separately — the audit's method).

| Page | Blocks | NATIVE | NATIVE+CSS | CUSTOM | Dropped | Audit before (N / N+C / C / W) |
|---|---:|---:|---:|---:|---:|---|
| Shared | 28 | 22 | 5 | 1 | 3 | 19 / 50 / 31 / 0 % |
| Home | 9 | 6 | 3 | 0 | — (v2 blocks merged) | 25 / 38 / 31 / 6 % |
| /apie-imone/ | 8 | 8 | 0 | 0 | 3 | 33 / 33 / 11 / 22 % |
| /pervezimo-paslaugos/ | 6 | 6 | 0 | 0 | — | 17 / 33 / 33 / 17 % |
| /tarptautiniai-pervezimai/ | 10 | 7 | 3 | 0 | 1 | 23 / 38 / 31 / 8 % |
| Service template (×11) | 13 | 11 | 2 | 0 | — | 18 / 82 / 0 / 0 % |
| Per-service specials | 15 | 14 | 1 | 0 | — | 21 / 43 / 21 / 14 % |
| /pervezimu-grafikas/ | 6 | 4 | 2 | 0 | 1 | 17 / 0 / 67 / 17 % |
| /siuntos-sekimas/ | 4 | 3 | 1 | 0 | 1 | 25 / 25 / 50 / 0 % |
| /taisykles/ | 7 | 7 | 0 | 0 | — | 17 / 50 / 17 / 17 % |
| /kontaktai/ + /privatumo-politika/ + 404 | 12 | 8 | 4 | 0 | — | 0–50 / 0–33 / 25–80 / 0–25 % |
| **Total** | **118** | **96 (81 %)** | **21 (18 %)** | **1 (1 %)** | **9** | **22 / 41 / 29 / 8 %** |

**Predicted: 99 % native (NATIVE + NATIVE+CSS), up from 63 %.** The only CUSTOM item is G27 (reduced motion + the WCAG 2.2.2 motion pause), which the project rules require and 18.2.1 lacks. Budget for build-time surprises (an option that renders differently from its label): plan on **≥ 95 %**. Every NATIVE+CSS row points to one numbered group of `sgp-custom.css` (§4); none of them changes an element's structure.

---

## 4. The custom layer and its budget (production: *Theme Options → General Settings → CSS/Script Related*)

### 4.1 What counts as custom (demo file → production)

| Layer | Demo file(s) | Production equivalent | Counts toward the budget? |
|---|---|---|---|
| Theme Options | `assets/css/theme-options.css` | Theme Options fields (§2) | no |
| **Salient emulation** | `assets/css/emul/*.css`, `assets/js/emul.js` | Salient 18.2.1 + Salient Core + Salient WPBakery (element options) | no — it disappears in WordPress |
| **Custom** | **`assets/css/sgp-custom.css`**, **`assets/js/sgp-custom.js`** | *Custom CSS Code* / *Custom JS (Head)*, pasted verbatim | **yes: ≤ 250 non-blank lines CSS (comments included), ≤ 30 lines JS** |
| Page CSS | `assets/css/pages/*.css` | nothing — Salient has no per-page CSS in this build | yes: anything a page really needs moves into a numbered `sgp-custom.css` group; page files stay **empty or ≤ 15 lines of demo-only spacing** |
| Demo-only | `assets/css/demo.css`, `assets/js/demo.js` | nothing („Salient žymės“ overlay, demo form stubs, `?kodas=SGP-DEMO` result) | no, never shipped |

Rule of thumb for every team: *if you cannot name the Salient element option that produces it, it either goes into a numbered group below (and costs lines) or it does not ship.*

### 4.2 `sgp-custom.css` groups (planned ≈ 215 lines)

| Group | Purpose (intent) | Production selectors | ≈ lines |
|---|---|---|---:|
| **C-1 Tokens** | the few `:root` values the rules below use (red, red-lit, red-ink, asphalt-800, hairlines, `--sgp-e-out`) — everything else comes from Theme Options | `:root` | 10 |
| **C-2 Reduced motion** | under `prefers-reduced-motion: reduce`: columns/images/Animated Text shown in their end state; Mask Reveal and Clip Path Inset → `clip-path:none`; parallax and Parallax Fade layers `transform:none`; Scrolling Text loop stopped (first repeat static); Content Trail hidden; Milestones show the final number; `::view-transition-*{animation:none}`; toggle/tab/HLI transitions ≤ .01 s; pinned/stacked sections lose scale/blur (scroll stays user-driven) | `.wpb_column[data-animation]`, `.img-with-aniamtion-wrap`, `.nectar-split-heading`, `[data-bg-animation]`, `.row-bg-wrap`, `.nectar-scrolling-text`, `.nectar-content-trail`, `.nectar-milestone`, `.nectar-sticky-media-sections`, `::view-transition-group(*)` | 45 |
| **C-3 Lithuanian typography** | `hyphens:manual`; `text-wrap:balance` on H1–H4; Animated Text line boxes never clip Į Š Ž (padding-top .08em + matching negative margin); `.sgp-num{font-variant-numeric:tabular-nums}` helper (Extra Class) | `html`, `h1–h4`, `.nectar-split-heading .inner`, `.sgp-num` | 12 |
| **C-4 Mobile call bar** | pins the Row to the bottom of the window below 1000 px (a Sticky Row cannot pin inside a Global Section — its sticky box is only as tall as the bar), `env(safe-area-inset-bottom)` padding, a spacer after the footer so the bar never hides the © line, stacking above the cookie card | `.sgp-callbar` (Row Extra Class), `#footer-outer` | 12 |
| **C-5 Schedule rows** | tabular dates/phones, phone column right-aligned, spacing of the „Iš Lietuvos / Į Lietuvą“ labels, hairline colour on the asphalt variant | `.sgp-grafikas .nectar-hor-list-item` | 10 |
| **C-6 Fluent Forms → Salient *Minimal* forms** | bottom-border fields (1 px, `#C3CBCB` / `rgba(242,244,243,.26)` on A), 17 px text (no iOS zoom), focus = 2 px red line, errors `#C4301E` (P) / `#F4604F` (A), select arrow, consent text size, submit uses the Nectar Button look and is full width on phones | `.fluentform .ff-el-form-control`, `.ff-el-input--label`, `.ff-btn-submit`, `.ff-el-is-error`, `.sgp-dark .fluentform` | 40 |
| **C-7 Image With Hotspots** | markers with radius 3 (crisp, not round; 24 px on phones), numbers in the Label font, the native pulse (`.nectar_hotspot:before`) limited to 2 cycles, tooltip `#0F1417` / snow text / radius 3 (also the native full-screen phone sheet) | `.nectar_image_with_hotspots .nectar_hotspot(::before)`, `.nttip` | 18 |
| **C-8 Page Submenu** | active item: 2 px red underline (Salient's scrollspy sets the class but draws nothing), bottom hairline on the dark bar — the links are a plain `<ul>` (page_submenu.php) | `.page-submenu li a::after`, `.page-submenu li.current-menu-item a::after` | 10 |
| **C-9 Consent plugin** | Complianz card in tokens: `#161D21`, radius 3, Label-font title, red accept with `#0F1417` text, See-Through deny, cookie table rows | `.cmplz-cookiebanner`, `#cmplz-cookies-overview` | 24 |
| **C-10 Header call button** | keeps the „Skambinti“ text `#0F1417` in the transparent, solid and mobile-persisted states; 44 px tap height on phones; GS-Telefonai dropdown padding | `#header-outer li[class*="menu-item-btn-style-button_accent"] > a`, `#header-outer .nectar-global-section-megamenu` (`li > .nectar-global-section-megamenu`, nav-menus.php) | 10 |
| **C-11 Focus visible** | 2 px outline, offset 3 px — `#EF4539` on asphalt, `#0F1417` on paper — for links, buttons, column links, HLI links, toggles, tabs, hotspots | `:focus-visible` scoped by `.sgp-dark` / default | 8 |
| **C-12 Ticker link** | underline + focus ring inside GS-Išvykimai's column link; the text chunks pause on hover/focus | `.sgp-ticker` (Row Extra Class) `.column-link`, `.sgp-ticker:hover .nectar-scrolling-text-inner > *` | 6 |
| **C-13 Motion pause state** | `html.sgp-paused`: Scrolling Text chunks `animation-play-state:paused`, Content Trail hidden, hotspot pulse stopped, Zoom Out Slowly frozen | `html.sgp-paused .nectar-scrolling-text-inner > *` … | 6 |
| **C-14 Pause button** | the pause Button (Extra Class `sgp-motion-toggle` lands on `div.nectar-cta`; the focusable element is its `a.link_text[role=button]`) — in GS-Poraštė on every page + the video heroes; 44 px target, icon swap by `aria-pressed`, label stays „Sustabdyti judesį“ | `.sgp-motion-toggle .link_text` | 10 |
| **C-15 Hero labels on phones** | ≤ 690 px a flat `rgba(11,14,16,.38)` scrim over the first row's overlay, so 12 px labels over hero photos reach 4.5 : 1 | `main > :first-child > .row-bg-wrap .row-bg-overlay::after`, `… > .video-color-overlay::after` | 4 |
| **C-16 Horizontal List Item helper** | secondary text typed as `<p class="muted">` in a column: opacity .7 | `.nectar-hor-list-item .muted` | 2 |
| **Total** | | | **≈ 215** |

### 4.3 `sgp-custom.js` (planned ≈ 22 lines; *Custom JS (Head)*)
- **J-1 Reduced motion (≈ 8 lines):** if `matchMedia('(prefers-reduced-motion: reduce)')` matches, add `html.sgp-rm` and stop Lenis before the theme initialises it (switch the smooth-scroll flag in `window.nectarOptions` via a setter; **verify on staging** — the demo does the same against its emulated `nectarOptions`).
- **J-2 Motion pause, WCAG 2.2.2 (≈ 14 lines):** every `.sgp-motion-toggle` button toggles `html.sgp-paused`, pauses/plays the Row/Section background videos and sets `aria-pressed` + its label („Sustabdyti judesį“ / „Paleisti judesį“); starts paused under reduced motion.
- Nothing else: `?domina=` pre-select is Fluent Forms' own `{get.domina}`; tracking redirects are Fluent Forms confirmations.

**Not in the custom layer (and why):** no rail, board, ticket, map, mono or graticule CSS (the blocks are gone); no header / menu / off-canvas / toggles / tabs / sticky-section / button / fancy-box styling (Salient draws them — in the demo that code lives in `emul/` and is not counted); no per-page CSS in production.

---

## 5. Implementation: six build teams (static demo)

### 5.0 Rules for every team
1. **Reproduce Salient, don't reinvent.** Every block is markup for the *Salient emulation kit* (§5.2): our own CSS/JS that copies Salient's **visible behaviour and numbers** (P§3, §2.6), never its code. Never copy a theme file or a verbatim chunk into the repo; read values, reproduce behaviour.
2. **One section = one Salient Row or Section**, built from the elements in §3 only. No Raw-HTML constructs, no decorative inline SVG (static image files are fine), no rails, rings, tickets, crop marks, split-flap, lane charts, hover videos, popovers, custom indexes. If a block is not in §3, it does not ship.
3. **`data-salient` on every Section/Row, Inner Row, Global Section root and element**, rewritten to the §3 *New* column with the exact 18.2.1 admin names. Format: `Element → Option: value · Option: value` (e.g. `Sticky Content Sections → Type: Horizontal Scrolling · Section Width: 45 · Subtract Navigation Height: ✓`); Global Sections start with `Global Section „GS-…“ → Location: …`. The „Salient žymės“ overlay reads it; `tools/check.py` validates it (§5.4).
4. **Content is verbatim** (DS§6 copy + approved fixes). NEW strings introduced by this plan: „Norite užsakyti? Paskambinkite arba parašykite.“, „Kelionė keltu“, „Kelionė per Europą“, „Klaida 404“ label, „Sustabdyti judesį“ / „Paleisti judesį“, chapter label texts, shortened menu labels „Paslaugos“ / „Grafikas“ — shared appends them to the NEW list in `docs/turinio-pataisos.md` at the end of Wave 3.
5. **Media** only from `docs/media.json` with the ids in §3 (Pexels `url_base + ?auto=compress&cs=tinysrgb&w=…`, `srcset`, `loading="lazy"` below the fold, `alt` = `alt_lt`, decorative = `alt=""`). Background videos only through `{{bgvideo:…}}` (desktop, `preload="none"` until near the viewport, poster on phones and under reduced motion); on-demand clips only through the Video Lightbox component.
6. **Quality floor:** premium at 1440 and 390; zero horizontal overflow; one H1 per page; nothing under 12 px; 16 px body on phones; visible `:focus-visible`; tap targets ≥ 44 px; every `tel:` link has an `aria-label` with the number; `prefers-reduced-motion` respected; no console errors; Lithuanian diacritics never clipped. Allowed CDNs: `cdn.jsdelivr.net/npm` (pinned: `lenis@1.1.13`, `flickity@2.3.0`) and Google Fonts. **No GSAP.**
7. **Breakpoints** 1000 / 691 only; check every page at 1440×900, 1024×768 and 390×844.
8. **Disjoint files.** Touch only your files. Need a kit change? Write the request (component, attribute, expected behaviour) into your hand-off note; shared implements it. Page teams own **no JS**; page CSS stays empty or ≤ 15 lines (§4.1).

### 5.1 File architecture (new)

| Path | Owner | Contents |
|---|---|---|
| `src/partials/head.html` | shared | font link from §2.8, preconnects, CSS order: `theme-options.css` → `emul/*.css` → `sgp-custom.css` → page CSS → `demo.css` |
| `assets/css/theme-options.css` | shared | §2.7 verbatim (Theme Options stand-in) |
| `assets/css/emul/base.css` | shared | reset, body/headings from the Typography slots, links (*Basic Underline*, *Left to Right Fancy*), `.screen-reader-text`, skip link |
| `assets/css/emul/grid.css` | shared | Section / Row / Inner Row / Column / Inner Column, container 1430 − 2 × 55 = 1320 + 55/20 px, 12-column grid, device visibility, Equal Height, Column Margin, flexbox layout, sticky columns, row BG layers + overlays, Column Link |
| `assets/css/emul/header.css` | shared | header (transparent → solid + blur, resize), menu underline, mega menu + dropdowns, „Skambinti“ button style, GS locations (nav-top-before-scroll, footer), mobile header, off-canvas **Fullscreen Cover Split** |
| `assets/css/emul/typography.css` | shared | Animated Text, Highlighted Text, Scrolling Text, Badge (Default + Minimal Line), Responsive Text, Price Typography, Divider |
| `assets/css/emul/buttons.css` | shared | Button (`nectar_cta`) types used here, Legacy Button Regular + lift, Next Section Button, Video Lightbox trigger |
| `assets/css/emul/lists-cards.css` | shared | Horizontal List Item, Icon List, Fancy Unordered List, Fancy Box (Image Above Text, Description on Hover), Milestone, Icon (Linea-style draw), Image with Animation + hovers, Cascading Images, Image With Hotspots, Image Gallery skin, Content Trail |
| `assets/css/emul/interactive.css` | shared | Toggle Panels (Animated Circle, Minimal Shadow), Tabs (Minimal, Toggle Button, Vertical Sticky Scrolling), Page Submenu, Sticky Content Sections (4 types), forms (*Form Styling: Minimal*) |
| `assets/css/emul/motion.css` | shared | entrance start states, Mask Reveal, BG layer animations, Clip Path Inset, Color Change Section, View Transitions (`@view-transition { navigation: auto }` + Vertical Reveal keyframes) |
| `assets/js/emul.js` | shared | all element behaviour (§5.2), Lenis init (`lerp` .153, desktop non-Safari, non-touch), `window.nectarOptions` stand-in; built in modules inside one IIFE, each ≤ 350 lines per edit |
| `assets/css/sgp-custom.css` / `assets/js/sgp-custom.js` | shared | the production custom layer (§4), header comment with the live line count |
| `assets/css/demo.css` / `assets/js/demo.js` | shared | „Salient žymės“ overlay (toggle kept), demo form stubs, `?kodas=SGP-DEMO` result, demo notices |
| `assets/css/pages/*.css` | page teams | empty or ≤ 15 lines of demo-only spacing |
| `assets/img/marsrutai.svg` | shared | static route map (see Wave 1) |
| `assets/img/paslaugos/*.svg` | service-template | static illustrations (X4, X13) |
| `src/partials/*`, `src/data/grafikas.json`, `tools/*` | shared | chrome + Global Section partials, schedule data, build/check |
| `src/pages/*.html` | page teams | pages (front matter `kit: salient`) |
| `src/templates/paslauga.html`, `paslauga.py`, `src/data/paslaugos.json` | service-template | 11 service pages |
| **Deleted in Wave 3** | shared | `tokens.css`, `base.css`, `components.css`, `motion.css`, `sgp.js`, all `assets/js/pages/*.js`, partials `board*.html`, `map-*.html`, `phero-calls.html`, `arrival.html`, `sprite.html` |

`tools/build.py`: pages with `kit: salient` get `SHARED_CSS = theme-options, emul/base, emul/grid, emul/header, emul/typography, emul/buttons, emul/lists-cards, emul/interactive, emul/motion, sgp-custom, demo` and `SHARED_JS = emul, sgp-custom, demo` (all `defer`; Lenis from jsDelivr before `emul.js`); pages without it keep the old stack until Wave 3.

### 5.2 Kit API (delivered by „shared“ in Wave 1)

**Conventions.** Class = the Salient base / DOM class of the element. Options = `data-*` attributes named after the admin option (kebab-case) carrying Salient's **saved values** (e.g. `data-style="arrow-circle-animation"`, `data-parallax-speed="medium"`). Per-instance WPBakery *Design Options* (padding, colours, radius, max width) = inline CSS variables. `data-salient` is separate and human-readable (§5.0). All behaviour is in `emul.js`, keyed on these attributes; nothing page-specific.

**Structure**

| Salient | Markup contract | Behaviour (values) |
|---|---|---|
| Section | `section.vc_section[data-type="full_width_background\|full_width_content\|in_container"][data-min-height="100svh"][data-min-height-phone][data-layout="flex"][data-justify="flex-end"][data-parallax="parallax\|parallax_fade"][data-parallax-speed="fast\|medium_fast\|medium\|slow"][data-text-color="light\|dark"][data-color-change]` > `.row-bg-wrap > .row-bg` (image/video) + `.row-bg-overlay` | parallax factor .20/.28/.40/.60; *Parallax Fade* also fades toward the overlay; off ≤ 999 (Theme Options) |
| Row | `div.wpb_row[data-type][data-text-color][data-bg-animation="fade-in\|zoom-out\|zoom-out-reveal\|slight-zoom-out-reveal\|zoom-out-slow\|clip-path"][data-parallax-speed][data-color-change][data-sticky="bottom"][data-sticky-mobile][data-hide="desktop,tablet,phone"][id]` > `.row-bg-wrap` + `.row_col_wrap_12` · Clip Path: `data-clip-type="scroll\|once" data-clip-applies="bg\|row" data-clip-start="0 6% 0 6%" data-clip-end="0" data-clip-round="3px,0" data-clip-offset="0,50" data-clip-addon="zoom-fade-in"` | BG layer timings §2.6; clip-path interpolated with scroll or played once (1.3 s / 2 s curves); Sticky Row bottom; device visibility |
| Inner Row | `div.vc_row.inner_row[data-backdrop-blur="16"][data-equal-height][data-hide]` + vars `--bg --r --pad --border --max-w` | backdrop-filter blur |
| Column / Inner Column | `div.wpb_column.vc_col-sm-{1..12}[data-t-w="6\|12"]` > `.vc_column-inner` · `data-animation="fade-in\|fade-in-from-bottom\|slight-fade-in-from-bottom\|fade-in-from-left\|fade-in-from-right\|grow-in\|zoom-out\|reveal-from-bottom\|reveal-from-right\|mask-reveal"` + `data-delay` + `data-mask-direction` + `data-mask-shape="straight\|circle"` · `data-animation-type="scroll_pos_advanced" data-scroll-start="ty:60;s:.92;o:1" data-scroll-end="ty:0;s:1;o:1" data-scroll-offset="0,100"` · `data-sticky="top\|middle"` · `data-bg-animation="mask-reveal\|ro-reveal-from-bottom\|zoom-out-slow"` · `data-bg-parallax="minimum\|very_subtle\|subtle\|regular\|medium\|high"` · `data-overlay-opacity=".72" data-overlay-opacity-hover=".42"` · `data-border-animation` · `data-backdrop-blur` · vars `--bg --bg-hover --r --pad --border` · last child `a.column-link[href][aria-label]` | entrance at 88 % (reveal 70 %), 1300 ms `(.19,1,.22,1)` + opacity 500 ms; mask 1.3 s; scroll-advanced interpolation; CSS sticky below the header; BG hover .45 s; overlay opacity hover |
| Global Section | `div.nectar-global-section[data-gs="GS-…"][data-location="nav-top-before-scroll\|footer\|after-content\|off-canvas-meta\|mega-menu\|404\|inline"]` | `nav-top-before-scroll` is hidden once `scrollY > 0` (with the header's transition) |

**Header partial contract** (`src/partials/header.html`, shared only): `#header-outer[data-format="default"][data-transparent-header="true"][data-lhe="animated_underline"][data-header-resize="1"][data-hhun="0"][data-full-width="true"]` > `#top` (logo, `nav > ul.sf-menu > li.menu-item`), mega menu items `li.megamenu[data-gs]`, call item `li.menu-item-btn-style-button_accent-color[data-persist-mobile]`, mobile toggle `.slide-out-widget-area-toggle[data-icon-style="circular"]`; off-canvas `#slide-out-widget-area.fullscreen-split` > `.left-side` (menu) + `.right-side` (GS-Telefonai). JS: `.transparent` at top → solid + blur after 1 px of scroll; `.small-nav` resize; mega menu open on hover/focus (Fade In Up); off-canvas open/close with focus trap, `Esc`, and the §2.6 stagger.

**Elements**

| Salient element | Markup contract | Behaviour (values) |
|---|---|---|
| Animated Text | `.nectar-split-heading[data-text-effect="default\|blur-bottom\|fade-bottom\|letter-reveal-bottom\|letter-reveal-blur-top\|scroll-opacity-reveal\|none"][data-stagger][data-m-rm-animation]` > `h1…h6\|p` (lines split on `<br>`), font sizing vars `--fs --fs-t --fs-m --fs-min --fs-max --lh` | split into words/letters in JS (text stays one accessible string); 1.2 s `(.25,1,.5,1)`, stagger clamps §2.6; scroll-opacity .2 → 1 |
| Highlighted Text | `.nectar-highlighted-text[data-style="regular_underline\|half_text\|full_text\|text_outline\|scribble"][data-color][data-underline-thickness="3px"]` with `<em>` phrases | `background-size` 0 → 100 % .9 s `(.15,.75,.4,1)` on entry |
| Scrolling Text | `.nectar-scrolling-text[data-s-dir="ltr\|rtl"][data-s-speed="slower\|slowest\|slow\|medium\|fast\|static"][data-repeat="3"][data-divider="✦"][data-divider-size="half\|full"][data-mask-edges][data-move-on-scroll][data-outline="thin"][data-spin-divider]` > heading text | loop 45 / 30 / 14 / 7 / 4 s (`slower` = Slowest 45 s, `slowest` = Slower 30 s — Salient's own swap); pauses under `html.sgp-paused`, static under reduced motion |
| Badge | `.nectar-badge[data-badge-style="default\|line"][data-typography="label\|body\|h6"][data-display="inline\|block"][data-padding="small\|medium\|large\|none"][data-backdrop-blur]` + vars `--bg --fg --border --line-w --r` | Minimal Line = 1 px line (`--line-w`, default 28 px) + 10 px gap before the text |
| Responsive Text · Price Typography | `.nectar-responsive-text[data-inherit="h1…h6\|p"]` · `.nectar-price-typography > .before-text + .price + .after-text` | font sizing vars |
| Divider | `.divider-wrap[data-line-type="no-line\|full-width\|small\|vertical"][data-animate][data-alignment]` + vars `--line-w --thickness --line-color --h` | *Animate Line*: `scaleX(0 → 1)` on entry (1.3 s entrance curve) |
| Button | `a.nectar-cta[data-style="arrow-circle-animation\|basic\|see-through\|underline\|text-reveal-wave\|text-reveal\|next-section"][data-alignment="stretch"][data-display="inline\|block"][data-backdrop-blur]` > `span.link_text > span.text` + vars `--btn-bg --btn-bg-h --btn-fg --btn-fg-h --btn-border --btn-border-h --r --fs`; Next Section adds `data-btn-type="minimal-arrow-alt" data-arrow-animation="hover-only"` | arrow circle .55 s `(.12,.75,.4,1)` (circle 50 % → 45 %, arrow exits ↗, twin enters); wave letters 15 ms apart .5 s; underline .4 s; colours .45 s |
| Legacy Button | `a.nectar-button.regular.large[data-color="extra-color-1"]` (+ `.default-arrow` icon) | hover `translateY(-3px)` + `0 20px 38px rgba(0,0,0,.16)` (from `body[data-button-style="slightly_rounded_shadow"]`) |
| Video Lightbox | `a.nectar-video-box[data-link-style="play_button_mouse_follow"][data-mouse-style="see-through-contrast"][data-hover="zoom_bg_image"][href="{{videourl:ID}}"]` > poster `img` | play button follows the cursor inside the box; click opens a `<dialog>` player (focus trap, `Esc`, pauses Lenis) |
| Icon List | `.nectar-icon-list[data-direction="horizontal\|vertical"][data-columns="3"][data-icon-size="medium"][data-icon-style="border\|no-border"][data-icon-color="accent-color"][data-animate]` > `.nectar-icon-list-item[data-icon-type="numerical\|icon"]` (`.list-icon-holder` + `.content > h4 + p`) | items fade/slide in 1 by 1 (120 ms); stacked ≤ 690 |
| Fancy Unordered List | `ul.nectar-fancy-ul[data-list-icon="dot\|dash\|check\|fa-times"][data-animation][data-spacing="10px"][data-link-style="animated-underline"]` + `--icon-color` | items fade in with 90 ms stagger |
| Horizontal List Item | `.nectar-hor-list-item[data-columns="2\|3"][data-column-layout="small_first\|xsmall_first\|medium_last\|large_middle"][data-hover-effect="default\|none\|full_border"][data-color="extra-color-1\|extra-color-2"][data-border-animation]` > `.nectar-list-item` ×n (+ `a.full-link`) | fill flips up .4 s `(.2,0,.15,1)`; bottom line draws on entry; 22 px padding |
| Fancy Box | `.nectar-fancy-box[data-style="image_above_text_underline\|hover_desc"][data-border-radius="none"][data-aspect="3-2"][data-hover-color="extra-color-1"][data-overlay=".55"][data-overlay-hover=".8"][data-bg-animation="short_zoom\|long_zoom"]` | image 1.1 .75 s + underline / card −10 px + shadow .65 s, text +20 px → 0 (delay .15 s) |
| Milestone | `.nectar-milestone[data-effect="count\|motion_blur\|none"][data-symbol="EUR"][data-symbol-pos="after"][data-symbol-alignment="superscript\|default"][data-delay="150"][data-inherit="h2"]` > `.number` | trigger 98 %; count 2.2 s easeOutCubic; motion blur digits 200 ms apart, .65 s |
| Image | `.img-with-aniamtion-wrap` > `img.img-with-animation[data-animation="fade-in-from-bottom\|grow-in\|ro-reveal-from-bottom\|slide-up\|none"][data-delay][data-hover-animation="zoom-in\|zoom-in-crop\|color-overlay\|none"]` (Salient's own class spelling) + `--r` | reveal-rotate 2.3 s; zoom .65 s `(.05,.2,.1,1)` |
| Cascading Images | `.nectar_cascading_images[data-aspect="4-5"]` > `.cascading-image[data-animation="grow-in-reveal\|fade-in-from-bottom"][data-parallax="subtle\|medium\|high"]` + vars `--x --y --max-w --shadow` | layers enter 200 ms apart; per-layer scroll parallax |
| Image With Hotspots | `.nectar_image_with_hotspots[data-hotspot-icon="numerical\|plus_sign"][data-tooltip-func="hover\|click\|always"][data-color="accent-color"][data-animation]` > `img` + `.nectar_hotspot_wrap[style="left:%;top:%"]` > `button.nectar_hotspot` + `.nttip[role=tooltip]` | markers pop in staggered, pulse (2 cycles, C-7), tooltip on hover **and** focus, `Esc` closes |
| Image Gallery (Flickity) | `.nectar-flickity[data-controls="touch_total"][data-image-parallax][data-mask-edges][data-drag-scale][data-columns="2,1,1"]` (vendor `flickity@2.3.0`) | touch indicator + total, parallax inside frames, scale while dragging |
| Content Trail | `.nectar-content-trail[data-type="text"][data-items="Airija\|Ispanija\|…"][data-colors="#EF4539/#0F1417,…"][data-frequency="85"][data-duration="1.2"][data-in="scale"][data-out="scale"][data-randomize]` | spawns a tag every 85 px of pointer travel, 1.2 s life; off on touch and reduced motion |
| Icon | `.nectar_icon_wrap[data-style="border-animation\|soft-bg\|default"][data-draw]` > own inline line icon (`{{icon:name}}`) | line draws on entry (Vivus-like stroke-dashoffset), border fills on hover |
| Toggle Panels | `.toggles[data-style="animated_circle\|minimal_shadow"][data-accordion][data-first-open][data-circle-position="right"][data-circle-size="40"][data-divider][data-radius="3px"]` > `.toggle` > `h3 > button[aria-expanded]` + `.inner-toggle-wrap[role=region]` | circle draws + panel opens .85 s `(.76,0,.24,1)`; deep link `?toggle=N`; multi-open when `data-accordion` absent |
| Tabs | `.tabbed[data-style="minimal\|toggle_button\|vertical_scrolling"][data-animation="fade"]` > `ul.wpb_tabs_nav[role=tablist] > li > a[role=tab]` + `.wpb_tab[role=tabpanel][id]` · vertical: `data-sticky-aspect="default" data-content-animation="fade" data-link-animation="opacity\|underline\|outline_fill" data-nav-width="30" data-nav-side="left"` | underline 4 px .3 s; ←/→ keys; deep link `?tab=<slug>`; vertical: active link by scroll position, sections stacked on phones |
| Page Submenu | `.page-submenu[data-sticky][data-alignment="left\|center"]` + vars `--bg --link` > `ul.page-submenu-links > li > a[href="#id"]` | sticks under the header (.3 s); scrollspy sets `.current-menu-item` |
| Sticky Content Sections | `.nectar-sticky-media-sections[data-type="default\|scroll-pinned-sections\|horizontal-scrolling\|layered-card-reveal"][data-subtract-nav][data-radius="3"][data-enabled="desktop,tablet"][data-section-height="85vh"]` · default: `data-content-position="right" data-media-width="45" data-media-height="80vh" data-content-spacing="30vh"` · pinned: `data-effect="none\|overlapping\|scale\|scale_blur\|fade_scale" data-stacked data-nav data-overlap="50"` · horizontal: `data-effect="none\|stacking" data-section-width="45" data-gap="8"` > `.nectar-sticky-media-section[data-section-type="image\|video\|color"][id][data-link][data-indicator-text]` + vars `--bg` | rAF scroll timelines: previous card 1 → .92, blur 0 → 5 px, −54 px stacked; horizontal track = vertical scroll while pinned; *Link Mouse Indicator* follows the pointer; everything stacks where `data-enabled` excludes the device and under reduced motion |
| Forms (*Form Styling: Minimal*) | plain `form` + `label` (Label typography) + inputs; demo forms never submit (`demo.js` shows the confirmation text) | bottom-border fields, focus red line, submit = Nectar Button with lift |

**Utilities** (only these): Extra Classes that production also uses — `sgp-dark`, `sgp-num`, `sgp-callbar`, `sgp-grafikas`, `sgp-ticker`, `sgp-motion-toggle`, theme class `nectar-inherit-label`, `screen-reader-text`; `data-text-align="left\|center\|right"`; Design-Options variables `--pt --pr --pb --pl` (+ `-t`/`-m` suffixes for tablet/phone), `--mt --mb`, `--bg`, `--fg`, `--r`, `--max-w`, `--gap`, `--min-h`. No other helper classes.

**Build placeholders** (`tools/build.py`, shared)

| Placeholder | Output |
|---|---|
| `{{partial:name\|k=v…}}` | partial with parameters (`{{param:k}}` inside) — GS partials: `gs-isvykimai`, `gs-artimiausi`, `gs-telefonai`, `gs-paslaugu-meniu`, `gs-grafikas-ie`, `gs-grafikas-es`, `gs-marsrutai` (`cols=2\|3`, `tone=A\|P`), `gs-paslaugos` (`tone`), `gs-pasitikejimas`, `gs-kvietimas`, `gs-uzklausa` (`media=ID`), `gs-skambuciu-juosta`, `gs-poraste`, `gs-404` |
| `{{grafikas:ticker}}` · `{{grafikas:next\|dir=ie\|es}}` · `{{grafikas:rows\|routes=…\|tone=A\|P}}` · `{{grafikas:updated}}` | Scrolling Text content · next-date text for GS-Artimiausi · HLI rows for GS-Grafikas · „Atnaujinta rugsėjo 23 d.“ — full Lithuanian dates, no relative words, no client-side recompute, no `window.SGP_SCHEDULE` |
| `{{paslaugos:menu}}` · `{{paslaugos:rows\|tone=…}}` · `{{paslaugos:hscroll}}` · `{{paslaugos:pinned}}` · `{{paslaugos:related\|slug=…}}` · `{{paslaugos:footer}}` | mega-menu columns · GS-Paslaugos HLI rows · home H3 sections · P3 pinned groups · S11 Fancy Boxes · footer list |
| `{{img:ID\|…}}` (unchanged) · `{{bgimg:ID\|w=\|pos=\|phone=ID\|phone-pos=}}` · `{{bgvideo:ID\|poster=ID}}` · `{{videourl:ID}}` · `{{poster:ID}}` · `{{alt:ID}}` | responsive image · `.row-bg` image layer with phone source · desktop-only BG video (`muted playsinline loop preload="none"`, poster on phones/reduced motion, `data-bg-video`) · lightbox MP4 (one HD file, no SD/HD switch) · poster · alt |
| `{{icon:name}}` | own inline line icons (phone, arrow-up-right, arrow-down, download, play, pause, times, dash + the H5/X6 comfort/price glyphs); replaces `sprite.html` |
| `{{svc:field}}` | service template fields (unchanged) |
| Front matter | `kit: salient` (required on rebuilt pages; `js:` is then a build error), `css:` (optional page CSS), `vendor: flickity`, `hero_media`, `salient:` (page summary with exact 18.2.1 names) |
| Removed | `{{grafikas:board\|stub\|next-strip\|lane\|timetable\|data}}`, `{{partial:board*\|map-*\|phero-calls\|arrival\|sprite}}`, `sd-only` / SD-HD flags |

**Kit page** `src/pages/kit.html` → `/kit/` (noindex, not linked, not one of the 21 pages): every component above in A and P tones with its `data-salient` label — the living style tile the page teams copy from.

### 5.3 Team checklists

**Waves.** Wave 1 = shared delivers the kit (§5.2) + `/kit/` + chrome + Global Section partials. Wave 2 = the five page teams rebuild their pages in parallel against the kit (front matter `kit: salient`). Wave 3 = shared deletes the old stack, runs acceptance (§5.4) and the re-count.

**Team „shared“** — owns `src/partials/*`, `tools/*`, `src/data/grafikas.json`, `assets/css/theme-options.css`, `assets/css/emul/*`, `assets/js/emul.js`, `assets/css/sgp-custom.css`, `assets/js/sgp-custom.js`, `assets/css/demo.css`, `assets/js/demo.js`, `assets/img/marsrutai.svg`, `src/pages/kit.html`, `docs/turinio-pataisos.md` (NEW list only). **Wave 1 (blocking), then Wave 3.**
- [ ] `theme-options.css` = §2.7 verbatim; `head.html` font link + CSS order (§5.1).
- [ ] `emul/*.css` + `emul.js`: every row of §5.2 (structure, header contract, 25 element contracts), real values from §2.6, reduced-motion end states, keyboard access (toggles, tabs, hotspots, lightbox, off-canvas, mega menu). Write in chunks (≤ 350 lines / 18 KB per edit).
- [ ] Header partial: GS-Išvykimai ticker + Default Layout header (transparent → `#0F1417` 90 % + blur, resize 84 → 70) + mega menus (GS-Paslaugų meniu, GS-Telefonai) + „Skambinti“ (persists on phones) + Fullscreen Cover Split off-canvas with GS-Telefonai on the right.
- [ ] GS partials (14, §5.2 list) and the footer (no wordmark, no gradient); call bar with the safe-area rule; Complianz-style cookie card in tokens.
- [ ] `sgp-custom.css` groups C-1…C-14 exactly as §4.2 (header comment: line count), `sgp-custom.js` J-1 + J-2 (≤ 30 lines); `demo.css/js`: „Salient žymės“ overlay with its toggle, demo form confirmations, `?kodas=SGP-DEMO` callout.
- [ ] `assets/img/marsrutai.svg`: static schematic in the v2 look on paper (ink `#1C1D1D` 3 px trunk LT → PL → DE → BE → FR → ES, IE leg `#4A5358` dashed with „maršrutas tikslinamas“, city dots, Barlow labels ≥ 15 px in a 1100-wide viewBox; **no graticule, crop marks, degree marks or animation**); hotspot coordinates listed in a comment for the page teams.
- [ ] `build.py`: placeholders and front matter of §5.2; `kit: salient` stack switch; remove the old schedule variants. `check.py`: rules of §5.4.
- [ ] `/kit/` page with every component in both tones.
- [ ] Wave 3: delete the old stack (§5.1 list), run `build.py` + `check.py`, screenshots of all 21 pages at 1440/390 (+1024), re-count §3.13, append NEW strings to `turinio-pataisos.md`.

**Team „home“** — owns `src/pages/index.html`, `assets/css/pages/home.css`.
- [ ] H1–H9 exactly as §3.2, v2 anchors kept; H1 video Section with Parallax Fade, Animated Text H1 (3 lines), road line, glass band with `{{partial:gs-artimiausi}}`, 2 red calls, pause button, Next Section button.
- [ ] H2 Highlighted Text statement + Cascading Images (7541981, 6169133) + KV rows + 4 Motion Blur milestones („3“ + symbol „–4“).
- [ ] H3 `{{paslaugos:hscroll}}` inside Sticky Content Sections → Horizontal Scrolling (45 %, link mouse indicator, stacked on phones).
- [ ] H4 outline Scrolling Text (Move on Scroll, Spin divider) + Image With Hotspots on the map + `{{partial:gs-marsrutai|cols=3|tone=P}}`.
- [ ] H5 video row with Clip Path Inset (Scroll Position) + Regular parallax + Scroll-Position-Opacity H2 + comfort Icon List + Video Lightbox 3987777.
- [ ] H6 Stations + KV + Scroll Position Advanced photo; H7 Animated Circle toggles (verbatim rules); H8 tracking card + Mask Reveal photo; H9 omitted.
- [ ] Color Change Section on H2–H8; no page JS; `home.css` empty or ≤ 15 lines; every `data-salient` rewritten; front matter `salient:` updated.

**Team „about-contact“** — owns `src/pages/apie-imone.html`, `kontaktai.html`, `privatumo-politika.html`, `404.html` and their `assets/css/pages/*.css`.
- [ ] Apie A1–A11 (§3.4): inner head (§3.3) on 9989463, Clip-Path photo band A2 (38404178), Highlighted Text + KV datasheet A3, milestones A6 on A, **Pinned Sections → Scale + Stacked** A7 (5 colour sections, rotate-reveal images), Flickity gallery A8, `{{partial:gs-pasitikejimas}}`, `{{partial:gs-kvietimas}}`.
- [ ] Kontaktai C1–C5 (§3.12): two dark call cards with Text Reveal Wave numbers + red calls, `mailto:` link (no copy button), **Tabs → Toggle Button** with GS-Grafikas IE / ES, `{{partial:gs-uzklausa|media=36377055}}`, hotspot map; no GS-Kvietimas.
- [ ] Privatumo politika V1–V3; 404 E1–E4 (no giant numerals; `{{partial:gs-paslaugos|tone=A}}`).
- [ ] Delete `apie.js`, `kontaktai.js`, `privatumo-politika.js`, `404.js` from the page front matter (files removed by shared in Wave 3); page CSS empty or ≤ 15 lines each.

**Team „services-routes“** — owns `src/pages/pervezimo-paslaugos.html`, `tarptautiniai-pervezimai.html`, `assets/css/pages/paslaugos.css`, `tarptautiniai.css`.
- [ ] Pervežimo paslaugos P1–P6 (§3.5): inner head; 3 Photo cards; `{{paslaugos:pinned}}` in **Pinned Sections → Blurred Scale + Stacked + Section Navigation** (group ids as anchors for the home H3 links); statement + calls; Scroll Position Advanced image P5; `{{partial:gs-marsrutai|cols=2|tone=A}}`, `{{partial:gs-kvietimas}}`.
- [ ] Tarptautiniai T1–T11 (§3.6): video hero 13707149 with glass band + GS-Artimiausi; T2 routes + hotspot map; T4/T5 **Pinned Sections → Overlapping** Airija/Ispanija with glass panels, GS-Grafikas (A), Cascading Images; T6 outline Scrolling Text + Video Lightbox 12421166; T7 GS-Pasitikėjimas; T8 texture row; T9 border-animated cards; T10 GS-Paslaugos.
- [ ] Color Change Section on T2–T10; no page JS; page CSS empty or ≤ 15 lines.

**Team „service-template“** — owns `src/templates/paslauga.html`, `paslauga.py`, `src/data/paslaugos.json`, `assets/css/pages/paslauga.css`, `assets/img/paslaugos/*`.
- [ ] Template S1–S13 (§3.7): photo hero + glass band (GS-Artimiausi, 2 calls); dark **Page Submenu**; Faktai KV + See-Through route chips (`?domina=…#uzklausa`); Apie paslaugą + Stations; **Sticky Media, Scrolling Content** on A; toggles; prohibited texture row with the 1200 EUR superscript Milestone; `{{partial:gs-marsrutai|cols=2|tone=P}}`; Highlighted Text closing; `{{paslaugos:related|slug=…}}`; „Kita paslauga“ Photo card band; `{{partial:gs-uzklausa|media=…}}` with Row ID `uzklausa`.
- [ ] `paslauga.py`: specials X1–X15 (§3.8) — Stations, Video Lightbox, Chips, static illustrations, Minimal Shadow checklist, Linea-style Icon cards, Pinned Scale, hotspots, KV, Callouts; no inline SVG, no storage.
- [ ] `assets/img/paslaugos/daliniai-skyriai.svg`, `pakavimas-5cm.svg`: static v2-look illustrations (ink lines, one red surface, labels ≥ 15 px).
- [ ] `paslaugos.json`: `related` (3 slugs), `next_label`, group ids; drop hover-video fields; keep all copy fields.
- [ ] Remove `paslauga.js` (domina pre-select = Fluent Forms `{get.domina}`; the demo form partial reads `?domina=` in `demo.js`); `paslauga.css` empty or ≤ 15 lines.

**Team „schedule-tracking-rules“** — owns `src/pages/pervezimu-grafikas.html`, `siuntos-sekimas.html`, `taisykles.html`, `assets/css/pages/grafikas.css`, `sekimas.css`, `taisykles.css`.
- [ ] Grafikas R1–R7 (§3.9): inner head; **Tabs → Minimal** Visi / Airija / Ispanija with `{{partial:gs-grafikas-ie|tone=A}}` + ES and the „Atnaujinta …“ label; 2 red calls; facts + hotspot map on P; lane chart removed.
- [ ] Siuntos sekimas K1–K5 (§3.10): callout form + Mask Reveal photo 6407553; demo `?kodas=SGP-DEMO` result via `demo.js` (no page JS); 3 Fancy Boxes → Description on Hover on A.
- [ ] Taisyklės L1–L7 (§3.11): **Tabs → Vertical Sticky Scrolling** (Sticky Aspect Tab Links: Regular nav, 1 px track + indicator, CTA = PDF), banned-items callout (6 + 6), fines Milestone + KV + toggle, 3 border-animated deadline Milestones, PDF callout with Lift button.
- [ ] Remove `grafikas.js`, `sekimas.js`, `taisykles.js` from front matter; page CSS empty or ≤ 15 lines each.

### 5.4 Acceptance (Wave 3, shared runs it)
- `python3 tools/build.py && python3 tools/check.py` pass. New `check.py` rules:
  - every `section.vc_section`, `.wpb_row`, `.inner_row`, GS root and element root has `data-salient`; its element names are in the 18.2.1 whitelist (§1.0 of `salient-18-2-1-parinktys.md`).
  - **banned** in markup / `data-salient`: `Stacking` next to `Pinned`, `Column Animation: Mask Reveal` on an outer column, `Button (Regular`, `(Line)`, `Fancy Box minimal`, `Before Footer`, `Fullscreen Split` (without „Cover“), `Centered Menu`, `sgp_grafikas`, `popover`, `18.3`, `Raw HTML`, `Inter Tight`, `sgp-mono`, `sgp-has-rail`, `sgp-rail`, `sgp-ring`, `sgp-flap`, `sgp-ticket`, `sgp-graticule`, `crop-mark`, `sgp-crop`, `data-sd`, `data-hd`, `po \d+ d\.`.
  - no `border-radius` above 4 px in `emul/`, `sgp-custom.css` or page CSS except `50%` on circles (arrow circle, hotspot pulse, toggle circle) and the native Tabs *Toggle Button* switch track (70 × 28) — enforces „no pill buttons“.
  - `<video autoplay>` only inside `.row-bg` with `muted playsinline`, and only on pages that contain a `.sgp-motion-toggle`.
  - `sgp-custom.css` ≤ 250 non-blank lines, `sgp-custom.js` ≤ 30, each page CSS ≤ 15; no `kit: salient` page references page JS.
  - existing link / id / alt / `tel:` aria-label / one-H1 / title checks stay; text under 12 px fails (grep `font-size:\s*1[01]px|0\.[5-6]\d*rem`).
- Screenshots of all 21 pages at 1440×900 and 390×844 (+ 1024×768) with `scratchpad/shoot.mjs` (unique names), contact sheets via `sheet.py`; reviewed for: dark/paper rhythm, Barlow Condensed / Barlow / mono labels only, 3 px corners, red only as signal, no horizontal overflow, no console errors, reduced-motion run (`--force-prefers-reduced-motion`) shows every block in its end state.
- Re-count §3.13 from the built pages; report native % and the `sgp-custom.css` / `.js` line counts.

---
## 6. Outline of the Lithuanian guide `salient-gidas.html` (produced after the rebuild)

Same form as `augejas/salient-gidas.html` and `elile/salient-gidas.html`: one self-contained HTML page, numbered chapters, for every section a grey „Šaltinis: …“ reference line (Harbor / Architect / Tether / Salient), then **Row / Column / Elementai / Tekstai** blocks with exact 18.2.1 option names in English and explanations in Lithuanian, copy buttons for CSS/JS, media tables with file names. Title: **„Salient įgyvendinimo gidas — SGP pervežimai“**.

1. **SGP v2 tapatybė, pastatyta Salient būdu** — įžanga (kas lieka iš v2: asfalto ir popieriaus skyriai, raudonas signalas, Barlow Condensed + Barlow + IBM Plex Mono etiketės, 3 px kampai, video hero su artimiausiais išvykimais, skambučiai pagal kryptis; kas perimta iš demo: Harbor išvykimų juosta, stiklo juosta, horizontalios kortelės, maršrutų kortelės, CTA su Content Trail; Architect vidiniai puslapiai ir telefono mygtukas; Tether toggles) ir lentelė *Demo | SGP | Kodėl*: spalvos (Harbor #000/#ff4a4b/#ffb500/#8ccbff → #EF4539/#0F1417/#F5F7F6/#C4301E), Inter Tight → Barlow šeima, „pill“ → 3 px, baltas fonas → tamsūs/šviesūs skyriai su Color Change Section, Hide Until Needed → Resize On Scroll, footerio gradientas ir užrašas → ramus tamsus footeris, atsiliepimai paslėpti, lipni skambučių juosta telefone. Atmesta alternatyva: `docs/kryptys/salient-tile-harbor.html`.
2. **Pasiruošimas** — testinė aplinka; Salient 18.2.1 + Salient Core + Salient WPBakery + Salient Demo Importer; Fluent Forms (Harbor demo reikalauja), Complianz, Yoast SEO; importuoti **Harbor** (Demo Content + Theme Options + Widgets); Architect — tik atskiroje testinėje svetainėje, išsaugoti eilutes kaip WPBakery šablonus; demo turinio valymas; vaikinė tema nebūtina (visas kodas Theme Options laukuose).
3. **Theme Options** — 3.1 Logotipas ir ikona (logo.svg, logo_light.svg, aukštis 36/30, favicon) · 3.2 Spalvos (Accent Colors + Overall BG/Font) · 3.3 Tipografija (Barlow Condensed H1–H4, Barlow H5–H6 / Body / Navigation / Nectar Button, IBM Plex Mono „Form and Category Labels“, Off Canvas; Fluid Typography OFF; Custom Responsive Headings %; Load Google Fonts Locally) · 3.4 Bendri nustatymai (Button Styling Slightly Rounded W/ Shadow + Button Roundness 3, Max Website Container Width 1320, Container Left/Right Padding 56 / 20 px, Column/Image Animation Easing easeOutExpo + Timing 1300, Page Builder Element Animations On Mobile Devices Enable, Smooth Scrolling 60, Lightbox fancyBox3, Back To Top OFF, General Link Style Basic Underline + Left to Right Fancy 1 px, Disable Parallax / Video Backgrounds On Mobile ON) · 3.5 Antraštė (§1.1 lentelė) · 3.6 Off Canvas (Fullscreen Cover Split, Circular, Even Lines, spalvos, Meta Area = GS-Telefonai) · 3.7 Page Transitions (View Transitions API → Vertical Reveal) · 3.8 Poraštė (Main Footer Area OFF, Copyright OFF → GS) · 3.9 Form Styling.
4. **Meniu ir Global Sections** — Appearance → Menus (6 punktai + „Skambinti“: Button Accent Color, tekstas #0F1417, fa-phone, Persist In Mobile Navigation Header, Mega Menu x2 Regular Dropdown / Right / GS-Telefonai; „Paslaugos“: Mega Menu 100% / GS-Paslaugų meniu) · lentelė visų 14 Global Sections: pavadinimas, Location arba kur įterpiama, turinys, kas redaguoja (GS-Išvykimai, GS-Artimiausi, GS-Telefonai, GS-Paslaugų meniu, GS-Grafikas Airija, GS-Grafikas Ispanija, GS-Maršrutai, GS-Paslaugos, GS-Pasitikėjimas, GS-Kvietimas, GS-Užklausa, GS-Skambučių juosta, GS-Poraštė, 404 Content).
5. **Pradžios puslapis** — 5.1 Hero (video, stiklo juosta) · 5.2 Apie mus · 5.3 Paslaugos (horizontalios kortelės) · 5.4 Maršrutai (žemėlapis su taškais) · 5.5 Kelionėje (video juosta) · 5.6 Kelionės eiga · 5.7 Prieš siunčiant · 5.8 Siuntos sekimas · 5.9 Atsiliepimai (išjungta eilutė) — kiekvienam: „Šaltinis: …“, Row, Column(s), Elementai su parinktimis, Tekstai, Nuotraukos.
6. **Vidiniai puslapiai** — 6.0 Bendras vidinio puslapio viršus (Architect About struktūra, tamsi v2 nuotaika) · 6.1 Apie įmonę · 6.2 Pervežimo paslaugos · 6.3 Tarptautiniai pervežimai · 6.4 Paslaugos šablonas („SGP – paslauga“, WPBakery Templates) + lentelė 11 paslaugų (URL, hero nuotrauka, specialus blokas, susijusios, kita paslauga) · 6.5 Pervežimų grafikas · 6.6 Siuntos sekimas · 6.7 Taisyklės · 6.8 Kontaktai · 6.9 Privatumo politika · 6.10 404.
7. **Formos (Fluent Forms)** — „SGP užklausa“ (laukai, „Kas Jus domina?“ su `{get.domina}`, patvirtinimo tekstas, el. laiško gavėjai, antispam) · „Siuntos sekimas“ (1 laukas, klaidos tekstas „Neįvestas siuntos kodas!“, Redirect to URL) · sutikimo tekstas · Theme Options Form Styling.
8. **Grafiko atnaujinimas kas mėnesį** — 4 Global Sections, žingsniai su ekrano iškarpomis: pakeisti datas GS-Išvykimai juostoje, GS-Artimiausi (hero juostoje), GS-Grafikas Airija / Ispanija eilutėse, datą „(Atnaujinta …)“; datų rašymo taisyklės („spalio 9 d.“, niekada skaičiais); patikrinti telefone; ≈ 10 min.
9. **Papildomas CSS ir JS** — 9.1 Custom CSS (§4 grupės C-1…C-14, ≈ 215 eil., mygtukas „Kopijuoti“) · 9.2 Custom JS (Head): reduced motion + judesio pauzės mygtukas (≈ 22 eil.) · 9.3 Kas **nėra** kodas (viskas kita — elementų parinktys).
10. **Nuotraukos ir video** — lentelė: vieta → media.json id → failo pavadinimas (`sgp-hero-2560.webp` …) → proporcija ir fokusas; eksporto taisyklės (WebP 1600/2560, ≤ 250 KB, spalvų korekcija), telefono hero versija, maršrutų schema `assets/img/marsrutai.svg` (Image With Hotspots), iliustracijos, video failai fonui (MP4 H.264 1080p, ≤ 8 MB, be garso) ir Video Lightbox'ui (720p).
11. **Seni adresai (301)** — DS§6.12 sąrašas (27 vaikiniai puslapiai → tėviniai, siuntos sekimas, privatumo politika, PDF).
12. **Patikslinti su klientu** — H1 „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“; sutrumpinti meniu pavadinimai; NEW tekstai (§5.0 p. 4); datų metai; Airijos maršruto dalis („maršrutas tikslinamas“); UK numeris; nuosavos nuotraukos; atsiliepimai; privatumo politikos tekstas; slapukų sąrašas; socialiniai tinklai (jų nėra).
13. **Prieš paleidžiant** — noindex išjungti; Safari / iOS / Android patikra (Lenis ten neveikia — tai normalu); reduced motion ir judesio pauzės mygtuko patikra; skambučių juostos, „Skambinti“ mygtuko telefone ir mega meniu patikra; formų laiškai; Complianz; Yoast (breadcrumbs schema, canonical, OG paveikslėlis 1200×630); PageSpeed telefone; 404 Global Section; 301 peradresavimai; `tel:` nuorodos visuose puslapiuose; atsarginė kopija.

