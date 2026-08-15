# Analyse des dessins amont contenant du texte allemand

Inventaire de premier passage, préparatoire à la fiche d'arbitrage annoncée
dans `CLAUDE.md` §9 (« chantier de francisation des dessins »). **Ce document
ne tranche rien** : il recense, il ne décide pas. Les décisions
(traduire / laisser en allemand / reformuler) reviennent à Pierre, dessin par
dessin ou par lot.

## 1. Nature du problème

Les dessins amont (`contents/drawings/<id>.tex`) sont du **TikZ/pgfplots en
source LaTeX**, pas des images matricielles. Le texte allemand qu'on y voit
(légendes d'axes, libellés de nœuds, texte de schéma) est donc du texte
LaTeX ordinaire — traduisible comme une section, sans OCR ni retouche
d'image. Les photos amont (`contents/photos/`), en revanche, sont de vraies
images ; ce document ne les couvre pas (aucun indice à ce jour qu'elles
portent du texte allemand incrusté).

**Aucun mécanisme de substitution n'existe aujourd'hui.** `build_book.py`
copie toujours la version amont d'un dessin (`for f in
(contents/"contents/drawings").glob("*.tex")`, ligne ~1270) ; contrairement
aux sections, rien ne permet de faire primer une version française placée
dans `traductions/<CLASSE>/`. C'est pourquoi la politique en vigueur jusqu'ici
a été « non traduit, interne aux figures » (cf. `traductions/A/NOTES-SESSION.md`).

## 2. Méthode

1. **Périmètre** : uniquement les dessins réellement référencés par nos
   sections déjà traduites (`[picture:ID:...]` dans `traductions/{N,E,A}/sections/*.md`),
   pas les 885 dessins de l'amont complet.
   - N : 81 dessins uniques · E : 156 · A : 182 · **389 au total** (certains
     partagés entre éditions).
2. **Extraction** : script Python, capture du contenu de toute paire
   d'accolades « feuille » (`{...}` sans accolade imbriquée) dans chaque
   `.tex` de dessin — indépendamment de la macro qui la précède
   (`\node`, `xlabel=`, `\addlegendentry`, `label=`...), car la syntaxe TikZ
   varie trop pour cibler macro par macro de façon fiable.
3. **Filtrage du bruit** : élimination programmatique des identifiants de
   composants circuitikz (`battery`, `resistor`, `diode`…), noms de styles/
   couleurs TikZ (`DARCblue`, `dezimalbox`…), environnements pgfplots
   (`loglogaxis`, `polaraxis`…), coordonnées et expressions mathématiques.
   Un premier filtre automatique a laissé passer trop de bruit — corrigé
   après relecture manuelle du résultat intermédiaire.
4. **Classification** : chaque chaîne restante est marquée soit
   **cognat/transparent** (mot proche du français : *Antenne, Batterie,
   Transistor, Signal*...), soit **à examiner** (nécessite une vraie
   traduction). Les lignes en **gras** ci-dessous contiennent au moins une
   phrase de 3 mots ou plus (priorité de lecture la plus haute).

### Limites connues de ce premier passage

- Quelques fragments résiduels de mots coupés par une césure LaTeX
  (`athode` pour *Kathode*, `ochpass` probablement pour *Hochpass*,
  `verarbeitung` pour *Signalverarbeitung*) : le script a coupé le mot au
  mauvais endroit. À corriger à la main en cas de fork.
  - « Kathode » et « Hochpass » ont dû être adjoints manuellement lorsque le
    fragment ne suffisait pas à deviner le mot complet — c'est probablement
    aussi arrivé, silencieusement, pour d'autres mots que je n'ai pas
    identifiés. Une relecture visuelle du PDF reste nécessaire dessin par
    dessin avant tout fork.
- Texte composé en mode mathématique (`$\text{...}$`) volontairement exclu
  du balayage : hors du périmètre de l'extraction actuelle.
- Deux libellés déjà connus par relecture PDF (« FPGA oder Software »,
  « Mapper », chaîne SDR ch. 10-11 classe A) n'apparaissent pas dans le
  tableau — dessin probablement hors du périmètre `[picture:...]` détecté,
  ou syntaxe non couverte par l'extracteur. À vérifier séparément.
- Aucune vérification que la traduction proposée par le contexte (section
  française environnante) ne contredit pas le mot allemand du dessin.

## 3. Inventaire

**134 dessins sur 389 utilisés (34 %)** contiennent au moins un texte jugé
non trivial. 9 dessins portent au moins une phrase complète (gras).

| dessin | édition(s) | section(s) (extrait) | texte(s) allemand détecté(s) |
|---|---|---|---|
| 45 | A | oszillator_pll | Ausgang |
| 49 | E | kondensator_1 | Dielektrikum · Metallbeläge · Wickel |
| 85 | A | transverter_2 | Mischer |
| 149 | A | demodulator | Bar |
| 153 | A | demodulator | ZF-Amp. |
| 341 | A | daempfungsglieder | Dämpfungsglied |
| 342 | A | daempfungsglieder | Dämpfungsglied |
| 354 | A | verstaerker_begrenzung_bandbreite | Modulator |
| 357 | N | fm | Amplitude |
| 439 | E | aequivalente_isotrope_strahlungsleistung_eirp_2 | Antenne · Dämpfung · Gewinn |
| 475 | N | sprachsignale | Leistung |
| 489 | A | frequenzvervielfacher_2 | Bar |
| 497 | A | oszillator_schaltungen | Bar |
| 501 | A | remote_station | Kontrollsignale · Netzwerk · Steuer- und |
| 542 | N | digital_voice | Internet |
| 591 | E | unerwuenschte_aussendungen_2 | Leistung |
| 593 | E | unerwuenschte_aussendungen_2 | Leistung |
| 615 | N | endgespeiste_antennen | Anpass- |
| 630 | N | computersteuerung | Audio · Netzwerk |
| 654 | N | rufzeichenaufbau | Präfix · Suffix |
| 657 | N | antennen | Antenne · Kabel · Transceiver |
| 659 | N | rundstrahler | Radial · Strahler |
| 665 | N | widerstandsfarbcode | Multiplikator · Toleranz |
| 666 | E/N | gleichrichter_1; halbleiter | Anode · Kathode |
| 668 | N | remote_stationen | Internet · Remote |
| 669 | N | rundstrahler | Strahler |
| 670 | N | swr | Antenne · Reflektiert · SWR-Meter · Transceiver · Vorlaufend |
| 672 | N | split_betrieb | Antwort- Frequenz · begehrte Station |
| 673 | N | split_betrieb | Antwort- bereich · begehrte Station |
| 674 | A | kanalcodierung | Empfänger · Kanal · Sender |
| 675 | A | quellencodierung | Quellencodierer |
| 676 | A | kanalcodierung | Kanalcodierer |
| 680 | N | netzgeraet_1 | **Hohe Spannung · Kurzschluss- und Verpolungsgefahr · Netzgerät · Sicherung** |
| 681 | N | gefahren | Lebensgefahr |
| 694 | N | bauelemente | **Antenne · Batterie · Kondensator · Masse und Erde · Schalter · Spannungs- messgerät · Spule · Strom- messgerät · Widerstand** |
| 699 | E | paketvermittelte_netzwerke | Hostanteil · Netzanteil · Netzmaske |
| 726 | N | amplitude_periode | Amplitude |
| 727 | N | amplitude_periode | Negative Halbwelle · Positive Halbwelle |
| 728 | N | amplitude_periode | Periode |
| 729 | E/N | ionosphaere; ionosphaere_2 | **Jahre · Sonnenflecken im Mittel pro Monat** |
| 730 | N | sprachsignale | Hohe Töne · Laut · Lautstärke · Leise · Tiefe Töne |
| 731 | N | wellenausbreitung | D-Region · E-Region · Erde · Ionosphäre · Sporadic-E · Troposphäre |
| 732 | N | ionosphaere | Empfänger · Sender |
| 733 | A/E/N | ionosphaere_2; sporadic_e_1; sporadic_e_3 | Empfänger · Erde · Sender · Sporadic-E · VHF-Signale |
| 734 | N | troposphaere | **Kalte Luft · Sehr kalte Luft · Warme Luft** |
| 737 | A/N | squelch; squelch_2 | Rauschen · Schwaches Signal · Squelch · Starkes Signal |
| 740 | N | netzgeraet_1 | Ausgang · Spannungseinstellung · Überlast |
| 741 | E/N | ionosphaere; tote_zone_1 | Empfänger · Sender · Tote Zone |
| 743 | E/N | ssb; ssb_2 | Leistung |
| 751 | E/N | aequivalente_isotrope_strahlungsleistung_eirp_1; aequivalente_isotrope_strahlung | Isotroper Strahler |
| 760 | A | oszillator_schaltungen | Bar |
| 790 | N | modulationsarten | Amplitude · Periode |
| 810 | A | doppelueberlagerungsempfaenger_doppelsuper | Produktdetektor |
| 828 | A/E | begrenzerverstaerker; verstaerker | Amplitude · Ausgangssignal · Begrenzung · Eingangssignal · Verstärkung |
| 842 | E | transverter_1 | RX-Mischer · TX-Mischer · Treiber |
| 843 | E | transverter_1 | RX-Mischer · TX-Mischer · Treiber |
| 847 | N | frequenzspektrum | Funkwellen · Gammastrahlung · Höhenstrahlung · Infrarot · Licht · Mikrowellenstrahlung · Radar · Röntgenstrahlung · Terahertzstrahlung · Ultraviolett · Wechselströme |
| 851 | A/E | antennen_beruehrung_2; strom_spannung_speisung_1 | Anpass- |
| 852 | A | antennen_beruehrung_2 | Anpass- |
| 857 | A | halbleiter_2 | Diffusion |
| 858 | E | diode_1 | Germanium · Leuchtdiode · Schottkydiode · Silizium |
| 865 | E | ionosphaere_2 | Bodenwelle · Refraktion · Scheinbare Reflexion · Tote Zone |
| 867 | A | langer_kurzer_weg_2 | Kurzer Weg · Langer Weg |
| 870 | A | muf_luf_2 | Refraktion |
| 872 | A | sprungdistanz_2 | Distanz |
| 873 | E | langer_kurzer_weg_1 | Kurzer Weg · Langer Weg |
| 874 | A/E | ionosphaere_2; ionosphaere_3 | Nacht · Sommertag · Wintertag |
| 875 | A/E | senderausgangsleistung; ssb_3 | Amplitude |
| 876 | N | satelliten | Azimuth · Elevation |
| 878 | A | phase | Bogenmaß · Drehwinkel · Zeit |
| 883 | E | h_feld | Erde |
| 884 | E | e_feld | Erde |
| 885 | E | em_feld | Erde |
| 886 | E | em_feld; polarisation_2 | Erde |
| 904 | E | unmodulierter_traeger | Amplitude |
| 905 | N | modulationsarten | Amplitude |
| 906 | E/N | fm_2; modulationsarten | Amplitude |
| 907 | A | pm | Amplitude |
| 911 | E | digitale_signalverarbeitung_einleitung | Digitale Signal(verarbeitung) |
| 914 | E | alc | Balance- · Mischer · Treiber · Modulator |
| 916 | E | senderausgangsleistung | Antenne · SWR-Meter · Senderausgangsleistung · Tiefpass · Transceiver |
| 917 | E | unerwuenschte_aussendungen_2 | **Antenne · Messung von unerwünschten Aussendungen · SWR-Meter · Tiefpass · Transceiver** |
| 922 | E | kondensator_1 | Dielektrikum · Elektrode |
| 923 | E | kondensator_1 | Keramik-Dielektrikum · Metalllegierung · Plastik-Gehäuse |
| 924 | E | kondensator_1 | Bar |
| 935 | E | polarisation_2 | Erde |
| 936 | E | polarisation_2 | Erde |
| 937 | A | innenwiderstand | Leistungsoptimum |
| 940 | A | modulatoren | Leistung |
| 941 | A | modulatoren | Leistung |
| 942 | E | spule_1 | **Spule mit Eisenkern · Spule mit Ferritkern · Spule ohne Kern · Veränderliche Spule** |
| 958 | A | photovoltaik | Dünne Sperrschicht · N-Dotiert · P-Dotiert · Sonnenlicht · Verbraucher |
| 987 | A | troposphaere_3 | Duct · Inversionsschicht |
| 988 | A | ionosphaere_3 | **Jahre · Sonnenflecken im Mittel pro Monat · Sonnenflecken, Flux** |
| 991 | E | muf_luf_1 | Stunden |
| 1000 | A | langer_kurzer_weg_2 | Kurzer Weg · Langer Weg |
| 1002 | A | physikalische_stromrichtung | Physikalische Stromrichtung · Technische Stromrichtung |
| 1003 | A | strom_spannung_messung_3 | zum Netzteil · zum TX |
| 1004 | A | strom_spannung_messung_3 | Reales Spannungsmessgerät |
| 1005 | A | oszilloskop_2 | Impulsdauer |
| 1007 | A | strom_spannung_messung_3 | Reales Strommessgerät |
| 1012 | E | widerstand_ntc_ptc | NTC · PTC |
| 1018 | A/E | innenwiderstand; spannungsquelle | Reale Spannungsquelle |
| 1022 | E | schwingkreis_1 | Grenzfrequenz |
| 1023 | E | schwingkreis_1 | Hochpass (probable, fragment « ochpass ») |
| 1024 | E | schwingkreis_1 | Grenzfrequenz |
| 1044 | E | bandbreite_2 | Bandbreite |
| 1048 | E | yagi_uda_2 | Direktor · Reflektor · Strahler · Strahlungsrichtung |
| 1051 | E | swr_meter_1 | Antennen- · tuner |
| 1052 | E | swr_meter_1 | Antennen- · tuner |
| 1056 | E | ssb_2 | Leistung |
| 1058 | A | innenwiderstand | Reale Stromquelle |
| 1060 | A | mapping | Amplitude · Phase |
| 1065 | A | kondensator_2 | Isolator |
| 1071 | A | transistor_2 | Basis · Emitter · Kollektor |
| 1072 | A | transistor_2 | Basis · Emitter · Kollektor |
| 1073 | A | transistor_2 | Drain · Gate · SiO · Source |
| 1074 | A | transistor_2 | Drain · Gate · SiO · Source |
| 1075 | A | transistor_2 | Selbstleitender N-Kanal-MOSFET · Selbstleitender N-Kanal-Sperrschicht-FET · Selbstleitender P-Kanal-MOSFET · Selbstleitender P-Kanal-Sperrschicht-FET · Selbstsperrender N-Kanal-MOSFET · Selbstsperrender P-Kanal-MOSFET |
| 1076 | A | brueckenschaltung | (aucun résidu fiable — bruit de style résiduel) |
| 1078 | A | innenwiderstand | Dämpfung · Leistung · normierter Wert |
| 1082 | A | oszillator_dds | Adresszähler · Bits · D/A Umsetzer · Register · Sinus-Tabelle · Taktgenerator |
| 1095 | A | intermodulation_kreuzmodulation | **Frequenz in MHz · Leistung** |
| 1096 | A | intermodulation_kreuzmodulation | Sättigung |
| 1097 | A | snr_rauschzahl | Rauschen · Signal |
| 1113 | A | nahfeld | Fernfeld · Reaktives Nahfeld · Strahlendes Nahfeld |
| 1114 | A | nahfeld | Fernfeld · Reaktives Nahfeld · Strahlendes Nahfeld |
| 1115 | A | nahfeld | Fernfeld · Reaktives Nahfeld · Strahlendes Nahfeld |
| 1116 | A | naeherungsformel_2; nahfeld | Elektrischer Dipol · Fernfeld · Magnetische Loop · Reaktives Nahfeld · Strahlendes Nahfeld |
| 1117 | A | polarmodulation | Phasenmodulator |
| 1118 | A | emitterschaltung; kollektorschaltung | Emitterschaltung · Kollektorschaltung |
| 1119 | A | kollektorschaltung | Arbeitspunkt · Ausgangskennlinien · Eingangskennlinie |
| 1120 | A | verstaerker_wirkungsgrad | **HF Nutzleistung · Verluste durch Abwärme und Ruheströme · Zugeführte Gleichstromleistung** |

## 4. Proposition pour la suite (à valider par Pierre)

> **Mise à jour du 15/08/2026 — le chantier est clos. Lire ceci en premier ;
> tout ce qui suit est conservé pour l'historique.**
>
> **Le §3 ci-dessus est périmé.** Il a été constitué avant les forks, par
> extraction de toute paire d'accolades « feuille » sur les versions **amont**.
> L'inventaire qui fait foi désormais a été mesuré sur
> `build-<CLASSE>/img/<id>include.tex`, c'est-à-dire la version **réellement
> composée** de chaque dessin — fork français s'il existe, amont sinon.
> 861 couples (classe, dessin) examinés, 418 mots distincts extraits des seules
> zones de texte composé.
>
> **Ce que cette mesure a trouvé, et que rien ne signalait :**
>
> | | forkés portant encore de l'allemand | non forkés portant de l'allemand |
> | --- | ---: | ---: |
> | N | 7 | 6 |
> | E | 4 | 19 |
> | A | 28 | 29 |
> | **total** | **39 — des défauts** | **54 — le chantier** |
>
> Les 39 premiers étaient **des défauts présents dans les trois PDF a.2
> livrés**. `sonde_dessins.py` rendait `rc=0` en toute bonne foi : sa liste ne
> contenait ni `Wert`, ni `Distanz`, ni `Mischer`, ni `Koaxialkabel`. Quatre
> exemples, vérifiés dans le PDF :
>
> - **1092 (A)** : « 2. AM de 1 : Einton moduliert Amplitude de la porteuse » —
>   la substitution du 14/08 avait traduit les mots de sa liste et laissé le
>   reste ;
> - **996 (A)** : fork de 8 782 lignes où seul « Höhe » avait été traduit ; la
>   légende affichait encore *Winter Nacht, Sommer Tag* et l'axe *Distanz [km]*
>   à côté d'un axe *Hauteur [km]* ;
> - **434 et 435 (A)** : « Auf le Signal perturbateur abgestimmt », moins
>   lisible que l'allemand d'origine ;
> - **666 (N et E)** : **« CCathode »**, un mot d'aucune langue, né de deux
>   substitutions enchaînées sur un libellé amont tronqué. Présent dès la a.1.
>   Détail dans `docs/defauts-amont.md` §5.
>
> **Traitement, feuille d'arbitrage nº 3 du 15/08/2026.** 98 fichiers produits
> par **remplacements littéraux comptés** — chaîne exacte vers chaîne exacte,
> échec fatal sur écart de comptage — et non par substitution mot à mot, qui
> est précisément ce qui avait produit « Auf le … abgestimmt ». Le dictionnaire
> a été établi par **comptage dans les 387 sections traduites** (corpus de
> 1,94 M caractères) : *puissance* 989, *valeur* 657, *mélangeur* 117 contre
> *mixeur* 0, *atténuateur* 52 contre *affaiblisseur* 0. Deux termes ont été
> réglés par un **précédent déjà composé**, ce qui vaut mieux qu'un comptage :
> `Treiber` → « Étage pilote » (dessins 842, 843, 914) et `Stromrichtung` →
> « sens physique du courant » (dessin 1002).
>
> Six arbitrages échappaient au comptage et ont été tranchés par Pierre :
> `Verbraucher` → **charge** · `Einton`/`Zweiton` → **un ton / deux tons** ·
> `Netzteil` → **alimentation secteur** · `Ort` → **position** ·
> `Langwelle`/`Mittelwelle` → **ondes longues / ondes moyennes** ·
> `Frequenzgemisch` → **mélange de fréquences**. La décision du §9 sur
> `Ordnung` → « ordre » a été close en même temps, dessin **et** formule.
>
> **Deux angles morts découverts en cours de route**, tous deux réels :
>
> - le texte en **mode mathématique** échappait à l'extraction. Un balayage de
>   `\mathrm{}` a révélé le dessin **488** (A), qui composait
>   `$\mathrm{Audioverstärker}$` — forké et traduit, `NF` passant à `BF` au
>   passage, comme dans les 61 emplois des sections ;
> - le symbole **`ü`** du rapport de transformation (dessins 260, 303, 315),
>   remplacé par **`m`** sur décision de Pierre.
>
> **État final : 222 dessins forkés** (N 39 · E 72 · A 111), tous compilés
> isolément sans erreur avant toute recompilation de livre, tous enregistrés au
> manifeste. `sonde_dessins.py` v0.2 porte les termes de cette feuille — sans
> quoi elle aurait continué de rendre `rc=0` sur des dessins fautifs.
>
> **Ce qui reste** : la sonde lit le source et non le PDF, et sa liste reste
> une liste. Elle donnera toujours un plancher. Le contrôle qui a réellement
> trouvé les défauts est l'extraction des **zones de texte composé** décrite
> ci-dessus ; elle est reproductible, mais n'est pas outillée au dépôt —
> décision de Pierre du 15/08/2026, pour ne maintenir qu'un seul outil.

> **Mise à jour du 14/08/2026 — conservée pour l'historique.**
>
> Ce document affirmait encore, plus bas, qu'« aucun dessin réel n'est forké à
> ce jour » et qu'« aucune de ces quatre propositions n'est mise en œuvre ».
> Les deux sont **fausses depuis longtemps** : il y a **126 dessins forkés et
> traduits** (N 30 · E 42 · A 54), et les propositions 2 et 3 sont faites. Les
> manifestes existent pour les trois classes.
>
> CLAUDE.md se trompait de son côté en parlant d'une « fiche d'arbitrage à
> 12 points » : cette section en compte **quatre**. Les deux mentions ont été
> corrigées.
>
> **Ce qui reste réellement à trancher : les points 1 et 4** — le critère de
> sélection des dessins à forker, et l'ordre de traitement.
>
> **Nouvelle mesure du 14/08/2026** : `sonde_dessins.py` (racine du dépôt)
> distingue deux populations parmi les dessins *effectivement composés* dans
> les livres. État après le chantier du jour :
>
> | | dessins utilisés | forkés | forkés avec allemand | affichant de l'allemand |
> | --- | ---: | ---: | ---: | ---: |
> | N | 142 | 33 | 0 | **1** (était 4) |
> | E | 305 | 53 | 0 | **10** (était 21) |
> | A | 414 | 78 | 0 | **13** (était 37) |
>
> Les **10 dessins forkés portant encore de l'allemand** étaient un défaut de
> traduction : corrigés (« onde de sol », « onde d'espace », « atténuation »,
> « gain » — vocabulaire déjà en usage, vérifié plutôt que supposé).
>
> **38 dessins ont été forkés et traduits** dans la foulée, portant le total de
> 126 à 164. La substitution ne touche **que les textes composés** — contenu de
> `\node{}`, `label=`, `\addlegendentry{}` — et jamais le reste du fichier, où
> « der », « und » et « oder » apparaissent dans des noms de macros et des clés
> de style. Les 164 dessins forkés ont été compilés isolément avant toute
> recompilation : zéro erreur LaTeX.
>
> **Les 24 dessins restants** sont ceux dont l'allemand n'est pas dans une zone
> repérable automatiquement — nœuds à syntaxe inhabituelle, texte porté par un
> chemin. Ils demandent un examen un par un, et constituent désormais l'essentiel
> du point 1 ci-dessous.
>
> La sonde donne un **plancher**, pas un compte exhaustif : un mot allemand
> sans umlaut et absent de sa liste passe au travers.

1. ~~**Fork ciblé, pas systématique**~~ — **TRANCHÉ par Pierre le 14/08/2026 :**
   *tout texte allemand composé est traduit, sans exception de cognat.*

   La proposition initiale — ne forker que les dessins « où le texte allemand
   gêne la lecture », et laisser les cognats transparents au jugement au cas
   par cas — est abandonnée. La règle est désormais uniforme et ne demande
   plus d'appréciation dessin par dessin.

   **Portée réelle de cette règle, mesurée le 14/08/2026.** Elle va bien au-delà
   des dessins que `sonde_dessins.py` sait voir. La sonde repose sur les
   umlauts et sur une liste de mots ; elle manque les **cognats partiels**,
   sans umlaut et absents de sa liste — `Kondensator`, `Kathode`, `Kollektor`,
   `Eingangssignal`, `Ausgangssignal`, `Drehwinkel`, `Begrenzung`… L'inventaire
   du §3 ci-dessus, constitué par une autre méthode, en recense **133 dessins**
   et **109 termes simples** distincts, contre 24 dessins encore signalés par la
   sonde.

   Un tri reste nécessaire : parmi ces 109 termes, certains n'ont rien à
   traduire (*Amplitude*, *Diffusion*, *Germanium*, *Drain*, *Duct*), d'autres
   demandent un vrai choix de vocabulaire (*Gewinn* → gain, *Bogenmaß* →
   radian, *Arbeitspunkt* → point de fonctionnement). **C'est un chantier de
   traduction technique à part entière**, non une substitution mécanique.

   > **REPORTÉ à la session suivante**, sur décision de Pierre du 14/08/2026.
   > La a.2 est livrée avec les 38 dessins traduits ce jour ; le reste constitue
   > un lot autonome.
   >
   > **Point de reprise, pour ne pas repartir de zéro :**
   >
   > 1. la liste des 109 termes s'obtient en parcourant les lignes du §3
   >    ci-dessus (`^| <id> |`), quatrième colonne, séparateur « · », en
   >    écartant les mots identiques ou anglais ;
   > 2. **faire valider le dictionnaire complet par Pierre en une fois**, avant
   >    toute application : c'est du vocabulaire d'examen, il doit coller à
   >    celui des sections. La méthode éprouvée est le comptage — « intensité de
   >    champ » (44 emplois), « longueur d'onde » (71), « porteuse » (177) — et
   >    non l'intuition ;
   > 3. réemployer la mécanique de fork du 14/08 : substitution **uniquement**
   >    dans les zones de texte composé (`\node{}`, `label=`,
   >    `\addlegendentry{}`), jamais dans tout le fichier — « der », « und » et
   >    « oder » vivent aussi dans des noms de macros et des clés de style ;
   > 4. compiler tous les dessins forkés isolément **avant** de relancer les
   >    livres, puis `verifier_amont.py initialiser --type dessins` pour
   >    enregistrer les empreintes ;
   > 5. penser à **enrichir `sonde_dessins.py`** des termes retenus : en l'état
   >    elle ne voit pas les cognats partiels et retournera 0 à tort.
   >
   > **Le fork est maintenu comme mécanisme** — décision de Pierre du
   > 14/08/2026, prise en connaissance de son coût. Une alternative avait été
   > proposée : faire appliquer par `build_book.py` un dictionnaire de
   > substitution au moment de la génération, sans dupliquer le dessin. Elle est
   > écartée.
   >
   > Le coût du fork, mesuré au commit : les 38 dessins de ce jour représentent
   > **69 466 lignes**, dont cinq pgfplots de données massives forkés pour un
   > seul mot — 994 (18 714 lignes), 997 (16 946), 998 (11 771), 996 (8 781),
   > 995 (6 403), tous pour traduire « Höhe ». La conséquence à garder en tête
   > est la **dette de synchronisation** : si le DARC fait évoluer l'un de ces
   > dessins, `verifier_amont.py` signalera la dérive, mais le report se fera à
   > la main dans un fichier de plusieurs milliers de lignes.
2. **Mécanisme technique** — ✅ fait (2026-08-11, `build_book.py` v0.15) :
   un dessin placé dans `traductions/<CLASSE>/dessins/<id>.tex` prime
   désormais sur l'amont, avec la même priorité que les sections (premier
   répertoire `--translations` cité qui contient le fichier l'emporte).
   Testé par substitution isolée sur un dessin fictif (aucun effet de bord
   sur les 130 autres dessins de la classe N, comptes de sections/questions
   inchangés). Aucun dessin réel n'est forké à ce jour — le mécanisme est
   prêt, pas encore utilisé.
3. **Suivi de la dérive amont** — ✅ fait (2026-08-11) : `verifier_dessins.py`,
   script autonome (pas une évolution de `build_book.py`, donc hors du
   protocole de version de ce dernier).

   > **Mise à jour du 14/08/2026** — `verifier_dessins.py` a été **supprimé**,
   > remplacé par `verifier_amont.py` (v0.2), qui suit de la même façon les
   > dessins forkés **et** les sections traduites. Les commandes décrites
   > ci-dessous existent toujours, avec un argument `--type dessins|sections`
   > en plus, et une commande `initialiser` pour constituer une ligne de base
   > en masse. Le format de `dessins-manifest.json` est inchangé.

   Deux commandes :
   - `enregistrer --edition <N|E|A> --input <amont> --id <id>` : après avoir
     créé `traductions/<CLASSE>/dessins/<id>.tex`, journalise l'empreinte
     SHA-256 de l'original amont correspondant et la date du jour dans
     `traductions/<CLASSE>/dessins-manifest.json` (un manifeste par classe,
     absent tant qu'aucun dessin n'y est forké).
   - `verifier --input <amont> [--edition <N|E|A>]` : recalcule l'empreinte
     actuelle de chaque dessin forké et la compare à celle enregistrée.
     Rapporte trois états par dessin — inchangé, **dérive détectée**
     (l'amont a changé depuis le fork, code de sortie 1), ou introuvable
     (le dessin a disparu ou été renommé côté DARC, code de sortie 1).
   Testé avec un fork jetable (créé puis supprimé) sur les trois cas :
   amont inchangé, amont modifié, amont disparu — tous correctement
   détectés. Aucun dessin n'est actuellement enregistré (le manifeste
   n'existe pas tant qu'aucun fork réel n'a eu lieu) ; à lancer en début de
   session dès qu'un premier dessin sera forké.
4. **Ordre suggéré** (à confirmer) : traiter d'abord les 9 dessins à phrase
   complète (impact lecture le plus fort), notamment 680 et 917 qui portent
   sur la sécurité (« Kurzschluss- und Verpolungsgefahr », « Messung von
   unerwünschten Aussendungen »).

**État au 14/08/2026** — les propositions 2 et 3 sont **faites** (mécanisme de
fork en v0.15, suivi de dérive dans `verifier_amont.py`), et 126 dessins sont
forkés et traduits. Les propositions **1 et 4 restent à trancher** : le critère
de sélection et l'ordre de traitement. Cf. l'encadré en tête de section, qui
donne le compte des dessins encore en allemand, classe par classe.
