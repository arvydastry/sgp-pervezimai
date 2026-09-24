# SGP v2 — build notes · team „pages-about-contact“

Pages: **/apie-imone/** (§6.2) · **/kontaktai/** (§6.9) · **/privatumo-politika/** (§6.10) · **/404.html** (§6.11).
Built only with `python3 tools/build.py apie-imone kontaktai privatumo-politika 404`; `python3 tools/check.py` → 21 pages, 0 errors, 0 warnings (at hand-off).
QA run with headless Chrome (puppeteer-core) at 360, 390, 768, 1000, 1024, 1280, 1366×657, 1440×900 and 1920: no horizontal overflow, no text < 12 px (Appendix D snippet 2), no tap target < 44 px in `main`, no console errors, reduced-motion pass, keyboard (tabs/links/form/radios) pass. Forms: no non-GET requests.

---

## 1. Files

| File | What |
|---|---|
| `src/pages/apie-imone.html` | Route header → 01 Įmonė → 02 Principai (stacking cards) → 03 Kelyje (Flickity gallery) → 04 GS-Trust → GS-Board → GS-Arrival (auto) |
| `src/pages/kontaktai.html` | Plain header with rail terminus + chapter index → 01 Skambinkite (switchboard tickets, all 5 numbers, e-mail + copy) → 02 Grafikas (timetable, 4 routes) → 03 Parašykite (demo contact form) → 04 Kur važiuojame (map, both routes). GS-Arrival hidden |
| `src/pages/privatumo-politika.html` | Plain header → document: sticky mini-TOC (2 stops, progress lane) + „Informacija ruošiama...“ + demo notice + clearly marked placeholder for the GDPR text + cookie table + „Keisti slapukų nustatymus“. GS-Arrival hidden |
| `src/pages/404.html` | Refined Foundation 404: full-height hero (rail comes down → dashed break → neutral ring; flap „4 0 4“), GS-Board, GS-ServiceList. Absolute root kept (`/sgp-pervezimai/`) |
| `assets/css/pages/apie.css` · `assets/js/pages/apie.js` | `ab-` · Flickity gallery (counter, image parallax, drag indicator, scroll-snap fallback) |
| `assets/css/pages/kontaktai.css` · `assets/js/pages/kontaktai.js` | `kt-` · header lane → terminus ring; route choice lights the matching phone row + pre-fills „Žinutės tema“ |
| `assets/css/pages/privatumo-politika.css` · `assets/js/pages/privatumo-politika.js` | `pp-` · reading-progress lane in the TOC; re-open cookie bar |
| `assets/css/pages/404.css` · `assets/js/pages/404.js` | `e4-` · „wrong turn“ lane (desktop) / mini route (phones) |

Front matter: apie uses `vendor: flickity`; every page declares its own `css:`/`js:`. No shared file was edited.

## 2. Effects used (all from the shared motion system unless marked *page*)

- **Apie:** M80 hero zoom-out + parallax; M22 word reveals; M23 underline draw on both routes; *page* mini-route (ring → lane → ring fills) under „Mes visada pasiruošę…“; M26 odometer stats + red km-marker hover; M61 sticky datasheet; **M63 stacking cards** (5 principles, 4:5 image right, *page* progress rings 01→05, *page* opaque dimming overlay instead of opacity — see REQUEST 3); **M68 Flickity gallery** (*page*: wrapAround, Touch & Total „01 / 05“, drag-driven image parallax ±12 %, Mask Edges, non-selected cells scale .94 + veil, custom drag indicator „Tempkite“ on fine pointers); GS-Trust rows = rail stops (`data-stops`: rings fill and the lane segment draws as each row passes 70 %), M45 row hover (indent + red rule draws), mask-reveal portrait with inner parallax, texture row with parallax; GS-Board flap.
- **Kontaktai:** *page* rail terminus — the lane draws down from under the header and the 22 px terminus ring fills with a halo (this page is the arrival); chapter index as stops (hover: ring fills, arrow turns down); ticket hover lift + perforation turns red (M70); 92 px / 64 px call rows with icon inversion (M86-like); copy e-mail (M73); tap-to-call timetable (M45); field focus lanes + demo validation/success (M71/M72); *page* „Greičiau – telefonu“ row lights up (3 px lane) for the chosen route; map trunk/branch draw (M41/M42) on a paper card.
- **Privatumo:** word reveals, scroll-spy TOC (ring fills), *page* reading-progress lane between the two stops, table rows with red edge on hover; table stacks into one card per cookie < 1000 px.
- **404:** hero zoom-out + parallax, flap „4 0 4“ (desktop, once), *page* lane: red lane draws down → stops with a cap → dashed ghost continues → neutral ring pops in; on phones the same story as a horizontal mini-route above the tiles.
- Reduced motion: every page element is in its final state (lanes drawn, rings filled, no parallax/drag indicator, stacking becomes a plain stack page-locally).

## 3. Typo / formatting corrections (verbatim otherwise)

Apie įmonę
1. Profesionalumas: „puiki žino“ → „puikiai žino“ (§8.2 #2).
2. Komfortas: „už **lanko** lepina saulė“ → „už **lango** lepina saulė“ — *new fix, not in §8.2* (obvious typo).
3. Komfortas: removed the DVD sentence and „Klejonė yra puikus būdas…“ (§6.2, §8.2 #1).
4. Saugumas: removed „Mūsų transporto priemonių parke – tik nauji (2017–2018 metų) mikroautobusai.“ (§6.2, §8.2 #1).
5. GS-Trust #3: „sako žmogiškųjų“ → „savo žmogiškųjų“; #6: „užtiktiname“ → „užtikriname“ (§8.2 #2).
6. GS-Trust #4: „tik naujausiais mikroautobusais“ → „tik techniškai tvarkingais mikroautobusais“ (client to confirm) and removed „; DVD – kad kelionė neprailgtų“ (sentence now ends „…jaustumėtės patogiai.“).

Kontaktai
7. Phone display unified: „+353 864 503104“ → „+353 86 450 3104“, „+447566878681“ → „+44 7566 878681“, „+34 60 25 47929“ → „+34 602 547 929“ (§8.2 #5); „Tel.:“ prefixes dropped (icon + label instead).
8. „PERVEŽIMAI Į AIRIJĄ / ISPANIJĄ“ (caps H5) → sentence case headings (§7.2 no ALL CAPS).
9. E-mail field tooltip, now shown as a visible hint: „išsiųti pasiūlymui parengtams“ → „išsiųsti pasiūlymui parengti“ (§8.2 #2).

Privatumo politika
10. „Techniniai svetainės slapukai **-** reikalingi…“ → en dash „–“.
11. Cookie source „sgppervezimai.lt“ → „sgp-pervezimai.lt“ (real domain; same rule as §8.2 #6).
12. „Slapukai naudojami Google Recaptcha **testo**“ → „…Google reCAPTCHA **testui**“ (case + brand spelling).

## 4. NEW copy introduced (for client approval, §8)

Apie įmonę
- Hero chips: „Nuo durų iki durų“ (§8.1 #10), „Lietuva – Airija – Lietuva“, „Lietuva – Ispanija – Lietuva“ (verbatim route names).
- Waypoints „Įmonė“, „Principai“, „Kelyje“, „Pasitikėjimas“; metas „5 principai“, „9 priežastys“ (+ existing „LT ⇄ IE · LT ⇄ ES“, „Apie 3–4 paros“).
- H2s reused, no new wording: 02 = Keleivių pervežimo H5 „Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?“; 03 = „Kelyje apie 3–4 paras“ (§8.1 #7); 04 = „Kodėl verta pasitikėti mumis?“ [P] with the verbatim Tarptautiniai lead „SGP pervežimai – komanda savo srities profesionalų…“. sr-only H2 „Apie mus“ for 01.
- Card counters „01 / 05“…; gallery counter „01 / 05“ (screen readers: „Nuotrauka 01 iš 05“); „Ankstesnė nuotrauka“, „Kita nuotrauka“, region „Nuotraukų galerija“ (role description „karuselė“); drag indicator „Tempkite“.
- Buttons „Pervežimo paslaugos“ / „Tarptautiniai pervežimai“ (labels of the live „Blokas po turiniu“).

Kontaktai
- Eyebrow „Atvykimas“ (existing chapter name); index „Skambinkite · Grafikas · Parašykite · Kur važiuojame“ (blueprint chapter names).
- H2 01 „Pervežimai į Airiją ir Ispaniją“ (composed from verbatim labels); meta „5 numeriai“; number labels „LT · Lietuva“ + live country names „Airija“, „Jungtinė Karalystė“, „Ispanija“; ticket kickers „Lietuva – Airija – Lietuva“ / „Lietuva – Ispanija – Lietuva“.
- 02: H2 „Artimiausi pervežimai“ [P] + note (§8.1 #15) + tip „Paspauskite eilutę – skambinsite tos krypties numeriu.“ (NEW).
- 03: H2 „Susisiekite su mumis“ (live footer H2), meta „El. paštu“, „Greičiau – telefonu“ with route labels „Lietuva → Airija“ etc.; form title „Parašykite“; **new optional fields** „Kryptis“ (Lietuva → Airija · Airija → Lietuva · Lietuva → Ispanija · Ispanija → Lietuva · Kita) and „Ką vežame?“ (service groups §8.1 #11 + „Kita“), marker „nebūtina“; subject placeholder „Pvz., Lietuva → Airija · Siuntos“; error „Įrašykite žinutės temą“.
- 04: H2 „Dvi kryptys. Keturios šalys pakeliui.“ (§8.1 #5) + home's trimmed verbatim paragraph + the delivery-facts pair (§4.12).

Privatumo politika
- Eyebrow „Informacija · Slapukai (Cookies)“; waypoint „Dokumentas“, meta „2 skyriai“; TOC „Turinys“ (aria „Dokumento skyriai“).
- Notice „Demonstracinė versija — Privatumo politikos tekstas bus pateiktas prieš paleidžiant svetainę.“ (§8.1 #25).
- **Placeholder (demo only)** „Laukiama kliento teksto“: „Duomenų valdytojas ir kontaktai“, „Kokius duomenis tvarkome ir kokiais tikslais“, „Kiek laiko saugome duomenis“, „Jūsų teisės“, „Slapukai ir sutikimas“ (structure from §8.3 #5; replaced by the client's text).
- Note „Pastaba — Lentelė perkelta iš dabartinės svetainės. Paleidus naują svetainę ją pakeis sutikimo valdymo įskiepio sugeneruotas slapukų sąrašas.“ (demo only); button „Keisti slapukų nustatymus“.

404
- H2 „Visos pervežimo paslaugos“ [P] + link „Visos paslaugos“ (existing label) above the service list. Everything else per §6.11/§8.1 #24.

## 5. REQUESTS for shared files (not edited — page-local workarounds in place)

1. **REQUEST: `assets/css/motion.css` — reduced motion must un-pin stacking cards (§5.5 „pinned sections … become plain stacks“).** Today `.sgp-stack__item` stays `position:sticky` under `prefers-reduced-motion`, so cards still overlap. Proposed: inside the reduce block add `.sgp-stack__item{position:relative;top:auto}`. Workaround: `.ab-stack .sgp-stack__item{position:relative;top:auto}` in apie.css.
2. **REQUEST: `assets/css/components.css` — stacking dim via overlay, not opacity.** `.sgp-stack__item>*{opacity:calc(1 - var(--sp)*.4)}` makes a dimmed card translucent, so with ≥ 3 stacked cards the text of the cards underneath shows through („ghost text“, clearly visible on the 5 principles). Proposed: keep opacity 1 and dim with `…>*::after{content:"";position:absolute;inset:0;background:var(--c-asphalt-950);opacity:calc(var(--sp,0)*.6);pointer-events:none}` (child needs `position:relative`). Workaround: `.ab-card::after` in apie.css.
3. **REQUEST: `assets/css/components.css` — ticket stub on phones.** In the ≤699 block `.sgp-ticket__stub>.sgp-mono{flex-basis:100%}` also matches `.sgp-ticket__rel` (it has `sgp-mono`), so „po 16 d.“ drops to its own line. Proposed: `.sgp-ticket__stub>.sgp-mono:first-child{flex-basis:100%}`. (Kontaktai uses its own stub layout, so only GS-Arrival/other pages are affected.)
4. **REQUEST: `tools/build.py` — hero preload widths.** The `hero_media` preload `imagesrcset` starts at 760w while `{{img}}` offers 480w, so DPR-1 phones load a different file and Chrome warns „preloaded but not used“ (seen on 404 at 390 px). Proposed: build the preload srcset with the same widths/sizes as the hero `{{img}}` (include 480).
5. **REQUEST (nice to have): `assets/js/sgp.js` — expose `SGP.cookie.open()`** so the privacy page's „Keisti slapukų nustatymus“ does not need to know the `sgp-cookie` localStorage key (currently the page removes the key and unhides `#sgp-cookie`).
6. **Optional:** the `.sgp-e404*` rules in components.css could move to `pages/404.css` now that 404 has its own page CSS.

## 6. Known issues / open questions for the client

- **Privacy policy text does not exist** — page shows the live „Informacija ruošiama...“ + demo notice + placeholder block. The Joomla cookie table (jpanesliders_…, joomsef_lang) will not exist in WordPress → replace with the consent plugin's list. Live link „Norėdami pasitikrinti … spauskite čia.“ **removed** (Joomla endpoint disappears) — flagged.
- Kept for confirmation (§8.2 #1): Komfortas „tik naujais, komfortiškais mikroautobusais“, GS-Trust #4 „techniškai tvarkingais“ and „Siuntos taip pat gabenamos naujais, patikimais mikroautobusais.“
- GS-Trust #7 „kad kelionė **bus** saugi ir sklandi“ kept verbatim (grammatically „būtų“) — client may approve the fix.
- Gallery = 5 Pexels photos per blueprint → replace with the client's own photos. Operatyvumas photo (17720190) is mostly night sky; shown with a 1.45× crop on the trucks — consider another photo.
- New optional contact-form fields („Kryptis“, „Ką vežame?“) need Fluent Forms set-up + approval; the live form only has vardas / el. paštas / tema / žinutė.
- Kontaktai rail terminus and 404 lane are desktop-only (no rail < 1000 px, as everywhere); phones get the inline terminus ring / horizontal mini-route.
- Local preview of 404 needs the repo served under `/sgp-pervezimai/` (Foundation §10.4 #1); QA used request mapping.

## 7. Verification pass (second run, same team)

- Re-built only this team's pages (`python3 tools/build.py apie-imone kontaktai privatumo-politika 404` → idempotent, 0 changed before the edits below); `python3 tools/check.py` → 21 pages, 0 errors, 0 warnings; `node --check` on all four page scripts passes.
- Headless Chrome re-check at 360, 390×844, 768×1024, 1024×768, 1366×657, 1440×900 and 1920×1080 on all four pages: horizontal overflow 0, no text < 12 px, exactly the 5 tel numbers (all with `aria-label`), one H1, no duplicate ids, no console errors/warnings, no failed requests, no non-GET requests; reduced motion → no element left hidden. The only target < 44 px is the shared breadcrumb link „Pradžia“ (42×32, inline text link, passes WCAG 2.5.8 24 px minimum; shared component).
- Functional re-check: contact form (empty submit → 4 field errors + focus on „Jūsų vardas“; route „Airija → Lietuva“ + „Siuntos“ → subject pre-filled „Airija → Lietuva · Siuntos“ and the IE row lights up; valid submit → success box focused, URL unchanged, nothing sent), e-mail copy („Nukopijuota“ + live status), header terminus lane measured, Flickity gallery (counter 01 → 02, prev ×2 → 05, one selected cell; phones 335 px cells), privacy „Keisti slapukų nustatymus“ re-opens the cookie bar and focuses „Sutinku“.
- Polish in this pass: Apie datasheet „Kryptys“ now shows the two routes on two lines (was one run-on line joined by „·“, hard to read when wrapped); privacy table title width 30ch → 44ch (it wrapped into 3 short lines above a full-width table).
- Requests §5 unchanged and still open.


---

**Integration pass (2026-09-23):** all REQUESTS above were resolved in the shared files and the page-local workarounds were removed — see `foundation.md` §11 for the table (only services-routes REQUEST 7, `data-hover-video-target`, was not adopted). Client-facing lists (typo fixes, new copy, content notes) are merged into `docs/turinio-pataisos.md`.

**Review fix (privacy page typography/callouts):** `.pp-lead` („Informacija ruošiama...“) is now a lead paragraph (`400 var(--fs-lead)/1.5 var(--f-text)`, `--fg-2`, max 60ch) instead of a `--fs-statement` Barlow Condensed line that read as a second heading under the H2. The „Pastaba“ note under the cookie table now uses the same standard `.sgp-callout` (3 px red left bar, card background, `role="note"`, text in a `<p>`) as the „Demonstracinė versija“ notice — the red-outline `.sgp-callout--line` variant is no longer used on this page, so it has one callout style. Files: `assets/css/pages/privatumo-politika.css`, `src/pages/privatumo-politika.html` → `privatumo-politika/index.html`. No copy changes.
