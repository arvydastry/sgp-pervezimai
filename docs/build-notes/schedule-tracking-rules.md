# Build notes — team „schedule-tracking-rules“ (Salient 18.2.1 rebuild, Wave 2)

Pages: **/pervezimu-grafikas/** (plan §3.9) · **/siuntos-sekimas/** (§3.10) · **/taisykles/** (§3.11).
Sources: `src/pages/pervezimu-grafikas.html`, `src/pages/siuntos-sekimas.html`, `src/pages/taisykles.html` — all `kit: salient`, **no page JS**; page CSS only on /taisykles/ (`assets/css/pages/taisykles.css`, 1 interim rule — see §3.9).

Status (2026-09-24):
- `python3 tools/build.py pervezimu-grafikas siuntos-sekimas taisykles` → OK.
- `python3 tools/check.py pervezimu-grafikas siuntos-sekimas taisykles` → **0 errors**. 1 warning per page = 15 element roots without `data-salient`, all inside the shared footer partial (GS-Poraštė); every element root on our pages is tagged.
- Headless Chromium: 1440×900, 1024×768 and 390×844 → horizontal overflow 0 on all three pages; no console errors or page errors (also `?tab=airija`, `?toggle=1`, `?kodas=SGP-DEMO`, `?kodas=ABC123`); reduced-motion run: every milestone at its end value, lists/lines visible, nothing left hidden except closed toggles, hover tooltips and Fancy Box hover text (as intended).
- Resume note: the previous attempt stopped in the middle of `taisykles.html` (tabs 4–6, PDF row and GS were missing → 12 check errors). Tabs 4–6, L6 and L7 were written in this pass; grafikas and sekimas were already migrated and are refined below.

---

## 1. Element composition

### /pervezimu-grafikas/
| # | Row | Salient build |
|---|---|---|
| R1 | Inner head (dark) | Row Full Width Background · **Video Background** 3847797 (phones: image 1225126) · Parallax **Subtle** · Background Layer Animation **Slight Zoom Out Reveal** · v2 hero grade overlay. Column 8/12: breadcrumbs, Badge (Minimal Line) „LT ⇄ IE · LT ⇄ ES“, **Animated Text H1** (Word Reveal, stagger), road line (Divider Small Line, Animate Line), Intro. Column 3/12 (offset 1): „Turinys“ + 2 × Button Underline → `#lenta`, `#ka-verta-zinoti`. **Glass band** = Inner Row (Backdrop Filter Blur 16): GS-Artimiausi · 2 × Call (Arrow Circle, stretch) · Pause button (`sgp-motion-toggle`, required: video) + Next Section button. |
| R3/R4 | `#lenta` Chapter A | Column **3/12** Sticky Content: Label „Lenta“ + Animated Text H2 (4.4vw, 40–64px) + road line + desktop-only Image (Reveal Rotate From Bottom, hover Zoom In). Column **9/12**: **Tabs → Minimal** (Fade) „Visi · Airija · Ispanija“ = GS-Grafikas Airija / Ispanija (tone A, „Atnaujinta …“ label inside the GS), full-width animated Divider between them in „Visi“; 2 × Call below. Deep links `?tab=visi|airija|ispanija`. |
| — | Photo band | Row Full Width Content · Background Image 1696742 · Parallax **Medium** · **Clip Path Inset** (Scroll Position, bg layer, 0 6 % → 0, radius 3 → 0, Zoom Fade In) · outline **Scrolling Text** (Slowest, ✦ spin divider, Move on Scroll, Mask Edges) of the four routes. |
| R6 | `#ka-verta-zinoti` Chapter P (Color Change Section) | Column 5/12 **Sticky Content**: Label + H2 „Laiką ir vietą suderinsime telefonu“ + road line + 4 **KV rows** (HLI 40\|60, Border Animation). Column 7/12: Inner Row map surface → Inner Column **Scroll Position Advanced** (ty 60 → 0, scale .94 → 1) with **Image With Hotspots** on `assets/img/marsrutai.svg` (7 numbered hotspots, hover tooltips) + Inner Row: Label „Susiję puslapiai“ + 5 **Link rows** (HLI, Color Hover Effect Extra Color 1, Full Item Link, „→“). *Change vs the earlier draft:* the link list moved under the map so the shorter (sticky) column is really sticky and the map column is not left half-empty. |
| R7 | GS-Kvietimas | `{{partial:gs-kvietimas}}` (Parallax Medium, Zoom Out Slowly, Content Trail). |

### /siuntos-sekimas/
| # | Row | Salient build |
|---|---|---|
| K1 | Inner head | Background Image 35497082 · Parallax Subtle · Slight Zoom Out Reveal · H1 „Siuntos sekimas“ · Intro · links Paieška / Pagalba · glass band (GS-Artimiausi, 2 × Call, „Visas grafikas →“, Next Section). |
| K2 | `#paieska` Chapter P | Column 5/12 **Callout** (#EAEEED, left 2px Accent): Label, Animated Text H2 „Kur keliauja Jūsų siunta?“, text, **Fluent Forms** „Siuntos sekimas“ (field „Siuntos kodas“, placeholder „Siuntos kodas...“, required msg „Neįvestas siuntos kodas!“, submit „Siuntos lokacija“; production Confirmation → Redirect to `https://siuntos.sgp-pervezimai.lt/sekimas.php?kodas={inputs.kodas}`), demo-only Inner Row (chip „Demo“ + note + „Išbandykite: SGP-DEMO →“), help line. Column 7/12 → Inner Column **Mask Reveal** (Right, Straight) → Image 6407553 (hover Zoom In). Column 12: full-width animated Divider + **Icon List Horizontal** (Stations 1–3). |
| K3 | `#rezultatas` **DEMO ONLY** | Hidden unless `?kodas=` (demo.js). Not found: Callout with the live tool's message „Toks siuntos kodas neegzistuoja!“ + demo note + 2 × Call. `SGP-DEMO`: white card Inner Row (**Equal Height + Column Content Alignment Middle**): chips, H3, KV rows, **Icon List Vertical** log (3 steps) | Image With Hotspots (1 hotspot, Always Show) + note. Production: row does not exist. |
| K4 | `#pagalba` Chapter A | Row **Column Alignment Bottom**: Label + H2 „Neradote siuntos kodo?“ + road line + Intro | 2 × Call (stretch) · 3 × **Fancy Box → Description on Hover** (Siuntų pristatymas 13456097 · Pervežimų grafikas 36383706 · Taisyklės 6169133; Short Zoom) in columns with **Scroll Position Advanced** (ty 40 / 110 / 180 → 0 — a staggered parallax cascade on desktop). |
| K5 | GS-Kvietimas | shared partial. |

### /taisykles/
| # | Row | Salient build |
|---|---|---|
| L1 | Inner head | Background Image 6169133 · Parallax Subtle · Slight Zoom Out Reveal · H1 „Siuntų siuntimo taisyklės“ · approved lead · link column: Button Underline with Icon download „Atsisiųsti sutartį su siuntėju (PDF, 72 KB)“ + links „Draudžiama siųsti (12)“ → `#draudziama-siusti`, „Baudos“ → `#baudos`, „Pretenzijos“ → `#pretenzijos` · glass band. |
| L2 | `#taisykliu-tekstas` Chapter P | **Tabs → Vertical Sticky Scrolling** · *Sticky Aspect: Tab Links* · *Navigation Functionality: All Links Visible* · *Navigation Width: Regular* · *Tab Link Element: H4* · 6 tabs = sections 1–6. Panel ids follow 18.2.1 `tab.php`: `tab-` + `sanitize_title(Title)` (`tab-1-siuntu-tikrinimas` … `tab-6-atvejai-kuriais-imone-neprisiima-atsakomybes`; *Tab ID* is only the fallback for fully non-Latin titles). The v2 anchors (`tikrinimas`, `siuntejo-garantija`, `vezejo-atsakomybe`, `draudziami-daiktai`, `pretenzijos`, `atsakomybes-ribos`) are the **Row ID of each tab's first Inner Row**, so hero links, the 2.2 link and cross-page links (`taisykles/#vezejo-atsakomybe`) resolve in production too. Each tab: Inner Row(s) with Animated Text H2 + full-width animated Divider + Text Blocks (clause ids `p2-1 … p6-2` kept). |
| L2·3 | 3.4 | **Highlighted Text** Regular Underline 3px („5 darbo dienas“) + 2 KV rows (Kelyje / Įsipareigojimas siuntoms). |
| L3 | 4.2 | Dark Inner Row `#draudziama-siusti` (#0F1417, radius 3, Extra Class `sgp-dark`; Inner Row has no Text Color option → each Inner Column has **Font Color #F2F4F3**) → Label „Draudžiama siųsti (12)“ + H3 + 2 × **Fancy UL** (Font Icon ✕, Accent, animated) 6 + 6. |
| L4 | 4.5 | Inner Row `#baudos`: Inner Column 5/12 (Border Advanced top 2px Accent + **Border Animation**) → Label „4.5. Baudos“ + **Milestone** 1200 · Count To Value · Symbol „EUR“ After/Superscript · Subject „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“ | Inner Column 7/12 → 6 **KV rows** (header + 5 fines, 40 \| 60, Responsive Display: **Stacked** — 2-column items keep 40 \| 60 natively; Column One = Text Element Type *Paragraph* with content `<p class="nectar-inherit-h6">` — there is no H6 option) · **Toggle Panels → Animated Circle** (closed) „Visas 4.5 punkto tekstas“ (`#visas-4-5`, `?toggle=1`) with the full verbatim 4.5 text + Fancy UL (Standard Dash) of the five fine sentences. |
| L5 | 5.1 | **Highlighted Text** (23px, underline on „per 5 dienas“, „per 14 dienų“; whole clause verbatim) + 3 Inner Columns with Border Advanced top + **Border Animation** (delays 0/200/400) → **Milestone** Motion Blur Slide In „0 d.“, „5 d.“, „14 d.“ with the captions. |
| L2·6 | 6.1 | Text Block + **Icon List Vertical** (Number 1–8, small, Icon Colored W/ BG; `screen-reader-text` „1) “… keeps the clause numbering for screen readers) + Text Block 6.2. |
| L6 | `#sutartis` P-alt | Column 6/12 **Callout** (white, left 2px Accent, Fade In From Left): **Icon** download (Border W/ Hover Animation, draw) + Label „PDF · 72 KB“ + Animated Text H3 „Sutartis su siuntėju“ + **Legacy Button** Regular Large Extra Color 1 (lift) „Atsisiųsti (PDF, 72 KB)“ (aria-label with the full name) + Link „Į turinį ↑“. Column 5/12 (offset 1) **Scroll Position Advanced** (ty 90 → −20, scale .94 → 1) → Image 7464731 (Reveal Rotate From Right, hover Zoom In, 4:3). |
| L7 | GS-Kvietimas | GS-Board dropped (plan). |

## 2. Content check — nothing lost

Compared the visible text of `git show HEAD:<page>/index.html` with the new build (`scratchpad/txtdiff.py`).
- **All legal text is complete**: sections 1–6, clauses 2.1–6.2, the 12 prohibited items, the fines table, the full 4.5 text, 6.1 items 1)–8), 6.2 — verbatim + approved fixes (`turinio-pataisos.md` §1.7 #56–60).
- Schedule: every route, date, number and the „Tikslų išvykimo laiką…“ note (now inside GS-Grafikas) + „Atnaujinta …“; KV facts; links (now 5).
- Tracking: H1, lead, H2, body, field/placeholder/button/messages verbatim, demo note, SGP-DEMO sample (chips, route, KV, 3-step log, map note), help line + both LT calls, 3 cards with their texts.
- Removed on purpose (DROP list / plan): relative statuses („po N d.“, „Artimiausias · po 4 d.“), table column captions, lane chart + its captions (#laiko-juosta), split-flap codes, waypoint rails („01 Lenta“, „01–06 Taisyklės“, „Turinys“ index), inline SVG map labels (now in `marsrutai.svg`), sekimas trip-lane stops and „Ieškoma…“ state, card kickers „Paslauga / Grafikas / Taisyklės“, GS-Arrival (form, e-mail, UK/IE/ES numbers — all still in the footer) → GS-Kvietimas, GS-Board on /taisykles/.
- Anchors kept: all section/clause ids above, `#lenta`, `#ka-verta-zinoti`, `#paieska`, `#rezultatas`, `#pagalba`, `#draudziama-siusti`, `#baudos`, `#visas-4-5`. Gone: `#laiko-juosta`, `#uzklausa` (GS-Arrival) — no page links to them.

NEW / changed strings (for the NEW list in `turinio-pataisos.md`): „Lenta“, „Turinys“, „Greitos nuorodos“, „Susiję puslapiai“, „Pagalba“, „Siuntos paieška“ (labels) · „4.5. Baudos“ · „PDF · 72 KB“ + H3 „Sutartis su siuntėju“ (was one label „Sutartis su siuntėju · PDF · 72 KB“) · button „Atsisiųsti (PDF, 72 KB)“ · „Į turinį ↑“.

## 3. Requests for shared (not edited by this team)

1. **Tabs → Vertical Sticky Scrolling: the kit mixes two option sets.** In salient-core 18.2.1 (`nectar_maps/tabbed_section.php`) *Tab Content Animation* (Fade / Slide Reveal / Slide Reveal Zoom), *Tab Link Animation* (Opacity Change / Animated Underline / Text Outline Fill), *Navigation Side* and the %-based *Navigation Width* exist **only for Sticky Aspect = Tab Content**. For *Tab Links* the options are *Navigation Functionality* (All Links Visible / Only Active Link Visible), *Navigation Width* (Regular / Wide / Narrow), *Navigation Item Spacing* 15–45px, *Navigation Item Mobile Display* (Visible Above Each Section / Hidden), *Tab Spacing* (5–50 %, 10/20px, None), *Tab Link Element*, CTA. The theme's Tab Links look: links change opacity, a **1 px line indicator (3 px wide) slides to the active link** (`transform .5s cubic-bezier(0,0,.34,.96)`), the nav is **hidden below 1000 px**, optional **CTA under the nav** (margin-top 35px, padding-left 50px). Please (a) emulate that for `data-sticky-aspect="default"` (line indicator, `data-tab-spacing`, nav hidden < 1000 unless Mobile Display = Visible Above Each Section, `vs_enable_cta` → e.g. the PDF link in the sticky nav), (b) fix the `_kit.html` specimen, kit.md §5 and plan §3.11 L2 (they say Tab Links + Fade + Text Outline Fill). /taisykles/ now carries the correct Tab Links label and no Fade/Outline attributes (content stays fully readable).
2. **Reduced motion (C-2):** if the kit keeps the Tab Content fade (`.wpb_tab:not(.active-tab){opacity:.28}`), force `opacity:1` under `prefers-reduced-motion` — a full-page reduced-motion capture showed every non-active tab at .28.
3. **C-5 schedule rows (GS-Grafikas):** at 1000–1199 px the number column wraps („+353 86 450 / 3104“, „+34 602 547 / 929“; seen at 1024 in a 9/12 column). Suggest `white-space:nowrap` on the number item and let the dates item take the slack.
4. **Toggle deep link:** `/taisykles/?toggle=1` opens `#visas-4-5` but lands with the toggle title above the viewport (scrollY 4402; the text of the opened panel is shown). `scrollToEl` seems to run before the open height/Lenis settle — scroll after the open transition, to the title minus header height.
5. **Inner Row borders:** `.vc_row.inner_row` supports only `--border`; WPBakery Design Options allow per-side widths. Not blocking (4.2 inset uses no side border now).
6. **C-7 hotspots on phones:** on /pervezimu-grafikas/ at 390 px the 7 markers crowd the ~330 px map and cover some labels — consider smaller markers ≤ 690 px.
7. **Wave 3 cleanup:** `assets/css/pages/grafikas.css`, `sekimas.css`, `taisykles.css` and `assets/js/pages/grafikas.js`, `sekimas.js`, `taisykles.js` are no longer referenced by any page. *(2026-09-25: `assets/css/pages/taisykles.css` now exists again with new content — only the §3.9 interim rule.)*
8. The old notes `docs/build-notes/pages-schedule-tracking-rules.md` describe the legacy v2 build; archive or delete with the legacy stack.
9. **Vertical Sticky Scrolling link contrast (review 2026-09-25):** 18.2.1 dims inactive Tab Links to `.45` (`class-nectar-element-styles.php`; the kit matches), i.e. #1C1D1D on #F5F7F6 ≈ 2.8:1 for 24px/600 text (needs 3:1). Interim page-level fix: `assets/css/pages/taisykles.css` (front matter `css:`) sets `.6` (≈ 3.9–4.4:1; active/hover stay 1), with both the kit selector and the real 18.2.1 selector (`.nectar-scrolling-tabs .scrolling-tab-nav ul li`). **Please move the rule into `sgp-custom.css` (C-8)** — /privatumo-politika/ („01 · Informacija“ / „02 · Slapukai“) has the same issue — then delete the page CSS and the `css:` line.

## 4. Open issues

- **6.1 numbering:** items shown as Icon List numbers 1–8 (the „)“ is visual only; screen readers get „1) …“). `turinio-pataisos.md` #60 promised the same „1)“ numbering — if the client insists on the parenthesis, switch to Fancy UL *None* with literal „1) …“.
- **4.2 list** has no 01–12 numbers any more (Fancy UL ✕); the count stays in the label „Draudžiama siųsti (12)“.
- **Tracking result** is demo-only (`demo.js`); production relies on the Fluent Forms redirect to the live tool (UAB „GP Soft“), whose success view was never observed.
- Headless screenshots jump-scroll, so Mask Reveal / lazy images sometimes look empty in the sheets; a real wheel-scroll probe shows them revealed (no bug).
- PDF: links to the live file (72 KB); content not reviewed.

## 5. Review fixes (2026-09-25)

- /taisykles/: panel ids → `tab-<sanitize_title>`; nav hrefs point to them; v2 anchors moved to the first Inner Row (Row ID) of each tab; hero column tag „Link to Inner Row IDs“. 4.2 inset: `data-text-color` moved from the Inner Row to its 3 Inner Columns (Font Color #F2F4F3). KV row tag no longer claims „Text Element Type: H6“. Tab-link contrast: §3.9.
- /pervezimu-grafikas/: photo-band Scrolling Text content „Lietuva → Airija · Lietuva → Ispanija · Airija → Lietuva · Ispanija → Lietuva“ — no ✦ in the text; only the element's red spinning ✦ divider separates the repeats.
- Checked, already correct: the fines header row was already *Responsive Display: Stacked* (markup has no `data-mobile="multiple"`); only this note still said Multiple Columns.
