# Séance 16 — Câbles, connecteurs et réglage

Domaine D · 1 h 30 · chapitre 16 du manuel · fiche d'activité nº 16

## Ce que l'élève doit emporter

- Le câble coaxial : âme, isolant, tresse, gaine ; 50 Ω ; pertes qui
  augmentent avec la longueur et la fréquence.
- Les connecteurs PL, BNC, N et SMA ; âme et tresse ne se touchent jamais.
- Le ROS : 1 parfait, jusqu'à 2 acceptable, 3 et plus à corriger ; très
  élevé, c'est une panne.
- Régler un dipôle à l'analyseur : creux trop bas, antenne trop longue, on
  raccourcit les deux brins par petites étapes.

## Avant la séance

**Acquis nécessaires :** dipôle et résonance (séance 14) ; les antennes des
groupes (séances 14 et 15).

**Matériel :**

- par groupe de 2 ou 3 : le dipôle du groupe, avec son câble ; une pince
  coupante, un mètre ruban, des lunettes ; la fiche nº 16 ;
- pour la classe : deux ou trois analyseurs d'antenne couvrant la bande des
  2 m (petit analyseur vectoriel de type « NanoVNA » calibré, ou analyseur
  d'antenne), à partager par rotation ;
- pour le montage d'une fiche : des morceaux de câble coaxial, des fiches
  (BNC ou PL à souder, ou à sertir), une pince à dénuder coaxiale, un fer à
  souder et son support, de la soudure, un multimètre en continuité ;
- quelques connecteurs de chaque type, et des adaptateurs, à faire passer.

**Sécurité :** fer à souder à 300-350 °C sur son support ; la soudure se
fait sous la surveillance du radioamateur ou de l'encadrant ; lavage des
mains après. Le montage de fiche peut être réservé à une démonstration si
l'atelier de soudure (séance 19) n'a pas encore eu lieu.

## Déroulé

| durée | phase | ce que fait l'encadrant | ce que font les élèves |
| --- | --- | --- | --- |
| 5 min | accroche | coupe un câble coaxial devant la classe et fait passer le morceau | nomment les couches |
| 10 min | câble et connecteurs | impédance, pertes ; les quatre connecteurs | associent chaque fiche à son nom |
| 10 min | le ROS | l'onde renvoyée ; la lecture ; l'analyseur | lisent une courbe de ROS projetée |
| 5 min | le réglage | trop long, trop court ; petites étapes | — |
| 50 min | manipulation | tient les analyseurs ; valide chaque coupe | règlent leur dipôle ; montent ou observent le montage d'une fiche (fiche nº 16) |
| 10 min | bilan | compare les fréquences de résonance finales | complètent « à retenir » ; répondent aux questions |

## Conduite de la manipulation

Deux ateliers en parallèle, par rotation de 25 minutes.

**Atelier A — régler son dipôle.**

1. Raccorder le dipôle à l'analyseur, le tenir à bout de bras, loin du
   corps et des objets métalliques, dans sa polarisation d'usage.
2. Balayer de 130 à 160 MHz ; relever la fréquence du creux et le ROS à
   145 MHz.
3. Si le creux est trop bas : raccourcir **chaque** brin de 5 mm, mesurer à
   nouveau. Noter chaque étape. S'arrêter quand le creux est entre 144 et
   146 MHz.

**Atelier B — monter une fiche.**

1. Dénuder le câble aux cotes de la notice de la fiche.
2. Monter et souder (ou sertir), sous surveillance.
3. Contrôler au multimètre : continuité âme-âme et tresse-corps ; **aucune**
   continuité entre âme et tresse.

## Ce qui coince souvent

- **Couper un seul brin.** Le dipôle devient dissymétrique. Couper les deux
  de la même longueur.
- **Couper trop d'un coup.** 5 mm à 145 MHz déplacent la résonance
  d'environ 1 à 1,5 MHz : c'est déjà beaucoup.
- **Mesurer l'antenne posée sur la table.** Le réglage change dès qu'on
  l'installe : mesurer dans la position d'usage.
- **Confondre ROS bas et antenne efficace.** Une charge fictive a un ROS
  parfait et ne rayonne rien : le ROS dit que la puissance est acceptée,
  pas qu'elle est bien rayonnée.
- **Tresse mal peignée dans la fiche.** Un seul brin qui dépasse suffit au
  court-circuit : le contrôle au multimètre le révèle.

## Pour aller plus loin

- **La puissance réfléchie** : un ROS de 2 correspond à environ 11 % de la
  puissance renvoyée ; un ROS de 3, à 25 %.
- **La boîte d'accord** adapte l'ensemble antenne et câble au poste ; elle
  ne rend pas l'antenne résonante.
- **Les pertes en dB** : les fabricants de câbles les donnent en dB pour
  100 m, fréquence par fréquence.
- **Le dipôle de 73 Ω** sur un câble de 50 Ω donne en principe un ROS
  d'environ 1,5 à la résonance : on ne descendra pas forcément à 1.

## Corrigé de la fiche

- Couches du câble, de l'intérieur vers l'extérieur : âme, isolant, tresse,
  gaine.
- Réglage : creux initial en général sous 145 MHz (brins coupés 2 cm trop
  longs à la séance 14), remonté par étapes de 5 mm jusqu'à 144-146 MHz ;
  ROS final à 145 MHz inférieur à 1,5 à 2.
- Contrôle de la fiche : âme-âme et tresse-corps conduisent ; âme-tresse ne
  conduit pas.

## Questions de la séance

RD1601 à RD1610.

## Sources

Manuel : sections `bir_le_cable_coaxial`, `bir_les_connecteurs`,
`bir_le_ros`, `bir_regler_une_antenne`. Voir `SOURCES.md`.
