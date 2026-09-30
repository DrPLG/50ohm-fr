# Manuel de l'utilisateur — le BIR : récupérer, modifier, recompiler

Ce document explique comment récupérer les fichiers du Brevet d'Initiation à
la Radio, les modifier sans rien casser, et reconstruire le manuel de l'élève
en PDF. Il s'adresse à quelqu'un qui n'a jamais ouvert le dépôt.

État au 30/09/2026 : `build_book.py` v0.34, `fenetre_compilation.py` v0.3,
branche de travail `version-a.4`.

---

## 1. Ce qu'il y a dans le dossier `bir/`

```
bir/
  PLAN.md              plan de l'ouvrage, décisions prises, points ouverts
  MODE-EMPLOI.md       ce document
  referentiel.md       D1 — le référentiel du brevet
  toc.json             le sommaire du manuel : chapitres, chapeaux, sections
  sections/bir_*.md    D2 — le texte du manuel de l'élève, une section par fichier
  questions/seance-XX.json   D5 — les questions, une séance par fichier
  formateur/seance-XX.md     D3 — le livre du formateur, une page par séance
  fiches/seance-XX-eleve.md  D4 — la fiche d'activité de l'élève
  fiches/seance-XX-encadrant.md   … et sa page côté encadrant
  composer.py          le script qui met en PDF les pages du formateur, les fiches,
                       le référentiel et ce mode d'emploi
  maquettes/           la classe LaTeX BIRdoc.cls, la mallette (D7) et le livret (D8)
  moodle/bir-questions.gift.txt   la banque de questions exportée pour Moodle ou éléa
  exporter_moodle.py   le script qui produit ce fichier GIFT
  SOURCES.md           d'où vient chaque section, et l'état de chaque affirmation réglementaire
```

**Ce qui est compilé dans le PDF du manuel :** `toc.json`, `sections/` et
`questions/`. Rien d'autre.

**Ce qui ne l'est pas :** les pages du formateur, les fiches, le référentiel
et ce mode d'emploi sont du Markdown ordinaire. On les lit tels quels (GitHub
les affiche mis en forme), ou on les met en PDF avec `composer.py` (§ 3.5).

**Ce qui vient d'ailleurs :** les dessins, les photos et les fichiers LaTeX de
mise en page ne sont pas dans `bir/`. Ils viennent du dépôt amont du DARC
(voir § 2.3), et les dessins déjà francisés des livres de classe viennent de
`traductions/*/dessins/`.

---

## 2. Récupérer les fichiers

### 2.1 Juste pour lire ou modifier un texte

Sur GitHub, dans le dépôt `DrPLG/50ohm-fr` :

1. choisir la branche `version-a.4` dans le menu déroulant des branches ;
2. ouvrir `bir/` ;
3. cliquer sur un fichier pour le lire ; l'icône crayon permet de le modifier
   directement dans le navigateur, puis « Commit changes » pour
   l'enregistrer (voir § 5).

C'est la voie la plus simple pour corriger une phrase ou une question. Elle ne
permet pas de recompiler le PDF.

### 2.2 Pour travailler sur sa machine

**Avec Git** (recommandé, parce qu'il permet de renvoyer les modifications) :

```
git clone https://github.com/DrPLG/50ohm-fr.git
cd 50ohm-fr
git checkout version-a.4
```

Pour récupérer plus tard les modifications des autres :

```
git pull
```

**Sans Git :** sur GitHub, branche `version-a.4`, bouton vert « Code », puis
« Download ZIP ». Attention : l'archive peut se décompresser dans un dossier
imbriqué de même nom (`50ohm-fr-version-a.4\50ohm-fr-version-a.4\`) ; c'est
le dossier intérieur qui compte.

### 2.3 Les deux dépôts amont, indispensables pour compiler

Le manuel se compile avec la chaîne des livres de classe, qui a besoin de deux
dépôts du DARC :

| dépôt | ce qu'il apporte | archive à télécharger |
| --- | --- | --- |
| `DARC-e-V/50ohm-contents-dl` | les fichiers LaTeX de mise en page, les dessins, les photos | `https://codeload.github.com/DARC-e-V/50ohm-contents-dl/zip/refs/heads/main` |
| `DARC-e-V/50ohm` | le générateur, qui fournit le paquet Python `renderer` | `https://codeload.github.com/DARC-e-V/50ohm/zip/refs/heads/main` |

Confusion fréquente : le paquet `renderer` est dans le dépôt **générateur**
(`50ohm`), pas dans le dépôt de contenus.

Les deux se placent côte à côte sous une même racine. Sous Windows, les
emplacements reconnus d'office sont :

```
C:\50ohm\50ohm-main\               le générateur
C:\50ohm\50ohm-contents-dl-main\   les contenus
```

(ou la même chose sous `D:\50ohm-amont\`). Pour une autre racine, définir la
variable d'environnement `OHM_AMONT` sur cette racine avant de lancer la
fenêtre ou `compiler.bat`.

### 2.4 Les logiciels

| logiciel | à quoi il sert | remarque |
| --- | --- | --- |
| Python **3.12 ou plus**, avec le module `mistletoe` | faire tourner `build_book.py` | le plus simple : dans `C:\50ohm\50ohm-main`, lancer `uv sync`, qui crée un environnement `.venv` complet |
| une distribution TeX avec **LuaLaTeX** et **latexmk** | composer le PDF | MiKTeX sous Windows, TeX Live sous Linux ou macOS |
| Perl | `latexmk` est un script Perl | MiKTeX n'en fournit pas ; celui de Git for Windows convient, la fenêtre l'ajoute d'elle-même |
| Ghostscript | compresser le PDF | facultatif |
| les polices Linux Libertine et Libertinus | utilisées par la mise en page | fournies par MiKTeX et TeX Live complètes ; sous Linux, paquets `fonts-linuxlibertine` et `texlive-fonts-extra` |

Piège connu sous Windows : le `python` trouvé dans le PATH peut être celui
d'Inkscape, trop ancien et sans `mistletoe`. La fenêtre et `compiler.bat`
essaient chaque interpréteur au lieu de le supposer ; la variable
`OHM_PYTHON` permet d'en désigner un.

---

## 3. Modifier

### 3.1 Corriger ou compléter le texte d'une section

Chaque section du manuel est un fichier `bir/sections/bir_<nom>.md`, écrit en
**DARCdown**, le Markdown du projet 50ohm. L'essentiel :

| on écrit | on obtient |
| --- | --- |
| un paragraphe, puis une ligne vide | un paragraphe |
| `*mot*` | *mot* en italique |
| `**mot**` | **mot** en gras |
| `* élément` sur plusieurs lignes, **puis une ligne vide** | une liste à puces |
| `1. étape` sur plusieurs lignes, **puis une ligne vide** | une liste numérotée |
| `---` seul sur une ligne | une séparation entre deux blocs |
| `$U = R \times I$` | une formule |
| `$$P = U \times I$$` seul sur une ligne | une formule centrée |
| `$\qty{145}{\mega\hertz}$` | 145 MHz, bien espacé |
| `[index:Antenne]` ou `[index:Antenne:Yagi]` | une entrée d'index |
| `[morse:sos]` | les points et traits d'un mot en Morse |
| `% une remarque` en début de ligne | un commentaire, non imprimé |

**Les encadrés.** La balise ouvrante et la balise fermante doivent être
**seules sur leur ligne** :

```
<tip>
Un conseil, en encadré bleu.
</tip>
```

| balise | encadré |
| --- | --- |
| `<tip>` | Astuce |
| `<attention>` | Attention |
| `<danger>` | Danger |
| `<margin>` | contenu placé dans la marge (figure, petit tableau) |
| `<qso>` | un dialogue radio ; les répliques du correspondant commencent par `> ` |

**Interdit dans le BIR :** l'encadré `<france>`. Tout l'ouvrage s'adresse à des
Français ; la compilation s'arrête si une section en contient un.

**Les tableaux.** La première ligne donne les titres et l'alignement de
chaque colonne (`l:` à gauche, `c:` centré, `r:` à droite, `X:` texte long) ;
la ligne qui suit le tableau lui donne un identifiant et une légende :

```
| l: Bande | X: Fréquences | l: Domaine |
| 2 m | 144 à 146 MHz | VHF |
| 70 cm | 430 à 440 MHz | UHF |
[table:bir_deux_bandes:Deux bandes radioamateur]
```

**Les figures.** On reprend un dessin ou une photo de l'amont par son numéro :

```
<margin>
[picture:589:bir_dipole:Une antenne dipôle — deux brins alimentés au centre]
</margin>
```

- `picture` pour un dessin, `photo` pour une photo ;
- le numéro est celui du fichier dans `contents/drawings/` ou
  `contents/photos/` du dépôt de contenus ; `SOURCES.md` et les sections des
  livres N, E et A (`traductions/*/sections/`) montrent quels numéros sont
  déjà utilisés, avec leur sujet ;
- préférer un dessin déjà utilisé par un livre français : il a été vérifié,
  et sa version francisée, si elle existe dans `traductions/*/dessins/`, est
  reprise automatiquement ;
- l'identifiant (`bir_dipole`) doit être **unique dans tout le manuel** et
  commencer par `bir_` ; on y renvoie dans le texte par
  `figure [ref:bir_dipole]` ;
- une figure en marge se place **juste avant** le paragraphe qu'elle
  illustre ; une grande figure se place sans `<margin>`, sur toute la
  largeur.

**Trois pièges déjà rencontrés :**

1. **Pas de deux-points dans une légende.** Le deux-points sépare les champs
   de la balise : `[picture:734:bir_inversion:Une inversion : …]` coupe la
   légende, et le renvoi à la figure sort en « ?? ». Utiliser un tiret long
   (—).
2. **Une ligne vide après chaque liste.** Sans elle, le paragraphe suivant
   est avalé par la liste.
3. **Une balise d'encadré partage sa ligne avec du texte.** Elle est alors
   imprimée telle quelle.

### 3.2 Changer un titre, un chapeau, ou l'ordre des sections

Tout se trouve dans `bir/toc.json` : pour chaque séance, son titre
(`title`), son chapeau (`abstract`, le petit texte en italique sous le titre
du chapitre) et la liste de ses sections, dans l'ordre d'impression.

```
{
 "ident": "bir_14",
 "title": "Les antennes : principes",
 "abstract": "L'antenne est la pièce maîtresse…",
 "sections": [
  {"ident": "bir_le_role_de_l_antenne", "title": "Le rôle de l'antenne"},
  {"ident": "bir_le_dipole_demi_onde", "title": "Le dipôle demi-onde"}
 ]
}
```

- `ident` d'une section = nom de son fichier, sans `.md` ;
- le titre d'une section se change ici, pas dans le fichier de la section ;
- attention aux virgules et aux guillemets : un JSON mal formé arrête la
  compilation dès le départ. Un éditeur comme VS Code ou Notepad++ signale
  l'erreur ;
- un chapitre dont la liste `sections` est vide est simplement sauté ; les
  autres gardent le numéro de leur séance.

### 3.3 Ajouter une section

1. Créer `bir/sections/bir_<nom>.md`, avec des minuscules, des chiffres et
   des soulignés seulement.
2. L'ajouter à la liste `sections` de sa séance dans `toc.json`, avec son
   titre.
3. Ajouter une ligne dans `SOURCES.md` : de quelle section amont elle part,
   comment elle est adaptée, quelles figures elle reprend.

### 3.4 Modifier ou ajouter une question

Les questions d'une séance sont dans `bir/questions/seance-XX.json` :

```
{
 "number": "RD1405",
 "class": "BIR",
 "question": "Environ combien mesure chaque brin d'un dipôle pour $\\qty{145}{\\mega\\hertz}$ ?",
 "answer_a": "49 cm",
 "answer_b": "2 m",
 "answer_c": "5 cm",
 "answer_d": "10 m"
}
```

Règles :

- **la bonne réponse est toujours `answer_a`.** Le manuel mélange les
  réponses à l'impression, toujours de la même façon pour une même question,
  et écrit le corrigé dans `corrige-BIR.txt` ; Moodle les mélange à
  l'affichage ;
- **le numéro** se lit R + lettre du domaine + numéro de séance sur deux
  chiffres + numéro d'ordre : `RD1405` est la question 5 de la séance 14,
  domaine D. Il doit être unique ;
- **chaque question doit être appelée** dans une section, par une ligne
  `[question:RD1405]`, là où elle doit s'imprimer. Une question appelée mais
  absente du catalogue arrête la compilation ;
- **dans le JSON, chaque barre oblique inverse est doublée** :
  `$\\qty{145}{\\mega\\hertz}$` ;
- **une réponse qui n'est qu'une valeur s'écrit en texte** : `"1,5 V"`, pas
  `"$\\qty{1,5}{\\volt}$"`. Une réponse faite d'une seule formule est
  composée en formule centrée, ce qui triple la hauteur de la question ;
- dans les énoncés et les réponses, seules les formules `\qty{…}{…}` et
  `\qtyrange{…}{…}{…}` passent vers Moodle ; toute autre formule arrête
  l'export (§ 4.4). Écrire `U = R × I` en texte simple plutôt qu'en formule ;
- quatre réponses, toutes différentes, une seule juste sans discussion
  possible.

Après toute modification de questions, régénérer l'export Moodle (§ 4.4).

### 3.5 Les pages du formateur, les fiches, le référentiel, le plan

Ce sont des fichiers Markdown ordinaires : on les modifie librement, avec
n'importe quel éditeur de texte, sans règle particulière. Ils ne passent pas
par la compilation du manuel.

Le Markdown est leur **seule source**. Pour les mettre en PDF, avec la mise
en page du BIR :

```
python bir/composer.py                 tous les documents
python bir/composer.py fiches-eleve    un seul : formateur, fiches-eleve,
                                       fiches-encadrant, mode-emploi, referentiel
```

Les PDF arrivent dans `bir/pdf/` : `livre-du-formateur.pdf`,
`fiches-eleve.pdf` (à imprimer recto verso : chaque fiche commence sur une
nouvelle feuille), `fiches-encadrant.pdf`, `mode-emploi.pdf` et
`referentiel.pdf`. Comptez une à deux minutes pour le tout.

Trois conventions dans les fiches de l'élève :

- `☐` devient une case à cocher ;
- une suite de `…` devient une ligne pointillée à remplir — jusqu'à la marge
  si elle termine la ligne, de la longueur de la suite sinon ;
- un bloc de code vide (quatre lignes blanches entre deux lignes de trois
  accents graves) devient un cadre où dessiner.

Dans un tableau, une case laissée vide est une case à remplir : le tableau
est alors tracé avec des lignes hautes.

Le script s'arrête sur toute construction qu'il ne connaît pas (citation
`>`, balise, liste dans une liste) : il vaut mieux une erreur qu'une page
fausse.

La mallette et le livret de l'élève, eux, sont écrits directement en LaTeX :

```
cd bir/maquettes
latexmk -lualatex D8-livret.tex
```

---

## 4. Recompiler

### 4.1 Avec la fenêtre de compilation (Windows, le plus simple)

Depuis la racine du dépôt :

```
python fenetre_compilation.py
```

(avec le Python du générateur si le `python` du PATH ne convient pas :
`C:\50ohm\50ohm-main\.venv\Scripts\python.exe fenetre_compilation.py`).

1. **Tome :** BIR.
2. **Format :** A4, 20 × 24, ou 20 × 24 avec marge de 52 mm (celui des
   premières épreuves du BIR).
3. **Langue :** français (le BIR n'existe qu'en français).
4. **Version :** `0.1` est proposée d'office ; changer le numéro à chaque
   édition diffusée.
5. **Pièces liminaires :** aucune pour le BIR, la fenêtre les désactive.
6. **Étapes :** laisser « purger les auxiliaires avant » coché. « Compresser »
   produit une version allégée pour l'envoi.
7. **Copier la commande** met dans le presse-papiers la ligne de commande
   exacte, utile pour la noter ou la relancer à la main.
8. **Lancer**, puis confirmer. Le journal défile dans la fenêtre ; il est
   aussi enregistré dans `build-BIR-…-console-<date>.txt`.

Compter quelques minutes pour le manuel complet.

### 4.2 En ligne de commande

Windows (à adapter à l'emplacement de l'amont) :

```
set OHM_RENDERER=C:\50ohm\50ohm-main
python build_book.py --edition BIR --lang fr --format 20x24-marge ^
  --input C:\50ohm\50ohm-contents-dl-main ^
  --output build-BIR-20x24-marge --version-label 0.1
```

Linux ou macOS :

```
export OHM_RENDERER=~/50ohm-amont/50ohm-main
python3 build_book.py --edition BIR --lang fr --format 20x24-marge \
  --input ~/50ohm-amont/50ohm-contents-dl-main \
  --output build-BIR-20x24-marge --version-label 0.1
```

- `--input` désigne la **racine** du dépôt de contenus, celle qui contient
  `latex/` et `contents/` ;
- `--format` : `a4`, `20x24` ou `20x24-marge` ;
- `--no-compile` génère les fichiers LaTeX **sans** lancer LuaLaTeX : en
  quelques secondes, on sait si toutes les sections, figures et questions
  sont trouvées. C'est le bon réflexe après chaque modification ;
- avant de relancer une compilation dans le même dossier de sortie, le
  purger (ou en choisir un autre) : des fichiers auxiliaires périmés font
  croire à `latexmk` qu'il n'a rien à faire ;
- toujours laisser `build_book.py` appeler `latexmk` ; ne jamais enchaîner
  soi-même deux passes de `lualatex`.

### 4.3 Ce que l'on obtient

Dans le dossier de sortie (`build-BIR-20x24-marge/`, par exemple) :

| fichier | contenu |
| --- | --- |
| `book-BIR.pdf` | le manuel de l'élève |
| `corrige-BIR.txt` | le corrigé : pour chaque question, la lettre de la bonne réponse **telle qu'imprimée** |
| `book-BIR.log` | le journal de LuaLaTeX, à consulter en cas d'erreur |
| `sections/*.tex` | le LaTeX produit pour chaque section |

Avec la compression, la fenêtre écrit aussi `livre-BIR-0.1-20x24-marge.pdf`
à la racine du dépôt.

Les PDF ne sont pas versionnés (ils sont exclus par `.gitignore`) : ils se
diffusent à part, par exemple dans une *release* GitHub.

### 4.4 Régénérer la banque de questions pour Moodle ou éléa

```
python bir/exporter_moodle.py
```

Le script lit tous les `questions/*.json` et écrit
`bir/moodle/bir-questions.gift.txt`, rangé par domaine puis par séance. Dans
Moodle ou éléa : *Banque de questions › Importer › format GIFT*, puis choisir
le fichier. Pour un examen, créer un test qui tire 8 questions au hasard dans
chacune des cinq catégories de domaine (référentiel, § 4).

Si le script s'arrête sur « formule non réécrite », une question contient une
formule autre que `\qty` ou `\qtyrange` : la réécrire en texte (§ 3.4).

### 4.5 Quand ça ne marche pas

| message ou symptôme | cause probable | que faire |
| --- | --- | --- |
| `--input ne désigne pas la racine de 50ohm-contents-dl` | mauvais chemin, souvent le dossier imbriqué d'une archive ZIP | suivre la suggestion affichée (« le bon chemin est probablement… ») |
| `No module named renderer` ou `mistletoe` | mauvais Python, ou `OHM_RENDERER` non défini | utiliser le Python du générateur ; définir `OHM_RENDERER` |
| `édition BIR : toc.json absent` | on ne lance pas depuis le bon dépôt, ou `--local` pointe mal | lancer depuis la racine de `50ohm-fr` |
| `édition BIR : encart <france> interdit — …` | une section contient `<france>` | retirer l'encadré, ou le réécrire en texte courant |
| `question(s) appelée(s) mais absente(s)` | une ligne `[question:…]` appelle un numéro absent des JSON | corriger le numéro, ou ajouter la question |
| erreur JSON au démarrage | virgule, guillemet ou barre oblique inverse mal placés dans `toc.json` ou un `questions/*.json` | ouvrir le fichier dans un éditeur qui vérifie le JSON |
| « ?? » dans le PDF à la place d'un numéro de figure | identifiant mal écrit, ou deux-points dans une légende | corriger la balise (§ 3.1) |
| `The font "LinBiolinum_K" cannot be found` | polices Linux Libertine absentes | installer les polices (§ 2.4) |
| `Command \@ already defined` au chargement de `settings.tex` | TeX Live trop ancien (2023) face aux fichiers amont | mettre la distribution TeX à jour |
| `Float too large` ou `lost some margin notes` | une figure trop haute pour la marge | la sortir de `<margin>`, ou choisir une autre figure |
| `Nothing to do` alors qu'on a modifié un fichier | auxiliaires périmés | purger le dossier de sortie et relancer |

---

## 5. Enregistrer et partager ses modifications

Avec Git, depuis la racine du dépôt :

```
git status                      voir ce qui a changé
git add bir                     préparer les fichiers du BIR
git commit -m "BIR : séance 12, corrections de la fiche"
git push                        envoyer sur GitHub
```

Sur GitHub, dans le navigateur : après une modification avec l'icône crayon,
« Commit changes » en choisissant soit la branche `version-a.4` (si l'on a le
droit d'y écrire), soit « Create a new branch » pour proposer la modification
par une *pull request*.

Bonnes habitudes :

- un commit par sujet, avec un message qui dit ce qui change ;
- après une modification de questions, commiter aussi le fichier GIFT
  régénéré ;
- après une nouvelle section, commiter aussi `toc.json` et `SOURCES.md` ;
- compiler (au moins en `--no-compile`) avant de pousser.

---

## 6. Aide-mémoire

| je veux… | je modifie… | puis je lance… |
| --- | --- | --- |
| corriger une phrase du manuel | `sections/bir_*.md` | `build_book.py … --no-compile`, puis une compilation |
| changer un titre ou un chapeau | `toc.json` | idem |
| ajouter une section | `sections/`, `toc.json`, `SOURCES.md` | idem |
| corriger une question | `questions/seance-XX.json` | la compilation, puis `exporter_moodle.py` |
| corriger une fiche ou une page du formateur | `fiches/` ou `formateur/` | rien : c'est du Markdown |
| refaire le PDF | — | la fenêtre, tome BIR |
| mettre à jour Moodle | — | `exporter_moodle.py`, puis import GIFT |
