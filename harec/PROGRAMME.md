# Programme de l'examen français et corpus disponible

> Établi le 22/10/2026 (feuille d'arbitrage nº 13, étape 1). La table
> rubrique → sections est dans [`programme.json`](programme.json). C'est une
> **table de départ** : elle sera affinée pendant la rédaction.

## 1. Le texte en vigueur

**Arrêté du 21 septembre 2000 fixant les conditions d'obtention des
certificats d'opérateur, d'attribution et de retrait des indicatifs des
services d'amateur**, version en vigueur au 22/10/2026 sur Légifrance
(`LEGITEXT000020278007`). L'article 2 et l'annexe I ont été modifiés en
dernier par l'**arrêté du 2 mars 2021** (art. 2 et 14), en vigueur le
**06/06/2021**.

> Lu sur Légifrance au moyen d'un outil de récupération qui résume la page.
> Les deux phrases du barème ont été citées mot pour mot, et à deux reprises.
> **Pierre : relire l'article 2 sur la page avant d'écrire sur l'examen.**

### Article 2 : les épreuves

| épreuve | programme | questions | durée |
| --- | --- | ---: | ---: |
| réglementation | annexe I, 1re partie | 20 | 15 min |
| technique | annexe I, 2e partie | 20 | 30 min |

- **Barème depuis 2021 : 1 point par bonne réponse, 0 pour une mauvaise
  réponse ou une absence de réponse.** **Plus de point négatif** : le
  « +3 / −1 / 0 » du fac-similé de 2000 (et de la feuille nº 13) est
  **périmé**.
- 10/20 exigé à **chaque** épreuve. Une épreuve réussie reste acquise un an.
- Après un échec, on ne peut se représenter qu'après un délai de **deux
  mois**.
- Taux d'incapacité de 70 % ou plus : **temps triplé** et épreuve adaptée.
- **Calculatrice : le texte n'en dit rien.** Pierre indique le 29/10/2026
  qu'une **calculatrice de type collège est autorisée** ; source officielle
  (ANFR) à citer avant publication.

### Article 3 : l'équivalence

Le certificat équivaut à l'ancienne classe 2 et à la classe **HAREC** de la
recommandation CEPT T/R 61-02.

### Annexe I : le plan

- **1re partie, épreuve de réglementation :**
  1. réglementation internationale (règlement des radiocommunications de
     l'UIT, CEPT) ;
  2. réglementation nationale ;
  3. **brouillages et protections** (dont décibels, rendement, PEP,
     protection électrique et foudre) ;
  4. **antennes et lignes de transmission** ;
  5. code Q et alphabet (tableaux du JO nº 236 du 11/10/2000 seulement).
- **2e partie, épreuve technique :** électricité et radioélectricité (avec
  le § 1.10 sur le traitement numérique du signal), composants, circuits,
  récepteurs, émetteurs, propagation et antennes, mesures.
- **3e partie (Morse) : abrogée.**

## 2. Ce que montre la table : mesures du 22/10/2026

Mots du texte français des sections citées, hors marqueurs et commentaires :

| | sections | mots |
| --- | ---: | ---: |
| 1re partie (réglementation) | 78 | 44 100 |
| 2e partie (technique) | 159 | 98 800 |
| citées deux fois (1re et 2e parties) | 10 | — |
| **hors programme** | **131** | **60 000** |

**Premier constat : l'épreuve de réglementation est à moitié technique.**
Les chapitres 3 et 4 (brouillages, décibels, antennes, lignes) pèsent
34 000 mots dans le corpus. Le budget de la feuille nº 13 (« réglementation
40 p., technique 170 p. ») découpait selon le droit et la technique, pas
selon les épreuves. **Il est à refaire** : le livre suivra les deux parties
de l'annexe, et la partie 1 sera bien plus grosse que 40 pages.

**Deuxième constat : le volume à condenser reste le même.** Environ
140 000 mots couvrent le programme, et il en faut environ 55 000 pour
260 pages A5. C'est le rapport d'un tiers de l'étude de faisabilité.

### Ce que le corpus ne couvre pas, ou mal

Recherche par mots dans le texte français des 379 sections du NEA :

| rubrique | constat |
| --- | --- |
| P1 ch. 2, réglementation nationale | **rien d'utilisable** : à écrire (CPCE, arrêtés de 2000 et de 2007, ANFR) |
| P1 1.1, résolution 640, article 25 du RR | absents |
| P2 3.5, discriminateur de Foster-Seeley | **absent** |
| P2 4.3, calibrateur à quartz | absent |
| P2 7.2, ondémètre à absorption | absent (les occurrences d'« absorption » portent sur autre chose) |
| P2 2.7, tube électronique | une mention dans `transistor_1`, rien de plus |
| P2 6.3, guides d'ondes | effleurés (`troposphaere_3`, `parbolspiegel_2`) |
| P2 6.3, affaiblissement en espace libre | « espace libre » apparaît dans 12 sections, mais pas la formule de l'affaiblissement : à vérifier |
| P1 4.3, boîte d'accord | dispersée dans 8 sections : à rassembler |

### Hors programme, à trier

La liste des 131 sections non citées est donnée par le script de mesure. Ce
sont surtout le droit allemand, les modes numériques avancés (PSK, QAM,
OFDM, codage), les connecteurs et le trafic. **Quelques-unes serviront
sans doute à la rédaction** : `daempfungsglieder` (atténuateurs, P1 3.3),
`morsetelegrafie` (claquements de manipulation, P2 5.4), `dummy_load_2`,
`vna_1`. Le choix se fera chapitre par chapitre.
