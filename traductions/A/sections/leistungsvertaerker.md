Dans le domaine du radioamateurisme, les amplificateurs de puissance servent à amplifier le signal HF produit en interne par les étages précédents, afin d'obtenir la puissance de sortie souhaitée de l'émetteur. On distingue ici fondamentalement 2 types d'amplificateurs HF. D'une part les amplificateurs HF à large bande, dont le gain reste constant sur une plage de fréquences relativement large (par exemple le domaine décamétrique $\qtyrange{1}{30}{\mega\hertz}$). D'autre part les amplificateurs HF sélectifs, dont le gain n'est maximal que dans une plage de fréquences étroite (par exemple seulement dans une bande amateur du domaine décamétrique).

Les amplificateurs HF à large bande se reconnaissent typiquement à leurs transformateurs de couplage large bande entre les différents étages amplificateurs, lesquels ne sont **pas** constitués en circuit oscillant par une capacité en parallèle ou en série.

Les amplificateurs HF sélectifs se reconnaissent en revanche typiquement à leur conception sélective en fréquence, caractérisée par des circuits oscillants série ou parallèle dans le trajet du signal HF.



[question:AF412]
[question:AF408]

Les amplificateurs des types précités peuvent aussi être réalisés en plusieurs étages, par mise en cascade d'étages individuels.

[question:AF413]

Entre les étages amplificateurs d'un amplificateur de puissance, ainsi qu'à leurs entrées et sorties, il est nécessaire de procéder à une adaptation d'impédance. Cela est nécessaire pour que l'impédance HF de sortie d'un étage précédent soit adaptée au mieux à l'impédance HF d'entrée de l'étage suivant, en vue d'un gain maximal, de distorsions minimales et d'un rendement optimal (évitement des réflexions et des non-linéarités). 

L'adaptation d'impédance peut se faire soit à large bande, par l'emploi d'un transformateur de rapport de transformation approprié, soit de façon sélective en fréquence, par un circuit oscillant à prise.

Dans le cas de l'adaptation sélective en fréquence, il existe deux possibilités fondamentales de la réaliser :
- par un diviseur de tension inductif (bobine à prise et condensateur en parallèle)
- par un diviseur de tension capacitif (deux condensateurs en série avec une bobine en parallèle)

Ces bobines et condensateurs peuvent être disposés selon différentes configurations (circuit parallèle ou série) afin d'obtenir la transformation d'impédance souhaitée et, le cas échéant, de supprimer en même temps les harmoniques supérieures (filtre en Pi).

[question:AF409]
[question:AF410]
[question:AF414]
[question:AF407]
[question:AF406]
[question:AF417]

---

Un filtre en Pi (cf. figure [ref:a_pi_filter]) peut adapter les impédances à son entrée et à sa sortie par le rapport des deux capacités. La bobine du filtre en PI définit, conjointement avec les deux capacités, la fréquence de conception du filtre. Le filtre en PI supprime en même temps, par son caractère de passe-bas, les harmoniques supérieures indésirables du signal émis.

<margin>
[picture:1100:a_pi_filter:Filtre en PI]
</margin>

[question:AF405]

Un montage LC placé après un amplificateur de puissance HF a une fonction analogue. Celui-ci sert lui aussi à l'adaptation d'impédance et, en même temps, à la suppression des harmoniques supérieures.

[question:AF404]

Le rendement d'un amplificateur de puissance HF est défini par le rapport de la puissance HF de sortie délivrée par l'amplificateur de puissance à la puissance d'alimentation en courant continu fournie à l'amplificateur.

[question:AF401]

Les éléments actifs d'un amplificateur de puissance ont besoin, outre de la tension de service nécessaire, d'un réglage du point de fonctionnement (BIAS) en tension continue. Ce point de fonctionnement est habituellement produit par des diviseurs de tension qui, à partir d'une tension auxiliaire stabilisée, produisent aux bornes des éléments la tension de BIAS souhaitée, l'emploi de potentiomètres ajustables permettant un réglage optimal.
Lorsque l'on considère la tension de BIAS et ses effets sur les éléments du montage, celui-ci n'est à considérer que du point de vue de la tension continue. Les condensateurs, en tant qu'éléments qui ne peuvent transmettre que des tensions alternatives, sont ici ignorés.
Les enroulements des transformateurs ainsi que les bobines sont vus comme des courts-circuits lors de l'examen en tension continue.

[question:AF420]
[question:AF423]
[question:AF424]

%TODO Fragennummern fixen
%TODO doe Frage 2373 bräuchte eine genauerer Erklärung wie man auf die 3.5 V kommt (370||6800 = 350).

Le calcul de la tension de BIAS pour un montage donné (question AF421) s'effectue en appliquant la loi d'Ohm, en tenant compte des montages de résistances en parallèle et en série. Il importe, dans l'examen de la question, de noter que les connexions de grille des transistors représentent des capacités et sont donc négligeables lors de l'examen en tension continue.

[question:AF421]

Dans les amplificateurs de puissance, il importe de découpler au mieux les différents étages de la tension de service du point de vue de la HF, afin d'éviter les réactions sur d'autres étages (tendance aux oscillations, effets de modulation, etc.). Pour cela, les amenées de tension de service des différents étages sont découplées les unes des autres par des inductances montées en série ainsi que par des condensateurs de découplage vers la masse. Cette disposition constitue un passe-bas, car, dans le cas idéal, seule la tension de service continue souhaitée est laissée passer, tandis que les composantes HF sont bloquées.

[question:AF411]
[question:AF419]
[question:AF418]
[question:AF422]

Les propriétés HF des condensateurs réels dépendent de la fréquence. Les grandes capacités, comme les condensateurs électrolytiques, ne peuvent être employées qu'aux basses fréquences et ne sont que d'une efficacité limitée dans le domaine HF. Pour découpler également les fréquences plus élevées au moyen de condensateurs, on utilise fréquemment une combinaison de types de condensateurs et de valeurs de capacité différents, qui peuvent ensemble découpler une plage de fréquences plus large.

[question:AF415]

Pour déterminer le gain total d'un amplificateur de puissance à plusieurs étages, il faut effectuer la différence entre la puissance de sortie et la puissance d'entrée par soustraction, en respectant les signes, des valeurs en dBm. Exemple : une puissance d'entrée de $\qty{-5}{\dBm}$ et une puissance de sortie de $\qty{20}{\dBm}$ donnent un gain total de $\qty{25}{\dB}$ ($\qty{20}{\dBm} - (\qty{-5}{\dBm}) = \qty{25}{\dB}$)

[question:AF428]

<france>
# Ce que la réglementation française plafonne, et ce qu'elle ne plafonne pas

Un amplificateur de puissance pose immédiatement la question de la limite légale. En France, la réponse tient à un choix de définition : l'annexe de la décision ARCEP n° 2012-1241, dans sa rédaction issue de la décision n° 2019-1412, fixe des plafonds en **puissance en crête à la sortie de l'émetteur**, au sens de l'article 1.157 du Règlement des radiocommunications — c'est-à-dire la PEP.

| Bandes | Puissance maximale |
| --- | --- |
| $\qtyrange{135,7}{137,8}{\kilo\hertz}$ et $\qtyrange{472}{479}{\kilo\hertz}$ | $\qty{1}{\watt}$ PIRE |
| $\qtyrange{5351,5}{5366,5}{\kilo\hertz}$ (bande 60 m) | $\qty{15}{\watt}$ PIRE |
| de $\qty{1,8}{\mega\hertz}$ à $\qty{24,99}{\mega\hertz}$ | $\qty{500}{\watt}$ |
| $\qtyrange{28}{29,7}{\mega\hertz}$ | $\qty{250}{\watt}$ |
| de $\qty{50}{\mega\hertz}$ à $\qty{250}{\giga\hertz}$ | $\qty{120}{\watt}$ |

Trois conséquences pratiques pour qui met un amplificateur en service :

* **Le gain d'antenne n'entre pas dans le calcul.** Le plafond s'apprécie à la sortie de l'émetteur, avant la ligne et avant l'antenne. Une Yagi à fort gain n'oblige donc pas à réduire la puissance — à la différence d'un plafond exprimé en puissance rayonnée. C'est un point sur lequel un opérateur venu de la réglementation allemande se trompera s'il ne l'a pas noté.
* **La mesure est une mesure de crête.** C'est le sommet de l'enveloppe de modulation qui compte, non la puissance moyenne. Un amplificateur affichant $\qty{400}{\watt}$ en régime porteuse continue et dont les crêtes atteignent $\qty{600}{\watt}$ en BLU dépasse le plafond des $\qty{500}{\watt}$.
* **Un indicateur de puissance est obligatoire.** Le dernier alinéa du paragraphe 1 de l'annexe l'exige — l'un des très rares équipements dont la présence soit imposée par le texte, avec la charge non rayonnante.

Trois bandes basses font exception et se comptent en **puissance isotrope rayonnée équivalente** : $\qtyrange{135,7}{137,8}{\kilo\hertz}$, $\qtyrange{472}{479}{\kilo\hertz}$ et la bande 60 m. C'est le Règlement des radiocommunications qui l'impose, par ses notes 5.67A, 5.80A et 5.133B — et c'est le seul endroit où le droit français adopte la logique de puissance rayonnée.

Ce que la réglementation ne plafonne pas, en revanche, mérite d'être dit : elle ne fixe **aucune limite au gain des antennes**. La contrainte qui joue alors est celle de la protection des personnes, traitée au chapitre correspondant, et qui, elle, raisonne bien en puissance rayonnée.
</france>
