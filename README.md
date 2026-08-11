# 50ohm-fr — Préparation à l'examen radioamateur allemand, en français

Traduction française des contenus pédagogiques de [50ohm.de](https://50ohm.de),
le support d'apprentissage du DARC e. V. pour les examens radioamateur
allemands des classes **N**, **E** et **A**.

Ce dépôt produit trois ouvrages PDF complets, augmentés d'encarts de droit
français signalant les différences réglementaires entre l'Allemagne et la
France.

| Classe | Sections | Questions | Encarts « En France » | Version | Pages |
| ------ | -------: | --------: | --------------------: | ------- | ----: |
| N      |      131 |       571 |                    55 | v0.9    |   252 |
| E      |      103 |       462 |                     6 | v0.9    |   202 |
| A      |      153 |       717 |                     5 | v1.2    |   368 |

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
sections/          sections traduites, au format DARCdown, par classe
titles.json        titres de chapitres, de sections et résumés traduits
questions.json     questions d'examen traduites
build_book.py      générateur : assemble les sections en LaTeX et compile
docs/              notes de projet, dont le relevé des défauts amont
CHANGELOG.md       historique des versions publiées
NOTICE             mentions d'attribution exigées par la licence
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
