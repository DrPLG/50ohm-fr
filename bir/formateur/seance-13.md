# Séance 13 — Les modes numériques et l'image

Domaine D · 1 h 30 · chapitre 13 du manuel · fiche d'activité nº 13

## Ce que l'élève doit emporter

- Analogique et numérique ; le bit.
- Les modes numériques passent par un ordinateur relié au poste ; FT8 :
  tranches de 15 secondes, contacts brefs, signaux très faibles.
- La voix numérique : plusieurs systèmes incompatibles entre eux ; un son
  clair qui disparaît d'un coup.
- La SSTV : une image fixe, ligne par ligne, en une à deux minutes.

## Avant la séance

**Acquis nécessaires :** modulation et largeur de bande (séance 11) ;
chute d'eau (séance 8) ; locator évoqué (repris à la séance 20).

**Matériel :**

- par groupe de 2 ou 3 : un ordinateur avec un logiciel de décodage FT8 et
  un logiciel de décodage SSTV installés et essayés ; écouteurs ; la fiche
  nº 13 ;
- une source de signaux : le poste HF du radioamateur relié à l'ordinateur
  projeté, ou un WebSDR dont le son est envoyé au logiciel de décodage
  (câble audio de bouclage ou périphérique audio virtuel) ;
- des enregistrements SSTV (fichiers son) en réserve, et un téléphone avec
  une application de décodage SSTV : elle décode un son joué par un haut-
  parleur, sans câble.

**À préparer :**

- Régler l'heure des ordinateurs à la seconde près : le FT8 ne décode rien
  si l'horloge est décalée de plus d'une ou deux secondes.
- Repérer la fréquence FT8 de la bande ouverte à l'heure de la séance (par
  exemple 14,074 MHz en USB sur 20 m).
- Vérifier si un événement SSTV de la Station spatiale internationale
  tombe pendant la période : les annonces sont publiées à l'avance par le
  programme ARISS. Sinon, utiliser les enregistrements.

## Déroulé

| durée | phase | ce que fait l'encadrant | ce que font les élèves |
| --- | --- | --- | --- |
| 5 min | accroche | fait entendre du FT8, puis montre l'écran du logiciel qui décode | comptent les stations décodées |
| 10 min | analogique, numérique | le bit ; pourquoi le numérique résiste | classent six exemples de la vie courante |
| 10 min | FT8 et voix numérique | les tranches de 15 s ; le locator ; les systèmes de voix | lisent une ligne de décodage FT8 |
| 5 min | la SSTV | l'image ligne par ligne ; l'ISS | — |
| 45 min | manipulation | aide aux réglages audio | décodent du FT8 et une image SSTV (fiche nº 13) |
| 15 min | bilan | projette les images reçues | complètent « à retenir » ; répondent aux questions |

## Conduite de la manipulation

1. **FT8 (25 min).** Le son du récepteur arrive au logiciel. Attendre
   quelques cycles. Relever cinq stations décodées : indicatif, locator,
   report en dB, pays d'après le préfixe. Repérer sur la chute d'eau la
   colonne d'une station choisie.
2. **SSTV (20 min).** Décoder une image, en direct si c'est possible, sinon
   depuis un enregistrement. Avec le téléphone : lancer l'application,
   poser le téléphone près du haut-parleur, lancer la lecture.

**Aucune émission.** Les élèves reçoivent seulement. Si le radioamateur
veut montrer un contact FT8, c'est lui qui émet, sous son indicatif.

## Ce qui coince souvent

- **Rien ne se décode en FT8.** Horloge de l'ordinateur décalée, niveau
  audio trop faible ou saturé, mauvaise bande latérale (il faut l'USB).
- **Confondre FT8 et messagerie.** Un contact FT8 n'échange que quelques
  informations fixes.
- **Image SSTV penchée.** L'horloge audio de l'ordinateur est un peu
  décalée : la plupart des logiciels corrigent l'inclinaison.
- **« Le numérique, c'est Internet. »** Le FT8 et la SSTV passent par
  radio, sans aucun réseau.

## Pour aller plus loin

- **Le report en dB** du FT8 : négatif quand le signal est plus faible que
  le bruit ; le FT8 décode jusque vers −20 dB.
- **Les modes par paquets et l'APRS** : transmission de positions et de
  messages courts, en VHF.
- **Pas de codage secret.** Les règles de tous ces modes sont publiques ;
  coder un message pour en cacher le sens est interdit aux radioamateurs.
- **Débit et largeur de bande.** Plus on veut transmettre vite, plus le
  signal occupe de place.

## Corrigé de la fiche

- Classement : analogique — disque vinyle, thermomètre à alcool, voix au
  microphone ; numérique — photo de téléphone, SMS, musique en ligne.
- Ligne FT8 d'exemple « CQ F4XAB JN18 » : un appel général de F4XAB, dont
  le locator est JN18.
- Relevés FT8 et image SSTV : selon la réception.

## Questions de la séance

RD1301 à RD1310.

## Sources

Manuel : sections `bir_analogique_et_numerique`,
`bir_les_modes_par_ordinateur`, `bir_la_voix_numerique`, `bir_la_sstv`.
Voir `SOURCES.md`.
