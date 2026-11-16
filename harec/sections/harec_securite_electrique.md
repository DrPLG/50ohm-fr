Le danger principal est le **contact avec une tension**. On la considère comme dangereuse au-delà de $\qty{50}{\volt}$ en alternatif et de $\qty{120}{\volt}$ en continu [index:Tension dangereuse]. Ce qui blesse, c'est le **courant** qui traverse le corps : au-delà de $\qty{30}{\milli\ampere}$, il peut être mortel, d'autant plus qu'il dure et qu'il passe par la poitrine.

Les effets possibles : **troubles du rythme cardiaque** et fibrillation, **brûlures** aux points d'entrée et de sortie, **tétanisation** des muscles qui empêche de lâcher prise, et **accidents secondaires**, comme la chute d'une échelle. Après tout accident électrique, on consulte un médecin : un trouble du rythme peut survenir des heures plus tard.

<attention>
**Les cinq règles de sécurité**, avant tout travail sur une installation ou un appareil :
1. mettre hors tension ;
2. empêcher la remise sous tension (débrancher la fiche) ;
3. vérifier l'absence de tension ;
4. mettre à la terre et en court-circuit ;
5. isoler les parties voisines restées sous tension.
</attention>

---

**Haute tension et condensateurs.** Un appareil débranché n'est pas sans danger : les **condensateurs** de l'alimentation restent chargés. Dans une alimentation à découpage, certains dépassent la tension du secteur ; dans un amplificateur à tubes, ils montent à plusieurs centaines, voire milliers de volts. On les décharge à travers une **résistance isolée de forte valeur**, jamais par un court-circuit franc, qui peut blesser, détruire les composants ou mettre le feu. Les travaux sur la partie $\qty{230}{\volt}$ d'un appareil reviennent à un électricien qualifié.

**L'alimentation de la station** transforme le $\qty{230}{\volt}$ du secteur en $\qty{13,8}{\volt}$ continu. Son boîtier métallique est relié par la prise au **conducteur de protection** (PE, vert et jaune) : en cas de défaut, le courant part à la terre au lieu de traverser l'opérateur, et le **dispositif différentiel** du tableau coupe le circuit. Côté continu, rouge pour le plus, noir pour le moins : une inversion peut détruire l'émetteur.

**Les fusibles** [index:Fusible] coupent le circuit en cas de court-circuit ou de surcharge. On ne remplace un fusible grillé qu'**après avoir trouvé la cause**, et par un modèle **identique** : même courant, même caractéristique.

| l: caractéristique | l: marquage | l: coupure à dix fois le courant nominal |
| rapide | F | $\qty{30}{\milli\second}$ au plus |
| semi-temporisé | M ou MT | $\qty{90}{\milli\second}$ au plus |
| temporisé | T | $\qty{300}{\milli\second}$ au plus |
[table:harec_fusibles:Caractéristiques des fusibles miniatures]

<attention>
**Ne jamais ponter un fusible**, avec du papier d'aluminium ou un fil : le court-circuit suivant met le feu.
</attention>
