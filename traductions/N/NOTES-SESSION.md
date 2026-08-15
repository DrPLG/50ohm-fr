
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
