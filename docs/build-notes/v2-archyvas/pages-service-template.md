# SGP v2 — build notes: pages-service-template (11 service pages)

Team: **pages-service-template** · Blueprint: `docs/dizaino-sistema.md` §6.5 (+ §4.12, §4.13, §4.17–4.19, §4.26, §5) · Content: `docs/turinys-paslaugos.md` [S], `docs/turinys-puslapiai.md` [P Tarptautiniai].

```bash
# build + check only the 11 services (the prefix "pervezimo-paslaugos/tarptautiniai-pervezimai/" also matches the overview page of another team)
B=pervezimo-paslaugos/tarptautiniai-pervezimai
python3 tools/build.py $B/kroviniu-pervezimas/ $B/negabaritiniu-kroviniu-pervezimas/ $B/daliniu-kroviniu-gabenimas/ $B/daiktu-pervezimas/ \
  $B/automobiliu-pervezimas/ $B/motociklu-pervezimas/ $B/keleiviu-pervezimas/ $B/gyvunu-pervezimas/ $B/siuntu-pervezimas/ \
  $B/siuntu-pristatymas/ $B/perkraustymo-paslaugos/
python3 tools/check.py pervezimo-paslaugos/tarptautiniai-pervezimai/     # 0 errors, 0 warnings (12 pages incl. the overview)
```
Status at hand-off (2026-09-23, second pass): build deterministic (second run „0 changed“), `check.py` full site **21 pages, 0 errors, 0 warnings**, `node --check` OK, `paslauga.py` parses, no console errors (headless Chrome, 390×844 and 1440×900, all 11 pages), `scrollWidth === innerWidth` on every page at 390 and 1440, no text < 12 px, one `<h1>`, every `<section>` in `<main>` has `data-salient`, reduced-motion pass (all `[data-reveal]/[data-split]/[data-mask]` visible, stacking cards un-pinned, no pulses, no parallax). Interaction checks: hotspots 1–4 open by click inside the 390 viewport (12 px margin), Esc closes; checklist ticks update „Pasiruošta 2 / 5“ + live region + bar; submenu spy follows every chapter and clears at the top. Content coverage script: every sentence of [S] „Tekstas (pažodžiui)“ is on its page except the 3 sentences removed on purpose (§4 below).

Second-pass fixes: (1) keleiviai „Principai“ — below 1000 px the page rule `top:calc(--sv-sticky…)` still applied to the now `position:relative` cards and pushed every card 145–200 px down, so the last card („Patogumas“) was covered by the next row; the rule is now desktop-only. (2) Hotspots row on phones/tablets: H2 → photo with markers → list (was photo first, heading below it). (3) Reduced motion: stacking cards become a plain stack (§5.5) — page-local. (4) Submenu: the shared spy kept the last link active after scrolling back to the hero (e.g. „Užklausa“ red at the top) — page JS clears it above the first chapter.

---

## 1. Files

| File | What |
|---|---|
| `src/templates/paslauga.html` | T1 route header (photo, parallax + zoom-out, breadcrumb 4 levels, H1 word reveal, lead, chips, phone-only next departure, compact call ticket) → `{{svc:submenu_html}}` → `{{svc:facts_html}}` → `{{svc:body_html}}` → `{{partial:board}}` → `{{svc:closing_html}}` → T10 „Kita stotelė“ (T11 GS-Arrival is added by the layout). Front matter loads `pages/paslauga.css` + `pages/paslauga.js`. |
| `src/templates/paslauga.py` | render hook (stdlib): `blocks(svc, ctx)` → `submenu_html`, `facts_html`, `body_html`, `closing_html`. Waypoint numbers are counted while rendering, so they always continue down the page. |
| `src/data/paslaugos.json` | content fields of all 11 services (Foundation fields untouched) + top-level `shared.prohibited_p` (the 8 [P] bullets). `_doc` documents the schema. |
| `assets/css/pages/paslauga.css` | page CSS, prefix `sv-` (≈28 KB, tokens + surface vars only). |
| `assets/js/pages/paslauga.js` | page JS (IIFE, `window.SGP` API only, no new scroll listener): form pre-select, sticky media swap, hotspots, checklist, submenu reset above chapter 1. |
| generated | `pervezimo-paslaugos/tarptautiniai-pervezimai/<slug>/index.html` × 11 |

### Data schema (added to each service)
`kv [{k,v}]` · `routes [..]` · `intro [html]` · `steps [{t,d,img,link?}]` (+ `steps_title`) · `why [{b, t, m | img, flag?}]` (b = bold first sentence, t = rest, m = index into `why_media`, img = extra media id) · `specials [{type, place, …}]` · `resp_lead [html]` · `responsibilities [{title, text[]}]` · `prohibited` (`{lead[], items[] | "P", tail, note[]}` | `"P"` | null) · `statement` · `closing` (+ `closing_more`, `closing_marks` = the 2 underlined phrases) · `related [3 slugs]`.
Special types and where they render (`place`): `define`, `video`, `tags`, `bays` → inside T3 („apie“) · `principles` → replaces T4 („why“) · `pack`, `hotspots`, `kvrow`, `checklist`, `price` → own rows after T4 („row“) · `box`, `callout` → T6 sticky column („aside“) · `note` → end of T6 („atsak-end“).

## 2. Page anatomy (Salient mapping is printed by „Salient žymės“)

| Row | Surface | Content | Motion | Salient |
|---|---|---|---|---|
| T1 Route header | dark photo | as §4.17, `data-svc` = service name | M80, M22, M81, M10 | Row Full Width, Parallax Subtle, Slight Zoom Out Reveal |
| T1b Submenu | light glass, sticky | per-service labels → `#apie-paslauga #privalumai #atsakomybes #draudziami #uzklausa` (keleiviai `#principai #patogumai`, gyvūnai `#pries-kelione #kaina`) | M83 (+ follows the header when it hides) | Page Submenu (Sticky) |
| T2 Faktai | paper | `dl.sgp-kv` (first row = Kryptys in display type) + link chips „Kryptys ir paslaugos“ → `?domina=<name>#uzklausa` + „Gauti pasiūlymą“ | M27 (60 ms) | Text Block `.sgp-kv` + Buttons |
| T3 01 Apie paslaugą | paper + rail | sticky H2 + verbatim intro (first paragraph in lead size) · specials „apie“ · „Kaip tai vyksta“ 3 stations | M13, M20, M55, M56 | Column Sticky Content + Text Block; Divider lane + 3 Columns |
| T4 02 Privalumai | dark + rail | sticky media stack (5/12, 78vh) + blocks (bold first sentence as display line, counter „01 / 03“, red progress line) — phones: image above each block | M64, M22 | Sticky Content Sections → Sticky Media, Scrolling Content |
| special rows | varies | see §3 | | |
| T6 Kliento atsakomybės | paper + rail | sticky H2 (+ lead / special) · Toggle Panels (≥ 2, deep links `#atsakomybe-N`) or callout (1) | M60 | Toggle Panels → Minimal Shadow |
| T7 Draudžiami daiktai | dark, texture 4040619 + parallax | H2, service lead, fines teaser, „Visos taisyklės“ · ✕ list (service list or [P] 8 bullets), tail, note | M62 stagger, M27 | Fancy Unordered List + Button |
| (gyvūnai) statement | paper-100 | „Mūsų patirtis rodo…“ + switchboard button | M22 | Text Block + Button |
| T8 GS-Board | dark | `{{partial:board}}` | M14 | Global Section |
| T9 Uždarymas | paper | closing statement with 2 drawn underlines + both LT call buttons · „Susijusios paslaugos“ 3 cards (hover zoom, hover video where the service has one) | M23, M32, M33 | Highlighted Text + Buttons + 3 Column Links |
| T10 Kita stotelė | dark | next service | M82 | Column Link |
| T11 GS-Arrival | dark | form pre-selects this service when there is no `?domina=` | M70–M72 | Global Section |

## 3. Special modules per service

| No | Service | Special(s) |
|---|---|---|
| 01 | Krovinių | row „Esminės krovinių pakavimo taisyklės“ — 4 numbered stops with line glyphs (paper-100) |
| 02 | Negabaritinių | T3: dark definition card + self-hosted video 19552565 (SD, desktop autoplay in view, pause button; poster on phones) |
| 03 | Dalinių | T3: inline SVG van with 3 bays, „your“ bay hatched in signal-ink; draws on enter (outline → bays → hatch → pin) |
| 04 | Daiktų | T3: large outline tags „Langai · Žoliapjovės · Buitinė įranga · Smulkios siuntos“ |
| 05 | Automobilių | T3: cinematic b/w video block 34371915 „Traliuku“ + verbatim sentence (word blur-in), parallax |
| 06 | Motociklų | T3: cinematic video block 34308329 + origin chips |
| 07 | Keleivių | T4 → „Principai“ 5 stacking cards (M63); row „Patogumai“ Image With Hotspots on 36377055 (4 markers, pulse ×2, hover/tap/focus tooltips, linked list, Esc closes, tooltips kept inside the viewport); row „Kokie dar privalumai?“ datasheet |
| 08 | Gyvūnų | row „Prieš kelionę“ documents checklist (Toggle Panels multi + Animated Circle ticks, progress „Pasiruošta N / 5“, per-visitor localStorage in try/catch) + callout „Gavėjas sutartu laiku“; row „Kaina“ (verbatim text + 3 factor tiles); statement before the board |
| 09 | Siuntų pervežimas | T6 aside „Pakavimo gidas“ — SVG box section with the red 5 cm dimension line (draws on enter) |
| 10 | Siuntų pristatymas | the stations lane itself: „Paimame iš siuntėjo → Kelyje apie 3–4 paras → Į rankas gavėjui“ (titled „Nuo durų iki durų“) |
| 11 | Perkraustymo | T6 aside: red-outline callout (pakrovimas / iškrovimas neįeina); end of T6: pets note + „Gyvūnų pervežimas →“ |

## 4. Typo / grammar corrections in [S] text (everything else verbatim)

All of these are in `src/data/paslaugos.json`; the ones marked **§8.2** are already on the design system's approval list, the others are NEW and need the client's „taip / ne“.

| Service | Live text | Demo text | Note |
|---|---|---|---|
| 01 Krovinių | „važiavimas geriausiais parinktas maršrutas“ | „važiavimas geriausiu parinktu maršrutu“ | NEW (case agreement) |
| 01 Krovinių | „nepažeistas dėžės ar kitas pakuotes“ | „nepažeistas dėžes …“ | NEW |
| 01 Krovinių | packing bullets „pakuotei naudokite …;“ | „Pakuotei naudokite ….“ (capital + full stop, each bullet = a numbered stop) | formatting |
| 02 Negabaritinių | „tam tiktų leidimų“ (lead + intro) | „tam tikrų leidimų“ | §8.2 |
| 04 Daiktų | „į / iš Vokietiją, į / iš Prancūziją, į / iš Ispaniją bei į / iš Airiją“ | „į Vokietiją ir iš Vokietijos, į Prancūziją ir iš Prancūzijos, į Ispaniją ir iš Ispanijos bei į Airiją ir iš Airijos“ | §8.2 pattern („šį / iš Airiją“ → „į Airiją ir iš Airijos“) |
| 05 Automobilių | „iš / į Vokietijos“ (2×), „iš / į Airiją“, „iš / į Ispaniją“ | „iš Vokietijos ir į Vokietiją“, „iš Airijos ir į Airiją“, „iš Ispanijos ir į Ispaniją“ | §6.5 („case fix, approval“) |
| 06 Motociklų | „gera kainą“ (lead + intro) | „gera kaina“ | §8.2 |
| 07 Keleivių | „puiki žino“ | „puikiai žino“ | §8.2 |
| 07 Keleivių | „už lanko lepina saulė“ | „už lango lepina saulė“ | NEW |
| 07 Keleivių | „Mūsų transporto priemonių parke – tik nauji (2017–2018 metų) mikroautobusai.“ · „DVD suteiks galimybę …“ · „Klejonė yra puikus būdas …“ | removed | §8.2 #1 (same edits as the /apie-imone/ principles) |
| 08 Gyvūnų | „Mikro autobusu“ / „mikro autobusu“ | „Mikroautobusu“ / „mikroautobusu“ | §8.2 |
| 08 Gyvūnų | „jūsų kiaulytes“ | „jūrų kiaulytes“ | NEW (guinea pigs — obvious slip) |
| 08 Gyvūnų | „tiks geriausius kelius“ | „tik geriausius kelius“ | §8.2 |
| 09 Siuntų pervežimas | „užtikrins sklandžia siuntinio kelionę“ | „sklandžią“ | §8.2 |
| 09 Siuntų pervežimas | „jei aktualu greitos siuntos gabenimas“ | „jei aktualus greitos siuntos gabenimas“ | NEW |
| 09 Siuntų pervežimas | „jei pasitikėsime mūsų komanda ir atsižvelgsite“ | „jei pasitikėsite … ir atsižvelgsite“ | NEW (person agreement) |
| 10 Siuntų pristatymas | „į / iš Vokietiją …“ (2×) | „į Vokietiją ir iš Vokietijos …“ | §8.2 pattern |
| 10 Siuntų pristatymas | „šias tris šalis“ (four are listed) | „šias šalis“ | §6.5 |
| 10 Siuntų pristatymas | „poilsio ir daržo režimo“ | „poilsio ir darbo režimo“ | §8.2 |
| 11 Perkraustymo | „esminiai mūsų veiklos principas“ | „esminiai mūsų veiklos principai“ | §8.2 |
| 11 Perkraustymo | „į / iš Vokietiją, …, ir šį / iš Airiją“ + second „į / iš …“ sentence | case forms as above | §8.2 |
| 11 Perkraustymo | „tik naujais (2017–2018 metų) mikroautobusais“ | „tik naujais mikroautobusais“ | §6.5 / §8.2 #1 |
| 11 Perkraustymo | „teisiai į rankas“ | „tiesiai į rankas“ | §8.2 |
| 11 Perkraustymo | „… vienos ant kitų).“ (stray bracket) | „… vienos ant kitų.“ | NEW |

Structural (no words changed): the prohibited-items sentences of 03 Dalinių („Į šį sąrašą patenka vertingi daiktai, ginklai, …“) and 09 Siuntų pervežimas („Į draudžiamų siųsti daiktų sąrašą yra įtraukti …“) are shown as ✕ lists (lead ends with „:“, items without commas, „ir kt.“ as the tail). Paragraphs are split into blocks at sentence boundaries (intro · why · responsibilities · specials); each sentence appears once.

## 5. Content decisions and deviations from §6.5 (for review)

1. **Complete content rule wins over two §6.5 omissions.** The brief asks for every paragraph, so two paragraphs §6.5 marked „not shown / to confirm“ are on the page but flagged for the WP developer (`data-salient` on the block, visible in „Salient žymės“): 02 Negabaritinių why 03 „Negabaritinių krovinių pervežimas vykdomas tik naujais mikroautobusais.“ (§8.3 #8 vehicle claim) and the „tik naujais / naujais mikroautobusais“ wording everywhere else (§8.2 #1 — keep only if still true). Only the three keleiviai sentences in §4 are removed.
2. **02 Negabaritinių closing** = the page's own final sentence („Negabaritinių krovinių pervežimas Europoje su „SGP pervežimai“ – tik techniškai tvarkingais mikroautobusais, …“), like the other 10 pages; §6.5's „Žinome visus niuansus, todėl drąsiai priimame šiuos iššūkius…“ stays inside why block 01 where it belongs.
3. **Why blocks:** 3–4 per page (every paragraph of the live „Kodėl …“ part), not 2–3; the 4th block reuses the hero or card photo when `why_media` has only 3 images.
4. **01 Krovinių:** „Visi mūsų gabenami kroviniai kelionės metu yra apdrausti.“ moved from the end of the why paragraph to the closing statement (T9).
5. **07 Keleivių:** T4 = „Principai“ stacking cards (media as §6.5), „Patogumai“ hotspots, T6 = „Kokie dar privalumai?“ datasheet (id `privalumai`), T7 omitted. Hotspot labels/descriptions reuse the [P] „Tarptautiniai pervežimai“ fragments (same as the home comfort lane).
6. **08 Gyvūnų:** T7 omitted; the single responsibility („Gavėjas sutartu laiku“) is the callout in the „Prieš kelionę“ sticky column instead of a separate T6 row; statement row before the board.
7. **Added beyond §6.5 (brief: „kaip tai vyksta“ steps, related services):** a 3-station „Kaip tai vyksta“ lane at the end of T3 on every page, and „Susijusios paslaugos“ (3 cards, hover video where the service has one) in T9. Schedule: GS-Board (T8) + the phone-only next-departure line in the hero (§6.5); no per-service ticket stubs, because the schedule has only LT ⇄ IE / LT ⇄ ES and every service runs on both lines.
8. **09 Siuntų pervežimas „Svarbu“ row** uses the full sentence („Siuntos turinys neturi liestis prie pakuotės sienelių – rekomenduojamas tarpas yra 5 centimetrai.“ — condensed from the verbatim sentence) instead of the fragment „rekomenduojamas tarpas yra 5 centimetrai“.
9. **Gyvūnų checklist** stores ticks per visitor in `localStorage` (try/catch; the page works without it) — a demo convenience, production = plain Toggle Panels.

## 6. NEW copy introduced (client approval, §8.1)

**Template labels (all 11 pages):** „Faktai“ · „Kryptys ir paslaugos“ (§6.5) · „Gauti pasiūlymą“ (link to `#uzklausa`) · H2 „Apie paslaugą“ + meta „07 / 11 · Keleivių pervežimas“ · „Kaip tai vyksta“ · waypoint metas „Nuo durų iki durų“ (Privalumai), „Taisyklių 4.5 p.“ (Draudžiami daiktai; was „Taisyklių 4.2 · 4.5 p.“ until the 2026-09-24 review), „4 taisyklės“, „5 principai“, „Salone“, „5 žingsniai“, „Individuali“ · T7 teaser label „Baudos“ + „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“ (§6.5 NEW summary) · „Visos taisyklės“ · callout key „Svarbu“ (with the [P] sentence „Už siuntinio turinį atsakingas siuntėjas.“ on pages that use the shared list) · „Susijusios paslaugos“ · „Visos paslaugos“ · „Kita stotelė · 08“ (§4.19) · video captions = `alt_lt` from media.json + „Pauzė/Paleisti“ · a11y: „Puslapio skyriai“ (submenu), marker labels „1 – Atlenkiamos sėdynės“, checkbox labels „Pažymėti kaip paruoštą: <titulas>“, live text „Pasiruošta N iš 5“.

**Datasheet (T2) values that are condensations, not quotes** (keys per §6.5): 01 „Airija, Ispanija, Vokietija, Prancūzija – ir atgal“ · 02 „Lietuva, Prancūzija, Ispanija, Airija“, „reikia išankstinio planavimo“, „Iškrovimo technika – kliento atsakomybė“ · 03/04/09/10/11 „… – į ir iš“ · 04 „nuo durų iki durų, be perdavimo keliems vežėjams“ · 05 „traliuku apie 3–4 paros“, „sutartu laiku į nurodytą vietą“ · 06 „iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos ir Airijos“ · 07 „nuo durų iki durų: keleiviai paimami iš jiems patogios vietos“ · 09 Svarbu (see §5.8) · 11 „Pakrovimas ir iškrovimas į paslaugą neįeina“ (§6.5).

**„Kaip tai vyksta“ stations (title — line), all NEW condensations of [S]/[P] facts:**
- 01 Paėmimas — „Iš Jūsų nurodytos vietos – nuo durų iki durų.“ · Kelyje apie 3–4 paras — „Skaičiuojama nuo paėmimo dienos. Kroviniai apdrausti.“ · Pristatymas — „Iškrauname, jei tam nereikalinga speciali technika.“
- 02 Paėmimas — (as 01) · Išankstinis planavimas — „Specialūs leidimai ir atitinkama technika.“ · Pristatymas — „Gavėjas sutartu laiku laukia atsiėmimo vietoje.“
- 03 Paėmimas — (as 01) · Kelyje apie 3–4 paras — „Viena transporto priemonė – kelių klientų kroviniai.“ · Pristatymas — „Gavėjas sutartu laiku laukia atsiėmimo vietoje.“
- 04 Paėmimas — (as 01) · Kelyje apie 3–4 paras — „Be perdavimo keliems vežėjams.“ · Pristatymas — „Gavėjui kitoje šalyje.“
- 05 Paėmimas — „Iš nurodytos vietos.“ · Kelyje apie 3–4 paras — „Traliuku – specialiu transportu.“ · Pristatymas — „Sutartu laiku į nurodytą vietą.“
- 06 Paėmimas — „Iš Ispanijos, Prancūzijos, Vokietijos, Lenkijos ar Airijos.“ · Kelyje 3–4 paras — „Skaičiuojama nuo krovinio paėmimo dienos.“ · Pristatymas — „Nuo durų iki durų.“
- 07 Paėmimas — „Iš Jums patogios vietos.“ · Kelyje 3–4 paras — „Atlenkiamos ir šildomos sėdynės, kondicionierius.“ · Pristatymas — „Į Jūsų kelionės tikslą.“
- 08 Paėmimas — „Iš sutartos vietos.“ · Kelyje apie 3–4 paras — „Narvus gyvūnams pervežti turime mes.“ · Pristatymas — „Gavėjui į rankas.“
- 09 Paėmimas — „Iš siuntėjo – nuo durų iki durų.“ · Kelyje apie 3–4 paras — „Siuntos vietą galite pasitikrinti pagal siuntos kodą.“ + link „Siuntos sekimas“ (the live site has the tracking tool) · Pristatymas — „Gavėjui į rankas.“
- 10 (title „Nuo durų iki durų“, §6.5) Paimame iš siuntėjo — „Iš siuntėjo nurodytos vietos.“ · Kelyje apie 3–4 paras — [S] sentence · Į rankas gavėjui — „Gavėjui – tiesiai į rankas.“
- 11 Paėmimas — „Daiktus į mikroautobusą pakrauna klientas.“ · Kelyje apie 3–4 paras — „Nuo krovinio paėmimo iki pristatymo gavėjui.“ · Pristatymas — „Pavyzdžiui, į namus. Iškrovimu pasirūpina klientas.“

**Special modules:** 01 stop titles „Nauja, standi pakuotė · Užpildas ertmėms · Lipni juosta per perimetrą · Adresas matomoje vietoje“, waypoint „Pakavimas“ · 02 „Apibrėžimas“ · 03 „Kaip veikia dalinis krovinys“ (§6.5), legend „Jūsų krovinys / Kitų klientų kroviniai“ · 04 „Pavyzdžiui“ + „Langai · Žoliapjovės · Buitinė įranga · Smulkios siuntos“ (§6.5) · 05 „Traliuku“ · 06 „Vežame iš“ + „Ispanija · Prancūzija · Vokietija · Lenkija · Airija“ · 07 „Principai“, „Patogumai“ + titles „Atlenkiamos sėdynės · Šildomos sėdynės · Kondicionierius · Keleiviai apdrausti“ (§6.1), caption „Iliustracinė nuotrauka“, keys „Kaina · Pažintys · Draudimas · Poilsio režimas“ (§6.5) · 08 „Prieš kelionę“, checklist titles (§6.5), „Pasiruošta 0 / 5“, „Kaina“ + tiles „Narvo dydis · Priežiūros sudėtingumas · Atstumas“ (§6.5) with fragments of the verbatim price sentence · 09 „Pakavimo gidas“ (§6.5), SVG labels „Pakuotė · Turinys · Užpildas“, „5 cm“ · 11 note key „Augintiniai“ + link „Gyvūnų pervežimas“.

**Responsibility titles** (texts verbatim): 01 „Atsakomybė už pakuotę · Iškrovimas · Tranzito šalių teisės aktai“ · 02 „Gavėjas sutartu laiku · Iškrovimas“ · 03 „Pakavimas ir adresai · Gavėjas sutartu laiku“ · 04 „Pakavimas“ · 05 „Pristatymas sutartu laiku“ · 06 „Adresai ir gavėjas“ · 08 „Gavėjas sutartu laiku“ · 09 „Turinys · Pakuotė“ · 10 „Turinys ir pakuotė“ · 11 „Pakavimas · Gavėjas sutartu laiku“ (all from §6.5).

## 7. REQUESTS for shared files (not edited — page-local workarounds are in place)

1. **REQUEST: `assets/css/motion.css` — reduced motion must un-pin stacking cards (§5.5).** What: inside `@media (prefers-reduced-motion:reduce)` add `.sgp-stack__item{position:relative;top:auto}`. Why: today only the scale/dim is removed, cards stay pinned. Workaround: `paslauga.css` (reduced-motion block) sets it for `.sv-princ`. Same as pages-about-contact REQUEST 1.
2. **REQUEST: `assets/js/sgp.js` §13 scroll spy — clear the active link above the first chapter.** What: the IO callback only reacts to `isIntersecting`, so after scrolling back to the hero the last link (often „Užklausa“) stays `aria-current`. Proposed code:
   ```js
   const io = new IntersectionObserver(es => es.forEach(e => {
     if (e.isIntersecting) setActive(e.target.id);
     else if (e.target === targets[0] && e.boundingClientRect.top > 0) setActive(null);   // scrolled back above chapter 1
   }), { rootMargin: '-45% 0px -50% 0px' });
   ```
   (`setActive(null)` then removes `aria-current`/`.is-active` everywhere.) Workaround: `paslauga.js` §5 clears the submenu in `SGP.onFrame` while the first chapter is below the spy band.
3. **REQUEST: `tools/build.py` — pass the top-level JSON to the service hook.** What: add `'shared': data.get('shared', {})` (or the whole `paslaugos.json` dict) to the `ctx` of `hook.blocks()`. Why: the 8 shared prohibited bullets live in `paslaugos.json → shared.prohibited_p`; the hook currently re-reads the file (`_shared()` fallback in `paslauga.py`, keeps working either way).
4. **REQUEST (nice to have): `assets/css/components.css` `.sgp-stack__item` top offset.** What: set `top` only inside `@media (min-width:1000px)` next to `position:sticky`. Why: any page that overrides `top` for its own sticky offset (as the services do, to sit below the page submenu) silently shifts the cards when the <1000 rule turns them `position:relative` — the bug fixed in this pass.

## 8. Known issues / open points

- **Client decisions pending:** vehicle claims („tik naujais mikroautobusais“, §8.2 #1 / §8.3 #8), the NEW typo fixes in §4, and all NEW copy in §6. Prices are never shown (none exist on the live site).
- **Videos** (02 define video 19552565, 05 34371915, 06 34308329, hover video on related cards) play only on desktop (≥1000 px, fine pointer for hover, no Save-Data); phones get the poster image — by design (§7.3). Pexels SD files are used via `{{bgvideo|sd-only}}`; production should self-host graded, trimmed files.
- **Headless full-page screenshots** show a strip without image at the top of parallax layers (T7 texture, cinematic video blocks) because the layer is translated for a scroll position far away; in a real scroll the 12 % bleed covers the offset (scripted scroll through every T7 and cinematic row at 1440×900 and 1366×657: 0 px uncovered).
- **Hotspot coordinates** (36377055) are hand-placed on the demo photo; the real interior photo in production needs new `x/y` values in `paslaugos.json` (or Salient Image With Hotspots positions).
- **Gyvūnų checklist ticks** persist per browser (`localStorage`); private windows / blocked storage just start at 0.
- The overview page `pervezimo-paslaugos/tarptautiniai-pervezimai/index.html` matches the same build prefix — always build the services with the 11 explicit prefixes above so the other team's page is not rebuilt mid-edit.

---

**Integration pass (2026-09-23):** all REQUESTS above were resolved in the shared files and the page-local workarounds were removed — see `foundation.md` §11 for the table (only services-routes REQUEST 7, `data-hover-video-target`, was not adopted). Client-facing lists (typo fixes, new copy, content notes) are merged into `docs/turinio-pataisos.md`.

**Review fixes (2026-09-24):**
- T7 waypoint meta „Taisyklių 4.2 · 4.5 p.“ → „Taisyklių 4.5 p.“ (`paslauga.py` `prohibited()`, 9 pages): the lists are the service's own / the Tarptautiniai 8-item list, not the rules 4.2 list; now matches /tarptautiniai-pervezimai/ #06 and the 1200 EUR fines teaser. `turinio-pataisos.md` §2.5 updated.
- Meta descriptions (`paslaugos.json`): wrong live domain fixed in 03 Dalinių, 08 Gyvūnų („SGP pervežimai siūlo…“), 09 Siuntų pervežimas, 10 Siuntų pristatymas → „sgp-pervezimai.lt“ (as footer / Taisyklių 6.2 / privacy). Client doc: `turinio-pataisos.md` #72.
- 07 Keleivių „Patogumai“ 4th hotspot description → „kelionės metu visi keleiviai yra apdrausti“ (lowercase, no period, like the other three; words unchanged). Client doc: #73.
- „Principai“ stacking cards (`sp_principles` + `paslauga.css`): Apie įmonę `.ab-card` structure — index row (ring · no · drawn hairline · „04 / 05“, `aria-hidden`) at the top → H3 → text → 5-ring progress lane at the bottom (`aria-hidden`), so a covered card's strip shows its index row and title instead of empty panel. Min-height `min(520px, 100vh − --sv-sticky − 120px)`; tighter type ≤900 px tall (`.9375rem/1.52`, smaller paddings) so the tallest card (04 Komfortas) fits under its sticky top — measured (headless Chromium, fonts loaded) bottom of every card ≤ viewport at 1000×700 (card 04: 186 + 482 = 668), 1000×760, 1000×800, 1280×800, 1440×900, 1920×1080; pinning kept from the shared 1000×700 threshold. No new visible copy.
- 09 „Pakavimo gidas“ SVG: labels 12 → 16 viewBox units (`letter-spacing .04em`), box moved left (x 30 → 14, 240 → 224 wide, leaders end at x 250) so „UŽPILDAS“ ends ≥19 px inside the figure; rendered label size 13.2 px at 360 px, 14.6 px at 390, 14.2 px at 1024, 18.2 px at 1440 (§2.3 ≥12 px); „5 cm“ 16.6 px+. No horizontal overflow.
