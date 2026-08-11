La fonction de base de la diode est déjà connue depuis la formation à la classe N : elle ne laisse passer le courant que dans un seul sens, à savoir lorsque la tension appliquée à l'anode ($U_a$) est supérieure à la tension à la cathode ($U_k$), cf. figure [ref:e_diode_u_i].

<margin>
[picture:859:e_diode_u_i:Tensions et courant sur une diode avec résistance série]
</margin>

Mathématiquement, nous pouvons écrire cette condition ainsi :

$U_d = U_a - U_k > 0$

Toutefois, si $U_d$ n'est que très légèrement supérieure à 0, aucun courant notable ne circule encore. Cela tient à la *caractéristique exponentielle* d'une diode. Le courant de diode vaut en effet :

$I_d = I_S \left(e^{\frac{U_d}{U_T}}-1\right)$

$e$ est le nombre d'Euler ($e\approx 2,718$), $U_T$ une constante qui vaut environ $\qty{26}{\milli\volt}$ à température ambiante.

$I_S$ est ici le *courant de saturation inverse*, c'est-à-dire le très faible courant qui circule dans la diode sous des tensions négatives. La valeur de $I_S$ dépend, outre quelques paramètres de la diode comme sa surface, surtout du matériau semi-conducteur utilisé. Pour des matériaux comme le germanium (Ge), à faible *largeur de bande interdite* (nous y reviendrons plus en détail dans la formation à la classe A), $I_S$ est plus grand ; pour des matériaux à plus grande largeur de bande interdite, $I_S$ est plus petit.

<margin>
[picture:861:e_diode_kennlinie_iu:Caractéristique d'une diode]
</margin>

[question:EC501]

Si l'on considère la caractéristique d'une diode sur la figure [ref:e_diode_kennlinie_iu], le courant de diode croît fortement pour des $U_d$ positives à partir d'une certaine tension. Cette tension est aussi appelée *tension de seuil* $U_{th}$, mais elle n'est que l'expression des différents $I_S$ : plus $I_S$ est petit, plus la tension de seuil est élevée.

Comme repères pour la tension de seuil des diodes pn, nous pouvons indiquer environ $\qtyrange{0,2}{0,3}{\volt}$ pour le Ge et environ $\qtyrange{0,6}{0,7}{\volt}$ pour le Si.

Les *diodes électroluminescentes* (LED) sont également des diodes pn, dont le matériau semi-conducteur est conçu de manière à émettre de la lumière lorsque la diode est polarisée en sens direct. Cela n'est possible qu'avec certains matériaux — pas avec le Si ni le Ge. La couleur de la lumière est déterminée par la largeur de bande interdite. Plus la largeur de bande interdite est grande, plus la lumière est de courte longueur d'onde, plus le courant de saturation inverse est faible, et donc plus la tension de seuil est élevée. C'est pourquoi les LED rouges ont une tension de seuil d'environ $\qty{1,7}{\volt}$ et les LED vertes d'environ $\qty{2,5}{\volt}$. Les différentes caractéristiques sont représentées sur la figure [ref:e_diode_kennlinien].

[question:EC513]
[question:EC510]
[question:EC509]
[question:EC511]
[question:EC512]

---

<margin>
[picture:858:e_diode_kennlinien:Caractéristiques de différentes diodes]
</margin>


[question:EC503]
[question:EC506]
[question:EC507]
[question:EC508]

Comme les LED fonctionnent en sens direct, il est important de placer une résistance $R_V$ entre la source de tension $U$ et la LED. $R_V$ fixe le courant $I$ souhaité. Il faut pour cela tenir compte de la tension de seuil $U_{th}$ de la LED :

$ I=\frac{U-U_{th}}{R_V}$

[question:EC514]
[question:EC515]
[question:EC516]

---

Dans notre modèle simple, seul un faible courant inverse circule pour des $U_d$ négatives. Cela n'est toutefois pas vrai pour des tensions très négatives. À un certain point, le champ électrique aux bornes de la zone de déplétion entre le n et le p devient trop élevé et la diode « claque » : le courant en sens inverse croît extrêmement fortement, comme le montre la figure [ref:n_diode_kennlinie_uz].

Ce *claquage inverse* peut avoir différentes causes physiques que nous ne pouvons pas traiter ici en détail. La tension à laquelle ce claquage se produit est communément appelée *tension Zener* $U_z$, même si l'effet Zener (un effet tunnel quantique) n'est qu'un mécanisme de claquage possible. Les *diodes Zener* sont utilisées pour la stabilisation de tension. Il est alors important de limiter le courant de claquage par une résistance série.

<margin>
[picture:862:n_diode_kennlinie_uz:Caractéristique d'une diode Zener]
</margin>

---

Le symbole d'une diode Zener (figure [ref:e_zener_symbol]) est celui d'une diode ordinaire, dont le trait de la cathode reçoit un prolongement supplémentaire à $\qty{90}{\degree}$. Cela doit rappeler le « coude » de la caractéristique au claquage.

<margin>
[picture:860:e_zener_symbol:Symbole d'une diode Zener]
</margin>



[question:EC517]
[question:EC520]
[question:EC521]
[question:EC522]

Les diodes traitées jusqu'ici étaient toutes des *diodes pn*, dont la propriété de diode provient d'une jonction de semi-conducteurs. La *diode Schottky* est une diode dont les propriétés proviennent d'une jonction métal-semi-conducteur. Sa tension de seuil est environ deux fois plus faible que celle d'une diode pn du même matériau, voire plus petite, selon la conception précise de la jonction métal-semi-conducteur. Les diodes Schottky sont employées lorsqu'une faible tension de seuil est souhaitée, ou bien comme diodes de commutation très rapides.

[question:EC504]
[question:EC505]

<margin>
Les diodes métal-semi-conducteur sont les plus anciens composants redresseurs à base de semi-conducteur. Ferdinand Braun découvrit leur effet redresseur dès 1874, sans toutefois pouvoir expliquer son observation.
</margin>

Résumons :

Les diodes ne laissent passer le courant que dans un seul sens. Elles conviennent donc au redressement du courant alternatif.

Sous de fortes tensions inverses toutefois ($U_d < U_z$), le courant en sens inverse croît fortement. Ce point de fonctionnement peut très bien être exploité pour la stabilisation de tension (*diode Zener*).

Par ailleurs, en sens inverse, elles peuvent aussi être utilisées comme capacités commandées en tension ; nous ne traiterons cependant cela que dans la formation à la classe A.

[question:EC502]
[question:EC518]
[question:EC519]
