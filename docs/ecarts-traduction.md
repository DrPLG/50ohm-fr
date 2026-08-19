# Les 39 écarts de `verifier_traduction.py` — analyse

`verifier_traduction.py --tout` sort en `rc=1` sur le dépôt entier depuis sa
mise en service, le 17/08/2026 : **386 sections, 345 conformes, 2 dérogations
assumées, 39 écarts**. Ces 39 étaient **préexistants et non analysés**.

Ce document les analyse. Mesure refaite le **19/08/2026**, après la
resynchronisation sur l'amont `07f3c861` : **le compte n'a pas bougé**, les
cinq sections retraduites ce jour-là n'en ajoutent aucun.

> **ÉTAT AU 19/08/2026, APRÈS EXÉCUTION DES RANGS 1 À 3 : 39 → 22.**
> Décision de Pierre du 19/08/2026, prise sur la foi de l'analyse ci-dessous et
> exécutée le jour même, avant la release `a.2`.
>
> | | écarts |
> | --- | ---: |
> | mesure initiale, 17/08 | 39 |
> | après restauration des commentaires et dérogation `morsetelegrafie` | **22** |
>
> Les **17 sections de la classe N sont sorties de l'écart**, sauf
> `analog_vs_digital`, qui signale aussi une formule ajoutée. Les 22 restants
> sont analysés aux familles 2, 3 et 4 ci-dessous, et **aucun n'est un défaut**
> hormis les deux ajouts hors `<france>`.
>
> **Aucun livre n'a été recompilé**, et la preuve est au §1 : le LaTeX effectif
> est identique sur les 131 sections de la classe N.

---

## Vue d'ensemble

| famille | sections | verdict |
| --- | ---: | --- |
| **commentaires amont non préservés** | **17** | **vrai défaut** — §6 violé |
| germanismes possibles | 11 | **faux positifs** |
| formules dans les encarts `<france>` | 7 | limite documentée du script |
| marqueurs DARCdown différents | 4 | 3 connus, 1 à trancher |
| | **39** | |

Répartition par classe : **N 25 · E 7 · A 7**. Le déséquilibre n'est pas un
hasard : **les 17 pertes de commentaires sont toutes en classe N**, la première
traduite.

---

## 1. Commentaires amont non préservés — 17 sections, toutes en N

C'est la seule famille qui contrevient à une règle explicite. Le §6 de
`CLAUDE.md` range les blocs commentés `%…` allemands, `%TODO` compris, parmi ce
qui est **préservé verbatim**.

Deux cas distincts :

| cas | sections | lignes |
| --- | ---: | ---: |
| commentaires **perdus** (amont > français) | 13 | **42** |
| commentaires **traduits** au lieu d'être laissés en allemand | 4 | — |

### Ce que contiennent les 42 lignes perdues

Rien qui s'imprime. L'inventaire est homogène :

- des `[photo:…]` **mis en commentaire par l'amont** — 9 lignes, dont sept dans
  la seule `funkfernschreiben` (des illustrations d'écrans FT8, Olivia, AM, FM) ;
- un tableau entier des procédés *Digital Voice* dans `digital_voice`, avec son
  `[table:…]`, son `<webmargin>` et un `% TODO:` qui dit pourquoi il est
  désactivé : « Auf die Tabelle wird nicht eingegangen und sie ist nicht
  komplett » ;
- des blocs `%<indepth>` et `%<margin>` désactivés, avec leur prose ;
- trois `% TODO: Editionsspezifisch machen` ;
- une paire `%[class:N]` / `%[/class]` ;
- quelques paragraphes de prose commentés, dont deux renvois au
  *Rufzeichenplan*.

### Gravité, et pourquoi elle est faible mais réelle

**Aucune de ces lignes n'apparaît dans le livre.** Ce n'est pas un défaut que
le lecteur puisse rencontrer.

Ce qu'on perd est ailleurs : ces blocs sont la trace de ce que **l'amont a
délibérément désactivé**. Le jour où le DARC réactive le tableau *Digital
Voice* — son `% TODO:` dit exactement à quelle condition — notre version
française n'en saura rien, parce que le commentaire n'y est plus pour être
comparé. C'est le même mécanisme que la dérive amont : ce qui n'est pas suivi
ne se signale pas tout seul.

Le cas des **4 sections aux commentaires traduits** est plus bénin encore, mais
c'est le même principe à l'envers : le commentaire est là, il ne correspond
simplement plus à l'amont, donc la comparaison ne se fait plus.

### Mesuré : la réparation ne changerait aucun livre

Vérifié le 19/08/2026 sur `N/ausbildungsrufzeichen`, section qui a **conservé**
ses commentaires. Un commentaire DARCdown ressort dans le `.tex` généré en
**commentaire LaTeX** :

```
%[photo:57:n_ausbildungsrufzeichen_…]      <- dans le .md français
% [photo:57:n_ausbildungsrufzeichen_…]     <- dans le .tex généré
```

Un commentaire LaTeX ne produit rien. **Restaurer les 42 lignes modifierait les
`.tex` et pas le contenu des PDF** — ce chantier peut donc se mener sans
recompiler la classe N, et la preuve est à portée : régénérer les `.tex` avant
et après, et vérifier que le diff ne porte que sur des lignes commençant par
`%`.

C'est ce qui en fait le premier fil à tirer : un vrai défaut, borné à 42
lignes, réparable sans toucher à un livre publié.

### Fait le 19/08/2026 — et la preuve qui va avec

Les 17 sections ont été traitées d'un seul geste : retrait de tous les
commentaires français, puis réinjection **verbatim** des blocs amont, ancrés
sur le nombre de marqueurs qui les précèdent — ancrage fiable ici, puisque
l'ordre des marqueurs est identique à l'amont et que c'est un contrôle du §5.
Vérifié au préalable : **aucun des 14 commentaires français n'était de notre
cru**, tous correspondaient à un commentaire amont. Le compte final est celui
de l'amont, section par section : 50 lignes, contre 14.

Deux pièges rencontrés, tous deux attrapés par le garde-fou du script :

- **les encarts `<france>` faussent le compte de marqueurs.** Ils ajoutent des
  marqueurs que l'amont n'a pas : dès le premier encart, les deux comptes
  divergent et l'ancrage ne tombe plus jamais juste. Le comptage côté français
  ignore désormais l'intérieur des blocs `<france>` ;
- **l'amont place des commentaires à l'intérieur d'un bloc `<indepth>`**, donc
  ailleurs qu'à une frontière de paragraphe.

**La preuve de neutralité, mesurée.** Les `.tex` de la classe N ont été
régénérés avant et après. Le diff brut montre 64 lignes, dont 22 qui ne sont
pas des commentaires — parce que le générateur **accole** le commentaire à la
fin d'une ligne existante :

```
avant :  }}\begin{DARCQuestionBox}
après :  }}% [picture:543:n_schaltzeichen_antenne:…]
         \begin{DARCQuestionBox}
```

En LaTeX, un `%` neutralise la fin de ligne **et le saut de ligne** : les deux
formes sont strictement équivalentes. Vérifié et non supposé, en normalisant
les deux arbres — retrait de tout `%` non échappé avec recollement de la ligne
suivante — puis comparaison octet à octet :

> **131 sections comparées, 0 divergence de LaTeX effectif.**

Le PDF de la classe N publié en `a.2` reste donc exactement ce que ces sources
produisent.

---

## 2. Germanismes possibles — 11 sections, faux positifs

`A/N_Ende` · `E/N_Ende` · `N/N_Ende` · `E/moegel_dellinger_effekt` ·
`E/spannungsquelle` · `N/ausgangsleistung` · `N/besondere_anlaesse` ·
`N/gefahren` · `N/gesetze_vorschriften` · `N/q_schluessel` · `N/zulassung`

Les mots signalés sont `der`, `und`, `werden`, `den`, `über`, `zur`,
`Leistung` — des mots outils, ce qui est déjà un indice.

Trois vérifiés à la source le 19/08/2026, et les trois sont non seulement des
faux positifs mais de la **bonne pratique** :

| section | occurrence | pourquoi c'est juste |
| --- | --- | --- |
| `N/ausgangsleistung` | « Frequenzbereiche », « Maximale Leistung » | ce sont les **intitulés de colonnes de l'annexe officielle** ; le candidat les lira tels quels le jour de l'examen |
| `N/besondere_anlaesse` | « Türen auf mit der Maus ! » | slogan d'un **indicatif spécial allemand** — un nom propre |
| `E/spannungsquelle` | « Verband der Elektrotechnik… » | nom d'un **organisme**, le VDE |

Les huit autres n'ont pas été ouvertes une par une, mais le motif est le même :
citations de documents officiels allemands, noms propres, sigles. Les trois
`N_Ende` sont notre section de **conclusion, écrite en français**, où figurent
des renvois à l'examen allemand.

**Rien à corriger.** La sonde fait son travail : elle signale pour relecture
humaine, elle ne prétend pas trancher. La seule action envisageable serait
d'inscrire ces onze sections en dérogation — à ne faire qu'après avoir ouvert
les huit restantes, sous peine de transformer la liste des dérogations en liste
d'excuses, ce que sa propre docstring interdit.

---

## 3. Formules dans les encarts « En France » — 7 sections

`A/personenschutzabstand_3` · `A/effektive_strahlungsleistung_erp_2` ·
`A/strom_spannung_messung_3` · `A/am_2` ·
`E/aequivalente_isotrope_strahlungsleistung_eirp_2` · `E/fm_2` ·
`E/naeherungsformel_1` · `E/reihe_parallel_kondensator`

C'est la **première des trois limites documentées** dans la docstring du
script : un ajout français compte comme un écart, parce que le script compare
au texte allemand et que l'ajout n'y est pas.

Trois sections concentrent l'essentiel : `personenschutzabstand_3` à elle seule
produit **71 signalements**, `aequivalente_isotrope_strahlungsleistung_eirp_2`
en produit 60 et `effektive_strahlungsleistung_erp_2` 36. Ce sont précisément
les sections à gros encart réglementaire français, farcies de formules.

**Rien à corriger** : c'est le fonctionnement attendu. En revanche, ces
signalements **noient les autres** — 167 lignes de bruit sur un rapport qui en
compte 342. Piste, si l'on veut que l'outil reste lisible : ignorer les
formules situées **à l'intérieur d'un bloc `<france>`**, puisqu'elles sont par
construction absentes de l'amont. Cela demanderait au script de suivre les
bornes des encarts, ce qu'il ne fait pas aujourd'hui.

---

## 4. Marqueurs DARCdown différents — 4 sections

| section | nature | verdict |
| --- | --- | --- |
| `A/elektrische_geaete_oeffnen_2` | un `<tip>` ajouté côté français, **hors encart `<france>`** | à traiter — §7 |
| `A/transverter_2` | un `<indepth>` ajouté, **hors encart `<france>`** | à traiter — §7 |
| `A/effektive_strahlungsleistung_erp_2` | encart français avec tableau | limite du script, cf. §3 |
| `N/morsetelegrafie` | `[morse:ß]` inséré au rang 35, tout décale d'un cran | **dérogation assumée non déclarée** |

### `N/morsetelegrafie` — une dérogation qui s'ignore

Le décalage vient d'un seul marqueur : nous ajoutons `[morse:ß]` à la table du
code Morse. C'est la **correction du code Morse** mentionnée au §12 de
`CLAUDE.md` parmi les livraisons de la a.2 — une décision prise et appliquée,
pas un accident.

Elle a simplement échappé à la liste `DEROGATIONS` du script. L'y inscrire est
une ligne :

```python
("N", "morsetelegrafie"):
    "[morse:ß] ajouté à la table du code Morse (a.2) ; décale d'un rang "
    "tous les marqueurs suivants",
```

**Effet : 39 écarts → 38.** C'est le gain le moins cher du lot.

### Les deux ajouts hors `<france>`

Déjà connus, déjà inscrits au §9 de `CLAUDE.md`. Le §7 veut que les compléments
nationaux vivent dans un encart `<france>` ; ces deux-là n'y sont pas. Rien
n'est perdu de l'amont — c'est une question de forme, mais c'est la forme qui
rend l'ajout identifiable comme français par le lecteur.

**Attention** : les déplacer **changerait le rendu** (un `<tip>` et un
`<indepth>` ne se composent pas comme un encart `<france>`), donc imposerait de
recompiler A et NEA. À ne pas entreprendre en même temps qu'une publication.

---

## Ordre de travail proposé

| rang | chantier | coût | recompilation |
| ---: | --- | --- | --- |
| 1 | inscrire `N/morsetelegrafie` en dérogation | une ligne | non |
| 2 | restaurer les 42 lignes de commentaires perdues | 13 sections | **non** — mesuré ci-dessus |
| 3 | remettre en allemand les 4 commentaires traduits | 4 sections | non |
| 4 | ouvrir les 8 germanismes non vérifiés | lecture | non |
| 5 | déplacer les deux ajouts hors `<france>` | 2 sections | **oui** — A et NEA |
| 6 | apprendre au script à ignorer l'intérieur des `<france>` | script | non |

### Ce que cela a donné — mesuré le 19/08/2026

| étape | écarts restants |
| --- | ---: |
| état initial | 39 |
| rangs 1 à 3, exécutés ensemble | **22** |
| rang 4, si les germanismes passent en dérogation | 11 |

**Rectification d'une prévision fausse.** La première rédaction de ce document
annonçait 18 après les rangs 1 à 3. Le chiffre était erroné : il comptait les
4 commentaires *traduits* comme des sections supplémentaires, alors qu'ils font
partie des 17. La restauration a traité les deux cas d'un seul geste — on
retire les commentaires français, on réinjecte ceux de l'amont verbatim — donc
les rangs 2 et 3 n'en font qu'un.

Les 22 restants se répartissent ainsi :

| famille | sections |
| --- | ---: |
| germanismes possibles — faux positifs | 11 |
| formules et tableaux d'encarts `<france>` | 9 |
| **ajouts hors `<france>` — seul vrai défaut restant** | **2** |

`N/analog_vs_digital` est passée de la famille 1 à la famille 3 : ses
commentaires sont restaurés, sa formule ajoutée demeure.
