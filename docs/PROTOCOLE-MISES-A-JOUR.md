# Protocole de veille des mises à jour

> Ouvert le 21/10/2026 (demande de Pierre). Deux sources sont surveillées :
> **l'amont DARC** (contenus et générateur) et **les retours des relecteurs**.
> Le réglementaire français et les outils de la chaîne restent hors protocole.
>
> Outil : `veille.py` v0.1. Registre des décisions :
> `Fichierstravail/REGISTRE-VEILLE.md` (local, comme les feuilles d'arbitrage).

Ce protocole **regroupe** ce qui existait en morceaux — `verifier_amont.py`,
le contrôle réseau du § 10 de CLAUDE.md, les feuilles d'arbitrage — et y ajoute
ce qui manquait : **un code de réponse par type de changement**, et la trace de
ce que chaque relecture est devenue.

---

## 1. Quand

| moment | commande |
| --- | --- |
| **début de chaque session** | `python veille.py` |
| avant d'ouvrir un chantier de traduction | `python veille.py` |
| **avant toute compilation destinée à une release** | `python veille.py` — un livre ne part pas sur un amont qu'on n'a pas regardé |
| à la réception d'une relecture | déposer le fichier, puis `python veille.py` |

Interpréteur : le venv du générateur (`C:\50ohm\50ohm-main\.venv\Scripts\python.exe`,
CLAUDE.md § 11). Il faut aussi `gh` authentifié.

## 2. Les cinq étapes

1. **Détecter** — `veille.py` compare le sha amont intégré à `main`, classe
   chaque fichier changé (§ 3), passe `verifier_amont.py` sur l'instantané
   local, et liste les relectures reçues sans feuille et les issues ouvertes.
2. **Lire le code de retour** :

   | rc | sens | suite |
   | --- | --- | --- |
   | 0 | rien de neuf | rien |
   | 1 | des éléments à traiter | étape 3 |
   | 2 | **verdict incomplet** (réseau, `gh`, instantané) | réparer la mesure, relancer. **Jamais lu comme un 0.** |

3. **Consigner** — une ligne au registre par événement : date, source, code,
   réponse retenue, renvoi à la feuille. Même un R0.
4. **Répondre** — selon le § 3 (amont) ou le § 4 (relectures). Tout code
   marqué *Pierre* passe par une **feuille d'arbitrage numérotée** ; l'exécution
   suit sa validation. **Aucune compilation sans son accord** (§ 2 de CLAUDE.md),
   même quand la feuille prévoit « puis recompiler ».
5. **Solder** — inscrire l'état atteint pour que la veille suivante reparte de
   là :
   - amont : `python veille.py amont-integre --depot contenus --sha <40 car.>`
     (avec `--instantane` si un nouvel instantané a été extrait) ;
   - relecture : `python veille.py relecture-traitee --feuille <nº> "<relecteur>/<fichier>"`.

   **On solde ce qui est traité, jamais ce qui est seulement vu.** Le rapport
   ne marque rien de lui-même.

## 3. Réponses types — amont

| code | changement | réponse | qui |
| --- | --- | --- | --- |
| **R0** | hors périmètre : `solutions/`, `slides/`, `html/`, `static/`, section hors sommaire, dessin appelé par aucune section traduite | consigner ; solder par `amont-integre --note "écart R0 seul, instantané <sha> conservé"` | autonome |
| **R1** | section **traduite** modifiée | nouvel instantané (§ 5) ; diff exact ; traduire le changement ; `verifier_traduction.py` ; réenregistrer au manifeste ; document réduit | **Pierre** dès que la prose change |
| **R2** | section **au sommaire** sans traduction | traduire en entier, contrôles § 5 de CLAUDE.md, enregistrer | **Pierre** |
| **R3** | dessin **forké** modifié | reporter le diff dans le fork ; compiler le dessin isolément ; `sonde_dessins.py` ; réenregistrer | autonome, sauf texte nouveau à traduire |
| **R4** | dessin **non forké** mais appelé | sort tel quel à la recompilation ; vérifier qu'il n'ajoute pas d'allemand visible, sinon forker (→ R3) | autonome |
| **R5** | question modifiée (détail par numéro dans le rapport) | traduite : revoir énoncé et réponses ; non traduite : rien, l'allemand est repris | **Pierre** si le sens change |
| **R6** | sommaire `toc/*.json` | mesurer sections entrées, sorties, déplacées, et l'effet sur chaque livre | **Pierre** |
| **R7** | `latex/` amont (`settings.tex`, `.sty`) | document réduit **avant** toute compilation ; vérifier les patchs de `build_book.py` (substitution à zéro correspondance = arrêt, § 10) | **Pierre** |
| **R8** | photo | sort telle quelle | autonome |
| **R9** | générateur `renderer/` | régénérer les arbres N, E, A **sans compiler** avant et après ; comparer | **Pierre** si un arbre change |

**Défaut amont rencontré en route** (unité non déclarée, coquille, label
orphelin) : préserver, documenter dans `docs/defauts-amont.md`, ne jamais
corriger en silence (CLAUDE.md § 6 et § 8).

**Suppression ou renommage** d'un élément R1 à R3 : le rapport le signale ;
traiter comme un R6.

## 4. Réponses types — relectures

| code | situation | réponse |
| --- | --- | --- |
| **L1** | fichier **nouveau ou modifié** dans `Fichierstravail/Relectures/<relecteur>/` | inventaire dans une **feuille d'arbitrage** : chaque remarque recherchée dans les sources **actuelles** (le relecteur a souvent lu une version périmée), rangée par famille, avec une proposition. Aucune décision prise dans la feuille |
| **L2** | fichier reçu, enregistré, **sans feuille** | même chose : il attend |
| **L3** | **issue GitHub** ouverte | même inventaire ; l'issue est fermée par un commit qui la cite une fois la décision exécutée |

Puis, dans tous les cas :

1. **Pierre arbitre** la feuille (éditorial et réglementaire lui reviennent).
2. Exécution, contrôles du § 5 de CLAUDE.md, document réduit.
3. **Défaut amont signalé par un relecteur** : il rejoint `docs/defauts-amont.md`,
   pas notre traduction.
4. **Retour au relecteur** : c'est Pierre qui écrit. Je peux préparer un
   brouillon récapitulant ce qui a été retenu, écarté et pourquoi.
5. Solder : `relecture-traitee --feuille <nº>`.

## 5. Renouveler l'instantané amont (R1 à R7)

Rappel des règles déjà payées (CLAUDE.md § 10-11) :

- tarball `codeload.github.com` au sha visé, **extrait avec `tarfile`**, jamais
  `tar.exe` (umlauts) ;
- **conserver l'ancien instantané** pendant le chantier, sous un nom daté ;
- `diff -rq` entre les deux arbres = **exactement** la liste des fichiers de
  l'API, ni plus ni moins ;
- `verifier_amont.py verifier` sur le nouvel instantané ;
- à la clôture : `veille.py amont-integre --sha … --instantane …`, et suppression
  de l'ancien instantané.

## 6. Limites connues

- La compare GitHub plafonne la liste des fichiers à **300** : au-delà le
  rapport l'annonce et seul le `diff -rq` de deux instantanés fait foi.
- Un dessin est dit « appelé » s'il figure dans un `[picture:…]` d'une section
  **traduite** ; un dessin appelé seulement par une section allemande non
  traduite sort en R0.
- Le classement des sections suit les sommaires **de l'instantané local** : une
  section que `main` vient d'ajouter à un sommaire sort en R0 tant que le
  sommaire n'est pas intégré — mais le sommaire changé, lui, sort en R6.
- Les relectures sont suivies **par fichier**, pas par remarque : un PDF
  annoté une seconde fois sous le même nom ressort en « modifié », un ajout
  sous un autre nom en « nouveau ».
