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

**Côté français.** Formule préservée verbatim (§5 : « formules `$…$`
verbatim »). Le défaut est donc reproduit tel quel.

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

## 5. Libellés tronqués dans le dessin 666 — `gleichrichter_1`, `halbleiter`

**Constaté le 15/08/2026**, en corrigeant un défaut de francisation qui l'a
révélé.

Le dessin 666 (classes N et E) légende les deux électrodes d'une diode. Deux
de ses quatre libellés sont **tronqués de leur première lettre** dans la source
amont :

```latex
\draw[red, thick] (1.280,0) to [short] ++(-1.0,-0.626) coordinate(node);
\draw[red] (node) node[rotate=-90, anchor=west]{node};      % « Anode » attendu
\draw[blue, thick] (1.280,0) to [short] ++(0.35,-0.35) coordinate(athode);
\draw[blue] (athode) node[anchor=west]{athode};             % « Kathode » attendu
```

La coordonnée et le texte portent la même chaîne tronquée : le dessin imprime
donc « node » et « athode » sous les deux électrodes, alors que la partie haute
du même dessin porte correctement « Anode » et « Kathode ». Le livre allemand
est affecté à l'identique.

L'hypothèse la plus simple est une saisie où la première lettre a servi de
raccourci et s'est perdue ; la coordonnée ayant été nommée d'après le texte, la
troncature s'est propagée sans provoquer d'erreur LaTeX.

### Ce que ce défaut nous a coûté côté français

Il a produit, chez nous, **un mot qui n'existe dans aucune langue**. Le fork
français substituait `Kathode` → `Cathode` **puis** `athode` → `Cathode` ; la
seconde règle s'appliquant au résultat de la première, le libellé haut est
devenu **« CCathode »**. Présent dans `livre-N-a.1.pdf` **et** dans les PDF
a.2, jamais relevé en relecture.

Corrigé côté français le 15/08/2026 (« Cathode »). Les deux libellés tronqués
du bas, eux, sont **laissés en l'état** : les corriger reviendrait à réécrire
le dessin amont, ce que le §6 de `CLAUDE.md` interdit. À signaler au DARC.
