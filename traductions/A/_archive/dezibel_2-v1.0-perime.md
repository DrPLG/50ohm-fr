Dans la classe E, nous avons déjà fait connaissance avec le décibel comme outil pour décrire des rapports, et vu qu'une variation de puissance de $\qty{3}{\dB}$ correspond à un facteur de puissance de $\num{2}$. Nous trouvons dans le recueil de formules le tableau [ref:a_dezibel_leistungsfaktoren], qui contient d'autres correspondances importantes. 

<margin>
| c:dB | c:≈ Facteur de puissance |
| $-20$ | $\num{0,01}$ |
| $-10$ | $\num{0,1}$ |
| $-6$ | $\num{0,25}$ |
| $-3$ | $\num{0,5}$ |
| $-1$ | $\num{0,79}$ |
| $0$ | $\num{1}$ |
| $1,5$ | $\sqrt{2} = \num{1,41}$ |
| $2,15$ | $\num{1,64}$ |
| $3$ | $\num{2}$ |
| $5$ | $\sqrt{10} = \num{3,16}$ |
| $6$ | $\num{4}$ |
| $10$ | $\num{10}$ |
| $20$ | $\num{100}$ |
[table:a_dezibel_leistungsfaktoren:Facteurs de puissance importants en $\unit{\dB}$]
</margin>

Le recueil de formules donne, pour convertir un rapport de puissances en $\unit{\dB}$, la formule suivante, que nous avons aussi déjà rencontrée dans la classe E. Le rapport $g$ de deux puissances $P_1$ et $P_2$ en $\unit{\dB}$ est :

$g = 10\cdot \log_{10}\left(\frac{P_2}{P_1}\right)\unit{\dB}$

Si l'on veut déterminer un facteur de rapport à partir d'une valeur en $\unit{\dB}$, il faut transformer la formule : 

$\begin{align*} g &= 10 \cdot \log_{10}\left( x \right) \unit{\dB} & \quad\quad\quad &|: \qty{10}{\dB} \\ \frac{g}{\qty{10}{\dB}} &= \log_{10}\left( x \right) &~&| \quad 10^{x}\\ x &= 10^{\frac{g}{\qty{10}{\dB}}} &~&~\end{align*}$

Avec ces deux formules, nous pouvons donc convertir facilement entre indications en $\unit{\dB}$ et facteurs de rapport. Essaie maintenant de calculer les deux questions suivantes : 

---

[question:AA105]
[question:AA106]

<tip>
Dans la classe E, nous avons déjà rencontré l'astuce suivante : tout à fait sans calculatrice, on peut estimer les valeurs en décibels qui se terminent par « $0$ » : il suffit de masquer le dernier zéro, le chiffre restant donne alors le nombre de zéros du facteur de rapport. Exemple : $\qty{30}{\dB} \rightarrow 3 \rightarrow 3~\text{zéros} \rightarrow \text{facteur de rapport}~1000$ !

Dans l'autre sens aussi, le calcul est facile : un un suivi de $12$ zéros ($\num{1000000000000}$) en $\unit{\dB}$, c'est simplement le nombre de zéros, donc $12$, multiplié par $10$. Il en résulte un facteur d'amplification de $\qty{120}{\dB}$.

Mais même pour des valeurs en $\unit{\dB}$ qui ne se terminent pas par $0$, on peut déterminer le facteur correspondant par décomposition :

* On peut décomposer $\qty{9}{\dB}$ en $\qty{6}{\dB} + \qty{3}{\dB}$, ce qui correspond à une multiplication de $4\cdot 2 = 8$. 
* Quel facteur correspond à un rapport de puissances de $\qty{17}{\dB}$ ? $\qty{17}{\dB} = \qty{20}{\dB} - \qty{3}{\dB}$, donc facteur $100$ divisé par $2$ égale $50$.
</tip>

Le décibel ($\unit{\dB}$) décrit fondamentalement un rapport sans dimension, par exemple de puissances ou de tensions. C'est pourquoi le $\unit{\dB}$ est surtout utilisé pour indiquer des amplifications et des atténuations. Dans ces cas, aucune mention supplémentaire n'est nécessaire, puisque seul le rapport de deux grandeurs est indiqué. Les valeurs négatives en décibels caractérisent d'ailleurs des rapports inférieurs à $1$. Ainsi, $\qty{-3}{\dB}$ correspond à un rapport de $\frac{1}{2} = \num{0,5}$.

Mais on peut aussi utiliser des valeurs en décibels pour indiquer un niveau absolu. Une grandeur de référence fixe $P_0$ est toutefois nécessaire pour cela :

$p = 10\cdot \log_{10}\left(\frac{P}{P_0}\right)\unit{\dB}$

---

Cette grandeur de référence peut par exemple être une puissance de $\qty{1}{\milli\watt}$. Dans ce cas, la valeur en décibels reçoit un suffixe correspondant : si le niveau se rapporte à $\qty{1}{\milli\watt}$, on parle de $\unit{\dBm}$. Il est ainsi établi sans ambiguïté à quelle valeur absolue de puissance se rapporte le niveau en décibels.

Si l'on rencontre par exemple l'indication « l'émetteur a une puissance de sortie de $\qty{20}{\dBm}$ », cette valeur se convertit facilement en milliwatts. Un niveau de $\qty{20}{\dB}$ correspond à un facteur de puissance de $100$ (donc deux zéros). Ce facteur est multiplié par la grandeur de référence de $\qty{1}{\milli\watt}$ :

$ P = 100 \cdot \qty{1}{\milli\watt} = \qty{100}{\milli\watt}$

Le tableau [ref:a_bezugsgroessen] liste les principales grandeurs de référence et leurs abréviations en $\unit{\dB}$ respectives.

<margin>
| l: Abréviation          | X: Valeur de référence |
| $\unit{\dBm}$           | $\qty{1}{\milli\watt}$ | 
| $\unit{\dBW}$           | $\qty{1}{\watt}$       | 
| $\unit{\dBu}$           | $\qty{0,775}{\volt}$   | 
| $\unit{\dB\micro\volt}$ | $\qty{1}{\micro\volt}$ | 
[table:a_bezugsgroessen:Grandeurs de référence importantes du recueil de formules]
</margin>

Les questions suivantes peuvent se calculer à l'aide de la formule du recueil de formules et de sa transformation du début de cette leçon, si l'on utilise la bonne grandeur de référence. 

[question:AA109]
[question:AA110]
[question:AA107]
[question:AA108]

---

Pourquoi fait-on tout cela et indique-t-on des puissances absolues en $\unit{\dBm}$ et $\unit{\dBW}$ ? Comme déjà évoqué dans la classe E, l'utilisation du décibel sert avant tout à simplifier les calculs. Grâce à la représentation des amplifications et des atténuations en décibels, des chaînes de signal complètes peuvent s'estimer très simplement par addition et soustraction, sans devoir recourir à des multiplications et divisions laborieuses.

La figure [ref:e_signalkette] montre une telle chaîne de signal avec trois étages amplificateurs. Le signal d'entrée possède une puissance de $\qty{1}{\milli\watt}$, ce qui correspond à $\qty{0}{\dBm}$. Par les trois étages amplificateurs, le signal est amplifié au total jusqu'à $\qty{60}{\dBm}$ (soit $\num{1000000}\cdot \qty{1}{\milli\watt}$), ce qui correspond à une puissance de $\qty{1000}{\watt}$.

La figure [ref:e_signalkette_2] montre un autre exemple de chaîne de signal, dans laquelle un atténuateur avec une atténuation de $\qty{20}{\dB}$ est en plus inséré, ce qui correspond à une amplification de $\qty{-20}{\dB}$. Le signal d'entrée possède une puissance de $\qty{1}{\milli\watt}$, donc $\qty{0}{\dBm}$. Le premier étage amplificateur élève le signal à $\qty{10}{\dBm}$. Il est ensuite affaibli par l'atténuateur à $\qty{-10}{\dBm}$ et enfin ré-amplifié par le deuxième étage amplificateur à $\qty{0}{\dBm}$, ce qui correspond de nouveau à $\qty{1}{\milli\watt}$.

<margin>
[picture:877:e_signalkette:Chaîne de signal avec trois amplificateurs]
[picture:1053:e_signalkette_2:Chaîne de signal avec deux amplificateurs et un atténuateur]
</margin>

<indepth>
Pourquoi est-il licite de soustraire une atténuation de $\qty{3}{\dB}$ d'un niveau de $\qty{9}{\dBm}$ ? Ces deux valeurs ont pourtant des unités de mesure différentes ! L'unité bel ($\unit{\bel}$) ou décibel ($\unit{\dB}$) est une unité auxiliaire (aussi pseudo-unité).
En principe, la valeur numérique pourrait aussi s'écrire sans l'unité $\unit{\dB}$. Mais avec la mention $\unit{\dB}$, il devient clair qu'il s'agit d'un rapport logarithmique de deux grandeurs. Sans cette unité, il faudrait décrire verbalement quelle signification a la valeur numérique.
</indepth>
  
Nous avons de plus déjà rencontré dans la classe E les suffixes $\unit{\dBd}$ et $\unit{\dBi}$, utilisés pour indiquer les gains d'antenne. Dans ce cas, la valeur en décibels ne se rapporte pas à une puissance ou à une tension, mais à un radiateur de référence donné. Sont usuels le $\unit{\dBi}$, rapporté au radiateur isotrope sphérique, ainsi que le $\unit{\dBd}$, rapporté au dipôle demi-onde.

---

À côté des rapports de puissances, nous pouvons aussi utiliser le décibel pour indiquer des *rapports de tensions* et des *niveaux de tension*. Nous pouvons pour cela utiliser la formule $P = \frac{U^2}{R}$. Nous pouvons donc écrire :

$\begin{split}g &= 10 \cdot \log_{10}\left(\frac{P_1}{P_2}\right)\\ &= 10 \cdot \log_{10}\left(\frac{\frac{U_1^2}{\cancel{R}}}{\frac{U_2^2}{\cancel{R}}}\right)\\ &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right) \end{split}$

<tip>
*Calculer avec des logarithmes :*
Quelques règles de calcul simples permettent de résoudre les exercices en décibels sans calculatrice.

* Le logarithme d'un produit de deux nombres correspond à la somme des logarithmes : $\log_{10}(a\cdot b) = \log_{10}(a)+ \log_{10}(b)$
* Le logarithme d'une division de deux nombres correspond à la différence des logarithmes : $\log_{10}(a / b) = \log_{10}(a) - \log_{10}(b)$
* Le logarithme d'un nombre au carré : $\log_{10}(x^2)= 2 \cdot \log_{10}(x)$
* Le logarithme d'une racine : $\log_{10}(\sqrt{x})= \frac{1}{2} \cdot \log_{10}(x)$
</tip>

Mais le logarithme d'un nombre au carré est égal à deux fois le logarithme du nombre :

$\log_{10}(x^2)=2 \cdot \log_{10}(x)$

Il en découle :

$\begin{split} g &= 10 \cdot \log_{10}\left(\left(\frac{U_1}{U_2}\right)^2\right)\\ &= 10 \cdot 2 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \\ &= 20 \cdot \log_{10}\left(\frac{U_1}{U_2}\right) \end{split}$

---

C'est pourquoi nous calculons un rapport *$a$* de deux tensions $U_1$ et $U_2$ en multipliant le logarithme du rapport non pas par le facteur $10$, mais par le facteur $20$. Nous trouvons aussi cette formule dans le recueil de formules.

[question:AA111]

<attention>
Lors du calcul en décibels, toujours bien vérifier s'il s'agit de rapports de puissances ou de rapports de tensions !
</attention>

Pour déterminer des niveaux de tension, nous devons de nouveau fixer d'abord une tension de référence (cf. tableau [ref:a_bezugsgroessen]). Pour les signaux reçus, nous aimons mesurer les (très petites) tensions à l'entrée du récepteur en $\unit{\micro\volt}$. Le niveau de tension correspondant a alors l'unité $\unit{\dBuV}$. Exemple :

$\qty{10}{\micro\volt} \rightarrow 20 \cdot \log_{10}\left(\frac{\qty{10}{\micro\volt}}{\qty{1}{\micro\volt}}\right)=\qty{20}{\dBuV}$

---

Dans la question suivante, la valeur de référence est $\qty{1}{\micro\volt\per\meter}$. Essaie de résoudre l'exercice avec tes connaissances.

<attention>
Attention, il s'agit ici de $\unit{\dB(\micro\volt\per\meter)}$ et non de $\unit{(\dB\micro\volt)/\meter}$ ! 
</attention>

[question:AA112]

<tip>
Pour les tensions aussi, on peut calculer beaucoup de choses de tête à l'aide du tableau du recueil de formules :

| c:dB | c:≈ Rapport de tensions |
| $-20$ | $\num{0,1}$ |
| $-10$ | $\num{0,32}$ |
| $-6$ | $\num{0,5}$ |
| $-3$ | $\num{0,71}$ |
| $-1$ | $\num{0,89}$ |
| $0$ | $\num{1}$ |
| $1$ | $\num{1,12}$ |
| $3$ | $\num{1,14}$ |
| $6$ | $2$ |
| $10$ | $3,16$ |
| $20$ | $10$ |
[table:a_spannungsverhaeltnisse:Rapports de tensions importants en $\unit{\dB}$]

*Exemple :*

* À combien de $\unit{\dB}$ correspond un rapport de tensions de $4$ ? $4 = 2 \cdot 2 \rightarrow \qty{6}{\dB} + \qty{6}{\dB} = \qty{12}{\dB}$
</tip>