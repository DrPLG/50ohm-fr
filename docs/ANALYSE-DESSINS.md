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

1. **Fork ciblé, pas systématique** — ne dupliquer que les dessins où
   Pierre juge le texte allemand gênant à la lecture ; laisser les cognats
   transparents (*Antenne, Signal, Transistor*...) au jugement au cas par cas.
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
   protocole de version de ce dernier). Deux commandes :
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

Aucune de ces quatre propositions n'est mise en œuvre à ce stade — ce
document attend l'arbitrage de Pierre.
