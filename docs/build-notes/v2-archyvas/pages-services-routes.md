# Build notes: pages-services-routes

Team: `/pervezimo-paslaugos/` (overview, prefix `ps-`) and `/pervezimo-paslaugos/tarptautiniai-pervezimai/` (routes, prefix `tp-`).
Source of truth: `docs/dizaino-sistema.md` §6.3 and §6.4. Content: `docs/turinys-puslapiai.md` [P] and `docs/turinys-paslaugos.md` [S].

Build and check only these pages:

```bash
python3 tools/build.py pervezimo-paslaugos/index.html pervezimo-paslaugos/tarptautiniai-pervezimai/index.html
python3 tools/check.py pervezimo-paslaugos/index.html pervezimo-paslaugos/tarptautiniai-pervezimai/index.html
```

Status: both pages pass with 0 errors and 0 warnings. A site-wide `check.py` run also reported 0 errors. The page JS passes `node --check`. There is no horizontal overflow and no text below 12 px at 390×844, 768×1024, 1024×768, 1366×657, 1366×768 and 1440×900. Only the 5 allowed `tel:` numbers are used, and each one has a full `aria-label`.

---

## 1. Files

| File | What |
|---|---|
| `src/pages/pervezimo-paslaugos.html` | Overview page. The markup for the 6 group cards was generated once from `src/data/paslaugos.json` (groups, names, `card` summaries, chips, `card_media`, `hover_video`) and pasted in. See REQUEST 2. |
| `src/pages/tarptautiniai-pervezimai.html` | Routes page. |
| `assets/css/pages/paslaugos.css` | Styles for tickets, the group index, group cards, the CTA and 02 Kryptys. Includes responsive and reduced-motion rules. |
| `assets/css/pages/tarptautiniai.css` | Styles for the hero overlay, route list, hotspots, overlapping chapters, route lane, stops, trust rows, the ✕ list, notice cards and service list. |
| `assets/js/pages/paslaugos.js` | Ticket tilt (M67), card media swap on row hover or focus plus SD hover video (M33/M64), group index spy and counter, and anchor jumps that land on the correct card. |
| `assets/js/pages/tarptautiniai.js` | Hotspot layer (sized to the SVG box, disclosure tooltips, Esc), overlapping-chapter pinning and the dimming veil (M65). |
| Generated | `pervezimo-paslaugos/index.html`, `pervezimo-paslaugos/tarptautiniai-pervezimai/index.html` |

## 2. What each page contains and which effects it uses

### /pervezimo-paslaugos/ (§6.3)
1. **Route header.** Photo 36383706 at crop 50% 55%, M80 zoom-out plus parallax, and the H1 word reveal. It has the eyebrow, lead [P], chips, a next-departure line on phones and both LT call buttons.
2. **Three route tickets** (Fancy Box → Parallax Hover Effect, `sgp-ticket-tilt`):
   - Each ticket has notches and a perforation. The ticket body sits on an inner masked layer, so the focus outline is not clipped.
   - **M67 tilt** gives about ±7° rotateX/Y. The background image moves against the tilt and the content layer sits at translateZ.
   - Hover changes: the arrow cell turns red, the title underline draws, and the stub ring fills.
   - Tile 01 plays the SD hover video 13707149 (shared `data-hover-video`).
   - Tile 02 meta is live schedule data from `{{grafikas:ticker limit=1}}`. That variant contains no link, so it can sit inside the ticket link.
   - Reveal stagger is 0/120/240 ms.
3. **01 Visos paslaugos.** Sticky Scroll Pinned Sections → **Stacking** (shared `data-stack`) with a sticky index of the 6 groups:
   - The index has a ring that fills, an odometer-style counter (`01 / 06`), a dashed lane, and jumps that land correctly on sticky cards.
   - **Richest hover system on the site.** When a service row gets hover or focus:
     - the row background tints and the row indents;
     - a red top rule draws in;
     - the number and title turn signal-lit, and the title underline draws;
     - the arrow cell fills red;
     - the card image crossfades to that service's photo with a 1.08 → 1 settle, and a caption chip shows `NN / 11 · <paslauga>`;
     - on 02 Negabaritiniai, 05 Automobiliai and 06 Motociklai, the SD **hover video** fades in over the photo.
   - The card border turns red at 55 % while hovered.
   - Covered cards scale down and darken under an opaque veil (see REQUEST 1).
   - Phones and tablets get a plain stack with the image on top and the index hidden. Desktop viewports shorter than 700 px get a plain stack too.
   - The row closes with a CTA: „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“ and both LT call buttons.
4. **02 Kryptys ir transportas** (paper, rail):
   - A sticky left column holds the waypoint and the H2 [P H5].
   - On the right: the lead [P], image 32821932 with **M66 scroll-scale** (`data-scroll-scale`), paragraphs 2–3 [P] with inline links to Gyvūnų and Keleivių pervežimas, and a datasheet (Kryptys / Taip pat / Kelyje / Įsipareigojimas siuntoms).
5. **GS-Board** (`{{partial:board}}`), then **GS-Arrival** (added automatically).

### /pervezimo-paslaugos/tarptautiniai-pervezimai/ (§6.4)
1. **Route header (video).**
   - Video 13707149: HD on desktop, SD on tablet, poster on phones. It has a pause control.
   - The overlay is lighter, 80 % on the left.
   - The header also has the eyebrow, lead [P], chips, a phone next-line and both LT call buttons.
2. **01 Dviem maršrutais:**
   - The H2 and the intro are from [P]. The two route bullets are verbatim [P]. They are rendered as Horizontal List Items with a border animation and link to `#ispanija` and `#airija`.
   - A datasheet shows Pakeliui / Kelyje.
   - **Image With Hotspots** sits on `{{partial:map-both}}`:
     - 6 markers: PL, DE, BE, FR (numbered) and IE, ES (termini).
     - **M69 pulse**, 2 cycles with a stagger.
     - Tooltips open on hover (fine pointers) and on click or tap, and Esc closes them.
     - The IE tooltip says „Maršrutas tikslinamas“ and shows +353 86 450 3104. The ES tooltip shows +34 602 547 929.
     - Below 700 px the SVG becomes the ordered list from the partial and the markers are hidden.
   - The Ireland transit path is **not invented**. The leg stays dashed as „maršrutas tikslinamas“.
3. **02 Airija / 03 Ispanija.** Sticky Scroll Pinned Sections → **Overlapping** (M65):
   - Each chapter pins once its bottom reaches the viewport bottom, so tall chapters are read in full first. The next chapter then slides over with a shadow edge, and the covered chapter darkens.
   - The chapters are pinned only at ≥1000 px with motion allowed. Otherwise they form a plain stack.
   - Airija background: video 2386447 **SD only**, loaded lazily on desktop, with a pause control. Phones get photo 13568682.
   - Ispanija background: 22033738 at crop 50% 60%, with parallax.
   - Each chapter has:
     - an H2;
     - a **route lane** that draws on enter (LT → PL → DE → dashed „Maršrutas tikslinamas“ → IE, or LT → PL → DE → BE → FR → ES);
     - a tap-to-call timetable from `grafikas.json`;
     - the delivery-facts pair;
     - a primary call button plus a phone list (LT/IE/UK or LT/ES);
     - two insets with **M24 mask reveal** (120 ms stagger), hover zoom, and parallax on the front inset.
   - No ferry media is used (§6.0 and §0.1 #28).
4. **04 Pakeliui.** Verbatim paragraph [P] and four stop tiles on a lane: LENKIJA, VOKIETIJA, BELGIJA, PRANCŪZIJA. The lane draws on enter, the rings fill in sequence, and a hover border animation draws in. The tiles are horizontal on desktop, 2×2 with a vertical lane on tablets, and 1 column on phones. VOKIETIJA and PRANCŪZIJA carry „į Vokietiją ir iš Vokietijos“ and „į Prancūziją ir iš Prancūzijos“, which covers the Germany/France directions from [P].
5. **05 GS-Trust**, „Kodėl verta pasitikėti mumis?“ (paper-100): a sticky H2 and 9 numbered rows with the first clause in bold, a hover rule and an indent. The §6.2 edits are applied.
6. **06 Ko negalima siųsti?** (dark, texture 4040619 with parallax):
   - The H2 and intro are [P].
   - The ✕ list has 8 items with stagger.
   - A sticky „Svarbu“ callout holds both [P] paragraphs.
   - Then come the fine line, the „Visos taisyklės“ button and the PDF link.
7. **07 Ką dar turite žinoti?** Four notice cards: an ink top rule that turns red on hover, a mono index, card 1 = delivery-facts pair, cards 2–4 = verbatim [P].
8. **08 Paslaugos.** `{{paslaugos:list}}` (GS-ServiceList) plus a link to the overview. Then **GS-Arrival**.

The waypoints are numbered 01–08, then Atvykimas. Every row, inner row and component has `data-salient`.

## 3. Typo and grammar fixes (the text is otherwise verbatim)

| # | Where | Live | Now | Basis |
|---|---|---|---|---|
| 1 | Overview, 02 paragraphs 2 and 3 | „į / iš Airiją, į / iš Ispaniją, į / iš Vokietiją, į / iš Prancūziją“ (and the same list in paragraph 3) | „į Airiją ir iš Airijos, į Ispaniją ir iš Ispanijos, į Vokietiją ir iš Vokietijos, į Prancūziją ir iš Prancūzijos“ | §8.2 #3, §6.3 |
| 2 | Overview, 02 lead | „sklandžia kelionę“ | „sklandžią kelionę“ | §8.2 #2 |
| 3 | Overview, 02 lead | „Keleivinių ir siuntų gabenimą reglamentuojančių…“ | „Keleivių ir siuntų gabenimą…“ | **new fix.** „keleivinis“ is an adjective; the meaning is unchanged |
| 4 | Overview, Gyvūnai card lead [S gyvūnų] | „Mikro autobusu“ | „Mikroautobusu“ | §8.2 #2 |
| 5 | Same sentence | „jūsų kiaulytes“ | „jūrų kiaulytes“ | **new fix.** It means guinea pigs; this is an obvious typo |
| 6 | Tarptautiniai, 01 bullet | „iš Lietuvos į Ispanija ir atgal;“ | „…į Ispaniją ir atgal;“ | §8.2 #2 |
| 7 | GS-Trust, bullet 3 | „sako žmogiškųjų“ | „savo žmogiškųjų“ | §6.2 / §8.2 |
| 8 | GS-Trust, bullet 4 | „vykdomi tik naujausiais mikroautobusais“ + „…; DVD – kad kelionė neprailgtų.“ | „tik techniškai tvarkingais mikroautobusais“; the DVD clause is removed and the list ends with „…jaustumėtės patogiai.“ | §6.2 / §8.2 #1 (**client to confirm**) |
| 9 | GS-Trust, bullet 6 | „užtiktiname“ | „užtikriname“ | §8.2 #2 |
| 10 | Tarptautiniai, 06 list | „visus daiktai, kuriuos draudžiama siųsti…“ | „visi daiktai…“ | §8.2 #2 |
| 11 | Tarptautiniai, 07 | „Nepriklausomai nuo to… pristatymas truks apie 3–4 paras nuo paėmimo datos.“ | Replaced by the delivery-facts pair (Kelyje / Įsipareigojimas siuntoms) | §6.4 #7, §8.3 #1 |

Kept verbatim but flagged for the client:
- GS-Trust bullet 7 reads „…vairuotojai, kad kelionė **bus** saugi ir sklandi“. We suggest „būtų“ and did not change it.
- GS-Trust bullet 4 keeps „Siuntos taip pat gabenamos **naujais**, patikimais mikroautobusais“.
- Overview paragraph 3 keeps „vykdomos **naujais**, techniškai tvarkingais, patogiais mikroautobusais“, verbatim per §6.3.

Both „naujais“ phrases fall under §8.2 #1: keep them only if still true.

## 4. New copy for client approval

Strings already on the §8.1 list and reused here are marked (§8.1 #…). Everything else is new.

**/pervezimo-paslaugos/**
- Eyebrow „Tarptautiniai pervežimai mikroautobusais“ (§8.1 #3).
- Hero chips „11 paslaugų“, „2 kryptys“, „Nuo durų iki durų“ (§8.1 #10, #19).
- Ticket lines:
  - „LT ⇄ IE · LT ⇄ ES“ (home meta);
  - „11 paslaugų · 2 kryptys“ (#19);
  - „Artimiausias išvykimas“ (#15);
  - „Siuntos kodas“ and „Pagal siuntos kodą“ (#19).
  - Numbers 01–03.
- Waypoints „Visos paslaugos“ (meta „11 paslaugų“) and „Kryptys ir transportas“. The labels are taken from the blueprint section names.
- Group names (#11). Counts „3 paslaugos“, „2 paslaugos“, „1 paslauga“ (**NEW**). Indices „01 / 06“ … and the counter.
- Hover caption „NN / 11 · <paslaugos pavadinimas>“ (derived from existing names).
- Accessibility label „Paslaugų grupės“ (**NEW**).
- CTA „Nežinote, kurią paslaugą rinktis? Paskambinkite – patarsime.“ (#8).
- Datasheet keys „Kryptys“, „Taip pat“, „Kelyje“, „Įsipareigojimas siuntoms“ (#12, #14).
- Group leads are verbatim [S] sentences:
  - Daiktai: daiktų santrauka;
  - Keleiviai: „Saugumas, operatyvumas, … keleivių vežimo paslaugos.“;
  - Gyvūnai: see fixes 4 and 5;
  - Siuntos: siuntų pristatymo santrauka.

**/…/tarptautiniai-pervezimai/**
- Eyebrow „LT ⇄ IE · LT ⇄ ES“. Chips „2 kryptys“, „Apie 3–4 paros“, „Nuo durų iki durų“.
- Waypoint labels „Dviem maršrutais“, „Airija“, „Ispanija“, „Pakeliui“, „Paslaugos“ (from the blueprint). Also „Kodėl mes“, „Ko negalima siųsti“ and „Ką dar žinoti“ (**NEW**).
- Waypoint metas „2 kryptys“, „LT ⇄ IE“, „LT ⇄ ES“, „4 šalys“ (**NEW**), „Taisyklių 4.5 p.“ and „11 paslaugų“.
- H2 „Keturios šalys pakeliui“ (**NEW**, from the approved #5 „Dvi kryptys. Keturios šalys pakeliui.“).
- Hint „Spauskite žymeklį schemoje“ (**NEW**, shown only when the hotspots are active).
- Hotspot tooltips:
  - „01 · Lenkija“ … „04 · Prancūzija“ + „Pakeliui – galite perduoti siuntą čia gyvenantiems artimiesiems.“ (#16);
  - „Airija · atvykimas“ / „Ispanija · atvykimas“ / „Maršrutas tikslinamas“ (#16).
- Route lanes: country names, codes LT/PL/DE/BE/FR/ES/IE, and „Maršrutas tikslinamas“.
- Stop tiles:
  - „Pakeliui“ and „Pakeliui · kryptis“ (**NEW**);
  - „į Vokietiją ir iš Vokietijos“ and „į Prancūziją ir iš Prancūzijos“ (fragments of the case-fixed [P] text, §8.2 #3).
- Notice card titles:
  - „Pristatymas“ (#12);
  - „Pakavimas“ (#17);
  - „Adresai ir gavėjas“ (#18);
  - „Iškrovimas“ (**NEW**).
- Fine line „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“ (#17). Button „Visos taisyklės“ and the PDF link (#17).
- Link „Visos paslaugos“ (mega menu). Datasheet „Pakeliui — Lenkija, Vokietija, Belgija, Prancūzija“ (#13 caption).
- Meta description per §6.12 (NEW, already listed there).

## 5. REQUESTS for shared files (not applied: page-local workarounds are in place)

1. **`assets/css/components.css` stacking cards.** The stack dims the covered card with opacity. From the 3rd card on, the cards underneath then show through the translucent card, and titles overlap visibly. Replace the opacity with an opaque veil:
   ```css
   .sgp-stack__item>*{position:relative;transform:scale(calc(1 - var(--sp,0) * .06));transform-origin:50% 0}   /* drop the opacity calc */
   .sgp-stack__item>*::after{content:"";position:absolute;inset:0;z-index:6;background:var(--c-asphalt-950);opacity:calc(var(--sp,0) * .6);pointer-events:none}
   @media (max-width:999px),(prefers-reduced-motion:reduce){.sgp-stack__item>*::after{display:none}}
   ```
   Workaround: `.ps-stack .sgp-stack__item>*{opacity:1!important}` plus a `.ps-grp::after` veil.
2. **`tools/build.py`: a `{{paslaugos:groups}}` (and `{{paslaugos:group-index}}`) variant.** It would render the overview group cards from `paslaugos.json`: group media, service rows with `card`, `chips`, swap layers from `card_media`/`card_crop`, and `hover_video` as `data-src`. Without it, the overview duplicates the service summaries. The markup contract is exactly what is in `src/pages/pervezimo-paslaugos.html` (article.sgp-stack__item > .ps-grp …). The swap photo for Keleiviai is 27383867 because its card image equals the group image.
3. **Stacking on short desktops.** A stuck card taller than `100vh - top` hides its last rows for good, because the next card covers them. Proposed shared rule:
   ```css
   @media (min-width:1000px) and (max-height:699px){.sgp-stack__item{position:relative;top:auto}.sgp-stack__item>*{transform:none!important}}
   ```
   Workaround: the same rule scoped to `.ps-stack`, plus compact card rules at a height of 820 px or less.
4. **`assets/js/sgp.js` `data-split` collapses `&nbsp;`.** `/\s+/` matches U+00A0, so „Lietuva&nbsp;– Airija“ cannot keep the dash with the preceding word, and lines start with „–“. Proposal: `el.textContent.replace(/[ \t\r\n]+/g,' ')` and `split(' ')`, so a no-break space stays inside a word. Workaround: the two chapter H2s use `data-reveal` instead of `data-split`.
5. **Spy and anchors for sticky targets.**
   - The IO spy (`rootMargin -45% 0 -50%`) never re-fires on scroll-up when the targets are stacked sticky cards.
   - The document anchor handler measures the stuck position of sticky targets, so jumps back up do nothing.
   - Suggestion: allow `data-spy="scroll"`, meaning "last target whose top < 50 % vh, computed in the rAF loop". For sticky targets, the anchor handler should compute the natural position (the parent's top plus the heights of the previous siblings).
   - Workaround: both are page-local in `paslaugos.js`.
6. **Ticker CSS is global.** `.sgp-tk__list` is styled globally, not as `.sgp-tk .sgp-tk__list`. We reuse `{{grafikas:ticker limit=1}}` as a link-free next-departure line inside a ticket link, because `{{grafikas:next}}` is an `<a>` and cannot sit inside another link. Please either scope the ticker styles, or add a link-free variant such as `{{grafikas:next tag=span}}`. Workaround: scoped overrides in `.ps-tk__m--sched`.
7. **Hover video from a different element.** `[data-hover-video]` needs the `<video>` inside the hovered element. On the overview the hover target (a row) and the media panel are different elements. Suggestion: `data-hover-video-target="<selector>"`. Workaround: page-local loader, gated the same way (fine pointer, ≥1000 px, no reduce, no saveData).
8. **`src/partials/map-both.html`: a stage wrapper around the SVG** (`<div class="sgp-map__stage">…svg…</div>`). A hotspot layer could then be positioned with CSS percentages only. Today `tarptautiniai.js` measures the SVG box on resize and positions the layer. The marker coordinates (`--x/--y` = node x/700, y/500) must be kept in sync if the node coordinates change.

## 6. Known issues and deviations

- **GS-Board is not on /tarptautiniai-pervezimai/.** §6.0 lists it there, but the §6.4 blueprint does not, and both route timetables are already in chapters 02/03. It is one include to add (`{{partial:board}}`) if wanted.
- **No ferry media.** The brief mentions ferry/road media, but the design system excludes all ferry media until the Ireland route is confirmed (§6.0, §0.1 #28, §8.3 #3). Only road and city media are used.
- **Heading levels on the overview.** The outline is chapter H2 → group H3 → service H4. §4.8 describes group H2 and service H3, but the chapter already has its H2 „Visos pervežimo paslaugos“, so everything is shifted one level to keep a single outline. The ticket titles are H2 (on the live site the tiles were H2).
- **Single-service cards** (Keleiviai, Gyvūnai) are sparser. They carry a verbatim [S] lead to fill the space. On desktops with a viewport height of 820 px or less, the leads and chips hide to keep every stuck card within the viewport.
- **Rail inside the pinned Airija chapter.** The shared rail uses a CSS view timeline, so it holds its progress while the chapter is pinned. This is cosmetic and desktop-only.
- **Verification limits.**
  - In the shared Browser pane, pointer hover could not be driven, so the media swap and hover-video paths were checked with synthetic `pointerenter` events. The layer switched and the SD video played (`readyState 4`).
  - Reduced motion was checked by code review, not emulation. Every effect has a reduce path: tilt, pinning, hover video and pulses are off; lanes and rings are drawn; masks are open.
- **The hotspot markers need JS.** Without it the layer stays `hidden` and the schematic, legend and list still work. Markers are hidden below 700 px, where the partial shows its ordered list.

---

**Integration pass (2026-09-23):** all REQUESTS above were resolved in the shared files and the page-local workarounds were removed — see `foundation.md` §11 for the table (only services-routes REQUEST 7, `data-hover-video-target`, was not adopted). Client-facing lists (typo fixes, new copy, content notes) are merged into `docs/turinio-pataisos.md`.

## 7. Review fixes (2026-09-24)

1. **Overview: hidden hover-swap photos no longer download.**
   - Problem: `{{paslaugos:groups}}` (tools/build.py `Services.groups()`) writes one `<img loading="lazy">` per service as an opacity-0 layer. Lazy loading does not skip transparent images, so all 11 layer photos downloaded as the stack scrolled by. Measured at 1440×900 before the fix: 11 of 11 fetched.
   - Fix (page-local, no shared-file change): `paslaugos.css` sets `.ps-grp__layer:not([data-for=""]):not(.is-warm) img{display:none}`. A lazy image with `display:none` is never fetched. `paslaugos.js` `show()` adds `.is-warm` to a layer on the first hover or focus of its row. That starts the fetch. The current photo stays on until the new one has loaded, and then the layers crossfade. If the pointer has moved to another row by then, the late load is ignored. The generated markup contract is unchanged, so `build.py` did not need a `data-src` variant.
   - Result at 1440×900 and 390×844 after a full scroll: 0 extra downloads. The 1 layer counted as "fetched" is Automobiliai, whose layer uses the same URL as its group's base photo. On hover, the swap happened within about 150 ms on first use and instantly from cache.
   - Idle preloading after load was **not** added, because it would bring back the ~1 MB this fix removes.
2. **Routes page: chapter photos on phones and tablets (≤999 px).**
   - Problem: the stacked chapter (about 1300 px tall) was covered by one landscape photo. The Ispanija photo 22033738 was upscaled to a blurry, lighter grey slab.
   - Fix in `tarptautiniai.css`: the section is solid `--c-asphalt-900`. `.tp-ch__media` becomes a top band (`top:0; height:min(82svh,760px)`, parallax transform cleared) that masks into the asphalt. The bright Malaga photo gets an extra `brightness(.7)` so its tone matches Airija. Both chapters get this treatment (Airija uses the 13568682 phone photo).
   - Fix in `src/pages/tarptautiniai-pervezimai.html`: both BG images use `sizes="(min-width:1000px) 100vw, 170vw"`, because a cover band is about 2.5× wider than the viewport. At 390 px, phones now pick w=760 at 1× and w=1600 at 2×, instead of w=480 and w=1100. The upscale is small. Desktop is unchanged. The `data-salient` notes say that the ≤999 px band is custom CSS for the WordPress build.
