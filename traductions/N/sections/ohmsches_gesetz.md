Nous avons déjà fait connaissance avec les trois grandeurs les plus importantes de l'électrotechnique, à savoir la tension électrique, le courant électrique et la résistance :
* Nous avons d'abord appris que des charges électriques sont séparées dans les sources de tension et qu'il en résulte une tension électrique. Nous la désignons par la lettre $U$ et la mesurons en volts ($\unit{V}$).
* Nous avons ensuite appris que la tension électrique fait circuler dans un circuit fermé un courant électrique, que nous désignons par la lettre $I$ et mesurons en ampères ($\unit{A}$).
* Et au début de ce chapitre, nous avons enfin appris que les consommateurs dans un circuit exercent une résistance et freinent ainsi le passage du courant. Nous désignons la résistance par la lettre $R$ et la mesurons en ohms ($\unit{\ohm}$).

%<margin>
%[p-h-o-t-o:147:ohmsches_gesetz_comic:Représentation imagée des relations de la loi d'Ohm]
%</margin>

[question:NA203]

---

Mais comment ces trois grandeurs sont-elles liées ? Examinons un exemple dans la figure [ref:n_ohmsches_gesetz_stromkreis_mit_batterie]. Nous avons un circuit composé d'une pile comme source de tension et d'une résistance. Nous connaissons la tension et nous pouvons mesurer le courant. La pile a une tension de $\qty{10}{\volt}$, et il circule un courant de $\qty{1}{\milli\ampere}$.

<margin>
[picture:664:n_ohmsches_gesetz_stromkreis_mit_batterie:Circuit avec pile]
</margin>

Si l'on remplaçait la pile de $\qty{10}{\volt}$ de l'exemple par une pile de $\qty{20}{\volt}$, le courant augmenterait lui aussi de $\qty{1}{\milli\ampere}$ à $\qty{2}{\milli\ampere}$. Si l'on double donc la tension, le courant double aussi. De même, le courant serait divisé par deux, à $\qty{0,5}{\milli\ampere}$, si l'on divisait la tension par deux, à $\qty{5}{\volt}$.

Nous pouvons reconnaître un motif : dans notre exemple, la tension $U$ en volts est toujours 10000 fois plus grande que le courant $I$ en ampères. Ou, exprimé mathématiquement :

$\dfrac{U}{I} = \dfrac{\qty{10}{\volt}}{\qty{0,001}{\ampere}} = \dfrac{\qty{20}{\volt}}{\qty{0,002}{\ampere}} = \dfrac{\qty{5}{\volt}}{\qty{0,0005}{\ampere}} = 10000 \frac{\unit{\volt}}{\unit{\ampere}}$

---

Dans le langage technique, on appelle cela la proportionnalité : $I$ est proportionnel à $U$. Si l'on met de côté les unités, le *facteur de proportionnalité* vaut 10000 dans notre exemple : en multipliant une valeur par 10000, on obtient l'autre valeur.
%Dieses Verhalten kann man sich auch wieder am Wasserkreislauf vorstellen: Wenn die Pumpe mit mehr Druck pumpt, wird auch mehr Wasser durch den Kreislauf fließen.

<indepth>
Le *facteur de proportionnalité* est le rapport numérique de deux grandeurs proportionnelles l'une à l'autre.
</indepth>

Il reste toutefois une question. D'où vient ce facteur de 10000 ? La réponse est simple : c'est notre résistance $R$ ! Et si nous considérons maintenant aussi les unités, un tableau d'ensemble se dessine : l'unité ohm est en effet définie de telle sorte que $\qty{1}{\ohm}$ est identique à $\qty{1}{\volt\per\ampere}$. Nous pouvons donc écrire simplement $\qty{10000}{\ohm}$ au lieu de $\qty{10000}{\volt\per\ampere}$ ! Notre résistance vaut donc $\qty{10000}{\ohm}$, ou en abrégé $\qty{10}{\kilo\ohm}$ :

$\qty{10000}{\volt\per\ampere} = \qty{10000}{\ohm}$

%Es stellt sich aber immer noch folgende Frage: Warum fließen in unserem Beispiel genau 1 mA, wenn die Spannung 10 V beträgt?

Nous avons appris : la valeur de la résistance peut être calculée à partir de la tension et du courant. Elle est le *rapport de la tension au courant*, ou autrement dit : en divisant la tension par le courant, on obtient la valeur de la résistance.

---

Cette relation peut être représentée par la formule suivante, appelée *loi d'Ohm* : 

$ R = \dfrac{U}{I} $

<person>
Le physicien allemand *Georg Simon Ohm* a découvert en 1826 la relation entre la tension électrique, le courant électrique et la résistance. En son honneur, la formule $ R = \frac{U}{I} $ est appelée loi d'Ohm.
</person>

[question:NB505]

Mais si l'on ne connaît que la résistance et la tension et que l'on veut calculer le courant correspondant, on peut utiliser la loi d'Ohm de la façon suivante : 

$ I = \dfrac{U}{R} $

Dans le cas où l'on ne connaît que la résistance et le courant et que l'on veut calculer la tension correspondante, il existe une autre variante de la formule : 

$ U = R\cdot I $

[question:NB504]

Il n'est pas indispensable de mémoriser ces formules. Elles figurent aussi dans le formulaire mis à disposition comme document d'aide lors de l'examen. Pour les calculs, on peut utiliser une calculatrice à l'examen.

[question:NB502]
[question:NB503]
[question:NB501]
