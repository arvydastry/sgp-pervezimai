# Salient 18.2.1 atitikimas — rezultatas (3 banga, integracija)

Data: 2026-09-24. Kryptis (vadovo sprendimas): **„SGP v2 tapatybė, sukurta Salient būdu“** — v2 paletė (asfaltas / popierius / raudona), Barlow Condensed + Barlow, 2–4 px spinduliai, tamsūs ir šviesūs skyriai, vaizdo įrašo hero su artimiausiais išvykimais, skambučiai pagal kryptį — bet kiekvienas blokas sudėtas tik iš natyvių Salient 18.2.1 elementų ir jų parinkčių. Harbor stiliaus plytelė liko tik alternatyva (`docs/kryptys/salient-tile-harbor.html`).

Šaltiniai: `docs/salient-auditas.md` (prieš), `docs/salient-atitikimo-planas.md` (planas), `docs/salient-18-2-1-parinktys.md` (tikrosios parinktys ir laikai), komandų pastabos `docs/build-notes/{kit,home,about-contact,services-routes,service-template,schedule-tracking-rules}.md`. Skaičiai gauti įrankiais `tools/coverage.py`, `tools/textdiff.py`, `tools/check.py`.

## 1. Santrauka

| Rodiklis | Prieš (v2 „Maršruto linija“, auditas) | Po (3 banga) |
|---|---|---|
| Blokai pagal verdiktą | 129 blokai: NATIVE **22 %** · NATIVE+CSS **41 %** · CUSTOM **29 %** · WRONG-MAPPING **8 %** | 96 unikalūs blokai: NATIVE **76 %** (73) · NATIVE+CSS **24 %** (23) · CUSTOM **0 %** · WRONG-MAPPING **0 %** |
| Papildomas CSS, kurio reikėtų Salient'e | ≈ 4 819 eil. (auditas); repozitorijoje 2 924 kompaktiškos CSS eil. (tokens/base/components/motion + 11 puslapių CSS) | **178** ne tuščios eil. `sgp-custom.css` (biudžetas 250) |
| Papildomas JS | ≈ 350 eil. savo JS (auditas); repozitorijoje 1 413 eil. (`sgp.js` + 11 puslapių JS) | **28** eil. `sgp-custom.js` (biudžetas 30) |
| Puslapių CSS / JS | 11 CSS + 11 JS failų | **0 / 0** (`assets/css/pages/`, `assets/js/pages/` ištrinti) |
| PHP trumpasis kodas / ACF | `[sgp_grafikas]` + ACF Pro | nėra — grafikas = ranka pildomi Global Sections |
| `data-salient` žymės (21 psl.) | 597 žymės (dažniausiai tik eilutėms ir savoms klasėms; 10 blokų su 18.3 / neegzistuojančiais pavadinimais) | **6 041** žymė, 48 elementų tipai, tikslūs 18.2.1 administravimo pavadinimai; kiekviena Section / Row / Inner Row / Global Section pažymėta (`check.py` klaida, jei ne), elementų be žymės — **0** |
| Automatinė patikra | — | `build.py` ✓ · `check.py` 21 psl., **0 klaidų, 0 įspėjimų** · `node --check` visi JS ✓ · turinio regresija: 0 nepaaiškintų praradimų |

**Kaip skaičiuota.** „Blokas“ = eilutės lygio WPBakery vienetas (Section / Row / Global Section tiesiai `<main>` viduje) + antraštės, meniu, off-canvas, poraštės ir skambučių juostos Global Sections (vieną kartą). Vienodas receptas keliuose puslapiuose (pvz. GS-Kvietimas, 11 paslaugų šablono eilutės) skaičiuojamas vieną kartą — taip pat, kaip audite šablonas buvo skaičiuotas vieną kartą. NATIVE+CSS = natyvūs elementai + numeruota `sgp-custom.css` grupė (C-4, C-5, C-6, C-7, C-8, C-9, C-12, C-14). Visai svetainei galiojančios grupės (C-2 sumažintas judesys, C-3 lietuviška tipografija, C-11 fokusas) blokams neskaičiuojamos. WRONG-MAPPING = 0, nes `check.py` atmeta visus audite rastus neegzistuojančius pavadinimus („Stacking“ Pinned efektas, „(Line)“ / „Regular“ mygtukai, Fancy Box „minimal“, „Fullscreen Split“, „Before Footer“, 18.3 parinktys).

## 2. Natyvus padengimas

### 2.1 Blokai pagal verdiktą (po)

| Puslapis | Blokų | NATIVE | NATIVE+CSS | Kokia CSS grupė |
|---|---:|---:|---:|---|
| / (pradžia) | 17 | 11 | 6 | C-5 grafikas, C-6 forma, C-7 schema, C-14 pauzė |
| /apie-imone/ | 10 | 10 | 0 | — |
| /pervezimo-paslaugos/ | 7 | 6 | 1 | C-5 |
| /…/tarptautiniai-pervezimai/ | 12 | 9 | 3 | C-5, C-7, C-14 |
| 11 paslaugų (kiekviena) | 14–15 | 10–12 | 3–4 | C-5 (Maršrutai), C-6 (GS-Užklausa), C-8 (Page Submenu), C-7 (keleivių salonas) |
| /pervezimu-grafikas/ | 5 | 2 | 3 | C-5, C-7, C-14 |
| /siuntos-sekimas/ | 4 | 3 | 1 | C-6 |
| /taisykles/ | 4 | 4 | 0 | — |
| /kontaktai/ | 5 | 2 | 3 | C-5, C-6, C-7 |
| /privatumo-politika/ | 2 | 1 | 1 | C-9 (Complianz slapukų lentelė) |
| 404 | 3 | 3 | 0 | — |
| _global (GS-Išvykimai, GS-Paslaugų meniu, GS-Telefonai, GS-Poraštė, GS-Skambučių juosta) | 5 | 3 | 2 | C-12 bėganti eilutė, C-4 skambučių juosta (antraštės mygtukas C-10 ir slapukų juosta C-9 — ne blokai) |

### 2.2 Dažniausi elementai (`data-salient` žymės visuose 21 puslapyje)

| Elementas | Žymių | | Elementas | Žymių |
|---|---:|---|---|---:|
| Button (nectar_cta: Arrow Circle, Underline, Text Reveal Wave, See Through, Basic, Next Section) | 1 327 | | Scrolling Text | 50 |
| Column / Inner Column | 872 / 310 | | Image | 44 |
| Badge (Minimal Line etiketės ir „chip“) | 870 | | Fancy Unordered List | 41 |
| Row / Inner Row | 392 / 246 | | Fancy Box | 40 |
| Responsive Text | 387 | | Price Typography | 26 |
| Horizontal List Item | 332 | | Milestone | 23 |
| Global Section | 215 | | Icon List | 22 |
| Divider | 207 | | Tabs / Toggle Panels | 19 / 8 |
| Animated Text | 154 | | Highlighted Text | 16 |
| Text Block | 77 | | Fluent Forms | 16 |
| Sticky Content Section / Sections | 66 / 15 | | Cascading Images | 15 |
| Page Submenu | 11 | | Content Trail · Image With Hotspots · Video Lightbox · Icon · Legacy Button · Image Gallery | 7 · 6 · 5 · 5 · 4 · 1 |

Parallax ir judesys — tik natyvios parinktys su tikrais 18.2.1 skaičiais: Row parallax Subtle .20 / Regular .28 / Medium .40 / High .60, Parallax Fade (Section), Background Layer Animation (Zoom Out Slowly 8 s, Slight Zoom Out Reveal 1.3 s, Clip Path Inset pagal slinktį), Column Scroll Position Advanced, Inner Column Mask Reveal, Reveal Rotate, Cascading Images sluoksnių parallax, Sticky Content Sections (Horizontal Scrolling, Pinned Scale / Blurred Scale / Overlapping + Stacked, Sticky Media), Scrolling Text su Move on Scroll ir Spin divider, Color Change Section, Lenis, View Transitions; stulpelių įėjimai easeOutExpo 1300 ms.

## 3. Papildomo kodo sluoksnis (vienintelis, einantis į produkciją)

`assets/css/sgp-custom.css` — **178** ne tuščios eilutės (su komentarais; biudžetas 250, `check.py` riba 260). Įklijuojama į *Theme Options → General Settings → CSS/Script Related → Custom CSS Code*.

| Grupė | Eil. | Paskirtis | Kodėl ne natyviai |
|---|---:|---|---|
| antraštė | 7 | failo paskirtis ir taisyklės | — |
| C-1 žetonai | 8 | tik tos spalvos / kreivės, kurių reikia žemiau | Theme Options neturi CSS kintamųjų |
| C-2 sumažintas judesys | 38 | visi įėjimai rodo galutinę būseną, sustoja parallax, clip path, bėgantis tekstas, Content Trail, lipnios sekcijos sukraunamos, Tabs turinys nepritemdomas | **18.2.1 visai neskaito `prefers-reduced-motion`** |
| C-3 lietuviška tipografija | 5 | be automatinio kėlimo, `text-wrap: balance` antraštėms, diakritikai nenukerpami žodžių animacijoje, lentelių skaitmenys | tokio nustatymo nėra |
| C-4 skambučių juosta | 8 | saugi zona (iPhone), 52 px mygtukai, poraštės ir slapukų kortelės atitraukimas | Sticky Row neturi safe-area |
| C-5 grafiko eilutės | 9 | lentelių skaitmenys, telefono stulpelis dešinėje ir **niekada nelūžta** (3 bangos pataisa — selektorius taikė į nuorodą, ne į stulpelį) | HLI neturi `nowrap` / skaitmenų parinkčių |
| C-6 Fluent Forms | 24 | Salient „Minimal“ formos išvaizda (apatinė linija, raudonas fokusas, klaidos) šviesiame ir tamsiame skyriuje | Fluent Forms yra įskiepis, ne Salient forma |
| C-7 Image With Hotspots | 17 | 3 px kvadratiniai žymekliai Label šriftu, 2 pulsavimo ciklai, tamsus tooltip; **telefone 24 px** (3 bangos pataisa — žymekliai nebeužstoja šalių pavadinimų) | Salient žymeklis yra 30 px apskritimas |
| C-8 Page Submenu | 9 | raudona linija po aktyviu (scrollspy) punktu | Salient uždeda `.current-menu-item`, bet nieko nepiešia |
| C-9 Complianz | 19 | slapukų juosta ir sąrašas SGP spalvomis | įskiepis |
| C-10 antraštės mygtukas | 9 | tamsus tekstas ant raudono „Skambinti“ visose antraštės būsenose, 44 px telefone, GS-Telefonai tarpai | meniu mygtuko teksto spalva paveldima iš antraštės |
| C-11 fokusas | 5 | 2 px žiedas: raudonas tamsiuose, rašalo šviesiuose skyriuose | nėra nustatymo |
| C-12 bėganti eilutė | 5 | nuorodos fokusas, pauzė užvedus / fokusuojant, pabraukimas | Scrolling Text neturi pauzės |
| C-13 judesio pauzės būsena | 5 | `html.sgp-paused` sustabdo bėgantį tekstą, Content Trail, pulsavimą, Zoom Out Slowly | WCAG 2.2.2, Salient neturi |
| C-14 pauzės mygtukas | 10 | 44 px taikinys, ikona pagal būseną | WCAG 2.2.2 |

`assets/js/sgp-custom.js` — **28** eilutės (*Custom JS (Head)*): **J-1** sumažinto judesio režimas (išjungia Lenis prieš temai perskaitant `nectarOptions`), **J-2** judesio pauzė (vaizdo fonai, Scrolling Text, Content Trail; WCAG 2.2.2).

Kas *nėra* papildomas kodas (produkcijoje jo nebus arba tai nustatymai): `theme-options.css` (107 eil. — Theme Options laukai), `emul/*.css` (1 224 eil.) + `emul.js` (983 eil.) — Salient elgsenos emuliacija, `demo.css` + `demo.js` (135 eil. — „Salient žymės“, demo formos, slapukų atmintis), inline `style="--…"` kintamieji (WPBakery Design Options) ir `data-*` atributai (elementų parinktys).

## 4. Kas pakeista kiekviename puslapyje (v2 → Salient)

| Puslapis | Kas buvo savas (v2) | Kuo pakeista (18.2.1 elementai) |
|---|---|---|
| **/** | Raw HTML maršruto H1, split-flap lenta, bėgis su stotelėmis, savas horizontalus paslaugų kelias su skaitikliu, inline SVG schemos su JS, hover video, savi akordeonai | Section + Background Video + **Parallax Fade** · **Animated Text** H1 · stiklo juosta (Inner Row **Backdrop Filter**) su GS-Artimiausi ir 2 skambučiais · Highlighted Text · **Cascading Images** · Milestones · **Sticky Content Sections → Horizontal Scrolling** (11 paslaugų, Link Mouse Indicator) · **Scrolling Text** · **Image With Hotspots** ant statinės `marsrutai.svg` · Clip Path Inset + Video Lightbox · Icon List „Stations“ · **Tabs Minimal** su GS-Grafikas · **Toggle Panels Animated Circle** · Fluent Forms · Mask Reveal |
| **/apie-imone/** | bėgis, „Pinned → Stacking“ (neegzistuoja), savas lipnus indeksas, žiedų linija GS-Trust | vidinė antraštė + stiklo juosta · Clip Path Inset nuotraukų juosta · Cascading Images (3 sluoksniai) · Milestones ant Zoom Out Slowly · **Pinned Sections → Scale + Stacked** (5 principai) · Scrolling Text + **Flickity** galerija · GS-Pasitikėjimas (HLI) · GS-Kvietimas |
| **/pervezimo-paslaugos/** | savas grupių indeksas su žiedais, bilietų kortelės | nuotraukų kortelės (Column BG + overlay hover + Column Link) · **Pinned Sections → Blurred Scale + Stacked + Section Navigation** (6 grupės, Content Alignment Stretch) · Fancy Box *Description on Hover* · Scroll Position Advanced · Tabs su GS-Grafikas · GS-Maršrutai |
| **/…/tarptautiniai-pervezimai/** | SVG schema + maršruto juostelės, popover | Section video + Parallax Fade · Image With Hotspots · **Pinned → Overlapping** (Airija / Ispanija / Artimiausi) su stiklo stulpeliais, Icon List stotelėmis, Cascading Images · Video Lightbox · Scrolling Text · Fancy UL ✕ + Milestone 1200 EUR · kraštinės animacija · GS-Paslaugos |
| **11 paslaugų** (šablonas) | 28 KB puslapio CSS, 114 eil. JS, hover video, savas bėgis ir „Kita stotelė“ | **Page Submenu** (Sticky, scrollspy) · KV = HLI · Cascading Images · Icon List stotelės · **Sticky Media, Scrolling Content** · Toggle Panels / Callout · Fancy UL + Milestone · Tabs + GS-Grafikas + Scrolling Text + GS-Maršrutai · Highlighted Text ant High parallax · Fancy Box susijusios · „Kita paslauga“ nuotraukos kortelė · GS-Užklausa; specialūs blokai X1–X15 (pvz. keleivių Pinned Scale, salono Hotspots, gyvūnų Icon List, video Lightbox) |
| **/pervezimu-grafikas/** | `[sgp_grafikas]` lenta, split-flap, laiko juosta (lane), SVG schema | vaizdo hero + stiklo juosta · **Tabs Minimal** (Visi / Airija / Ispanija) su GS-Grafikas · Clip Path Inset + Scrolling Text juosta · KV + Image With Hotspots · GS-Kvietimas |
| **/siuntos-sekimas/** | kelionės juosta su stotelėmis, „Ieškoma…“ būsena | Fluent Forms (Redirect į tikrą sekimo įrankį) · Mask Reveal nuotrauka · Icon List · demo rezultatas (tik demo) · 3 Fancy Box *Description on Hover* su pakopiniu Scroll Position Advanced |
| **/taisykles/** | lipnus turinys su užpildomomis stotelėmis, taisyklių terminų juosta | **Tabs → Vertical Sticky Scrolling (Tab Links)** su CTA = PDF · Highlighted Text · tamsus Inner Row + Fancy UL ✕ · Milestone 1200 EUR + KV + Toggle · 3 Milestones (0 / 5 / 14 d.) · Icon List 6.1 · Lift button |
| **/kontaktai/** | bilietų kortelės, kopijavimo mygtukas, stotelių indeksas, SVG schema | stiklo kortelės ant Zoom Out Slowly (Text Reveal Wave numeriai) · **Tabs Toggle Button** su GS-Grafikas · Fluent Forms „SGP kontaktai“ · Mask Reveal · Image With Hotspots |
| **/privatumo-politika/** | mini turinys + skaitymo progreso juosta | **Tabs → Vertical Sticky Scrolling (Tab Links)** · **Toggle Panels Minimal Shadow** (slapukai; produkcijoje Complianz `[cmplz-cookies]`) · „Keisti slapukų nustatymus“ vėl atidaro slapukų juostą |
| **404** | „4 0 4“ split-flap, nutrūkęs bėgis | GS-404: Section + Parallax Fade + Animated Text (Blur) · Scrolling Text · GS-Paslaugos |
| **Visi puslapiai** (chrome) | popover skirstytuvas, GS-Board, GS-Arrival bilietai | GS-Išvykimai (Scrolling Text *In Navigation Top Before Scrolling*) · permatoma → sulieta antraštė, Resize On Scroll, Animated Underline · „Skambinti“ mygtukas + GS-Telefonai mega meniu · **Off Canvas Fullscreen Cover Split** · GS-Poraštė · GS-Skambučių juosta · **Back To Top** · View Transitions · Lenis |

## 5. 3 bangos integracija — kas padaryta

**Sprendimas dėl `/_kit/`.** Rinkinio pavyzdys nebėra viešos svetainės dalis: `src/pages/_kit.html` lieka (šaltiniai, kurių vardas prasideda `_`, praleidžiami), `python3 tools/build.py --kit` jį sugeneruoja į **`docs/kit.html`** (šalia kitų dizaino pavyzdžių `docs/kryptys/`; `check.py` jo netikrina ir klaida, jei vėl atsiranda `_kit/`). Aprašyta `README.md` ir `docs/build-notes/kit.md` §0.

**Senasis v2 sluoksnis ištrintas** (niekas jo nebenaudojo): `src/partials/legacy/*` (14), `assets/css/legacy/*` (4), `assets/js/legacy/sgp.js`, `assets/js/pages/*.js` (10), `assets/css/pages/*.css` (10; paslaugos šablono failus komanda ištrynė anksčiau), senieji grafiko / paslaugų atvaizduotojai `tools/build.py` (920 → 617 eil.). `kit: salient` dabar privalomas. Senos komandų pastabos perkeltos į `docs/build-notes/v2-archyvas/`.

**Bendri (kit) pataisymai pagal komandų prašymus:**

| Prašymas | Pataisa |
|---|---|
| Icon List horizontalus: pavadinimai skirtingame aukštyje (home) | `align-content:start` elemente (kaip Salient) |
| Icon List telefone: „kelio“ linija kerta pavadinimą (home, sekimas, tarptautiniai, paslaugos) | emuliuotas **Divider → Custom Height (tablet / phone)**; stotelių linijos gavo `--h-m:64px` — telefone linija virš sąrašo |
| `marsrutai.svg`: nukirpta legendos eilutė; žymekliai telefone dengia šalių pavadinimus | legenda pakelta į 720 viewBox; pavadinimai atitraukti ≥ 40 vnt. nuo stotelių; C-7 telefone 24 px žymekliai |
| `{{grafikas:next}}` lūžta prieš „d.“ | datose nelaužiamas tarpas („rugsėjo 28 d.“) — GS-Artimiausi, GS-Grafikas, bėganti eilutė |
| GS-Maršrutai: sąrašas prilipęs prie „3–4 paros kelyje“ | Design Options `--mt:18px;--mb:28px`; emuliacija gavo elemento *margin-bottom* |
| `data-salient` trūko 19 elementų partial'uose | pažymėta: GS-Poraštė (15), GS-Užklausa (4), GS-Pasitikėjimas (8), GS-404 (2), GS-Maršrutai (2) → **0 įspėjimų** |
| Slapukų nustatymų mygtukas tik šokdavo į `#slapukai` | `demo.js`: `.cmplz-manage-consent` vėl atidaro juostą ir fokusuoja pirmą mygtuką (produkcijoje `[cmplz-manage-consent]`) |
| GS-404 H1 per mažas | vidinės antraštės dydis (6.4vw, 44–104 px) |
| GS-Grafikas telefono stulpelis lūžta 1000–1199 px | C-5 selektorius taikytas ne į tą elementą (paskutinis vaikas — nuoroda) → `[data-text-align="right"]` + `nowrap` |
| Tabs → Vertical Sticky Scrolling maišė dvi parinkčių grupes | emuliacija perrašyta pagal 18.2.1: **Tab Links** (25 % / Wide / Narrow, 1 px takelis + 3 px indikatorius .5 s, Item Spacing, Tab Spacing, Mobile Display, CTA) ir **Tab Content** (Fade + Opacity / Text Outline Fill); `/taisykles/` ir `/privatumo-politika/` perjungti į švarų Tab Links; PDF — CTA mygtukas navigacijoje; pataisyti `_kit`, kit.md ir planas §3.11 |
| Sumažintas judesys: neaktyvūs Tabs .28 | C-2: `.tabbed .wpb_tab{opacity:1}` |
| `?toggle=N` nusileidžia per aukštai | gilioji nuoroda slenka po `load`, momentiniu Lenis šuoliu iki pavadinimo ir pasitikrina po 1.3 s (patikrinta: pavadinimas 75–85 px nuo viršaus, 1440 ir 390); akordeone gilioji nuoroda pakeičia *First Toggle Open* |
| Scrolling Text skirtukas ✦ 8.5 px | *Divider Size* skaičiuojamas nuo *Custom Font Size* (`--fs`, `--fs-m`), ne nuo įvyniojančio 17 px |
| HLI rodyklė užlipa ant ilgo teksto | `:has(.nectar-list-item-btn)` specifiškumas pakeltas; telefone 48 px / 14 px |
| Color Change Section: išeinančio skyriaus tekstas tos pačios spalvos kaip fonas | aktyvaus skyriaus tonas perduodamas visoms Color Change eilutėms (`html[data-cc-tone]`, 0.8 s), kaip Salient `--nectar-page-text-color`; eilutės su savo fono vaizdu tono nekeičia |
| Pinned Sections → Content Alignment nebuvo | Middle / Stretch / Top / Bottom (sekcija — flex stulpelis, Stretch ištempia Inner Row) |
| Mask Reveal + vidinė animacija vėluoja | kit.md §10: nedėti įėjimo animacijų į Mask Reveal stulpelį |

**Harmonizavimas:** visos vidinės antraštės turi tą patį receptą — viršus **184 px** (planšetė 168, telefonas 128), apačia 48 / 32 px (be stiklo juostos 72 / 48 px), H1 **6.4vw, 44–104 px, eilutės aukštis .92** (anksčiau 5 skirtingi dydžiai nuo 6.2 iki 7.4vw ir numatytasis H1 paslaugų puslapyje); stiklo juostos nuoroda visur „Visas grafikas →“ (lūžo 1024 px); duonos trupiniai vienodi visuose 19 vidinių puslapių. Pridėtas natyvus **Back To Top** (*Theme Options → Functionality*, 350 px, tik kompiuteryje) — grąžina v2 „↑ Į pradžią“ funkciją.

## 6. Turinio regresija

`python3 tools/textdiff.py` palygina kiekvieno puslapio matomą tekstą su `git HEAD` (v2 build): **3 448** HEAD fragmentai, **516** nerasti — visi priskirti plano sprendimams, **0 peržiūrėtinų**:
- dekoratyvūs užrašai (leidžiama): santykiniai statusai „po N d.“, split-flap datos, „Kitas / Artimiausias išvykimas“, stotelių skaitikliai „04 / 11“, „Kita stotelė · 05“, „5 principai“, „9 priežastys“, laiko juostos (lane) tekstai, schemų legendos (dabar `marsrutai.svg` viduje), „Kopijuoti“, gyvūnų kontrolinio sąrašo mygtukai, „Pauzė“, „LT ⇄ IE“;
- GS-Arrival → GS-Kvietimas (plano G23/G24) puslapiuose be GS-Užklausa: užklausos formos laukai ir sakinys „Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!“ — forma lieka `/kontaktai/`, pradžioje ir 11 paslaugų, sakinys — `/kontaktai/`; GS-Kvietimas turi abu skambučius ir „Parašykite mums →“;
- GS-Board nuimtas nuo /apie-imone/, /taisykles/, 404 (plano A11 / L7 / E4) — datos lieka GS-Išvykimai (kiekviename puslapyje) ir GS-Artimiausi.

Paslaugų sąlygos, taisyklės (1–6 skyriai, 12 draudžiamų daiktų, baudos, 4.5 p.), visi 5 telefonai, el. paštas ir visos grafiko datos yra kiekviename puslapyje, kuriame buvo.

## 7. Kokybės patikra

- `python3 tools/build.py` → 21 puslapis; `python3 tools/check.py` → **0 klaidų, 0 įspėjimų** (nuorodos, id, alt, 5 tel:, vienas H1, `data-salient` kiekvienai eilutei ir elementui, draudžiamos v2 konstrukcijos, radius ≤ 4 px, tekstas ≥ 12 px, biudžetai); `node --check` — visi `assets/js/*.js`.
- Playwright Chromium, visi 21 puslapiai, 1440×900 ir 390×844, slenkant visą puslapį: **horizontalus perpildymas 0**, **0 konsolės klaidų / nepavykusių užklausų**; sumažinto judesio režimu (1440) viskas matoma galutinėje būsenoje, Horizontal Scrolling tampa slenkama eile, lipnios sekcijos sukraunamos. Kontaktiniai lapai: `scratchpad/shots/sheet-c1-*.jpg` (1440), `sheet-c3-*.jpg` (390), `sheet-rm1-*.jpg` (reduced motion).
- Vaizdo įrašai Playwright Chromium'e nerodomi (H.264) — matomi plakatai; tai numatyta.

## 8. Likę savi elementai ir priežastys

| Elementas | Kodėl paliktas | Produkcijoje |
|---|---|---|
| `sgp-custom.css` C-1…C-14 (178 eil.), `sgp-custom.js` J-1, J-2 (28 eil.) | žr. §3 — prieinamumas (sumažintas judesys, pauzė, fokusas), lietuviška tipografija, įskiepių (Fluent Forms, Complianz) išvaizda, 3 Salient elementų detalės | Theme Options → Custom CSS / Custom JS (Head) |
| `assets/img/marsrutai.svg` | statinė maršrutų schema — tai *paveikslėlis* Image With Hotspots elementui, ne kodas | įkelti į Media Library (SVG įskiepis arba eksportuoti PNG / WebP) |
| `assets/img/paslaugos/*.svg` (2) | dalinio krovinio ir pakavimo iliustracijos — paprasti Image elementai | Media Library |
| Grafiko Global Sections | redaktorius kas mėnesį perrašo datas GS-Išvykimai, GS-Artimiausi, GS-Grafikas Airija / Ispanija (demo generuoja iš `grafikas.json`) | ranka, be trumpojo kodo |
| Siuntos sekimo rezultatas `?kodas=SGP-DEMO` | tik demo (`demo.js`) | Fluent Forms Confirmation → Redirect į tikrą sekimo įrankį |
| Inline 15 px šriftas P3 paslaugų aprašymuose (`/pervezimo-paslaugos/`) | tekstas Horizontal List Item stulpelyje; WordPress'e tai `<span style>` stulpelio turinyje | arba 2 eil. į sgp-custom.css (biudžete vietos yra) |

## 9. Neišspręsta / tikrinti staging aplinkoje

- **Emuliacija ≠ temos DOM** (kit.md §10): C-2, C-5, C-7, C-8, C-10 selektorius, Pinned Scale / Overlapping, Clip Path Inset, stiklo kortelių Backdrop Filter ir naują Color Change teksto elgseną patikrinti su tikru Salient.
- Pinned sekcija, aukštesnė nei `100vh − antraštė`, prisegta nerodo savo apačios (Salient elgiasi taip pat) — puslapiai sudėti taip, kad tilptų ≥ 1024×768 ir 1280×720; automatinės apsaugos nėra.
- Kliento sprendimai: Airijos atkarpa („maršrutas tikslinamas“, keltų medija nenaudojama), transporto teiginiai („tik naujais mikroautobusais“), nauji šablono užrašai (`turinio-pataisos.md`), tikri atsiliepimai (H9 eilutė produkcijoje išjungta), privatumo politikos tekstas.
- Keleivių salono žymeklių koordinatės — demo nuotraukai; tikrai nuotraukai reikės naujų.
