# Livre N français — compte rendu d'intégration v0.6

Session du 7 août 2026. Réconciliation des 21 encarts « En France » rédigés le
6 août avec les 51 encarts en place, correction de deux erreurs de droit,
première compilation avec la chaîne typographique complète.

Remplace le compte rendu du 28 juillet (v0.5).

## 1. Ce qui a été fait

- Vérification préalable de l'archive reçue : 131 sections pour 131 idents,
  571 questions, 14 chapitres et abstracts, 131 titres de sections, 51 encarts.
- **Réconciliation, et non insertion.** Sur les 21 idents visés par le nouveau
  lot, **17 portaient déjà un encart**. Chaque cas a été arbitré séparément
  (document `arbitrages-encarts-N.md`, 22 points) : 14 fusions, 2 remplacements,
  4 ajouts nets, 1 déplacement de tableau entre sections.
- Total après fusion : **55 encarts** dans 55 sections, 55 balises ouvrantes
  pour 55 fermantes.
- Génération : 131 sections, 571 questions traduites, 55 encarts rendus,
  **zéro avertissement de validation** (aucun marqueur non rendu, aucune
  référence orpheline, aucune clé de `titles.json` invalide).
- Validation structurelle contre la source allemande : **131/131 sections,
  marqueur pour marqueur, décompte et ordre — 100 %**. Les blocs `<france>` et
  les lignes commentées par `%` sont exclus de la comparaison ; les clés
  `[index:…]` sont comparées en présence et en ordre seulement, leur contenu
  étant traduit.
- Sonde anti-germanismes sur les 21 corps modifiés : **0 occurrence**.
- Compilation `latexmk` : **rc=0, 251 pages, aucune erreur LaTeX, zéro parasite
  « „, », zéro référence non résolue à la passe finale, zéro « ?? » dans le PDF**.
- Compression Ghostscript `/ebook` : 299 Mo → **3,2 Mo**.

## 2. Deux erreurs de droit corrigées

Les deux figuraient dans les encarts du lot du 28 juillet et ont été établies
sur Légifrance au 7 août 2026.

**a) `rufzeichenaufbau` — annexe IV → annexe II.** L'encart renvoyait à
« l'annexe IV de l'arrêté du 21 septembre 2000 modifié » pour la grille de
codification. L'arrêté du 2 mars 2021 a réécrit l'article 7 pour viser
l'**annexe II**, et a **supprimé les annexes III et IV**. Même texte modificatif
que la correction déjà consignée sur le fondement de l'attribution (adresse et
position géographique de la station déclarée, et non plus domicile fiscal) :
l'encart portait encore l'état antérieur du droit.

**b) `antennen_baurecht_haftung` — le droit à l'antenne couvre l'émission.**
L'encart affirmait que la loi n° 66-457 du 2 juillet 1966 ne vise que la
réception et que les antennes d'émission du service d'amateur « ne bénéficient
d'aucun droit automatique ». C'est l'inverse. L'article 1er, dans sa rédaction
issue de l'ordonnance n° 2014-329 du 12 mars 2014, interdit au propriétaire d'un
immeuble de s'opposer, sans motif sérieux et légitime, à l'installation, au
remplacement ou à l'entretien des antennes individuelles **émettrices et
réceptrices** nécessaires au bon fonctionnement des stations du service d'amateur
autorisées. L'article 4 étend le bénéfice de la loi à l'indivision et à la
copropriété ; le décret n° 67-1171 modifié par le décret n° 93-533 vise nommément
l'antenne émettrice et réceptrice d'une station d'amateur dans sa procédure
d'information du propriétaire.

La rédaction retenue conserve la nuance de portée : ce droit règle le rapport
entre l'occupant et le propriétaire de l'immeuble ; il ne crée rien d'opposable
aux voisins ni à la commune, et ne dispense d'aucune formalité d'urbanisme.

Une troisième correction, plus légère : `buchstabiertafel` écrivait « Alpha »,
alors que la graphie de l'UIT est **Alfa** — précisément l'un des quatre pièges
que le nouvel encart apprend à éviter.

## 3. La réserve typographique est levée

Les compilations précédentes se faisaient dans un conteneur dépourvu de
`texlive-fonts-extra` : Libertinus, Source Sans/Serif, FontAwesome et MnSymbol
étaient remplacés par des stubs, et **la typographie des PDF livrés n'était pas
la bonne**. Cette fois, la chaîne complète a été installée. Le PDF embarque
LibertinusSerif, LibertinusMath, LibertinusMono, SourceSerifPro (régulier, gras,
italique, gras italique), SourceSansPro et FontAwesome5Free.

C'est donc **le premier PDF de ce projet dont la mise en page est celle qui sera
imprimée**. Il explique aussi l'essentiel de l'écart de pagination avec la
v0.5 — 207 pages en polices de substitution, 251 pages en polices réelles ; les
quatre encarts ajoutés et l'allongement des dix-sept fusionnés ne pèsent qu'une
poignée de pages dans ce total.

## 4. Correction de `rst.md` appliquée

Le `[photo:…][index:…]` concaténé sur une seule ligne — défaut amont préservé
verbatim jusqu'ici — a été scindé en deux lignes côté français. Le compte
d'avertissements de génération passe de 1 à 0, la photo du S-mètre de l'IC-9700
est revenue, et l'unique « ?? » du livre a disparu. Le dépôt amont n'est pas
touché ; le défaut reste consigné dans `docs/defauts-amont.md`.

## 5. Décisions de structure prises pendant la fusion

- **Tableaux.** Les 21 encarts reçus utilisaient le Markdown standard avec ligne
  de séparation `| --- |`. DARCdown déclare l'alignement par préfixe dans la
  ligne d'en-tête (`| l: Bande | X: Puissance |`) et **n'utilise pas de ligne de
  séparation** — 42 en-têtes du corpus le confirment, aucune ligne de tirets.
  Les dix tableaux ont été convertis ; il ne reste aucune ligne de séparation
  dans les 131 sections.
- **Titres et ton.** Les nouveaux encarts ont été alignés sur la convention en
  place : titre de niveau 1 en français courant, sans préfixe « En France », et
  une phrase d'accroche adressée au lecteur.
- **Doublons résorbés.** Le tableau des territoires a été déplacé de
  `rufzeichenaufbau` vers `internationale_landeskenner`, sous sa forme
  « préfixe complet » (FG, FM, FY…), qui est celle que le lecteur entend sur
  l'air. Le tableau des puissances par bande n'a **pas** été dupliqué dans
  `sendeleistung_klasse_n` : il existe déjà dans `amateurfunkbaender`, et
  l'encart y renvoie. Le contenu « conformité et marquage CE » de `zulassung`,
  qui faisait double emploi avec `recht_zum_selbstbau`, a été consolidé dans ce
  dernier ; `zulassung` porte désormais l'encart sur la classe unique HAREC.

## 6. Réserve de rédaction sur `itu_regionen`

L'encart reçu proposait un tableau comparatif de cinq bandes entre région 1 et
région 2, dont 50 à 54 MHz en statut primaire et 144 à 148 MHz. Ce sont les
attributions du Règlement des radiocommunications ; **je n'ai pas pu confirmer
que la colonne « région 2 » de l'annexe de la décision ARCEP les reprend telles
quelles**. Le tableau retenu est donc limité aux lignes adossées à une source
vérifiée : 160 m et 40 m, déjà affirmées dans l'encart en place, et
220 à 225 MHz, attribué en région 2 seulement, mentionné dans l'encart
`amateurfunkbaender`. L'exemple du QSO sur 3950 kHz depuis la Martinique, qui
supposait 3500 à 4000 kHz en région 2, a été remplacé par un exemple sur
1900 kHz depuis la Guadeloupe, adossé au 160 m.

À vérifier sur le texte de l'annexe si tu veux compléter le tableau.

## 7. Ce qui n'a pas été traité

Les trois sujets volontairement écartés faute de vérification suffisante le
restent, et aucun encart n'a été rédigé à leur sujet :
`fernmeldegeheimnis_abhoerverbot` (articulation liberté d'écoute / secret des
correspondances), les servitudes de protection des centres radioélectriques
(la « règle des 1000 mètres » ne vaut que pour certaines catégories de stations
protégées), et `gebuehren_beitraege` (régime des taxes et véhicule législatif de
la suppression de la taxe annuelle sur l'indicatif).

## 8. Amont

Comparaison effectuée jusqu'au 7 août 2026. `toc/N.json`, le catalogue de
questions et les métadonnées sont inchangés ; aucune figure utilisée par la
classe N n'a bougé ; le répertoire `latex/` est inchangé. Une seule section N
modifiée en amont, `betriebsabwicklung` — correction d'un participe passé
allemand, sans incidence sur la traduction française. Cette section reçoit par
ailleurs l'un des quatre encarts ajoutés. Le parseur `renderer/image.py` n'a pas
bougé : le défaut des deux-points dans les légendes subsiste, et
`docs/issue-darc-legendes.md` garde son objet.

## 9. Version et outillage

PDF étiqueté **v0.6** sur sa page de titre.

`build_book.py` reste à la **v0.8** : la balise `<france>` date de la v0.5, et
les v0.7 (validation des chemins) comme v0.8 (repli symlink Windows) n'ont aucun
effet sur le rendu. Aucune montée de version du script n'était nécessaire.

**L'archive de livraison ne contient pas de `build_book.py`.** L'exemplaire
présent dans le zip reçu était une v0.6 ; la compilation a été faite avec lui,
au rendu identique, mais l'inclure dans la livraison aurait écrasé ta v0.8 par
une version antérieure. Conserve ta v0.8.
