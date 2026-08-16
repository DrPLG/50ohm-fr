## SESSION 15/08/2026 — version a.2, francisation des dessins (feuille d'arbitrage nº 3)

Génération : 131/131 sections, 571 questions, 39 dessins francisés,
55 encarts « En France ». **258 pages**, 3,19 Mo après Ghostscript.

Contrôles du §4 : tous conformes (0 · 0 · 0 · 0), 0 erreur LaTeX,
**0 référence « ?? »**, 0 question séparée de ses réponses.
Clamps : 132 figures, 1 tableau.

### Dessins traités — 13 fichiers

**7 forks portaient encore de l'allemand**, donc visibles dans le PDF a.2
livré : 408 et 411 (`ylabel=Wert`), 659 et 669 (`Koaxialkabel`), 665
(`1. Ziffer`), 680 (`Gleichstrom`), 731 (`D-Region`, `bis 10`, `Regionen`).

**6 dessins forkés pour la première fois** : 628 (`Ort`, `Feldstärke`), 658
(`Region 1/2/3`), 734 (`Kalte`/`Warme`/`Sehr kalte Luft`), 745
(`DVB-T2 Kanal 35`), 908 et 909 (`70 cm Band` → « bande 70 cm »).

**Et « CCathode ».** Le dessin 666 imprimait ce mot, qui n'existe dans aucune
langue, **depuis la a.1**. Un fork antérieur substituait `Kathode` → `Cathode`
puis `athode` → `Cathode`, la seconde règle s'appliquant au résultat de la
première. Le libellé amont tronqué qui l'a rendu possible est consigné en
défaut amont (`docs/defauts-amont.md` §5). Jamais relevé en relecture.

### Ce que la sonde ne voyait pas

`sonde_dessins.py` rendait `rc=0` sur cette classe. Sa liste ne contenait ni
`Wert`, ni `Koaxialkabel`, ni `Ziffer` — et sa docstring l'annonçait. Passée en
v0.2 avec les termes de la feuille.

### Un piège de compilation, payé comptant

Les trois livres ont d'abord été recompilés **sans `--front-matter`** : ils sont
sortis sans avant-propos ni remerciements, et N est tombée de 258 à 254 pages.
Ce sont les **compteurs de clamp, rigoureusement identiques au 14/08**, qui ont
écarté la piste des figures et mené à la vraie cause. `build_book.py` ne se
plaint pas de l'absence de pièces liminaires ; seul `compiler.bat` passe les
deux options. **Lancer `build_book.py` à la main impose de les passer aussi.**

### Feuille d'arbitrage nº 4 — relecture de la classe E (15/08/2026, soir)

Dix points relevés par Pierre sur le livre E dans `Préparation_Version_a.2.txt`.
Tous reproduits, leur cause mesurée, et leurs équivalents cherchés en N et A.
**Deux points sur dix seulement étaient des réglages de classe** ; ce sont eux
qui ont imposé la recompilation des trois livres.

| décision | objet |
| --- | --- |
| **A4** | espace avant `!` et `?` — **rien changé**. Mesuré : babel donne 0,5 unité avant `; ! ?` et 1,0 avant `:`, ce qui EST la règle de l'Imprimerie nationale. Ce n'était pas un bogue |
| **B1** | nombres gras dans les énoncés — `build_book.py` v0.19 |
| **C1b** | dessin 942, libellés sur deux lignes |
| **C2b** | dessins 911 et 96, texte sur trois lignes, boîte élargie |
| **C3a** | dessin 666, « Anode » et « Cathode » en entier |
| **C4** | dessins 434-437, français fautif corrigé puis libellés ancrés à l'est |
| **D1** | `spannungsteiler_1`, point parasite retiré ; les 42 absences de point devant une formule restent, usage allemand |
| **E** | abréviation « OW » conservée, les légendes françaises l'emploient déjà |

### Le vrai diagnostic de B1 n'était pas celui de la feuille

La feuille proposait de « passer les énoncés en version mathématique grasse ».
En ouvrant le `.sty` amont, il s'est avéré que **le DARC le demande déjà** :
`\newkomafont{questiontext}{\bfseries\boldmath}`. Le fautif n'était pas la
définition de la question mais la **configuration des polices** —
`settings.tex` charge `unicode-math` sans jamais déclarer de version
mathématique grasse, si bien que `\boldmath` restait sans effet **et sans le
moindre avertissement**.

Le défaut touchait **418 énoncés** : N 102, E 122, A 194, soit un sur quatre.
Correctif en une ligne, vérifié sur document réduit puis dans le livre.

### Deux défauts trouvés en cherchant les équivalents en N et A

1. **Dessins 436 et 437 (classe A)** : le livre affichait « 1/2 **le Longueur**
   d'onde » et « **le Fréquence** perturbatrice ». Substitution mot à mot du
   14/08, `der` rendu par « le » sans accord ni minuscule. Pierre ne l'avait pas
   signalé.
2. **Le chevauchement du texte sur le circuit**, dans les quatre réponses
   illustrées de la question AF223. Il préexistait, un peu moins marqué ; la
   correction grammaticale, plus longue, l'a rendu criant. Corrigé en ancrant
   les libellés à l'est : le texte croît vers la gauche et ne peut plus
   atteindre le schéma, quelle que soit sa longueur.

### Ce que cette relecture a appris sur mes propres contrôles

**Mon audit du matin cherchait de l'ALLEMAND résiduel.** Les libellés « le
Longueur d'onde » n'en contiennent aucun : ils sont en français fautif, et
passaient donc au travers. Une seconde sonde, écrite après coup, cherche un
article français suivi d'un nom commun à majuscule ; elle sort 4 cas, tous en
classe A.

**Trois fois dans la journée, une conclusion tirée du SOURCE s'est révélée
fausse à l'écran** : le `rc=0` de `sonde_dessins.py` le matin, l'aide-mémoire du
dessin 666 qualifié à tort de défaut amont, et le chevauchement de AF223 que
l'extraction de texte ne montrait pas — `pdftotext` n'extrait rien de ces
quatre figures. La seule vérification qui tranche est **la page ouverte**.

### Résultats

N 258 p. · E 214 p. · A 376 p., pagination inchangée. Contrôles du §4 conformes
sur les trois, `??` à 0 · 1 · 3, aucune question coupée. Les pièces liminaires
portent désormais « du traducteur ».

### Édition combinée NEA — première compilation (15-16/08/2026)

**808 pages**, 384 sections, 1 751 questions, 805 dessins distincts. Contrôles du
§4 conformes du premier coup ; 4 références « ?? », soit les quatre orphelines
amont cumulées. Les compteurs de clamp s'additionnent proprement (948 figures,
10 tableaux, 7 formules) : aucun dessin n'est traité différemment en combiné.

Durée : environ 1 h 15 pour cinq passes, contre 50 min pour la classe A seule.

**Deux tirages.** Le premier, à l'ordre `N, E, A` et filigrane à plat, faisait
806 pages. Le définitif — ordre `A, E, N`, filigrane empilé — en fait **808** :
les deux pages d'écart viennent de `N_Ende`, dont la version A est plus longue
que celle de N (5 497 octets contre 5 224). C'est la seule différence de
contenu entre les deux, et elle est conforme à ce qu'on attendait. Vérifié
après coup par comparaison directe : le `N_Ende` composé dans le NEA est
identique à celui de la classe A, et différent de ceux de N et E.

### Ordre des `--translations` : `A` d'abord

Décision de Pierre : la version de la classe la plus avancée l'emporte. **La
portée du choix a été mesurée avant de trancher, et elle est étroite :**

- **une seule section** est traduite dans plusieurs classes — `N_Ende`
  (« Conclusion du cours »), présente dans les trois. C'est du contenu
  **français**, pas une traduction de l'amont : les trois versions renvoient
  chacune à l'examen de leur classe. La version N dit « il n'existe pas de
  premier échelon équivalent », la E « il n'existe pas d'échelons » et ajoute
  trois points du programme français sans équivalent allemand ;
- **20 dessins forkés** sont partagés entre classes, mais **tous identiques au
  contenu**. Deux d'entre eux, 354 et 935, sont sortis « différents » d'une
  comparaison par empreinte : ils ne diffèrent en réalité que par leurs fins de
  ligne, CRLF contre LF. L'ordre n'a donc aucun effet sur les dessins.

Un document de comparaison des trois versions de `N_Ende` a été produit pour
la décision, chaque version sur sa page avec sa classe en titre courant.

### `vorwort` n'est pas dans le NEA

La section est traduite (`traductions/N/sections/vorwort.md`) et figure dans le
livre N, mais le sommaire amont du NEA ne l'appelle pas : **l'édition combinée
perd l'avant-propos allemand**. C'est ce qui explique l'écart de comptage — 385
idents distincts traduits pour 384 sections composées — et c'est aussi
l'origine de l'avertissement « clé *vorwort* n'est pas un ident connu » émis
par `titles.json` à chaque compilation NEA.

### Filigrane de la page de titre — `build_book.py` v0.20

Relevé par Pierre : dans le bandeau de droite, « NEA » à plat est illisible. La
mesure sur épreuve a montré pire que « trop étroit » — **le N mordait sur la
zone blanche à gauche et le A était coupé au bord droit de la page**, alors même
que la v0.9 avait déjà réduit le corps à 105 pt.

L'ancien gabarit ne pouvait faire varier que le corps et le texte, jamais
l'ancrage ni la position : il était structurellement incapable de loger trois
lettres. Le nœud entier est désormais construit côté Python.

Trois dispositions ont été composées et comparées sur épreuve — à plat, pivotée
à 90°, empilée. **Pierre a retenu l'empilement** : une lettre par ligne, 150 pt,
centrées sur l'axe du bandeau et calées en haut. Chaque lettre reste lisible à
l'endroit. Une lettre seule ne change pas.

---


## SESSION 14/08/2026 — version a.2 (build_book.py v0.18)

Génération : 131/131 sections, 571 questions, 55 encarts, 30 dessins francisés.
**258 pages** (254 en a.1), 3,04 Mo après Ghostscript.

Contrôles du §4 : tous à 0. Clamps : 132 figures, 1 tableau, 0 formule.

| mesure | a.1 | a.2 |
| --- | ---: | ---: |
| plus grand débordement horizontal | 124,97 pt | **19,7 pt** |
| débordements > 20 pt | 1 | **0** |
| total `Overfull \hbox` | 41 | 46 |
| pages « Underfull \vbox » | 93 | **0** |
| questions séparées de leurs réponses | 19 relevées | **0 sur 571** |
| accolades imprimées dans le PDF | 12 | **0** |
| dessins affichant de l'allemand | 4 | **1** |

Les `Overfull \hbox` montent légèrement (41 → 46) : ce sont des lignes
justifiées un peu pleines, conséquence attendue du changement de césure. Aucune
ne dépasse 20 pt, contre une à 125 pt en a.1.

### Le code Morse — un défaut de contenu déguisé en défaut de mise en page

Le plus gros débordement de la classe, **124,97 pt (44 mm)**, venait du tableau
des caractères spéciaux : `[morse:correction]` était rendu par le mot
CORRECTION **épelé en trente symboles**, enfermé dans un `\mbox` insécable.
Cause : `renderer/morse.py` parcourt le texte caractère par caractère, ce qui
rend inatteignable toute clé de plus d'un caractère — alors que la table
contient bien `"correction": [8 points]`. Quatre des cinq lignes du tableau
étaient fausses (BK, AR, SK, Correction) ; seule `=` était juste, sa clé tenant
en un caractère. Corriger le contenu a fait disparaître le débordement.

Deux éléments relevés par Pierre **sur l'édition papier allemande** et absents
du dépôt numérique ont été rétablis : le **ß** sous le `ü` (figure 6.3) et le
**`=`** (figure 6.4). Cette dernière passe à sept lignes et réunit les deux
sources — le papier donne `=` à la place de `-` et ignore `@`, que le dépôt
possède. Seul endroit du projet, hors encarts `<france>`, où le contenu
français est volontairement plus complet que l'amont. Détail dans
`docs/defauts-amont.md` §4.

### Douze accolades imprimées depuis la a.1

`\emph{pas}` avait été écrit dans `questions.json`, qui traverse le renderer :
celui-ci échappe les accolades, et onze énoncés affichaient « ne devriez-vous
**{pas}** établir… », sans italique. Présent dans le PDF a.1 livré, jamais
relevé en relecture. Rétabli en markdown `*pas*`.

**Leçon de méthode, payée trois fois dans la journée** : les backslashes ne
survivent pas au passage par le shell. Un `python -c` a mangé un backslash sur
deux et cassé `questions.json` (`\*pas*` n'est pas un échappement JSON valide),
faisant échouer une compilation complète. Toute manipulation de LaTeX ou de
JSON passe désormais par un fichier de script.

## SESSION 10/08/2026 — compilation v0.9 définitive

- génération : 131/131 sections, 571 questions, 55 encarts « En France »,
  **zéro avertissement** (seule des trois classes dans ce cas)
- 3 passes : 250 p., 252 p., 252 p. stable — **rc=0 au premier tour**
- 0 « lost some margin notes », 0 « Float too large », 0 référence indéfinie
- Ghostscript `/ebook` : **3,17 Mo**
- **252 pages contre 256 en v0.6** : les 40 remplacements d'anglicismes
  (« émetteur-récepteur », plus long que « transceiver ») ont déplacé les
  coupures. Aucun contenu perdu — audit de dérive à 0 écart.

### Incident et récupération

Une commande erronée de ma part a supprimé `livraison/traductions-N/N`.
Récupération intégrale depuis le répertoire de travail. Contrôle effectué :
la source restaurée régénère **131 sections rigoureusement identiques** à celles
déjà compilées (0 différence). Rien n'a été altéré.

### Défaut cosmétique à instruire au chantier images

51 avertissements `Missing character ... in font nullfont` (42 points-virgules,
9 zéros), toujours au voisinage de l'inclusion d'un dessin TikZ. Même défaut en
classe E (304) et A (398). `nullfont` = caractères NON IMPRIMÉS. Cause non
établie ; à inspecter visuellement lors de la francisation des images.

### Règle de build

Le `gardien.sh` de sauvegarde des auxiliaires est réservé aux volumes LONGS
(classe A). Sur N et E il restaure un `.aux` périmé et provoque une oscillation
de pagination sans fin. Compiler N sans gardien, sur arbre purgé.

## SESSION 10/08/2026 (chantier 3) — AUDIT DE SOURÇAGE DES 55 ENCARTS

Audit systématique déclenché par la question de Pierre : « as-tu bien pensé à
toujours préciser tes sources ? ». Trois défauts trouvés, tous corrigés.

### DÉFAUT 1 (grave) — un décret ABROGÉ cité dans deux encarts

`elektromagnetische_vertraeglichkeit` et `recht_zum_selbstbau` s'appuyaient sur
le **décret n° 2006-1278**, abrogé par l'article 21 du décret n° 2015-1084 du
27 août 2015. Le fond de l'exclusion des équipements radioamateur est conservé,
mais **la lettre a changé** :

| rédaction abrogée (2006-1278) | rédaction EN VIGUEUR (2015-1084 modifié) |
| --- | --- |
| « non disponibles dans le commerce » | « à moins qu'ils ne soient **mis à disposition sur le marché** » |
| « ensembles de composants » | « **kits de composants** » |
| « équipements commerciaux modifiés à leur intention » | « équipements mis à disposition sur le marché et **modifiés par et pour les radioamateurs** » |

Dans un manuel d'examen, citer la formulation d'un texte abrogé n'est pas un
détail : c'est ce qui fait rater une question. Les deux encarts sont réécrits.

### DÉFAUT 2 — 23 élisions cassées, introduites par MOI la veille

Le remplacement automatique `transceiver` -> `émetteur-récepteur` (78 occurrences
le 09/08) n'a pas traité l'élision. Résultat : « **le** émetteur-récepteur »,
« **du** émetteur-récepteur », « **de** émetteurs-récepteurs ».

**37 occurrences au total sur les trois classes**, présentes dans les trois PDF
déjà livrés. Toutes corrigées (`l'émetteur-récepteur`, `de l'émetteur-récepteur`,
`d'émetteurs-récepteurs`).

**Règle : après tout remplacement lexical automatique, sonder les élisions.**
Motifs à tester : `\b(le|de|du|ce|que|ne|se|au) ` suivi d'une voyelle.
Attention aux faux positifs légitimes : « diode émetteur-base » dans
`transistor_1` n'est pas concerné.

### DÉFAUT 3 — une copie de livraison désynchronisée

`livraison/traductions-A/A` datait d'une copie antérieure et n'avait pas reçu les
corrections. La source de vérité pour la classe A est `travail-A/` ; la copie de
livraison doit être refaite juste avant la mise en archive, jamais avant.

### Textes vérifiés et CONFIRMÉS en vigueur

| texte | statut |
| --- | --- |
| loi n° 66-457 du 2 juillet 1966, art. 1er | en vigueur au 19/06/2026. Rédaction issue de mars 2014 confirmée : « antennes individuelles, émettrices et réceptrices, nécessaires au bon fonctionnement de stations du service amateur autorisées conformément à la réglementation en vigueur ». Date et attribution exactes dans `antennen_baurecht_haftung`. |
| décret n° 2002-775 | consolidé, en vigueur au 10/08/2026 |
| décision ARCEP n° 2012-1241 | annexe réécrite par la décision n° 2019-1412 (JORF 13/02/2020) |
| décret n° 2015-1084 | en vigueur au 25/07/2026 |
| décret n° 2024-1023 | applicable aux demandes déposées depuis le 01/12/2024 |

### Chiffres NON sourcés mais CORROBORÉS

Les valeurs des encarts `aequivalente_isotrope_strahlungsleistung_eirp_1`,
`amateurfunkbaender`, `iaru_bandplan_2m` et `effektive_strahlungsleistung_erp_1`
(1 W PIRE, 15 W sur 60 m, 120 W au-dessus de 50 MHz, 10 W classe 3, seuil de
déclaration à 5 W PAR) concordent avec l'annexe consolidée lue en séance.
Elles sont exactes ; il leur manque seulement la citation du texte.

### RESTE À VÉRIFIER (non fait, faute de temps)

- **`gebuehren_beitraege` : le montant de 46 €.** Non vérifié, et c'est le type
  de valeur qui change d'une année à l'autre. À contrôler avant publication.
- décret n° 67-1171 modifié par le décret n° 93-533 (procédure LRAR
  d'information du propriétaire) — plausible, non vérifié.
- arrêté du 23 avril 2012 (suppression de l'épreuve de télégraphie).
- décret n° 2014-1621 du 24 décembre 2014 (compétences ANFR).

### Enseignement de méthode

Les deux erreurs de sourçage de la journée — l'article 4 pour l'indicateur de
puissance, et le décret 2006-1278 — viennent du **même geste** : citer un texte
à travers un autre texte qui le cite, sans remonter à la source. Les textes
consultés directement (décret 2002-775, annexe 2019-1412) étaient justes.
**Un texte cité de seconde main doit être vérifié à la source avant publication.**
