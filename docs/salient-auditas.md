# Salient 18.2.1 auditas — SGP v2 demo („Maršruto linija“)

Data: 2026-09-24. Tikrinta pagal naudotojo licencijuotą **Salient 18.2.1** kodą (tema `salient/`, `salient-core` elementų žemėlapiai `includes/nectar_maps/*.php`, eilučių/stulpelių parametrai `includes/nectar-addons.php`, Theme Options `nectar/redux-framework/options-config.php`, Global Sections `includes/global-sections/display-options.php`, JS `js/build/init.js`), ne pagal 18.3 dokumentaciją. Kiekvienas `data-salient` teiginys sutikrintas su tikrais parametrų pavadinimais. Temos kodas į projektą nekopijuotas.

Ekrano nuotraukos (1440×900): pradžia, pervežimo paslaugos, krovinių pervežimas, pervežimų grafikas + apie, tarptautiniai, taisyklės, kontaktai, siuntos sekimas, keleivių ir gyvūnų paslaugos. Palyginimui peržiūrėti Salient demo duomenys (Signal, Harbor, Tether, Corporate 3, Business 3) iš Demo Importer.

Verdiktai: **NATIVE** — tikslus elementas ir nustatymai, be papildomo kodo; **NATIVE+CSS** — natyvus elementas + nedaug Custom CSS; **CUSTOM** — reikia Raw HTML / savo JS / PHP trumpojo kodo / ACF; **WRONG-MAPPING** — nurodyto nustatymo 18.2.1 nėra. „Atrodo kaip Salient?“: yes / partly / no. `custom_css_lines` — apytikslis Custom CSS eilučių kiekis, kurio reikėtų Salient'e, kad blokas atrodytų kaip demo.

## 1. Santrauka

**Iš viso blokų: 129.** NATIVE **22 %** (28) · NATIVE+CSS **41 %** (53) · CUSTOM **29 %** (38) · WRONG-MAPPING **8 %** (10).

Ar atrodo kaip Salient elementas: yes 35 · partly 72 · no 22. Norint išlaikyti dabartinę išvaizdą, Salient'e reikėtų ≈4 819 eil. Custom CSS (vien blokams, be bendrųjų stilių), plius PHP trumpojo kodo, ACF ir ≈350 eil. savo JS.

| Puslapis | Blokų | NATIVE | NATIVE+CSS | CUSTOM | WRONG-MAPPING | Atrodo kaip Salient (yes/partly/no) | Custom CSS ≈ |
|---|---:|---:|---:|---:|---:|---|---:|
| _global (visi puslapiai) | 32 | 19 % | 50 % | 31 % | 0 % | 9/14/9 | 1517 |
| / (pradžia) | 16 | 25 % | 38 % | 31 % | 6 % | 5/8/3 | 633 |
| /apie-imone/ | 9 | 33 % | 33 % | 11 % | 22 % | 2/7/0 | 165 |
| /pervezimo-paslaugos/ | 6 | 17 % | 33 % | 33 % | 17 % | 1/4/1 | 285 |
| /pervezimo-paslaugos/tarptautiniai-pervezimai/ | 13 | 23 % | 38 % | 31 % | 8 % | 5/5/3 | 458 |
| paslauga (šablonas ×11) | 11 | 18 % | 82 % | 0 % | 0 % | 3/8/0 | 195 |
| paslauga: specialūs blokai | 14 | 21 % | 43 % | 21 % | 14 % | 6/6/2 | 281 |
| /pervezimu-grafikas/ | 6 | 17 % | 0 % | 67 % | 17 % | 0/4/2 | 345 |
| /siuntos-sekimas/ | 4 | 25 % | 25 % | 50 % | 0 % | 0/4/0 | 60 |
| /taisykles/ | 6 | 17 % | 50 % | 17 % | 17 % | 1/4/1 | 270 |
| /kontaktai/ | 5 | 0 % | 20 % | 80 % | 0 % | 0/5/0 | 380 |
| /privatumo-politika/ | 3 | 33 % | 33 % | 33 % | 0 % | 0/3/0 | 120 |
| 404 | 4 | 50 % | 0 % | 25 % | 25 % | 3/0/1 | 110 |
| **Iš viso** | **129** | **22 %** | **41 %** | **29 %** | **8 %** | **35/72/22** | **4 819** |

„_global“ — antraštė, meniu, poraštė, Global Sections (GS-Board, GS-Arrival, GS-Ticker, GS-CallBar) ir bendri komponentai; jie matomi kiekviename puslapyje, todėl jų CUSTOM dalis „užkrečia“ visus 21 puslapį. 11 paslaugų puslapių skaičiuojami vieną kartą (šablonas) + specialūs blokai atskirai.

### Pagrindinės išvados

- **Salient karkasas parinktas teisingai**: antraštė, off-canvas meniu, eilučių fonai (video, parallax, Slight Zoom Out Reveal, Advanced gradient), Sticky Content Sections (Sticky Media, Overlapping, Horizontal Scrolling), Tabs, Toggle Panels, Milestone, Highlighted Text, Cascading Images, Image With Hotspots, Flickity galerija ir Fluent Forms — visi egzistuoja 18.2.1 su nurodytais pavadinimais.
- **Bet išvaizdą kuria ne Salient, o savas sluoksnis**: maršruto bėgis per visą puslapį, split-flap išvykimų lenta, SVG schemos, bilietai su perforacija, mono lentelės, žiedų linijos, popover. Demo turi ≈11 800 CSS eilučių (išskleidus) ir ≈1 170 JS eilučių; ≈7 250 CSS eilučių yra grynai savas dizainas be Salient atitikmens. Ankstesniuose naudotojo projektuose Custom CSS buvo 45–89 eilutės (Augėjas, Elilė).
- **Grafikas ([sgp_grafikas]) — didžiausia ne Salient priklausomybė**: PHP trumpasis kodas + ACF Pro + JS kopija. Jį galima pakeisti dviem ranka pildomais Global Sections.
- **10 eilučių su 18.2.1 neegzistuojančiais nustatymais**: „Sticky Scroll Pinned Sections → Effect: Stacking“ (3 eilutės), „Mask Reveal“ kaip Column/Image animacija (3 eilutės, 4 vietos), mygtukų tipai „Regular“/„Line“ (3 eilutės + kontaktų grafikas), Fancy Box „minimal“ (1). Visiems yra natyvūs pakaitalai (žr. §3).
- **Artimiausias Salient demo šiai krypčiai — Harbor** (+ Tether sukrautoms kortelėms). Harbor turi tą pačią struktūrą: viršutinė Scrolling Text juosta per Global Section „In Navigation Top“, hero su apatine matinio stiklo (Backdrop Filter) juosta, Sticky Content Sections, Horizontal Scrolling, Badge etiketės, Fluent Forms. Rekomenduojama demo perdaryti kaip „Harbor + SGP spalvos/šriftai“ ir gide aprašyti „Kas pakeista lyginant su Harbor“, kaip Augėjo gide su Business 3.

## 2. 15 didžiausių nukrypimų nuo Salient

| # | Kas | Kur | Verdiktas | Kodėl tai ne Salient | Natyvus pakaitalas |
|---:|---|---|---|---|---|
| 1 | Grafiko sistema: GS-Board su split-flap plytelėmis + [sgp_grafikas] (ticker, next, board, timetable, table, stub, updated, lane) | visi 21 puslapiai (GS-Board 8 psl., ticker/next/stub visur) | CUSTOM | PHP trumpasis kodas + ACF Pro + JS kopija (sgp.js §1–2 ≈150 eil.) + ≈450 CSS eil.; split-flap nėra Salient elementas | 2 Global Sections, pildomi ranka kartą per mėnesį: GS-Board = Inner Row su Backdrop Filter „Blur“ (Harbor hero juosta) + 4 Columns (Text Block + Button „Underline“ → tel:); viršutinė juosta = Scrolling Text „In Navigation Top Before Scrolling“ vietoje; tvarkaraščiai = Horizontal List Item eilutės |
| 2 | Maršruto bėgis per visą puslapį + skyrių žymekliai (sgp-has-rail, sgp-wp, sgp-ring, rail-end) | ~70 eilučių visuose puslapiuose | CUSTOM | ≈200 CSS eil. + JS (rail-end, stops); absoliučiai pozicionuota per kelias eilutes — WPBakery trapu; stipriausias „ne Salient“ ženklas | Atsisakyti bėgio; skyrių antraštės = Badge elementas su „Inherit Typography From: Minimal Line“ (kaip Signal demo) arba etiketė + Divider |
| 3 | Raw HTML SVG maršrutų schemos, maršruto juostelės ir SVG diagramos | pradžia ×2, tarptautiniai (+2 juostelės), grafikas, kontaktai, dalinių ir siuntų paslaugos | CUSTOM | ≈210 CSS eil. žemėlapiams + ≈120 juostelėms + ~60 eil. SVG kiekvienam; klientas negali redaguoti | Eksportuoti schemą į WebP/PNG → Image With Hotspots (Hotspot Icon „Numerical“, Tooltip „Show On Hover“, Enable Animation) arba paprastas Image |
| 4 | Pradžios „paslaugų kelias“: horizontalus slinkimas su savo kortelėmis, stotelių linija ir skaitikliu „04 / 11“ | pradžia #paslaugos | CUSTOM | home.js prisegimo emuliacija + ≈380 CSS eil.; vaikai deklaruoti kaip Column Link kortelės, o Salient reikalauja „Sticky Content Section“ | Sticky Content Sections → „Horizontal Scrolling“, Section Width 26 %, Effect None, Subtract Navigation Height ✓; 11 × Sticky Content Section (Image + Link URL + Text Block/Badge); be linijos ir skaitiklio |
| 5 | Bilietų komponentai (.sgp-ticket, kt-tk, ps-tk): įpjovos, perforacija, šaknelė su kitu išvykimu | GS-Arrival (visi psl.), kontaktai, pervežimo paslaugos | CUSTOM | ≈500 CSS eil. + stub trumpasis kodas; Salient tokios formos neturi | Column su Background Color + Border (Advanced) + Button „Basic“ su telefono ikona; paslaugų plytelės = Fancy Box „Parallax Hover Effect“ |
| 6 | „Skambinti“ popover / apatinis lapas | antraštė visuose puslapiuose + „gyvūnų“ CTA | CUSTOM | Popover API + JS + ≈66 CSS eil.; 18.2.1 neturi popup/modal Global Section vietos | Meniu punktas „Skambinti“ = Mega Menu su „Mega Menu Global Section“ (GS-Telefonai); telefonuose — tas pats GS „Off Canvas Menu Meta Area“ + lipni skambučių juosta |
| 7 | Savos „linijų“ diagramos: grafiko „Laiko juosta“, taisyklių terminų juosta, 404 „4 0 4“ + nutrūkęs bėgis, „Pakeliui“ stotelės, GS-Trust žiedų linija | grafikas, taisyklės, 404, tarptautiniai, apie | CUSTOM | ≈800 CSS eil. + grafikas.js, 404.js, IO stebėtojai | Išjungti „Laiko juostą“; terminai = 3 × Milestone (0 / 5 / 14, simbolis „d.“); 404 = Animated Text; stotelės = Icon List (Number) arba HLI be linijos |
| 8 | „Sticky Scroll Pinned Sections → Effect: Stacking“ — tokio efekto nėra | apie #principai, paslaugos #visos-paslaugos, keleivių „Principai“ | WRONG-MAPPING | 18.2.1 efektai: None / Overlapping / Scale / Blurred Scale / Fade Scale + žymimasis „Stacked Appearance“; „Stacking“ yra tik Horizontal Scrolling efektas; kortelių progreso žiedai — savas CSS | Effect „Overlapping“ (arba „Scale“) + „Stacked Appearance“ ✓ (kaip Tether demo); Effect Enabled planšetėje/telefone „Disabled“; indeksą keičia „Section Navigation“ |
| 9 | „Mask Reveal“ kaip Column / Image animacija — tokios nėra | pradžia #eiga, tarptautinių skyrių nuotraukos ×2, apie GS-Trust nuotrauka | WRONG-MAPPING | Column Animation sąraše 18.2.1 nėra Mask Reveal; ji yra tik Column → Background Layer Animation (kaukė ant stulpelio FONO paveikslėlio) | Nuotrauka kaip Column Background Image + Background Layer Animation „Mask Reveal“ (kryptis Bottom, forma Straight/Circle), arba Image animacija „Reveal Rotate From Bottom“ |
| 10 | Savi lipnūs indeksai su žiedų linija ir scroll-spy | paslaugų grupių indeksas, taisyklių turinys, privatumo mini-TOC, kontaktų stotelių sąrašas | CUSTOM | ≈330 CSS eil. + taisykles.js, privatumo-politika.js, paslaugos.js, sgp.js §13 | Tabs → „Vertical Sticky Scrolling“ (taisyklėms), Pinned Sections „Section Navigation“, Page Submenu (turi įtaisytą scrollspy) arba paprastos inkaro nuorodos |
| 11 | Pradžios H1 iš Raw HTML su nupieštomis maršruto jungtimis | pradžia #pradzia | CUSTOM | Raw HTML antraštė nematoma kūrėjui, sunkiai redaguojama | Animated Text (H1, Word „Reveal“, Stagger): „Lietuva – Airija. Lietuva – Ispanija. Ir atgal.“ + pasirinktinai Highlighted Text |
| 12 | Dviejų eilučių skambučių plytelės .sgp-callbtn (raudonas kvadratas + etiketė + numeris) | kiekvienas hero, CTA blokai, GS-Arrival | NATIVE+CSS | ≈76 CSS eil.; tai ne Salient mygtuko išvaizda | Button „Basic“ + telefono ikona + Preset lg (numeris kaip tekstas), krypties etiketė — Badge virš mygtuko |
| 13 | Savas akordeono vaizdas (.sgp-acc: indeksas, skaičius skliaustuose, žiedas) | pradžia, visos 11 paslaugų, taisyklės | NATIVE+CSS | ≈80 CSS eil. + sgp.js §12; natyvus Toggle Panels atrodo kitaip | Toggle Panels „Minimal Shadow“ / „Animated Circle“ be perdarymo; gilioji nuoroda ?toggle=N |
| 14 | Mono raktų–reikšmių lentelės (.sgp-kv, ~25 vietos) + mono didžiosios raidės visur | beveik visi puslapiai | NATIVE+CSS | ≈48 CSS eil., bet vizualiai labiausiai „ne Salient“ tipografija | Horizontal List Item (Columns 2, „30% \| 70%“, „Bottom Border, No Hover Effect“); mono šriftas tik Label tipografijai (Badge, meniu meta) |
| 15 | Hover video, eilutės užvedimo nuotraukų keitimas ir savas pakreipimas (tilt) | pradžia, pervežimo paslaugos, paslaugų kortelės | CUSTOM | sgp.js §6 + paslaugos.js ≈80 JS eil. + ≈60 CSS eil. | Image hover „Zoom In Crop“, Fancy Box „Parallax Hover Effect“ (natyvus tilt), statiška nuotrauka kiekvienai grupei |

## 3. Neteisingi atitikmenys ir pataisos `salient-elementai.md` (18.3 → 18.2.1)

| Blokas | Teiginys demo žymėje | Kas iš tikrųjų yra 18.2.1 |
|---|---|---|
| / (pradžia) · #eiga process stations | Row paper · Divider (2 px accent, line animation) as lane · 3 Columns (Fade In From Bottom 0/120/240) · Image Mask Circle + Column Mask Reveal (circle) · Text Block .sgp-kv | Divider (Line Thickness 2px, Animate Line ✓) + 3 Columns 'Fade In From Bottom' + Image → Mask (Enable Mask, Shape Circle) ✓. 'Mask Reveal' is NOT a Column Animation in 18.2.1 — it exists only as Column → Background Layer Animation 'Mask Reveal' (Shape Straight/Circle) on a column BACKGROUND image |
| /apie-imone/ · #principai pinned principle cards | Sticky Content Sections → Sticky Scroll Pinned Sections · Effect: Stacking · Section Navigation OFF · effect OFF on tablet/phone | Type 'Sticky Scroll Pinned Sections', Effect 'Overlapping' (or 'Scale' / 'Blurred Scale') + 'Stacked Appearance' ✓ (Tether demo = overlapping + stacked); Effect Enabled: tablet/phone Disabled; Section Navigation off |
| /apie-imone/ · GS-Trust photo (mask reveal) | Single Image · Mask Reveal (straight, bottom) · Parallax (image scaled 1.16) | Photo as Column Background Image + Background Layer Animation 'Mask Reveal' (Direction Bottom, Shape Straight) + Background Image Parallax Scrolling ✓ — or Image Animation 'Reveal Rotate From Bottom' + Scroll Based Animation 'Move Y Axis' |
| /pervezimo-paslaugos/ · #visos-paslaugos pinned groups + index | Column 3/12: Sticky Content (CSS, Top 88) group index … (ring fills = custom JS) · Column 9/12: Sticky Content Sections → Sticky Scroll Pinned Sections · effect Stacking · Section Navigation off · effect off on tablet/phone | Pinned Sections Effect 'Overlapping' + 'Stacked Appearance' ✓; replace the custom index with 'Section Navigation' ✓ (+ Navigation Color) or a Page Submenu |
| /pervezimo-paslaugos/tarptautiniai-pervezimai/ · Chapter inset photos ×2 (mask reveal) | 2 × Image · Column Animation: Mask Reveal (bottom, delays 0/120 ms) · hover Zoom In Crop · front image parallax | Column Animation has no 'Mask Reveal' → Column Background Image + Background Layer Animation 'Mask Reveal' (Bottom), or Image Animation 'Reveal Rotate From Bottom' + Delay 0/120; Cascading Images is the closest single element |
| paslauga: specialūs blokai · gyvunu: 'Kaina' factors | Special „Kaina“ · Row dark + sgp-has-rail · Text Block (verbatim) + 3 Columns (Fancy Box minimal: icon + NEW label + fragment) · Button Underline → #uzklausa | Fancy Box has no 'minimal' style (Bottom Color Bar Hover Effect / Color Box Hover Effect / Color Box Basic / Parallax Hover Effect / Description on Hover / Image Above Text) → Text With Icon ×3, or Icon + Text Block in bordered columns |
| paslauga: specialūs blokai · keleiviu: 'Principai' pinned cards | Special „Principai“ (replaces T4) · Sticky Content Sections → Sticky Scroll Pinned Sections, effect Stacking, Section Navigation off, off on tablet/phone (M63) | Effect 'Overlapping' (or 'Scale') + 'Stacked Appearance' ✓ |
| /pervezimu-grafikas/ · Board footer button | Inner Row: Text Block (stamp + board note) · Button (Regular, Line) href=#sgp-call | The Button element has no 'Regular' or 'Line' type in 18.2.1 (Basic, See Through, Arrow Animation, Arrow Circle Animation, Curved Arrow Animation, Underline, Text Reveal Wave, Text Reveal, Material, Next Section; 'Regular' exists only in Legacy Button) → Button 'See Through' + phone icon |
| /taisykles/ · Hero with PDF button + anchor chips | Row Full Width · Route header · BG image 6169133 + Parallax + Slight Zoom Out Reveal · Color Overlay Advanced · Button (Line, download icon) → PDF · link chips = Button (Regular) to #anchors | No 'Line'/'Regular' Button types → Button 'See Through' + download icon; chips = Button 'Basic' (Preset sm) or Badge |
| 404 · 404 buttons | Button (Signal, Arrow Animation) + Button (Line) | 'Line' → Button 'See Through' |

Kitos pastabos, kurios nėra klaidos, bet keičia įgyvendinimą: Column Sticky Content neturi skaitinio „Top 120“ (poslinkis skaičiuojamas pagal antraštę); GS „Before Footer“ vadinasi „After Page/Post Content“; Off Canvas stilius vadinasi „Fullscreen Cover Split“; video išjungimas telefonuose — tik visos temos nustatymas; HD/SD video perjungimo nėra; Horizontal Scrolling vaikai turi būti „Sticky Content Section“, ne Column Link; „nectar-inline-subscribe-form“ — WPForms stiliaus klasė, ne Raw HTML formai.

Pataisos `docs/salient-elementai.md` (jis rašytas 18.3 dokumentacijai):

- **Column Animation.** Tik: None, Fade In, Fade In From Left/Right/Bottom, Slight Fade In From Bottom, Grow In, Zoom Out, Slight Twist, Flip In Horizontal/Vertical, Reveal From Right/Bottom/Left/Top. „Mask Reveal“ ir „Reveal Rotate …“ yra tik Column → Background Layer Animation (fono paveikslėliui). „Fade In From Top“ (18.3) 18.2.1 nėra.
- **Sticky Scroll Pinned Sections.** Effect: None / Overlapping / Scale / Blurred Scale / Fade Scale + žymimasis „Stacked Appearance“; Effect Enabled atskirai desktop/tablet/phone; Section Navigation + Navigation Color. „Stacking“ — tik Horizontal Scrolling efektas. Yra ir naujas tipas „Layered Card Reveal“.
- **Horizontal Scrolling.** Section Width — slankiklis 25–100 % (ne vw); Effect None / Stacking; Section Gap; vaikai — „Sticky Content Section“ (konteineris su Image/Video/Color + Link URL) arba vc_row.
- **Tabs / Toggle Panels gilioji nuoroda.** Salient skaito užklausos parametrus, ne #hash: ?tab=<skirtuko-pavadinimas-slug>, ?toggle=<numeris arba pavadinimas>&focus=true.
- **Button tipai.** Basic, See Through, Arrow Animation, Arrow Circle Animation, Curved Arrow Animation, Underline, Text Reveal Wave, Text Reveal, Material, Next Section. „Regular“, „Line“ nėra (Regular — tik Legacy Button).
- **Fancy Box stiliai.** Bottom Color Bar Hover Effect, Color Box Hover Effect, Color Box Basic, Parallax Hover Effect, Description on Hover, Image Above Text, Additional Brands. „Minimal“ nėra.
- **Horizontal List Item.** „Style“ reikšmės: Bottom Border, Color Hover Effect / Bottom Border, No Hover Effect / Full Border; „Border Animation“ — atskiras žymimasis. Iki 4 stulpelių su išdėstymais (pvz. 30% | 70%), Full Item Link URL, 2 CTA.
- **Image elementas.** Animacijos: Fade In (4 kryptys), Grow In, Slide Up, Flip In H/V, Reveal Rotate From Top/Bottom/Left/Right; Mask grupė (forma Circle ir kt.) — statinė kaukė, ne atsiradimo animacija; Scroll Based Animation Move Y/X.
- **Row aukštis.** Height / Min Height per įrenginį (svh/dvh) rodomi tik kai „Full Height Row“ išjungtas; video išjungimas telefonuose — tik visos temos nustatymas „Disable Video Backgrounds On Mobile Devices“.
- **Global Section vietos.** In Navigation Top, In Navigation Top Before Scrolling, After Navigation, Before/After Page/Post Content, Sidebar Top/Bottom, Before/After Blog Loop, 404 Content, Before/After Off Canvas Menu Items, Off Canvas Menu Meta Area, Footer, Footer Parallax, After Footer (+ Woo/Portfolio). „Before Footer“ ir popup/modal vietos nėra.
- **Kiti naudingi elementai.** Badge (su „Minimal Line“ — skyrių antraštėms), Scrolling Text (Harbor viršutinė juosta), Responsive Text, Icon List Item su „Number“ tipu, Page Submenu su įtaisytu scrollspy, Mega Menu Global Section meniu punkte.
- **Sklandus slinkimas ir perėjimai.** Theme Options „Smooth Scrolling“ naudoja Lenis (nectar-smooth-scroll.js); Page Transitions „View Transitions API (Modern)“ su efektais Fade / Horizontal Gradient Wipe / Vertical Reveal Scale / Vertical Reveal.
- **Duonos trupiniai.** Salient automatiškai įterpia tik Yoast breadcrumbs (nectar_yoast_breadcrumbs); Rank Math — per [rank_math_breadcrumb] Text Block'e.

## 4. Savas (custom) sluoksnis

### 4.1 CSS

Išmatuota išskleidus taisykles (1 selektorius + deklaracijos + uždarymas = eilutės).

| Failas | Eilučių (išskleidus) | Kas ten |
|---|---:|---|
| tokens.css | 160 | Theme Options (spalvos, tipografija) + ~40 eil. kintamųjų |
| base.css | 298 | didžioji dalis — Salient tinklelis/tipografija |
| motion.css | 294 | Salient animacijos; lieka tik odometras ir linijų piešimas |
| components.css | 3341 | bėgis, lenta, bilietai, žemėlapiai, stotelės, skambučių plytelės, popover, meniu diagrama |
| pages/*.css (11 failų) | 7709 | puslapių specifika: home 1117, paslauga 1530, tarptautiniai 915, sekimas 793, paslaugos 665, kontaktai 599, apie 573, taisyklės 572, grafikas 479, privatumo 310, 404 156 |
| **Iš viso** | **11802** | ≈240 KB |

Suskirsčius pagal komponentus: **≈7 250 eil.** — savas dizainas be Salient atitikmens (bėgis, lenta, bilietai, žemėlapiai, stotelės, linijų diagramos, savi indeksai, skambučių plytelės); **≈3 860 eil.** — Salient atkartojimas (antraštė, meniu, mygtukai, formos, skirtukai, akordeonai, tinklelis, animacijos, sticky media, hotspot'ai, galerija), kurį Salient padaro pats; **≈690 eil.** — tik demo (sekimo būsenos, „Salient žymės“, privatumo vietos rezervavimas). Jei dizainas liktų kaip dabar, į Theme Options → Custom CSS / vaikinę temą reikėtų perkelti **≈5 000–6 000 eilučių** (dalį savų komponentų išdėstymo perimtų stulpeliai). Pritaikius šiame audite siūlomus pakaitalus lieka **≈300–450 eilučių** (žetonai, Badge/mono etiketės, skambučių mygtukai, formos laukai, keli akcentai).

### 4.2 JS

`assets/js/sgp.js` — 641 kodo eilutė (44,7 KB), puslapių JS — 535 eilutės (35 KB). Salient'e reikalingas savas JS, jei dizainas liktų kaip dabar: ≈350 eilučių + PHP trumpasis kodas; su pakaitalais — 0–20 eilučių (nebent video pauzės mygtukas ir sekimo iframe).

| Failas / modulis | Funkcija | Salient daro pats? | Salient atitikmuo | Eil. |
|---|---|---|---|---:|
| sgp.js §1 | Grafiko atvaizdavimas pagal lankytojo datą ([sgp_grafikas] veidrodis, 7 variantai) | Ne | PHP trumpasis kodas + ACF arba ranka pildomi Global Sections | ≈120 |
| sgp.js §1 | fitTicker — netelpantys bėgančios juostos punktai slepiami | Ne | Scrolling Text (marquee) nereikia skaičiavimo | ≈8 |
| sgp.js §2 | Split-flap plytelės | Ne | — | ≈25 |
| sgp.js §3 | Žodžių skaidymas / blur žodžiai | Taip | Animated Text (Reveal / Blur, Stagger) | ≈15 |
| sgp.js §3 | Odometro skaitikliai (data-reel) | Ne (kitas efektas) | Milestone „Count To Value“ / „Motion Blur Slide In“ | ≈6 |
| sgp.js §4 | Atsiradimo animacijos (IO → .in), kaukės | Taip / iš dalies | Column/Image animacijos; kaukė — Image Mask + Column BG „Mask Reveal“ | ≈45 |
| sgp.js §5 | Fono video: lazy, tik desktop, pauzė už ekrano | Iš dalies | Background Video Loading „Lazy Load“ ✓, tema „Disable Video Backgrounds On Mobile“ ✓; HD/SD perjungimo ir pauzės mygtuko nėra | ≈30 |
| sgp.js §6 | Hover video kortelėse | Ne | — | ≈12 |
| sgp.js §7 | Antraštė: stiklas, slėpimas, perspalvinimas virš šviesių eilučių; Mega Menu Esc | Taip | Header Blur Background, Hide Until Needed, Permanent Transparent + Row Text Color | ≈40 |
| sgp.js §8 | „Skambinti“ popover | Ne | Mega Menu Global Section | ≈15 |
| sgp.js §9 | Off-canvas meniu: fokusas, Esc, scroll lock | Taip | Off Canvas Menu (Fullscreen Cover Split) | ≈30 |
| sgp.js §10 | Bėgio stotelės (is-reached, skaitiklis) | Ne | — | ≈10 |
| sgp.js §11 | Skirtukai + #hash gilioji nuoroda | Taip | Tabs; gilioji nuoroda ?tab=<pavadinimo-slug> | ≈25 |
| sgp.js §12 | Akordeonas + #hash | Taip | Toggle Panels; ?toggle=N (&focus=true) | ≈20 |
| sgp.js §13 | Scroll spy (submeniu, lipnūs indeksai, sticky media) | Iš dalies | Page Submenu scrollspy ✓, Sticky Media ✓; savi indeksai — ne | ≈45 |
| sgp.js §14 | Formų validacija, {domina} parinkimas, siuntos kodo laukas | Taip (Fluent Forms) | Fluent Forms validacija, numatytoji reikšmė {get.domina}, peradresavimas | ≈60 |
| sgp.js §14 | El. pašto kopijavimo mygtukas | Ne | mailto nuoroda | ≈10 |
| sgp.js §15 | Bėgio pabaiga (terminus) | Ne | — | ≈5 |
| sgp.js §16 | Slapukų juosta | Įskiepis | Complianz / CookieYes | ≈10 |
| sgp.js §17 | „Salient žymės“ kūrėjo sluoksnis | Tik demo | — | ≈50 |
| sgp.js §18 | Parallax, scroll-scale, sukrautos kortelės | Taip | Parallax BG, Column „Scroll Position Advanced“, Sticky Scroll Pinned Sections | ≈40 |
| sgp.js §20 | Lenis sklandus slinkimas + inkarų poslinkis | Taip | Theme Options „Smooth Scrolling“ (Lenis viduje nectar-smooth-scroll.js) + „One Page Scroll Support“ | ≈35 |
| home.js | Horizontalaus kelio prisegimas + klaviatūros fokusas | Taip (fokusas — ne) | Sticky Content Sections → Horizontal Scrolling | 43 |
| apie.js | Flickity galerija, vaizdo parallax, tempimo indikatorius | Taip | Image Gallery „Flickity Style“ + Image Parallax + Touch Indicator | 87 |
| paslaugos.js | Pakreipimas (tilt), grupių nuotraukų keitimas + hover video, indekso spy | Tilt — taip; kita — ne | Fancy Box „Parallax Hover Effect“; Section Navigation | 83 |
| tarptautiniai.js | Hotspot'ai, persidengiantys skyriai | Taip | Image With Hotspots; Pinned Sections „Overlapping“ | 50 |
| paslauga.js | Formos parinkimas, sticky media, hotspot'ai, dokumentų varnelės (localStorage) | Taip, išskyrus varneles | Fluent Forms, Sticky Media Scrolling Content, Image With Hotspots | 101 |
| grafikas.js | Laiko juostos etikečių išdėstymas | Ne | — | 28 |
| sekimas.js | Demo sekimo būsenos; ?kodas= → paieška | Tik demo / ne | Raw HTML iframe arba peradresavimas | 66 |
| taisykles.js | Turinio linijos pildymas skaitant | Ne | Tabs „Vertical Sticky Scrolling“ | 46 |
| kontaktai.js | Bėgio terminus, greito skambučio paryškinimas | Ne | — | 39 |
| privatumo-politika.js | Skaitymo progreso linija, slapukų juostos atidarymas | Ne / įskiepis | Complianz „Manage consent“ | 23 |
| 404.js | „Klaidingo posūkio“ bėgio animacija | Ne | — | 18 |

## 5. Kryptis: kaip demo priartinti prie Salient

1. **Bazė — Harbor demo** (Salient → Demo Importer → Harbor): viršutinė Scrolling Text juosta (GS „In Navigation Top“), foto/video hero su apatine Backdrop Filter juosta (čia — artimiausi pervežimai, pildomi ranka), Sticky Content Sections, Horizontal Scrolling paslaugoms, Badge etiketės, Fluent Forms. Sukrautoms kortelėms — Tether nustatymas (Pinned Sections „Overlapping“ + „Stacked Appearance“).
2. **Išlaikyti SGP tapatybę Theme Options priemonėmis**: Accent #EF4539, tamsus asfaltas / šviesus popierius per Row fonus ir Text Color, Barlow Condensed antraštės, IBM Plex Mono tik Label tipografijai (Badge, meniu meta). Tinklelį (graticule) — kaip pasikartojantį fono paveikslėlį arba atsisakyti.
3. **Signatūrinius elementus sumažinti iki 2 natyvių**: (a) maršruto schema kaip paveikslėlis + Image With Hotspots; (b) raudona Highlighted Text „Regular Underline“ pabraukimo linija. Bėgio, split-flap, bilietų, žiedų linijų ir popover atsisakyti.
4. **Grafikas be PHP**: du Global Sections (lenta ir tvarkaraštis) su Horizontal List Item eilutėmis; datos atnaujinamos vienoje vietoje. Jei klientas nori automatinio „Artimiausias“ — tik tada vienas mažas trumpasis kodas.
5. **Demo žymes (`data-salient`) pataisyti pagal §3** ir perrašyti README/salient-elementai.md iš „18.3“ į „18.2.1“.

## 6. Visi blokai

### _global (visi puslapiai)

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| header #sgp-hdr | NATIVE | yes | Logo left, centred menu, red 'Skambinti' button; transparent over the hero, glass blur + hides on scroll-down, recolours over light rows | Theme Options → Header Navigation: Header Layout 'Centered Menu' (centered-menu); Header Permanent Transparent ✓; Header Hide Until Needed ✓; Header Resize On Scroll ✓; Header Blur Background ✓ (Functionality 'Active when not at the top of the page'); Header Link Hover/Active Effect 'Animated Underline'; row Text Color Light/Dark drives the recolouring | 10 | All option ids verified in options-config.php (header_format, header-permanent-transparent, header-hide-until-needed, header-resize-on-scroll, header-blur-bg, header-hover-effect). 84→64 = header padding + 'Header Logo Shrink Number'. Demo hdr/nav CSS (~110 lines) and sgp.js §7 are replaced by the theme. |
| GS-Ticker (top strip 'Artimiausi išvykimai') | CUSTOM | partly | Dark strip above the header: 3 next departures with live dates and relative days + 'VISAS GRAFIKAS →' | Global Section at location 'In Navigation Top Before Scrolling' (label verified) with a Scrolling Text element (Harbor demo 'Harbor Secondary Nav' pattern: speed Slow, Custom Symbol divider, Mask Edges) and the dates typed once a month; or Theme Options → Secondary Header Bar (text + link) | 20 | The location exists; the content does not — it needs the custom PHP shortcode + ACF. fitTicker JS becomes unnecessary with Scrolling Text. |
| Mega menu 'Pervežimo paslaugos' | NATIVE+CSS | yes | 3-column dark mega menu, 6 service groups, 2 px red top border | Appearance → Menus → Salient menu-item options: 'Enable Mega Menu', 'Mega Menu Width', 'Mega Menu Column Width', 'Mega Menu Column Background Color' (or 'Mega Menu Global Section'); dropdown colours in Theme Options | 12 | Esc/hover behaviour is Salient's own; only the red top border + mono group headings need CSS. |
| Header button 'Skambinti' | NATIVE | yes | Red button in the menu bar | Menu item option 'Menu Item Link Button Style' (+ 'Persist In Mobile Navigation Header' for phones) | 0 | The button is native; what it opens (popover) is not — see next row. |
| Switchboard popover #sgp-call | CUSTOM | no | Dropdown (desktop) / bottom sheet (phone) with 5 phone numbers grouped by direction | Make 'Skambinti' a Mega Menu item whose content is a Global Section ('Mega Menu Global Section' = GS-Telefonai with Buttons → tel:). Phones: same GS in 'Off Canvas Menu Meta Area' + the sticky call bar | 66 | Salient 18.2.1 has no popup/modal Global Section location (global-sections/display-options.php). Popover API + JS + ~66 lines CSS. |
| Off-canvas menu #sgp-menu | NATIVE+CSS | partly | Fullscreen split menu: left = menu drawn as a route diagram with rings, right = phones + e-mail | Theme Options → Off Canvas Menu Style 'Fullscreen Cover Split' (exact label); right column = Global Section at 'Off Canvas Menu Meta Area' or 'After Off Canvas Menu Items'; drop the line diagram | 60 | Focus trap, Esc, scroll lock are Salient's (sgp.js §9 not needed). The route-diagram styling (~60 of 122 demo lines) is the only custom part. |
| Footer | NATIVE+CSS | partly | 5-column dark footer: logo + text + e-mail, 2 phone columns with mono country codes, services and info lists with ring bullets | Global Section at location 'Footer' (verified) with 5 Columns: Text Block, Buttons/Icon List for phones, WP Custom Menu for the two lists | 45 | .sgp-line-list ring bullets + mono codes ≈45 lines; plain lists = 0. |
| GS-CallBar (sticky call bar <1000 px) | NATIVE+CSS | yes | Bottom bar with two equal call buttons on tablet/phone | Row → Advanced: Sticky Row ✓, Sticky Alignment 'Bottom of Window', 'Sticky Row on Mobile' ✓; Device Visibility: Desktop Hidden | 25 | sticky_row, sticky_row_alignment=bottom, sticky_row_mobile, device_visibility_* verified in nectar-addons.php. |
| Cookie consent #sgp-cookie | NATIVE+CSS | partly | Bottom-left dark card with red top border: Sutinku / Atmesti / Plačiau | Complianz or CookieYes banner (plugin), colours in the plugin, a few CSS lines | 30 | Not a Salient feature; plugin-native. |
| GS-Board 'Artimiausi pervežimai' (departure board, 8 pages) | CUSTOM | no | Frosted dark band with 4 route cells: split-flap date tiles, relative days, 'Artimiausias' highlight, later dates, tel: links | Global Section = Row + Inner Row with Design options → Backdrop Filter 'Blur' (verified) — the Harbor demo hero band — holding 4 Columns: Text Block (route + dates typed once) + Button 'Underline' → tel:. Drop split-flap tiles and the automatic 'Artimiausias' | 190 | Backdrop filter exists on Inner Row. Board content needs the PHP shortcode + ACF + flap JS (~25 lines) + CSS board/bcell/fc/sched ≈190 lines. |
| [sgp_grafikas] shortcode family (ticker, next, board, timetable, table, stub, lane, updated) | CUSTOM | no | Server-rendered schedule in 8 variants, data from an ACF options page; client JS re-renders by visitor date | Drop it or keep ONE small variant. Maintain the dates as text in 2 Global Sections (GS-Board, GS-Grafikas) reused everywhere; timetables = Horizontal List Items | 250 | Needs child-theme PHP (~150–250 lines) + ACF Pro + sgp.js §1 mirror (~120 lines). The largest non-Salient dependency of the build. |
| sgp-next strip (<1000 px) | CUSTOM | no | Mobile strip under each hero: 'Artimiausias išvykimas …' | Drop (sticky call bar + GS-Board cover it) or a Text Block in a row hidden on desktop | 31 |  |
| Hero call ticket .sgp-callbtn (all heroes + CTAs) | NATIVE+CSS | partly | Two call buttons: red square phone tile + mono label 'PERVEŽIMAI Į AIRIJĄ' + large number | Button → Type 'Basic', icon phone (left), Preset lg, text = the number; the direction label as a small Text Block/Badge above | 60 | A 2-line tile button (icon block + label + number) is not a Salient button look; demo CSS ~76 lines. |
| Route rail + chapter waypoints (.sgp-has-rail, .sgp-wp, .sgp-ring) | CUSTOM | no | Red vertical rail at the left edge through every page; numbered chapter markers ('02 PASLAUGOS' + hairline + meta); rings that fill; terminus ring at 'Atvykimas' | Drop the rail. Chapter eyebrows = Badge element with 'Inherit Typography From: Minimal Line' (Signal demo uses 30 Badges) or a label Text Block + Divider | 200 | ≈200 CSS lines + sgp.js rail-end/stops. Positioned across rows — fragile in WPBakery (overflow/z-index per row). The single strongest 'not Salient' signal. |
| Graticule grid on paper rows | NATIVE | partly | Faint 1 px grid over the light rows | Row → Background Image = tiled grid PNG/SVG + Background Repeat 'Repeat' (or drop) | 0 | Demo draws it with CSS gradients; as a repeated background image it is native. |
| Key/value tables .sgp-kv (~25 instances) | NATIVE+CSS | partly | Mono uppercase key + value rows with hairlines (facts, delivery terms, fines) | Horizontal List Item ×n: Columns 2, Column Layout '30% \| 70%', Style 'Bottom Border, No Hover Effect', Inherit Font From p/h6 | 48 | HLI column layouts verified (nectar_horizontal_list_item.php) → can be fully native. |
| Chips .sgp-chips | NATIVE+CSS | partly | Mono outlined chips ('NUO DURŲ IKI DURŲ', '3–4 PAROS') | Badge element (Display Inline, Border ✓, Border Radius 0px, Inherit Typography From 'Label') | 10 |  |
| Callouts .sgp-callout | NATIVE+CSS | yes | Box with 3 px red left bar and 'SVARBU' label | Inner column with Background Color + Border Type 'Advanced' (left 3 px, accent) — native — or keep a 10-line class | 10 | Per-side column borders (border_left_desktop …) verified. |
| ✕ lists .sgp-xlist | NATIVE | yes | Lists with circled ✕ icons in 2 columns, staggered entrance | Fancy Unordered List → Icon Type 'Font Icon' (times-circle), Enable Animation + Animation Delay | 5 |  |
| GS-ServiceList (11 services) | NATIVE+CSS | yes | 11 services as a numbered line list with arrows, 2 columns | Horizontal List Item ×11: Columns 2 ('20% \| 80%'), Full Item Link URL, Style 'Bottom Border, Color Hover Effect' + 'Border Animation' ✓ | 15 | Label fix: 'Border Animation' is a checkbox; Style values are 'Bottom Border, Color Hover Effect' / 'Bottom Border, No Hover Effect' / 'Full Border'. |
| Link cards .sgp-card | NATIVE+CSS | partly | Image 16:11 + mono index + H3 + summary + square arrow | Fancy Box → Style 'Image Above Text' (Image Aspect Ratio, Link URL) or Column Link + Image (hover 'Zoom In Crop') | 30 |  |
| Crop marks on photos (.sgp-crop) | NATIVE+CSS | no | Printer's crop marks at image corners | Drop; use Image Box Shadow / Border Radius instead | 25 | Pure CSS decoration with no Salient counterpart. |
| Buttons .sgp-btn (signal + arrow cell) | NATIVE+CSS | partly | Square red buttons with a separate arrow cell ('Gauti pasiūlymą \| →'), outline variant | Button Type 'Arrow Animation' or 'Basic' + icon right; Theme Options → Button Styling 'Default' + Button Roundness 0; colours = Accent | 20 | The split arrow cell is a custom look. |
| Typography & colour tokens | NATIVE | partly | Barlow Condensed display, Barlow body, IBM Plex Mono labels; asphalt / paper / signal-red palette | Theme Options → Typography (H1–H6 Barlow Condensed, Body Barlow, Label + Navigation meta IBM Plex Mono) + Accent Color #EF4539 + Extra Colors + Overall BG | 40 | Keep only a few CSS variables. The heavy use of mono uppercase (labels, kv keys, nav meta, counters) is the most visible non-Salient trait — use it sparingly. |
| Breadcrumbs .sgp-crumbs | NATIVE+CSS | yes | Pradžia → … with a red end dot | Salient auto-inserts Yoast breadcrumbs (nectar_yoast_breadcrumbs hook); with Rank Math put [rank_math_breadcrumb] in a Text Block | 20 |  |
| Split-flap tiles .sgp-flap (route codes, dates, 404) | CUSTOM | no | Characters flip like an airport board once on desktop | Plain text; numbers → Milestone 'Count To Value' / 'Motion Blur Slide In' | 31 | sgp.js §2 ≈25 lines JS. |
| Hover videos on cards/tiles | CUSTOM | no | Muted clip plays on hover in service cards, tiles, group images | Drop; Image hover 'Zoom In Crop' or Fancy Box 'Parallax Hover Effect' | 15 | Salient has hover media only for menu items ('Media Hover'). |
| Video pause button .sgp-vctl | CUSTOM | partly | 'II PAUZĖ' mono toggle on autoplay video rows (WCAG 2.2.2) | Keep as tiny Raw HTML + ~20 JS lines, or use clips ≤5 s / Self Hosted Video Player with controls | 19 | Salient row video backgrounds have no pause control. |
| Motion system (reveals, masks, parallax, scroll-scale, stacking, Lenis, page transition) | NATIVE | yes | Word reveals, fade-ups with stagger, parallax, scroll-scale, stacked cards, smooth scroll, page transition | Column Animation + Delay, Animated Text, Image animations, Row/Column Parallax BG, Column 'Scroll Position Advanced', Theme Options 'Smooth Scrolling' (Lenis inside nectar-smooth-scroll.js), Page Transitions 'View Transitions API' → 'Vertical Reveal' | 0 | Pure emulation — replaced 1:1 by the theme (the odometer reel and CSS lane draws excepted). |
| GS-Arrival 'Atvykimas' section | NATIVE+CSS | partly | Dark bokeh row before the footer: H2 'Susisiekite su mumis…', 2 call tickets left, form right | Global Section at location 'After Page/Post Content' (or Theme Options → Global Sections → 'After Page Content') — there is no 'Before Footer' label; Row BG image + Color Overlay + Parallax Subtle ✓ | 20 | Location label corrected; tickets and form are separate rows. |
| GS-Arrival call tickets .sgp-ticket + stub | CUSTOM | no | Ticket cards with perforation/notches and a stub 'KITAS IŠVYKIMAS · Spalio 9 d. · SKAMBINTI' | Column with Background Color + Border + Button 'Basic' (icon phone); drop the stub | 150 | Ticket CSS ≈123 lines + stub shortcode. |
| Enquiry form (Fluent Forms) .sgp-form | NATIVE+CSS | partly | Dark form, mono labels inside fields, 'Kas Jus domina?' select, red submit with arrow cell | Fluent Forms (Harbor/Signal demos ship Fluent Forms JSON) + Theme Options: Overall Form Style 'Minimal', Enable Fancy Select Styling ✓, Form Submit Button Style 'Nectar Button'; default value {get.domina} | 60 | Label-inside-field layout ≈60 lines; otherwise native. |

### / (pradžia)

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| #pradzia hero row | NATIVE | yes | Full-height video hero, dark gradient overlay, content at the bottom | Row: Video BG (MP4 + WebM + Video Preview Image, loading Lazy Load), Parallax Background Media On Scroll 'Subtle', Color Overlay Type 'Advanced', Text Color Light. Height: either 'Full Height Row' + Column Alignment 'Bottom', or (for svh) leave Full Height off and set Height/Min Height 100svh | 0 | The Height/Min Height group only appears when Full Height is OFF (height_group dependency). Phones: theme-wide 'Disable Video Backgrounds On Mobile Devices'. |
| Hero H1 route rows (.sgp-h1-route) | CUSTOM | no | H1 'Lietuva ○──● Airija. / Lietuva ○──● Ispanija. / Ir atgal.' with drawn connectors | Animated Text (H1, Word Animations 'Reveal', Stagger ✓): 'Lietuva – Airija. Lietuva – Ispanija. Ir atgal.'; optional Highlighted Text on 'Ir atgal.' | 28 | Raw HTML headings are invisible to the builder and hard for the client to edit. |
| Hero call buttons + 'Visas pervežimų grafikas' | NATIVE+CSS | partly | Two red-tile call buttons + underline link | Button 'Basic' + phone icon (see global .sgp-callbtn row); Button 'Underline' ✓ | 5 | CSS counted in the global .sgp-callbtn row. |
| #apie row | NATIVE | yes | Light paper row: statement + text + facts left, layered photos right | Row Type 'Full Width Background', BG colour, Text Color Dark (graticule/rail → global rows) | 0 |  |
| Statement with red underline | NATIVE | yes | Large statement, key phrase underlined in red (draws in) | Highlighted Text → Style 'Regular Underline', Underline Thickness '3px', Highlight Color #EF4539 | 0 | style=regular_underline and underline_thickness 3px verified. |
| Cascading photos | NATIVE+CSS | yes | Two overlapping photos with parallax and crop marks | Cascading Images: Image #1 CSS Animation 'Grow In Reveal', Image #2 'Fade In From Bottom', Enable Parallax Scrolling ✓ (Intensity Subtle); drop the crop marks | 25 | All options verified in nectar_cascading_images.php. |
| Milestones ×4 | NATIVE+CSS | partly | Stats 2 / 11 / 3–4 / 4 rolling like an odometer, short red marker on a top rule | Milestone: Animation Effect 'Motion Blur Slide In' (or 'Count To Value'), Animation Delay 0/150/300/450; top rule = Column border top | 15 | The demo animates with a custom odometer (data-reel) — the Salient build will look different (motion blur). Make the demo use the real effect. |
| #paslaugos horizontal services road | CUSTOM | partly | Pinned horizontal track of 11 service cards on a red lane with stop rings and a '04 / 11' counter | Sticky Content Sections → Type 'Horizontal Scrolling', Section Width 26 (slider 25–100 %, unit %), Effect 'None', Subtract Navigation Height ✓; 11 × 'Sticky Content Section' children (Section Type Image + Link URL) with Text Block + Badges inside; drop the lane, rings and counter | 150 | Children must be 'Sticky Content Section' elements (as_parent: nectar_sticky_media_section, vc_row) — not Column Link cards. Demo = home.js pin emulation (43 lines) + ≈380 CSS lines. |
| Services counter '01 / 11' | CUSTOM | no | Large mono counter that follows the stops | Static Text Block '11 paslaugų' or drop | 10 |  |
| #marsrutai route tabs | NATIVE+CSS | partly | Two-tab switch Airija / Ispanija; each tab = map 7/12 + dates and phones 5/12 | Tabs → Style 'Toggle Button' (exactly two tabs), Tab Change Animation 'Fade'. Deep link = ?tab=airija (init.js reads ?tab=<tab-title-slug>), not #hash | 20 | Demo tab look is custom (h-rtab). The maps inside are a separate row. |
| SVG route maps ×2 (.sgp-map) | CUSTOM | no | Hand-drawn SVG schematic (LT–PL–DE–BE–FR–ES / IE) with drawing route line, mono labels, legend | Export each map as WebP/PNG → Image With Hotspots (Hotspot Icon 'Numerical', Tooltip 'Show On Hover', Enable Animation ✓) or a plain Image with 'Reveal Rotate From Bottom' | 210 | Map CSS (sgp-map + mapsvg) ≈210 lines + ~60 lines SVG per map; the same map appears on 5 pages. |
| #kelioneje cinematic video row | NATIVE+CSS | partly | Video row, H2 blurs in, 5 comfort icons in red outlined squares on a scroll-driven lane | Row options verified (Parallax 'Medium', Background Layer Animation 'Zoom Out Slowly', Animated Text Word 'Blur'); comfort list = Icon List (Direction Horizontal, Columns 5, Icon Style 'Icon Colored W/ BG'); drop .sgp-stops | 60 | BG Layer Animation animates the image layer — check it with a video BG on the build. |
| #eiga process stations | WRONG-MAPPING | partly | 3 stations on a red lane: round photo, number, title, text + delivery facts | Divider (Line Thickness 2px, Animate Line ✓) + 3 Columns 'Fade In From Bottom' + Image → Mask (Enable Mask, Shape Circle) ✓. 'Mask Reveal' is NOT a Column Animation in 18.2.1 — it exists only as Column → Background Layer Animation 'Mask Reveal' (Shape Straight/Circle) on a column BACKGROUND image | 40 | Station rings/labels CSS ≈130 lines in the demo. |
| #pries-siunciant rules accordion | NATIVE+CSS | partly | Dark texture row: sticky heading + callout + button left; numbered accordion right ('Draudžiama siųsti (12)' …) | Toggle Panels Style 'Minimal Shadow' (or 'Minimal'), Accordion Toggles 'Allow', Starting 'First Toggle Open'; Column Sticky Content (CSS Powered, Alignment Top) — there is no numeric 'Top 120' (offset follows the header); deep link = ?toggle=1 | 40 | Demo accordion (index '01', count '(12)', ring state) is the custom .sgp-acc look (~80 lines); native Minimal Shadow looks different. |
| #siuntos-sekimas tracking strip | CUSTOM | partly | Tracking-code field + red button → /siuntos-sekimas/?kodas= | Fluent Forms, 1 required field, Confirmation 'Redirect to URL' /siuntos-sekimas/?kodas={inputs.kodas} | 30 | 'nectar-inline-subscribe-form' comes from Salient's WPForms stylesheet (css/build/third-party/wpforms.css) — it styles WPForms only, not a Raw HTML form. |
| Reviews placeholder | NATIVE | yes | Dashed placeholder 'Čia bus tikri klientų atsiliepimai' | Row → 'Disable row' ✓ until reviews exist; then Testimonial Slider Style 'Minimal' ✓ | 0 |  |

### /apie-imone/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Hero (route header) | NATIVE+CSS | partly | Photo header with breadcrumb, eyebrow, H1, chips, call ticket on the right | All row options verified (bg_image_animation 'slight-zoom-out-reveal', bg_position custom); chips → Badge; calls → Button | 20 | Route-header layout CSS ≈110 lines in the demo, mostly replaced by columns. |
| #imone company row | NATIVE | yes | Statement + text 7/12, sticky facts 4/12 with offset | Column offset via 'Responsiveness' ✓; Sticky Content (CSS Powered) ✓ — no numeric top | 0 |  |
| ab-promise mini route | NATIVE+CSS | partly | Display line + mini route: origin ring → red lane → destination ring | Divider with Animate Line ✓; drop the rings | 30 |  |
| Buttons under the text | NATIVE | yes | Red 'Pervežimo paslaugos' button with arrow + underline link | Button Type 'Arrow Animation' (Accent Color) + Button Type 'Underline' | 0 |  |
| Milestones ×4 | NATIVE+CSS | partly | Same stats as home with top rule + red marker | Milestone 'Motion Blur Slide In' + delays; rule = column border | 15 | Same odometer divergence as home. |
| #principai pinned principle cards | WRONG-MAPPING | partly | 5 principle cards pinned and stacking (index, H3, text, progress rings, image 5/12) | Type 'Sticky Scroll Pinned Sections', Effect 'Overlapping' (or 'Scale' / 'Blurred Scale') + 'Stacked Appearance' ✓ (Tether demo = overlapping + stacked); Effect Enabled: tablet/phone Disabled; Section Navigation off | 60 | Pinned-section effects are None / Overlapping / Scale / Blurred Scale / Fade Scale — 'Stacking' exists only for Horizontal Scrolling. Card progress rings (ab-card ≈135 lines) are custom. |
| #kelyje photo gallery | NATIVE | partly | Draggable photo slider with '01 / 05' counter and arrows, image parallax, masked edges | Image Gallery Type 'Flickity Style', Controls 'Touch Indicator and Total Visualized', Image Parallax ✓, Mask Edges ✓, Subtle Image Scale When Dragging ✓ | 0 | All verified. The demo draws its own counter/arrows (apie.js 87 lines, ~150 CSS) — accept Salient's indicator look. |
| #pasitikejimas GS-Trust | CUSTOM | partly | Dark texture row: sticky heading + masked photo left; 9 numbered reasons on a lane whose rings fill at 70 % of the viewport | Keep 9 × Horizontal List Item (Columns 2 '20% \| 80%', Style 'Bottom Border, No Hover Effect', Border Animation ✓); drop the stops lane and its IntersectionObserver | 40 | HLI label fix (Style vs Border Animation). Lane ≈150 CSS lines + JS. |
| GS-Trust photo (mask reveal) | WRONG-MAPPING | partly | Photo revealed by a mask from the bottom, with parallax | Photo as Column Background Image + Background Layer Animation 'Mask Reveal' (Direction Bottom, Shape Straight) + Background Image Parallax Scrolling ✓ — or Image Animation 'Reveal Rotate From Bottom' + Scroll Based Animation 'Move Y Axis' | 0 | The Image element (image_with_animation) has no Mask Reveal animation in 18.2.1. |

### /pervezimo-paslaugos/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Hero (route header + breadcrumbs) | NATIVE+CSS | partly | Photo header, breadcrumb, H1, chips, call ticket | Verified row options; breadcrumbs per global row | 20 |  |
| Ticket tiles row (3 entry tiles) | CUSTOM | no | 3 ticket-shaped tiles (notches + perforation) that tilt; tile 1 plays a hover video, tile 2 shows the live next departure | 3 × Fancy Box Style 'Parallax Hover Effect' (image, overlay, Link URL) as Salient renders it — no notches, no live date, no video | 120 | Fancy Box parallax_hover verified; the demo re-implements the tilt (paslaugos.js) + ps-tk ≈206 CSS lines. |
| #visos-paslaugos pinned groups + index | WRONG-MAPPING | partly | Sticky left index with filling rings + 6 group cards pinned and stacking | Pinned Sections Effect 'Overlapping' + 'Stacked Appearance' ✓; replace the custom index with 'Section Navigation' ✓ (+ Navigation Color) or a Page Submenu | 80 | 'Stacking' is not a pinned-sections effect; index ring JS custom (ps-idx ≈93 CSS lines). |
| Group child sections ×6 | CUSTOM | partly | Each group: 4:5 image (swaps on row hover, hover video) + heading + service rows with arrows | Child = vc_row (allowed child) with Image + Horizontal List Items (Full Item Link URL ✓); one static image per group | 60 | ps-grp + ps-row ≈260 CSS lines + paslaugos.js media swap. |
| CTA 'Nežinote, kurią paslaugą rinktis?' | NATIVE+CSS | partly | Statement + 2 call buttons | Text Block + 2 × Button 'Basic' with phone icon | 5 |  |
| #kryptys why row | NATIVE | yes | Sticky H2 left; text + photo scaling in on scroll + facts | Column Animation Type 'Scroll Position Advanced' (Animation State start/end: Scale, Translate Y) ✓; Image hover 'Zoom In Crop' ✓ | 0 | animation_adv_start_end + start/end scale verified in vc_column params. |

### /pervezimo-paslaugos/tarptautiniai-pervezimai/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Hero (video route header) | NATIVE | yes | Video header with H1, chips, call ticket, pause toggle | Row Video BG (one MP4 + WebM + Video Preview Image, Background Video Loading 'Lazy Load'), Parallax Subtle, Slight Zoom Out Reveal, Color Overlay | 0 | 'Disable Video Backgrounds On Mobile Devices' is a theme-wide option, not per row; HD/SD switching by viewport is not native (ship one 720p file). Pause button → global row. |
| #marsrutai routes + hotspot schematic | NATIVE+CSS | partly | H2 + text + 2 route rows + clickable numbered schematic with tooltips (Ireland leg dashed) | Image With Hotspots: image = exported schematic, Hotspot Icon 'Numerical', Tooltip Functionality 'Show On Hover' (one mode for all devices), Enable Animation ✓ (theme CSS has the 'pulsate' keyframes), Color = accent; HLI ×2 with Full Item Link URL | 20 | The demo builds the hotspots itself (≈110 CSS + tarptautiniai.js 28 lines) on top of a Raw HTML SVG. 'hover desktop / click touch' is not selectable separately. |
| Both-routes SVG map (.sgp-map) | CUSTOM | no | Raw HTML SVG schematic behind the hotspots | Exported image inside Image With Hotspots (row above) | 0 | CSS counted in the home map row. |
| Overlapping route chapters (Airija, Ispanija) | NATIVE | yes | Two full-screen chapters sliding over each other | Type 'Sticky Scroll Pinned Sections', Effect 'Overlapping' (+ Overlap Amount per device), Subtract Navigation Height ✓, Effect Enabled tablet/phone 'Disabled' | 0 | Children may be full vc_row (as_parent includes vc_row), so each chapter keeps its own video/image background. |
| Chapter rows #airija / #ispanija (×2) | NATIVE+CSS | partly | Dark chapter: H2, route strip, timetable, facts, call button + phones \| 2 inset photos | Row BG video/image + Background Image tablet/phone (bg_image_tablet / bg_image_phone ✓) + overlay; phone list = Icon List or HLI (code \| number) | 30 | Mobile 'top band fading' needs ~30 CSS lines; route strip, timetable and insets are separate rows. |
| Route strip in chapters (.tp-strip) ×2 | CUSTOM | no | Mini route LT–PL–DE–IE with rings, drawn on enter; Ireland leg dashed | Text Block 'LT → PL → DE → IE' or Icon List (Direction Horizontal); drop the drawing | 120 |  |
| Chapter timetables ×2 | CUSTOM | no | Date rows per direction, each row a tel: link | Horizontal List Item ×2 (Columns 3: direction \| dates \| phone icon, Full Item Link URL tel:) typed manually, or the shared GS | 55 | sgp-tt ≈55 CSS lines + shortcode. |
| Chapter inset photos ×2 (mask reveal) | WRONG-MAPPING | yes | Two overlapping photos revealed from the bottom with 120 ms stagger, front image parallax | Column Animation has no 'Mask Reveal' → Column Background Image + Background Layer Animation 'Mask Reveal' (Bottom), or Image Animation 'Reveal Rotate From Bottom' + Delay 0/120; Cascading Images is the closest single element | 20 |  |
| #pakeliui countries on a lane | CUSTOM | partly | 4 countries on a horizontal lane that draws on enter (vertical below 1000 px) | Icon List (List Icon Type 'Number', Direction Horizontal, Columns 4) or 4 × HLI without the lane | 160 | Draw-on-enter needs a JS trigger class — not something HLI does. tp-stops + tp-stop ≈166 CSS lines. |
| #kodel-mes trust list | NATIVE+CSS | partly | Sticky H2 left; 9 numbered reasons (mono 01–09, first clause bold) | HLI ×9 (Columns 2 '20% \| 80%', Style 'Bottom Border, No Hover Effect', Border Animation ✓) | 20 |  |
| #ko-negalima-siusti banned items | NATIVE+CSS | partly | Dark texture: H2 + intro; ✕ list 7/12; sticky 'Svarbu' callout + fine + outline button 5/12 | Fancy Unordered List (Font Icon ✕, Enable Animation); callout = column with left border; Button 'See Through' ✓ | 25 |  |
| #ka-dar-zinoti info cards | NATIVE+CSS | yes | 4 cards (2×2) with a thin top rule + mono index; rule turns red on hover | Column Border Type 'Advanced' (top 1px) ✓ + Column Animation 'Fade In From Bottom' + Delay; hover colour = 5 CSS lines | 8 |  |
| #paslaugos service list | NATIVE | yes | H2 + text + GS-ServiceList + link | Animated Text + Text Block + Global Section element + Button 'Underline' | 0 |  |

### paslauga (šablonas ×11)

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| T1 hero (route header, 4-level breadcrumb) | NATIVE+CSS | partly | Photo header: breadcrumb, '01 / 11' index, H1, text, chips, call ticket | Verified row options; breadcrumbs per global row; chips → Badge | 20 |  |
| T1b sticky submenu | NATIVE+CSS | yes | Sticky mono submenu under the header; active item underlined in red | Page Submenu: Sticky ✓, Link Alignment Left, Menu BG Color, Link Color; items = 'Menu Link' elements; active state from Salient's built-in scrollspy + ~12 CSS lines | 15 | init.js ships a scrollspy for the page submenu (calcPageSubemnu) — sgp.js §13 not needed. |
| T2 Faktai | NATIVE+CSS | partly | Facts table 7/12 + outlined link chips 5/12 (→ ?domina=…#uzklausa) | HLI key/value rows + Button 'See Through' (Preset sm); form pre-select via Fluent Forms default value {get.domina} | 10 |  |
| T3 Apie paslaugą | NATIVE | yes | Sticky H2 4/12 + long text 8/12 | Column Sticky Content ✓ + Text Block (max width via column) | 0 |  |
| 'Kaip tai vyksta' 3 steps | NATIVE+CSS | partly | 3 stations on a red animated lane with round photos | Divider (2px, Animate Line) + 3 Columns + Image Mask 'Circle' — all verified; station rings = CSS (or drop) | 40 |  |
| T4 Privalumai (sticky media) | NATIVE | yes | Dark: sticky photo 45 % on the left changes as text blocks scroll | Type 'Sticky Media, Scrolling Content', Media Width 45%, Media Height 80%, Content Position Right, Mobile Media Aspect Ratio 4:5 | 0 | Transition is Salient's own; 'crossfade + scale 1.06 → 1' is not an option. Demo emulation (≈161 CSS + paslauga.js media swap) disappears. |
| T6 Kliento atsakomybės accordion | NATIVE+CSS | partly | Sticky H2 + lead left; numbered accordion right with deep links | Toggle Panels 'Minimal Shadow', Accordion ✓; deep link = ?toggle=N (init.js), not #id | 30 | Custom .sgp-acc look vs native Minimal Shadow — see home rules row. |
| T7 Draudžiami daiktai | NATIVE+CSS | partly | Dark texture: H2 + text + red-outlined '1200 EUR' fine teaser + button; ✕ list | Fancy Unordered List (Font Icon) ✓; fine teaser = column with border (Advanced) or ~15 CSS lines | 20 |  |
| T9 Uždarymas statement | NATIVE+CSS | partly | Statement with 2 underlined phrases + call ticket + links | Highlighted Text 'Regular Underline' 3px ✓ + Buttons | 10 |  |
| Related service cards ×3 | NATIVE+CSS | partly | 3 cards: image 16:11, index, H3, summary, arrow; hover video | Fancy Box 'Image Above Text' ×3 (or Column Link + Image 'Zoom In Crop'); drop hover video | 20 |  |
| T10 'Kita stotelė' next-service link | NATIVE+CSS | partly | Dark full-width link to the next service; photo fades in on hover, lane draws on hover | Column Link ✓ + Background Color / Background Color Hover + Hover Opacity; the photo fade-in and the lane need ~30 CSS lines (or drop) | 30 | Column hover options change the colour layer, not the image opacity. |

### paslauga: specialūs blokai

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| kroviniu: packing rules stations | NATIVE+CSS | partly | 4 numbered packing rules with icons on a red lane | Divider (Animate Line) + 4 Columns with Icon + Text Block; or Icon List (Number) in 4 columns | 40 |  |
| automobiliu + motociklu: cinematic video band (×2) | NATIVE | yes | Full-width (b/w) looping video band with overlay text | Self Hosted Video Player: Autoplay ✓ + 'Start Playing When Scrolled Into View', Loop ✓, Hide Controls ✓, 'Replace With Image on Mobile' ✓, Advanced gradient overlay ✓. The player has no parallax — use a Row Video BG + Parallax Subtle if parallax matters | 0 | Grade (b/w) the video file itself. |
| daiktu: large tag buttons | NATIVE | yes | Big outlined tags (Langai, Žoliapjovės …) | Button 'See Through' (Preset lg) or Badge | 0 |  |
| daliniu: bays diagram (SVG) | CUSTOM | no | Inline SVG of shared van bays, drawn on enter | Static image (Image, 'Fade In From Bottom') + caption | 65 |  |
| gyvunu: 'Prieš kelionę' checklist | CUSTOM | partly | Multi-open accordion with tick boxes remembered per visitor | Toggle Panels Style 'Animated Circle', Accordion Toggles unchecked (multi-open) ✓; drop the tick boxes | 40 | sv-chk ≈130 CSS + paslauga.js checklist. |
| gyvunu: 'Kaina' factors | WRONG-MAPPING | partly | Dark row: text + 3 factor boxes (icon, index, label) + link | Fancy Box has no 'minimal' style (Bottom Color Bar Hover Effect / Color Box Hover Effect / Color Box Basic / Parallax Hover Effect / Description on Hover / Image Above Text) → Text With Icon ×3, or Icon + Text Block in bordered columns | 20 |  |
| gyvunu: statement + call button | NATIVE | yes | Statement + button that opens the phone list | Text Block + Button (menu mega/GS phones instead of the popover) | 0 |  |
| keleiviu: 'Principai' pinned cards | WRONG-MAPPING | partly | 5 principle cards pinned and stacking | Effect 'Overlapping' (or 'Scale') + 'Stacked Appearance' ✓ | 40 | Same wrong effect name as /apie-imone/. |
| keleiviu: 'Patogumai' hotspots | NATIVE+CSS | yes | Van interior photo with 4 red numbered hotspots + legend list | Image With Hotspots (Numerical, Color accent, Tooltip hover) + Icon List; 28 px markers and a 2-cycle pulse = ~10 CSS lines (native pulse loops) | 10 | Demo emulation (≈188 CSS + paslauga.js 48 lines) disappears. |
| keleiviu: 'Kokie dar privalumai?' facts | NATIVE+CSS | partly | Sticky H2 + key/value list | Column Sticky Content + HLI key/value rows | 0 | CSS in the global .sgp-kv row. |
| negabaritiniu: definition + video | NATIVE+CSS | partly | Dark definition callout 5/12 + looping video 7/12 with pause | Column BG colour callout + Self Hosted Video Player (Autoplay scroll-based, Loop, Hide Controls, Replace With Image on Mobile) | 15 | Pause button → global row. |
| perkraustymo: red-outline callout | NATIVE+CSS | yes | Callout with a red outline | Column Border (Simple, 1px accent) or 8 CSS lines | 8 |  |
| siuntu-pervezimas: packing guide (SVG) | CUSTOM | no | Inline SVG box cross-section with a red 5 cm dimension line | Static image + caption | 43 |  |
| single-responsibility callout (4 services) | NATIVE+CSS | yes | One responsibility shown as a callout instead of an accordion | Callout per the global row | 0 |  |

### /pervezimu-grafikas/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Compact header (44svh) | NATIVE | partly | Short dark texture header: H1, 'ATNAUJINTA …' stamp, call ticket | Row Height/Min Height 44svh (height group) ✓ + BG image + Color Overlay (texture strength) + Parallax + Slight Zoom Out Reveal | 0 |  |
| 'Atnaujinta' stamp | CUSTOM | no | '● ATNAUJINTA RUGSĖJO 23 D.' set automatically | Type the date in the Text Block (or inside the schedule GS) | 5 |  |
| #lenta board with tabs | CUSTOM | partly | Dark board: tabs Visi / Airija / Ispanija; rows route (flap code) · dates · status · phone; every row is a tel: link | Tabs Style 'Minimal', Tab Change Animation 'Fade' ✓ (deep link ?tab=airija); each tab = Horizontal List Items (Columns 4, layout '35% \| 35% \| 15% \| 15%', Full Item Link URL tel:) typed manually | 100 | Tabs are native; the table is the shortcode (sgp-sched ≈103 CSS lines). |
| Board footer button | WRONG-MAPPING | partly | Stamp + outlined 'Skambinti' button | The Button element has no 'Regular' or 'Line' type in 18.2.1 (Basic, See Through, Arrow Animation, Arrow Circle Animation, Curved Arrow Animation, Underline, Text Reveal Wave, Text Reveal, Material, Next Section; 'Regular' exists only in Legacy Button) → Button 'See Through' + phone icon | 0 |  |
| #laiko-juosta lane chart | CUSTOM | no | Timeline: one lane per route over a day scale; rings = departures, soonest filled red | Disable the row — the tabs table shows the same data | 240 | gr-lane ≈239 CSS lines + grafikas.js label placement. |
| #ka-verta-zinoti facts + map | CUSTOM | partly | Sticky H2 + facts + 2 links left; SVG route map right | Column Sticky Content + HLI facts + Button 'Underline'; map = exported Image | 0 | Map CSS counted in the home map row. |

### /siuntos-sekimas/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Compact header (44svh) | NATIVE | partly | Short photo header with H1 + call ticket | Verified row options (Min Height 44svh) | 0 |  |
| #paieska tracking search | CUSTOM | partly | Large code field + red 'Siuntos lokacija' button; empty → 'Neįvestas siuntos kodas!' | Fluent Forms (1 required field, error text verbatim) → Confirmation 'Redirect to URL' ?kodas={inputs.kodas}; or redirect straight to the external tool URL | 30 |  |
| #rezultatas iframe frame | CUSTOM | partly | Result area on a 'map paper' frame with crop marks (demo shows route progress + log) | Raw HTML iframe is unavoidable for the external tool (+ ~15 CSS lines); drop the crop-mark frame | 20 | The sk-* demo states (≈600 CSS lines) are demo-only and never built. |
| #pagalba help + link cards | NATIVE+CSS | partly | 'Neradote siuntos kodo?' + call buttons + 3 link cards | Buttons + Fancy Box 'Image Above Text' ×3 | 10 |  |

### /taisykles/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Hero with PDF button + anchor chips | WRONG-MAPPING | partly | Route header + 'Atsisiųsti sutartį (PDF)' button + 3 anchor chips | No 'Line'/'Regular' Button types → Button 'See Through' + download icon; chips = Button 'Basic' (Preset sm) or Badge | 20 |  |
| #taisykliu-tekstas rules document | NATIVE+CSS | partly | Long document: sticky left index drawn as a lane with 6 stops that fill while reading; numbered clauses 2.1 … | Tabs Style 'Vertical Sticky Scrolling' ✓ (Navigation Width 25–30 %, Tab Link Animation 'Animated Underline' or 'Opacity Change', Navigation Item Mobile Display 'Visible Above Each Section'); clauses = Text Block + ~20 CSS lines for hanging numbers | 40 | Demo emulates it with scroll-spy + lane (taisykles.js 46 lines, tr-index ≈100 CSS). The native element fits; the ring-lane look does not. |
| 4.2 banned items inset | NATIVE+CSS | partly | Dark inset with 12 numbered ✕ items in 2 columns | Inner Row BG colour + Fancy Unordered List (✕) or Icon List (List Icon Type 'Number') — one or the other, not both | 30 |  |
| 4.5 fines (1200 EUR) | NATIVE | yes | Big '1200 EUR' (superscript), fines table, toggle with the full text | Milestone: Number 1200, Symbol 'EUR', Symbol Position 'After Number', Symbol Alignment 'Superscript', Effect 'Count To Value'; HLI table; Toggle Panels 'Minimal Shadow' | 0 | All verified in milestone.php / toggles.php. |
| 5. deadline lane (0 → 5 → 14 d.) | CUSTOM | no | Deadline lane with 3 stops drawing on enter | 3 Columns × Milestone (0 / 5 / 14, Symbol 'd.') + Divider with Animate Line, or HLI with 3 columns | 160 | tr-dead ≈159 CSS lines. |
| PDF end card | NATIVE+CSS | partly | Card with red download tile + link + 'Turinys ↑' | Button 'Underline' + download icon ✓; card = column border | 20 |  |

### /kontaktai/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Plain header + jump-link stop list | CUSTOM | partly | Dark header, H1, rail terminus ring; right: 4 jump links drawn as route stops | Row Min Height 40svh + Animated Text H1; right column = HLI ×4 (Full Item Link URL #anchors) or the native (horizontal) Page Submenu; drop the terminus | 60 | Page Submenu renders a horizontal bar — a vertical stop list is custom; kontaktai.js terminus 14 lines. |
| #skambinkite call tickets | CUSTOM | partly | 2 large call tickets (LT number 92 px, IE/UK/ES numbers, stub with next departure) + e-mail with copy button | 2 Columns with Background Color + Border (Advanced) + Button 'Basic' (phone icon, Preset lg) per number; e-mail = mailto link; drop stub + copy | 170 | kt-tk ≈167 CSS lines + copy JS. |
| #grafikas timetable | CUSTOM | partly | Sticky H2 + note + button; 4 route date rows (tel: links) | HLI ×4 typed manually (or the shared schedule GS); 'Button Line' → Button 'See Through' | 50 | Also uses the non-existent 'Line' button type. |
| #parasykite contact form | NATIVE+CSS | partly | Sticky quick-call list (matching direction lights up) + contact form with radio/checkbox chips | Fluent Forms + Theme Options 'Enable Fancy Checkbox Styling' ✓ / Overall Form Style; quick-call list = Icon List/HLI without the JS highlight | 60 | kt-quick highlight = custom JS (drop); chip radios (kt-opt) ≈55 CSS lines. |
| #kur-vaziuojame map | CUSTOM | partly | Dark: text + facts + link; SVG map on a paper card | Exported map Image (or Image With Hotspots) in a column with BG colour | 40 |  |

### /privatumo-politika/

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| Plain header | NATIVE | partly | Dark short header with H1 | Row Min Height 40svh + Animated Text | 0 |  |
| #dokumentas policy + mini-TOC | CUSTOM | partly | Sticky mini-TOC with a reading-progress lane + policy text + callouts | Column Sticky Content with plain anchor links (no progress lane), or Tabs 'Vertical Sticky Scrolling' with 2 tabs | 90 | pp-toc ≈90 CSS + privatumo-politika.js reading progress. |
| Cookie table | NATIVE+CSS | partly | Cookie list styled as timetable rows (mono keys), cards below 1000 px | Complianz [cmplz-cookies] / CookieYes cookie table shortcode in a Text Block + ~30 CSS lines | 30 |  |

### 404

| Blokas | Verdiktas | Atrodo kaip Salient? | Dabar | Natyvus pakaitalas | CSS ≈ | Pastabos |
|---|---|---|---|---|---:|---|
| 404 hero row | NATIVE | yes | Full-height graded photo, H1 'Maršrutas nerastas', buttons | Build as a Global Section at location '404 Content' (nectar_hook_404_content ✓) with these row options | 0 |  |
| '4 0 4' board tiles + broken rail | CUSTOM | no | Split-flap '4 0 4' tiles; the rail comes down, breaks into a dashed segment, ends in a grey ring | Animated Text '404' (Single Letter 'Reveal') or Milestone; drop the rail | 110 | e4-route + e4-lane ≈100 CSS lines + 404.js. |
| 404 buttons | WRONG-MAPPING | yes | Red arrow button + outline button | 'Line' → Button 'See Through' | 0 |  |
| GS-ServiceList (2 columns) | NATIVE | yes | 11 services as a 2-column line list | Global Section element with HLI ×11 | 0 |  |

Pilni `data-salient` teiginiai kiekvienam blokui — `docs/salient-auditas.json` (laukas `claimed`).
