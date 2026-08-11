Dans la classe E, nous nous sommes aussi déjà penchés sur la bobine. En courant continu, la bobine a, en régime établi, une très petite résistance. La bobine agit alors comme un morceau de fil. En courant alternatif cependant, la bobine présente, de manière semblable à un condensateur, une résistance en courant alternatif $X_{\textrm{L}}$, c'est-à-dire que, bien que le fil de la bobine ne possède qu'une très petite résistance ohmique (résistance du conducteur), il circule un courant qui devient toutefois plus petit à mesure que la fréquence de la tension alternative augmente :

$|X_{L}| = \omega \cdot L = 2\cdot\pi\cdot f \cdot L$

On reconnaît à la formule que la résistance en courant alternatif augmente quand la fréquence croît et diminue quand la fréquence décroît. Contrairement au condensateur, la résistance en courant alternatif d'une bobine est positive. 

<indepth>
Pourquoi la réactance inductive est-elle positive ? L'arrière-plan se trouve de nouveau dans le calcul complexe des courants alternatifs, qui n'est pas strictement nécessaire pour l'examen radioamateur.

Pour les lectrices et lecteurs ayant des connaissances en nombres complexes, notons cependant que la représentation correcte de la réactance inductive s'écrit en fait

$X_L = j\omega L$

où $j$ représente de nouveau l'unité imaginaire $\sqrt{-1}$.

Il en ressort que la réactance inductive est non seulement positive, mais aussi complexe. Le signe positif décrit la relation de phase entre courant et tension aux bornes de la bobine, que nous examinerons encore plus précisément dans ce chapitre.
</indepth>

[question:AC202]

[question:AC203]

---

Avec un analyseur de réseau vectoriel (VNA), on peut représenter la variation de la réactance inductive $X_L$ en fonction de la fréquence (cf. figure [ref:a_XL_Verlauf]). 

<margin>
[photo:265:a_XL_Verlauf:Variation de la réactance inductive $X_L$ d'une bobine de $\qty{500}{\kilo\hertz}$ à $\qty{10}{\mega\hertz}$]
</margin>

Essaie maintenant de répondre à la question suivante à l'aide de la formule ci-dessus. Fais particulièrement attention aux unités et aux puissances de dix pour obtenir les bons résultats.

[question:AC204]

---

De manière semblable au condensateur, un déphasage entre tension et courant apparaît aussi dans la bobine. Il est de $\qty{+90}{\degree}$, le courant étant en retard sur la tension, comme le représente la figure [ref:a_Blindleistung_Spule]. La ligne rouge de la figure [ref:a_XL_Verlauf] montre la phase de la réactance inductive $X_L$ à environ $\qty{+90}{\degree}$.

<tip>
Moyen mnémotechnique : dans une inductance, le courant est en retard — dans un L, I traîne après U !
</tip>

[question:AC201]

Il en résulte une courbe de puissance qui oscille symétriquement autour de la ligne du zéro. La valeur moyenne de cette puissance est nulle, c'est-à-dire que — exactement comme pour le condensateur — aucune puissance active n'est absorbée. Au lieu de cela, de l'énergie est périodiquement stockée dans le champ magnétique de la bobine puis restituée à la source.

C'est pourquoi on parle, pour une bobine idéale sans pertes, de puissance réactive et de réactance.

<margin>
[picture:944:a_Blindleistung_Spule:Le produit $U \cdot I$ donne la courbe de puissance verte]
</margin>

Si une bobine chauffe dans des applications haute fréquence, c'est qu'elle possède des pertes qui provoquent cet échauffement. Les pertes proviennent de la résistance ohmique du fil, et s'y ajoute encore l'effet de peau, qui réduit en apparence la section du fil. Ici aussi, comme pour le condensateur, le facteur de qualité $Q$ ou le facteur de pertes $\tan\delta$ sont utilisés pour décrire les pertes.

[question:AC209]

---

Nous avons maintenant fait connaissance avec la réactance capacitive $X_C$ du condensateur et la réactance inductive $X_L$ de la bobine. Ces deux grandeurs dépendent de la fréquence et forment, avec la résistance ohmique $R$, ce qu'on appelle l'*impédance* $Z$ d'un composant.

Les réactances $X_L$ et $X_C$ agissent en sens opposés et peuvent s'annuler mutuellement, partiellement ou complètement. Pour combiner les réactances avec la résistance ohmique, une simple addition algébrique n'est cependant pas possible : une addition géométrique est nécessaire. Elle s'effectue à l'aide du théorème de Pythagore (cf. figure [ref:a_impedanzdreieck]).

Le résultat est l'impédance $Z$, qui décrit la résistance complexe totale d'un composant. Le module de l'impédance $|Z|$ correspond à ce qu'on appelle l'impédance apparente :

$Z = \sqrt{R^2 + (X_L - X_C)^2}$ 

ou, de manière simplifiée (cf. recueil de formules — mot-clé : Scheinwiderstand, impédance apparente) :

$Z = \sqrt{R^2 + X^2}$ 

En technique des hautes fréquences, l'impédance joue un rôle central, car elle détermine le comportement des composants dans les circuits et est en particulier décisive pour l'adaptation des lignes, des antennes et des amplificateurs. Elle s'indique en ohms ($\unit{\ohm}$) et décrit la résistance totale d'un composant en fonctionnement en courant alternatif. Dans un montage en série d'une réactance et d'une résistance active, il en résulte une impédance apparente $Z$ qui n'apparaît qu'en fonctionnement sous tension alternative et ne peut pas être mesurée avec un ohmmètre. 

<margin>
[picture:1067:a_impedanzdreieck:Impédance $Z$ comme addition géométrique de $R$ et $X$]
</margin>

<indepth>
L'impédance $Z$ est une grandeur complexe qui prend en compte aussi bien la résistance ohmique $R$ que les réactances $X_L$ et $X_C$ ($Z = R + j\cdot X$).
</indepth>

[question:AA101]

<tip>
Une résistance active de $\qty{100}{\ohm}$ et une réactance de $\qty{100}{\ohm}$ en montage série donnent une impédance apparente (impédance) de $\qty{141}{\ohm}$.
Le résultat s'obtient par addition géométrique des deux résistances via un triangle rectangle selon le théorème de Pythagore $a^2 + b^2 = c^2$.
Pour les résistances, cela signifie : $R^2 + X_L^2 = Z^2$
$Z = \sqrt{(\qty{100}{\ohm})^2 + (\qty{100}{\ohm})^2} = \qty{141}{\ohm}$
</tip>


---

Nous avons également déjà fait connaissance avec l'inductance d'une bobine dans la classe E. Fondamentalement, l'inductance augmente quand le nombre de spires est accru, quand la longueur de la bobine est raccourcie, quand la section de la bobine est agrandie et quand un matériau magnétiquement plus perméable est utilisé comme noyau de bobine. Pour augmenter l'inductance sans accroître drastiquement le nombre de spires, l'enroulement est bobiné sur un tore de ferrite. Des selfs de choc à haute inductance sont employées pour réduire les courants haute fréquence.

<indepth>
[photo:270:a_Pulvereisenringkern:Exemple de tore en poudre de fer]
[photo:271:a_Ferritringkern:Exemple de noyau de ferrite]
</indepth>

[question:AC211]

Pour les bobines toriques, afin de faciliter le calcul de l'inductance, on indique ce qu'on appelle la valeur $A_\text{L}$ du matériau du noyau.
Le calcul de l'inductance s'écrit alors :
$L = N^2 \cdot A_\text{L}$ (voir recueil de formules — mot-clé : inductance d'une bobine torique). Essaie maintenant de répondre ainsi aux questions suivantes. 

<attention>
La valeur $A_\text{L}$ est exprimée en nanohenrys par spire au carré.
</attention>


[question:AC205]
[question:AC206]
[question:AC207]
[question:AC208]

<indepth>
Si un matériau magnétiquement perméable se trouve à l'intérieur de la bobine (p. ex. fer, ferrite), le champ magnétique est alors renforcé. La densité de flux magnétique $B$ alors effective peut se calculer avec la formule (voir recueil de formules — mot-clé : densité de flux magnétique)
$B = \mu_0 \cdot \mu_r \cdot H$
où $\mu_0$ correspond à la constante magnétique $\qty{1,2566e-6}{\volt\second\per\ampere\meter}$ et $\mu_r$ représente la perméabilité relative du matériau du noyau dans la bobine. Pour l'air, on insère le facteur $1$ (voir recueil de formules — mots-clés : constante magnétique ; perméabilité relative).
</indepth>

Pour blinder un champ magnétique, il faut un matériau bon conducteur magnétique, par exemple du fer-blanc. La figure [ref:a_abschirmbecher] montre un exemple de bobines avec pot de blindage. Les pots de blindage métalliques contiennent des bobines avec un noyau de ferrite réglable, que l'on visse ou dévisse par l'ouverture du dessus avec un tournevis. L'inductance de la bobine change ainsi.

[question:AC210]

<margin>
[photo:333:a_abschirmbecher:Exemple de bobines avec pot de blindage pour le blindage de champs magnétiques]
</margin>
