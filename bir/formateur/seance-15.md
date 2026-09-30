# Séance 15 — Construire son antenne

Domaine D · 1 h 30 · chapitre 15 du manuel · fiche d'activité nº 15

## Ce que l'élève doit emporter

- Le diagramme de rayonnement : omnidirectionnelle ou directive.
- L'antenne verticale, omnidirectionnelle, pour les relais, les voitures,
  les portatifs.
- La Yagi : radiateur relié au câble, réflecteur derrière, directeurs
  devant ; plus d'éléments, faisceau plus étroit, gain plus grand.
- Le gain concentre la puissance, il ne la crée pas.
- Une antenne s'installe en hauteur, loin des lignes électriques.

## Avant la séance

**Acquis nécessaires :** dipôle demi-onde et polarisation (séance 14). Les
dipôles coupés par les groupes à la séance 14.

**Matériel, par groupe de 2 ou 3 :**

- le dipôle du groupe (séance 14) ;
- une poutre isolante (tasseau de bois sec ou tube PVC) d'environ 60 cm,
  deux colliers ou supports ;
- un élément réflecteur : un fil ou une tige rigide environ 5 % plus long
  que le dipôle du groupe, soit environ 1,03 m pour un dipôle de 0,98 m ;
- un câble coaxial de 2 à 3 m avec, à un bout, le raccordement au dipôle
  (dominos, cosses) et, à l'autre, la fiche du récepteur ;
- une clé SDR sur ordinateur, ou un récepteur avec S-mètre ;
- la fiche élève nº 15, une boussole ou une application de boussole.

**Pour l'encadrant :** un signal de référence stable en VHF à l'heure de la
séance, dans une direction connue : relais local, balise, ou à défaut un
émetteur FM de radiodiffusion éloigné (le dipôle 2 m reçoit correctement la
bande FM voisine). Noter sa direction depuis l'établissement.

**Principe.** On transforme le dipôle en une Yagi à deux éléments en
ajoutant un réflecteur derrière lui, à environ 40 cm (un cinquième de
longueur d'onde à 145 MHz). On compare la réception dans plusieurs
directions, avec et sans réflecteur.

## Déroulé

| durée | phase | ce que fait l'encadrant | ce que font les élèves |
| --- | --- | --- | --- |
| 5 min | accroche | photo d'un toit : « pourquoi ces antennes ont-elles des formes si différentes ? » | proposent |
| 10 min | le diagramme | dipôle horizontal, antenne verticale ; lecture du diagramme | dessinent le diagramme d'une antenne verticale vue de dessus |
| 10 min | la Yagi | radiateur, réflecteur, directeurs ; le gain | nomment les éléments d'une antenne de télévision |
| 5 min | sécurité | lignes électriques, toits, orages | — |
| 45 min | manipulation | aide au montage ; tient le cahier des mesures | assemblent l'antenne, mesurent la réception dans plusieurs directions (fiche nº 15) |
| 15 min | bilan | compare les résultats des groupes | complètent « à retenir » ; répondent aux questions |

## Conduite de la manipulation

1. **Assembler (15 min).** Fixer le dipôle au bout de la poutre, brins
   horizontaux ou verticaux selon la polarisation du signal de référence.
   Raccorder le câble au centre. Fixer le réflecteur parallèle au dipôle,
   à 40 cm derrière, sans le relier à rien.
2. **Mesurer sans réflecteur (10 min).** Réflecteur retiré, tourner le
   dipôle par quarts de tour (nord, est, sud, ouest) ; relever le niveau du
   signal de référence à chaque position.
3. **Mesurer avec réflecteur (15 min).** Même chose avec le réflecteur. Le
   signal doit être nettement plus fort quand le dipôle est entre le
   réflecteur et l'émetteur, et nettement plus faible dans l'autre sens.
4. **Chercher la direction (5 min).** Tourner lentement pour trouver le
   maximum ; lire la direction à la boussole et la comparer à celle de
   l'émetteur.

**Réception seulement.** Ces antennes ne servent qu'à recevoir pendant la
séance. Si le radioamateur veut émettre dessus, il le fait après la séance
16 et le réglage.

## Ce qui coince souvent

- **Relier le réflecteur au câble.** Il ne doit toucher à rien : c'est un
  élément « passif ».
- **Réflecteur du mauvais côté.** L'antenne pointe alors vers l'arrière :
  bonne occasion de faire comprendre ce que fait le réflecteur.
- **Mesures faussées par les corps.** Les élèves se tiennent derrière
  l'antenne, jamais devant, et restent immobiles pendant la lecture.
- **Différences faibles.** À l'intérieur, les réflexions brouillent tout :
  si possible, mesurer près d'une fenêtre ou dehors.

## Pour aller plus loin

- **Le rapport avant-arrière** : la différence entre le signal reçu de
  face et de dos ; bonne mesure de l'efficacité d'une Yagi.
- **Les antennes de télévision** sont des Yagi pour les UHF, souvent à
  polarisation horizontale.
- **La chasse au renard** (séance 20) utilise justement une petite antenne
  directive pour trouver un émetteur caché.
- **Les cotes d'une Yagi** à trois éléments ou plus se calculent avec des
  logiciels : les longueurs et les écarts dépendent les uns des autres.

## Corrigé de la fiche

Les valeurs dépendent du lieu. Sont attendus : quatre relevés sans
réflecteur à peu près égaux deux à deux (dipôle horizontal : forte
réception de face et de dos, faible dans l'axe des brins) ; avec
réflecteur, un maximum marqué dans une direction et un minimum à l'opposé ;
une direction du maximum proche de celle de l'émetteur, à 30° près.

## Questions de la séance

RD1501 à RD1510.

## Sources

Manuel : sections `bir_omnidirectionnelle_ou_directive`,
`bir_l_antenne_yagi`, `bir_installer_une_antenne`. Voir `SOURCES.md`.
