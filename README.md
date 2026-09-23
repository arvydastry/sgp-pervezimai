# SGP pervežimai — v2 demo („Maršruto linija“)

Demonstracinė naujos **sgp-pervezimai.lt** svetainės versija (Lietuva – Airija – Lietuva, Lietuva – Ispanija – Lietuva). Galutinė svetainė bus perkurta **WordPress + Salient 18.3** tema, todėl demo rodo tik tai, ką galima atkurti Salient elementais ir nedideliu kiekiu papildomo CSS / JS.

- Gyva demo versija: <https://arvydastry.github.io/sgp-pervezimai/>
- Ankstesnė demo versija: [`v1/`](v1/index.html) (nekeičiama)
- Dizaino sistema (vienintelis dizaino šaltinis): [`docs/dizaino-sistema.md`](docs/dizaino-sistema.md)
- Turinio pataisos ir naujas tekstas klientui patvirtinti: [`docs/turinio-pataisos.md`](docs/turinio-pataisos.md)

Demo — statinis HTML / CSS / vanilla JS. Formos niekur nesiunčia duomenų (rodomas sėkmės pranešimas), siuntos sekimas veikia tik demonstraciniu režimu (kodas `SGP-DEMO`), tikrasis sekimo įrankis nekviečiamas. Visi puslapiai turi `noindex, nofollow`.

## Puslapiai

| Puslapis | Failas |
|---|---|
| Pradžia | [`index.html`](index.html) |
| Apie įmonę | [`apie-imone/`](apie-imone/index.html) |
| Pervežimo paslaugos | [`pervezimo-paslaugos/`](pervezimo-paslaugos/index.html) |
| Tarptautiniai pervežimai | [`pervezimo-paslaugos/tarptautiniai-pervezimai/`](pervezimo-paslaugos/tarptautiniai-pervezimai/index.html) |
| 01 Krovinių pervežimas | [`…/kroviniu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/kroviniu-pervezimas/index.html) |
| 02 Negabaritinių krovinių pervežimas | [`…/negabaritiniu-kroviniu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/negabaritiniu-kroviniu-pervezimas/index.html) |
| 03 Dalinių krovinių gabenimas | [`…/daliniu-kroviniu-gabenimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/daliniu-kroviniu-gabenimas/index.html) |
| 04 Daiktų pervežimas | [`…/daiktu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/daiktu-pervezimas/index.html) |
| 05 Automobilių pervežimas | [`…/automobiliu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/automobiliu-pervezimas/index.html) |
| 06 Motociklų pervežimas | [`…/motociklu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/motociklu-pervezimas/index.html) |
| 07 Keleivių pervežimas | [`…/keleiviu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/keleiviu-pervezimas/index.html) |
| 08 Gyvūnų pervežimas | [`…/gyvunu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/gyvunu-pervezimas/index.html) |
| 09 Siuntų pervežimas | [`…/siuntu-pervezimas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/siuntu-pervezimas/index.html) |
| 10 Siuntų pristatymas | [`…/siuntu-pristatymas/`](pervezimo-paslaugos/tarptautiniai-pervezimai/siuntu-pristatymas/index.html) |
| 11 Perkraustymo paslaugos | [`…/perkraustymo-paslaugos/`](pervezimo-paslaugos/tarptautiniai-pervezimai/perkraustymo-paslaugos/index.html) |
| Pervežimų grafikas | [`pervezimu-grafikas/`](pervezimu-grafikas/index.html) |
| Siuntos sekimas | [`siuntos-sekimas/`](siuntos-sekimas/index.html) |
| Taisyklės | [`taisykles/`](taisykles/index.html) |
| Kontaktai | [`kontaktai/`](kontaktai/index.html) |
| Privatumo politika | [`privatumo-politika/`](privatumo-politika/index.html) |
| 404 „Maršrutas nerastas“ | [`404.html`](404.html) |

Naudingi demo parametrai: `?siandien=2026-10-15` (grafikas perskaičiuojamas kitai dienai; `?siandien=2026-11-30` — tuščias grafikas), `/siuntos-sekimas/?kodas=SGP-DEMO` (pavyzdinis rezultatas), `…/pervezimu-grafikas/#ispanija` (atidaromas skirtukas).

## Kaip sugeneruoti

Reikia tik `python3` (standartinė biblioteka, be npm ir be priklausomybių).

```bash
python3 tools/build.py              # sugeneruoja visus 21 puslapį (index.html, 404.html, */index.html)
python3 tools/build.py apie-imone   # tik puslapiai, kurių kelias prasideda „apie-imone“
python3 tools/check.py              # patikra: nuorodos, id, alt, 5 tel: numeriai, lang, H1, title/description, {{ }} likučiai
python3 -m http.server 8765         # peržiūra: http://127.0.0.1:8765/
for f in assets/js/sgp.js assets/js/pages/*.js; do node --check "$f"; done   # JS sintaksė (nebūtina)
```

Generavimas deterministinis: „šiandiena“ grafikui imama iš `src/data/grafikas.json` → `render_today`, failai perrašomi tik pasikeitus turiniui. Naršyklėje `sgp.js` grafiką perskaičiuoja pagal lankytojo datą (Europe/Vilnius). **Sugeneruotų `*.html` failų ranka neredaguokite** — keiskite `src/` ir paleiskite `tools/build.py`.

`404.html` naudoja absoliučias nuorodas `/sgp-pervezimai/…` (GitHub Pages jį rodo bet kuriame gylyje); lokaliai jį peržiūrėti galima tik aptarnaujant repozitoriją po `/sgp-pervezimai/` keliu. `.nojekyll` išjungia GitHub Pages Jekyll apdorojimą (šaltiniai `src/` turi `{{ }}` žymas).

## Struktūra

```
index.html, 404.html, */index.html   sugeneruoti puslapiai (GitHub Pages rodo repozitorijos šaknį)
src/pages/*.html                     puslapių šaltiniai: front matter (title, description, out, nav, css, js …) + turinys
src/templates/paslauga.html (+ .py)  vienas šablonas → 11 paslaugų puslapių
src/partials/*.html                  bendri blokai: head, header (bėgantis grafikas, meniu, telefonai), footer,
                                     skambučių juosta, GS-Arrival užklausa, GS-Board lenta, žemėlapiai
src/data/grafikas.json               pervežimų grafikas: 4 kryptys × datos (ISO), telefonai
src/data/paslaugos.json              11 paslaugų + 6 grupės (tekstai, nuotraukos, duomenų lapai)
assets/css/tokens.css, base.css, components.css, motion.css   bendri stiliai (dizaino žetonai, komponentai, judesys)
assets/css/pages/*.css               puslapių stiliai (priešdėliai ab-, ps-, tp-, sv-, gr-, sk-, tr-, kt-, pp-, e4-, h-)
assets/js/sgp.js                     bendras JS (Lenis, antraštė, meniu, atsiradimo efektai, bėgėjas, grafikas,
                                     skirtukai, akordeonai, formos, „Salient žymės“) — window.SGP
assets/js/pages/*.js                 puslapių JS
tools/build.py, tools/check.py       generatorius ir patikra
docs/                                dizaino sistema, turinys, media sąrašas, komandų pastabos (build-notes/)
v1/                                  ankstesnė demo versija
```

Leidžiamos išorinės bibliotekos: Lenis 1.1.13, Flickity 2.3.0 (galerija „Apie įmonę“), Google Fonts (Barlow, Barlow Condensed, IBM Plex Mono). Visi efektai paiso `prefers-reduced-motion`.

## Kaip tai atitinka Salient

- **Dizaino sistema** [`docs/dizaino-sistema.md`](docs/dizaino-sistema.md): žetonai (§2, įklijuojami į Theme Options → Custom CSS), grafiniai elementai (§3), komponentai su būsenomis (§4), judesys ir kiekvieno efekto Salient atitikmuo (§5), kiekvieno puslapio planas (§6), prieinamumas ir našumas (§7). Salient elementų pavadinimai — [`docs/salient-elementai.md`](docs/salient-elementai.md).
- **„Salient žymės“** — mygtukas apatiniame kairiajame kampe (ekranuose nuo 700 px pločio). Įjungus prie kiekvienos eilutės ir bloko rodomas jo Salient elementas ir nustatymai (iš `data-salient` atributų), pvz. „Row Full Width · Parallax BG: Subtle“, „Global Section GS-Board“, „Sticky Scroll Pinned Sections → Stacking“.
- Bendros klasės `sgp-*` — tie patys pavadinimai, kuriuos WordPress kūrėjas perkels į Salient Extra Class / Custom CSS.
- Grafikas — būsimo `[sgp_grafikas]` trumpojo kodo veidrodis: `{{grafikas:board|timetable|table|ticker|stub|next|lane}}` (dizaino sistema §6.0, A priedas); duomenys — ACF parinkčių puslapis.
- Pasikartojantys blokai = Salient Global Sections: GS-Ticker, GS-Menu, GS-Board, GS-Arrival, GS-Footer, GS-CallBar, GS-Trust, GS-ServiceList.
- Techninės kūrimo taisyklės ir integracijos pakeitimai — [`docs/build-notes/foundation.md`](docs/build-notes/foundation.md) (§11 — integracijos suvestinė).

## Nuotraukos ir vaizdo įrašai

Visos nuotraukos ir vaizdo įrašai — iš [Pexels](https://www.pexels.com/) (Pexels licencija, nemokama naudoti; autorių nurodymas nebūtinas, bet pateikiamas). Naudojami tik [`docs/media.json`](docs/media.json) patikrinti failai, kraunami tiesiai iš Pexels CDN (`?auto=compress&cs=tinysrgb&w=…`). Tai iliustracijos demo versijai — prieš paleidimą jas verta pakeisti tikromis įmonės nuotraukomis.

Autoriai (naudojami demo puslapiuose):

- **Adrianna CA** — [22033738](https://www.pexels.com/photo/22033738/)
- **Alejandro De Roa** — [27868340](https://www.pexels.com/photo/27868340/)
- **Alex Kalinin** — [32821932](https://www.pexels.com/photo/32821932/)
- **Altaf Shah** — [34371915](https://www.pexels.com/video/34371915/) (video)
- **Andreas Schnabl** — [3868901](https://www.pexels.com/photo/3868901/)
- **ArtHouse Studio** — [4858429](https://www.pexels.com/photo/4858429/)
- **Batuhan Küçükdemir** — [21767483](https://www.pexels.com/photo/21767483/)
- **Caleb Oquendo** — [34585120](https://www.pexels.com/photo/34585120/)
- **cottonbro studio** — [7541981](https://www.pexels.com/photo/7541981/)
- **Craig Adderley** — [2449454](https://www.pexels.com/photo/2449454/)
- **David Brown** — [17720190](https://www.pexels.com/photo/17720190/)
- **David Geib** — [3220828](https://www.pexels.com/photo/3220828/)
- **Dextar Studio** — [12418936](https://www.pexels.com/photo/12418936/)
- **Engin Akyurt** — [4040619](https://www.pexels.com/photo/4040619/)
- **Enric Cruz López** — [9989463](https://www.pexels.com/photo/9989463/)
- **Gerbiamas Ponas Stonys** — [1696742](https://www.pexels.com/photo/1696742/)
- **Grigoriy Bunkov** — [19552565](https://www.pexels.com/video/19552565/) (video)
- **Gustavo Fring** — [6720534](https://www.pexels.com/photo/6720534/)
- **Ian Findley** — [31570314](https://www.pexels.com/photo/31570314/)
- **Irek Marcinkowski** — [35497082](https://www.pexels.com/photo/35497082/)
- **Jan Kopřiva** — [7024783](https://www.pexels.com/photo/7024783/)
- **Jonas Von Werne** — [1225126](https://www.pexels.com/photo/1225126/)
- **Jonathan Borba** — [36933446](https://www.pexels.com/photo/36933446/)
- **Juan R. Real** — [29786116](https://www.pexels.com/photo/29786116/)
- **K** — [2386447](https://www.pexels.com/video/2386447/) (video), [2881400](https://www.pexels.com/photo/2881400/), [4685871](https://www.pexels.com/video/4685871/) (video)
- **Kate Kerr** — [13568682](https://www.pexels.com/photo/13568682/)
- **Ketut Subiyanto** — [4246238](https://www.pexels.com/photo/4246238/)
- **Krzysztof Jaworski Fotografia Toruń** — [38927007](https://www.pexels.com/photo/38927007/)
- **Lee Salem** — [36377055](https://www.pexels.com/photo/36377055/)
- **Leo Lu** — [36383706](https://www.pexels.com/photo/36383706/)
- **Lia L.** — [34497909](https://www.pexels.com/photo/34497909/)
- **Luke Miller** — [29566910](https://www.pexels.com/photo/29566910/)
- **Malte Luk** — [1606957](https://www.pexels.com/photo/1606957/)
- **Maurice Renois** — [5713164](https://www.pexels.com/photo/5713164/)
- **Michael Solo** — [35332902](https://www.pexels.com/photo/35332902/)
- **Mizuno K** — [13456097](https://www.pexels.com/photo/13456097/)
- **Oliver Wagenblatt** — [32872983](https://www.pexels.com/photo/32872983/)
- **Pavel Danilyuk** — [6407553](https://www.pexels.com/photo/6407553/)
- **Piotr Wojnowski** — [29374299](https://www.pexels.com/video/29374299/) (video)
- **Pixabay** — [160483](https://www.pexels.com/photo/160483/)
- **Plato Terentev** — [9807331](https://www.pexels.com/photo/9807331/)
- **Polina Tankilevitch** — [4440774](https://www.pexels.com/photo/4440774/)
- **Prestige by Nature** — [21041157](https://www.pexels.com/photo/21041157/)
- **Quang Nguyen Vinh** — [2177200](https://www.pexels.com/photo/2177200/)
- **Rafael Fernanz** — [13707149](https://www.pexels.com/video/13707149/) (video)
- **RDNE Stock project** — [7464731](https://www.pexels.com/photo/7464731/)
- **Sergei Skrynnik** — [11053641](https://www.pexels.com/photo/11053641/)
- **Stepan Vrany** — [27383867](https://www.pexels.com/photo/27383867/)
- **Tayssir Kadamany** — [38095094](https://www.pexels.com/photo/38095094/)
- **Tiger Lily** — [4487517](https://www.pexels.com/photo/4487517/)
- **Tima Miroshnichenko** — [6169133](https://www.pexels.com/photo/6169133/), [6170458](https://www.pexels.com/photo/6170458/)
- **Timur Weber** — [9185835](https://www.pexels.com/photo/9185835/)
- **Tom Jurman** — [34308329](https://www.pexels.com/video/34308329/) (video)
- **Yusuf Çelik** — [17455631](https://www.pexels.com/photo/17455631/)
- **Алексей Гвоздев** — [8858566](https://www.pexels.com/photo/8858566/)
