Une station relais permet une portée plus grande que ce qui est souvent possible en liaison directe entre deux stations radioamateur. Les stations relais sont le plus souvent installées sur des sites exposés, p. ex. sommets, immeubles de grande hauteur, clochers et autres tours. Il existe aussi des stations relais dans des satellites en orbite autour de la Terre. La structure et le fonctionnement d'une telle station sont représentés sur la figure [ref:n_relaisfunkstellen_aufbau].

[picture:648:n_relaisfunkstellen_aufbau:Représentation schématique d'une station relais et de ses utilisateurs]

Si, par exemple, une montagne se dresse entre deux stations, il est impossible d'émettre à travers la montagne. Une station relais au sommet permet malgré tout d'établir une liaison, car les deux stations peuvent atteindre le relais directement.

Les stations relais sont aussi appelées relais ou repeaters. On les reconnaît à ce qu'elles émettent régulièrement leur indicatif. Selon le [plan des indicatifs](https://50ohm.de/rzp), l'indicatif d'une station relais commence en général par DB0, DM0 ou DO0.

La définition officielle des repeaters est un peu plus aride : *« Station relais » : une station radioamateur télécommandée (y compris dans des satellites) qui réémet, sur déclenchement à distance, des émissions radioamateur reçues, des parties de celles-ci ou d'autres signaux injectés ou mémorisés, et qui sert ainsi à améliorer la joignabilité des stations radioamateur.*

La question suivante sur cette définition se résout d'ailleurs bien par élimination, si l'on sait ceci :
* Les stations relais ne sont pas exploitées avec des indicatifs personnels.
* Les stations relais ne sont habituellement pas occupées en permanence.
* Les stations relais ne doivent pas obligatoirement être exploitées sur des sites géographiquement exposés.

[question:VD118]

---

Une station relais reçoit sur sa fréquence d'entrée le signal d'une station radioamateur et le réémet simultanément sur sa fréquence de sortie. Pour que l'émetteur du relais ne perturbe pas son propre récepteur, les fréquences d'émission et de réception sont en général différentes. L'écart entre fréquence d'émission et de réception s'appelle le décalage de fréquence (shift), ou simplement le décalage. Les décalages habituellement utilisés en Allemagne figurent dans le tableau [ref:n_relaisfunkstellen_ablage].

<margin>
| r: Bande | X: Décalage |
| $\qty{10}{\meter}$ | $\qty{100}{\kilo\hertz}$ |
| $\qty{2}{\meter}$ | $\qty{600}{\kilo\hertz}$ |
| $\qty{70}{\centi\meter}$ | $\qty{7,6}{\mega\hertz}$ |
| $\qty{23}{\centi\meter}$ | $\qty{28}{\mega\hertz}$ |
[table:n_relaisfunkstellen_ablage:Décalage de fréquence]
</margin>

Par exemple, la fréquence d'un relais des $\qty{70}{\centi\meter}$ s'indique ainsi :
* fréquence d'entrée : $\qty{431,275}{\mega\hertz}$
* décalage : $\qty{+7,600}{\mega\hertz}$
* fréquence de sortie : $\qty{438,875}{\mega\hertz}$

[question:BE401]
[question:BE402]
[question:BE403]

<indepth>
Certaines stations relais travaillent aussi en *trafic crossband*. Cela signifie qu'une station émet et reçoit sur une bande (p. ex. $\qty{70}{\centi\meter}$), une autre station sur le même relais mais sur une autre bande (p. ex. $\qty{2}{\meter}$). La commande du relais achemine les conversations entre les deux bandes. Une conversion du mode d'émission peut aussi avoir lieu, par exemple de SSB vers FM.
</indepth>

Une station relais qui transmet des données plutôt que de la voix s'appelle un digipeater. Un digipeater est capable de recevoir des paquets de données et de les réémettre. Sa particularité est que la réémission peut ne porter que sur des parties des données ou s'effectuer en différé. Des paquets peuvent aussi être répétés, ou certains champs de données modifiés.

[question:NF118]

---

Avant de pouvoir trafiquer via une station relais, il faut connaître ses particularités techniques et ses paramètres. Pour certains relais, des réglages supplémentaires de l'émetteur-récepteur, en plus de la fréquence, sont nécessaires pour garantir un trafic sans perturbations. Outre la FM analogique (modulation de fréquence), des procédés numériques comme le DMR et le D-Star sont utilisés pour la transmission de la voix.

<tip>
Les informations sur les stations relais, leurs paramètres techniques et leurs particularités s'obtiennent auprès de la section locale DARC la plus proche, de la personne responsable du relais ou sur Internet.
</tip>

[question:NE309]
[question:NE308]

Un réglage important en trafic FM est la largeur de canal. Rappelons-le : la largeur de bande indique combien de « place » l'émission occupe dans le spectre. Il y a d'une part le Wide-FM, d'une largeur de $\qty{25}{\kilo\hertz}$, affiché p. ex. *FM-W* à l'écran. Il y a d'autre part la FM à bande étroite (Narrow-FM), qui n'occupe que $\qty{12,5}{\kilo\hertz}$ et s'affiche p. ex. *FM-N* sur le poste. Beaucoup de repeaters n'apprécient pas du tout les signaux trop larges : il peut en résulter des signaux distordus et des perturbations des fréquences relais voisines.

[question:BE407]

Le trafic via des stations radioamateur télécommandées doit par principe être permis à tous les radioamateurs disposant d'un indicatif attribué. Pour garantir un trafic sans perturbations, l'exploitant peut toutefois exclure d'autres radioamateurs de l'utilisation de la station. La BNetzA doit en être informée.

[question:VD504]

En trafic via des stations relais, les passages doivent rester aussi courts que possible, afin que les stations mobiles et portables puissent utiliser le relais plus facilement, en particulier lorsqu'elles ne se trouvent que brièvement dans la zone de réception. Entre les passages, il faut marquer une pause pour donner à d'autres stations la possibilité de s'annoncer.

[question:BE406]
[question:BE404]

Si deux stations différentes parlent en même temps, l'émission du relais est perturbée jusqu'à devenir illisible. Pour éviter ce « doublage », une passation ordonnée entre les utilisateurs du relais doit toujours avoir lieu. Cela signifie aussi ne commencer sa propre émission que lorsque la station précédente a terminé la sienne.

[question:NE310]
[question:BE405]

L'annexe 1 de l'AFuV, déjà évoquée, contient aussi des prescriptions sur les puissances d'émission des stations relais. Au-dessus de 30 MHz, une station automatique peut être exploitée avec au maximum 50 W ERP.

[question:VD503]

L'évaluation d'une liaison via une station relais présente une particularité. Comme la force du signal avec laquelle on reçoit son correspondant est celle de la station relais, et non celle du correspondant, on renonce à l'indiquer. Le report ne porte alors que sur la lisibilité (R).

[question:BE408]

<france>
# Les relais français, en Z

Une station répétitrice française porte un suffixe commençant par **Z** : F1ZAB, F5ZXY. La même série sert aux relais et aux balises, si bien qu'en France le suffixe en Z signale « station automatique » sans dire laquelle.

Les conditions d'attribution sont plus fermées que pour un indicatif personnel :

- seuls les titulaires d'un certificat de classe 1, de classe 2 ou HAREC peuvent installer une station répétitrice ;
- le demandeur doit s'assurer lui-même de la compatibilité technique du projet avant de déposer sa demande ;
- la demande est accompagnée d'un dossier technique présentant les grandes lignes de l'installation projetée ;
- le dossier est adressé au pôle de Saint-Dié de l'ANFR, et la délivrance de l'indicatif est gratuite.

S'y ajoute l'obligation générale des stations automatiques : pouvoir couper l'émission immédiatement par télécommande.
</france>
