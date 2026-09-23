# SGP pervežimai — esamo tinklapio turinys (puslapiai)

Šaltinis: https://www.sgp-pervezimai.lt (Joomla, šablonas „b4“, kūrėjas itsolutions.lt). Nuskaityta 2026-09-23 su `curl`, tekstas išgautas iš žalio HTML (python `html.parser`), paliekant originalią rašybą (įskaitant klaidas). Apsaugoti nuo šiukšlių el. pašto adresai iššifruoti iš Joomla „cloak“ skripto.

Puslapių eiliškumas: 1) Pradžia, 2) Apie įmonę, 3) Pervežimo paslaugos, 4) Tarptautiniai pervežimai, 5) Pervežimų grafikas, 6) Siuntos sekimas, 7) Taisyklės, 8) Kontaktai, 9) Privatumo politika.

## Navigacija ir poraštė

### Pagrindinis meniu (antraštė, visuose puslapiuose)

Kairėje — logotipas (https://www.sgp-pervezimai.lt/images/logo/logo.svg) su nuoroda į pradžią; logotipo viduje paslėpta antraštė `<h1 class="logo_title">Pervežimas</h1>` (t. y. **H1 visuose puslapiuose = „Pervežimas“**). HTML komentare paliktas ir šviesus logotipo variantas https://www.sgp-pervezimai.lt/images/logo/logo_light.svg.

- [Pradžia](https://www.sgp-pervezimai.lt/)
- [Apie mus](https://www.sgp-pervezimai.lt/apie-imone)
- [Pervežimo paslaugos](https://www.sgp-pervezimai.lt/pervezimo-paslaugos) *(išskleidžiamas submeniu)*
  - [Tarptautiniai pervežimai](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai)
  - [Siuntos sekimas](https://www.sgp-pervezimai.lt/siuntos-sekimas)
- [Taisyklės](https://www.sgp-pervezimai.lt/taisykles)
- [Kontaktai](https://www.sgp-pervezimai.lt/kontaktai)
- **Susisiekite** — mygtukas (`btn btn-outline-warning`), atidaro modalinį langą `#modal-a` su užklausos forma (žr. žemiau)

Mobiliame vaizde meniu atsidaro kaip šoninis skydelis (`sidebar right`, „hamburger“ `fa-bars`) su tais pačiais punktais.

**Pastaba:** puslapis „Pervežimų grafikas“ (https://www.sgp-pervezimai.lt/pervezimu-grafikas) pagrindiniame meniu **nėra** — į jį patenkama tik per pradžios puslapio „hero“ plytelę.

### Modalinis langas „Susisiekite“ (visuose puslapiuose)

**[H2]** Susisiekite

Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!

Formoje pateikti duomenys naudojami susisiekimui su klientu

Forma `#contact-form_213` (modulis its_form, ID 213):

| Laukas (placeholder) | Tipas | Privalomas | Paaiškinimas (title / tooltip) |
|---|---|---|---|
| Jūsų vardas | text | taip | Jūsų vardas |
| El. pašto adresas | email | taip | El. pašto adresas naudojamas išsiųti pasiūlymui parengtams pagal kliento poreikius. Saugomas mūsų sistemoje iki vartotojo pareikalavimo panaikinti duomenis. |
| Telefono numeris | tel | taip | Telefono numeris naudojamas susisiekti su klientu ir pasitikslinti detales, kurios reikalingos pasiūlymo parengimui. Saugomas mūsų sistemoje iki vartotojo pareikalavimo panaikinti duomenis. |
| Kas Jus domina? | text | taip | Kas Jus domina? |
| Žinutė | textarea | taip (min. 20 simbolių) | Žinutė |
| Google reCAPTCHA v2 | — | taip | sitekey `6LedWYsUAAAAANrPFYsOMCFWF3aQlg2EmLAN3CxN` |

Mygtukas: **Gauti pasiūlymą**

Pranešimai: „Jūsų žinutė sėkmingai išsiųsta“ / „Oi kažkas ne taip! Bandykite dar kartą.“ / „Įveskite teisingą apsaugos kodą.“

Formų veikimas (visos its_form formos): AJAX `POST` į tą patį puslapio URL — pirmiausia `option=com_ajax&module=its_form&method=recaptcha&format=raw` (reCAPTCHA patikra), jei atsakymas `s` — antras `POST` `option=com_ajax&module=its_form&format=raw` su visais formos laukais (`data`).

### Poraštė (visuose puslapiuose)

**1 blokas — „Susisiekite su mumis“** (sekcija `bottom-b`; kontaktų puslapyje šio bloko poraštėje nėra, nes jis rodomas turinyje; privatumo politikos puslapyje jo taip pat nėra):

**[H2]** Susisiekite su mumis

**[H6]** Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!

**[H6]** El. paštas: saugiai.greitai.patikimai@gmail.com

*(HTML'e adresas užkoduotas Joomla „email cloak“ skriptu; be JS rodomas tekstas „Šis el. pašto adresas yra apsaugotas nuo šiukšlių. Jums reikia įgalinti JavaScript, kad peržiūrėti jį.“)*

**[H5]** PERVEŽIMAI Į AIRIJĄ
- Tel.: [+370 650 53161](tel:+37065053161)
- Tel.: [+353 864 503104](tel:+353864503104)
- Tel.: [+447566878681](tel:+447566878681)

**[H5]** PERVEŽIMAI Į ISPANIJĄ
- Tel.: [+370 638 28919](tel:+37063828919)
- Tel.: [+34 60 25 47929](tel:+34602547929)

Šalia — užklausos forma `#contact-form_207`:

Formoje pateikti duomenys naudojami susisiekimui su klientu

| Laukas (placeholder) | Tipas | Privalomas | Paaiškinimas (title) |
|---|---|---|---|
| Jūsų vardas | text (`name`) | taip | Jūsų vardas |
| El. pašto adresas | email | taip | El. pašto adresas naudojamas išsiųti pasiūlymui parengtams pagal kliento poreikius. Saugomas mūsų sistemoje iki vartotojo pareikalavimo panaikinti duomenis. |
| Žinutės tema | text (`subject`) | taip | Žinutės tema |
| Žinutė | textarea (`message`) | taip (min. 5 simboliai) | Žinutė |
| (paslėptas) `url` | hidden | — | dabartinio puslapio URL |
| Google reCAPTCHA v2 | — | taip | — |

Mygtukas: **Susisiekite su mumis**

**2 blokas — tamsi poraštė** (sekcija `footer-b`):

- Logotipas (šviesus, PNG): https://www.sgp-pervezimai.lt/cache/images/moditsimage/223/27/1471c0b8d23b647a9bf2e7aa98c2b3cf_387_60_r.png (alt tuščias)
- Meniu stulpelis **„Tarptautiniai pervežimai“** (11 paslaugų puslapių):
  - [Krovinių pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/kroviniu-pervezimas)
  - [Negabaritinių krovinių pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/negabaritiniu-kroviniu-pervezimas)
  - [Dalinių krovinių gabenimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/daliniu-kroviniu-gabenimas)
  - [Daiktų pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/daiktu-pervezimas)
  - [Automobilių pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/automobiliu-pervezimas)
  - [Motociklų pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/motociklu-pervezimas)
  - [Keleivių pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/keleiviu-pervezimas)
  - [Gyvūnų pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/gyvunu-pervezimas)
  - [Siuntų pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/siuntu-pervezimas)
  - [Siuntų pristatymas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/siuntu-pristatymas)
  - [Perkraustymo paslaugos](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/perkraustymo-paslaugos)

**3 blokas — autorių teisės** (sekcija `copyright`):

© 2026 sgppervezimai.lt Visos teisės saugomos.

Sukurta: [itsolutions.lt](http://www.itsolutions.lt)

**Slapukų juosta** (rodoma apačioje):

**[H4]** Informuojame, kad šioje svetainėje naudojami slapukai (angl. cookies)

Sutikdami, paspauskite mygtuką „Sutinku“ arba naršykite toliau. Savo duotą sutikimą bet kada galėsite atšaukti pakeisdami savo interneto naršyklės nustatymus ir ištrindami įrašytus slapukus

Mygtukai: **Sutinku** · [Plačiau](https://www.sgp-pervezimai.lt/privatumo-politika/policies)

**Socialiniai tinklai / pokalbių programėlės:** svetainėje **nėra** jokių Facebook, Instagram, LinkedIn, Messenger, Viber ar WhatsApp nuorodų (patikrinta visuose 9 puslapiuose).

**Bendri techniniai elementai:** Google Tag Manager `GTM-WCW69V4`, Google Analytics `UA-115748704-1`, Google reCAPTCHA v2, OG paveikslėlis pagal nutylėjimą https://www.sgp-pervezimai.lt//templates/b4/images/og_image.jpg, favicon https://www.sgp-pervezimai.lt/templates/b4/favicon.png.

**Spalvos (iš šablono CSS):** pagrindinė raudona `#ef4539` (rgba(239,69,57)) — mygtukai, akcentai; tamsi `rgba(29,29,29)`; mėlyna `rgba(46,107,169)` (#2e6ba9); fonai balti / `#fcfcfc` / `#f3f3f3`. Ikonos — „Flaticon“ šriftas (`flaticon-truck-2`, `flaticon-calendar-1` ir kt.) ir Font Awesome.

---

## Visos pervežimo paslaugos | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/

- **Title:** Visos pervežimo paslaugos | sgp-pervezimai.lt
- **Meta description:** SGP Pervezimai paslaugos keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, pervezimai i Airija Prancuzija Ispanija
- **Meta keywords:** Keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, paslaugos, pervezimai, Airija, Prancuzija, Ispanija
- **H1:** Pervežimas (paslėptas logotipe)
- **OG image:** https://www.sgp-pervezimai.lt//templates/b4/images/og_image.jpg

### Blokas 1 — „Hero“ slankiklis (carousel `#items-carousel-132`, fullscreen, fade)

Slankiklyje yra **tik 1 skaidrė**. Fono paveikslėlis: https://www.sgp-pervezimai.lt/cache/images/k2/383/23/d9b6a84b782c3c0b7f4396f4cbb2f90c_2000_1000_c.jpg

Tekstas (dešinėje, didžiosiomis raidėmis):

> Visos pervežimo **paslaugos**
>
> **saugiai greitai patikimai**

Po tekstu — 2 plytelės (ikonos raudonos/geltonos `text-warning`, antraštės H2 baltos):

| Ikona | Antraštė (H2) | Nuoroda |
|---|---|---|
| `flaticon-truck-2` (sunkvežimis) | Tarptautiniai pervežimai | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai |
| `flaticon-calendar-1` (kalendorius) | Pervežimų grafikas | https://www.sgp-pervezimai.lt/pervezimu-grafikas |

Apačioje — rodyklė žemyn (`fa-angle-down`, „scroll-page“).

### Blokas 2 — „Artimiausi pervežimai“ (sekcija `main-top`, fonas https://www.sgp-pervezimai.lt/images/template/sections/sgp.jpg)

**[H2]** Artimiausi pervežimai

4 kortelės (H3 + datos `<time>`), tekstas pažodžiui:

| Maršrutas (H3) | Datos |
|---|---|
| Lietuva - Airija | Spalio - 09d. ; 23d. |
| Lietuva - Ispanija | Spalio - 09d. ; 23d. |
| Airija - Lietuva | Rugsėjo - 28d. / Spalio - 15d.; 28d. |
| Ispanija - Lietuva | Rugsėjo - 27d. / Spalio - 14d.; 28d. |

(„/“ žymi atskiras `<time>` eilutes toje pačioje kortelėje. Metai nenurodyti.)

### Blokas 3 — „Apie įmonę“ (sekcija `main-bottom`, `items-block split`, šviesus tekstas ant tamsaus fono)

**[H2]** Apie įmonę

**„SGP“** – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu **Lietuva – Ispanija – Lietuva**, **Lietuva – Airija – Lietuva** ir kitas Europos šalis (**Vokietiją, Prancūziją**).

Mygtukas: [Skaityti daugiau](https://www.sgp-pervezimai.lt/apie-imone)

### Blokas 4 — Poraštė

„Susisiekite su mumis“ blokas su telefonais ir forma, tamsi poraštė su paslaugų meniu, copyright — žr. skyrių „Navigacija ir poraštė“.

### Paveikslėliai pradžios puslapyje

| URL | Paskirtis | Alt |
|---|---|---|
| https://www.sgp-pervezimai.lt/images/logo/logo.svg | Logotipas antraštėje | (nėra) |
| https://www.sgp-pervezimai.lt/cache/images/k2/383/23/d9b6a84b782c3c0b7f4396f4cbb2f90c_2000_1000_c.jpg | Hero slankiklio fonas (CSS background) | — |
| https://www.sgp-pervezimai.lt/images/template/sections/sgp.jpg | „Artimiausi pervežimai“ sekcijos fonas (CSS `.main-top`) | — |
| https://www.sgp-pervezimai.lt/cache/images/moditsimage/223/27/1471c0b8d23b647a9bf2e7aa98c2b3cf_387_60_r.png | Logotipas poraštėje | (tuščias) |

---

## Apie įmonę | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/apie-imone

- **Title:** Apie įmonę | sgp-pervezimai.lt
- **Meta description:** „SGP“ – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu Lietuva – Ispanija – Lietuva, Lietuva – Airija – Lietuva ir kitas Europos šalis (Vokietiją, Prancūziją).
- **Meta keywords:** lietuva, bei, kvalifikuota, tik, saugų, greitą, patikimą, pervežimą
- **OG title:** Apie įmonę · **OG image:** https://www.sgp-pervezimai.lt/cache/images/k2/358/23/242b05aae70bf32c41a3f5b7ecd2ef9c_2000_1000_c.jpg
- **Puslapio antraštė (juosta, H2):** Apie mus — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias (breadcrumbs):** Pradžia › Apie įmonę

### Pagrindinis tekstas

**„SGP“** – esame įmonė įsikūrusi Lietuvoje, kuri užsiima keleivių, siuntų ir automobilių pervežimu **Lietuva – Ispanija – Lietuva**, **Lietuva – Airija – Lietuva** ir kitas Europos šalis (**Vokietiją, Prancūziją**).

Nuo pirmos darbo dienos savo klientams užtikriname ne tik saugų, greitą bei patikimą pervežimą, bet ir malonų bendravimą su kvalifikuota bei patyrusia komanda.

Mes visada pasiruošę teikti kokybiškas transporto paslaugas už Jums prieinamą kainą!

### Šoninis blokas (dešinėje)

**[H3]** Saugiai greitai patikimai

SGP – visos pervežimo paslaugos

Galerija (iGallery #39, 5 nuotraukos, `title="Apie įmonę"`, alt tušti; paspaudus atsidaro didesnis vaizdas):

| # | Miniatiūra (360×280) | Didelis vaizdas (1000×900) |
|---|---|---|
| 1 | https://www.sgp-pervezimai.lt/cache/images/igallery/39/251/22/bf602a61230c39d4a76435451df061af_360_280_c.jpg | https://www.sgp-pervezimai.lt/cache/images/igallery/39/251/24/bf602a61230c39d4a76435451df061af_1000_900_r.jpg |
| 2 | https://www.sgp-pervezimai.lt/cache/images/igallery/39/252/22/2804b0101066ba5cad1319c1b0d417e3_360_280_c.jpg | https://www.sgp-pervezimai.lt/cache/images/igallery/39/252/24/2804b0101066ba5cad1319c1b0d417e3_1000_900_r.jpg |
| 3 | https://www.sgp-pervezimai.lt/cache/images/igallery/39/253/22/db3c7ea75f94be58763537c75689f9fd_360_280_c.jpg | https://www.sgp-pervezimai.lt/cache/images/igallery/39/253/24/db3c7ea75f94be58763537c75689f9fd_1000_900_r.jpg |
| 4 | https://www.sgp-pervezimai.lt/cache/images/igallery/39/254/22/04bc288b31244ae9d50377a9e8219731_360_280_c.jpg | https://www.sgp-pervezimai.lt/cache/images/igallery/39/254/24/04bc288b31244ae9d50377a9e8219731_1000_900_r.jpg |
| 5 | https://www.sgp-pervezimai.lt/cache/images/igallery/39/255/22/8d7ee4af202b26c6f949af4e1c03a75c_360_280_c.jpg | https://www.sgp-pervezimai.lt/cache/images/igallery/39/255/24/8d7ee4af202b26c6f949af4e1c03a75c_1000_900_r.jpg |

(Yra ir kitų dydžių variantai: `_570_350_c`, `_328_200_c`, `_185_164_c`.)

### Blokas po turiniu

**[H2]** Pervežimo paslaugos

Viena plytelė: ikona `flaticon-truck-2` + [Tarptautiniai pervežimai](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai)

---

## Pervežimo paslaugos | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/pervezimo-paslaugos

- **Title:** Pervežimo paslaugos | sgp-pervezimai.lt
- **Meta description:** Profesionalios keleivių, krovinių, automobilių, gyvūnų, daiktų pervežimo paslaugos mikroautobusais. Susisiekite jau dabar!
- **Meta keywords:** paslaugos, pervežimo, bei, keleivių, paslaugų, mūsų, europoje, airiją
- **OG description:** Pervežimo paslaugų poreikis Europoje nuolat auga. Tai – puikus būdas komunikuoti, keistis apčiuopiama informacija, prekėmis ir kitais daiktais tarp fi...
- **OG image:** `https://www.sgp-pervezimai.lt/home/sc000378/domains/sgp-pervezimai.lt/public_html/media/k2/categories/82.jpg` (neveikia — 404, serverio kelias)
- **Puslapio antraštė (juosta, H1):** Pervežimo paslaugos — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias:** Pradžia › Pervežimo paslaugos

### Plytelės (K2 kategorijos sąrašas)

| Ikona | Antraštė (H2) | Nuoroda |
|---|---|---|
| `flaticon-truck-2` | Tarptautiniai pervežimai | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai |
| (be ikonos) | Siuntos sekimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/siuntos-sekimas |

### Kategorijos aprašymas (tekstas pažodžiui; `####` = originalo H5)

Pervežimo paslaugų poreikis Europoje nuolat auga. Tai – puikus būdas komunikuoti, keistis apčiuopiama informacija, prekėmis ir kitais daiktais tarp fizinių asmenų bei verslo subjektų skirtingose šalyse. Mūsų paslaugų sąraše: automobilių, gyvūnų, daiktų ir krovinių gabenimas bei keleivių pervežimo paslaugos. Platus paslaugų spektras suteikia universalumo, nes savo klientams galime pasiūlyti kur kas daugiau sprendimų.

Pervežimo paslaugos patrauklia kaina vykdomos tokiomis kryptimis Europoje: į / iš Airiją, į / iš Ispaniją, į / iš Vokietiją, į / iš Prancūziją. Keleivių, krovinių, automobilių, [gyvūnų pervežimas](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/gyvunu-pervezimas) nurodytais maršrutais trunka apie 3–4 paras, skaičiuojant nuo paėmimo dienos.

Pervežimo paslaugos į / iš Vokietiją, į / iš Prancūziją, į / iš Airiją, į / iš Ispaniją vykdomos naujais, techniškai tvarkingais, patogiais mikroautobusais. [Keleivių pervežimo paslaugos](https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/keleiviu-pervezimas) Europoje visiems keliaujantiems garantuoja komfortišką kelionę. Važiuodami mūsų mikroautobusais mėgausitės kiekviena kelionės minute, jausitės patogiai bet kuriuo metų laiku, pasirūpinsime, kad laikas neprailgtų.

#### Kodėl mūsų pervežimo paslaugos – geriausias sprendimas Jums?

Komandoje turime subūrę savo srities profesionalus, todėl garantuojame saugią ir sklandžia kelionę. Keleivinių ir siuntų gabenimą reglamentuojančių teisės aktų išmanymas leidžia išvengti įvairių niuansų bei nenumatytų atvejų. Patirtis ir žinios leidžia pasirinkti geriausią maršrutą, kad tikslą pasiektume ne tik greitai, bet ir saugiai. Negana to, kokybiškos pervežimo paslaugos itin patrauklia kaina yra tai, dėl ko pelnėme plataus klientų rato simpatijas.

---

## Tarptautiniai pervežimai Europoje (mikroautobusais) | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai

- **Title:** Tarptautiniai pervežimai Europoje (mikroautobusais) | sgp-pervezimai.lt
- **Meta description:** Tarptautiniai pervežimai Europoje, krovinių gabenimas tarptautiniais maršrutais. Domina Sgppervezimai.lt – paslaugos? Susisiekite jau dabar!
- **Meta keywords:** pervežimai, kad, mūsų, siuntos, jei, daiktai, tarptautiniai, taip
- **OG title:** Tarptautiniai pervežimai · **OG description:** SGP pervežimai – komanda savo srities profesionalų, turinčių vieningą tikslą – užtikrinti, kad siuntiniai ir keleiviai į Ispaniją ir Airiją keliautų s...
- **Puslapio antraštė (juosta, H1):** Tarptautiniai pervežimai — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias:** Pradžia › Pervežimo paslaugos › Tarptautiniai pervežimai

### Paslaugų plytelės (11 vnt., H2, kiekviena veda į atskirą paslaugos puslapį)

| # | Ikona | Paslauga | Nuoroda |
|---|---|---|---|
| 1 | `flaticon-deliver-2` | Krovinių pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/kroviniu-pervezimas |
| 2 | `flaticon-box-1` | Negabaritinių krovinių pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/negabaritiniu-kroviniu-pervezimas |
| 3 | `flaticon-box-4` | Dalinių krovinių gabenimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/daliniu-kroviniu-gabenimas |
| 4 | `flaticon-shipping-1` | Daiktų pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/daiktu-pervezimas |
| 5 | `flaticon-tow-truck` | Automobilių pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/automobiliu-pervezimas |
| 6 | `flaticon-motorcycle` | Motociklų pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/motociklu-pervezimas |
| 7 | `flaticon-passenger` | Keleivių pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/keleiviu-pervezimas |
| 8 | `flaticon-cage` | Gyvūnų pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/gyvunu-pervezimas |
| 9 | `flaticon-truck-7` | Siuntų pervežimas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/siuntu-pervezimas |
| 10 | `flaticon-package` | Siuntų pristatymas | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/siuntu-pristatymas |
| 11 | `flaticon-warehouse` | Perkraustymo paslaugos | https://www.sgp-pervezimai.lt/pervezimo-paslaugos/tarptautiniai-pervezimai/perkraustymo-paslaugos |

### Kategorijos aprašymas (tekstas pažodžiui; `####` = originalo H5)

SGP pervežimai – komanda savo srities profesionalų, turinčių vieningą tikslą – užtikrinti, kad siuntiniai ir keleiviai į Ispaniją ir Airiją keliautų saugiai, greitai, patikimai ir komfortiškai.

Tarptautiniai pervežimai Europoje – tai mūsų veiklos pagrindas. **Vežame keleivius, gabename siuntas ir automobilius dviem maršrutais:**

- iš Lietuvos į Ispanija ir atgal;
- iš Lietuvos į Airiją ir atgal.

Tarptautiniai pervežimai minėtais maršrutais apima ir tokias Europos šalis kaip Lenkija, Vokietija, Belgija, Prancūzija, todėl nedvejokite, jei norite perduoti siuntą jose gyvenantiems artimiesiems, draugams ar verslo partneriams, taip pat jei norite šias šalis aplankyti ir patys.

#### Kodėl verta pasitikėti mumis?

- Mūsų tarptautinių pervežimų paslauga apima keleivių, siuntinių, gyvūnų, negabaritinių krovinių gabenimą.
- Solidus patirties ir žinių bagažas suponuoja, kad išmanome keleivių ir siuntų transportavimui aktualius teisės aktus, žinome visus kelionėje galinčius kilti niuansus, taip pat kitus su transportavimu Europoje susijusius ypatumus.
- Tarptautinis krovinių gabenimas vyksta konkurencingoje aplinkoje, kurioje gebame puikiai laviruoti, nes didžiausiu konkurenciniu pranašumu laikome sako žmogiškųjų išteklių profesionalumą ir vieningumą.
- Tarptautiniai pervežimai vykdomi tik naujausiais mikroautobusais, siekiant užtikrinti siuntinių saugumą ir keleivių komfortą. Visi mikroautobusai, kuriais vežame keleivius, turi tokius ypatumus: atlenkiamas sėdynes – patogiai Jūsų kelionei tiek dieną, tiek naktį; šildomas sėdynes – komfortui net žvarbiausiomis žiemos dienomis; kondicionierius – kad oras autobuse visada būtų šviežias, o karštą vasaros dieną jaustumėtės patogiai; DVD – kad kelionė neprailgtų. Tai nebaigtinis patogumų sąrašas. Siuntos taip pat gabenamos naujais, patikimais mikroautobusais.
- Tarptautiniai pervežimai nuo durų iki durų – patogumas ir efektyvus laiko taupymas.
- Patrauklios kainos – daugeliui svarbus aspektas, tad užtiktiname labai gerą kainos ir kokybės santykį.
- Mūsų komandoje – tik atsakingi ir patikimi vairuotojai, kad kelionė bus saugi ir sklandi.
- Tarptautiniai pervežimai apima ir gyvūnų transportavimą.
- Automobilių tarptautiniai pervežimai Europoje – pasiūlysime geriausias sąlygas.

#### Krovinių pervežimas tarptautiniais maršrutais: ko negalima siųsti?

Tarptautiniai krovinių pervežimai turi tam tikrus apribojimus, kurių vieni svarbiausių – apribojimai siuntų turiniui. **Siekiame didžiausio savo klientų informuotumo, todėl pateikiame draudžiamų siųsti daiktų sąrašą:**

- vertingi daiktai (šiai kategorijai priklauso pinigai, čekiai, brangakmeniai, juvelyriniai dirbiniai, neapdirbti taurieji metalai, vertybiniai popieriai ir kiti brangūs daiktai, reikalaujantys papildomo draudimo);
- alkoholis, tabakas ir tabako gaminiai, visos narkotinės bei psichotropinės medžiagos;
- sprogiosios, degiosios, radioaktyviosios ir kitos pavojingos medžiagos;
- ginklai, amunicija, karo technika;
- daiktai, turintys nepadorių ar įžeidžiančio turinio užrašų ar paveikslų;
- greitai gendantys maisto produktai, pavyzdžiui, žalia mėsa ir pan.;
- visus daiktai, kuriuos draudžiama siųsti pagal mūsų šalies teisės aktus;
- visi daiktai, kuriuos pagal įstatymus draudžiama įvežti į šalį, į kurią keliauja siunta, bei į tranzitines šalis.

Už siuntinio turinį atsakingas siuntėjas. Prašome savo klientų nepakuoti draudžiamų siųsti daiktų ir taip užtikrinti sklandžią siuntos kelionę iki gavėjo. Mes pasiliekame sau teisę bet kuriame siuntinio transportavimo etape pakuotės turinį patikrinti, jei kyla įtarimų, kad joje – draudžiami siųsti daiktai. Įtarimams pasitvirtinus imsimės visų saugumo priemonių, o klientas, įteikęs mūsų komandai tokio turinio siuntą, privalės atlyginti mūsų įmonės patirtą žalą, atsiradusią dėl šio incidento.

Už valstybinių institucijų konfiskuotas siuntas mes atsakomybės neprisiimame.

#### Tarptautiniai pervežimai: ką dar turite žinoti?

Nepriklausomai nuo to, kuriuo mūsų maršrutu keliausite Jūs ar siųsite siuntą, pristatymas truks apie 3–4 paras nuo paėmimo datos.

Jei siųsite siuntą, labai svarbu, kad ji būtų įpakuota tinkamai. Tai – siuntėjo atsakomybė. Siuntoms pakuoti rekomenduojame naudoti naujas, standžias pakuotes, negailėti specialios medžiagos laisvai erdvei dėžėje užpildyti. Pakuotė turi apsaugoti ne tik Jūsų siunčiamus daiktus, bet ir nepadaryti žalos kitoms drauge keliaujančioms siuntoms. Mes neatsakome už tai, jei siuntos turinys bus apgadintas dėl netinkamos pakuotės, taip pat pasiliekame teisę klientui pareikšti pretenzijas, jei dėl netinkamo jo siuntos supakavimo mūsų kompanija arba tretieji asmenys patirs žalą.

Labai svarbu nurodyti tikslius siuntinio paėmimo ir pristatymo adresus Europoje. Jei sutartu laiku gavėjas arba siuntos adresatas negali atiduoti / paimti siuntos, pakartotinis mūsų atvykimas apmokestinamas.

Neretai siunčiami didesni, sunkesni daiktai, kurių iškrovimui reikalinga speciali technika. Tokiu atveju iškrovimu turi pasirūpinti siuntos gavėjas.

---

## Pervežimų grafikas | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/pervezimu-grafikas

- **Title:** Pervežimų grafikas | sgp-pervezimai.lt
- **Meta description:** SGP Pervezimai paslaugos keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, pervezimai i Airija Prancuzija Ispanija (numatytoji, tokia pati kaip pradžios)
- **Meta keywords:** Keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, paslaugos, pervezimai, Airija, Prancuzija, Ispanija
- **Puslapio antraštė (juosta, H1):** Pervežimų grafikas — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias:** Pradžia › Pervežimų grafikas

Pagrindinio turinio (`<main>`) blokas **tuščias**. Visas grafikas — tai modulis „Artimiausi pervežimai“ (`items-block235`, tas pats turinys kaip pradžios puslapyje), rodomas `main-bottom` sekcijoje:

**[H2]** Artimiausi pervežimai

| Maršrutas (H3) | Datos eilutė 1 | Datos eilutė 2 |
|---|---|---|
| Lietuva - Airija | Spalio - 09d. ; 23d. | — |
| Lietuva - Ispanija | Spalio - 09d. ; 23d. | — |
| Airija - Lietuva | Rugsėjo - 28d. | Spalio - 15d.; 28d. |
| Ispanija - Lietuva | Rugsėjo - 27d. | Spalio - 14d.; 28d. |

Išvestinė informacija (interpretacija, ne svetainės tekstas): išvykimai iš Lietuvos į Airiją ir Ispaniją — spalio 9 ir 23 d.; grįžimai iš Airijos — rugsėjo 28, spalio 15 ir 28 d.; iš Ispanijos — rugsėjo 27, spalio 14 ir 28 d. Ritmas ≈ kas 2 savaites. Metai nenurodyti (pagal nuskaitymo datą 2026-09-23 — datos aktualios, artimiausios).

Išvykimo/atvykimo laikai, vietos, kainos **nenurodyti**.

---

## Siuntos sekimas | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/siuntos-sekimas

- **Title:** Siuntos sekimas | sgp-pervezimai.lt
- **Meta description:** `&lt;b&gt;test&lt;/b&gt;` (t. y. „<b>test</b>“ — palikta testinė reikšmė)
- **Meta keywords:** `&lt, b&gt, test&lt, /b&gt` (testinė)
- **OG title:** Siuntos sekimas · **OG description:** tuščias („ “)
- **Puslapio antraštė (juosta, H2):** Pervežimo paslaugos *(ne „Siuntos sekimas“)* — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias:** Pradžia › Pervežimo paslaugos › Siuntos sekimas
- Tas pats puslapis pasiekiamas ir adresu https://www.sgp-pervezimai.lt/pervezimo-paslaugos/siuntos-sekimas (dublis).

### Turinys

**[H1]** Siuntos sekimas

Po antrašte — `<iframe src="https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1" width="100%" height="500">` (be rėmelio).

### Kaip veikia sekimo forma (iframe turinys)

- **Endpoint:** `https://siuntos.sgp-pervezimai.lt/sekimas.php` — `GET` forma (`action="?embed=1"`).
- **Laukai:**
  - `embed` — paslėptas, reikšmė `1`
  - `kodas` — tekstinis laukas, placeholder **„Siuntos kodas...“**
- **Mygtukas:** **Siuntos lokacija** (fonas `#ef4539`, baltas tekstas)
- **Užklausos pavyzdys:** `https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=<SIUNTOS_KODAS>`
- **Pranešimai (raudoni, `#e60023`, paryškinti):**
  - be kodo: „Neįvestas siuntos kodas!“
  - neteisingas kodas (pvz., `TEST123`): „Toks siuntos kodas neegzistuoja!“
- **Rezultatas:** puslapyje yra `<img style="max-height: 400px; width: auto;" src="">` — radus siuntą, matyt, rodomas siuntos vietos paveikslėlis/žemėlapis; puslapio `<title>` = „Map“, įkeltas Leaflet 1.7.1 CSS ir `#map` stiliai (400 px aukščio, suapvalinti kampai, šešėlis, `.map-overlay`). Teisingo kodo pavyzdžio neturime, todėl sėkmingo rezultato vaizdas nepatikrintas.
- Subdomeno šaknis https://siuntos.sgp-pervezimai.lt/ nukreipia į `/login` — tai siuntų valdymo sistemos (Laravel) administravimo prisijungimas, `<title>SIUNTOS.SGP-PERVEZIMAI.LT</title>`, meta author „UAB GP Soft“.

---

## Taisyklės | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/taisykles

- **Title:** Taisyklės | sgp-pervezimai.lt
- **Meta description:** Paslaugos Mokėtojai (užsakovai) privalo susipažinti su šiomis taisyklėmis ir vadovautis jomis ruošiant siuntas ir užsakant paslaugas.Siuntos išdalinamos per 3 dienas nuo atvykimo į šalį. Kelionė trunka nuo 2 iki 3 parų nuo išvykimo datos.Esant
  *(šio teksto matomame puslapyje nėra — tai tik meta aprašymas, nukirstas ties „Esant“)*
- **Meta keywords:** sgp, nuo, siuntas, privalo, yra, draudžiama, kuriuos, neatsako
- **OG title:** Siuntų siuntimo taisyklės · **OG description:** 1. Siuntų tikrinimas: Vežėjas pasilieka teisę patikrinti perduodamą siuntą, kad galėtų įsitikinti, jog siuntoje nėra draudžiamų vežti daiktų. Siuntėju...
- **Puslapio antraštė (juosta, H2):** Siuntų siuntimo taisyklės — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias:** Pradžia › Siuntų siuntimo taisyklės

### Taisyklių tekstas (pažodžiui; skyrių antraštės originale — H5 su linija `<hr>`)

#### 1. Siuntų tikrinimas:

Vežėjas pasilieka teisę patikrinti perduodamą siuntą, kad galėtų įsitikinti, jog siuntoje nėra draudžiamų vežti daiktų. Siuntėjui pageidaujant, patikrinimas atliekamas perdavimo metu, kitu atveju vežėjas įgyja teisę siuntą patikrinti bet kuriuo metu vėliau. Siuntėjas, pasirašydamas šią sutartį, patvirtina, kad sutinka, jog perduota siunta gali būti patikrinta perdavimo metu arba bet kada vėliau, pačiam Siuntėjau nedalyvaujant. Siuntos tikrinamos nepažeidžiant LR įstatymų.

#### 2. Siuntėjo garantija:

2.1. Siuntėjas garantuoja, kad perduodama siunta yra tinkamai supakuota ir paženklinta. Ant siuntos yra nurodyti tikslūs siuntėjo ir gavėjo adresai, telefono numeriai. Esant netiksliam adresui ar telefono numeriui, siunta gali būti nepristatyta gavėjui ir grąžinama į įmonės būstinę.

2.2. Siuntėjas garantuoja, kad siuntoje nėra draudžiamų siųsti daiktų, kurie yra išvardinti 4 punkte. Jeigu Siuntėjas pažeis 4 punkte numatytą draudimą, pasirašydamas šią sutartį, patvirtina, jog sutinka atlyginti visus dėlto Vežėjo ir trečiųjų asmenų patirtus nuostolius, įskaitant ir negautas pajamas.

2.3. Jeigu už siuntinį priskaičiuojami muito ar kiti mokesčiai, juos papildomai apmoka Siuntėjas.

#### 3. Vežėjo atsakomybė:

3.1. Vežėjas atsako už siuntų neišsaugojimą (sugadinimą, trūkumą, praradimą), atsiradusį dėl Vežėjo kaltės. Tokiu atveju Vežėjas sutinka atlyginti Siuntėjui patirtą žalą vadovaudamasis Lietuvos Respublikos įstatymais ir kitais teisės aktais nustatytais pagrindais ir tvarka.

3.2. Vežėjas neatsako už perduoto siuntinio sugadinimą ar trūkumą, jeigu jis nebuvo supakuotas ir paženklintas nesilaikant taisyklių.

3.3. Vežėjas neatsako už valstybės institucijų sulaikytą ar konfiskuotą siuntą.

3.4. Vežėjas įsipareigoja pristatyti perduotą siuntą per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos.

#### 4. Daiktai kuriuos įmonė vežti atsisako:

4.1. Daiktai ar medžiagos, kurių gabenimas yra uždraustas pagal valstybės įstatymus, kurios teritorijoje vykdomas pervežimas.

4.2. Nepriimami ir draudžiami vežti daiktai: 1) bet kokie tabako gaminiai; 2) bet kokie alkoholiniai gėrimai; 3) pinigai ir vertybiniai popieriai; 4) taurieji metalai; 5) juvelyriniai gaminiai; 6) vaistai ir maisto papildai; 7) šaunamiejii ir kiti ginklai; 8) meno kūriniai ir antikvariniai daiktai; 9) cheminiai kroviniai ir degios prekės 10) greitai gendantys maisto produktai; 11) daiktai, kurių pervežimui reikalingos specialios temperatūros, oro, drėgmės ir kitos papildomos sąlygos; 12) Visos kitos prekės, kurias vežti draudžiama įstatymais, bet kurios Vyriausybės ar valstybės bet kurioje šalyje kur prekės yra gabenamos.

4.3. Vežėjas neprisiima jokios atsakomybės už per klaidą priimtus vežti Sutarties 4.2. punkte numatytus daiktus.

4.4. Siuntėjas įteikdamas arba bet kokiu kitu būdu sąlygodamas perdavimą Vežėjui, daiktų, kurie yra numatyti Sutarties 4.2. punkte, prisiima visišką atsakomybę už tokių veiksmų sukeliamus teisinius padarinius ir įsipareigoja apmokėti visus Vežėjo dėl to patirtus nuostolius (gautas baudas, kitas patirtas išlaidas, negautas pajamas).

4.5. Siunta ar krovinys, kuriame buvo rasta draudžiamų vežti daiktų, grąžinamą į Vežėjo būstinę iš kur, Siuntėjas privalės atsiimti savo sąskaita, nes siunta nebus transportuojama. Prieš atsiimant minėto pobūdžio siuntą ar krovinį Siuntėjas įsipareigoja: 1) sumokėti siuntos transportavimo mokestį pagal nustatytus Vežėjo įkainius; 2) jam skirtą baudą už jo siuntoje rastus draudžiamus vežti daiktus; 3) atlyginęs visus kitus Vežėjo patirtus nuostolius dėl tokio pažeidimo. Siuntėjas, pasirašydamas šią sutartį, patvirtina, jog jam yra žinoma, kad dėl draudžiamų vežti daiktų transportavimo Vežėjui gali būti skirtos baudos, todėl sutinka, kad už jo siuntoje rastus draudžiamus transportuoti daiktus įvardintus 4.2. punkte, Siuntėjui būtų pritaikytos toliau nurodytos baudos, kurių dydis yra pagrįstas, atsižvelgus į atitinkamų valstybės institucijų (kur yra gabenamas krovinys) galimų paskirti baudų dydžius. Radus siuntoje ar krovinyje alkoholinių gėrimų, taikoma 1200 EUR bauda už kiekvieną alkoholinio gėrimo vienetą; Radus siuntoje ar krovinyje vaistų, taikoma po 1200 EUR bauda už kiekvieną siuntoje rastą vienetą ( ampolę, tabletę ) ir kita... Siuntoje radus cigarecių, taikoma po 1200 EUR bauda už kiekvieną siuntoje rastą bloką cigarecių (200vnt.), ta pati bauda taikoma ir už mažesnį kiekį; • Radus tabako ar jo gaminių, taikoma po 1200EUR bauda už kiekvienus rastus 200g, ta pati bauda taikoma ir už mažesnį kiekį; • Radus kitų, dar nepaminėtų draudžiamų daiktų iš 4.2. punkto taikoma 1200 EUR bauda.

#### 5. Pretenzijų reiškimas

5.1. Klientai privalo pranešti Vežėjui apie patirtus nuostolius ar žalą per 5 dienas, nuo siuntos gavimo dienos ir patvirtinti tai raštu per 14 dienų nuo siuntos gavimo dienos. Jeigu klientas neįvykdo pretenzijos pareiškimo pagal numatytą tvarką, Vežėjas neatsako už jokius nuostolius ar žalą išskyrus tuos atvejus, kai klientas patvirtina, kad pagrįstai nebuvo įmanoma perspėti Vežėjo arba pateikti pretenziją raštu per numatytą laikotarpį.

#### 6. Atvejai, kuriais įmonė neprisiima atsakomybės

6.1. Vežėjas neatsako už netiesioginius nuostolius, tokius kaip: pelno praradimas, neturtinės žalos padarymas, reputacijos pažeidimas, tiek kiek tai apibrėdžia taikytini teisės aktai. Vežėjas neatsako ir neišmoka jokios kompensacijos, jeigu yra patiriami nuostoliai dėl to, kad siunta ar krovinys prarandami ar pristatomi pavėluotai, dėl nuo Vežėjo nepriklausančių aplinkybių, tokių kaip: 1) teisėti ar neteisėti valstybės įstaigų ar institucijų veiksmai arba neveikimas, dėl jų susidariusios transporto spūstys, ar bet kokios kitokios kliūtys siuntų ar krovinių pervežimui; 2) baikotai, streikai, lokautai, nespartus darbas kaip streiko forma, gamybinių ar administracinių pastatų užėmimas bei darbo sustabdymas; 3) stichinės nelaimės, tokios kaip: smarkios audros, pūgos, ciklonai, gausiai iškritęs sniegas, žemės drebėjimai, potvyniai; 4) sprogimai, gaisrai, gamybinių pastatų ar vidaus komunikacijų sunaikinimas; 5) karas, pilietinis karas, maišrai, revoliucijos, piratavimas, sabotažas; 6) Muitinės ar kitų valstybės institucijų procedūros; 7) Siuntėjo ar gavėjo veiksmai (neveikimas); 8) Kitos Lietuvos respublikos teisės aktuose ir tarptautinėse sutartyse numatytos aplinkybės, Vežėją atleidžia nuo bet kokos atsakomybės.

6.2. Pasirašydami šią sutartį Siuntėjas ir Vežėjas sutaria, kad Vežėjo patvirtintos siuntų pervežimo taisyklės ir kainos, kurios yra viešai skelbiamos Vežėjo internetinėje svetainėje http://sgppervezimai.lt, yra sudėtinė ir neatskiriama šios sutarties dalis, tiek kiek jos neprieštarauja šios sutarties nuostatoms.

### Atsisiunčiamas failas

- [sgp_sutartis-su-siunteju.pdf](https://www.sgp-pervezimai.lt/siuntu-siuntimo-taisykles/download/sgp-sutartis-su-siunteju-pdf-3) — `application/pdf`, 73 599 B (~72 KB), `Content-Disposition: attachment` (ikona `fa-cloud-download`). PDF turinys neatsisiųstas ir neišanalizuotas.

### Blokas po turiniu

Modulis „Artimiausi pervežimai“ (tas pats kaip pradžios / grafiko puslapyje):

| Maršrutas | Datos |
|---|---|
| Lietuva - Airija | Spalio - 09d. ; 23d. |
| Lietuva - Ispanija | Spalio - 09d. ; 23d. |
| Airija - Lietuva | Rugsėjo - 28d. / Spalio - 15d.; 28d. |
| Ispanija - Lietuva | Rugsėjo - 27d. / Spalio - 14d.; 28d. |

---

## Kontaktai | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/kontaktai

- **Title:** Kontaktai | sgp-pervezimai.lt
- **Meta description:** SGP Pervezimai paslaugos keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, pervezimai i Airija Prancuzija Ispanija (numatytoji)
- **Meta keywords:** Keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, paslaugos, pervezimai, Airija, Prancuzija, Ispanija
- **Puslapio antraštė (juosta, H1):** Kontaktai — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- Kelio (breadcrumbs) juostos šiame puslapyje nėra.

### Turinys (sekcija `main-top`)

**[H2]** Kontaktai

**[H6]** Susisiekite su mumis ir mes pasiūlysime Jums geriausią kainą!

**[H6]** El. paštas: [saugiai.greitai.patikimai@gmail.com](mailto:saugiai.greitai.patikimai@gmail.com)

*(iššifruota iš Joomla cloak skripto)*

**[H5]** PERVEŽIMAI Į AIRIJĄ

| Telefonas | Nuoroda | Šalies kodas |
|---|---|---|
| +370 650 53161 | tel:+37065053161 | Lietuva |
| +353 864 503104 | tel:+353864503104 | Airija |
| +447566878681 | tel:+447566878681 | Jungtinė Karalystė |

**[H5]** PERVEŽIMAI Į ISPANIJĄ

| Telefonas | Nuoroda | Šalies kodas |
|---|---|---|
| +370 638 28919 | tel:+37063828919 | Lietuva |
| +34 60 25 47929 | tel:+34602547929 | Ispanija |

(Kiekvienas numeris originale rašomas kaip „Tel.: <numeris>“.)

### Kontaktų forma (`#contact-form_217`)

Formoje pateikti duomenys naudojami susisiekimui su klientu

| Laukas (placeholder) | Tipas | Privalomas | Paaiškinimas (title) |
|---|---|---|---|
| Jūsų vardas | text | taip | Jūsų vardas |
| El. pašto adresas | email | taip | El. pašto adresas naudojamas išsiųti pasiūlymui parengtams pagal kliento poreikius. Saugomas mūsų sistemoje iki vartotojo pareikalavimo panaikinti duomenis. |
| Žinutės tema | text | taip | Žinutės tema |
| Žinutė | textarea | taip (min. 20 simbolių) | Žinutė |
| Google reCAPTCHA v2 | — | taip | — |

Mygtukas: **Siųsti**

Pranešimai: „Jūsų žinutė sėkmingai išsiųsta“ / „Oi kažkas ne taip! Bandykite dar kartą.“ / „Įveskite teisingą apsaugos kodą.“

### Ko kontaktų puslapyje NĖRA

- fizinio adreso / biuro ar sandėlio vietos;
- žemėlapio (Google Maps ar kito);
- įmonės rekvizitų (juridinis pavadinimas, įmonės kodas, PVM kodas);
- darbo laiko;
- Messenger / Viber / WhatsApp nuorodų;
- socialinių tinklų nuorodų.

Poraštėje šiame puslapyje nėra „Susisiekite su mumis“ bloko (jis perkeltas į turinį) — rodoma tik tamsi poraštė su paslaugų meniu ir copyright.

---

## Privatumo politika | sgp-pervezimai.lt — https://www.sgp-pervezimai.lt/privatumo-politika/policies

- **Title:** Privatumo politika | sgp-pervezimai.lt
- **Meta description:** SGP Pervezimai paslaugos keleiviai, siuntiniai, automobiliai, perkraustymai, gyvunai, pervezimai i Airija Prancuzija Ispanija (numatytoji)
- **Puslapio antraštė (juosta, H1):** Privatumo politika — fonas https://www.sgp-pervezimai.lt/images/highway-3010146_1920.jpg
- **Kelias:** Pradžia › Privatumo politika
- Šiame puslapyje nėra „Susisiekite su mumis“ bloko poraštėje.

### Informacija *(H3)*

Informacija ruošiama...

### Slapukai (Cookies) *(H3)*

**[H5]** Techniniai svetainės slapukai - reikalingi normaliam svetainės veikimui

| Slapuko pavadinimas | Šaltinis | Aprašymas | Sukūrimo momentas | Galiojimo laikas |
|---|---|---|---|---|
| cookie_agree | sgppervezimai.lt | Slapukas skirtas privatumo (slapukų) politikos pranešimui / sutikimui realizuoti. | Sutinkant su nuostatomis | 5 dienos |
| Atsitiktinių skaičių ir raidžių seka sugeneruotas unikalus raktas | sgppervezimai.lt | Naudojamas saugoti naršymo sesijos raktą. | Įėjimo į puslapį metu | Iki interneto svetainės lango uždarymo |
| APISID, CONSENT, HSID, NID, S, SAPISID, SID, SIDCC, SSID | google.com | Slapukai naudojami Google Recaptcha testo | Įėjimo į puslapį metu | Iki interneto svetainės lango uždarymo |
| jpanesliders_sef-info-pane | sgppervezimai.lt | Slapukai naudojami prisiminti naršyklės nustatymus | Įėjimo į puslapį metu | Iki interneto svetainės lango uždarymo |
| joomsef_lang | sgppervezimai.lt | Slapukai naudojami prisiminti svetainės kalbą | Įėjimo į puslapį metu | Iki interneto svetainės lango uždarymo |

Norėdami pasitikrinti, kokius duomenis susijusius su Jūsų el. paštu esame sukaupę ir naudojame rinkodaros tikslais - [spauskite čia.](https://www.sgp-pervezimai.lt/surinktu-ir-rinkodaros-tikslais-naudojamu-duomenu-ataskaita/request)

---

### Pastabos

**Spragos (turinys, kurio nepavyko gauti arba jo nėra):**

- **Įmonės rekvizitai:** juridinis pavadinimas (UAB/MB/IĮ), įmonės kodas, PVM kodas, registracijos adresas — nėra nė viename puslapyje. Svetainėje naudojamas tik prekės ženklas „SGP“ / „SGP pervežimai“ / „sgppervezimai.lt“.
- **Adresas, žemėlapis, darbo laikas** — nėra.
- **Messenger / Viber / WhatsApp / socialiniai tinklai** — nėra jokių nuorodų (el. paštas — tik Gmail adresas).
- **Kainos** — nenurodytos niekur (tik frazės „geriausią kainą“, „patrauklios kainos“). Vieninteliai skaičiai eurais — baudos taisyklių 4.5 p. (1200 EUR).
- **Pervežimų grafikas** — tik artimiausios datos (be metų, be išvykimo laikų, vietų ar maršruto stotelių). Senesnių/ateities mėnesių grafiko nėra.
- **Siuntos sekimas** — sėkmingo paieškos rezultato vaizdas nepatikrintas (neturime tikro siuntos kodo).
- **PDF „sgp_sutartis-su-siunteju.pdf“** — nuoroda ir metaduomenys užfiksuoti, bet failas neatsisiųstas (failų atsisiuntimui reikalingas atskiras vartotojo leidimas); jo turinys greičiausiai atitinka „Taisyklės“ puslapio tekstą (sutartis su siuntėju).
- **Privatumo politika** — faktiškai neparengta: skyrius „Informacija“ turi tik „Informacija ruošiama...“; yra tik slapukų lentelė.
- **Paslaugų subpuslapiai** (11 vnt. po `/pervezimo-paslaugos/tarptautiniai-pervezimai/…`) šiame dokumente neaprašyti — jie ne šios užduoties apimtyje.

**Pastebėjimai / pasenusi ar nenuosekli informacija:**

- **Pristatymo trukmė prieštaringa:** „apie 3–4 paras“ (Pervežimo paslaugos, Tarptautiniai pervežimai) vs. „per 5 darbo dienas nuo pirmos išvykimo iš Lietuvos dienos“ (Taisyklės 3.4) vs. „Kelionė trunka nuo 2 iki 3 parų“ ir „Siuntos išdalinamos per 3 dienas nuo atvykimo į šalį“ (tik Taisyklių meta aprašyme — senas tekstas).
- **Šalių sąrašas nenuoseklus:** pradžia/apie — „Lietuva – Ispanija – Lietuva, Lietuva – Airija – Lietuva ir kitas Europos šalis (Vokietiją, Prancūziją)“; paslaugos — „į / iš Airiją, Ispaniją, Vokietiją, Prancūziją“; tarptautiniai — maršrutai apima „Lenkija, Vokietija, Belgija, Prancūzija“. Meta raktažodžiuose minima Prancūzija, bet ne Vokietija.
- **Domeno neatitikimas:** Taisyklių 6.2 p. nurodo „http://sgppervezimai.lt“, copyright — „sgppervezimai.lt“, o tikrasis domenas — sgp-pervezimai.lt.
- **Pasenęs turinys:** mikroautobusų privalumuose minimas „DVD – kad kelionė neprailgtų“. Naudojamas Google Analytics `UA-115748704-1` (Universal Analytics, nebeveikia nuo 2023 m.).
- **Testiniai/sugadinti SEO duomenys:** Siuntos sekimo puslapio meta description = „<b>test</b>“; Pervežimo paslaugų OG image — serverio kelias (404); daugelio puslapių meta aprašymai be lietuviškų raidžių ir vienodi (numatytieji); keywords sugeneruoti automatiškai („lietuva, bei, kvalifikuota, tik…“).
- **H1 problema:** kiekviename puslapyje H1 = „Pervežimas“ (logotipe); puslapių pavadinimai kai kur H1, kai kur H2 („Apie mus“, „Siuntų siuntimo taisyklės“, siuntos sekime juostoje net „Pervežimo paslaugos“). Meniu punktas „Apie mus“, puslapio title „Apie įmonę“.
- **Dublis:** Siuntos sekimas pasiekiamas dviem URL (`/siuntos-sekimas` ir `/pervezimo-paslaugos/siuntos-sekimas`).
- **Pervežimų grafikas** nėra pagrindiniame meniu; jo puslapio pagrindinis turinys tuščias (tik modulis).
- **Apie įmonę** puslapio bloke „Pervežimo paslaugos“ — tik viena plytelė; pradžios „hero“ slankiklyje — tik viena skaidrė.
- **Airijos kontaktuose** yra JK numeris (+44 7566 878681) — tikėtina, kad kelionė į Airiją eina per JK arba vairuotojas turi JK SIM.
- **Telefono formatai nevienodi:** „+447566878681“ be tarpų, „+34 60 25 47929“ netaisyklingai sugrupuotas.
- **Rašybos klaidos originale** (palikta pažodžiui): „sako žmogiškųjų“, „užtiktiname“, „sklandžia kelionę“, „Siuntėjau nedalyvaujant“, „dėlto“, „šaunamiejii“, „cigarecių“, „baikotai“, „maišrai“, „kokos“, „išsiųti pasiūlymui parengtams“, „grąžinamą“, „į Ispanija ir atgal“, „visus daiktai“.
- **Siuntų sistemos tiekėjas:** siuntos.sgp-pervezimai.lt — Laravel sistema, meta author „UAB GP Soft“ (galimai valdymo sistemos kūrėjas).
- **Laiko kontekstas:** copyright „© 2026“, grafiko datos (rugsėjo 27–28, spalio 9–28) atitinka nuskaitymo datą 2026-09-23 — grafikas atnaujinamas rankiniu būdu ir šiuo metu aktualus.
