# Build notes · team „about-contact“ (Salient 18.2.1 rebuild, Wave 2)

Direction: „SGP v2 identity, built the Salient way“. Pages: **/apie-imone/** (plan §3.4), **/kontaktai/**, **/privatumo-politika/**, **/404.html** (§3.12). All four are `kit: salient`, composed only from Kit API components (`docs/build-notes/kit.md`); no page JS, no page CSS.
Supersedes `pages-about-contact.md` (v2 „Maršruto linija“ notes, kept for history).

- Build: `python3 tools/build.py apie-imone kontaktai privatumo 404` · `python3 tools/check.py` → my 4 pages **OK, 0 errors**. The remaining warning per page („N element roots without data-salient“) comes from shared chrome/partials only (header, footer, GS-Pasitikėjimas, GS-404 — see R3).
- QA (Playwright Chromium): 1440×900, 1024×768, 390×844 and 390 with `prefers-reduced-motion: reduce` → no horizontal overflow, 0 console errors, no text < 12 px in `main` (except the decorative ✦ divider glyph of Scrolling Text, aria-hidden, shared), reduced motion shows every end state (Pinned Sections stack, clip path open, words visible).
- Front matter: `js:` removed everywhere; `css:` removed. `assets/css/pages/apie.css`, `kontaktai.css`, `privatumo-politika.css`, `404.css` now hold a 2-line comment only (no page references them). 404 keeps `root: /sgp-pervezimai/` (absolute asset/link paths).
- Resume note: the previous run was cut off mid-way. Apie and Kontaktai were migrated already (kept, polished); Privatumo politika was truncated half-way through the document (mis-nested `</main>`, missing `#slapukai`) — rewritten; 404 was still on the legacy stack — rebuilt.

## 1. Element composition

### /apie-imone/ (tone rhythm: Ph → Ph band → P → A photo → A → P → A → CTA)

| # | Row (tone) | Salient build |
|---|---|---|
| A1 | Inner head (Ph · 9989463) | Row Full Width Background · Parallax **Subtle** · BG Layer Animation **Slight Zoom Out Reveal** · Color Overlay v2 grade · Column 8/12: Yoast breadcrumbs, Label „Saugiai greitai patikimai“, **Animated Text H1** (Word Reveal, stagger), Road line, Intro, 3 Chips (Badge, Backdrop Blur 12) · Column 3/12 offset 1 (hidden on phones): Label + 4 **Link rows** (HLI 20/80, Color Hover, ↓) to `#imone #principai #kelyje #kodel-mes` · **glass band** Inner Row (Backdrop Blur 16): Label + **GS-Artimiausi** (4/12) · 2 × **Call (red)** Arrow Circle (5/12) · 2 × Link (3/12) — same split as home |
| A2 | Photo band (Ph · 1696742) | Row Full Width Content · **Clip Path Inset → Scroll Position** (0 8 % → 0, radius 3 → 0, offset 0–60) · Parallax **Regular** · height via padding 36vh (phone 24vh) |
| A3 | `#imone` (P) | Label + **Highlighted Text** (Regular Underline, Accent 3 px, H3 46/28 px; both routes are the `em` phrases) · Column 5/12 **Sticky** with **Cascading Images** (4:5, 3 layers 29566910 / 36377055 / 4440774, Grow In Reveal + Fade In From Bottom, parallax Subtle/Medium/High, Large Depth shadow) · Column 6/12 offset 1: Intro, Road line, promise (Responsive Text H3), **Button (ink)** Arrow Circle „Pervežimo paslaugos“, Link „Tarptautiniai pervežimai“, 6 **KV rows** (HLI 30/70, border animation) |
| A6 | `#skaiciai` (A photo · 1225126) | Parallax **Medium** · **Zoom Out Slowly** · overlay .82 · 4 × Column ¼ (tablet/phone ½) with Border Advanced top + **Border Animation** (delays 0/150/300/450): Label + **Milestone** Motion Blur (2 · 11 · 3 „–4“ · 4) + caption |
| A7 | `#principai` (A) | Label + Animated Text H2 + Road line · Intro (verbatim lead) · **Sticky Content Sections → Sticky Scroll Pinned Sections · Effect: Scale · Stacked Appearance ✓** · 80vh · desktop only (tablet/phone stack): 5 Colour sections (#161D21 / #EAEEED alternating) · Inner Row (Equal Height · **Column Content Alignment: Middle**): numeral (Responsive Text H1, 104 px, Accent / #C4301E) + H3 + verbatim paragraph grouped (gap 22 px) · Inner Column BG image with Column Animation **Fade In** + overlay .16 → 0 on hover (31570314, 17720190, 6720534, 17455631, 27383867) |
| A8 | `#kelyje` (P) | Label + Animated Text H2 „Kelyje apie 3–4 paras“ + Road line · **Scrolling Text** outline (Slowest, Move on Scroll, Spin divider ✦, Mask Edges) with the 7 route countries · **Image Gallery → Flickity** (Touch Indicator and Total, Image Parallax, Mask Edges, Drag Scale; 11053641, 2449454, 8858566, 21041157, 1606957) |
| A9 | `#kodel-mes` | `{{partial:gs-pasitikejimas|id=kodel-mes}}` (shared) |
| A11 | CTA | `{{partial:gs-kvietimas}}` (shared) |

### /kontaktai/ (Ph → A photo → P → A → P-alt; no GS-Kvietimas)

| # | Row (tone) | Salient build |
|---|---|---|
| C1 | Inner head (Ph · **18035726**) | as A1 without chips/band: breadcrumbs, Label „Atvykimas“, H1 „Kontaktai“, Road line, lead · Column 4/12 offset 1: 4 Link rows `#skambinkite #grafikas #parasykite #kur-vaziuojame` |
| C2 | `#skambinkite` (A photo · 7024783 red bokeh) | Row BG image · Parallax **Medium** · **Zoom Out Slowly** · overlay .78 · Equal Height · Column Margin 10px · 2 **glass Cards** (Column BG rgba(22,29,33,.62) → hover .86, **Backdrop Filter Blur 16**, radius 3, border 1px): Label (route) + H3 + number as **Text Reveal Wave** (Display block, 3.6vw 32–54 px) + „LT · Lietuva“ + **Call (red)** „Skambinti“ + tel **Link rows** (IE, JK / ES; No Hover Effect + typed →, so they share the KV rows' 0 inset) + Divider No Line + Label „Artimiausi išvykimai“ (content top-aligned; the Ispanija card keeps its spare space at the bottom) + 2 KV rows with `{{grafikas:next}}` dates · glass e-mail card (Text Reveal Wave `mailto:`; copy button dropped) |
| C3 | `#grafikas` (P) | Column 4/12 **Sticky**: Label, Animated Text H2 „Artimiausi pervežimai“, Road line, tip „Paspauskite eilutę…“, **Lift button** (Legacy Button) „Visas pervežimų grafikas“ · Column 8/12: **Tabs → Toggle Button** (Fade) with `gs-grafikas-ie` / `gs-grafikas-es` (tone P) |
| C4 | `#parasykite` (A) | Label + Animated Text H2 „Susisiekite su mumis“ · Column 7/12 **Callout** (left 2 px Accent) with **Fluent Forms „SGP kontaktai“** (vardas, el. paštas + visible help text, Kryptis, Ką vežame?, Žinutės tema, Žinutė, „Siųsti“, `data-demo-form`) · Column 5/12: Inner Column BG 13456097 with **Mask Reveal** (right, straight) + BG parallax Subtle + 4 route tel Link rows „Greičiau – telefonu“ |
| C5 | `#kur-vaziuojame` (P-alt) | Label + Animated Text H2 „Dvi kryptys. Keturios šalys pakeliui.“ + Road line + text + 2 KV rows + 3 Links · Column 7/12 **Scroll Position Advanced** (ty 70 → 0, scale .94 → 1, opacity .7 → 1) holding **Image With Hotspots** on `assets/img/marsrutai.svg` (7 numbered hotspots, tooltips with the per-direction numbers) |

### /privatumo-politika/ (A → P)

| # | Row | Salient build |
|---|---|---|
| V1 | Inner head without photo (A) | breadcrumbs, Label „Informacija · Slapukai (Cookies)“, Animated Text H1, Road line, e-mail as **Link** (Underline + mail icon) — no link column (plan V1) |
| V2 | `#dokumentas` (P) | **Tabs → Vertical Sticky Scrolling** (nav 25 %, **Text Outline Fill** links, content Fade; replaces the custom mini-TOC + reading-progress lane) · tab „01 · Informacija“ (panel `tab-01-informacija`, Inner Row ID `informacija`): Label, H2, „Informacija ruošiama...“, demo **Callout**, dashed placeholder card with the 5 GDPR parts (HLI rows) |
| V3 | tab „02 · Slapukai (Cookies)“ (panel `tab-02-slapukai-cookies`, Inner Row ID `slapukai`) | Label, H2 „Slapukai (Cookies)“, H3 (verbatim table caption) · **Toggle Panels → Minimal Shadow** (first open, multi-open): 5 cookies, each with 4 KV rows (Šaltinis · Aprašymas · Sukūrimo momentas · Galiojimo laikas) — production: Complianz `[cmplz-cookies]` (C-9) · „Pastaba“ Callout · **Lift button** „Keisti slapukų nustatymus“ (class `cmplz-manage-consent`, production `[cmplz-manage-consent]`) + Link „Kontaktai“ |

### /404.html (Ph → A)

| # | Row | Salient build |
|---|---|---|
| E1–E3 | GS „404 Content“ | `{{partial:gs-404}}` (shared): Section 100svh, 160483, **Parallax Fade** Medium, Label „Klaida 404“, Animated Text H1 **Blur** „Maršrutas nerastas“, Road line, lead, Button (paper) „Į pradžią“ + Button (glass) „Pervežimų grafikas“ + 2 tel Links |
| E4a | route strip (A) | outline **Scrolling Text** of the 7 route countries (Move on Scroll, Spin divider) — the „…mikroautobusai kursuoja toliau“ line made visible |
| E4 | `#paslaugos` (A) | Column 4/12 **Sticky**: Label „Paslaugos · 11“, Animated Text H2 „Visos pervežimo paslaugos“, Road line, Link „Visos paslaugos →“ · Column 8/12: `{{partial:gs-paslaugos|tone=A}}` (11 Link rows, Color Hover) |

## 2. Content check (compared with `git show HEAD:<page>` text in `<main>` and `docs/turinys-*.md`)

Kept verbatim: every heading, lead, paragraph, the 5 principles (approved fixes), the 6-row datasheet, all 5 phone numbers with their routes, e-mail, form labels/help/validation/success texts, the privacy placeholder list, demo notice, cookie table (all 5 rows × 4 fields + caption + note), 404 texts and the 11-service list.
Removed only as DROP/plan items: route ticket + relative „po N d.“ statuses, board/timetable tiles („09 SPAL.“), flap „4 0 4“, rails/rings/stop labels („Pasitikėjimas · 9 priežastys“, „2 skyriai“, „01 / 05“, „Tempkite“), copy-e-mail button („Kopijuoti“), map legend text (now inside the static SVG), GS-Board and GS-Arrival from Apie/404 (plan A11/E4: GS-Kvietimas resp. none). Dates still show in full words from `grafikas.json` (GS-Artimiausi, cards, GS-Grafikas tabs).
Changed form control: „Ką vežame?“ was a checkbox group (multi-choice) and „Kryptis“ a radio group in v2; both are now Fluent Forms **Dropdowns** with the same options (plain checkboxes/radios in the emulation give < 44 px tap rows). Production may switch „Ką vežame?“ back to a Fluent Forms Checkbox field.

## 3. Deviations from the plan (and why)

- **A2 photo 1696742** (Lithuanian road through pines) instead of 38404178 — 38404178 is on the „never used“ list (third-party truck branding, `check.py` NEVER_USE).
- **C1 photo 18035726** (frosty Lithuanian road, previously unused) instead of 7828591 — Vilnius panoramas are „never used“ (imply an office). The red bokeh 7024783 moved to C2 behind glass cards.
- **C4** keeps the page's own form („SGP kontaktai“: Žinutės tema, no phone field) instead of `gs-uzklausa` — the fields differ and must not be lost.
- **V2** uses Tabs → Vertical Sticky Scrolling (lead's brief: custom sticky indexes → Page Submenu / Vertical Sticky Scrolling) instead of a sticky 3/12 link column.
- **E4a** outline Scrolling Text added on 404 (native, no custom CSS).

## 4. Requests for shared (kit / partials / demo)

- **R1 demo.js** — re-open consent: click on `.cmplz-manage-consent` → `preventDefault()`, unhide `.cmplz-cookiebanner`, focus its first button (v2 had this in `privatumo-politika.js`; now the button only jumps to `#slapukai`). Production: Complianz `[cmplz-manage-consent]`.
- **R2 gs-404.html** — H1 is default H1 size on a 100svh hero; give the Animated Text the inner-head sizing `--fs:7.4vw;--fs-min:58px;--fs-max:116px;--lh:.92`; add `data-salient` to its 2 tel Links (2 warnings on 404).
- **R3 gs-pasitikejimas.html** — 8 of 9 Horizontal List Items lack `data-salient` (8 warnings on Apie and Tarptautiniai).
- **R4 GS-Grafikas rows (C-5 or kitlib)** — at 1000–1100 px in an 8/12 column the 25 % tel column wraps („+370 650 / 53161“); add `white-space: nowrap` to the tel cell (1 line in C-5) or use 20-45-35.
- **R5 emul Tabs → Text Outline Fill** — below 1000 px the nav becomes a static 18 px row; outline text is hard to read there. Suggest solid text with the opacity treatment under 1000 px (affects Privatumo politika and Taisyklės).
- **R6 Image With Hotspots on phones (C-7)** — at 390 px the 30 px markers cover the map labels; consider 24 px markers ≤ 690 px.
- **R7 Wave 3 cleanup** — `assets/js/pages/{apie,kontaktai,privatumo-politika,404}.js` are unreferenced; the four page CSS files hold only a comment and can be deleted.

No `sgp-custom.css` lines requested except the optional 1 line in R4.

## 5. Open issues

- Privatumo politika is still a demo: the client must supply the GDPR text; the cookie list is the old Joomla site's list (to be replaced by Complianz' generated list).
- No address, opening hours or company code exist — none are shown (by design, no invented facts).
- `marsrutai.svg` is schematic; the Ireland leg stays „maršrutas tikslinamas“.
- Emulation ≠ theme DOM (kit §10): verify Pinned Sections Scale, Clip Path Inset and the glass cards' Backdrop Filter on staging with the real Salient markup.
- Screenshots: `scratchpad/shots/ac5-*`, `ac3-*`, `ac2-*` (1440, 1024, 390, reduced motion). 404 was checked through a parent-directory server (`/sgp-pervezimai/` root).

## 6. Review fixes (page-findings „about-contact“)

- **Privatumo politika · tab anchors** — production renders tab panels as `tab-<sanitize_title(title)>` (salient-core tab.php / tabbed_section.php), so the demo panels are now `tab-01-informacija` / `tab-02-slapukai-cookies` (nav hrefs match) and `#informacija` / `#slapukai` are Row IDs on each tab's first Inner Row. „Keisti slapukų nustatymus“ (`#slapukai`) and deep links keep working (checked: nav click, in-page link, `/#informacija` at 390).
- **Kontaktai · phone cards** — tel rows switched to Style „Bottom Border, No Hover Effect“ (+ typed →), so labels line up with the KV rows at the card's content edge (1440: x 109 / 774; 390: x 43). No Design Options exist on Horizontal List Item, so padding-left on the KV rows was not an option. Badge „Artimiausi išvykimai“ lost Margin Top auto: both cards are top-aligned; the Ispanija card's spare ~80 px now sits at the bottom instead of mid-card.
- **Apie · Principai stack** — image Inner Columns use Column Animation Fade In instead of Background Layer Animation Reveal Rotate (the next pinned card covered still-tilted images); Inner Rows use Column Content Alignment Middle and the text blocks dropped Margin Top auto, so the numeral sits with its H3 + text (no 300 px void).
- **Skipped · Kontaktai `#parasykite`** — the right column is already top-aligned with the Mask Reveal photo (13456097, 300 px) above „Greičiau – telefonu“; the „empty 340 px“ in the review frame was that photo before its 1.3 s clip-path reveal.
- **Skipped · GS-Pasitikėjimas on phones (R8 for shared)** — shared partial; `data-mobile="columns"` is already gone. Natively a 2-column Horizontal List Item keeps its 20 | 80 ratio below 1000 px (element-horizontal-list-item.css stacks only 3/4 columns), so the text column is still ~261 px at 390 (item 04 ≈ 16 lines). If it should stack, the partial needs 1-column items with the number inline (e.g. Label above the paragraph) — a shared change.

