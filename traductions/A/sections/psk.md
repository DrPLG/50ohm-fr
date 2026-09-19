Dans la modulation par déplacement de phase (Phase-Shift Keying, PSK), les différents symboles sont représentés par des phases différentes d'une porteuse. L'amplitude et la fréquence de la porteuse restent alors identiques. Lors du passage d'un symbole au suivant, la phase peut en revanche changer.

La figure [ref:a_psk] montre un signal PSK en représentation temporelle. Aux frontières entre symboles, on reconnaît que l'oscillation se poursuit avec une autre phase.

<margin>
[picture:705:a_psk:Modulation par déplacement de phase (Phase-Shift Keying)]
</margin>

---

La forme la plus simple est la modulation par déplacement de phase binaire (Binary Phase-Shift Keying, BPSK). On dispose alors de deux phases différentes, et donc de deux symboles possibles. On peut par exemple employer les phases $\qty{0}{\degree}$ et $\qty{180}{\degree}$ et les associer aux valeurs binaires $0$ et $1$. La figure [ref:a_psk_mapping] montre un mapping possible des deux valeurs binaires sur les deux symboles BPSK.

Comme les deux symboles ne se distinguent que par leur phase et que leur amplitude est identique, les deux points du diagramme de constellation se situent en vis-à-vis sur un cercle.

<margin>
[picture:1101:a_psk_mapping:BPSK dans le diagramme de constellation]
</margin>

<indepth>
Subtilité : à strictement parler, la BPSK aux angles $\qty{0}{\degree}$ et $\qty{180}{\degree}$ peut aussi être considérée comme un procédé ASK, dans lequel l'amplitude du signal porteur est commutée entre une valeur négative et une valeur positive. Pour un signal sinusoïdal, une multiplication par $-1$ se traduit par un déphasage de $\qty{180}{\degree}$ :

$-\sin(\omega t)=\sin(\omega t+\qty{180}{\degree})$

Il s'agit d'un cas particulier. D'autres angles de phase seraient d'ailleurs possibles, comme p. ex. $\qty{90}{\degree}$ et $\qty{270}{\degree}$, dont les deux phases de symbole seraient elles aussi séparées de $\qty{180}{\degree}$.
</indepth>

[question:AE401]

---

Avec plus de deux phases différentes, on peut représenter d'autant plus de symboles. Cela permet de regrouper plusieurs bits en un seul symbole.

---

Dans la modulation par déplacement de phase en quadrature (Quadrature Phase-Shift Keying, QPSK), on dispose de quatre phases différentes, et donc de quatre symboles possibles. Comme il existe quatre combinaisons possibles de deux bits, chaque symbole permet de transmettre deux bits.

À titre de comparaison :

* BPSK : $\num{2}$ symboles → $\num{1}$ bit par symbole
* QPSK : $\num{4}$ symboles → $\num{2}$ bits par symbole
* 8-PSK : $\num{8}$ symboles → $\num{3}$ bits par symbole

[question:AE402]

Examinons maintenant la QPSK dans le diagramme de constellation. Les quatre symboles possibles possèdent la même amplitude, mais se distinguent par leur phase. C'est pourquoi les quatre points de signal se situent sur un cercle. La figure [ref:a_qpsk] montre un mapping possible des quatre combinaisons de bits $00$, $01$, $10$ et $11$ sur les quatre symboles QPSK.

<margin>
[picture:1059:a_qpsk:Diagramme I/Q d'un mapping QPSK]
</margin>

---

Dans cet exemple, les phases suivantes sont employées :

* $11$ correspond à $\qty{45}{\degree}$
* $01$ correspond à $\qty{135}{\degree}$
* $00$ correspond à $\qty{225}{\degree}$
* $10$ correspond à $\qty{315}{\degree}$

<margin>
L'applet suivant illustre la modulation QPSK numérique. Dans un système réel, le signal est affecté par le bruit et par d'autres perturbations. Les points de signal reçus ne se situent alors pas exactement aux positions idéales, mais s'en écartent aussi bien en amplitude qu'en phase. L'applet simule cela en ajoutant du bruit. Les croix marquent les quatre symboles QPSK idéaux. Chaque point coloré est une valeur reçue bruitée. Le récepteur la rattache au symbole le plus proche. Les zones colorées en fond sont les zones de décision du récepteur. Tant qu'une valeur reçue bruitée se situe dans la zone du symbole initialement émis, celui-ci est correctement reconnu. Si un point franchit, du fait d'un bruit important, une frontière vers une zone voisine, le récepteur se décide pour le mauvais symbole. Ces erreurs peuvent toutefois être corrigées par le codage de canal. Nous nous en occuperons dans une section ultérieure.

[include:applet_qpsk]
</margin>

Les quatre phases sont décalées de $\qty{90}{\degree}$ les unes par rapport aux autres. Le récepteur peut déterminer, d'après la phase reconnue, quel symbole et donc quelle combinaison de bits a été transmis.

L'association des combinaisons de bits aux différentes phases n'est pas fixée de façon univoque. Seul importe d'abord qu'une combinaison de bits univoque soit associée à chaque symbole.

En pratique, le mapping est fréquemment choisi de telle sorte que les combinaisons de bits de points de signal voisins ne se distinguent que par un seul bit. Une telle association est appelée *code de Gray*. Si, du fait du bruit, un point de signal voisin est reconnu par erreur, cela ne conduit alors souvent qu'à une seule erreur binaire.

Le diagramme de constellation rend ainsi immédiatement visible une différence essentielle entre l'ASK et la PSK : en ASK, les symboles se distinguent par leur distance à l'origine et se situent en règle générale uniquement sur l'axe I positif, tandis qu'en PSK ils se distinguent par leur angle. En PSK, les points de signal se situent donc sur un cercle, à amplitude égale.
