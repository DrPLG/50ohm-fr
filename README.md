# 50ohm-fr — Préparation à l'examen radioamateur allemand, en français

Traduction française des contenus pédagogiques de [50ohm.de](https://50ohm.de),
le support d'apprentissage du DARC e. V. pour les examens radioamateur
allemands des classes **N**, **E** et **A**.

Ce dépôt produit trois ouvrages PDF complets, plus une édition combinée qui
les réunit, augmentés d'encarts de droit français signalant les différences
réglementaires entre l'Allemagne et la France.

| Classe | Sections | Questions | Encarts « En France » | Version | Pages |
| ------ | -------: | --------: | --------------------: | ------- | ----: |
| N      |      131 |       571 |                    55 | a.2     |   258 |
| E      |      103 |       462 |                     6 | a.2     |   214 |
| A      |      152 |       717 |                     5 | a.2     |   382 |
| NEA    |      383 |     1 751 |                    64 | a.2     |   814 |

Chiffres du 17/08/2026. La colonne « Questions » compte les usages : une même
question peut servir dans deux classes. Aucune version n'est encore publiée —
le dépôt ne porte ni tag ni release.

## Nature de l'ouvrage

Il s'agit d'une **œuvre dérivée** au sens de la licence CC BY 4.0. Le contenu
pédagogique et les questions officielles de la BNetzA proviennent intégralement
du projet 50ohm.de ; le travail apporté ici est celui de la traduction, de la
mise en page en volume relié et de l'ajout des compléments français.

Deux principes gouvernent le projet :

1. **Rien n'est retiré du contenu allemand.** Les encarts français
   s'*ajoutent* au texte amont, ils ne le remplacent ni ne le corrigent.
2. **Aucun contenu réglementaire n'est inventé.** Les encarts sont sourcés
   exclusivement sur les textes officiels en vigueur (Légifrance, ARCEP).

## Avertissement

Cet ouvrage prépare aux examens **allemands**. Le programme, les questions et
le droit exposés dans le corps du texte sont ceux de la BNetzA. Les encarts
« En France » sont fournis à titre d'information comparative et ne constituent
pas une préparation à l'examen français de l'ANFR.

La traduction a été réalisée avec l'assistance d'une IA, puis relue. Malgré ce
soin, des erreurs subsistent probablement : en cas de doute, le texte allemand
d'origine fait foi. Les signalements sont bienvenus (voir *Contribuer*).

## Contenu du dépôt

```
traductions/<C>/  par classe : sections traduites (DARCdown), dessins forkés,
                  titres, questions, et les manifestes de suivi de l'amont
build_book.py     générateur : assemble les sections en LaTeX et compile
compiler.bat      point d'entrée pratique : purge, compile, passe les contrôles
verifier_amont.py     détecte la dérive de l'amont sur nos forks et traductions
verifier_traduction.py  contrôle une traduction face à son original allemand
verifier_questions.py   vérifie qu'aucune question n'est séparée de ses réponses
sonde_dessins.py      cherche l'allemand résiduel dans les dessins forkés
docs/             notes de projet, dont le relevé des défauts amont
CHANGELOG.md      historique des versions
NOTICE            mentions d'attribution exigées par la licence
```

Les PDF compilés sont publiés dans les
[*Releases*](https://github.com/DrPLG/50ohm-fr/releases) et non
versionnés dans le dépôt.

## Compilation

La chaîne requiert Python 3, une distribution TeX complète avec LuaLaTeX et
`latexmk`, et deux dépôts amont :

- [`DARC-e-V/50ohm-contents-dl`](https://github.com/DARC-e-V/50ohm-contents-dl) — les contenus ;
- [`DARC-e-V/50ohm`](https://github.com/DARC-e-V/50ohm) — le générateur, qui
  fournit le paquet Python `renderer`.

```bash
python3 build_book.py --edition A --lang fr \
        --input /chemin/50ohm-contents-dl \
        --translations ./A \
        --output build-book
```

Le paquet `renderer` appartient au dépôt *générateur*, pas au dépôt de
contenus — confusion fréquente. La variable d'environnement `OHM_RENDERER`
permet d'en forcer l'emplacement.

Deux règles de compilation à ne pas contourner :

- toujours passer par `latexmk`, jamais par deux passes `lualatex` successives
  lancées à la main ;
- purger les fichiers auxiliaires avant chaque compilation.

## Licence

Contenus originaux : © 50ohm.de-Autorenteam / DARC e. V., sous licence
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr).

Traduction française et compléments : © Pierre F4JWI, sous la même licence
CC BY 4.0. Voir [`LICENSE`](LICENSE) et [`NOTICE`](NOTICE).

Vous êtes libre de partager et d'adapter cet ouvrage, y compris à des fins
commerciales, à condition d'en créditer les auteurs et d'indiquer les
modifications apportées.

## Contribuer

Corrections de traduction, coquilles, imprécisions réglementaires : ouvrez une
*issue* ou une *pull request*. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

Les défauts constatés dans les sources allemandes ne sont **jamais corrigés
silencieusement** : ils sont préservés à l'identique, consignés dans
[`docs/defauts-amont.md`](docs/defauts-amont.md) et signalés au DARC.

## Remerciements

À l'équipe 50ohm.de du DARC e. V., et en particulier à Lars DC4LW et
Matthias DL9MJ, pour un travail pédagogique remarquable et pour l'avoir placé
sous une licence qui rend ce projet possible.

---

Pierre — F4JWI — Haguenau, Grand Est
