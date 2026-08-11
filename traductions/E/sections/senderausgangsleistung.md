Les radioamateurs sont légalement tenus de respecter certaines valeurs limites concernant la puissance de leurs installations radio. Sont particulièrement importantes la puissance de sortie de l'émetteur ainsi que la prévention des émissions non désirées — nous aborderons ces dernières au chapitre suivant. Dans ce chapitre, nous nous occupons d'abord de la puissance de sortie de l'émetteur.

Dans beaucoup de bandes radioamateur attribuées à titre primaire au service d'amateur, la puissance de sortie maximale de l'émetteur — en anglais Peak Envelope Power (en abrégé PEP) — constitue la valeur limite de référence. Les prescriptions de puissance exactes se trouvent dans l'[annexe 1](https://50ohm.de/a1) de l'AFuV.

---

Comme le montre la figure [ref:e_senderausgangsleisung], la puissance de sortie d'un émetteur se mesure toujours directement à la sortie de l'émetteur — sans qu'aucun appareil supplémentaire, filtre ou câble ne soit intercalé. Pour déterminer la puissance d'un émetteur SSB, celui-ci doit être excité par une modulation appropriée d'amplitude constante. Un procédé simple consiste à injecter un signal à une tonalité, par exemple en appuyant sur le manipulateur morse en mode CW ; une excitation à deux tonalités est toutefois encore meilleure. Une mesure avec de la parole est inadaptée, car la puissance de sortie fluctue alors fortement.

<margin>
[picture:916:e_senderausgangsleisung:Mesure de la puissance de sortie de l'émetteur]
</margin>

<indepth>
Un *signal à deux tonalités* est idéal pour la mesure de puissance et de linéarité d'un émetteur SSB, parce qu'il contient deux tonalités sinusoïdales propres d'amplitude constante. Il se forme ainsi dans l'émetteur exactement les produits de mélange typiques des signaux de parole réels, mais sous une forme clairement définie et reproductible.
</indepth>


[question:EF401]
[question:EF402]

---

La PEP décrit la puissance de crête de l'émetteur dans des conditions normales d'exploitation : c'est la puissance que l'émetteur peut fournir en moyenne à une charge résistive réelle, pendant une période de l'oscillation haute fréquence, au sommet le plus élevé de l'enveloppe de modulation (cf. figure [ref:e_senderausgangsleisung_2]). La manière de mesurer exactement la PEP — par exemple à l'aide d'un oscilloscope — ne sera traitée en détail qu'en classe A.

<margin>
[picture:875:e_senderausgangsleisung_2:Sommet le plus élevé de l'enveloppe de modulation]
</margin>

[question:EB501]

Outre la puissance de crête d'un émetteur (PEP), il existe aussi la *puissance moyenne*. Elle est indépendante de l'enveloppe, parce que la puissance mesurée au cours du temps est moyennée sur un intervalle long par rapport à la période de la fréquence de modulation la plus basse. Avec ce raisonnement, on peut identifier très facilement la bonne réponse à la question suivante.

[question:EB502]
<france>
# La France plafonne la PEP, pas la puissance rayonnée

La notion que vous venez d'étudier est précisément celle sur laquelle repose le droit français. Là où la réglementation allemande raisonne en puissance rayonnée, l'annexe de la décision ARCEP n° 2012-1241 fixe des plafonds en **puissance en crête à la sortie de l'émetteur**, au sens de l'article 1.157 du Règlement des radiocommunications — c'est-à-dire exactement la PEP.

La différence est considérable en pratique. Un plafond exprimé à la sortie de l'émetteur ne tient compte ni du gain de l'antenne, ni des pertes de la ligne : une antenne directive à fort gain n'oblige pas à réduire la puissance de l'émetteur, alors qu'un plafond en puissance rayonnée l'imposerait. En contrepartie, le calcul de la protection des personnes s'appuie bien, quant à lui, sur la puissance rayonnée — les deux notions coexistent, chacune pour son usage.

Les paliers sont dégressifs avec la fréquence, tels que les fixe l'annexe de la décision dans sa rédaction issue de la décision n° 2019-1412 :

| Bandes | Puissance maximale |
| --- | --- |
| $\qtyrange{135,7}{137,8}{\kilo\hertz}$ et $\qtyrange{472}{479}{\kilo\hertz}$ | $\qty{1}{\watt}$ PIRE |
| $\qtyrange{5351,5}{5366,5}{\kilo\hertz}$ (bande des $\qty{60}{\meter}$) | $\qty{15}{\watt}$ PIRE |
| de $\qty{1,8}{\mega\hertz}$ à $\qty{24,99}{\mega\hertz}$ | $\qty{500}{\watt}$ |
| $\qtyrange{28}{29,7}{\mega\hertz}$ | $\qty{250}{\watt}$ |
| de $\qty{50}{\mega\hertz}$ à $\qty{250}{\giga\hertz}$ | $\qty{120}{\watt}$ |

Notez l'exception des trois bandes basses, où le texte raisonne non plus en puissance de sortie mais en **puissance isotrope rayonnée équivalente**. C'est le seul endroit où le droit français adopte la logique allemande, et il le fait parce que le Règlement des radiocommunications l'impose par les notes propres à ces trois bandes.

Deux conséquences pour l'opérateur :

* le plafond s'entend **crête**, donc mesuré au sommet de l'enveloppe de modulation, et non en puissance moyenne ; c'est la valeur qu'affiche un wattmètre en position PEP ;
* le dernier alinéa du paragraphe 1 de l'annexe impose de disposer d'un **indicateur de puissance** — l'un des rares équipements dont la présence est exigée par le texte.
</france>
