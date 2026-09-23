# SGP v2 — build notes: team „pages-schedule-tracking-rules“

Pages: **/pervezimu-grafikas/** (§6.6) · **/siuntos-sekimas/** (§6.7) · **/taisykles/** (§6.8).
Build/check: `python3 tools/build.py pervezimu-grafikas siuntos-sekimas taisykles && python3 tools/check.py pervezimu-grafikas siuntos-sekimas taisykles` → 0 errors, 0 warnings. `node --check` passes for all three page scripts.

QA done (headless Chrome, not the shared browser pane): 390×844, 768×1024, 1366×657, 1440×900 → horizontal overflow 0 on every page, no rendered text < 12 px, no console errors; reduced-motion full-page pass; only the 5 allowed `tel:` numbers, each with `aria-label`; every `main > section` has `data-salient` (overlay prints 20 / 16 / 24 tags); tracking page makes **no request** to `siuntos.sgp-pervezimai.lt`; schedule tested with `?siandien=2026-10-15` and `?siandien=2026-11-30` (empty state).

---

## 1. Files

| File | What |
|---|---|
| `src/pages/pervezimu-grafikas.html` | compact texture header · 01 Lenta (Tabs Minimal „Visi · Airija · Ispanija“ → 3 × `{{grafikas:table}}`) · 02 Laiko juosta (lane chart) · 03 Ką verta žinoti (kv + `{{partial:map-both}}`) · GS-Arrival |
| `assets/css/pages/grafikas.css` | `gr-` classes: board head/tabs, column header row, table re-scoping, flap route codes, row stagger on tab switch, lane chart, facts grid |
| `assets/js/pages/grafikas.js` | route codes → split-flap tiles (M14, desktop, once per tab) · lane chart rendered from `SGP.schedule` (visitor's today, same data as the table) + label collision/edge layout |
| `src/pages/siuntos-sekimas.html` | compact photo header · 01 Paieška (large `.sgp-track` field) · 02 Rezultatas (framed map-paper „screen“ with demo states) · 03 Pagalba (both LT call buttons + 3 link cards) · GS-Arrival |
| `assets/css/pages/sekimas.css` | `sk-` classes: form sizing, demo line, screen frame + crop marks, idle/load/none/found states, trip lane (horizontal ≥700, vertical below), log, help head |
| `assets/js/pages/sekimas.js` | demo tracking state machine (no network): empty → „Neįvestas siuntos kodas!“ · any code except `SGP-DEMO` → „Toks siuntos kodas neegzistuoja!“ · `SGP-DEMO` → demo result · reads `?kodas=` on load, writes it back with `replaceState` |
| `src/pages/taisykles.html` | route header (PDF button, jump chips) · 01–06 all six rule sections verbatim (sticky lane index + clauses) · PDF again · GS-Board · GS-Arrival |
| `assets/css/pages/taisykles.css` | `tr-` classes: sticky lane index, outlined section numerals (fill when active), clauses, 3.4 key box, 4.2 dark prohibited panel, 4.5 odometer + fines table + toggle, 5.1 deadline lane, 6.1 „1)“ numbering, end card, phone layout |
| `assets/js/pages/taisykles.js` | index lane fills stop-to-stop with reading progress, passed stops marked (`data-spy` from sgp.js sets the active one) · ✕-list stagger indexes |
| `docs/build-notes/pages-schedule-tracking-rules.md` | this file |

Anchors other pages may link to: `taisykles/#tikrinimas`, `#siuntejo-garantija`, `#vezejo-atsakomybe`, `#draudziami-daiktai`, `#draudziama-siusti` (4.2 list), `#baudos` (4.5), `#visas-4-5` (opens the full 4.5 toggle), `#pretenzijos`, `#atsakomybes-ribos`, every clause `#p2-1 … #p6-2`; `pervezimu-grafikas/#lenta`, `#visi` / `#airija` / `#ispanija` (tab deep links), `#laiko-juosta`, `#ka-verta-zinoti`; `siuntos-sekimas/?kodas=…`, `#paieska`, `#rezultatas`, `#pagalba`.

## 2. Effects used (all from the shared motion system unless noted; every one has a reduced-motion end state)

- **All pages:** inner-hero zoom-out + parallax Subtle (M80/M10, `data-parallax`), breadcrumb draw (M81), H1/H2 word reveal (`data-split`, M22), fade-ups with staggers (`data-reveal`, `data-stagger`, M13/M27), rail draw + waypoint rings (`sgp-has-rail`, M20/M21), call-button / link / card hovers (M84–M86, M32/M44), GS-Arrival tickets + form.
- **Grafikas:** Tabs Minimal (M40) with a page-owned row stagger on tab switch · split-flap on the route codes only (M14 — desktop, once per tab, never phone numbers) · table row hover lane + phone icon tilt (M45) · **lane chart** (page-owned): lanes draw, rings arrive as the lane passes them, soonest ring pulses 2× (M15-like), row focus-dim on hover · map-both trunk/branch draw (M41/M42).
- **Sekimas:** idle „how it works“ lane draws on enter (M55-like) · one-shot scan while „Ieškoma…“ (0.9 s) · not-found lane breaks into a dashed segment ending in a neutral „?“ ring (404 idea) · found: trip lane fills to the current stop, stops fade in, current ring pulses 2×, log staggers · card image mask reveal (M24) + hover (M32).
- **Taisyklės:** sticky index = Vertical Sticky Scrolling emulation (M61/M83): rings fill as sections are reached, red lane fills stop-to-stop with reading progress (page JS), outlined numerals fill for the active section · `<mark class="sgp-mark">` underline draw on „5 darbo dienas“, „per 5 dienas“, „per 14 dienų“ (M23) · 4.2 ✕ list stagger (M62-like) · „1200“ odometer (M26) · accordion toggle (M60) · 5.1 deadline lane draws + rings pop.

## 3. Typo / formatting corrections (text otherwise verbatim)

Taisyklės (legal text — **client must approve**, most are already in §8.2):
1. 1.: „pačiam Siuntėj**au** nedalyvaujant“ → „Siuntėj**ui**“ (§8.2 #2).
2. 2.2: „dėlto“ → „dėl to“ (§8.2 #2).
3. Section headings: trailing colons dropped („1. Siuntų tikrinimas:“ → „Siuntų tikrinimas“); 4: „Daiktai kuriuos…“ → „Daiktai**,** kuriuos įmonė vežti atsisako“ (missing comma).
4. 4.2: „šaunamiejii“ → „šaunamieji“ (§8.2); missing „;“ after item 9 „degios prekės“ added; item 12 „Visos kitos…“ → „visos kitos…“ (list style, same as the home digest). The list keeps the original „;“ endings; numbers render as 01–12.
5. 4.5: „grąžinam**ą**“ → „grąžinam**a**“ (§8.2); „3) atlyginęs visus kitus…“ → „3) atlyginti visus kitus…“ (grammar, **not in §8.2 — new, needs approval**); „( ampolę, tabletę )“ → „(ampulę, tabletę)“; „cigarecių“ ×2 → „cigarečių“ (§8.2); „(200vnt.)“ → „(200 vnt.)“; „1200EUR“ → „1200 EUR“; „200g“ → „200 g“; stray „•“ bullets removed — the five fine sentences are shown as a list (words unchanged; „ir kita...“ kept). Fines table keys adapted exactly as the Foundation home digest (§6.8).
6. 6.1: „apibrėdžia“ → „apibrėžia“; „baikotai“ → „boikotai“ (§8.2); „maišrai“ → „maištai“ (§8.2); „kokos“ → „kokios“ (§8.2); „Lietuvos respublikos“ → „Lietuvos Respublikos“; enumerations 1)–8) shown as a list with the original „1)“ numbering, items 6) „Muitinės“ → „muitinės“ and 8) „Kitos“ → „kitos“ (list style; „Siuntėjo“ keeps its capital — defined term).
7. 6.2: „http://sgppervezimai.lt“ → „https://www.sgp-pervezimai.lt“ (§8.2 #6).

Siuntos sekimas: the live band said „Pervežimo paslaugos“ → H1 „Siuntos sekimas“ (§8.2 #7). Tool messages kept verbatim („Neįvestas siuntos kodas!“, „Toks siuntos kodas neegzistuoja!“, placeholder „Siuntos kodas...“, button „Siuntos lokacija“).
Pervežimų grafikas: only live strings are „Pervežimų grafikas“ and „Artimiausi pervežimai“; dates come from `grafikas.json` (Foundation format).

## 4. NEW copy (for client approval, §8)

**Pervežimų grafikas**
- Eyebrow „LT ⇄ IE · LT ⇄ ES“ (reused Arrival meta). Waypoints „01 Lenta“ (meta „4 kryptys“), „02 Laiko juosta“ (meta „Nuo šiandien“), „03 Ką verta žinoti“ (meta „Apie 3–4 paros“).
- Table column labels „Maršrutas · Išvykimo datos · Būsena · Skambinti“. Tabs „Visi · Airija · Ispanija“ (§8.1 #15).
- 02: H2 „Visi išvykimai vienoje juostoje“; lead „Kiekviena stotelė – išvykimo diena. Juosta prasideda šiandien ir baigiasi paskutine grafike paskelbta data.“; axis „Šiandien“, „po 7 d.“, „po 14 d.“ …; legend „Artimiausias · Kitas išvykimas kryptimi · Vėliau · Šiandien“.
- 03: H2 „Laiką ir vietą suderinsime telefonu“ (from the board note); kv keys „Išvykimo laikas ir vieta“, „Principas“, „Kelyje“, „Įsipareigojimas siuntoms“ (§8.1 #12/#14); links „Siuntos sekimas“, „Siuntų siuntimo taisyklės“.

**Siuntos sekimas**
- Eyebrow „Pagal siuntos kodą“ (§8.1 #19); lead „Įveskite siuntos kodą ir sužinokite, kur yra Jūsų siunta.“ (first sentence of the NEW meta, §6.12).
- Waypoints „01 Paieška“, „02 Rezultatas“ (meta „Demonstracinė versija“), „03 Pagalba“. H2 „Kur keliauja Jūsų siunta?“; body „Siuntos vietą galite pasitikrinti pagal siuntos kodą.“ (§8.1 #7).
- Help line „Neradote siuntos kodo? Paskambinkite – pasakysime, kur Jūsų siunta.“ + „Skambinti“ (§8.1 #19); H2 „Neradote siuntos kodo?“ (§8.1 #19).
- Result screen: „Siuntos kodas:“, idle steps „Įveskite siuntos kodą“ · „Spauskite „Siuntos lokacija““ · „Matysite, kur yra Jūsų siunta“, „Ieškoma…“.
- Demo-only (removed in production): badge „Demo“, „Demonstracinė versija – paieška veikia tik tikroje svetainėje.“ (§8.1 #25), try button „Išbandykite: SGP-DEMO →“ (own row under the demo sentence; was an inline chip „Išbandykite kodą SGP-DEMO“); not-found state repeats „Demo“ + „Demonstracinė versija – paieška veikia tik tikroje svetainėje.“ directly under „Toks siuntos kodas neegzistuoja!“ (also in the screen-reader announcement); found state „Demonstracinis pavyzdys · ne tikra siunta“, „Kelyje“, stop notes „išvykimas / siunta čia / atvykimas“, log „Paimta iš siuntėjo – Siunta paimta iš siuntėjo nurodytos vietos.“, „Kelyje – Siunta keliauja Ispanijos link.“, „Pristatymas – Pristatome gavėjui tiesiai į rankas.“ (§8.1 #7), kv keys „Siuntos kodas“, „Kryptis“, note „Tikroje svetainėje čia bus rodoma siuntos vieta žemėlapyje iš siuntų sistemos.“, screen-reader status „Siunta rasta – demonstracinis pavyzdys: Lietuva → Ispanija, kelyje.“ The demo parcel's position (Prancūzija on the Spain route) is an illustration, clearly labelled.
- Cards: labels „Paslauga“, „Grafikas“, „Taisyklės“; texts „Artimiausios išvykimo datos abiem kryptimis.“ (§8.1 #15) and „Tikrinimas, siuntėjo garantija, vežėjo atsakomybė, draudžiami daiktai, baudos ir pretenzijos.“ (from the NEW meta).

**Taisyklės**
- Eyebrow „Taisyklės · 1–6 skyriai“; jump chips „Draudžiama siųsti (12)“, „Baudos“ (§8.1 #17), „Pretenzijos“; aria „Greitos nuorodos“, „Taisyklių skyriai“.
- Waypoint „01–06 Taisyklės“ (meta „Taisyklių tekstas“); index label „Turinys“.
- 4.2 panel label „Draudžiama siųsti (12)“. (The callout „Svarbu – Už siuntinio turinį atsakingas siuntėjas.“ from Tarptautiniai pervežimai was removed from the 4.2 box in the review pass — the rules page shows the contract text only; 2.2 and 4.4 already cover sender responsibility.)
- 4.5: „1200 EUR“ + „Radus draudžiamų daiktų – 1200 EUR bauda (Taisyklių 4.5 p.)“, fines table, toggle „Visas 4.5 punkto tekstas“ (all §8.1 #17). 3.4 delivery-facts pair (§8.1 #14).
- 5.1 lane labels „0 d. – Siuntos gavimo diena“, „5 d. – Pranešti Vežėjui apie nuostolius ar žalą“, „14 d. – Patvirtinti tai raštu“ (paraphrase of 5.1 — the clause itself stays verbatim beside it).
- End card „Sutartis su siuntėju · PDF · 72 KB“, link „Į turinį“. PDF link = the live file (`{{url:pdf}}`, external, `rel="noopener"`).

## 5. Deviations from the blueprint (and why)

1. **Grafikas 02 „Ką verta žinoti“ does not repeat the two ticket cards** — GS-Arrival (auto, directly below) already shows both tickets with next-departure stubs; duplicating them 1 screen apart looked like a bug. Added instead: the **lane chart** (NEW, optional row — needs `[sgp_grafikas variant="lane"]`, disable the row if not wanted; the table holds the same data) and the both-routes schematic next to the kv.
2. **Grafikas hero** has no photo per §6.6 (texture 9807331 at 18 %); the Lenta row's top padding is reduced so the table follows the header closely („the table is the hero“).
3. **Sekimas result** is a state machine (idle / load / not found / demo found) instead of the static „two messages“ card, so the client can click through the real messages. Nothing is requested; production swaps the states for the iframe (data-salient says so).
4. **Sekimas 03 Pagalba**: call block (both LT numbers) as the section head + three link cards (Siuntų pristatymas, **Pervežimų grafikas** (added), Taisyklės) instead of three small cards with one call card.
5. **Taisyklės „Tabs → Vertical Sticky Scrolling“** is emulated as a sticky lane index + all six sections in the reading flow (better for long legal text, search and print; Salient's element behaves the same way on scroll). Below 1000 px the index becomes a static „Turinys“ box. Hero chips are hidden ≤690 px (the contents box follows immediately) so the call buttons stay near the first screen.
6. Taisyklės 4.5 shows a large „1200 EUR“ odometer above the fines table (emphasis requested in the brief); the full 4.5 text stays complete inside the toggle.
7. Map-both on /pervezimu-grafikas/ sits beside the kv only ≥1280 px; below that it stacks (its 15-unit SVG labels would fall under 12 px in a narrower column).

## 6. REQUESTS for shared files (not edited by this team)

1. **REQUEST: `tools/build.py` + `assets/js/sgp.js` (schedule) — optional `lane` variant.** What: move the lane chart markup from `assets/js/pages/grafikas.js` into `Schedule.lane()` / `V.lane()` (`<figure class="gr-lane" data-sched="lane">…</figure>`, same markup the page JS builds: axis ticks every 7 days up to `max(21, ceil((lastDiff+4)/7)*7)` days; per route a row with stops `is-next` / `is-soon`). Why: static/no-JS output + parity with the planned PHP shortcode. Until then the page renders it client-side and hides the row without JS. Only if the client approves the row.
2. **REQUEST: `tools/build.py` table variant + `sgp.js V.table` — flap-ready route codes.** What: output `<span class="sgp-mono sgp-flap" data-flap>LT → IE</span>` inside `.sgp-sched__name` (and let `observeReveal` skip `[data-flap]` inside `[role=tabpanel][hidden]`). Why: §6.6 asks for M14 on route codes; today `grafikas.js` flapifies them after sgp.js' re-render (safe because the re-render happens once, before page scripts), which is post-processing the foundation notes discourage.
3. **REQUEST: `assets/js/sgp.js` §14 tracking — page hook.** What: before navigating, dispatch a cancelable `sgp:track` event (`detail:{code}`) on the form; if a page calls `preventDefault()`, sgp.js stays out. Also expose the error setter (`SGP.track.error(form,msg)`) so pages can show „Toks siuntos kodas neegzistuoja!“ without rewriting the shared `<em>`. Why: `sekimas.js` currently relies on listener order (sgp.js' empty-check listener runs first) and swaps the `<em>` text itself. Proposed code: `const ev=new CustomEvent('sgp:track',{cancelable:true,detail:{code:i.value.trim()}}); if(!form.dispatchEvent(ev)) e.preventDefault();`.
4. **REQUEST: `assets/css/motion.css` odometer.** What: `.sgp-reel>span{align-items:center}` + `.sgp-reel{font-variant-numeric:tabular-nums}` (or measure the final digit and set the reel width). Why: each reel column is as wide as its widest digit, so a narrow „1“ leaves a gap („1 200“ here, „1 1“ on the home stats). Page-local workaround in `taisykles.css` (right-align the first reel, −0.19em).
5. **REQUEST: `assets/css/components.css` `.sgp-clause`.** What: allow a `<div class="sgp-clause__t">` with several `<p>`/`<ol>` (`.sgp-clause__t p+p,.sgp-clause__t p+ol{margin-top:12px}`) and stack number above text ≤560 px (`grid-template-columns:1fr`). Why: long legal clauses (6.1) read in a ~270 px column on phones. Page-local in `taisykles.css`.
6. **REQUEST: `docs/build-notes/foundation.md` §4.16 note.** What: „`{{partial:map-*}}` needs a figure ≥ ~600 px wide (≥ 12 px labels); stack it in columns narrower than that.“ Why: at 1000–1279 px in a 6/12 column the labels drop to 8–11 px.

## 7. Known issues / open points

- **Year/weekday:** the lane chart uses day offsets only (no weekday, no year) — consistent with §6.0; the dates themselves still carry the „client to confirm the year“ caveat from Foundation.
- **No-JS:** lane row hidden; flap tiles show as plain mono codes; tracking form submits `?kodas=` to itself and shows the idle screen (production: iframe works without our JS).
- **Demo tracking:** any code except `SGP-DEMO` returns „Toks siuntos kodas neegzistuoja!“ — by design, always shown together with the demo note „Demonstracinė versija – paieška veikia tik tikroje svetainėje.“ (§6.7) so a real code is never presented as non-existent; the real lookup lives in the siuntų sistema (Laravel, UAB GP Soft). The success view of the real tool was never observed (§ turinys) — the demo „found“ layout is our proposal for the iframe's surroundings, not a copy of the tool.
- **PDF:** links to the live download URL (attachment, 72 KB); its content was not reviewed (same as §6.8).
- **Salient reproduction cost:** grafikas lane chart (optional shortcode variant), flap on codes (custom JS ≈0.8 KB, already in the inventory), taisyklės index progress lane (≈1 KB custom JS; without it the native Vertical Sticky Scrolling tabs still work), sekimas demo states (demo only).
- Environment note for the orchestrator: the Browser pane and the session scratchpad are shared by parallel agents (tabs and scratch scripts were overwritten); this team used headless Chrome from `scratchpad/sst/` for QA.

---

**Integration pass (2026-09-23):** all REQUESTS above were resolved in the shared files and the page-local workarounds were removed — see `foundation.md` §11 for the table (only services-routes REQUEST 7, `data-hover-video-target`, was not adopted). Client-facing lists (typo fixes, new copy, content notes) are merged into `docs/turinio-pataisos.md`.

**Review fix pass (2026-09-24):**
- Sekimas: not-found card now carries the approved demo note (§6.7 / §8.1 #25) under the verbatim tool message; the live-region text includes it too.
- Sekimas: the dashed inline `SGP-DEMO` chip (negative margins, broke onto its own line at 1440 and 390) replaced by a small line button on its own row „Išbandykite: SGP-DEMO →“ (34 px visual, `::after` extends the hit area to 44 px). New copy: „Išbandykite:“ (demo only).
- Taisyklės: callout „Svarbu – Už siuntinio turinį atsakingas siuntėjas.“ removed from the dark 4.2 clause box (not part of the contract text); `.tr-ban__callout` CSS removed.
