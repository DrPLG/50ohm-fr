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
