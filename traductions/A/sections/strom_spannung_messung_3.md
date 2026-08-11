Dans les classes N et E, nous avons déjà appris comment mesurer correctement le courant et la tension et quelles propriétés ont les résistances internes des appareils de mesure. Si les appareils de mesure ne sont pas insérés correctement dans le circuit, on obtient des affichages faux ou absurdes, ou l'on peut, dans le pire des cas, endommager l'appareil de mesure. Dans la classe A, il y a à ce sujet encore deux questions supplémentaires qui contrôlent la mesure correcte du courant et de la tension — mais dans un contexte un peu plus complexe.

La première question porte sur la mesure de puissance d'un amplificateur (Power Amplifier, PA). Nous connaissons déjà la relation $P = U \cdot I$ : la puissance peut se déterminer en mesurant la tension et le courant, puis en multipliant les deux valeurs. Sur la figure [ref:a_strom_spannung_messung], l'alimentation en tension sous forme d'un bloc d'alimentation est raccordée à gauche, la PA se trouve au milieu, et un autre consommateur, l'émetteur (TRX), est raccordé à droite. Si nous voulons maintenant déterminer la puissance de la PA, seul le courant qui entre dans la PA doit être mesuré.

<margin>
[picture:1003:a_strom_spannung_messung:Mesure de la puissance d'un amplificateur (PA)]
</margin>

[question:AI101]

Pour la question suivante, rappelons-nous les règles de la classe E : les appareils de mesure de tension se branchent toujours en parallèle et les appareils de mesure de courant toujours en série. La question devient ainsi très facile à résoudre. 

[question:AI102]

---

Dans ce qui suit, nous voulons examiner deux grandeurs caractéristiques de la mesure qui sont souvent confondues :

- la résolution
- la précision de mesure (aussi appelée tolérance ou erreur)

La *résolution* désigne la plus petite variation de la grandeur mesurée qu'un appareil peut encore afficher. Exemple : un multimètre avec une résolution de $\qty{0,1}{\volt}$ ne peut pas faire la différence entre $\qty{10,5}{\volt}$ et $\qty{10,45}{\volt}$ si l'écart est plus petit que la résolution. Un appareil avec une résolution de $\qty{0,01}{\volt}$ peut en revanche distinguer nettement plus finement. La résolution est en règle générale indiquée par le fabricant de l'appareil de mesure.

<tip>
Considérons d'abord la *résolution* à l'aide d'une montre. Si la montre possède un affichage des heures et des minutes, l'heure peut être indiquée à une minute près. Mais on ne peut pas lire s'il est 13 heures 3 minutes et 10 secondes ou 13 heures 3 minutes et 59 secondes. *Une minute* est donc la *plus petite résolution* de la montre (de même, une montre avec trotteuse a une plus petite résolution d'une seconde).
</tip>

La *précision de mesure* (aussi erreur de mesure ou tolérance) d'un appareil décrit de combien la valeur affichée peut au maximum s'écarter de la valeur réelle — aussi bien vers le haut que vers le bas, par exemple $\pm\qty{5}{\percent}$. Une règle empirique simple : plus la plage de mesure qu'un appareil doit couvrir est grande, plus la précision de la mesure est en général faible.

La précision de mesure dépend entre autres de la résistance interne de l'appareil de mesure, car celle-ci influence le résultat de la mesure.
Dans la classe E, nous avons appris : un appareil de mesure de courant a une résistance interne très faible (idéalement $\qty{0}{\ohm}$), un appareil de mesure de tension au contraire une résistance interne très élevée (idéalement $\qty{\infty}{\ohm}$). Dans la classe A, nous voulons maintenant regarder en plus avec quelle exactitude nos appareils de mesure peuvent saisir la tension ou l'intensité réellement présente. La valeur mesurée affichée diffère en effet en règle générale de la valeur réelle — et cela tient aux résistances internes non parfaites des appareils de mesure, qui influencent la mesure.

---

Examinons le schéma équivalent d'un voltmètre réel sur la figure [ref:a_reale_spannungsmessung] pour la question d'examen suivante. En plus de l'ampèremètre idéal, un voltmètre réel contient une résistance branchée en parallèle, p. ex. de $\qty{10}{\mega\ohm}$. Si cette résistance était infiniment grande, elle n'existerait pratiquement pas — et nous aurions un appareil de mesure idéal. Cela signifie cependant que, lors d'une mesure de tension réelle, un petit courant circule toujours à travers cette résistance et influence notre résultat de mesure. Imaginons par exemple que nous voulions mesurer la tension aux bornes d'un diviseur de tension : la résistance interne de l'appareil de mesure charge légèrement le diviseur de tension, de sorte que nous ne mesurons pas exactement la tension qu'un appareil de mesure idéal afficherait. 

<margin>
[picture:1004:a_reale_spannungsmessung:Schéma équivalent d'un voltmètre réel]
</margin>

---

Il en va de même pour l'ampèremètre que pour le voltmètre. Un ampèremètre réel se compose de l'ampèremètre proprement dit et d'une petite résistance branchée en série, aux bornes de laquelle chute toujours une petite tension. Si cette résistance était nulle, elle n'existerait pratiquement pas — et nous aurions de nouveau l'appareil de mesure idéal.

<margin>
[picture:1007:a_reale_strommessung:Schéma équivalent d'un ampèremètre réel]
</margin>

---

[question:AI104]

<tip>
Dans cette question, l'indication « plus petite résolution $\qty{100}{\micro\volt}$ » n'est pas importante. Elle peut être résolue à l'aide de la seule loi d'Ohm.
</tip>

---

Qu'en est-il maintenant des grandeurs caractéristiques calculées à partir de valeurs mesurées — comme la puissance dans notre exemple du début ($P = U \cdot I$) après une mesure de courant et de tension ? Les grandeurs mesurées individuelles comme le courant et la tension s'écartent chacune de la valeur réelle en raison des erreurs de mesure, et ces écarts se répercutent en conséquence dans le calcul.

Regardons un exemple concret : supposons que nous voulions déterminer la puissance et que nous mesurions pour cela une tension continue et un courant continu. Les deux appareils de mesure affichent des valeurs qui sont chacune trop basses de cinq pour cent. Il ne faut pas commettre l'erreur d'additionner simplement les écarts des grandeurs mesurées individuelles. La formule de la puissance fait apparaître que les erreurs se multiplient dans ce cas. Regardons cela en détail :

$U_\text{mes}=0,95 \cdot U_\text{vrai}$ et $I_\text{mes}=0,95 \cdot I_\text{vrai}$

Nous calculons la puissance avec notre formule bien connue :

$P_\text{mes}=U_\text{mes} \cdot I_{mes}$

Insérons maintenant les valeurs vraies : 

$P_\text{mes} = 0,95 \cdot U_\text{vrai} \cdot 0,95 \cdot I_\text{vrai} = 0,9025 \cdot U_\text{vrai} \cdot I_\text{vrai}$

Cela signifie que la puissance mesurée est environ $\qty{9,75}{\percent}$ plus basse que la puissance réelle, car $1-0,9025 \equiv \qty{9,75}{\percent}$. Avec ces connaissances, la question d'examen suivante peut être résolue ; les valeurs concrètes de courant et de tension ne sont pas pertinentes pour la solution.

[question:AI103]
