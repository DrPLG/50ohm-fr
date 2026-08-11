Dans la modulation d'amplitude (AM) ainsi qu'en SSB, l'information à transmettre est véhiculée par une variation de l'amplitude de la porteuse haute fréquence. En classe N, nous avons déjà appris qu'avec la modulation de fréquence (FM), l'amplitude de la porteuse reste au contraire constante — l'information est ici transmise par une variation de la fréquence instantanée de la porteuse.

La figure [ref:e_frequenzmodulation_t] montre l'évolution temporelle d'un signal FM à amplitude constante. Un signal FM se reconnaît donc au fait que l'amplitude de la porteuse reste (idéalement) constante, tandis que sa fréquence instantanée varie continuellement en fonction du signal modulant.

<margin>
[picture:906:e_frequenzmodulation_t:Évolution temporelle d'un signal FM]
</margin>

[question:EE301]

---

La figure [ref:e_frequenzmodulation_frequenzhub] montre à titre d'exemple un signal BF sinusoïdal qui provoque dans le spectre un écart de fréquence correspondant (excursion de fréquence) d'une porteuse haute fréquence. Autrement dit, dans un signal FM, l'information de volume sonore est transmise par l'*excursion de la fréquence porteuse (excursion de fréquence)*. Un signal BF plus fort conduirait à une plus grande excursion de la fréquence porteuse et donc à une largeur de bande plus élevée du signal FM.

<margin>
[picture:827:e_frequenzmodulation_frequenzhub:Excursion de la porteuse en modulation de fréquence]
</margin>

<indepth>
La largeur de bande occupée par une émission FM est déterminée par l'excursion et par la fréquence de modulation maximale. En première approximation, pour une faible excursion et une fréquence de modulation basse, on peut appliquer la *formule de Carson*. Elle indique dans quelle largeur de bande se trouvent $\qty{90}{\percent}$ de la puissance d'émission.

$B\approx2 \cdot \left(\Delta f_{\textrm{T}} + f_{\textrm{mod max}} \right)$
  
Ce sujet est traité plus en détail en classe A. 
</indepth>

[question:EE306]
[question:EE304]

Pour respecter les prescriptions légales concernant la largeur de bande occupée par un signal FM, le signal du microphone est d'abord limité en amplitude dans les émetteurs FM (par un amplificateur limiteur), puis modulé en FM sur la porteuse. L'excursion de fréquence du modulateur à l'excursion maximale du volume est alors soit fixée, soit réglable au moyen d'un réglage d'excursion.

[question:EE305]

Du fait que l'information modulée n'est pas contenue dans l'amplitude mais uniquement dans la fréquence, les signaux FM sont relativement insensibles aux perturbations d'amplitude (par exemple dues aux éclairs, aux systèmes d'allumage, aux moteurs) en comparaison de l'AM ou de la SSB. Il en résulte des avantages en matière de sensibilité aux perturbations, en particulier pour le trafic en véhicule et dans les environnements perturbés.

[question:EE302]
[question:EE303]
<france>
# Ce que « prescriptions légales » veut dire en France

Les prescriptions auxquelles renvoie ce paragraphe sont, côté français, des valeurs chiffrées. Le paragraphe 3 de l'annexe de la décision ARCEP n° 2012-1241 plafonne la largeur de bande occupée en fonction de la seule fréquence d'émission, quel que soit le mode :

| Fréquence d'émission | Largeur de bande occupée |
| --- | --- |
| en dessous de $\qty{28}{\mega\hertz}$ | $\qty{6}{\kilo\hertz}$ au plus |
| de $\qty{28}{\mega\hertz}$ à $\qty{144}{\mega\hertz}$ | $\qty{12}{\kilo\hertz}$ au plus |
| de $\qty{144}{\mega\hertz}$ à $\qty{225}{\mega\hertz}$ | $\qty{20}{\kilo\hertz}$ au plus |
| au-dessus de $\qty{225}{\mega\hertz}$ | aucune limite chiffrée |

C'est ce qui donne tout son sens à l'amplificateur limiteur décrit ici. Une FM de radiodiffusion, avec son excursion généreuse, occuperait bien davantage : le limiteur d'amplitude n'est pas un raffinement de confort, il est la condition du respect du plafond.

L'application pratique est immédiate. Une émission FM courante, dont la formule de Carson donne une quinzaine de kilohertz, tient sans difficulté sur $\qty{145}{\mega\hertz}$. La même émission serait **hors des clous sur $\qty{29}{\mega\hertz}$**, où le plafond tombe à $\qty{12}{\kilo\hertz}$ — et davantage encore en dessous de $\qty{28}{\mega\hertz}$, où il n'est plus que de $\qty{6}{\kilo\hertz}$. C'est la raison pour laquelle la FM ne se pratique pas en décamétrique, hors du segment supérieur du $\qty{10}{\meter}$.

Le réglage d'excursion mentionné ci-dessus n'est donc pas neutre : mal réglé, il fait sortir l'émission de son gabarit légal avant même d'être audible comme une distorsion.
</france>
