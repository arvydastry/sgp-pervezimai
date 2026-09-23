# SGP v2: medijos pasirinkimas (Pexels)

Visi failai yra iš Pexels (licencija leidžia nemokamai naudoti komerciškai, autorių nurodyti nebūtina). Išsami informacija pateikta faile `media.json`: 62 nuotraukos ir 13 video. Kiekvienas URL patikrintas su `curl -sIL` ir grąžino HTTP 200 su teisingu `image/*` arba `video/*` tipu. Nuotraukų URL sudaromas taip: `url_base + ?auto=compress&cs=tinysrgb&w=<plotis>`. Ankstesnio demo ID (12261472, 5025635, 34539243, 33384858, 39572426, 5025663, 12615250, 34369733, 7183495) nenaudojami. Taip pat vengta tos pačios Artem Podrez kurjerių serijos (5025xxx), kad nauja versija nebūtų panaši į senąją.

## Video

| Kategorija | ID (pirmas – geriausias) | HD dydis | Kodėl |
|---|---|---|---|
| Hero | **12421166**, 29374299, 4685871, 13707149, 3847797, 15602514 | 1.5–6.2 MB | Kinematografiški kadrai iš drono prieblandoje: vilkikas vingiuotame kelyje, Europos greitkelių mazgas, miško greitkelis, sunkvežimis rūke, JK automagistralės timelapse, baltas furgonas. Visi mažesni nei 7 MB. |
| Keltas | **19274366**, 3987777, 32313192 | 7–11 MB | Kelto vaga jūroje, vilkiko vairuotojo POV įvažiuojant į keltą (tinka pasakoti, kaip vyksta kelionė), keltas iš drono. |
| Negabaritiniai | **19552565** | 8.5 MB | Vėjo jėgainės mentė lietingame greitkelyje. |
| Motociklai | **34308329** | 4.2 MB | Motociklas užkeliamas ant priekabos. |
| Automobiliai | **34371915** | 7.1 MB | Autovežis kelyje. Vaizdas nespalvotas, todėl tinka su tamsiu overlay. |
| Airija | **2386447** | 11.2 MB | Airijos uolos ir Atlanto bangos iš drono. |

## Nuotraukos

| Kategorija | ID (pirmas – geriausias) | Kodėl |
|---|---|---|
| Hero | **11053641**, 36383706, 9989463 | Tamsus sunkvežimio kadras mėlynąją valandą, greitkelis sutemus, baltas furgonas kalnų kelyje. Tinka kaip poster arba fallback video. |
| Kroviniai | **38927007**, 17720190, 38404178 | Vilkikai Europos greitkelyje (Lenkija) saulėlydyje, apšviesti vilkikai naktį, juodas autoparkas. |
| Negabaritiniai | **35332902**, 38095094 | Negabaritinis krovinys lietuje (niūri nuotaika), technika ant žemos platformos. |
| Daliniai | **34585120**, 29786116, 12418936 | Padėklai kraunami į priekabą, tamsi sandėlio rampa, padėklai prieš šviesą. |
| Daiktai | **36933446**, 9185835, 160483 | Premium lagaminai su dirželiais, pakavimas, žmogus su lagaminu rūke. |
| Automobiliai | **29566910**, 1606957, 35531295 | Automobilis kraunamas ant autovežio, autovežis saulėlydyje, automobiliai kelto denyje. |
| Motociklai | **4858429**, 2177200, 5713164 | Motociklo iškrovimas saulėlydyje, motociklininkas rūke, motociklas prie furgono. |
| Keleiviai | **36377055**, 27383867, 17455631 | Juodas odinis mikroautobuso salonas, baltas mikroautobusas prie kelio, šviesus salonas. |
| Gyvūnai | **32872983**, 3868901, 21767483 | Šuo furgono sėdynėje, šuo su šeimininku furgone, katė narvelyje. |
| Siuntų pristatymas | **13456097**, 4440774 | Kurjeris prie durų, rankos perduoda dėžes. |
| Siuntų pervežimas | **6170458**, 4487517, 6407553 | Tvarkingos dėžės furgone, tamsus kadras su kurjeriu, atviras furgonas. |
| Perkraustymas | **7464393**, 4246238, 7464731 | Krovikai neša sofą, supakuotos dėžės, atsargus elgesys su dėže. |
| Maršrutai: Airija | **2881400**, 3220828, 13568682, 15885602 | Dublinas naktį, Airijos pakrantės kelias, Moherio uolos, keltas Dublino įlankoje. |
| Maršrutai: JK / Šiaurės Airija | **35497082** | Šviesų pėdsakai Craigavon mieste. |
| Maršrutai: Ispanija | **27868340**, 34497909, 22033738 | Madrido greitkelis prieblandoje, Barselona, Malaga. |
| Maršrutai: Europa | **32821932** | Sunkvežimis Viduržemio jūros pakrantės kelyje (Rivjera). |
| Maršrutai: Lietuva | **11479826**, 7828591, 1696742, 18035726 | Vilniaus senamiestis žiemos vakarą, Gedimino pilis, kelias per pušyną, žiemos kelias. |
| Žemėlapis | **8874803**, 8828587 | Europos žemėlapis su smeigtukais Airijoje ir JK. |
| Apie mus / komanda | **7541981**, 6720534, 21041157, 2449454, 8858566, 31570314, 6169133 | Vairuotojas naktį, kontrolinis sąrašas, rankų paspaudimas prie priekabų, rampa, rūkas kieme, krovinio tvirtinimas grandinėmis, važtaraščiai. |
| Tekstūros (parallax) | **9807331**, 4040619, 5919143, 7024783, 1225126, 7019611 | Šlapias asfaltas, asfalto makro, galinių žibintų bokeh, šviesų pėdsakai Vokietijoje, protektorius. |

## Ko trūksta

- Nėra tinkamos spalvotos autovežio nuotraukos Europos greitkelyje judant. Yra tik nespalvotas video 34371915 ir stovinčio autovežio kadrai.
- Neradome **krovinio diržo su terkšle stambiu planu**. Vietoj jo siūlome 31570314 (tvirtinimas grandinėmis).
- Neradome Ispanijos greitkelio su sunkvežimiu. Vietoj jo naudojama 32821932 (Prancūzijos Rivjera) ir Madrido greitkelis 27868340.
- Nerasta Korko, Galway, Valensijos ir Alikantės nuotraukų, kurios tiktų tamsiam dizainui. Esamos yra ryškios dieninės, jas galima pridėti vėliau.
- Nerasta be logotipų, važiuojančio keleivinio mikroautobuso nuotraukos ar video.
