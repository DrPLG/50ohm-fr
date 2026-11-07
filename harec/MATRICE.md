# Matrice de l'ouvrage HAREC — A5 noir et blanc, 260 pages

> **Proposition du 22/10/2026, à arbitrer par Pierre.** Elle suit le plan de
> l'annexe I de l'arrêté du 21/09/2000 (version en vigueur,
> [`PROGRAMME.md`](PROGRAMME.md)), et ses **poids** suivent la banque Exam'1
> (§ 1). Les colonnes « disponible » sont **mesurées** sur le corpus traduit,
> chaque section de [`programme.json`](programme.json) n'étant comptée qu'une
> fois. Les colonnes « cible » sont **estimées** : elles seront recalées sur
> le pilote compilé.

## 1. Ce que dit la banque Exam'1

**Source :** `https://exam1.r-e-f.org/assets/questions.json`, version du
30/09/2026, **2 961 questions** en 20 thèmes, lue le 22/10/2026.

**Licence CC BY-NC-SA, incompatible (§ 7 de CLAUDE.md).** On n'en tire que
des **comptes et des natures de questions** pour orienter les priorités.
Aucun énoncé, aucune réponse ni aucun libellé n'est repris, ni ici ni dans
le livre.

La banque mêle des questions reconstituées à partir de comptes rendus de
candidats et des questions « maison ». Elle sert d'**indicateur** de ce qui
tombe à l'examen, pas de mesure exacte.

### Épreuve de réglementation : 1 085 questions

Hors 175 exercices générés (préfixes 50, 60 et 70 : épellation, indicatifs,
code Q) et hors le thème « entraînement » (361 questions mêlées).

| thème Exam'1 | part | réponses chiffrées | → chapitre |
| --- | ---: | ---: | --- |
| indicatifs français et préfixes européens | **19,7 %** | 5 % | I.1 / I.2 |
| sanctions, examen, perturbations, bande passante | 14,7 % | 31 % | I.2 / I.3 |
| définition et autorisation des classes d'émission | 13,7 % | 44 % | I.2 |
| teneur des messages, matériel obligatoire, exposition | 11,8 % | 12 % | I.2 / I.3 |
| gammes d'ondes, décibels, CEM, protection | 10,0 % | 39 % | I.3 |
| adaptation, ROS, affaiblissement linéique | 9,1 % | 74 % | I.4 |
| caractéristiques des antennes, longueur d'onde | 8,1 % | 26 % | I.4 |
| table d'épellation | 6,7 % | 0 % | I.5 |
| code Q | 6,2 % | 1 % | I.5 |

### Épreuve technique : 1 340 questions

| thème Exam'1 | part | réponses chiffrées | schéma cité dans l'énoncé (minimum) | → chapitre |
| --- | ---: | ---: | ---: | --- |
| antennes, couplage, propagation, lignes | **15,4 %** | 55 % | 13 % | II.6 |
| transformateurs, ampli op, filtres RC, LC, RLC | **15,3 %** | 74 % | 31 % | II.2 / II.3 |
| électricité de base | 12,1 % | 75 % | 17 % | II.1 |
| synoptiques d'émetteurs et de récepteurs | 10,6 % | 6 % | 18 % | II.4 / II.5 |
| condensateurs et bobines | 9,7 % | 81 % | 7 % | II.2 |
| diodes et transistors, classes d'amplification | 8,5 % | 49 % | 29 % | II.2 / II.3 |
| rôle des étages HF, haut-parleur, micro | 8,2 % | 22 % | 11 % | II.4 / II.5 |
| courants alternatifs | 8,2 % | 86 % | 16 % | II.1 |
| groupements de résistances | 6,8 % | 96 % | 35 % | II.3 |
| code des couleurs des résistances | 5,1 % | 96 % | 49 % | II.2 |

Chaque question est servie comme une image (« carte » de 770 × 350 pixels,
comme à l'écran de l'examen). La colonne « schéma » ne compte donc que les
énoncés qui **nomment** un schéma : c'est un minimum.

### Ce que cela change pour le livre

1. **La réglementation, c'est d'abord du droit français et des tableaux.**
   Indicatifs, classes d'émission, sanctions et teneur des messages font
   **60 %** de l'épreuve. La première matrice leur donnait 26 pages sur 72 ;
   les brouillages et les antennes, à 17 % des questions, en avaient 42.
   **Rééquilibré ci-dessous.**
2. **La technique, c'est du calcul.** Les trois quarts des questions de
   théorie ont une réponse chiffrée, sur des énoncés très courts (12 à
   22 mots). Chaque chapitre technique porte donc des **encadrés
   « méthode »** (formule, exemple chiffré, ordre de grandeur à retenir),
   pris sur le budget de prose et non en plus.
3. **Les synoptiques pèsent 19 %** (synoptiques et rôle des étages). Il faut
   des schémas-blocs nets, lisibles en gris, et appris étage par étage.
4. **Le corpus ne couvre pas tout.** L'ampli op et le haut-parleur/micro
   sont présents dans la banque mais absents du texte de l'annexe : à
   traiter brièvement (l'ampli op existe dans `integrierte_schaltkreise`). Les
   classes d'émission et les indicatifs français sont **à écrire** sur
   sources officielles (CRT-43 et UIT pour la désignation, arrêtés pour les
   autorisations).
5. **Calculatrice : une calculatrice de type collège est autorisée**
   (information de Pierre, 29/10/2026 ; le texte de l'arrêté n'en dit rien).
   Les encadrés « méthode » s'appuient donc sur elle (racine, sinus en
   degrés, puissances de 10), en gardant les ordres de grandeur de tête
   (décibels ronds, ×2 = 3 dB, doubler la distance = +6 dB) pour vérifier
   le résultat. **Source officielle à citer avant publication** (page
   « examen » de l'ANFR).
6. **Questions d'entraînement** dans le même format que l'examen : énoncé
   court, quatre réponses, majorité chiffrée en technique.

## 2. Hypothèses de densité (estimées)

- Page de prose A5, corps 10 : **≈ 450 mots**.
- Figure : **⅓ de page** en moyenne, en tenant compte de la borne de 0,6 de la largeur pour les
  figures des notes de marge (document réduit du 22/10).
- Photos : très peu, car elles passent mal en gris. Elles sont comptées avec les figures.
- Rappel de la feuille nº 12 : l'estimation peut se tromper de moitié.
  **Le pilote décide.**

## 3. Vue d'ensemble

| bloc | pages | part |
| --- | ---: | ---: |
| liminaires (titre, mentions, avant-propos, l'examen mode d'emploi, sommaire) | 12 | 5 % |
| **Partie I — Réglementation** (épreuve 1 : 20 questions, 15 min) | **72** | 28 % |
| **Partie II — Technique** (épreuve 2 : 20 questions, 30 min) | **138** | 53 % |
| **Partie III — Entraînement** (2 examens blancs et corrigés) | 30 | 12 % |
| annexes (formulaire, bandes) et index | 8 | 3 % |
| **total** | **260** | 260 % 4 = 0 |

## 4. Partie I — Réglementation (annexe I, 1re partie)

| ch. | titre | poids Exam'1 | disponible | pages | figures | mots cibles | à écrire |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| I.1 | Réglementation internationale | ~10 % | 8 100 | 12 | 4 | 3 500 | art. 25 du RR, rés. 640 ; **tableau des préfixes européens** |
| I.2 | Réglementation nationale | **~50 %** | **0** | **26** | 0 | 9 000 + 6 p. de tableaux | **tout** : certificat, examen, sanctions, indicatifs français, classes d'émission et autorisations, bandes et puissances, teneur des messages, matériel obligatoire |
| I.3 | Brouillages et protections | ~13 % | 18 600 | 12 | 8 | 4 000 | exposition du public : textes français à vérifier |
| I.4 | Antennes et lignes | ~17 % | 14 900 | 16 | 14 | 4 600 | boîte d'accord à rassembler |
| I.5 | Code Q et alphabet | ~13 % | 1 700 | 6 | 0 | tableaux et exercices | encarts France de N à reprendre |
| | **total I** | | **43 300** | **72** | **26** | **≈ 21 100** | |

Les poids sont approximatifs, parce que deux thèmes Exam'1 chevauchent deux
chapitres (sanctions et perturbations, teneur des messages et exposition).

## 5. Partie II — Technique (annexe I, 2e partie)

| ch. | titre | poids Exam'1 | disponible | pages | figures | mots cibles | à écrire |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| II.1 | Électricité, électromagnétisme, radioélectricité | ~20 % | 23 400 | 28 | 24 | 8 100 | encadrés « méthode » |
| II.2 | Composants | ~22 % | 16 300 | 28 | 24 | 8 100 | tube électronique ; code des couleurs en exercices |
| II.3 | Circuits | ~20 % | 20 400 | 28 | 30 | 7 700 | Foster-Seeley ; ampli op (bref) |
| II.4 | Récepteurs | ~10 % | 6 400 | 13 | 12 | 3 800 | calibrateur à quartz ; haut-parleur |
| II.5 | Émetteurs | ~9 % | 7 700 | 13 | 12 | 3 800 | microphone |
| II.6 | Propagation et antennes | ~15 % | 11 000 | 20 | 20 | 5 500 | affaiblissement en espace libre, guides d'ondes |
| II.7 | Mesures | ~4 % | 7 300 | 8 | 6 | 2 500 | ondemètre à absorption |
| | **total II** | | **92 400** | **138** | **128** | **≈ 39 500** | |

## 6. Partie III — Entraînement

| | contenu | pages |
| --- | --- | ---: |
| III.1 | Examen blanc nº 1 : 20 questions de réglementation + 20 de technique | 10 |
| III.2 | Examen blanc nº 2 : même composition | 10 |
| III.3 | Grilles de réponses et corrigés commentés, barème en vigueur (+1 / 0) | 10 |

**Questions écrites par nous**, dans le format de l'examen : énoncé court,
quatre réponses mélangées (mécanisme du CIR 2), réponses chiffrées en
majorité pour la technique. La répartition par thème suit les parts du § 1.
Les questions de technique peuvent être adaptées du catalogue allemand
(CC BY 4.0), jamais d'Exam'1.

## 7. Totaux

| | disponible | retenu |
| --- | ---: | ---: |
| mots de prose | 135 700 | **≈ 60 600** (45 %) |
| figures | 402 | **≈ 154** (38 %) |
| pages de cours | — | 210 |

## 8. Points à arbitrer

> **07/11/2026 — I.4 Antennes et lignes rédigé** (choix de Pierre) :
> 14 sections, **≈ 3 570 mots** (24 % des 14 900 du corpus, cible 4 600),
> 21 figures, 4 tableaux, 9 encadrés « méthode » ou « attention ». Arbre
> généré sans compilation : 21 figures sur 21, 0 label en double, 0 faux
> positif d'unité, 0 accent en mode math, 0 deux-points en légende.
> **Non compilé.** À la densité du pilote (≈ 180 mots et une figure par
> page), compter **18 à 20 pages** pour 16 prévues.
>
> **Partage avec II.6 (fait sans arbitrage, à confirmer) :** I.4 garde les
> types d'antennes, leurs caractéristiques et l'usage pratique des lignes
> (coaxial et bifilaire, ROS, quart d'onde, symétriseur, boîte d'accord) ;
> le calcul de $Z_0$, le coefficient de vélocité, l'affaiblissement
> linéique et les lignes accordées restent en II.6, où I.4 renvoie par le
> titre du chapitre. La $\frac{5}{8}\lambda$ n'est que citée.
>
> **Écrit au-delà du corpus** (technique, pas réglementaire) : boîte
> d'accord (rubrique « à écrire » : filtre en pi repris de
> `impedanztransformation`, montage en T, où placer la boîte), formule
> $s = R/Z_0$ et coefficient de réflexion, pertes de polarisation croisée
> (> 20 dB, 3 dB circulaire/linéaire), rotation de polarisation en HF,
> symétriseur 4:1 du dipôle replié, impédance basse des Yagi. **À faire
> relire par Sylvain F6DBI.** Aucune règle nouvelle : PAR et PIRE renvoient
> à I.2.
>
> **Compilé le 07/11/2026** (accord de Pierre), I.2 + I.4 + II.6, A5 noir
> et blanc, v0.38, 2 min 05 : **68 pages** (68 % 4 = 0). **I.4 : pp. 21 à
> 43, soit 23 pages** pour 16 prévues (p. 44, verso blanc). 0 erreur,
> 0 note de marge trop haute, 0 caractère manquant, 0 « ?? », 42 figures
> sur 42 sans coupure (mesuré au `.aux`), 0 pixel coloré (pp. 21-43).
> 1 débordement de 12 pt (`harec_parabole`, « décimètres » non coupé) :
> phrase reformulée dans la source, **non recompilé**.
> **Densité : ≈ 155 mots par page**, moins que le pilote (180). Cause vue
> sur planche : les figures sont composées à pleine largeur et plusieurs
> occupent une demi-page ou plus (669 Marconi p. 26, 1046 p. 27, 326 et
> 51 pp. 33-34, 633 p. 41, 1100 filtre en pi p. 42). C'est le levier
> « borne des figures à 0,45 » déjà noté plus bas, plus pressant ici.
>
> **Réglé le même jour en `build_book.py` v0.39** (demande de Pierre) :
> figures des notes bornées à **0,45 de la largeur et 0,3 de la hauteur
> du bloc** (la largeur seule ne réduisait pas les dessins élancés). Bloc
> injecté en A5 seulement : arbre N régénéré **identique** à la v0.38.
> Document réduit (verticales, parabole, polarisation, adaptation, boîte
> d'accord) : 0 erreur, 0 débordement, 6 figures ramenées, 0 pixel
> coloré, **8 pages contre ≈ 12 dans le livre du 07/11**. Touche aussi
> I.2 et II.6.
>
> **Recompilé en v0.39 le 07/11/2026** (accord de Pierre), 2 min 09 :
> **62 pages** (68 en v0.38). **I.4 : pp. 21 à 40, 20 pages** (23 en
> v0.38, 16 prévues) ; **II.6 : pp. 41 à 59, 19 pages** (21) ; I.2
> inchangé (pp. 5 à 19). 0 erreur, 0 débordement (celui de la parabole a
> disparu), 0 caractère manquant, 0 « ?? », 42 figures sur 42 sans
> coupure, 36 figures ramenées par le clamp, 0 pixel coloré sur tout le
> livre. **62 % 4 = 2** : sans importance tant que le livre est incomplet.
> **Vu sur planche :** le tableau des ROS (p. 37) est séparé de sa légende,
> rejetée en haut de la p. 38. `verifier_figures.py` ne contrôle pas les
> tableaux, et le moteur ne rend pas un tableau insécable avec sa légende.
> Il reste aussi un blanc en bas de la p. 37.
>
> **Défaut repéré :** le dessin 562 (dipôle replié, non forké) porte
> $V_\mathrm{K}$ (*Verkürzungsfaktor*), là où II.6 écrit $k_\mathrm{v}$.
> Il sort ainsi dans le livre E publié. Forker le dessin toucherait E.

> **30/10/2026 — I.2 Réglementation nationale rédigé** (choix de Pierre) :
> 10 sections, **≈ 4 400 mots**, 8 tableaux, 4 encadrés « méthode » (lire un
> indicatif, faut-il déclarer sa station, retenir les puissances, décoder une
> classe d'émission). **Aucune règle nouvelle** : tout est repris des encarts
> « En France » de N, rédigés sur les textes (§ 7 de CLAUDE.md), plus le
> barème de l'art. 2 lu sur Légifrance le 22/10. Arbre généré sans
> compilation : 0 renvoi pendant, 1 faux positif d'unité corrigé.
> **Non compilé.**
>
> **Compilé le 30/10/2026 avec II.6** (accord de Pierre), A5 noir et
> blanc, 1 min 30 : **44 pages** (44 % 4 = 0). **I.2 : pp. 5 à 19, soit
> 15 pages** pour 26 prévues (≈ 4 800 mots et 9 tableaux) ; II.6 : pp. 21
> à 40, inchangé. 0 erreur, 0 débordement, 0 caractère manquant, 0 renvoi
> non résolu, 21 figures sans coupure, 0 pixel coloré, folio à 6,6 mm.
> **Corrigé sur épreuve :** le tableau des textes (§ 2.1) avait une
> première colonne rigide qui écrasait la seconde (un mot par ligne,
> 14 débordements et une page trop haute de 125 pt) — colonnes passées en
> `X` ; trois lignes reformulées ; codes (A1A, J3E, indicatifs) passés de
> `\mathrm` à `\text`, la police mathématique les composant trop petits.
> Les tableaux sont légendés « Fig. » : comportement du moteur amont, commun
> à tous nos livres. PDF : `build-HAREC/livre-HAREC-v0.1-a5-nb.pdf`.
>
> **À valider par Pierre avant publication (réglementaire) :**
> 1. décision ARCEP n° 2012-1241 : aucune modification trouvée après la
>    n° 2019-1412 (recherche du 30/10) — à confirmer sur Légifrance ;
> 2. tableau des bandes et puissances : repris de l'encart de N, à relire
>    contre l'annexe en vigueur ;
> 3. classes d'émission : j'ai ajouté **N** et **H** (1re lettre) et
>    l'exemple $\mathrm{F2A}$ d'après l'appendice 1 du RR, au-delà de ce que
>    portait l'encart — à vérifier sur le RR ou la CRT-43 ;
> 4. indicatifs spéciaux (15 jours sur 6 mois, 20 jours ouvrables), relais
>    (classes admises, dossier) : repris des encarts, source ANFR à citer ;
> 5. calculatrice de type collège : **non écrite** (commentaire `% TODO`
>    dans `harec_certificat_examen`), en attente d'une source ;
> 6. ~~écoute et secret des correspondances : exclus~~ — **rédigé le
>    30/10/2026** (`harec_ecoute_secret`, 389 mots), à la demande de Pierre,
>    **après lecture des textes sur Légifrance le même jour** : code pénal
>    art. 226-15 al. 2 et 226-3 (loi n° 2020-936), R226-7 (décret
>    n° 2019-1139), arrêté du 4 juillet 2012 modifié, annexe II, item 2
>    (arrêté du 11/08/2016). Sources en commentaire en tête du fichier.
>    **Non repris, faute de source retrouvée :** « écoute libre depuis 1990 ».
>    **Défaut trouvé dans le livre N publié** (encart de
>    `fernmeldegeheimnis_abhoerverbot`) : il rattache l'exclusion des bandes
>    d'amateur à l'art. R. 226-3, alors que l'arrêté la place à l'annexe II,
>    qui relève de l'art. R226-7 ; et il affirme l'écoute libre « depuis
>    1990 » sans source. **Corrigé le 30/10/2026** (décision de Pierre), N et
>    NEA non recompilés.

> **29/10/2026 — pilote retenu par Pierre : II.6 Propagation et antennes.**
> Rédigé le même jour dans `harec/sections/` : 14 sections, **3 711 mots**
> (34 % des 11 000 du corpus), 21 figures, 4 tableaux, 6 encadrés
> « méthode ». Deux rubriques écrites à neuf, absentes du corpus :
> affaiblissement en espace libre et guides d'ondes. Arbre généré sans
> compilation : 0 figure perdue, 0 renvoi pendant, 0 faux positif d'unité.
> **Compilé le 29/10/2026** (accord de Pierre), A5 noir et blanc, v0.38,
> 1 min 30 : **28 pages, dont le chapitre aux pp. 5 à 25, soit 21 pages**
> pour 20 prévues. 0 erreur, 0 débordement, 0 caractère manquant, 0 renvoi
> non résolu, 21 figures sur 21 sans coupure (mesuré au `.aux`), 0 pixel
> coloré, folio à 6,6 mm du bord fini sur toutes les pages.
>
> **Densité mesurée : ≈ 180 mots et une figure par page.** La matrice
> supposait 450 mots par page de prose et ⅓ de page par figure : avec ces
> hypothèses, le pilote aurait tenu en 17 à 18 pages. L'écart vient
> d'environ 1,5 page de blancs (pp. 7, 8, 10, 16, 18 : une figure ou un
> tableau insécable qui ne tient plus en bas de page) et de figures de notes
> plus hautes que prévu (borne de 0,6 de la largeur : la fig. 11.18 occupe
> une demi-page à elle seule).
>
> **Conséquence pour le budget, estimée :** les cibles de la matrice
> (≈ 60 600 mots et 154 figures sur 210 pages de cours) demanderaient
> environ **225 à 230 pages** à la densité du pilote, soit 15 à 20 pages
> de trop. Leviers, à arbitrer : borne des figures de notes à 0,45 au lieu
> de 0,6 ; environ 10 % de mots en moins ; ou corps 9,5 (D5).
>
> **Vu sur épreuve, à régler :**
> - formules de mes sources : `0,85` composé « 0, 85 » et `MUF` en italique
>   espacé en mode mathématique — **corrigé** (8 formules, `\num{}` et
>   `\mathrm{MUF}`), recompilé, vérifié sur le texte extrait ;
> - gris trop pâles sur les étiquettes de certains dessins (865, 874 : F₂,
>   F₁, E, D presque illisibles) — palette noir et blanc, déjà connue ;
> - encadrés « méthode » rendus en « Astuce », corps réduit des notes : une
>   boîte « Méthode » dédiée serait plus lisible ;
> - nombres en `\qty` un peu plus petits que le texte : rendu de siunitx
>   en mode mathématique, commun à tous nos livres ;
> - `verifier_figures.py` ne connaît pas l'édition HAREC (mesure faite à la
>   main sur le `.aux`).
>
> PDF de relecture : `build-HAREC/livre-HAREC-pilote-II6-a5-nb.pdf`.
> Le point 4 ci-dessous est réglé.

1. **Le pilote de D9 est à redéfinir.** « Propagation et antennes » est
   coupé en deux par le programme : antennes et lignes en I.4, propagation
   en II.6. Avec les poids Exam'1, deux candidats se dégagent :
   - **I.2 Réglementation nationale** (26 p., poids ~50 %, entièrement à
     écrire) : c'est le chapitre qui décide de l'épreuve 1, mais il ne mesure
     pas la densité des figures ;
   - **II.6** (20 p., 20 figures) : il mesure la densité d'un chapitre
     technique condensé.
2. **Ordre des parties.** Réglementation d'abord (celui de l'annexe) ou
   technique d'abord (les décibels et les antennes de I.3 et I.4 supposent
   l'électricité de II.1) ?
3. **Entraînement.** Deux examens blancs seulement (80 questions,
   30 pages), ou en plus quelques questions en fin de chapitre ?
4. **Calculatrice.** À vérifier auprès de l'ANFR avant d'écrire les
   encadrés « méthode ».
