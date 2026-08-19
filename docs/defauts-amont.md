# Défauts constatés dans les sources amont

Registre annoncé par le §6 de `CLAUDE.md` (« Défauts amont : préservés et
documentés, jamais corrigés silencieusement ») et par le `README`. Créé le
14/08/2026.

Chaque entrée décrit un défaut de la source allemande, l'effet observé, et ce
qui a été fait côté français. **Rien n'est corrigé en amont, et rien n'est
corrigé silencieusement côté français.** Ces défauts font l'objet d'un
signalement au DARC, rédigé en allemand.

Le §8 de `CLAUDE.md` porte un relevé antérieur (labels dupliqués, deux-points
dans les légendes, `\tikzstyle` déprécié, coquilles). Il reste à migrer ici ;
il n'a pas été recopié tel quel faute d'avoir été revérifié un par un.

---

## 1. Référence orpheline `a_zeppelinantenn` — `antennenformen_3`

**Constaté le** 14/08/2026, sur l'instantané amont du même jour.

La section `contents/sections/antennenformen_3.md` écrit :

```
On parle alors d'une *Zeppelinantenne* (vgl. Abbildung[ref:a_zeppelinantenn]).
```

alors que le dessin est déclaré quelques lignes plus bas sous l'ident
`a_zeppelinantenne`, avec le `e` final :

```
[picture:314:a_zeppelinantenne:Aufbau einer Zeppelinantenne]
```

Deux défauts distincts sur la même ligne : l'ident tronqué, et l'espace
manquant entre `Abbildung` et `[ref:`.

**Effet.** `build_book.py` lève « référence orpheline (\ref sans \label) » et
la référence sort en `??` dans le PDF. Le livre allemand est touché à
l'identique.

**Côté français.** L'ident est préservé verbatim, conformément au §6 qui impose
de conserver les idents « y compris les fautes d'orthographe allemandes
d'origine ». L'espace manquant, lui, relève de la typographie de la prose et
non de l'ident : la traduction écrit `cf. figure [ref:a_zeppelinantenn]` avec
l'espace normal.

**Conséquence de contrôle.** Le nombre de `??` attendus dans le PDF de la
classe A passe de 2 à 3. Le tableau du §4 de `CLAUDE.md` a été mis à jour.

---

## 2. Caractère accentué nu en mode mathématique — `antennenformen_3`

**Constaté le** 14/08/2026.

La même section écrit le rapport de transformation d'un transformateur ainsi :

```
mit einem Übersetzungsverhältnis von $ü = 1:7$
```

Le `ü` est placé **nu en mode mathématique**. LuaLaTeX le compose alors dans
l'italique mathématique (`cmmi8`), qui ne possède pas ce glyphe.

**Effet.** Le journal signale `Missing character: There is no ü (U+00FC) in
font cmmi8!` et **le caractère disparaît du PDF** : le lecteur lit
« rapport de transformation de = 1:7 ». Vérifié par extraction du texte du PDF
compilé. Le livre allemand est touché à l'identique.

**Côté français.** ~~Formule préservée verbatim.~~ **Corrigé le 15/08/2026, sur
décision de Pierre**, qui assume la dérogation à la règle « formules `$…$`
verbatim » du §5.

### L'ampleur réelle, mesurée le 15/08/2026

Ce défaut ne touchait pas une section mais **cinq**, pour **18 occurrences** —
comptées au journal de compilation, qui est ici la mesure la plus sûre :
`Missing character: There is no ü (U+00FC)` sort **17 fois en classe A et 5 fois
en classe E**.

| section | classe | occurrences |
| --- | --- | ---: |
| `uebertrager_2` | A | 10 |
| `uebertrager_1` | E | 4 |
| `antennenformen_3` | A | 2 |
| `brueckengleichrichter` | A | 1 |
| `mantelwellen_2` | A | 1 |

Le cas le plus grave n'était pas celui qui avait été relevé. Dans
`uebertrager_2`, c'est **la formule centrale du chapitre sur les
transformateurs** qui s'imprimait sans son membre de gauche :

```
Dans la classe E, nous avons déjà rencontré la formule du rapport de transformation :
    𝑁𝑃   𝑈𝑃  ==
    𝑁𝑆   𝑈𝑆
```

Et dans `antennenformen_3`, le texte donnait « un transformateur ayant un
rapport de spires **()** de 1:7 » — deux parenthèses vides.

### Ce qui a été fait

Le symbole `ü` (pour *Übersetzungsverhältnis*) est remplacé par **`m`**,
notation française du rapport de transformation. Le remplacement n'a eu lieu
**que dans les spans `$…$`** : hors de là, les `ü` restent verbatim comme
l'impose le §6 — un commentaire allemand (`% TODO: … prüfen`) et l'ident de
photo `Brückengleichrichter` sont intacts, ce que le script vérifie avant
d'écrire.

La décision est cohérente avec celle prise le même jour sur les dessins 260,
303 et 315, où le même symbole était composé en mode texte : il y survivait,
mais aurait laissé un livre dont les figures disent « m » et le texte rien.

**Le livre allemand reste affecté** — le `ü` y disparaît toujours, dans les
cinq sections. À signaler au DARC : c'est le défaut de ce registre qui touche
le plus de pages.

**À noter** : c'est la démonstration du mécanisme derrière la règle du §6
(« jamais d'accent dans `\mathrm{}` »), avec une frontière plus précise que
celle qui y est écrite. Un accent placé dans `\mathrm{}` ou `\text{}` **passe**
sans dommage, ces macros basculant sur une police de texte qui possède les
glyphes accentués ; c'est le caractère accentué **nu**, composé en italique
mathématique, qui disparaît.

---

## 3. `\qty{0.05}{\lambda}` — unité composée d'une macro mathématique

**Constaté le** 14/08/2026, dans `antennenformen_3` (contenu ajouté en amont
après notre traduction initiale).

```
oder ein Teil der koaxialen Zuleitung (mindests $\qty{0.05}{\lambda}$)
```

`\lambda` est passé à `siunitx` comme **unité**. siunitx la compose dans la
police de texte droite, où le glyphe U+1D706 (lambda mathématique) est absent
de Libertinus Serif.

**Effet.** `Missing character: There is no 𝜆 (U+1D706) in font
[LibertinusSerif-Regular.otf]` et **le lambda disparaît du PDF** : le lecteur
lit « au moins 0,05 », sans unité, ce qui ne veut rien dire. Vérifié par
extraction du texte. siunitx convertit par ailleurs correctement `0.05` en
`0,05` en français.

Même famille que le `\qty{120\pi}{\ohm}` du §8, contourné en v0.14 de
`build_book.py` par `fix_latex()`.

**Côté français. Contourné en v0.16 de `build_book.py`**, sur décision de
Pierre du 14/08/2026 et sur le modèle de la v0.14 :

```python
text = re.sub(r"\\qty\{([0-9.,]+)\}\{\\lambda\}", r"\\num{\1}\\,\\lambda", text)
```

`\num{}` est conservé plutôt que le nombre brut : c'est lui qui rend la virgule
décimale française. **La source amont n'est pas touchée** — la correction vit
dans le générateur, comme pour la v0.14. Vérifié après coup : zéro
« Missing character U+1D706 » au journal, et le PDF affiche « au moins
0,05 λ ». Le livre allemand, lui, reste affecté.

Coquille associée dans la même parenthèse : `mindests` pour `mindestens`.

## 4. `[morse:…]` — les clés multi-caractères sont inatteignables

**Constaté le** 14/08/2026, dans `morsetelegrafie` (classe N), à partir d'une
vérification de Pierre sur **l'édition papier allemande** du livre.

Il ne s'agit pas d'un défaut de contenu mais d'un **défaut du générateur** :
`renderer/morse.py`. La table de conversion contient bien les prosignes,
lignes 74 à 77 :

```python
"ar": [dit, dah, dit, dah, dit],
"bk": [dah, dit, dit, dit, dah, dit, dah],
"sk": [dit, dit, dit, dah, dit, dah],
"correction": [dit, dit, dit, dit, dit, dit, dit, dit],
```

Mais la conversion parcourt le texte **caractère par caractère** :

```python
for char in text:
    if char.lower() in morse_code:
        result.append(morse_code[char.lower()])
```

Aucune clé de plus d'un caractère ne peut donc être atteinte. `[morse:bk]`
n'est pas lu comme la clé `bk` : il est épelé `b` puis `k`.

**Effet.** Quatre des cinq lignes du tableau des caractères spéciaux
(`n_morsetelegrafie_morsecode_spezial`, figure 6.5) sont fausses, **sans
aucun avertissement de compilation** :

| ligne | rendu | ce que c'est | valeur correcte |
| --- | --- | --- | --- |
| Interruption (BK) | `-... -.-` | B puis K épelés | `-...-.-` |
| Séparation (BT, =) | `-...-` | — | correct |
| Fin du passage (AR) | `.- .-.` | A puis R épelés | `.-.-.` |
| Fin de l'émission (SK) | `... -.-` | S puis K épelés | `...-.-` |
| Correction | `-.-. --- .-. .-. . -.-. - .. --- -.` | le mot CORRECTION épelé | `........` |

Seule la ligne `=` est juste, parce que sa clé tient en un caractère.

**Effet de bord de mise en page.** La séquence « CORRECTION » épelée est
enfermée dans un `\mbox` insécable, dans un tableau à colonnes de largeur
naturelle : elle débordait de **124,97 pt** (44 mm) hors de la colonne de
texte — le plus gros débordement horizontal de toute la classe N, et l'origine
du relevé de Pierre « page 124 : le code morse pour Correction apparaît-il
complet ? ». Il n'apparaissait pas complet. Corriger le contenu a fait
disparaître le débordement : plus aucun `Overfull \hbox` dans la section.

**Deux éléments présents au papier et absents du dépôt numérique**, relevés
par Pierre sur la même page :

- figure 6.3 (lettres) : le **ß** figure sous le `ü` ; la case correspondante
  est vide dans le dépôt. La clé `ß` existe pourtant dans la table
  (`[dit, dit, dit, dah, dah, dit, dit]`) ;
- figure 6.4 (chiffres et ponctuation) : le **`=`** est donné ; il est absent
  du dépôt. La clé existe également. À noter que le papier et le dépôt
  divergent dans les deux sens sur cette figure : le papier donne `=` **à la
  place** du `-`, et ne comporte ni `-` ni `@`, que le dépôt numérique a.

**Écart volontaire assumé sur la figure 6.4.** Sur décision de Pierre du
14/08/2026, l'édition française **réunit les deux sources** plutôt que d'en
suivre une : elle conserve `-` et `@` (du dépôt) et ajoute `=` (du papier),
soit sept signes de ponctuation contre six de chaque côté. La figure passe de
six à sept lignes. C'est le seul endroit du projet où le contenu français est
volontairement plus complet que l'amont, hors encarts `<france>`.

**Côté français.** Corrigé le 14/08/2026 dans
`traductions/N/sections/morsetelegrafie.md`, **sans montée de version du
générateur** : les cellules DARCdown acceptent du LaTeX brut, on y écrit donc
directement les prosignes.

```
| Fin du passage (AR) | \MorseDit\MorseDah\MorseDit\MorseDah\MorseDit |
```

**Piège, payé d'une compilation complète.** Le renderer laisse passer le
**backslash** mais **échappe les accolades** : `\mbox{\MorseDah{}}` ressort en
`\mbox\{\MorseDah\{\}\}` et les accolades **s'impriment littéralement** dans le
PDF. Il faut donc écrire les macros **sans accolades ni `\mbox`** —
`\MorseDit`, `\MorseDah` et `\MorseCharSep` ne prennent aucun argument
(`settings.tex` lignes 840-844), les `{}` du rendu amont ne sont que des
séparateurs de tokens. Le `\mbox` est inutile ici : la colonne du tableau est
de largeur naturelle et ne coupe pas.

**Contrôler sur le PDF, pas sur le `.tex`.** Une vérification qui cherchait les
noms `MorseDit`/`MorseDah` dans le `.tex` les trouvait dans `\MorseDah\{\}` et
décodait un signal parfaitement correct, alors que le rendu était cassé. Elle
mesurait la présence des macros, pas la validité du code. Même piège que le
clamp `\DARCimage` de la v0.12, dont la mesure était structurellement
constante : une vérification doit porter sur le résultat, jamais sur un
intermédiaire.

Les valeurs employées sont exactement celles de la table amont — on ne corrige
pas le contenu du DARC, on rétablit ce que son propre générateur aurait dû
produire. Le `ß` est rétabli par `[morse:ß]`, qui fonctionne (clé d'un seul
caractère). **La source amont n'est pas touchée** ; le livre allemand, lui,
reste affecté — édition numérique comme papier pour les prosignes.

**À signaler au DARC** : c'est le seul des quatre défauts de ce registre qui
porte sur le générateur et non sur les contenus, et il se corrige en une ligne
(itérer sur les clés avant d'itérer sur les caractères).

---

## 5. ~~Libellés tronqués dans le dessin 666~~ — ENTRÉE RETIRÉE

**Écrite le 15/08/2026, retirée le même jour. Elle était fausse.**

J'avais consigné ici que le dessin 666 portait deux libellés « tronqués de leur
première lettre » — « node » pour *Anode*, « athode » pour *Kathode* — et
proposé de le signaler au DARC.

Ce n'est pas un défaut. C'est un **aide-mémoire délibéré** : les traits rouges
du dessin tracent un **A**, que le texte « node » complète en *Anode* ; les
traits bleus tracent un **K**, que « athode » complète en *Kathode*. Le lecteur
lit le mot en suivant le tracé. Le procédé est intentionnel.

L'erreur vient de la même source que celle du matin : une conclusion tirée du
**source** sans jamais regarder la figure composée. C'est Pierre qui a signalé
« absence de "a" au mot anode » en relisant le PDF, ce qui a conduit à ouvrir
la page et à comprendre le mécanisme.

L'entrée est conservée sous cette forme plutôt que supprimée, pour que la
prochaine lecture du dessin 666 ne refasse pas le même chemin.

**Ce qui reste vrai** : notre fork français avait bien produit « CCathode », un
mot d'aucune langue, par application successive de `Kathode` → `Cathode` puis
`athode` → `Cathode`. C'est notre défaut, pas celui de l'amont ; il est corrigé.
Le mécanisme de l'aide-mémoire, lui, ne survit pas au passage au français : le
**A** fonctionne encore (*Anode* s'écrit pareil), le **K** ne donne pas
*Cathode*. Décision de Pierre du 15/08/2026 (feuille nº 4, C3a) : écrire les
deux mots en entier et renoncer à l'aide-mémoire.

## 6. `\qty{5}{8}\lambda` — une fraction tapée en `\qty`, la barre disparaît

**Constaté le** 16/08/2026, pendant la resynchronisation amont, dans la légende
du dessin 650 appelé par `elektrische_verlaengerung_verkuerzung` (classe A) :

```
[picture:650:a_5_8_lambda:$\qty{5}{8}\lambda$-Vertikalantenne]
```

`\qty{5}{8}` passe **« 8 » comme unité** du nombre 5. L'auteur voulait
manifestement `\frac{5}{8}` : le dessin s'appelle `a_5_8_lambda`, et **le corps
de la même section écrit partout `$\frac{5}{8}\lambda$`** (trois occurrences).
Seule la légende porte la coquille.

**Effet, mesuré sur document réduit et extraction du PDF le 16/08/2026** : la
compilation **réussit sans erreur**, et la légende compose **« 58λ »** — les
deux chiffres accolés, barre de fraction perdue. Le lecteur lit « antenne
verticale 58 λ ». Le rendu correct, obtenu avec `\frac{5}{8}\lambda`, donne
bien le 5 sur le 8.

Même famille que les §3 et §8 (une macro mathématique là où siunitx attend
autre chose), avec la même signature : **aucune erreur, un rendu faux**. Le
livre allemand est affecté à l'identique.

**Côté français : les deux voies à la fois, décision de Pierre du 16/08/2026.**

1. **Règle `fix_latex()` en v0.21 de `build_book.py`**, sur le modèle des v0.14
   et v0.16 : `\qty{<nombre>}{<nombre>}` → `\ensuremath{\frac{...}{...}}`. La
   source amont n'est pas touchée ; la correction vit dans le générateur et
   couvre donc aussi tout cas futur, y compris hors de nos traductions.
   `\ensuremath` et non `\frac` nu : `\qty` s'emploie aussi hors mode
   mathématique, où un `\frac` nu ferait échouer la compilation. Vérifié dans
   les deux modes sur document réduit.
2. **Légende française écrite directement en `$\frac{5}{8}\lambda$`**, sur le
   modèle de la dérogation « ordre / *Ordnung* » du 15/08/2026. La règle ne
   mord donc pas sur notre source — elle est la ceinture, la légende corrigée
   est les bretelles. `verifier_traduction.py` signale l'écart de formule avec
   l'amont, et c'est normal.

### L'élargissement demandé, et pourquoi il s'arrête là

Pierre a demandé d'étendre la correction « aux autres cas ». Le corpus entier
(amont et traductions, sections et dessins) a donc été balayé à la recherche
des `\qty{}{}` dont l'unité n'en est pas une. Quatre familles, **dont deux
seulement composent faux** — mesuré sur document réduit et extraction du PDF :

| famille | exemple | occurrences | rendu | verdict |
| --- | --- | ---: | --- | --- |
| unité **numérique** | `\qty{5}{8}` | 1 | « 58 » | **cassé**, traité en v0.21 |
| unité **macro** | `\qty{0.625}{\lambda}` | 7 | « 0,625 » | **cassé**, déjà v0.16 |
| unité **vide** | `\qty{30}{}` | 5 | « 30 » | sain, identique à `\num{30}` |
| unité en **texte nu** | `\qty{10}{dB}` | 71 | « 10 dB » | sain, identique à `\decibel` |

Les 71 occurrences de la dernière famille sont réparties dans 25 dessins
(`\qty{0,3}{V}`, `\qty{-5}{dBm}`, `\qty{25}{A}`…). **Les convertir en macros
siunitx n'aurait rien corrigé** — le rendu est déjà bon — **et aurait touché
des dessins déjà livrés**. Elles restent en l'état, et c'est un choix mesuré,
non une omission.

Le balayage a aussi confirmé que la règle v0.16 couvre bien les quatre
`\qty{...}{\lambda}` apparus le 14/08 dans `elektrische_verlaengerung_verkuerzung`,
plus les deux de `antennenformen_2` en classe E : rien à ajouter de ce côté.

## 7. Label dupliqué `a_richtkoppler_rechts_links` — dessins 1109 et 1110

**Constaté le** 16/08/2026 dans `swr_meter_2` (classe A), section entièrement
réécrite en amont le même jour.

```
[picture:1109:a_richtkoppler_rechts_links:Richtkoppler, die Welle läuft von links nach rechts]
[picture:1110:a_richtkoppler_rechts_links:Richtkoppler, die Welle läuft von rechts nach links]
```

**Deux figures différentes déclarent le même label.** Le texte y renvoie
pourtant deux fois, une fois pour le sens gauche-droite et une fois pour le
sens droite-gauche : les deux `[ref:]` résolvent nécessairement vers le même
numéro de figure, et l'une des deux renvoie le lecteur vers la mauvaise
illustration.

Même famille que les 20 labels dupliqués du §8 de `CLAUDE.md`, mais ici les
deux déclarations sont **dans la même section**, ce qui rend la collision
certaine — elle ne dépend pas de l'édition compilée.

Préservé verbatim côté français, légendes traduites.

## 8. Dessins 1135 et 1136 — ajoutés puis jamais appelés

**Constaté le** 16/08/2026. Les deux dessins ont été ajoutés à
`contents/drawings/` dans la même salve que les 1103 à 1112 et 1134, 1137,
1138, mais **aucune section, aucune diapositive ne les référence**. Ils ne sont
donc composés dans aucun livre.

Sans effet sur nous ; signalé pour que le DARC sache que deux figures produites
ne servent à rien — ou qu'un appel a été oublié.

## 9. Coquilles relevées pendant la resynchronisation du 16/08/2026

Toutes dans des sections réécrites en amont les 14, 15 et 16/08.

| section | écrit | attendu |
| --- | --- | --- |
| `swr_meter_2` | `Zu nächst` | `Zunächst` |
| `swr_meter_2` | `misst hierzu die  die Ausgangsspannungen` | « die » en double |
| `swr_meter_2` | `gemessern` | `gemessen` |
| `elektrische_verlaengerung_verkuerzung` | `Eine von mehreren Möglichkeit` | `Möglichkeiten` |
| `fusspunktimpedanz_2` | `Fußpolimpedanz` (légende) | `Fußpunktimpedanz` |
| `strom_spannung_speisung_2` | `Freqeuenzen` | `Frequenzen` |
| `strom_spannung_speisung_2` | `eine möglichkeit` | `Möglichkeit` |
| `nvis` | `Weitere Informationen indest du` | `findest` |
| `wellenwiderstand` | `Ausbreitungsgeschwingkeit` (tableau) | `Ausbreitungsgeschwindigkeit` |
| `impedanztransformation` | `aus dem Vorherigen Abschnitt` | `vorherigen` |
| `strom_spannung_speisung_1` | `verschiedneen` (légende) | `verschiedenen` |

La dernière est ancienne et **corrigée en amont** dans la nouvelle version de
`strom_spannung_speisung_2`, mais subsiste dans `strom_spannung_speisung_1`.

## 11. Coefficient de vélocité donné en pourcent — `wellenwiderstand`

**Constaté le** 16/08/2026 dans le tableau `a_rg58`, ajouté en amont le 15/08 :

```
| Ausbreitungsgeschwingkeit    | $\qty{0,66}{\percent}$                |
```

Ce n'est pas une coquille de frappe mais une **erreur d'unité d'un facteur
cent**. Le coefficient de vélocité d'un RG-58 vaut $0{,}66$, soit $66\,\%$ de
la vitesse de la lumière. Écrit `\qty{0,66}{\percent}`, il compose
« $0{,}66\,\%$ » — cent fois trop peu, et le lecteur qui s'y fie calculerait
une longueur électrique absurde.

La ligne voisine du même tableau donne d'ailleurs la valeur correcte sous une
autre forme dans le corps du texte, et le reste de la section est juste.

**Préservé verbatim côté français**, conformément au §8 de `CLAUDE.md` : c'est
une erreur de contenu, pas un défaut de rendu, et la corriger reviendrait à
réécrire l'amont. À signaler au DARC — c'est, de tous les défauts relevés ce
jour, celui qui peut réellement induire un candidat en erreur.

## 10. Renommage de label incomplet — `[ref:e_stromverteilungen]` orpheline en A

**Constaté le** 16/08/2026 dans `strom_spannung_speisung_2` (classe A), lors du
refactor amont du 15/08.

L'amont a **renommé le label du dessin 1050** dans cette section, de
`e_stromverteilungen` à `a_stromverteilungen` — un bon correctif, qui supprime
une collision avec `strom_spannung_speisung_1` (classe E), laquelle déclare le
même dessin sous le label `e_`. C'est l'un des 20 labels dupliqués du §8 de
`CLAUDE.md`, et nos propres notes de la classe A le recensaient déjà.

**Mais le `[ref:]` de la première phrase n'a pas suivi** : il pointe toujours
vers `e_stromverteilungen`.

Conséquence, vérifiée sur les sommaires amont : `strom_spannung_speisung_1`
**n'est pas dans le sommaire de la classe A**. Dans le livre A seul, le label
`e_stromverteilungen` n'est donc déclaré nulle part, et la référence pend —
**un `??` de plus, qui ferait passer la classe A de 3 à 4**. Les éditions EA et
NEA, qui contiennent les deux sections, s'en tirent : la référence y résout
vers la figure de la classe E, qui est le même dessin 1050.

Le refactor a donc **déplacé** le défaut plutôt que de le supprimer : la
collision de label disparaît, une référence orpheline apparaît. Le livre
allemand de la classe A est affecté.

**Côté français : renommage adopté sur les DEUX lignes** — le `[picture:]` et
le `[ref:]` — en application de la décision D2 de la feuille d'arbitrage nº 5
(Pierre, 16/08/2026), qui portait précisément sur « deux lignes à changer dans
notre fichier A ». C'est une **dérogation assumée à la règle « marqueurs
identiques à l'amont »** du §5 : `verifier_traduction.py` la signale, et c'est
normal. Sans elle, nous importerions un `??` que l'amont vient de créer.

## 12. Trois coquilles du relevé, corrigées en amont sans signalement

**Constaté le 19/08/2026**, en resynchronisant sur `07f3c861`. Ces trois
entrées **sortent du relevé** : elles n'existent plus en amont.

| section | écrit | corrigé en |
| --- | --- | --- |
| `polarmodulation` | `Blochschaltbild` | `Blockschaltbild` |
| `emitterschaltung` | `richtet sich Die Bezeichnung` | `die Bezeichnung` |
| `emitterschaltung` | `im vergleich zur Kollektorschaltung` | `im Vergleich` |

**Aucune des trois ne nous avait été signalée par le DARC, et nous ne les
avions pas signalées non plus.** L'amont les a trouvées seul.

Deux conséquences, et la seconde est la plus importante :

1. **Notre traduction n'en portait aucune.** `Blochschaltbild` était rendu par
   « schéma fonctionnel », et les deux autres sont des fautes de casse
   allemande qui n'ont pas d'équivalent en français. Le passage à la version
   corrigée n'a donc rien changé au texte français.
2. **L'amont relit son propre corpus.** C'est l'argument le plus concret en
   faveur du signalement resté en attente : les onze entrées de ce relevé
   trouveraient un interlocuteur qui les traiterait. La plus urgente reste le
   §11 — le coefficient de vélocité du RG-58 donné en `\qty{0,66}{\percent}`,
   erreur d'unité d'un facteur cent, la seule du relevé qui puisse réellement
   égarer un candidat.

Le §8 de `CLAUDE.md` datait la correction de `Blochschaltbild` du 16/08/2026.
La mesure la place plus tard : notre instantané `a290eb28`, pris le 17/08,
portait encore la coquille. Elle fait partie des 18 commits repris le 19/08.
