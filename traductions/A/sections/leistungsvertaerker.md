Dans le chapitre consacré aux montages fondamentaux, nous avons déjà fait connaissance avec différents amplificateurs à transistors. Dans l'émetteur, nous nous intéressons maintenant en particulier aux *amplificateurs de puissance*. Ils amplifient le signal HF produit dans les étages précédents jusqu'à la puissance de sortie souhaitée de l'émetteur.

On distingue fondamentalement deux types d'amplificateurs de puissance HF :

1. Les *amplificateurs HF à large bande* présentent un gain aussi constant que possible sur une plage de fréquences relativement large, par exemple sur une grande partie du domaine décamétrique de $\qtyrange{1}{30}{\mega\hertz}$, cf. figure [ref:a_breitbandverstärker].
2. Les *amplificateurs HF sélectifs* sont en revanche accordés sur une plage de fréquences comparativement étroite, par exemple sur une seule bande radioamateur, cf. figure [ref:a_selektiver_verstaerker].

Les amplificateurs HF à large bande se reconnaissent souvent à leurs transformateurs de couplage large bande entre les différents étages amplificateurs. Ceux-ci ne forment pas, avec des condensateurs, de circuits oscillants accordés sur une fréquence particulière. On retrouve également, dans de nombreux amplificateurs de puissance HF, le principe déjà connu de l'amplificateur push-pull.

<margin>
[picture:491:a_breitbandverstärker:Amplificateur de puissance HF à large bande, montage push-pull]
</margin>

[question:AF412]

Les amplificateurs HF sélectifs se reconnaissent en revanche typiquement à leur conception sélective en fréquence, caractérisée par des circuits oscillants série ou parallèle dans le trajet du signal HF.

<margin>
[picture:778:a_selektiver_verstaerker:Amplificateur de puissance HF sélectif, à conception sélective en fréquence]
</margin>

[question:AF408]

---

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

---

La figure [ref:a_fet_verstaerker] montre un amplificateur décamétrique à transistors à effet de champ LDMOS. LDMOS signifie *Laterally Diffused Metal-Oxide-Semiconductor* et désigne un type particulier de transistor à effet de champ destiné aux amplificateurs de puissance HF. Le montage amplificateur proprement dit (partie supérieure) est de conception très simple : il s'agit là encore d'un amplificateur push-pull, à deux FET fonctionnant en configuration push-pull. Les deux transistors sont attaqués par un transformateur d'entrée commun. La sortie de l'amplificateur est prélevée par l'intermédiaire d'un autre transformateur. La partie inférieure du montage est elle aussi moins complexe qu'il n'y paraît : dans l'ensemble, elle ne fait que produire, au moyen d'un diviseur de tension, la tension de BIAS des transistors.

Il ne faut pas se laisser tromper par la propriété bien connue d'un transistor à effet de champ : en tension continue, la grille ne laisse pratiquement passer aucun courant et présente donc une impédance d'entrée très élevée. Aux fréquences élevées, en revanche, les capacités parasites du transistor jouent un rôle important, en particulier les capacités entre grille et source ainsi qu'entre grille et drain. Leur réactance capacitive diminue lorsque la fréquence augmente, de sorte qu'un courant HF peut circuler dans la grille. Pour les transistors de puissance HF, l'impédance d'entrée peut donc être nettement plus faible que ne le laisserait attendre l'examen en courant continu d'un FET. Le transformateur d'entrée $T_1$ sert donc à adapter les $\qty{50}{\ohm}$ à la faible impédance d'entrée des transistors.

<margin>
[picture:786:a_fet_verstaerker:Amplificateur décamétrique à transistors à effet de champ]
</margin>

[question:AF417]

---

Comme évoqué plus haut, les éléments actifs d'un amplificateur de puissance ont besoin, outre de la tension de service nécessaire, d'un réglage du point de fonctionnement (BIAS) en tension continue. Ce point de fonctionnement est habituellement produit par des diviseurs de tension qui, à partir d'une tension auxiliaire stabilisée, produisent aux bornes des éléments la tension de BIAS souhaitée, l'emploi de potentiomètres ajustables permettant un réglage optimal.

<tip>
Lorsque l'on considère la tension de BIAS et ses effets sur les éléments du montage, celui-ci n'est à considérer que du point de vue de la tension continue. Les condensateurs, en tant qu'éléments qui ne peuvent transmettre que des tensions alternatives, sont ici ignorés. Les enroulements des transformateurs ainsi que les bobines sont vus comme des courts-circuits lors de l'examen en tension continue. De façon générale, il suffit pour ces questions d'appliquer les connaissances de base des classes N et E sur la loi d'Ohm et les diviseurs de tension !
</tip>

[question:AF420]

---

Le calcul de la tension de BIAS pour le montage donné dans la question suivante s'effectue en appliquant la loi d'Ohm, en tenant compte des montages de résistances en parallèle et en série. Il importe, dans l'examen de la question, de noter que les connexions de grille des transistors représentent des capacités et sont donc négligeables lors de l'examen en tension continue.

[question:AF421]

<indepth>
La résistance $R_5=\qty{51}{\ohm}$ n'a pratiquement aucun effet sur la tension continue de grille, car il ne circule quasiment aucun courant continu dans la grille du transistor LDMOS. Pour le signal HF, en revanche, $R_5$ joue un rôle important : associée à la capacité de grille, elle amortit d'éventuelles oscillations haute fréquence et améliore ainsi la stabilité de l'amplificateur.

La résistance $R_4=\qty{6,8}{\kilo\ohm}$ garantit que la grille conserve un potentiel défini par rapport à la masse, même en cas de coupure du réglage du point de fonctionnement. Elle décharge en outre la capacité de grille et évite ainsi qu'une grille flottante ne rende le transistor conducteur de façon intempestive, par exemple si le potentiomètre $R_3$ est défectueux. $R_4$ étant montée en parallèle sur la branche inférieure du diviseur de tension, il faut en tenir compte pour le calcul précis de la tension de grille.
</indepth>

---

Le montage de la figure [ref:a_fet_verstaerker_vhf] montre un amplificateur de puissance VHF à transistors à effet de champ. Là encore, les deux transistors fonctionnent en étage final push-pull, ce qui constitue la partie simple du montage. Les courtes lignes coaxiales font partie du réseau d'adaptation et servent à transformer la faible impédance des transistors LDMOS vers une impédance adaptée au reste du montage. Le reste du montage consiste, une fois de plus, à produire la tension de BIAS des transistors, avec en plus une compensation en température. Les potentiomètres $R_1$ et $R_2$ forment chacun un diviseur de tension qui règle la tension de BIAS du transistor correspondant.

[question:AF424]
[question:AF423]

<margin>
[picture:783:a_fet_verstaerker_vhf:Amplificateur VHF à transistors à effet de champ]
</margin>


---

Un filtre en Pi (cf. figure [ref:a_pi_filter]) peut adapter les impédances à son entrée et à sa sortie par le rapport des deux capacités. La bobine du filtre en PI définit, conjointement avec les deux capacités, la fréquence de conception du filtre. Le filtre en PI supprime en même temps, par son caractère de passe-bas, les harmoniques supérieures indésirables du signal émis.

<margin>
[picture:1100:a_pi_filter:Filtre en PI]
</margin>

[question:AF405]

Un montage LC placé après un amplificateur de puissance HF a une fonction analogue. Celui-ci sert lui aussi à l'adaptation d'impédance et, en même temps, à la suppression des harmoniques supérieures.

[question:AF404]

Dans les amplificateurs de puissance, il importe de découpler au mieux les différents étages de la tension de service du point de vue de la HF, afin d'éviter les réactions sur d'autres étages (tendance aux oscillations, effets de modulation, etc.). Pour cela, les amenées de tension de service des différents étages sont découplées les unes des autres par des inductances montées en série ainsi que par des condensateurs de découplage vers la masse. Cette disposition constitue un passe-bas, car, dans le cas idéal, seule la tension de service continue souhaitée est laissée passer, tandis que les composantes HF sont bloquées.

[question:AF411]
[question:AF419]
[question:AF418]
[question:AF422]

Les propriétés HF des condensateurs réels dépendent de la fréquence. Les grandes capacités, comme les condensateurs électrolytiques, ne peuvent être employées qu'aux basses fréquences et ne sont que d'une efficacité limitée dans le domaine HF. Pour découpler également les fréquences plus élevées au moyen de condensateurs, on utilise fréquemment une combinaison de types de condensateurs et de valeurs de capacité différents, qui peuvent ensemble découpler une plage de fréquences plus large.

[question:AF415]

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
