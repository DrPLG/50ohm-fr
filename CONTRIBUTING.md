# Contribuer à 50ohm-fr

Merci de votre aide. Ce document dit **ce qu'on attend d'un signalement**, et
surtout **ce que le projet ne corrigera pas** — cette seconde partie évite
beaucoup de travail perdu de part et d'autre.

---

## Ce qu'est ce dépôt

Une **œuvre dérivée** des contenus de [50ohm.de](https://50ohm.de) (DARC e. V.),
sous licence CC BY 4.0. Nous traduisons, nous mettons en page, et nous ajoutons
des encarts de droit français. Nous ne réécrivons pas le cours allemand.

Deux principes en découlent, et ils gouvernent tout le reste :

1. **Rien n'est retiré du contenu allemand.** Les encarts « En France »
   s'*ajoutent* au texte amont ; ils ne le remplacent ni ne le corrigent.
2. **Aucun contenu réglementaire n'est inventé.** Les encarts sont sourcés
   exclusivement sur les textes officiels en vigueur (Légifrance, ARCEP).

---

## Signaler quelque chose

Ouvrez une [*issue*](https://github.com/DrPLG/50ohm-fr/issues/new/choose) en
partant du gabarit **Relecture**. Il demande quatre choses, et il les demande
parce que sans elles un signalement est difficilement exploitable :

| champ | pourquoi |
| --- | --- |
| **édition et version** | N, E, A ou NEA — la pagination diffère d'une édition à l'autre |
| **numéro de page** | celui imprimé sur la page du PDF |
| **titre de la section** | il survit à une recompilation, contrairement au numéro de page |
| **citation exacte** | quelques mots copiés du PDF, qui permettent de retrouver le passage |

**Un signalement par sujet.** Une *issue* qui liste vingt points est difficile à
traiter, à discuter et à clore ; vingt *issues* d'une ligne se traitent une par
une. Si votre relecture produit une longue liste, ouvrez une *issue* par
chapitre plutôt qu'une seule pour tout le livre.

**Le doute est un signalement valable.** « Cette phrase, je ne la comprends
pas » est une information utile : le livre s'adresse à des candidats, et une
phrase incompréhensible est un défaut même si elle est exacte.

---

## Les catégories

- **Traduction** — contresens, faux ami, terme technique impropre, tournure
  calquée sur l'allemand. C'est la catégorie la plus utile : le texte a été
  traduit avec l'assistance d'une IA, puis relu, et des erreurs subsistent.
- **Coquille** — orthographe, grammaire, typographie française.
- **Mise en page** — figure qui déborde, tableau écrasé, question séparée de ses
  réponses, grande zone de vide, ponctuation en début de ligne.
- **Réglementaire français** — une erreur ou une omission dans un encart
  « En France ». **Joignez la source**, de préférence un lien Légifrance vers le
  texte consolidé en vigueur (voir plus bas).
- **Défaut amont** — l'erreur est dans le texte allemand d'origine. Voir la
  section suivante : elle ne sera pas corrigée, mais elle nous intéresse
  beaucoup.

---

## Ce qui ne sera pas corrigé

### Les défauts du texte allemand

Ils sont **préservés à l'identique**, consignés dans
[`docs/defauts-amont.md`](docs/defauts-amont.md) et signalés au DARC. Nous ne
les corrigeons pas en silence dans la version française : le lecteur qui compare
les deux ouvrages doit retrouver le même contenu.

Cela vaut pour les coquilles allemandes, les libellés d'index fautifs, les
renvois cassés et les erreurs de fond. **Signalez-les quand même** — c'est ainsi
que le relevé s'enrichit, et c'est lui qui part au DARC.

### Les idents et références

Les identifiants de sections, de figures et de photos sont préservés
**verbatim**, umlauts, espaces, points et fautes d'orthographe allemandes
compris. Ce ne sont pas des coquilles : ce sont des clés.

### Le programme de l'examen

Cet ouvrage prépare aux examens **allemands**. Une question de l'examen français
qui manque n'est pas un défaut. Les encarts « En France » sont un complément
d'information comparative, pas un cours de préparation à l'examen de l'ANFR.

---

## Les encarts « En France »

C'est la partie la plus délicate du projet, et la seule où nous produisons du
contenu original. Trois règles, sans exception :

1. **Sources officielles en vigueur uniquement** — Légifrance (textes
   consolidés), ARCEP, ANFR. Un texte abrogé ne vaut rien.
2. **Un texte cité de seconde main doit être vérifié à la source.** Citer un
   décret à travers un article de blog ou un autre texte qui le cite est la
   manière la plus sûre de propager une erreur.
3. **Les publications sous licence CC BY-NC-SA** (F6KGL/F5KFF, Exam'1) portent
   une licence **incompatible** avec la nôtre. Elles peuvent servir à orienter
   les priorités ; elles ne peuvent **jamais** servir de source de rédaction.

Un signalement réglementaire sans référence à un texte officiel ne pourra pas
être retenu, quelle que soit sa pertinence apparente.

---

## Proposer une modification directement

Les *pull requests* sont bienvenues, sur les fichiers de
`traductions/<CLASSE>/sections/`. Quelques points à connaître avant de vous
lancer :

- le format est du **DARCdown**, pas du Markdown : `[question:AD407]`,
  `[picture:136:ident:Légende]`, `[ref:ident]`, `<margin>`, `<tip>`,
  `<indepth>`, `<france>` ;
- **le nombre, la nature et l'ordre de ces marqueurs doivent rester identiques à
  l'original allemand.** C'est vérifié mécaniquement par
  `verifier_traduction.py` ;
- les formules `$…$` sont reprises **verbatim** ;
- **jamais de `:` dans une légende de figure** — le parseur amont fait alors
  disparaître la figure, sans erreur ni avertissement ;
- **jamais d'accent nu en mode mathématique** — le glyphe disparaît
  silencieusement du PDF.

Ces contraintes ne sont pas décoratives : chacune correspond à un défaut qui a
déjà traversé une compilation sans être détecté.

---

## Sans compte GitHub

Écrivez directement à Pierre, F4JWI. Un courriel, un message, une liste dans un
fichier texte : tout est exploitable. Le gabarit d'*issue* ci-dessus donne les
quatre informations à fournir dans tous les cas.

---

## Licence des contributions

En contribuant, vous acceptez que votre apport soit publié sous
**CC BY 4.0**, comme le reste de l'ouvrage.
