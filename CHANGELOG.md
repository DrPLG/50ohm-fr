# Journal des versions

Les versions sont suivies **par classe**, chacune évoluant à son rythme.
Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

Rubriques employées : *Ajouté*, *Modifié*, *Corrigé*, *Préservé* (défauts amont
laissés intacts et consignés), *Connu* (limitations non résolues).

---

## a.3 (en cours) — 20 août 2026

**Chantier ouvert le 20/08/2026 : refonte amont du chapitre DSP.**

### 20 août 2026, après-midi — le livre allemand, et le format en paramètre

Séance en trois temps : compiler pour la première fois le livre **allemand**,
recompiler les livres de la a.3, et rendre le **format de page** paramétrable.

Contrôle de dérive amont en ouverture : `7c1d87a3` en local **et** sur le
dépôt du DARC. Pour la première fois depuis que ce contrôle existe, le réseau
et l'instantané concordent — aucune dérive à rattraper.

#### Ajouté

- **v0.23 — option `--format a4|20x24`** (feuille nº 8, D2 = variante C, D3a).
  La maquette n'était pas paramétrable : papier, cinq cotes, folio et largeur
  du dessin 202 étaient écrits en dur. Ils passent dans un tableau `FORMATS`.
  **Défaut `a4`** : sans l'option, le `.cls` produit ne diffère de celui de la
  v0.22 par **aucune ligne de code** — seul un commentaire se déplace, les
  cotes en toutes lettres n'étant plus écrites qu'une fois, là où le format les
  décide. Quatre points de code suffisaient : tout le reste de la mise en page
  est en unités relatives, y compris les clamps v0.17 et v0.18, la page de
  titre et **907 des 908 dessins amont**.
  Maquette 20 × 24 retenue : `15 + 125 + 6 + 42 + 12 = 200 mm`, hauteur de
  texte 202 mm, folio à 45 mm — cette dernière valeur n'étant pas devinée mais
  calculée par `2 × (paperwidth/2 − (inner + textwidth/2))`, formule que
  l'A4 vérifie (elle y redonne les 56 mm déjà codés).
- **Le livre N en allemand**, compilé pour la première fois dans ce dépôt :
  **230 pages**, quatre contrôles du §4 verts, 2,86 Mo après compression.
  La traduction française coûte donc **28 pages, soit +12,2 %** (258 contre
  230) — premier chiffre dont nous disposions sur ce point.

#### Compilé

- **Classe A, a.3 : 386 pages** (384 en a.2), 5,40 Mo. Convergée, aucune erreur
  fatale, et **les deux seuils annoncés tranchés par la mesure — un seul des
  deux bougeait** :
  - **notes de marge : 4, inchangé.** On en attendait 5, en croyant que
    `fehlerkorrektur` viendrait s'ajouter aux quatre existantes après que
    l'amont eut rallongé son encart Hamming. Elle y était **déjà** : comparée à
    la console de la a.2, les trois premières hauteurs sont identiques au
    centième (731,83 · 976,66 · 828,91 pt) et la quatrième passe de 919,69 à
    **1035,49 pt**. Elle a grossi, elle ne s'est pas ajoutée. `compiler.bat`
    avait raison, rien n'a été touché ;
  - **références `??` : 3 → 2, confirmé sur le PDF.** L'amont a corrigé
    `a_sender` en `a_sdr_sender`. Restent `a_mehrwegeausbreitung_ionosphäre` et
    `a_zeppelinantenn`. **Deuxième défaut que l'amont corrige seul** sans que
    nous l'ayons signalé, après les trois coquilles du 19/08.
- **Classe N, a.3 : 258 pages**, pagination inchangée. N n'était pas au
  programme de la a.3 : elle y est entrée par la correction des doubles
  crochets, qui touche `wellenlaenge`. Quatre contrôles verts, convergée.
- **Classe E, a.3 : 214 pages**, 3,02 Mo. Les quatre contrôles du §4 sont
  verts, une seule référence `??` (le défaut amont `e_ssb_am_modulation`), et
  aucun « Rerun » demandé — le document est convergé.
  **La pagination ne bouge pas** : 214 pages en a.2 comme en a.3, malgré
  l'ident renommé et la section réécrite.
  *À savoir pour les diagnostics futurs :* l'index de la classe E est **vide**,
  et c'est normal. E ne porte **aucune** entrée `\index{}` (N en compte 77) —
  un `book-E.idx` à zéro octet n'est donc pas le symptôme d'une compilation
  incomplète, contrairement à ce qu'il donnerait à croire en classe N.

#### Corrigé

- **v0.22 — la francisation typographique n'est plus inconditionnelle.** Trois
  réglages de la v0.17 (arbitrage nº 1) s'appliquaient quelle que soit la
  langue : `\babelprovide{french}` en langue **principale**, les puces en tiret
  cadratin avec le séparateur de légende « -- », et les listes resserrées. Le
  livre allemand aurait donc été coupé selon les règles **françaises** et aurait
  porté des espaces fines devant « : ; ! ? » — deux fautes en allemand. Vérifié
  après correction, sur document réduit : `Fern-mel-de-an-la-ge`,
  `Be-triebs-span-nung`, et le séparateur redevenu `Abb. 1:`.
- **`compiler.bat` ne pouvait plus être lancé.** Le `.gitattributes` portait
  `* text=auto eol=lf`, qui normalise en LF **le répertoire de travail** —
  y compris les `.bat`. Sur des fins de ligne LF nues, cmd.exe se désynchronise
  en lisant le script et perd des caractères en tête de ligne : « setlocal »
  devient « tlocal », « chcp » devient « cp », et le batch part en cascade de
  « n'est pas reconnu en tant que commande interne ou externe ». Règle
  `*.bat text eol=crlf` ajoutée, fichier reconverti en binaire.
- **Les quatre scripts de contrôle plantaient sur la console Windows.**
  `verifier_traduction.py --tout` s'interrompait sur un `λ` par
  `UnicodeEncodeError`, APRÈS avoir affiché la moitié de ses résultats : son
  code de retour devenait celui d'un plantage, **indiscernable d'un `rc=1`
  légitime**. Un contrôle qui ne peut pas rendre son verdict ne contrôle rien.
  Les quatre reconfigurent désormais leur sortie en UTF-8. Verdict complet
  retrouvé : **382 sections, 355 conformes, 7 dérogations, 20 écarts** — tous
  préexistants et documentés.

- **Doubles crochets d'unité ramenés au crochet simple** — 20 formules, 3
  sections (`N/wellenlaenge`, `E/wellenlaenge_2`, `E/formeln_umstellen`).
  L'amont écrit `$f[[\unit{\mega\hertz}]]$` ; rien n'absorbe le doublement — ni
  le parseur, qui ne traite pas `[[`, ni LaTeX, où les crochets sont des
  délimiteurs ordinaires en mode mathématique — et le PDF composait
  littéralement **« f [[MHz]] »**, sans le moindre avertissement.
  Le **principe** du crochet est conservé : c'est la *zugeschnittene
  Größengleichung* du formulaire officiel que le candidat aura sous les yeux à
  l'examen, et le texte amont dit lui-même en venir. Seul le doublement tombe.
  Relevé par Pierre à la lecture du N en 20 × 24 ; décision du 20/08/2026.
  Dérogation assumée à « formules verbatim » (§6), déclarée dans
  `verifier_traduction.py`, détaillée en `defauts-amont.md` §21.
  **Conséquence : N et E sont à recompiler.** La classe A n'a aucune
  occurrence et n'est pas concernée.

- **66 connecteurs allemands « und » traduits en « et »**, dans **15 questions
  de la classe N**. Le §6 classe pourtant une question en « forme complète »
  précisément quand ses réponses contiennent de la prose allemande,
  « connecteurs compris (und, bis, ca., Punkt, beides) » : la règle était
  écrite, elle n'avait pas été appliquée sur ces quinze-là.
  Questions touchées : `BD303` à `BD318` (13 sur les indicatifs de pays),
  `NA101` et `VD738`. **E et A sont indemnes** — zéro occurrence, mesuré.
  **Deux exceptions conservées, vérifiées une par une** : `VC104`
  (« Bundesanstalt für Post und Telekommunikation » est un nom propre
  d'institution, comme « Bundesnetzagentur » dans la même question) et `VE501`
  (« Elektromagnetische Verträglichkeit in der Umwelt » est la glose du sigle
  EMVU, sujet même de la question).
  **Conséquence : N et NEA sont à recompiler.**

  *Comment il a été trouvé, et c'est le plus instructif.* Pas par un contrôle,
  mais en **lisant** le rendu Beamer de `bandbreite` : « 135,7 à 137,8 kHz,
  472 à 479 kHz **und** 10100 à 10150 kHz ». Aucun de nos quatre scripts ne
  regarde `questions.json` — `verifier_traduction.py` compare les sections à
  l'amont, `sonde_dessins.py` lit les dessins. Ce défaut était dans les PDF
  publiés de la **a.2** depuis le 19/08, sous les yeux de tous. **Un prototype
  écrit pour répondre à une question de faisabilité a trouvé un défaut que
  l'outillage ne pouvait pas voir.**

#### Préservé

- Le défaut amont **§20** (marqueurs `[photo:…][index:…]` accolés) est
  désormais constaté **dans le PDF allemand** : la photo du S-mètre manque et
  son renvoi pend en « Wie im Bild ?? zu sehen ist ». C'est la capture qui
  manquait au courrier `COURRIER-DARC-DE.md`.

#### Connu

- **`compiler.bat` ne peut pas aller au bout en processus détaché**, et ce
  n'est pas un défaut : sa ligne 274 demande `Compresser le PDF avec
  Ghostscript maintenant ?`, conformément au §2 qui veut que la compression
  soit décidée par Pierre. Sans console interactive, la question reste sans
  réponse et le batch attend — après avoir tout fait, contrôles compris.
  Pour un lancement automatique : `echo O | compiler.bat N`.

  *Trois diagnostics faux avant celui-là, et c'est la leçon de la journée.*
  L'arrêt des batches a été successivement attribué à un `find` parcourant le
  disque, puis à `find.exe` bloqué sur son entrée standard — au point qu'un
  correctif a été écrit pour ce second motif. Il n'a rien changé : à la
  compilation suivante, le batch s'est arrêté au même endroit, **sans le
  moindre `find.exe` vivant**. La vraie cause était affichée en clair dans la
  console depuis le début. Le correctif du comptage est conservé — il est
  équivalent, vérifié 4 = 4 — mais son commentaire a été rectifié.
  **Lire ce que la machine affiche avant de théoriser sur ce qu'elle fait.**

- **Le comptage des `??` dans le PDF sur-compte en allemand.** Le §4 érige ce
  comptage en référence contre le journal, qui sous-compte — vrai en français,
  trompeur en allemand : le PDF N allemand porte **4 occurrences pour 1 seul
  vrai défaut**, les trois autres étant la question BB203 sur les codes Q, où
  deux `?` légitimes se collent (`bestätigen??`). En français, l'espace fine
  de la v0.17 les sépare. Le contrôle se relit, il ne se prend pas au mot.
- **Les 260 « Missing character » sur le caractère `` ` ``** ne concernent
  **que la classe E** : le N allemand comme le N français en comptent **zéro**,
  et leurs profils sont par ailleurs identiques (51 caractères manquants, dont
  42 `;` du défaut `\tikzstyle` et 9 `0` venant des formes circuitikz). En E,
  ils apparaissent page 23, après le dessin 992 — dont les 7 826 lignes de
  `filecontents` émettent des messages du type `` `world.dat' ``. Piste, pas
  conclusion.

### 20 août 2026 — troisième resynchronisation amont (feuille d'arbitrage nº 7)

**Ce n'est plus une dérive de contenu, c'est une restructuration de périmètre**
— une première pour ce dépôt. L'amont est passé de `07f3c861` à `7c1d87a3` :
**56 commits, 75 fichiers, 20 sections traduites** (19 en A, 1 en E), et
**5 sommaires** touchés.

| | avant | après |
| --- | ---: | ---: |
| sections classe A | 152 | **148** |
| sections classe E | 103 | 103 |
| sections classe NEA | 383 | **379** |
| dessins forkés (N · E · A) | 39 · 73 · 113 | 39 · 73 · **116** |
| éléments suivis au manifeste | 611 | **610** |

Le chapitre `a_digitale_signalverarbeitung` passe de 14 à 8 sections,
`a_digitale_uebertragungsverfahren` de 13 à 15, et **deux sections changent de
chapitre** (`iq_verfahren`, `polarmodulation`).

#### Ajouté

- **5 sections traduites** : `dac_adc`, `anti_alias_rekonstruktionsfilter`,
  `symbole_symbolrate`, `digital_iq` (classe A) et `datenuebertragungsrate`
  (classe E).
- **3 dessins forkés et francisés** : 1130 (convertisseurs A/N et N/A), 1131
  (filtres anti-repliement et de reconstruction, avec `A` → `S` pour la
  sortie), 1132 (« Autres parties du récepteur », « Information de commande »).
  **13 dessins nouvellement appelés ont été examinés un à un** ; les 10 autres
  ne composent aucun texte allemand.
- 4 titres de section neufs, 1 abstract de chapitre.

#### Modifié

- **11 sections resynchronisées** : `psk`, `qam`, `sampling_quantisierung`,
  `iq_verfahren`, `mapping` et `fourier_transformation` sont des réécritures
  quasi complètes ; `digitale_filter`, `fehlerkorrektur`, `ofdm`,
  `parasitaere_schwingungen` et `sende_empfangsketten` sont des ajouts ciblés.
- **2 titres changés en amont** : `psk` devient « Modulation par déplacement de
  phase : PSK et QPSK », `iq_verfahren` « Représentation I/Q et diagramme de
  constellation ».

#### Retiré

- **9 traductions**, dont les 8 sections de la classe A fondues dans les
  nouvelles (`analog_digital_umsetzer`, `digital_analog_umsetzer`,
  `anwendung_dac_adc`, `anti_alias_filter`, `rekonstruktionsfilter`,
  `sampling`, `quantisierung`, `mehrwertige_verfahren`) et
  `datenuebertragungsdrate` en classe E. Décision de Pierre : suppression
  simple, git fait mémoire.
- L'ident amont `datenuebertragungs**d**rate` est corrigé en
  `datenuebertragungsrate`. **Ce n'est pas un simple renommage** : la section
  est aussi réécrite et amputée de la notion de rapidité de modulation.

#### Corrigé

- **`\sample`** (`digital_iq`) : l'unité n'est déclarée nulle part en amont et
  l'erreur est **fatale** — `latexmk` sort en `rc=12`. Rendue `\mega\sps`.
  Voir `docs/defauts-amont.md` §18.
- **`<tipp>`** (`elektrische_geaete_oeffnen_2`) : marqueur DARCdown inexistant,
  qui **s'imprime littéralement dans le PDF allemand**. Rendu `<tip>`. §17.
- **Référence orpheline `a_sender`** : corrigée en amont (`a_sdr_sender`),
  correction adoptée. La classe A devrait passer de **3 à 2 `??`** — confirmé
  par le validateur du générateur, à vérifier sur le PDF.

#### Préservé

- **Labels dupliqués `a_adc_4bit` et `a_adc_12bit`** : les dessins 300 et 299
  sont déclarés dans `dac_adc` **et** `anti_alias_rekonstruktionsfilter`, avec
  des légendes différentes et un renvoi de part et d'autre. Défaut **introduit
  par la refonte**, confirmé à la compilation (`multiply defined`). §13.
- Trois coquilles allemandes (`ofdm`, `datenuebertragungsrate`,
  `parasitaere_schwingungen`). §14.
- **La classe E emploie le baud sans plus le définir** : la rapidité de
  modulation part en classe A, alors que `9600_port` écrit
  `\qty{9600}{\baud}` douze fois. Suivi tel quel (décision de Pierre, D6a) —
  l'examen E n'interroge pas dessus. §16.

#### Connu

- **Une cinquième note de marge rétrogradée en classe A**, dans
  `fehlerkorrektur` : l'amont a rallongé l'encart `<indepth>` du code de
  Hamming, qui culmine à **1035,5 pt** pour un seuil de 711,3 pt. Le garde-fou
  v0.13 fait son travail, mais le compte du §4 passe de 4 à 5.
- Les avertissements « Missing character … in font nullfont » ont été
  **mesurés** : ils viennent des formes circuitikz du dessin 196 et des
  `\tikzstyle` dépréciés, **aucun texte lisible ne disparaît**. Les dessins ASK
  et FSK, rendus en image, portent bien leurs six bits. §19.

#### Mesuré

- **L'hypothèse du remontage était fausse.** La note de clôture du 19/08
  pariait qu'il y aurait « beaucoup à réemployer plutôt qu'à retraduire » :
  comparaison phrase à phrase des 5 sections neuves (142 phrases), **95 % de
  prose neuve**, et 4 des 7 phrases reprises sont de simples lignes
  `[question:…]`. C'est une réécriture, pas un remontage.
- **Aucune question perdue ni gagnée** : 717 · 462 · 1 750, usages identiques.
  Les 28 mouvements sont des déplacements, et nos `questions.json` étant
  indexés par identifiant, ils ne coûtent rien.
- Instantané rebasculé et vérifié : **4 162 blobs sur 4 162 identiques** à
  l'arbre amont par empreinte git, **0 nom corrompu**.
- `verifier_traduction.py` : **20 écarts**, contre 22 avant la session — tous
  préexistants et documentés dans `docs/ecarts-traduction.md`. Aucun écart neuf
  n'a été introduit.

---

## a.2 — 14 au 19 août 2026 — **première version publiée**

Publiée le 19/08/2026, tag `a.2`. C'est la **première release du dépôt** : la
`a.1` du 14/08 était un test de la chaîne de publication, supprimée le jour
même avec son tag.

| Classe | Sections | Questions | Encarts | Dessins forkés | Pages (a.1 → a.2) |
| ------ | -------: | --------: | ------: | ---: | ----: |
| N | 131 | 571 | 55 | 39 | 254 → 258 |
| E | 103 | 462 | 6 | **73** | 206 → 214 |
| A | **152** | 717 | 5 | **113** | 372 → **384** |
| NEA | 383 | 1 751 | 64 | 225 | — → **816** |

### 19 août 2026 — seconde resynchronisation amont, et publication

**Deuxième passage du cycle complet** de l'objectif nº 1 de la a.2, deux jours
après le premier. L'amont était passé de `a290eb28` à `07f3c861` : **18 commits,
6 fichiers, 5 sections traduites**, toutes en classe A. Aucun dessin forké
touché — confirmé par `diff -rq` entre les deux instantanés, qui rend exactement
les 6 mêmes fichiers que l'API.

Le piège du §10 s'est présenté une fois de plus, en vraie grandeur :
`verifier_amont.py` rendait **`rc=0` sur 611 éléments** pendant que l'amont
avait 18 commits d'avance. Les deux disaient vrai. **Seul le contrôle réseau
le montrait.**

- **`polarmodulation`** (+22/−6) — réécriture pédagogique : avertissement
  explicite qu'aucune question d'examen ne porte sur le sujet, trois paragraphes
  neufs qui **construisent** l'idée au lieu de la poser, un paragraphe sur
  l'amplificateur d'enveloppe, un bloc `<indepth>` historique (HELAPS, satellite
  AO-7), et une entrée d'index. Section entièrement réécrite côté français.
- **`snr_rauschzahl`** (+6/−2) — le passage `Rauschzahl` → `Rauschmaß` n'est
  plus présenté comme une conversion mais comme deux **représentations** de la
  même grandeur ; bloc `<indepth>` neuf sur la définition DIN.
- **`verstaerker_klasse`** (+6/−6) — la linéarité n'est plus définie par la
  rectitude du tracé, c'est l'inverse : la rectitude en devient une conséquence
  observable. Et **le paragraphe sur la puissance de sortie, avec la question
  `AD424`, passe après le tableau récapitulatif** — un déplacement, pas une
  suppression.
- **`emitterschaltung`** et **`kollektorschaltung`** (+4/−4 et +2/−2) — glose de
  `bias`, précision « à la base » sur la tension d'entrée, et une phrase en
  double supprimée.

**A : 382 → 384 pages. NEA : 814 → 816 pages** — exactement les deux mêmes.
Compteurs de clamp **545 · 4 · 4** et **966 · 10 · 7**, identiques au 17/08 :
aucun clamp ne s'est mis à ne plus se déclencher. `??` à **3** et **4**, valeurs
documentées. Contrôles du §4 verts, notes de marge rétrogradées à 4 sur les deux,
`verifier_questions.py` rc=0 sur 717 et 1 750 questions.

### Corrigé — les commentaires amont de la classe N

**Les 39 écarts de `verifier_traduction.py` ont été analysés** — c'est
`docs/ecarts-traduction.md` — puis les deux premiers chantiers exécutés :
**39 → 22**.

Dix-sept sections de la classe N ne préservaient pas les blocs commentés `%…`
de l'amont, ce que le §6 range parmi ce qui est **préservé verbatim** : 42
lignes perdues sur 13 sections, 4 sections aux commentaires traduits. Ce sont
des `[photo:…]` et `[table:…]` désactivés par l'amont, des blocs `%<indepth>`
commentés, trois `% TODO: Editionsspezifisch machen`. **Rien qui s'imprime** —
ce qu'on perdait, c'est la trace de ce que l'amont a délibérément désactivé, et
donc la possibilité de voir le jour où il le réactive.

Restauration verbatim, ancrée sur le nombre de marqueurs précédant chaque bloc.
**Aucun livre recompilé, et la neutralité est prouvée** : les `.tex` de la
classe N régénérés avant et après, normalisés par retrait des commentaires
LaTeX avec recollement de ligne, sont **identiques sur les 131 sections**. Un
`%` neutralise la fin de ligne *et* le saut de ligne — les 22 lignes du diff
qui n'étaient pas des commentaires relèvent toutes de cette équivalence.

`verifier_traduction.py` gagne une dérogation : **`N/morsetelegrafie`**, dont le
`[morse:ß]` ajouté à la table du code Morse — correction livrée en a.2 — décale
d'un rang tous les marqueurs suivants. Décision prise, jamais déclarée.

### Préservé

**Trois coquilles du relevé sont sorties de `docs/defauts-amont.md`** : l'amont
a corrigé de lui-même `Blochschaltbild`, `richtet sich Die Bezeichnung` et
`im vergleich`, sans que nous les ayons jamais signalées. Les quatre autres
subsistent, vérifiées une par une. **L'amont relit son propre corpus** — c'est
l'argument le plus concret en faveur du signalement au DARC, toujours en
attente.

### Ajouté — accueil des relecteurs

- **`CONTRIBUTING.md`**, que le README appelait depuis le 14/08 sans qu'il
  existe.
- **Gabarit d'*issue* « Relecture »** en formulaire GitHub : édition, version,
  page, titre de section, nature du défaut, citation exacte. Un signalement
  réglementaire sans source officielle ne peut pas être retenu, et le formulaire
  le dit.
- **Dix labels français** : `relecture`, `traduction`, `coquille`,
  `mise en page`, `reglementaire`, `defaut amont`, et un par édition.
- **`docs/ecarts-traduction.md`** — l'analyse des 39 écarts, famille par
  famille, avec l'ordre de travail et ce que chaque chantier coûte en
  recompilation.

**E et A recompilées les 16 et 17/08/2026** après la resynchronisation amont.

- **E : 214 pages, inchangées** malgré la figure ajoutée à `antennenformen_2`.
  Compteurs de clamp **289 · 5 · 3**, contre 288 · 5 · 3 le 14/08 — la figure
  de plus, et rien d'autre. PDF compressé : 3,03 Mo.
- **A : 376 → 382 pages**, les six pages des ~3 340 mots et 15 figures ajoutés.
  Compteurs de clamp **545 · 4 · 4**. PDF compressé : 5,23 Mo.

**Les quatre contrôles du §4 sont verts sur les deux classes**, notes de marge
rétrogradées comprises (E 0, A 4). `verifier_questions.py` rc=0 sur les 1 750
questions, `sonde_dessins.py` rc=0 sur les deux classes.

**Références `??` : E 1, A 3 — inchangées.** C'est le résultat de la décision
D2 : sans le renommage du renvoi, la classe A serait passée à 4. Vérifié sur le
PDF, pas sur le journal.

- **NEA : 808 → 814 pages**, exactement les six pages gagnées par A. 383
  sections, 1 751 usages de questions, 202 dessins francisés, 64 encarts.
  Compteurs de clamp **966 · 10 · 7**. Quatre contrôles du §4 verts, notes de
  marge rétrogradées à 4. **`??` : 4** — les trois de A plus celle de E, toutes
  documentées au §8.

**La classe N n'est pas recompilée** — aucune de ses sections n'était touchée
par la dérive amont.

Deux mots allemands subsistent dans le NEA (`Sperrkreis`, `Mantelwellensperre`,
4 occurrences) : ce sont des **gloses délibérées**, le terme allemand donné
entre parenthèses après sa traduction française. Pratique établie du corpus, et
utile puisque le lecteur passera un examen allemand.

`sonde_dessins.py` n'est pas lançable sur une édition combinée — elle indexe
les forks par `traductions/<CLASSE>/dessins`, qui n'existe pas pour NEA. Les
trois classes ont été sondées séparément, ce qui couvre le même corpus de
dessins.

Pagination inchangée après la francisation des dessins du 15/08, et compteurs de
clamp identiques à ceux du 14/08 (E : 288 · 5 · 3) — les libellés traduits n'ont
pas dérangé la mise en page.

Effet mesuré des corrections, sur les trois classes :

| mesure | a.1 | a.2 |
| --- | ---: | ---: |
| plus grand débordement horizontal (N · E · A) | 125 · 104 · 200 pt | **20 · 11 · 11 pt** |
| débordements > 20 pt (N · E · A) | 1 · 8 · 17 | **0 · 0 · 0** |
| pages « Underfull \vbox » (total) | 306 | **0** |
| questions séparées de leurs réponses | 19 relevées en N | **0 sur 1 750** |
| figures ramenées dans leur gabarit | 0 | **948** |
| tableaux et formules réduits | 0 | 10 et 9 |
| dessins affichant de l'allemand | 62 | **0** (24 au 14/08, puis 93 mesurés et traités le 15/08) |
| dessins forkés | 126 | **222** |

**Plus aucun débordement au-delà de 20 pt dans les trois livres**, alors qu'il y
en avait vingt-six, dont un à 200 pt.

**Chantier de mise en page**, ouvert après la relecture page à page de Pierre
(une quarantaine de défauts relevés sur les trois livres). Le parti pris a été
de chercher les causes racines plutôt que de retoucher page par page : quatre
corrections de classe, puis deux de plus, ont remplacé l'essentiel des
retouches ponctuelles.

### Ajouté
- **Typographie française** (A1). Les trois livres étaient composés avec la
  césure et les espacements **allemands** : le `.sty` amont fait
  `\PassOptionsToPackage{ngerman}{babel}`, et rien ne l'avait jamais corrigé.
  Mesuré par `\showhyphens` : « ali-men-ta-ti-on », « ray-onne-ment » — des
  coupures allemandes, fautives en français. Corrigé par le mode **moderne** de
  babel (`\babelprovide[import, main, transforms = punctuation.space]{french}`),
  qui insère les espaces fines avant « : ; ! ? » par transformation de nœuds
  LuaTeX, sans rendre aucun caractère actif — contrairement à `french.ldf`,
  dont les catcodes actifs se seraient heurtés à la syntaxe à deux-points de
  siunitx, tcolorbox, circuitikz et pgfplots. Chaque règle pose une pénalité de
  10000 : la ponctuation haute ne peut plus tomber en début de ligne.
  Conventions françaises complètes ajoutées explicitement : puces en tiret
  cadratin, listes resserrées, légendes « Fig. 1 – ».
- **Contrôle exact des questions coupées** (B6) : deux `\label` par question,
  comparés dans le `.aux` par `verifier_questions.py`. Remplace une lecture du
  PDF qui produisait douze faux positifs sur la seule classe N.
- **Sonde anti-germanisme sur les dessins** : `sonde_dessins.py`. Elle sépare
  les dessins **forkés** portant encore de l'allemand — un défaut — des dessins
  **non forkés**, qui sortent tels quels de l'amont et relèvent du chantier de
  francisation.

### Corrigé
- **Clamp de `\DARCimage` : il ne clampait rien** (A2). Il mesurait `\wd` d'une
  boîte contenant déjà le `\makebox[\linewidth]` final de la macro amont ; sa
  mesure valait donc toujours `\linewidth`. Vérifié sur quatre dessins d'essai,
  du minuscule au démesuré : 147,95 pt en marge et 335,74 pt dans le corps,
  sans une seule variation. Pire, dès que la cible était inférieure à
  `\linewidth`, la comparaison était vraie par construction et réduisait une
  figure conforme **au carré du facteur demandé** — une figure appelée à
  `0.5\linewidth` sortait à `0.25\linewidth`. 242 appels étaient concernés.
  La hauteur, elle, n'était comparée à rien. Réécrit : il mesure la boîte de
  l'autoscale amont avant tout `\makebox`, et borne largeur **et** hauteur.
- **Zones de vide** (A3). Le livre composait en `\flushbottom` alors que la
  classe amont fait `\raggedbottom` : le blanc laissé par un objet insécable
  était distribué entre les paragraphes au lieu d'être rassemblé en bas de
  page. 306 pages étaient concernées sur les trois classes.
- **Questions séparées de leurs réponses** (A4). L'énoncé est un paragraphe,
  les réponses un `tabular` insécable, et la boîte est `breakable` : la
  jointure était le seul point de rupture possible. Corrigé par `\samepage`.
- **Tableaux et formules débordant de la colonne de marge** (B1). Une fois les
  figures traitées, 151 des 180 débordements restants étaient du contenu
  insécable dans une colonne de 52 mm — jusqu'à 168,9 pt pour un tableau,
  97,2 pt pour une formule. Clamp analogue à celui des images.
- **Code Morse (classe N)** : quatre des cinq lignes du tableau des caractères
  spéciaux étaient fausses. Détail dans `docs/defauts-amont.md` §4.
- **Douze accolades imprimées** dans les énoncés de questions de la classe N
  (« ne devriez-vous **{pas}** établir… »), présentes depuis la a.1 : du LaTeX
  écrit dans un champ qui traverse le renderer, lequel échappe les accolades.
  Rétabli en markdown.
- **Dix dessins forkés** portaient encore de l'allemand (N 3 · E 5 · A 2),
  traduits avec le vocabulaire déjà en usage dans le corpus.

- **Francisation des dessins : 38 dessins forkés et traduits**, portant le total
  de 126 à 164. Les dessins affichant encore de l'allemand passent de 62 à 24
  (N 4 → 1 · E 21 → 10 · A 37 → 13). Le vocabulaire suit l'usage déjà établi
  dans les sections, relevé par comptage : « intensité de champ » (44 emplois),
  « longueur d'onde » (71), « porteuse » (177), « atténuateur » (36).
  La substitution ne touche **que les textes composés** — contenu de `\node{}`,
  `label=`, `\addlegendentry{}` — jamais le reste du fichier, où « der », « und »
  et « oder » se retrouvent dans des noms de macros et des clés de style. Les
  164 dessins forkés ont été compilés isolément avant toute recompilation :
  zéro erreur.
- **Pièces liminaires renommées** : `avant-propos-N.md` → `avant-propos.md` et
  `remerciements-N.md` → `remerciements.md`. Leur texte ne mentionne aucune
  classe et `compiler.bat` les imposait déjà aux trois : le suffixe `-N` était
  trompeur.
- **Tableau `{lX}` de `widerstand_materialien`** (classe E) : ne déborde plus.
  Sa colonne rigide portait « Résistances à couche d'oxyde métallique »
  (39 caractères) là où l'allemand tenait en 28 ; première colonne passée en
  `X`, sans toucher au texte.
- **Francisation des dessins, achevée** (15/08/2026, feuille d'arbitrage nº 3).
  L'inventaire a été refait par mesure sur la version **réellement composée** de
  chaque dessin — 861 couples (classe, dessin), 418 mots distincts extraits des
  seules zones de texte composé. Il a montré que le périmètre n'était pas de 24
  dessins mais de **93**, et surtout que **39 d'entre eux étaient des dessins
  forkés affichant encore de l'allemand dans les PDF a.2 livrés** :
  `Wert`, `Distanz`, `Mischer`, `Koaxialkabel` ne figuraient dans aucune des
  deux détections de la sonde, qui rendait `rc=0`.
  - Le plus visible : le dessin **1092** composait « 2. AM de 1 : Einton
    moduliert Amplitude de la porteuse ». Le dessin **996**, forké sur
    8 782 lignes, n'avait vu traduire que « Höhe » : sa légende portait encore
    *Winter Nacht, Sommer Tag* et son axe *Distanz [km]* voisinait avec un axe
    *Hauteur [km]*. Les dessins **434** et **435** affichaient « Auf le Signal
    perturbateur abgestimmt », moins lisible que l'allemand d'origine.
  - Traitement par **remplacements littéraux comptés** (chaîne exacte vers
    chaîne exacte, échec fatal sur écart de comptage), et non par substitution
    mot à mot — celle-ci étant justement la cause des libellés mixtes.
  - Dictionnaire établi par **comptage dans les 387 sections traduites**
    (1,94 M caractères) : *mélangeur* 117 contre *mixeur* 0, *atténuateur* 52
    contre *affaiblisseur* 0. `Treiber` → « Étage pilote » et `Stromrichtung` →
    « sens physique du courant » ont été réglés par un précédent déjà composé
    dans les livres, ce qui vaut mieux qu'un comptage.
  - Six arbitrages tranchés par Pierre : `Verbraucher` → charge ·
    `Einton`/`Zweiton` → un ton / deux tons · `Netzteil` → alimentation
    secteur · `Ort` → position · `Langwelle`/`Mittelwelle` → ondes longues /
    ondes moyennes · `Frequenzgemisch` → mélange de fréquences.
  - Deux angles morts trouvés en chemin : le texte en **mode mathématique**
    (dessin **488**, `$\mathrm{Audioverstärker}$`, `NF` passé à `BF`) et le
    **symbole `ü`** du rapport de transformation (dessins 260, 303, 315),
    remplacé par `m`.
  - **222 dessins forkés** au total, tous compilés isolément sans erreur avant
    toute recompilation de livre, tous enregistrés au manifeste (606 éléments
    suivis par `verifier_amont.py`, 0 dérive).
- **« CCathode » corrigé** (dessins 666, classes N et E). Un fork antérieur
  substituait `Kathode` → `Cathode` **puis** `athode` → `Cathode`, la seconde
  règle s'appliquant au résultat de la première : le livre imprimait un mot
  d'aucune langue, **depuis la a.1**, sans que la relecture l'ait relevé. Le
  libellé amont tronqué qui l'a rendu possible est consigné en défaut amont
  (`docs/defauts-amont.md` §5).
- **Le symbole `ü` du rapport de transformation remplacé par `m`** — 18
  occurrences dans 5 sections (A : `uebertrager_2` 10, `antennenformen_3` 2,
  `brueckengleichrichter` 1, `mantelwellen_2` 1 · E : `uebertrager_1` 4).
  Un `ü` **nu** en mode mathématique est composé dans l'italique mathématique,
  qui n'a pas le glyphe : il **disparaissait du PDF** sans erreur de
  compilation. Mesuré au journal — `Missing character U+00FC` sortait 17 fois
  en classe A et 5 fois en E. Le cas le plus grave n'était pas celui qui avait
  été relevé en a.1 : dans `uebertrager_2`, **la formule centrale du chapitre
  sur les transformateurs s'imprimait sans son membre de gauche**, et
  `antennenformen_3` donnait « un rapport de spires **()** de 1:7 ».
  Dérogation à la règle « formules `$…$` verbatim » assumée par Pierre, et
  cohérente avec la décision du même jour sur les dessins 260, 303 et 315 : sans
  elle, les figures auraient dit « m » et le texte rien. Le remplacement n'a eu
  lieu que dans les spans `$…$` — le commentaire allemand `prüfen` et l'ident
  de photo `Brückengleichrichter` sont intacts. Détail dans
  `docs/defauts-amont.md` §2.
- **`$\text{Ordnung}=m+n$` → `$\text{Ordre}=m+n$`** validé, et la légende
  « 3. Ordnung » du dessin 1096 traduite en « ordre 3 ». La décision, en
  suspens au §9 depuis plusieurs sessions, est close ; la dérogation à la règle
  « math verbatim » est assumée.

- **Relecture de la classe E, feuille d'arbitrage nº 4** (15/08/2026). Dix points
  relevés par Pierre sur le livre E, tous reproduits et leur cause mesurée, puis
  cherchés systématiquement en N et A.
  - **Nombres gras dans les énoncés** (v0.19, ci-dessous). Deux réglages
    seulement sur les dix touchaient les trois livres ; c'est le principal.
  - **Dessin 942** : « Bobine à noyau de ferrite » (25 caractères contre 20 à
    « Spule mit Ferritkern ») faisait se toucher les libellés voisins. Passés
    sur deux lignes.
  - **Dessins 911 et 96** : « Traitement numérique du signal » sortait de son
    encadrement, dont la largeur est fixée. Texte sur trois lignes en un seul
    nœud centré, boîte élargie. *Première tentative écartée* : deux nœuds
    ancrés au nord et au sud se chevauchaient, la boîte n'ayant pas la hauteur
    de trois lignes — vu à l'image, la compilation sortant en `rc=0`.
  - **Dessin 666** : « Anode » et « Cathode » écrits en entier. Le dessin porte
    un aide-mémoire où les tracés rouge et bleu forment un **A** et un **K** que
    le texte complète (*A*+*node*, *K*+*athode*). Le procédé ne survit pas au
    français, *Cathode* ne commençant pas par K.
  - **Dessins 434 à 437** (classe A, défaut non signalé, trouvé en cherchant les
    équivalents) : le livre affichait « 1/2 **le Longueur** d'onde » et « **le
    Fréquence** perturbatrice », l'amont « 1/2 der Wellenlänge / der
    Störfrequenz » ayant subi la substitution mot à mot du 14/08. Corrigé, puis
    **les libellés ancrés à l'est** : le français, plus long que l'allemand,
    chevauchait le circuit. Le texte croît désormais vers la gauche et ne peut
    plus l'atteindre.
  - **`spannungsteiler_1`** : point parasite avant un deux-points, reproduit de
    l'amont (`Formelsammlung finden.:`). Corrigé côté français.
  - **Préservés sur décision de Pierre** : l'espace fine avant `!` et `?`
    (babel applique la règle de l'Imprimerie nationale — 0,5 unité contre 1,0
    avant `:` ; ce n'est pas un bogue), l'absence de point devant les formules
    hors texte (usage allemand constant, 16 cas en E et 26 en A), et
    l'abréviation « OW » d'*Oberwellen*, que les légendes françaises emploient
    déjà.
  - **Une entrée de `docs/defauts-amont.md` rétractée** : le §5, écrit le matin
    même, qualifiait à tort l'aide-mémoire du dessin 666 de « libellés
    tronqués » et proposait de le signaler au DARC. Conclusion tirée du source
    sans regarder la figure. L'entrée est conservée sous forme rétractée.

- **Édition combinée NEA compilée pour la première fois** (15-16/08/2026) :
  **808 pages**, 384 sections, 1 751 questions, 805 dessins. Contrôles du §4
  conformes du premier coup, 4 références « ?? » — les quatre orphelines amont
  cumulées, rien de nouveau. Les compteurs de clamp cumulent proprement (948
  figures, 10 tableaux, 7 formules), ce qui confirme qu'aucun dessin n'est
  traité différemment en édition combinée. Durée : environ 1 h 15 pour cinq
  passes, contre 50 min pour la classe A seule.
  Un premier tirage avait donné 806 pages avec l'ordre `N, E, A` ; les deux
  pages d'écart viennent de `N_Ende`, dont la version A est plus longue que
  celle de N (5 497 octets contre 5 224). C'est la seule différence de contenu
  entre les deux tirages.
  - **Ordre des `--translations` arrêté : `A` en premier**, puis `E`, puis `N`.
    La portée du choix est étroite et a été mesurée : **une seule section** est
    traduite dans plusieurs classes, `N_Ende` (« Conclusion du cours »), du
    contenu français dont les trois versions renvoient chacune à l'examen de
    leur classe. Les **20 dessins forkés partagés sont identiques au contenu** —
    deux d'entre eux ne diffèrent que par leurs fins de ligne, CRLF contre LF.
  - **`vorwort` n'est pas dans le NEA.** La section est traduite et figure dans
    le livre N, mais le sommaire amont du NEA ne l'appelle pas : l'édition
    combinée perd l'avant-propos allemand. C'est aussi l'origine de
    l'avertissement « clé *vorwort* n'est pas un ident connu » de `titles.json`.

### Ajouté
- **Resynchronisation amont du 16/08/2026** — feuille d'arbitrage nº 5. C'est
  l'objectif nº 1 de la a.2, « suivre les évolutions des documents allemands »,
  concrétisé pour la première fois.
  Notre instantané a d'abord été identifié **par empreinte git** et non par la
  date des fichiers : ses 385 sections sont byte pour byte l'amont au commit
  `a74ed171`. Cela a corrigé le périmètre annoncé la veille — **23 commits et
  23 sections, non 28 et 28**. Cinq sections données pour en retard étaient
  déjà à jour, dont `antennenformen_3`, présentée comme le plus gros morceau du
  chantier.
  **22 sections traduites** (21 en A, 1 en E), environ 3 340 mots de prose
  allemande, dont ~1 900 inédits. **15 figures** nouvellement appelées, avec
  leurs légendes. **2 tableaux** amont neufs (`a_rg58`,
  `a_kabel_phasenverschiebung_table`). Aucune question perdue ni gagnée : les
  neuf mouvements sont des déplacements entre sections, la classe A reste à
  717 questions.
- **2 dessins forkés et francisés** : 1106 (« Richtantenne », « Dipol ») et
  **633 (« Dipolschenkel »)**. Le second était **déjà composé dans les livres E
  et A** : le mot figurait dans les PDF a.2 relus. `sonde_dessins.py` ne l'avait
  jamais vu — la liste contenait « Dipol », mais ses frontières de mot ne
  mordent pas dans un composé. Sonde passée en **v0.3**.

- **`verifier_traduction.py` (v0.1)** — mécanise les huit contrôles du §5 :
  marqueurs DARCdown (nombre, nature **et ordre**), formules verbatim,
  séparateurs, puces, commentaires, légendes sans « : », accents nus en mode
  mathématique, sonde anti-germanisme. C'est lui qui a fait remonter l'erreur
  des 6,25 mV ci-dessous.
  Il documente honnêtement **trois limites**, chacune payée par un faux
  positif : il ne voit pas une prose périmée (sur 21 sections en retard il en
  a signalé 19) ; il compte un ajout français hors encart `<france>` comme un
  écart ; et il prend une **glose allemande volontaire** pour un germanisme —
  dans `q_schluessel`, le mot allemand porte le moyen mnémotechnique du code Q,
  « grande puissance (gr*o*ße Leistung) » expliquant le O de QRO.
  État mesuré au 17/08 sur 386 sections : **345 conformes, 2 dérogations,
  39 écarts préexistants** non analysés, dont un commentaire amont réellement
  perdu dans `antennen`.

### Corrigé
- **`digital_analog_umsetzer` : un pas de quantification faux dans un livre
  livré.** La traduction avait perdu la phrase d'avertissement de l'amont
  (« avec 16 échelons, il n'y a que 15 pas intermédiaires »), rendu
  *Zwischenschritte* par « échelons », et affichait un pas de
  **$\qty{6,25}{\milli\volt}$ au lieu de $\approx\qty{67}{\milli\volt}$**.
  Trouvé en outillant les contrôles du §5, pas à la relecture.

### Supprimé
- **`frequenzabhaengige_stromverteilung`** (classe A), effacée en amont —
  fichier, entrée de sommaire, ligne de manifeste et titre. Ses quatre
  questions `AG203`–`AG206` sont reprises par `strom_spannung_speisung_2`, dans
  un texte neuf qui explique le phénomène au lieu de l'annoncer.

### Préservé
- **Label dupliqué `a_richtkoppler_rechts_links`** — les dessins 1109 et 1110
  déclarent le même label dans `swr_meter_2`, et le texte y renvoie deux fois.
  Préservé verbatim, légendes traduites.
- **`\qty{0,66}{\percent}`** pour le coefficient de vélocité d'un RG-58
  (tableau `a_rg58`) : erreur d'unité d'un facteur cent. Préservée, signalée.

### Modifié
- **Renommage de label `e_stromverteilungen` → `a_stromverteilungen`**, adopté
  sur **les deux lignes** — la figure et le renvoi. L'amont n'avait renommé que
  la figure ; comme `strom_spannung_speisung_1` n'est pas au sommaire de la
  classe A, le renvoi y pendait et **aurait fait passer la classe A de 3 à 4
  `??`**. Vérifié après coup : la référence a disparu de la liste des
  orphelines. Dérogation assumée à « marqueurs identiques à l'amont ».
- **`compiler.bat` : l'interpréteur Python est désormais essayé, pas supposé.**
  Chaque candidat (`OHM_PYTHON`, venv du générateur, `py -3.14/-3.13/-3.12`,
  `python`) doit prouver qu'il importe `mistletoe` à une version ≥ 3.12.
  L'ancienne règle fonctionnait ici — le venv `uv` du générateur est bien en
  place — mais son repli était un piège : sur une machine sans venv, elle
  retenait le `python` du PATH sans le vérifier, qui est ici celui d'Inkscape,
  en 3.9 et sans `mistletoe`.
- **`build_book.py` v0.21 : `\qty{5}{8}` → `\ensuremath{\frac{5}{8}}`.**
  Troisième défaut de la famille des v0.14 et v0.16 — une construction siunitx
  que l'amont n'écrit pas comme il la pense — mais le premier où l'erreur porte
  sur le **nombre et l'unité à la fois** : « 8 » y est passé comme unité de
  « 5 ». Cas amont : la légende du dessin 650, appelée par
  `elektrische_verlaengerung_verkuerzung` depuis le refactor du 14/08. Le corps
  de la **même section** écrit pourtant `\frac{5}{8}\lambda` trois fois — la
  coquille est certaine.
  **Mesuré sur document réduit puis extraction du PDF : la compilation réussit
  sans erreur et la légende compose « 58λ »**, barre de fraction perdue. Même
  signature que la v0.16 : aucune alerte, un rendu faux.
  `\ensuremath` plutôt qu'un `\frac` nu, parce que `\qty` s'emploie aussi hors
  mode mathématique dans le corpus, où un `\frac` nu ferait échouer la
  compilation ; vérifié dans les deux modes.
  **La portée a été mesurée avant d'écrire la règle**, et c'est ce qui l'a
  gardée étroite. Les `\qty{}{}` douteux du corpus se rangent en quatre
  familles, dont **deux seulement composent faux** :

  | famille | exemple | rendu | verdict |
  | --- | --- | --- | --- |
  | unité numérique | `\qty{5}{8}` | « 58 » | **cassé** — traité ici |
  | unité macro | `\qty{0.625}{\lambda}` | « 0,625 » | **cassé** — v0.16 |
  | unité vide | `\qty{30}{}` | « 30 » | sain |
  | unité en texte nu | `\qty{10}{dB}` | « 10 dB » | sain |

  Les **71 occurrences** de la dernière famille (`\qty{0,3}{V}`, `\qty{-5}{dBm}`
  dans 25 dessins) rendent exactement comme leur équivalent en macro siunitx :
  les convertir n'aurait rien corrigé et aurait touché des dessins déjà livrés.
  Elles restent en l'état. Neuf cas de test couvrent la règle, dont **quatre
  `\qty` légitimes qu'elle ne doit pas toucher**.
  Décision de Pierre du 16/08/2026 : appliquer la règle **et** corriger la
  légende côté français, les deux. La source amont n'est pas touchée.
- **`build_book.py` v0.20 : filigrane de la page de titre empilé.** Le bandeau
  de droite fait 0,34 de la largeur du papier, soit 71 mm en A4. La v0.9
  réduisait le corps du filigrane à mesure — 220 pt pour une lettre, 150 pour
  deux, 105 pour trois. **Mesuré sur épreuve : « NEA » à 105 pt débordait
  encore**, le N mordant sur la zone blanche à gauche et le A se faisant couper
  au bord droit. Dès deux lettres, elles sont désormais empilées une par ligne,
  centrées sur l'axe du bandeau et calées en haut, à 150 pt — lisibles à
  l'endroit, et sans débordement. Une lettre seule est inchangée.
  L'ancien gabarit ne pouvait faire varier que le corps et le texte, jamais
  l'ancrage ni la position : le nœud entier est maintenant construit côté
  Python. Trois dispositions ont été composées et comparées sur épreuve — à
  plat, pivotée à 90°, empilée — avant la décision de Pierre.
- **`build_book.py` v0.19 : nombres gras dans les énoncés de question.** Une
  ligne, pour un défaut qui touchait **418 énoncés** — N 102, E 122, A 194, soit
  un sur quatre. Le parseur amont rend « 230 V » par « `$230$\,V` », et le mode
  mathématique n'hérite pas du gras du texte.
  Le diagnostic a d'abord visé la définition de `\Question` ; elle était hors de
  cause. **L'amont demande déjà le gras mathématique**
  (`\newkomafont{questiontext}{\bfseries\boldmath}`), mais `settings.tex` charge
  `unicode-math` sans déclarer de version mathématique grasse : `\boldmath` est
  alors sans effet, **et sans le moindre avertissement**. Correctif :
  `\setmathfont[version=bold, FakeBold=2]{Libertinus Math}` après
  `\input{settings.tex}` — Libertinus Math n'ayant pas de fonte grasse compagne,
  le gras est synthétique. Vérifié sur document réduit avant application, puis
  dans le livre (question NA212, classe N).
- **`sonde_dessins.py` v0.2** : la liste de mots reçoit les termes de la feuille
  d'arbitrage nº 3. « Signal », « Filter » et « Band » ont été essayés puis
  **retirés** — ils sont aussi français et produisaient du bruit ; « Tag » et
  « Ort » sont écartés pour la même raison.
- **`verifier_amont.py` v0.3 : détection des forks absents du manifeste.** Le
  script ne comparait l'amont qu'aux entrées **déjà** enregistrées ; un fork
  créé sans `enregistrer` lui était donc entièrement invisible, et n'aurait
  **jamais** été signalé en dérive. Trois dessins de la classe A (260, 303, 315)
  étaient dans ce cas, forkés après un `initialiser` : `verifier` répondait
  « 261 éléments suivis, 0 dérive » sans rien dire. Le script compte désormais
  les fichiers réellement présents dans `dessins/` et `sections/` — c'est le
  dossier qui fait foi, le manifeste n'étant que sa mémoire — et sort en `rc=1`
  sur tout fork non suivi. Testé sur les trois cas : arbre propre (`rc=0`), fork
  jetable non enregistré (`rc=1`, signalé), retour à l'état propre (`rc=0`).

### Connu
- Les tableaux à colonne `X` échappent au clamp : `tabularx` fixe leur largeur
  à `\linewidth`, si bien que la mesure est toujours conforme même quand le
  contenu déborde. Ces cas se corrigent à la source, pas dans la classe.
- ~~**24 dessins affichent encore de l'allemand**~~ — **traité le 15/08/2026,
  et le compte était très en deçà de la réalité** : voir *Corrigé* ci-dessus.
- `sonde_dessins.py`, même enrichie, **lit le source TikZ et non le PDF**, et sa
  détection reste une liste de mots. Elle donnera toujours un plancher. Le
  contrôle qui a réellement trouvé les 39 défauts — extraction des zones de
  texte composé, puis relecture — est reproductible (méthode décrite au §4 de
  `docs/ANALYSE-DESSINS.md`) mais n'est pas outillée au dépôt.
- **La classe A passe de 3 à 4 notes de marge rétrogradées.** `schwingkreis_2`
  contient 22 formules hors texte ; la redéfinition de `displaymath` coûte
  environ 1 pt à chacune, et la note franchit le seuil de 23 pt. Pas d'erreur de
  compilation — le garde-fou la compose dans le corps, en boîte sécable — mais
  une section change de mise en page.

---

## a.1 — 14 août 2026

**Première release publiée.** Les trois classes portent désormais un numéro de
version commun. Les versions par classe antérieures (N v0.9, E v0.9, A v1.2)
restent consignées plus bas à titre historique.

| Classe | Sections | Questions | Encarts | Pages |
| ------ | -------: | --------: | ------: | ----: |
| N | 131 | 571 | 55 | 254 |
| E | 103 | 462 | 6 | 206 |
| A | 153 | 717 | 5 | 372 |

### Ajouté
- **Avant-propos et remerciements** dans les trois livres, en chapitres non
  numérotés inscrits au sommaire. C'est ce qui distingue `a.1` des versions par
  classe qui précèdent, et ce qui explique environ deux pages de plus chacune.
- Squelette de dépôt public : README, LICENSE, NOTICE, CONTRIBUTING,
  GUIDE-GITHUB, `.gitignore`, `docs/defauts-amont.md`.
- **Suivi de la dérive amont étendu aux sections.** `verifier_amont.py` suit
  513 éléments — 126 dessins forkés et 387 sections traduites — en comparant
  l'empreinte SHA-256 de l'original allemand à celle enregistrée. Il remplace
  `verifier_dessins.py`, qui ne couvrait que les dessins.

### Modifié
- **Resynchronisation de quatre sections de classe A** sur la dérive amont :
  `antennenformen_3`, `photovoltaik`, `polarisation_3`, `remote_station`. Du
  contenu allemand ajouté en amont depuis notre traduction manquait au livre
  français sans qu'aucun signal ne le révèle.
- Paginations relevées sur amont à jour : 254 · 206 · 372.
- `compiler.bat` localise seul les dépôts amont et l'interpréteur, au lieu de
  chemins codés en dur.

### Corrigé
- **Les pièces liminaires manquaient à toute compilation lancée par
  `compiler.bat`** : l'option `--front-matter` n'y figurait pas.
- `build_book.py` v0.16 — `\qty{0.05}{\lambda}` : `\lambda` n'étant pas une
  unité siunitx, le glyphe disparaissait du PDF sans la moindre erreur, et le
  lecteur lisait « au moins 0,05 », sans unité.
- Détection de Ghostscript en 32 bits, dont l'exécutable console porte un autre
  nom que celui de la version 64 bits.
- Le décompte des références non résolues se fait désormais dans le PDF et non
  dans le journal, qui ne conserve que la dernière passe et sous-compte.

### Préservé
- **Référence orpheline `a_zeppelinantenn`** dans `antennenformen_3` : l'ident
  est tronqué en amont, le dessin déclarant `a_zeppelinantenne`. Sort en `??`,
  côté allemand comme côté français.
- **`$ü = 1:7$`** dans la même section : un caractère accentué nu en mode
  mathématique est composé dans l'italique mathématique, qui n'a pas le glyphe.
  L'umlaut disparaît du PDF, dans les deux langues.

### Connu
- **Discordances texte / figure.** Les indices allemands des formules ont été
  francisés dans le corps du texte, mais tous les dessins TikZ amont ne le sont
  pas encore : **126 dessins francisés sur 403 référencés** par les sections
  traduites (N 81 · E 156 · A 199). Exemple : le dessin 1082 affiche
  « Taktgenerator » là où le texte écrit `f_horloge`.
- **20 dessins à double citation.** Ils sont appelés à la fois par une section
  et par une question d'examen. Les franciser modifierait simultanément une
  illustration officielle de la BNetzA — arbitrage en attente.
- Terminologie en attente de validation : rendu de l'acronyme ERP,
  `\text{Ordnung}` dans une formule, indice `P_\mathrm{S}` non résolu.
- Trois notes de marge de la classe A dépassent la hauteur de colonne et sont
  rétrogradées dans le corps du texte par le garde-fou prévu à cet effet.

---

## Classe A

### v1.2

#### Ajouté
- Traduction française complète : 153 sections, 717 questions.
- 5 encarts « En France ».
- 368 pages, pagination paire garantie pour un dos carré collé.

#### Connu
- Dessins 1096 et 687 : dimensions hors gabarit non résolues. Le clamp de
  `\DARCimage` ne borne que la largeur.

---

## Classe E

### v0.9

#### Ajouté
- Traduction française complète : 103 sections, 462 questions.
- 6 encarts « En France ».
- 202 pages.

#### Corrigé
- Dessin 202 (diagramme d'affaiblissement des câbles) : l'axe pgfplots fixait
  ses propres dimensions, 21 × 29 cm, que l'autoscale amont n'atteint pas.
  Placée en note de marge, la figure devenait inplaçable ; `marginfix` perdait
  cette note et toutes les suivantes, et la classe E ne compilait plus du tout.
  Le dessin est désormais précompilé isolément à 52 mm et substitué par un
  `\includegraphics`.

---

## Classe N

### v0.9

#### Ajouté
- Traduction française complète : 131 sections, 571 questions.
- 55 encarts « En France » — la classe N concentre l'essentiel des
  divergences réglementaires.
- 252 pages.

#### Modifié
- Deux points corrigés par rapport à la documentation radioamateur
  francophone courante :
  - **Seuil d'urbanisme porté de 2 m² à 5 m²**, en application du décret
    n° 2024-1023 du 13 novembre 2024, pour les demandes déposées à compter du
    1<sup>er</sup> décembre 2024.
  - **Attribution des indicatifs fondée sur l'adresse de la station
    déclarée**, et non sur le domicile fiscal, depuis l'arrêté du
    2 mars 2021.
- Mention du droit d'opposition à la publication dans l'annuaire ANFR
  (« liste orange »), instauré par le même arrêté.

---

## Défauts amont préservés

Constatés dans les sources allemandes, **volontairement non corrigés** dans
l'œuvre dérivée, consignés dans `docs/defauts-amont.md` et destinés à être
signalés au DARC :

- 20 libellés dupliqués ;
- 5 légendes cassées par un caractère `:` — le parseur amont impose
  `caption = [^:\]]+` ;
- 5 références orphelines, dont `a_zeppelinantenn` relevée le 14/08/2026 ;
- défauts d'emploi de siunitx et coquilles diverses ;
- syntaxe `\tikzstyle{…};` dépréciée, 22 occurrences sur 21 dessins.

---

## Historique du générateur

Le journal détaillé de `build_book.py` figure dans l'en-tête du script
lui-même, où chaque version documente le défaut qu'elle corrige et sa cause
racine.
