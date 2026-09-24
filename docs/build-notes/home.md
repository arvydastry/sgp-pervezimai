# Home team — build notes (Wave 2, „SGP v2 identity, built the Salient way“)

**Page:** `src/pages/index.html` → `index.html` (front matter `kit: salient`, no `css:`, no `js:`).
**Page CSS:** none. `assets/css/pages/home.css` (279 lines) and `assets/js/pages/home.js` are the old v2 files. Nothing references them any more, so shared can delete them in Wave 3.
**Checks:** `python3 tools/build.py index.html` and `python3 tools/check.py` pass for `index.html` (0 errors). 19 warnings for element roots without a label remain, and all of them are in shared partials (see requests). No console errors, and there is no horizontal overflow at 1440×900, 1024×768 or 390×844. With reduced motion (Playwright `reducedMotion: 'reduce'`) every block shows its end state, the sticky sections are stacked and the button reads „Paleisti judesį“.
**Resuming the interrupted attempt:** the page was already about 95 % migrated when this attempt started. It was kept and completed. Changes in this pass:
- H4: the Scrolling Text divider is now a solid red spinning ✦ that marks each loop (*Outline Applies To: Text Content*).
- H4: the map column now uses *Column Animation Type: Scroll Position Advanced* (scale .92 → 1).
- H4: added a Link to `/tarptautiniai-pervezimai/`. This brings back the original site's hero tile „Tarptautiniai pervežimai“.
- H5: the plain image became a **Video Lightbox** (Mouse Follow, MP4 15602514, poster 27383867, label „Kelionė per Europą“). It sits in a column with *Reveal From Right*.
- 15 element roots that had no label now have `data-salient`.
- The front matter `salient:` line was updated to match.

## Review fixes (Wave 4, `page-findings.json` → home)

- **Color Change Section:** every column / inner column with its own background inside a color-change row now declares its own text colour — #siuntos-sekimas card (`data-text-color="light"`), #pries-siunciant „Svarbu“ callout and the #marsrutai map surface (`"dark"`). Forced-tone check: card text 15.4:1 / fog 6.8:1 / label 4.5:1 on #161D21, callout 16.9:1 on #FFF. The three ink buttons (#apie, #eiga, #pries-siunciant Legacy) take `--btn-bg / --lb-bg: var(--tone-inv-bg)`, so they turn paper while a dark chapter is active instead of melting into #0F1417. The outline Scrolling Text stroke is `var(--tone-fg)`. Note: deleting `--outline-color` is not enough; emul `typography.css:80` falls back to `currentColor`, which is `transparent` on that element.
- **Services (H3):** Section Width 35 → 28. Content Alignment is Middle and Height stays 100 %: the cards measure 565–596 px against 602–782 px sections from 1280×720 to 1440×900, so they never clip and no 200 px band is left at the bottom. The chapter head is now section 1 of the pinned track, and the separate head row shows on tablet and phone only. Pinned element 5 724 → 4 933 px. Home 18 197 → 16 777 px at 1440. The Horizontal Scrolling tag no longer claims *Effect Enabled*, and `data-enabled` was removed.
- **Glass band:** a 12/12 bottom-edge inner column (hairline, desktop only) holds the pause Button (now Underline) and the Next Section button. The 3/12 column keeps only „Visas grafikas →“, so it no longer wraps at 1024. The #kelioneje pause column is desktop only too. Tablets and phones get one pause Button under the Scrolling Text in H4, and the footer keeps the site-wide one. Salient elements have no Device Visibility, so everything device-specific sits in its own column.
- **Hero H1:** changed to Highlighted Text. The two destinations get the red route underline.
- **Cascading Images:** the milestones moved to their own row, leaving about 110 px between layer 2 and the top rules. The parallax was dropped, because in 18.2.1 it disables the layer animations (`nectar_cascading_images.php`), so the old tag was not reproducible.
- **Tags:** the Link rows say „no CTA“, and the images say „file uploaded pre-cropped 4:3 / 16:10 / 16:9“ (the Image element has no aspect option).
- **H9:** disabled in the demo.
- **Hero on phones:** this finding was already fixed by shared C-15. Measured per text line: label ≥ 4.72:1, H1 ≥ 5.6:1, intro ≥ 4.98:1. No page change.

## Section composition (v2 anchors kept; Color Change Section on every chapter row)

| # | Row ID · tone | Salient 18.2.1 composition |
|---|---|---|
| H1 | `#pradzia` · Ph | **Section** Full Width Background: Min Height 100svh (phone 92svh), Flexbox column / flex-end, **Video** 29374299 + poster (phone 36383706), **Parallax Fade · Medium**, Color Overlay = v2 hero grade. Row 1 (Column Alignment Bottom): Column 8/12 (Slight Fade In From Bottom) = **Badge** Minimal Line + **Highlighted Text H1** (Regular Underline, Accent, 3px, delay 700; Theme Options H1 typography) „Lietuva – *Airija*. / Lietuva – *Ispanija*. / Ir atgal.“ — the two destinations carry the red route line, as in the #apie statement + **Divider** Small Line (Animate Line, delay 500) + **Responsive Text** H5. Column 4/12 (phone hidden, Fade In 900 ms) = 3 **Badge** chips (Backdrop Blur 12). Row 2 = glass band: **Inner Row** Backdrop Filter Blur 16, rgba(11,14,16,.55), radius 3. Inner Columns: 4/12 Label + **GS-Artimiausi**; 5/12 two **Call (red)** buttons (Arrow Circle, Stretch); 3/12 **Underline** „Visas grafikas →“; 12/12 bottom edge (Border top hairline, Flexbox row, flex-end, **Device Visibility: tablet + phone hidden**) = pause **Button → Underline** (`sgp-motion-toggle`) + **Next Section**. |
| H2 | `#apie` · P | Chapter row. Column 10/12 = Label „01 · Apie mus“ + **Highlighted Text → Regular Underline** (Accent, 3px; the two route phrases are underlined). Column 5/12 = **Cascading Images** 4:5 (7541981 Grow In Reveal · 6169133 Fade In From Bottom, Large Depth; *Enable Parallax Scrolling* off — in 18.2.1 it switches the layer animations off). Column 6/12 (offset 1) = Intro + **KV rows ×6** (HLI 30\|70, Border Animation) + **Button (ink)** „Skaityti daugiau“. Row padding bottom 112px (phone 64px). **Second row** (P, Color Change, padding 0 / 8 %): four Columns 3/12 (Border Advanced top, Border Animation, delays 0/150/300/450) = Label + **Milestone** Motion Blur: 2 · 11 · 3 + symbol „–4“ · 4. |
| H3 | `#paslaugos` · A | Tablet/phone head row (`#paslaugos`, Device Visibility: desktop hidden): Label + **Animated Text H2** + Road line + Intro · Chip + Link. Desktop row (A, **Color Change**, Device Visibility: tablet + phone hidden): **Sticky Content Sections → Horizontal Scrolling** (Section Width 28, Gap 16, Height 100 %, Subtract Navigation Height, **Content Alignment: Middle**, radius 3) with 13 sections: 1 = the chapter head (Color #0F1417 = page colour, no link: Label, H2, Road line, Intro, Chip, Link), 2–12 = the 11 services (Color #161D21, **Link Mouse Indicator** „Plačiau“: Image pre-cropped 4:3 + Hover Zoom In, red numeral, H3, summary, tags), 13 = #0B0E10 „Pagalba renkantis“ with two red calls and a Link. Tablet/phone row (desktop hidden): 11 **Link rows** (HLI 20\|80, Color Hover White, no CTA) with summaries + „Nežinote…“ + two red calls. |
| H4 | `#marsrutai` · P | Label „03 · Maršrutai“ + Animated Text H2 „Dvi kryptys. Keturios šalys pakeliui.“ + Road line. Full Width Content row: **Scrolling Text** Slowest 45 s, Text Outline Thin (text only; outline = row text colour, follows the Color Change tone), Move on Scroll, Mask Edges, divider ✦ ½ red + Spin on Scroll, 8vw (phone 17vw). Row 3: Column 8/12 is a Callout surface (#EAEEED, radius 3) with **Scroll Position Advanced** (ty 70 / .92 / .6 → 0 / 1 / 1). It holds the **Image With Hotspots** on `assets/img/marsrutai.svg` (Numerical, Show On Hover, Medium Depth, Enable Animation, 7 hotspots: LT phones, PL/DE/BE/FR „Pakeliui…“, ES +34, IE +353 „maršrutas tikslinamas“); Font Color Dark on its own surface. Column 4/12 = Label „Pakeliui“ + H3 + verbatim paragraph + **Badge** „4 šalys“ (Accent) + Link „Tarptautiniai pervežimai →“. Then `{{partial:gs-marsrutai\|cols=2\|tone=P}}`. |
| H5 | `#kelioneje` · Ph | Row Full Width Background: **Video** 4685871, **Parallax Regular (0.28)**, **Clip Path Inset** (Scroll Position, Background Layer, 0 6 % 0 6 % → 0, round 3 → 0, offset 0–50, addon Zoom Fade In), cinematic overlay. Column 7/12 = Label + **Animated Text H2 → Scroll Position: Opacity** „Du namai, vienas kelias tarp jų.“ + Intro + Link „Keleivių pervežimas →“. Column 5/12 (**Reveal From Right**) = **Video Lightbox** Play Button With Image – Mouse Follow (See Through Contrast, Zoom BG Image, 15602514 / poster 27383867). Column 12 = **Divider** Full Width (Animate Line) + **Icon List** horizontal ×5 (Icon Colored No BG, Accent, Animate): the 5 comfort items verbatim. Flex column with the pause Button (Underline; Device Visibility: tablet + phone hidden — no video there). Tablets and phones get their pause Button under the Scrolling Text in H4. |
| H6 | `#eiga` · P | Column 4/12 **Sticky (CSS, Top)**: Label „05 · Kelionės eiga“ + Animated Text H2 „Nuo durų iki durų“ + Road line + **KV rows ×2** (Kelyje · Įsipareigojimas siuntoms) + Button (ink) „Siuntos sekimas“ (colours follow the Color Change tone). Column 7/12 (offset 1) = **Divider** Full Width (Animate Line, the road) + **Icon List** Stations 1/2/3 (Icon Colored W/ BG, numbers) + Inner Column **Scroll Position Advanced** (ty 70 / .9 / .7 → 0 / 1 / 1) with Image 4440774 16:10, Hover Zoom In Crop. |
| H6b | `#grafikas` · A | Asphalt texture row: BG image 4040619, **Parallax Subtle (0.20)**, **Slight Zoom Out Reveal**, overlay .9. Column 4/12 **Sticky**: Label „06 · Grafikas“ + H2 „Artimiausi pervežimai“ + Road line + two red calls + 3 destination-line Links (+353, +44, +34) + **Button (glass)** „Visas pervežimų grafikas“. Column 7/12 (offset 1) = **Tabs → Minimal** (Fade): Airija / Ispanija, each Image 16:9 (Zoom In) + `{{partial:gs-grafikas-ie\|es\|tone=A}}` (Horizontal List Item rows). |
| H7 | `#pries-siunciant` · P-alt | Column 5/12 **Sticky**: Label „07 · Prieš siunčiant“ + H2 (verbatim question) + **Callout** Inner Column (#FFF, left 2px Accent, **Font Color: Dark**) „Už siuntinio turinį atsakingas siuntėjas.“ + **Milestone** Count To Value 1200 + superscript „EUR“ + **Legacy Button** Regular Large Extra Color 1 „Visos taisyklės“ (−3 px lift; colours follow the tone) + Underline Link with download icon (PDF). Column 7/12 = **Toggle Panels → Animated Circle** (Right, 40, Divider, Accordion, First Open): Draudžiama siųsti (12) with Fancy UL ✕ · Pakavimas (4) with Fancy UL dash · Gavėjas ir pristatymas · Baudos with KV rows 40\|60 and Link. |
| H8 | `#siuntos-sekimas` · A | Equal Height. Column 6/12 **Card (A)** #161D21, **Font Color: Light** = Label „08 · Siuntos sekimas“ + H2 + Responsive Text + **Fluent Forms** „Siuntos sekimas“ (demo `tracking`, redirect `?kodas=`) + Link „Skambinti – visi telefonai →“ (`/kontaktai/#skambinkite`). Column 6/12 → Inner Column **Mask Reveal** (Right, Straight) with Image 6170458 (Fit, Zoom In). |
| H9 | `#atsiliepimai` · P | **Row → Disable Row ✓ in the demo too** (review fix) — not rendered; a source comment marks the spot. Reserved texts for later: „Čia bus tikri klientų atsiliepimai“ / „Vieta rezervuota – išgalvotų atsiliepimų nenaudojame.“ Then Testimonial Slider → Minimal with real reviews only. |
| — | GS | `{{partial:gs-uzklausa\|id=uzklausa\|media=36377055}}` (form + phones) → `{{partial:gs-kvietimas}}` (After Page/Post Content) → footer / call bar are automatic. |

Parallax and motion used on the page: Parallax Fade (H1), Cascading layer parallax Subtle + Medium (H2), the Horizontal Scrolling track + mouse indicator (H3), Scroll Position Advanced (H4 map, H6 photo), Scrolling Text Move on Scroll + Spin (H4), video parallax Regular + Clip Path Inset (H5), row parallax Subtle + Slight Zoom Out Reveal (H6b), Mask Reveal (H8), Reveal Rotate / Reveal From Right / Fade In entrances, Milestones Motion Blur / Count, Border Animation on KV rows and milestone columns, and Divider line draws. Hover effects: Arrow Circle buttons, Legacy lift, image Zoom In / Zoom In Crop, Link rows colour hover, Video Lightbox mouse follow, hotspot tooltips, toggles circle.

## Deviations from plan §3.2 / §5.3 (deliberate)

- **H3 uses the 11 service cards, not `{{paslaugos:hscroll}}` (6 groups, 45 %).** The v2 page (HEAD) had 11 per-service cards with a summary and tags. Keeping them keeps that content and links each service in one click. The width is 28 (the chapter head rides as section 1), so about 3.5 sections show at a time. Phones and tablets get 11 Link rows with summaries instead of 11 stacked 100vh cards. The 6-group set stays available for the services page.
- **H4 uses `gs-marsrutai|cols=2`.** The „Pakeliui“ column sits next to the map instead of inside the GS as a 3rd column. The content is the same and the map gets its explanation beside it.
- **H5 Video Lightbox uses 15602514, not 3987777.** 3987777 is a ferry clip, and ferry media stays unused until the Ireland route is confirmed (`turinio-pataisos.md` #9, DS media exclusions). The label is „Kelionė per Europą“ from the approved NEW-string list.
- **H6b `#grafikas` was added** because the brief asks for a schedule section with tabs and rows. It replaces the v2 route timetables. As a result the chapter numbers are 06 Grafikas · 07 Prieš siunčiant · 08 Siuntos sekimas.
- **H9 is disabled in the demo as well** (review: the dashed placeholder between two dark chapters made the page look unfinished).

## Content check (HEAD `src/pages/index.html` + `turinys-puslapiai.md` → now)

All text from HEAD is present verbatim:
- the H1 lines and lead
- both calls (Airija / Ispanija)
- the next departures (GS-Artimiausi)
- the company statement, the intro paragraph, the 6 KV rows and „Skaityti daugiau“
- the 4 stats
- the services H2 and intro, and the 11 service names with summaries and tags
- „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“
- the routes H2 and the „Pakeliui“ paragraph
- route cards 3–4 paros with IE/UK/ES numbers (GS-Maršrutai + H6b)
- the timetables (GS-Grafikas)
- the H5 H2, lead and 5 comfort items, plus the Keleivių link
- the 3 steps and 2 KV facts, plus the Siuntos sekimas link
- the rules H2, callout, Visos taisyklės and PDF
- all 4 toggles verbatim, including the 12 prohibited items, the 4 packing rules, the 5 cm note and the 6 fines rows
- the tracking H2, field, error, button and helper
- the reviews placeholder texts (kept in this note; the row is disabled)

Every HEAD link target is still linked, and `/tarptautiniai-pervezimai/` is new. The original site's two hero tiles now map to the „Visas pervežimų grafikas →“ link and the „Tarptautiniai pervežimai →“ link.

Removed as DROP devices: the Raw HTML route H1 and its sr-only keyword sentence (it stays in `<title>`/meta), the docked split-flap board, the rail/rings/crop marks, inline SVG maps with JS, the „01 / 11“ counter and the „Praleisti paslaugų juostą“ skip link of the custom road, the step thumbnail photos (6407553, 1696742 → Icon List numbers), hover videos, and the SD/HD switch.

## Requests for shared (`emul/*`, partials, assets)

1. **Icon List horizontal: titles do not line up (visible on H6 Stations).** `emul/lists-cards.css` l.59: the horizontal `.nectar-icon-list-item` grid is stretched to the row height, and its auto rows share the extra space, so items with shorter text sit lower (Paėmimas / Kelyje / Pristatymas titles at different heights). Fix: add `align-content:start` to `.nectar-icon-list[data-direction="horizontal"] .nectar-icon-list-item`. Salient aligns the items to the top.
2. **Icon List on phones (≤ 690):** the horizontal road line runs through the item title (H6 Stations at 390 px). The line/border should be hidden, or turned into a vertical line, when the list stacks.
3. **`assets/img/marsrutai.svg`:** the legend's last line „SCHEMA · NE MASTELIS“ is at y = 724 in a 720 viewBox, so it is clipped. Move the legend group up (e.g. `translate(660 580)`).
4. **Hotspots on phones (C-7):** at 390 px the 30 px square markers cover the country labels (LIETUVA, LENKIJA, VOKIETIJA). Please add a phone size of about 22 px / 12 px text to C-7.
5. **`{{grafikas:next}}` dates:** please join the number and „d.“ with a no-break space (`28&nbsp;d.`). In the hero glass band (Inner Column 4/12 at 1440) „Atgal iš Airijos – rugsėjo 28 d.“ breaks before „d.“.
6. **`gs-marsrutai`:** the Fancy UL starts right under „3–4 paros kelyje“ with no space. Something like `--mt:18px` on the list, plus a little space before the red call, would help.
7. **Labels in partials:** add `data-salient` to the 19 unlabelled element roots on the built home page.
   - GS-Poraštė (15): 7 page links (including Tarptautiniai), 6 contact links, the © Responsive Text and the Privatumo politika link.
   - GS-Užklausa (4): the Responsive Text and 3 phone HLI rows.
8. **Wave 3:** delete the unused `assets/css/pages/home.css` and `assets/js/pages/home.js`.

9. **Wave 4 (emulation gaps met while fixing the home review, not worked around in shared files):**
   - `interactive.css` l.209: Section Width has presets 35/45/60/75 only, but Salient's slider goes 25–100. Home uses 28 with an inline `--sec-w:28vw` stand-in. A generic mapping would remove it.
   - `lists-cards.css` l.205: cascading layers have no `medium_depth` / `small_depth` shadow rule. The generic `[data-shadow="medium_depth"]` in `grid.css` would paint on the layer box before its image fades in, so home keeps Large Depth.
   - `typography.css` l.80: the outline fallback `currentColor` is transparent. `tarptautiniai-pervezimai.html` l.244 still hard-codes `--outline-color:#1C1D1D` on a page with 4 dark color-change rows (services-routes team).
   - Review suggestion for `src/templates/paslauga.py` `callout()`: give the tone-A callout `data-text-color="light"` and the P callout `"dark"` (service team).

## Open issues

- During the Color Change Section sweep, a chapter head that is under 40 % visible shows its text on the previous chapter's colour for a moment. This is Salient's own behaviour and is documented in kit §10.
- Playwright Chromium cannot play H.264, so the H1/H5 videos show their posters in the screenshots. This is expected.
- The Ireland leg is still unconfirmed. The map (dashed IE leg „maršrutas tikslinamas“), the IE hotspot text and the absence of ferry media all depend on the client's answer.
