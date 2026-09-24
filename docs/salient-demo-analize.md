# Salient demo analizė: bazinis demo SGP pervežimams

**Data:** 2026-09-24 · **Temos versija:** Salient 18.2.1 (jūsų licencija), Salient Core ir Salient WPBakery iš to paties paketo.
**Tikslas:** išsirinkti Salient demo, kurio išvaizdą perimsime SGP v2 demo, kad visas dizainas būtų surenkamas **vien Salient elementais ir Theme Options**, o ne atrodytų kaip atskirai programuota svetainė.

---

## Santrauka

**Pagrindinis demo: Harbor.** Tai naujausias Salient demo (Salient Studio šablonų data – 2025-10). Jį galima importuoti per 18.2.1 Demo Importer. Reikalingi įskiepiai: Salient WPBakery, Salient Core ir Fluent Forms.
Harbor atitinka SGP, nes:
- spalvų pora beveik ta pati: Accent `#000000`, Extra Color 1 `#ff4a4b`, o SGP turi `#1c1d1d` ir `#ef4539`;
- jame daugiausia natyvaus judesio: parallax hero su išblukimu, horizontaliai slenkančios spalvotos kortelės, sluoksniuotos atsiliepimų kortelės, parallax statistikos juosta, raidžių atsiradimo antraštės, animuoto gradiento footeris;
- viršuje yra slenkanti raudona juosta, į kurią tiesiogiai tinka „Artimiausi išvykimai“;
- jo sekcijos yra ir kaip atskiri **Salient Studio** šablonai (Harbor Hero, Intro, Difference, Testimonials, Pricing, CTA, Footer), todėl jas galima įterpti į bet kurį puslapį.

**Antrinis demo vidiniams puslapiams: Architect.** Iš jo imami:
- antraštės telefono mygtukas, kuris telefone lieka matomas;
- vidinių puslapių išdėstymas: About, Projects, projekto puslapis;
- numeruotos eilutės 01/02/03, Fancy Box kortelės karuselėje, post grid su animuotu pabraukimu.

Iš Architect **Theme Options neimportuojami.** Imami tik išdėstymo šablonai.

**Atmesta kaip pagrindas: Signal.** Jį jau naudojo v1 (commit `988c4f3`). Jo agentūrinis „hype“ tonas ir didžiosios raidės H1 netinka šeimoms ir užsienyje gyvenantiems lietuviams.

---

## 0. Šaltiniai ir metodas

| Šaltinis | Kas iš jo paimta |
|---|---|
| `salient-demo-importer/.../demo-data/*/theme-options.txt` (41 demo, 18.2.1) | Tikslios Theme Options reikšmės: šriftai, dydžiai, spalvos, antraštė, off-canvas, konteineris, animacijos |
| `.../demo-data/*/content.xml` | WPBakery shortcode'ai su tiksliais parametrais (`split_line_heading`, `nectar_sticky_media_sections`, `nectar_cta`…), Global Section vietos, meniu punktų nustatymai |
| `field_wbc_importer.js` (`nectar_demo_depends`) | Kokių įskiepių reikia kiekvienam demo importuoti |
| `salient-core/includes/nectar_maps/*.php`, `nectar-addons.php`, `menu/class-nectar-wp-menu-settings.php` | Patikrinta, kad visos naudojamos parinktys yra 18.2.1 versijoje |
| `salient-core/includes/salient-studio-templates.php` | 470 Salient Studio šablonų, iš jų Harbor ×7, Signal ×3, Tether ×3, Architect ×1 |
| Gyvi demo themenectar.com (dabar veikia 18.3.0) | Playwright ekrano nuotraukos 1440×900 ir 390×844, `#header-outer` `data-*` atributai, apskaičiuoti šriftai, elementų klasių skaičius |
| `augejas/salient-gidas.html`, `elile/salient-gidas.html`, `atpsprendimai/_build/salient-robust-notes.md` | Jūsų ankstesnė praktika: pagrindu imamas vienas demo, jo nustatymai perkeliami, o skirtumai aprašomi lentelėje „Kas pakeista lyginant su …“ |

Pastaba apie versijas: gyvi demo sukasi ant 18.3.0 (`style.css?ver=18.3.0`). Visi čia nurodyti elementai ir parinktys patikrinti **18.2.1 kode**. Ten yra `js/build/elements/nectar-sticky-media-sections.js`, `nectar-fit-text.js`, `nectar-content-trail.js`, `nectar-animated-gradient.js`, parinktys `header-hide-until-needed`, `page-transition-type: view-transitions`, `device_visibility_*` ir meniu parinktis `menu_item_persist_mobile_header`. Neatitikimų, dėl kurių reikėtų 18.3, neradau.

---

## 1. Demo atranka

18.2.1 Demo Importer turi 41 demo. Visi gyvame sąraše esantys demo turi atitikmenį importeryje; naujesnių demo, kurių 18.2.1 neturėtų, nėra.

Iš karto atmesti:
- eCommerce ×4 ir Old-School-Ecommerce, nes reikia WooCommerce;
- blog'ai ×5 ir Mag;
- portfolio ir fotografų demo ×6: Freelance, Minimal, Layered, Quantum, Fullscreen Slider, Photography;
- Band, Restaurant, Wellness, Nonprofit, App, Landing Product, One-Page, Old-School-All-Purpose, Ascend, Frostwave. Tai kitos tematikos arba 2013–2016 m. išvaizdos demo.

Liko 10 verslo krypties demo: Harbor, Architect, Signal, Tether, Business 3, Corporate 3, SaaS, Resort, Business 2 ir Corporate Creative.

### 1.1 Trumpasis sąrašas

Vertinimo kriterijai, kiekvienas iki 10 balų:
- **M** – modernumas;
- **J** – natyvus judesys, t. y. parallax ir hover efektai, kurių prašė klientas;
- **S** – ar tinka raudona ir beveik juoda;
- **T** – ar tinka auditorijai, kuri naršo telefonu ir nori skambinti;
- **V** – ar demo turi vidinių puslapių pavyzdžių;
- **P** – ar tinka solidžiam transporto prekės ženklui.

Bendras įvertinimas yra svertinis, M ir J turi didžiausią svorį.

| Demo | URL | M | J | S | T | V | P | **Įvertinimas** | Kodėl | Įskiepiai importui |
|---|---|---|---|---|---|---|---|---|---|---|
| **Harbor** | https://themenectar.com/salient/harbor/ | 10 | 10 | 10 | 7 | 4 | 8 | **9,0** | Naujausias demo. Juoda ir `#ff4a4b` beveik sutampa su SGP spalvomis. Turi slenkančią viršutinę juostą, milžinišką hero antraštę per visą plotį, horizontaliai slenkančias paslaugų korteles, parallax statistikos juostą, sluoksniuotus atsiliepimus ir gradientinį footerį. Yra 7 Salient Studio šablonai | Salient WPBakery, Salient Core, **Fluent Forms** |
| **Architect** | https://themenectar.com/salient/architect/ | 7 | 8 | 9 | **10** | **9** | 9 | **8,3** | Accent `#ff5149` raudonas. Antraštėje telefono „pill“ mygtukas, kuris telefone lieka šalia meniu. Turi About, Projects ir projekto puslapį. Parallax nuotraukų stulpeliai, Fancy Box karuselė, „Next project“ juosta | Salient WPBakery, Salient Social, Salient Portfolio, Salient Core |
| **Signal** | https://themenectar.com/salient/signal/ | 9 | 8 | 6 | 7 | 5 | 5 | **7,0** | Stiprus ir šiuolaikiškas, bet agentūrinis: oranžinis, didžiosiomis raidėmis rašomas H1, spalvos keitimas slenkant, nuotraukos tekste. v1 jau buvo „Signal kryptis“, o v2 šių judesių sąmoningai atsisakė | Salient WPBakery, Salient Core, Fluent Forms |
| **Tether** | https://themenectar.com/salient/tether/ | 9 | 7 | 4 | 6 | 3 | 5 | **6,0** | SaaS programėlės demo. Serif H1 (Instrument Serif), geltona `#ffff00`, bento tinklelis, DUK toggles. Gražus, bet „app“ tonas ir tik vienas puslapis | Salient WPBakery, Salient Core |
| **Business 3** | https://themenectar.com/salient/business-3/ | 5 | 6 | 5 | 6 | 3 | 6 | **5,4** | 2019 m. išvaizda: koralo ir mėlynas gradientas, Alegreya Sans. Jau panaudotas Augėjui, todėl pakartojimas nepageidautinas | Salient WPBakery, Salient Core, Salient Social, Salient Widgets |
| **Corporate 3** | https://themenectar.com/salient/corporate-3/ | 5 | 5 | 6 | 6 | 5 | 6 | **5,3** | 2019 m. korporatyvinis demo: Cabin 700, oranžinė, daug komandos narių. Solidus, bet senstelėjęs | Salient WPBakery, Salient Core, Salient Social, Salient Widgets |

Taip pat peržiūrėti, bet į sąrašą nepateko:
- **Resort** (4,8): kelionių tema ir telefonas su „Book now“ antraštėje, bet prabangus serif stilius su smėlio spalvomis;
- **SaaS** (4,5): žaismingas startuolis su gradientinėmis dėmėmis;
- **Business 2** ir **Corporate Creative** (4): 2017–2018 m. išvaizda, Nunito ir Muli šriftai.

Ekrano nuotraukose peržiūrėti 1440 px pločio vaizdai: Harbor, Architect, Business 3, Signal, Corporate 3, SaaS, Tether, Nonprofit, Resort. Telefono vaizdai 390 px: Harbor, Architect, Signal. Papildomai peržiūrėti Architect About ir projekto puslapiai bei Harbor Contact.

---

## 2. Harbor: išsami analizė (pagrindinis demo)

**Pobūdis:** vieno puslapio finansų konsultantų svetainė su Contact puslapiu. **Turinys:** 1 landing puslapis, 1 kontaktų puslapis ir 2 Global Sections („Harbor Secondary Nav“, „Harbor Footer“).
**Klasių skaičius gyvame puslapyje:** `.nectar-split-heading` 9, `.nectar-responsive-text` 55, `.nectar-sticky-media-sections` 2, `.nectar-cta` 8, `.nectar-badge` 4, `.parallax_section` 2, `.nectar-content-trail` 1, `.nectar-animated-gradient` 1, `.nectar-global-section` 2. Fancy Box, Milestone ir Nectar Button nenaudojami: dizainas remiasi tipografija, spalvų plokštumomis ir judesiu.

### 2.1 Antraštė ir viršutinė juosta
- **Header Format:** `default` (logotipas kairėje, meniu dešinėje), `header-fullwidth` 1, šoninis tarpas 40 px (telefone 25 px), `header-padding` 22, logotipo aukštis 24 px.
- **Transparent header:** `transparent-header` 1, `header-permanent-transparent` 1, `header-starting-color` `#ffffff`. Fonas `#ffffff`, šešėlio nėra, apatinė linija išjungta.
- **Hover:** `header-hover-effect: text_reveal`, t. y. meniu žodis „išsivynioja“ į viršų. **Header Hide Until Needed: ON**: slenkant žemyn antraštė pasislepia, slenkant aukštyn grįžta. Resize ir condense išjungti.
- **Off-canvas:** kompiuteryje hamburgerio nėra (`header-slide-out-widget-area` 0). Telefone (riba 1000 px) veikia `slide-out-from-right`: juodas apvalus mygtukas (`menu-btn-bg #000`, `icon-style circular`), juodas fonas, `overlay-opacity: solid`, šrifto dydis 24/26 px.
- **Viršutinė juosta** yra Global Section, rodoma vietoje `nectar_hook_before_secondary_header_before_scrolling`, visur išskyrus kontaktų puslapį.
  - Stulpelio fonas `#FF4A4B`, tekstas tamsus, visas stulpelis veda į Contact puslapį.
  - Elementas **Scrolling Text** (`nectar_scrolling_text`): `scroll_direction="ltr"`, `scroll_speed="slow"`, `text_repeat_number="8"`, skirtukas `✦`, `custom_font_size="0.9rem"` (telefone 15 px), `mask_edges="yes"`.
  - Juosta rodoma ir telefone.

### 2.2 Hero
- **vc_section:** `type="full_width_background"`, `min_height_desktop="100svh"`, `content_layout="flexbox"`, turinys prispaustas prie apačios (`flex_justify_content_desktop="flex-end"`).
- **Fonas:** nuotrauka su atskira versija telefonui (`background_image_phone`). `parallax_bg="true"`, **`parallax_bg_scroll_effect="parallax_fade"`**, `parallax_bg_speed="medium"`: fonas slenka lėčiau už turinį ir tamsėja.
- **Antraštė:** **Split Line Heading** su `fit_text_to_container="true"`, todėl tekstas ištempiamas per visą konteinerio plotį (apie 213 px, esant 1440 px ekranui). Kiti parametrai: `font_style="h2"`, `line_reveal_by_space_text_effect="letter-reveal-blur-top"`, `stagger_animation`, `mobile_disable_animation`. Po antrašte eina 1 px balta linija, `#FFFFFF36`.
- **Apatinė eilutė, kairė pusė:** „stiklinė“ kortelė, t. y. `vc_row_inner` su `backdrop_filter="blur"` 16, fonu `#0000006E` ir 15 px kampais.
  - Joje kvadratinė 1/3 nuotrauka (kampai 15 px), H5 tekstas ir mygtukas **nectar_cta `btn_style="arrow-circle-animation"`**.
  - Mygtukas baltas „pill“ su juodu tekstu: `border_radius="100"`, `backdrop_filter blur 13`, paddingai 4/4/4/20 px, šalia apskritime rodyklė ↗.
- **Apatinė eilutė, dešinė pusė:** matoma tik kompiuteryje (`vc_hidden-sm vc_hidden-xs`). Joje H5 tekstas ir **nectar_cta `btn_style="next-section"`** `minimal-arrow-alt`: rodyklė ↓, animuojama tik užvedus pelę. Kairėje 1 px balta linija.

### 2.3 Tipografija
Visur naudojamas **Inter Tight**. Google Fonts jam turi `latin-ext`, todėl lietuviškos raidės ąčęėįšųūž veikia.

| Vieta | Nustatymas |
|---|---|
| H1 | 400, **4rem**, line-height 1,3 |
| H2 | 400, 2,7rem / 1,3 |
| H3 | 400, 2rem / 1,3 |
| H4 | 400, 1,4rem / 1,3 |
| H5 | 1,1rem / 1,4 |
| H6 | 500, 1rem / 1,4 |
| Body | 400, 1rem / 1,6 |
| Navigacija | 500, 0,9rem |
| Label | 500, 0,9rem |
| Fluid šaknis | `calc(1vw + 0.1rem)`; kompiuteryje min 0,8rem, telefone 1–1,5rem |
| Responsive heading % | H1 75/70/65 (mažas kompiuteris / planšetė / telefonas), H2 –/80/60, body telefone 90 |

- **Rašyba:** sakinio rašyba, jokių didžiųjų raidžių ir jokio monospace šrifto.
- **Sekcijų „eyebrow“ užrašai** rašomi skliaustuose paprastu body šriftu: „(About Us)“, „(Pricing)“, „(NYC Experts)“.
- **Įžangos** yra ilgi H5 dydžio sakiniai **Responsive Text** elemente.
- **Skaičiai** rašomi `font_size_desktop="3vw"`, `font_size_min="40px"`.
- **Svoris 400 visur,** todėl vaizdas lengvas ir „konsultantiškas“. SGP reikės 500 (žr. 5.3).

### 2.4 Spalvos
- **Accent:** `#000000`. **Extra 1:** `#ff4a4b` (raudona). **Extra 2:** `#ffb500` (gintarinė). **Extra 3:** `#8ccbff` (dangaus mėlyna).
- **Fonas:** `#ffffff`. **Tekstas:** `#1e1e1e`. **Off-canvas:** `#000000`.
- **Spalva naudojama tik didelėmis plokštumomis:** viršutinė juosta, paslaugų kortelės (raudona, gintarinė, mėlyna), atsiliepimų kortelės, ženkliukas „Reccomended“, content trail žymos ir footerio gradientas.
- **Smulkiose detalėse spalvos nėra:** linijos, ikonos ir nuorodos yra juodos arba baltos.
- **Kontaktų stulpelis:** labai šviesus šiltas fonas `#ECEAE612`.

### 2.5 Tarpai ir konteineris
- **Konteineris:** `max_container_width` 1600. `ext_responsive_padding` 40 px, telefone `percent` 6 %. Stulpelių tarpas `default`.
- **Eilučių tarpai:** dažniausiai 10 % viršuje ir 5 % apačioje; statistikos eilutėse 40 px.
- **Kitas ritmas:** stulpelių paddingai 40 px (planšetėje 20 px); horizontalių kortelių tarpas 5 px.
- **Apvalinimai:** 10 px nuotraukoms, 15 px kortelėms ir stiklui, 20 px atsiliepimams ir ženkliukams, 100 px „pill“ mygtukams.
- **Mygtukų stilius:** `button-styling: slightly_rounded_shadow`, roundness 8.

### 2.6 Mygtukai ir hover
- **Pagrindinis CTA** yra `nectar_cta` **Arrow Circle Animation** („pill“ ir rodyklė apskritime, kuri užvedus pelę pasislenka ir pasikeičia).
  - Ant nuotraukos: baltas, `backdrop blur`.
  - Kainų kortelėse: juodas su balta rodykle.
- **Nuorodos:** `general-link-style: basic-underline`, `animated-underline-type: ltr-fancy`, linija 1 px. Kitos nuorodos (View Services, Get in touch) yra paprastas `nectar_cta` su pabraukimu.
- **Nuotraukos** neturi hover efekto (`hover_animation="none"`). Stiprus hover efektas yra tik **Content Trail** paskutiniame CTA: pelę sekančios tekstinės žymos „Say hello“ ir kt. atsiranda su `scale`, su atsitiktiniu pasukimu, spalvomis iš paletės, `frequency` 85, trukme 1,2 s.
- **Ženkliukai (`nectar_badge`):** „stikliniai“, fonas `#FFFFFF1F`, `backdrop blur 12`, 20 px kampai.

### 2.7 Judesys slenkant
- **Globaliai:**
  - `smooth-scroll` 1 (Lenis), stiprumas 85;
  - `column_animation_easing: easeOutCubic`, `column_animation_timing: 1300`;
  - `page-transition-type: view-transitions`, `ajax-page-loading` 1, telefone išjungta.
- **Split Line Heading efektai:** `letter-reveal-blur-top` (hero), `blur-bottom` (CTA), `fade-bottom` („(Pricing)“), **`scroll-opacity-reveal`** (statistikos juostos antraštė ryškėja slenkant).
- **Paslaugos:** **Sticky Media Sections, `type="horizontal-scrolling"`**, `horizontal_section_width="85"`, `section_height="100vh"`, tarpas 5 px, kampai 15 px.
  - Trys spalvinės sekcijos: `section_type="color"`, `section_color_palette` = extra-color-1/2/3.
  - Kiekvienoje kortelėje: didelis numeris „01“ (≈ 150 px), H3 pavadinimas, tekstas ir nuotrauka.
  - Telefone kortelės išsidėsto viena po kitos vertikaliai.
- **Statistika:** vc_section su dangaus nuotrauka, `parallax_bg_scroll_effect="parallax"`, `speed="fast"`, šešėlis `rgb(0,0,0)` 0,2. Joje H2 su scroll-opacity-reveal ir trys stulpeliai: stiklinis ženkliukas, skaičius 3vw ir trumpas tekstas.
- **Atsiliepimai:** **Sticky Media Sections, `type="layered-card-reveal"`**, `layered_card_reveal_effect="stack"`, proporcija 4:5, plotis 400 px (telefone 85vw), kampai 20 px. Kortelėse didelė pirmoji vardo raidė, portretas, citata ir vardas.
- **Footeris:** eilutė su `animated_gradient_bg="true"`, `color_1 #FF4A4B`, `speed 850`.

### 2.8 Sekcijų seka (landing)
1. Viršutinė juosta (GS, Scrolling Text).
2. Hero 100svh: parallax fade, per visą plotį ištempta antraštė, stiklinė kortelė su CTA.
3. „(About Us)“: didelis teiginys H2 per visą plotį, po juo tinklelis 1/3 + 1/6 + 1/3 + 1/6 su tekstu, CTA ir portretu.
4. „How we can help you“ ir horizontaliai slenkančios paslaugų kortelės (3 spalvos).
5. „Difference“: H2 teiginys, dvi nuotraukos 1/3 + 1/3 ir trys naudos 1/3.
6. Parallax statistikos juosta: dangus, scroll-opacity H2, 3 skaičiai su stikliniais ženkliukais.
7. Atsiliepimai: layered card reveal.
8. „(Pricing)“: H2, logotipų juosta (Gallery `flickity_static_height_style`) ir 3 kainų stulpeliai (atskirti linijomis, „Recommended“ ženkliukas, fancy-ul su taškais).
9. CTA: „Want to get started? Click here to book a meeting.“ – visas stulpelis yra nuoroda, fone Content Trail.
10. Footeris (GS).

### 2.9 Footeris
Global Section vietoje `nectar_hook_global_section_footer`, rodoma visur. Temos footer ir copyright sritys išjungtos (`enable-main-footer-area` 0, `disable-copyright-footer-area` 1).
- **1 eilutė** (40 px paddingai), 1/4 + 1/2 + 1/4:
  - kairėje socialinių tinklų ikonos Accent spalva ir „© ThemeNectar.“ + `nectar_current_year`;
  - viduryje `nectar_cta` nuorodos (About, Services, Pricing);
  - dešinėje „All Rights Reserved.“
- **2 eilutė:** Divider.
- **3 eilutė:** animuotas raudonas gradientas ir **Split Line Heading `font_style="h1"`, `fit_text_to_container`**, `font_line_height="1"`, „Harbor“ per visą plotį.

### 2.10 Vidinis puslapis (Contact)
- **Puslapio antraštės nėra:** `header-auto-title` 0, pirma eilutė prasideda po header.
- **Kairysis stulpelis (2/5):** šviesus fonas `#ECEAE612`, „How can we support you?“ (Responsive Text), Divider, Fluent Form su žymimaisiais laukeliais, vardu, el. paštu, telefonu ir žinute, juodas pilno pločio mygtukas, po juo „Perfer email? Get in touch“.
- **Dešinysis stulpelis (3/5):** nuotrauka su `mask_enable` `blur-gradient`, apačioje citata, vardas ir `nectar_star_rating`.
- **Formos:** `form-style default`, `form-fancy-checkbox` 1, laukų fonas permatomas.

### 2.11 Telefono vaizdas (390 px)
- Raudona juosta lieka viršuje (15 px tekstas). Po ja logotipas ir juodas apvalus meniu mygtukas.
- Hero antraštė vis dar per visą plotį. Stiklinė kortelė per visą plotį, mygtukas „Book a Call“ matomas pirmame ekrane.
- Horizontalios kortelės virsta vertikaliu sąrašu. Sluoksniuotos atsiliepimų kortelės išsidėsto vėduokle.
- Kainos išdėstomos vertikaliai. Footerio „Harbor“ antraštė išlieka per visą plotį.
- Horizontalaus perslinkimo nėra.

### 2.12 Harbor silpnybės SGP atveju
1. Yra tik 2 puslapiai, todėl 20 SGP puslapių išdėstymą reikia pasiskolinti iš Architect.
2. Antraštėje nėra telefono, o SGP tai būtina.
3. Svoris 400 atrodo per lengvai transporto įmonei. Sprendimas: 500.
4. Gintarinė ir mėlyna nėra SGP spalvos.
5. Kainų blokas SGP nereikalingas, nes kainų sąrašo nėra, bet jo forma puikiai tinka dviem maršrutų kortelėms.
6. Atsiliepimų SGP kol kas neturi.

---

## 3. Architect: išsami analizė (antrinis demo vidiniams puslapiams)

**Pobūdis:** architektūros biuras. **Puslapiai:** Landing, About, Projects, 5 Portfolio projektai ir GS „Architect Footer“ (vieta `global-section-above-footer`).
**Klasių skaičius:** `.nectar-fancy-box` 6, `.nectar-split-heading` 10, `.nectar-scrolling-text` 3, `.nectar-post-grid` 1, `[data-parallax-speed]` 5, `.nectar-text-inline-images` 1, `[class*=menu-item-btn-style]` 2.

### 3.1 Antraštė: telefono mygtukas
- **Formatas:** `default`, pilno pločio, `header-padding` 28, logotipas 28 px, permanent transparent, `header-hover-effect: animated_underline`, `condense-header-on-scroll` 1.
- **Hamburgeris matomas visada** (`header-slide-out-widget-area` 1, `slide-out-from-right`, apvalus juodas `#0a0a0a`). Pagrindinis meniu yra off-canvas, o šalia hamburgerio lieka tik telefono mygtukas.
- **Telefono mygtukas** yra meniu punktas „1-808-123-4567“ meniu „Salient Architect Top Menu“ (Salient Core → Menu Item Options). Parinktys:
  - `menu_item_icon = fa-phone`;
  - `menu_item_link_link_style = button-border-white-animated_extra-color-gradient` (baltas bordered pill);
  - **`menu_item_persist_mobile_header = on`**: telefone mygtukas lieka antraštėje šalia meniu mygtuko, o ne paslepiamas off-canvas meniu;
  - teksto spalvos: `#000000`, užvedus pelę `#ffffff`.
- **Kitos 18.2.1 stiliaus parinktys:** Button Accent Color, **Button Extra Color #1**, Bordered Accent/Extra #1, gradientiniai variantai.
- **`header-button-styling: shadow_hover_scale`:** užvedus pelę mygtukas padidėja ir atsiranda šešėlis.

### 3.2 Hero ir tipografija
- **Hero:** eilutė su fonu `#2b323a`, video arba nuotrauka su `overlay_strength 0.8`, `bg_image_animation="fade-in"`.
  - Antraštė: Split Line Heading H1 „Rethink architecture.“ su `letter-reveal-bottom`.
  - Apačioje `image_with_animation animation_type="looped"`: besisukantis apskritas užrašas „SCROLL DOWN“, nuoroda į `#intro`.
- **Šriftai:**
  - H1: **Urbanist** 600, 62/68 px, −0,03em;
  - H2: **Public Sans** 300;
  - body: Public Sans 17/26;
  - navigacija: Public Sans 500 15 px.
- **„Eyebrow“ užrašai** (RESIDENTIAL, COMMERCIAL, PORTFOLIO) rašomi didžiosiomis raidėmis mažu `vc_column_text` tekstu.

### 3.3 Spalvos, tarpai, mygtukai
- **Spalvos:** Accent `#ff5149`, Extra 1 `#3648d6`, fonas baltas, footeris `#111`.
- **Tarpai:** konteineris 2000, `ext_responsive_padding` 70, `column-spacing` 50px. Eilučių tarpai 6 %, 10 %, 12 %, dideli stulpelių paddingai (`padding-8-percent`).
- **Mygtukai:** `rounded_shadow`, roundness 4. `nectar_cta` **`arrow-animation`**: bordered pill (rėmelis `#cccccc`, užvedus pelę `#0a0a0a`), H6 tekstas, paddingai 15/40, kairėje linija-rodyklė, kuri užvedus pelę pailgėja.

### 3.4 Judesys
- **Parallax nuotraukų stulpeliai:** `parallax_bg="true"`, `parallax_bg_speed="very_subtle"` ir `animation_type="parallax"` sudaro dviejų nuotraukų sluoksnius, kurie slenka skirtingu greičiu. Tai Salient būdas gauti „cascading“ efektą be Cascading Images elemento.
- **Karuselė:** `carousel` (flickity) su 6 **Fancy Box `box_style="image_above_text_underline"`**, proporcija 4:5, `fade-in-from-right`.
  - Kompiuteryje 4 stulpeliai, `flickity_overflow="visible"`.
  - Valdymas `touch_total`: raudonas tempimo indikatorius `#ff5149`.
- **Scrolling Text `style="text_outline"`** „innovation“ (`slowest`).
- **Text With Inline Images** H1.
- **Parallax nuotrauka per visą plotį:** `medium_fast`.
- **Paskutinė eilutė:** `bg_image_animation="slight-zoom-out-reveal"`, dvi Scrolling Text juostos priešingomis kryptimis ant nuotraukos.
- **Portfolio sąrašas:** kairysis stulpelis „lipnus“, dešinėje **Post Grid** `content_under_image`, 1 stulpelis, 60vh.
  - `hover_effect="animated_underline_zoom"`;
  - pelę sekantis indikatorius „view“ `#ff5149` (`enable_indicator="yes"`).

### 3.5 Vidiniai puslapiai
- **About:**
  - pradžioje H1 „About Salient“ su letter-reveal (4/5 pločio), dešinėje 1/5 stulpelis su trimis `nectar_cta` nuorodomis į tos pačios puslapio dalis (Team, Values, Culture);
  - toliau parallax nuotrauka per visą plotį (`very_subtle`), didelis teiginys H1 per centrą, komanda (Team Member 2+3) su citata;
  - **„Culture“ sąrašas:** H1, po kiekvienu punktu Divider, eilutėje Highlighted Text `full_text` ir didelis numeris „01/02/03“ dešinėje.
- **Projects:** Post Grid, 3 stulpeliai, `content_under_image`, `animated_underline_zoom`, 10 px kampai, `fade-in-from-bottom`.
- **Projekto puslapis:**
  - hero per visą plotį su nuotrauka, H1 ir įžanga centre;
  - „The Outcome“: nuotrauka ir tekstas su citata;
  - 3 nuotraukų galerija;
  - **„Next Project“ juosta** (`portfolio_single_nav: after_project_next_only`).
- **Footeris:** plona eilutė su linija viršuje (`shape_type straight_section`): „Beautiful Architecture“, nuorodos su pabraukimu ir © metai.

### 3.6 Telefono vaizdas (390 px)
- Viršuje logotipas, baltas „pill“ su numeriu ir apvalus meniu mygtukas. **Iš visų peržiūrėtų demo tik čia paskambinti galima nuo pirmo ekrano.**
- Hero antraštė centre. Karuselė telefone rodo 1,3 kortelės ir leidžia tempti.

### 3.7 Kodėl ne pagrindinis
- 2022 m. demo: fiksuoti px šriftai, fluid tipografijos nėra, smooth scroll ir page transitions išjungti.
- Mažiau naujų v18 elementų: nėra horizontal-scrolling, layered cards, content trail, animated gradient.
- Urbanist su lietuviškomis raidėmis atrodo gerai, bet deriniu su Public Sans 300 H2 tekstas pasidaro per blankus.

---

## 4. Signal: išsami analizė (atmestas kaip pagrindas)

**Pobūdis:** marketingo agentūra. **Puslapiai:** Landing, Work, 5 projektai, GS „Signal Footer“ ir „Signal Related Projects“.
- **Antraštė:**
  - `default`, `header-padding` 30, permanent transparent;
  - **`header-hover-effect: button_bg`** (`grow-in`, `small`): užvedus pelę už meniu žodžio išauga pilkas „pill“ fonas;
  - `header-blur-bg` 1 (`gradient`, `active_not_at_top`);
  - condense ir hide-until-needed;
  - bordered „pill“ mygtukas „Get Started“;
  - `slide-out-from-right`, fonas `#121213`.
- **Hero:**
  - vientisa oranžinė eilutė `#FF5513` su **`color_change_section="true"`**: puslapio fonas slenkant keičia spalvą;
  - 2× Split Line Heading H1 **didžiosiomis raidėmis**: Zalando Sans 700, 4,5rem, line-height 1, −0,03em, `letter-reveal-bottom`;
  - **Content Trail `type="images"`**: pelę sekančios nuotraukos;
  - apačioje 3 maži užrašai.
- **Spalvos:** Accent `#121213`, Extra 1 `#ff6022`, fonas **šiltai pilkas `#f1efed`**, konteineris 1700, padding 60.
- **Sekcijos:**
  - paslaugų karuselė (flickity, `autorotate`): nuotraukos kortelės su baltu pavadinimu ir 5 „stikliniais“ ženkliukais;
  - Text With Inline Images („IN A 🖼 WORLD FULL OF NOISE…“), ryškėja slenkant;
  - Post Grid `vertical_list`: projektų pavadinimai su ↗ ir linijomis;
  - Testimonial Slider `minimal`;
  - Video su „Play Video“ CTA;
  - footeris: oranžinis GS su Fluent Form, el. paštu, socialiniais tinklais ir milžinišku „SIGNAL“.
- **Telefone:** oranžinis hero per visą ekraną, H1 tik 2 eilutės, karuselė tempiama, sąrašas su rodyklėmis patogus.
- **Kodėl ne:**
  - v1 jau buvo Signal kryptis, o v2 sąmoningai uždraudė Color Change Section, Text With Inline Images ir marquee kaip „v1 judesius“ (`dizaino-sistema.md` §0.2);
  - lietuviškos didžiosios raidės su diakritikais (Į, Š, Ž, Ė) sunkiai telpa į 1,0 line-height;
  - agentūrinis tonas netinka šeimos siuntiniams ir keleiviams.
- **Ką verta pasiskolinti:** `header-hover-effect: button_bg` kaip alternatyvą Harbor `text_reveal` ir šiltai pilką `#f1efed` kaip trečią SGP kortelių spalvą.

---

## 5. Rekomendacija

### 5.1 Sprendimas
| Vaidmuo | Demo | Kaip naudoti |
|---|---|---|
| **Pagrindas: visa išvaizda, Theme Options, pradžia, Global Sections** | **Harbor** | Testinėje aplinkoje importuoti viską: Demo Content, Theme Option Settings, Widgets. Prieš importą įdiegti ir aktyvuoti **Fluent Forms** (nemokamas, wordpress.org). Po importo Harbor sekcijas galima kelti ir per **Salient Studio → Harbor Hero / Intro / Difference / Testimonials / Pricing / CTA / Footer** |
| **Antrinis: tik vidinių puslapių išdėstymas ir telefono mygtukas** | **Architect** | Importuoti **atskiroje bandomojoje svetainėje**. Jei tai ta pati svetainė, Theme Option Settings išjungti, kad nepakeistų Harbor nustatymų. Pasiimti About, Projects ir projekto puslapio eilučių struktūrą (WPBakery → Save as template / kopijuoti shortcode) ir vėliau demo turinį ištrinti. Reikia Salient Social ir Salient Portfolio įskiepių. Jų nereikia, jei paslaugos lieka puslapiais |
| Trečio demo nereikia | – | Du demo išlaiko dizainą vientisą, o daugiau šaltinių jį suskaldytų. Signal naudojamas tik kaip vienos parinkties šaltinis (5.3, `button_bg`) |

### 5.2 Ką perimti iš Harbor (ir Architect)

| Sritis | Perimama | Salient nustatymas / elementas |
|---|---|---|
| **Struktūra** | Pradžios puslapis kaip Harbor seka: juosta → hero 100svh → teiginys ir „(Apie mus)“ → horizontalios paslaugų kortelės → „Difference“ tipo blokas → parallax statistika → (atsiliepimai) → dvi kortelės pagal Pricing formą → CTA su Content Trail → gradientinis footeris | vc_section / vc_row, Salient Studio „Harbor …“ šablonai |
| **Antraštė** | Harbor: default, full width, permanent transparent, balta ant hero, Text Reveal hover, Hide Until Needed, telefone apvalus juodas off-canvas mygtukas. **Iš Architect:** raudonas „Skambinti“ pill su telefono ikona, telefone likęs antraštėje | Theme Options → Header Navigation; Appearance → Menus → Salient Menu Item Options: *Menu Item Link Button Style* = **Button Extra Color #1**, *Icon* = `fa-phone`, **Persist In Mobile Navigation Header = On** |
| **Viršutinė juosta** | Raudona Scrolling Text juosta su artimiausiais išvykimais | Global Section, Location: **In Navigation Top Before Scrolling**; `nectar_scrolling_text` ltr / slow / `✦` / 0,9rem / mask edges; stulpelio nuoroda → /pervezimu-grafikas/ |
| **Tipografija** | Vienas šriftas Inter Tight, sakinio rašyba, fluid dydžiai rem vienetais, skliaustuose rašomi „eyebrow“ užrašai, H5 įžangos | Typography: Inter Tight, fluid root `calc(1vw + 0.1rem)`, H1 4rem / H2 2,7rem / H3 2rem / H4 1,4rem / body 1rem 1,6; Local Google Fonts ON |
| **Mygtukai** | „Pill“ su rodykle apskritime; ant nuotraukos baltas „stiklinis“ variantas, ant balto fono juodas; tekstinės nuorodos su 1 px animuotu pabraukimu | `nectar_cta btn_style="arrow-circle-animation"`, `border_radius="100"`; `general-link-style: basic-underline` + `ltr-fancy` |
| **Kortelės** | Horizontaliai slenkančios spalvinės sekcijos su dideliu numeriu; kitur Fancy Box „Image Above Text Underline“ 4:5 (Architect) | `nectar_sticky_media_sections type="horizontal-scrolling"` (85 %, 100vh, 5 px, 15 px); `fancy_box box_style="image_above_text_underline"` |
| **Stiklo detalės** | Hero kortelė ir statistikos ženkliukai su `backdrop blur` | `vc_row_inner backdrop_filter="blur"` 16; `nectar_badge` `#FFFFFF1F` blur 12 r20 |
| **Judesys** | Lenis smooth scroll, easeOutCubic 1300 ms, raidžių ir eilučių atsiradimas, parallax fade hero, parallax statistika, scroll-opacity-reveal, view-transitions, animuotas gradientas, Content Trail CTA eilutėje, Architect parallax nuotraukų stulpeliai | Theme Options → General → Smooth Scroll 85, Column Animation; Split Line Heading efektai; vc_section `parallax_bg_scroll_effect`; Page Transitions → View Transitions API |
| **Vidiniai puslapiai** | Architect About: H1 ir 1/5 stulpelis su nuorodomis į puslapio dalis; paslaugos puslapis kaip projekto puslapis (nuotrauka per visą plotį, H1 centre); numeruotos eilutės su Divider; „Kita paslauga“ juosta | Split Line Heading H1 `letter-reveal-bottom`; `nectar_cta` nuorodos; Divider; Highlighted Text |
| **Footeris** | Plona informacinė eilutė ir animuoto gradiento juosta su ištemptu „SGP pervežimai“ užrašu | GS Location **Footer**; `animated_gradient_bg`, Split Line Heading `fit_text_to_container` |
| **Tarpai** | Konteineris 1600, šoniniai tarpai 40 px (telefone 6 %), eilutės 10 % / 5 %, stulpeliai 40 px, apvalinimai 10 / 15 / 20 / 100 px | Theme Options → General → Layout (max container width, Ext. Responsive Padding) |

### 5.3 Ką pakeisti SGP (lentelė „Kas pakeista lyginant su Harbor“)

| Harbor | SGP | Kodėl |
|---|---|---|
| Accent `#000000` | **Accent `#1c1d1d`** (logotipo beveik juoda) | Prekės ženklas |
| Extra 1 `#ff4a4b` | **Extra 1 `#ef4539`** | Firminė raudona. Ant jos rašyti **juodą tekstą** (`#000` 5,58:1, kaip Harbor juostoje). Baltas tekstas ant `#ef4539` turi tik 3,76:1, todėl tinka tik ≥ 24 px antraštėms |
| Extra 2 `#ffb500` (gintarinė) | **Extra 2 `#c4301e`** („signal-ink“ iš v2) | Smulkus raudonas tekstas ant balto fono (5,54:1) ir baltas tekstas ant raudono mygtuko, jei reikia |
| Extra 3 `#8ccbff` (mėlyna) | **Extra 3 `#f1efed`** (šilta šviesiai pilka, iš Signal) | Trečia kortelių spalva, šviesūs skydeliai (formos, žemėlapio fonas). Kortelių ritmas: raudona / beveik juoda / pilka |
| Tekstas `#1e1e1e` | `#1c1d1d` | Vienas juodos tonas |
| Inter Tight **400** antraštėms | Inter Tight **500** H1–H4, letter-spacing −0,02em; body 400 17 px (1,0625rem), line-height 1,6 | 400 atrodo per lengvai krovinių ir keleivių vežėjui. 17 px body dėl vyresnių skaitytojų telefone |
| Barlow Condensed + IBM Plex Mono (v2) | **Atsisakoma**, lieka tik Inter Tight | Mono UPPERCASE užrašai ir siauras šriftas buvo pritaikyta v2 kalba, o Harbor pasiekia tą patį skliausteliais ir dydžių kontrastu |
| „(About Us)“ | „(Apie mus)“, „(Paslaugos)“, „(Maršrutai)“, „(Kelionėje)“, „(Taisyklės)“ | Harbor „eyebrow“ lietuviškai |
| Header be telefono | **„Skambinti“ pill**: Extra Color 1, `fa-phone`, Persist In Mobile Navigation Header. Kompiuteryje po juo 2 punktai (Airija / Ispanija su numeriais). Telefone mygtukas veda į `#skambinti` bloką su dviem numeriais. v2 `popover` gali likti kaip patobulinimas | Auditorija skambina telefonu. Du numeriai, pagal kryptį |
| Header Hide Until Needed ON | **OFF** | Skambinimo mygtukas turi būti vienu paspaudimu pasiekiamas ir slenkant žemyn. v2 mobili apatinė skambinimo juosta tampa nebereikalinga |
| Juosta „Book Your Startup Valuation Call ✦“ | „Lietuva → Airija: spalio 9 d. ✦ Airija → Lietuva: spalio 15 d. ✦ Lietuva → Ispanija: … ✦ Visas grafikas →“, turinys iš `[sgp_grafikas format="ticker"]` (Scrolling Text vidų apdoroja `do_shortcode()`) | Tikri duomenys, ne dekoracija. Vieta „Before Scrolling“, todėl juosta slenkant dingsta ir neužima vietos |
| Hero kalnų nuotrauka, antraštė „Vision in Focus“ per visą plotį | Greitkelio „blue hour“ kadras (v2 medija 29374299, nuotrauka ir poster), atskira telefono versija. **Split Line Heading `font_style="h1"`, fit to container**, pvz. „Lietuva – Airija – Ispanija“; SEO sakinys stiklinėje kortelėje | Harbor hero formatas, SGP maršrutai kaip „vardas“ |
| Stiklinė kortelė: nuotrauka, tekstas, „Book a Call“ | Dvi `arrow-circle-animation` pill nuorodos „Į Airiją +370 650 53161“, „Į Ispaniją +370 638 28919“ (`tel:`) ir eilutė „Artimiausias išvykimas: …“ | Pirmame ekrane iš karto galima paskambinti |
| 3 paslaugų kortelės | **6 grupių kortelės** (Kroviniai; Daiktai ir perkraustymas; Automobiliai ir motociklai; Keleiviai; Gyvūnai; Siuntos). Kortelėje „01 / 06“, pavadinimas, įžanga, paslaugų nuorodos (`nectar_cta`), nuotrauka. Paskutinė kortelė – „Visos 11 paslaugų →“ | 11 kortelių horizontaliame slinkime per ilgai; grupės jau yra `src/data/paslaugos.json` |
| „Difference“ (2 nuotraukos + 3 naudos) | „(Kelionėje)“: 2 salono nuotraukos ir naudos (atlenkiamos sėdynės, kondicionierius, keleiviai apdrausti, poilsio režimas) | Tas pats Salient Studio šablonas „Harbor Difference“ |
| Parallax dangaus juosta su 3 skaičiais | Parallax kelio nuotrauka, H2 „Du namai, vienas kelias tarp jų.“ su scroll-opacity-reveal, 4 skaičiai su stikliniais ženkliukais: 2 kryptys / 11 paslaugų / 3–4 paros / 4 šalys pakeliui | v2 turinys, Harbor forma |
| Atsiliepimai (layered cards) | **Paslėpti**, kol nėra tikrų. Vėliau ta pati forma: raidė, nuotrauka, citata | Nerodyti netikrų atsiliepimų |
| Kainų lentelė (3 planai) | **Dvi maršrutų kortelės** (Lietuva ⇄ Airija, Lietuva ⇄ Ispanija). Vietoje „$99 /month“ rašoma „3–4 / paros kelyje“, fancy-ul su artimiausiomis datomis ir vežamais dalykais, du `arrow-circle` mygtukai (LT numeris / tikslo šalies numeris). Ženkliukas „Artimiausias“ (Extra 1) ant kortelės su artimiausiu išvykimu. Logotipų juostos nėra | Harbor Pricing forma tinka maršrutams |
| CTA su Content Trail („Say hello“…) | „Norite užsakyti? Paskambinkite arba parašykite.“, visas stulpelis veda į /kontaktai/. Content Trail žymos: „Airija“, „Ispanija“, „Siunta“, „Keleivis“, „Automobilis“, „Gyvūnas“, spalvos raudona / juoda / pilka. `prefers-reduced-motion` (reduced motion) atveju išjungti | Harbor žaismas su SGP turiniu |
| Footeris „Harbor“ ant animuoto raudono gradiento | Tas pats su „SGP pervežimai“ (`#ef4539`, speed 850). Virš jo 3 stulpeliai: Airija (LT / IE numeriai), Ispanija (LT / ES numeriai), el. paštas ir nuorodos | Kontaktai yra svarbiausias footerio turinys |
| Contact: forma ir nuotrauka su citata | /kontaktai/: kairėje (2/5, `#f1efed`) Fluent Forms užklausa su paslaugos pasirinkimu (`?domina=`), dešinėje (3/5) nuotrauka su `mask blur-gradient` ir abiem kryptimis su numeriais vietoje citatos | Harbor Contact + v2 forma |

### 5.4 Puslapių žemėlapis

| SGP puslapis | Šablonas | Pastabos |
|---|---|---|
| `/` Pradžia | Harbor Landing (5.3 seka) | Harbor Studio šablonai eilės tvarka |
| `/pervezimo-paslaugos/` | Architect About viršus (H1 letter-reveal ir 1/5 nuorodos į 6 grupes) + kiekviena grupė kaip Harbor horizontal-scrolling kortelė **arba** Fancy Box „Image Above Text Underline“ tinklelis 3 stulpeliais | v2 Pinned Sections → Stacking (horizontal_effect `stacking`) irgi 18.2.1 parinktis |
| 11 paslaugų puslapių `/pervezimo-paslaugos/tarptautiniai-pervezimai/…/` | Architect projekto puslapis: hero per visą plotį (nuotrauka su parallax fade, H1 centre, įžanga), teiginys „(Apie paslaugą)“, faktai kaip numeruotos eilutės su Divider, toggles DUK, CTA, juosta „Kita paslauga →“ per visą plotį | Paslaugos lieka **puslapiais** (URL nekeičiami). „Next“ juosta pagal Architect formą, bet sukurta ranka, jei nenaudojamas Salient Portfolio |
| `/pervezimo-paslaugos/tarptautiniai-pervezimai/` | Harbor maršrutų kortelės ir žemėlapio schema (Raw HTML SVG, restilizuota: juodos 1,5 px linijos, raudonas aktyvus maršrutas) | |
| `/pervezimu-grafikas/` | Architect About viršus + Tabbed Section (2 kryptys) + `[sgp_grafikas]` eilutės Harbor kainų lentelės stiliumi (1 px linijos `#0000001a`, tabular skaičiai, visa eilutė yra `tel:` nuoroda) | Duomenų šaltinis lieka ACF |
| `/siuntos-sekimas/` | Harbor Contact išdėstymas (2/5 laukas, 3/5 nuotrauka) | |
| `/taisykles/` | Architect „Culture“ numeruotos eilutės + Toggles su skaičiais skliaustuose („Draudžiama siųsti (12)“) | |
| `/apie-imone/` | Architect About (H1 ir nuorodos, parallax nuotrauka, didelis teiginys, faktai) + Harbor statistikos juosta | |
| `/kontaktai/` | Harbor Contact (5.3) | |
| `/privatumo-politika/`, 404 | Paprastas tekstas 60ch pločio, H1 kaip Architect | |

### 5.5 Importas: eiga
1. **Testinė WordPress aplinka**, ne veikianti svetainė: importas perrašo Theme Options.
2. Įdiegti Salient 18.2.1, Salient Core, Salient WPBakery Page Builder, Salient Demo Importer ir **Fluent Forms**.
3. Salient → Demo Importer → **Harbor** → visi trys jungikliai ON (Demo Content, Theme Option Settings, Widgets) → Confirm. Importeris pats priskiria „Harbor Landing“ kaip pradžios puslapį, sukuria Global Sections ir Fluent formą.
4. **Theme Options → General → Accent Colors:** Accent `#1c1d1d`, Extra 1 `#ef4539`, Extra 2 `#c4301e`, Extra 3 `#f1efed`. **Typography:** Inter Tight 500 antraštėms, body 17 px (5.3). **Header Hide Until Needed:** OFF. **Header:** logotipas `assets/img/logo.svg` / `logo_light.svg` (starting logo ant hero).
5. **Architect:** atskiroje bandomojoje svetainėje (arba toje pačioje su **Theme Option Settings OFF** ir Widgets OFF). Reikia Salient Social ir Salient Portfolio. About, Projects ir „23 World Plaza“ eilutes išsaugoti kaip WPBakery šablonus, po to Architect turinį ištrinti.
6. Salient Studio šablonus („Harbor …“, „Architect Carousel“) galima įterpti tiesiai: WPBakery → Add Template → Salient Studio.

### 5.6 Rizikos ir ką patikrinti
- **Kontrastas:** baltas tekstas ant `#ef4539` turi 3,76:1, todėl raudonose plokštumose naudoti juodą tekstą (`#000` 5,58:1) arba ≥ 24 px baltą. `#1c1d1d` ant `#ef4539` turi 4,49:1, t. y. ribinė reikšmė, smulkiam tekstui naudoti `#000`.
- **Reduced motion:** Salient 18.2.1 kode (`js/build`, `css/build`, Salient Core `js`/`css`) `prefers-reduced-motion` nėra, todėl tema pati judesio neišjungia. Reikia Custom CSS/JS (jį numato ir CLAUDE.md taisyklė nr. 4): kai įjungtas reduced motion, išjungti Lenis, Split Line Heading ir kolonų animacijas, Content Trail, Scrolling Text ir parallax. v2 taisyklė „M## judesys išjungiamas“ perkeliama į šį sluoksnį.
- **Horizontal-scrolling su 6+1 kortele** yra apie 5 ekranai slinkimo. Reikia palikti v2 „Praleisti paslaugų juostą“ nuorodą (Salient elementas to neturi) arba apriboti iki 4 kortelių ir paskutinės „Visos paslaugos“.
- **Fit-text H1:** ilgesnis lietuviškas tekstas susitraukia. Esant 390 px ekranui „Lietuva – Airija – Ispanija“ bus apie 34–38 px, tai gerai. Ilgesnių frazių nedėti.
- **Juosta telefone:** Harbor ją rodo ir telefone. SGP atveju tai gerai, nes vieta „Before Scrolling“ reiškia, kad juosta slenkant dingsta. Bet v2 sprendimas buvo „tik kompiuteryje“, todėl apie tai reikia pranešti klientui.
- **v2 sprendimai, kurie keičiasi:** marquee (v2 buvo uždraudęs kaip „v1 judesį“) grįžta kaip Harbor signatūra su tikrais duomenimis; bėgančios lentos lenta, kelio juosta su žiedais ir mono užrašai **atsisakomi**, nes tai buvo bespoke elementai, ne Salient.
- **18.3 skirtumai:** gyvi demo naudoja 18.3.0, o importo duomenys ir kodas patikrinti su 18.2.1. Jei kuri nors parinktis Theme Options pavadinta kitaip, šaltinis yra `options-config.php` 18.2.1.

---

## 6. 12 vizualinių bruožų, kuriuos perimame

1. **Spalvos kaip plokštumos:** baltas fonas, beveik juodas `#1c1d1d` tekstas ir mygtukai, raudona `#ef4539` tik didelėms plokštumoms (juosta, kortelė, ženkliukas, footerio gradientas). Raudonų linijų ir žiedų nėra.
2. **Raudona slenkanti juosta virš antraštės:** Global Section „In Navigation Top Before Scrolling“, Scrolling Text ltr / slow / `✦` / 0,9rem, juodas tekstas. Joje artimiausi išvykimai iš `[sgp_grafikas]`, nuoroda į grafiką.
3. **Permatoma pilno pločio antraštė:** default formatas, padding 22, Text Reveal hover. Joje raudonas „Skambinti“ pill (`fa-phone`, Button Extra Color #1, Persist In Mobile Navigation Header). Telefone apvalus juodas off-canvas mygtukas.
4. **Hero 100svh:** parallax fade nuotrauka (atskira telefono versija), Split Line Heading H1 per visą plotį su `letter-reveal-blur-top`. Apačioje stiklinė kortelė (blur 16, `#0000006E`, r15) su dviem skambinimo pill ir artimiausiu išvykimu. 1 px baltos linijos.
5. **Vienas šriftas Inter Tight:** sakinio rašyba, be didžiųjų raidžių ir mono. Fluid rem skalė: H1 4rem, H2 2,7rem, H3 2rem, body 1,0625rem / 1,6, antraštės 500 −0,02em.
6. **Skliausteliuose rašomi „eyebrow“ užrašai** („(Paslaugos)“) body dydžiu ir **didelės H5 įžangos** Responsive Text elementu. Jie pakeičia v2 mono UPPERCASE užrašus.
7. **„Pill“ mygtukai su rodykle apskritime** (`nectar_cta arrow-circle-animation`, r100): ant nuotraukos balti stikliniai, ant balto fono juodi. Tekstinės nuorodos su 1 px `ltr-fancy` animuotu pabraukimu.
8. **Paslaugos kaip horizontaliai slenkančios spalvinės kortelės** (Sticky Media Sections → Horizontal Scrolling, 85 %, 100vh, tarpas 5 px, r15). Spalvos keičiasi raudona / juoda / `#f1efed`, didelis numeris „01“, nuotrauka dešinėje. Telefone kortelės vertikaliai viena po kitos.
9. **Parallax statistikos juosta:** vc_section su parallax (fast) nuotrauka, H2 ryškėja slenkant (scroll-opacity-reveal), stikliniai ženkliukai (`#FFFFFF1F`, blur 12, r20) ir dideli skaičiai 3vw: 2 kryptys / 11 paslaugų / 3–4 paros / 4 šalys.
10. **Vidiniai puslapiai pagal Architect:**
    - H1 letter-reveal ir 1/5 stulpelis su nuorodomis į puslapio dalis;
    - paslaugos hero per visą plotį su H1 centre;
    - numeruotos 01/02/03 eilutės su Divider taisyklėms ir procesui;
    - Fancy Box „Image Above Text Underline“ 4:5;
    - juosta „Kita paslauga →“ per visą plotį.
11. **Natyvi judesio sistema:**
    - Lenis smooth scroll 85;
    - kolonų atsiradimas easeOutCubic 1300 ms;
    - Split Line Heading eilučių ir raidžių atsiradimas;
    - Architect parallax nuotraukų stulpeliai;
    - View Transitions tarp puslapių (telefone išjungta);
    - Content Trail žymos paskutiniame CTA;
    - layered-card atsiliepimai, kai atsiras tikrų.
12. **Footeris:** plona informacinė eilutė su numeriais pagal kryptį, socialiniais tinklais ir © metais, tada Divider ir animuoto raudono gradiento juosta su „SGP pervežimai“ per visą plotį. Visur konteineris 1600, šoniniai tarpai 40 px (telefone 6 %), eilutės 10 % / 5 %, apvalinimai 10 / 15 / 20 / 100 px.
