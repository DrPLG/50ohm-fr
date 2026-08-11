Dans la classe N, nous avons déjà fait connaissance avec le radiateur isotrope (cf. figure [ref:e_Kugelstrahler]). Le radiateur isotrope n'est pas une antenne réelle, c'est un modèle physique d'un radiateur qui rayonne l'énergie uniformément dans toutes les directions de l'espace. 

La puissance isotrope rayonnée équivalente (EIRP) d'une antenne réelle se rapporte au radiateur isotrope. En d'autres termes, la puissance rayonnée d'une antenne réelle est comparée à la puissance rayonnée du radiateur isotrope. Pour la puissance rayonnée, seule est pertinente l'énergie qui arrive effectivement à l'antenne. En raison de l'atténuation de câble, etc., la puissance de l'émetteur ne peut pas, dans le monde réel, être intégralement transmise à l'antenne. Cette puissance perdue ne doit pas entrer dans le calcul de la puissance rayonnée. Le gain d'antenne dans la direction privilégiée fait naturellement partie du calcul. En formules, cela donne :

$P_\text{EIRP} = (P_\text{Sender} - P_\text{Verluste}) \cdot G_\text{Antenne}$

où $G$ représente ici le gain d'antenne. L'EIRP est donc le produit de la puissance fournie directement à l'antenne par son gain dans une direction, rapporté au radiateur isotrope.

<margin>
[picture:751:e_Kugelstrahler:Radiateur isotrope au centre d'une sphère, produisant la même puissance rayonnée en tous les points de la surface de la sphère]
</margin>

<tip>
Avant l'examen, il convient de bien se familiariser avec sa calculatrice. Les calculs et les formules des différentes questions devraient être exercés régulièrement, afin de maîtriser avec assurance l'appareil et les étapes de calcul le jour de l'examen.
</tip>

[question:EG501]

Dans la question suivante, il faut impérativement faire attention aux signes des opérations. Les pertes sont *soustraites* de la puissance d'émission, puis le résultat est *multiplié* par le facteur de gain ($G_{Antenne}$). Comme c'est l'EIRP qui doit être calculée, la référence doit être le radiateur isotrope.

[question:EG502]

---

Dans le chapitre sur le décibel, nous avons appris qu'il est judicieux de calculer avec des valeurs en dB, car de nombreux calculs s'en trouvent nettement simplifiés. Les gains et les atténuations en décibels s'additionnent, respectivement se soustraient, tout simplement. La figure [ref:e_verstaerkung_daempfung] montre une installation radio avec plusieurs éléments amplificateurs et atténuateurs. Le gain total de cette installation s'obtient par addition des différentes contributions : $\qty{-2}{\dB} + \qty{6}{\dB} - \qty{3}{\dB} + \qty{2}{\dB} = \qty{3}{\dB}$, ce qui correspond à un facteur de puissance de $\num{2}$.

<margin>
[picture:439:e_verstaerkung_daempfung:Gains et atténuations dans une installation radio]
</margin>

---

Les questions suivantes exigent le calcul de l'EIRP. Pour cela, on peut soit utiliser directement une formule, soit — avec un peu d'entraînement — résoudre les exercices entièrement de tête. Dans ce qui suit, nous voulons donc le plus souvent présenter les deux méthodes.

La formule de calcul de l'EIRP découle du recueil de formules et s'énonce :

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

<indepth>
On obtient la formule de $P_\text{EIRP}$ en réarrangeant en conséquence la formule du gain du recueil de formules :
  
$g = 10 \cdot \log_{10}\left(\frac{P_2}{P_1}\right) \unit{\dB}$
  
Comme il faut en outre tenir compte d'une atténuation $a$, celle-ci est soustraite du gain d'antenne. Pour $P_1$, nous insérons la puissance de l'émetteur $P_\text{Sender}$, puisqu'elle représente la puissance d'entrée, et pour $P_2$ en conséquence $P_\text{EIRP}$, puisqu'il s'agit de la puissance de sortie résultante.

$g-a = 10 \cdot \log_{10}\left(\frac{P_\text{EIRP}}{P_\text{Sender}}\right) \unit{\dB} \quad\quad\quad | : \qty{10}{\dB}$
  
Nous divisons les deux membres par $\qty{10}{\dB}$ :
  
$\frac{g-a}{\qty{10}{\dB}} = \log_{10}\left(\frac{P_\text{EIRP}}{P_\text{Sender}}\right) \quad\quad\quad | 10^x$
  
Nous appliquons ensuite $10^x$ aux deux membres pour éliminer le logarithme :
  
$10^{\frac{g-a}{\qty{10}{\dB}}} = \frac{P_\text{EIRP}}{P_\text{Sender}} \quad\quad\quad | \cdot P_\text{Sender}$
  
Par multiplication par $P_\text{Sender}$, on obtient la formule recherchée :
  
$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}$
</indepth>

Ici, $g_i$ est le gain d'antenne rapporté au radiateur isotrope, tandis que $a$ décrit l'atténuation due aux câbles et aux appareils d'adaptation.

[question:EG503]

La première méthode de calcul utilise la formule évoquée ci-dessus. Comme il n'y a pas de pertes de puissance, l'atténuation est $a=0$ et la formule se simplifie en : 

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 10^{\frac{\qty{26}{\dBi}}{\qty{10}{\dB}}}= \qty{250}{\milli\watt} \cdot 398 \approx \qty{100}{\watt}$

---

La deuxième méthode de calcul possible utilise le fait qu'on peut « décomposer » les valeurs en dB. Dans la question, le gain d'antenne est $g = \qty{26}{\dBi}$. Dans le recueil de formules, le tableau [ref:e_dezibel_leistungsfaktoren] donne un aperçu des facteurs de puissance pour les valeurs importantes en dB. Pour $\qty{26}{\dB}$, il n'y a pas d'entrée directe. Mais comme les niveaux en décibels peuvent s'additionner, on peut décomposer la valeur judicieusement :

$\qty{26}{\dBi} = \qty{20}{\dBi} + \qty{6}{\dB}$

<margin>
| c:dB | c:≈ facteur de puissance |
| $\num{0}$ | $\num{1}$ |
| $\num{1,5}$ | $\sqrt{2} = 1,41$ |
| $\num{2,15}$ | $\num{1,64}$ |
| $\num{3}$ | $\num{2}$ |
| $\num{5}$ | $\sqrt{10} = 3,16$ |
| $\num{6}$ | $\num{4}$ |
| $\num{10}$ | $\num{10}$ |
| $\num{20}$ | $\num{100}$ |
[table:e_dezibel_leistungsfaktoren:Facteurs de puissance importants en dB]
</margin>

Pour $\qty{20}{\dB}$, le tableau indique un facteur de puissance de $\num{100}$, pour $\qty{6}{\dB}$ un facteur de $\num{4}$. La puissance isotrope rayonnée équivalente se calcule ainsi très simplement :

$P_\text{EIRP} = \qty{250}{\milli\watt} \cdot 100 \cdot 4 = \qty{100}{\watt}$

La bonne réponse est donc $\qty{100}{\watt}$ EIRP.

Pour la question suivante, nous pouvons procéder exactement comme pour la question précédente. 

[question:EG504]

---

Pour beaucoup de radioamateurs, il est difficile de respecter la distance de sécurité nécessaire avec une puissance d'émission de par exemple $\qty{100}{\watt}$. Le trafic QRP est dans ces cas une solution. Si l'on reste, avec la puissance rayonnée, sous la limite de $\qty{10}{\watt}$ EIRP, la déclaration d'une installation radioamateur fixe selon le § 9 BEMFV peut être omise. Même avec un appareil non QRP, on peut réduire la puissance de sortie à une valeur déterminée, comme représenté sur la figure [ref:e_ausgangsleistung_ic].

<margin>
[photo:229:e_ausgangsleistung_ic:Sur beaucoup d'émetteurs-récepteurs, la puissance de sortie se règle en continu ou, comme ici sur l'IC-705, par petits pas.]
</margin>

[question:EG511]

L'antenne verticale indiquée dans cette question a un gain de $g=\qty{5,15}{\dBi}$, les pertes de câble sont négligées, c'est-à-dire $a = 0$. Si l'antenne n'avait pas de gain ($\qty{0}{\dBi}$), il suffirait de limiter la puissance d'émission à $\qty{10}{\watt}$ au maximum. La puissance rayonnée ne serait alors que de $\qty{10}{\watt}$ EIRP. Mais comme il y a un gain d'antenne de $\qty{5,15}{\dBi}$, la puissance d'émission doit être abaissée en conséquence. La puissance d'émission doit être inférieure d'au moins $\qty{5,15}{\dB}$ à $\qty{10}{\watt}$.

Ici aussi, il y a de nouveau deux méthodes de calcul possibles. Commençons par la méthode utilisant la formule connue. Dans cet exercice, ce n'est toutefois pas la puissance rayonnée $P_\text{EIRP}$ qui est recherchée, mais la puissance d'émission $P_\text{Sender}$. Nous devons donc réarranger la formule en conséquence :

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_i-a}{\qty{10}{\dB}}} \quad\quad\quad | : 10^{\frac{g_i-a}{\qty{10}{\dB}}}$

On obtient ainsi :

$ P_\text{Sender} = \frac{P_\text{EIRP}}{10^{\frac{g_i-a}{\qty{10}{\dB}}}} $

Nous insérons les valeurs :

$ P_\text{Sender} = \frac{\qty{10}{\watt}}{10^{\frac{\qty{5,15}{\dBi}}{\qty{10}{\dB}}}} = \frac{\qty{10}{\watt}}{3,27} \approx \qty{3,05}{\watt} $

Le calcul à la calculatrice donne $\qty{3,05}{\watt}$. Avec une limitation à $\qty{3}{\watt}$, on respecte la valeur limite de moins de $\qty{10}{\watt}$ EIRP.

La deuxième méthode de calcul passe de nouveau par la décomposition des valeurs en dB. En regardant la valeur $g=\qty{5,15}{\dBi}$, on reconnaît qu'on peut la décomposer en 

$\qty{5,15}{\dBi} = \qty{3}{\dBi} + \qty{2,15}{\dB}$

Dans le tableau [ref:e_dezibel_leistungsfaktoren], on trouve le facteur $\num{1,64}$ pour $\qty{2,15}{\dB}$. On obtient ainsi pour la puissance d'émission maximale :

$P_\text{Sender} = \frac{\qty{10}{\watt}}{2\cdot 1,64} = \frac{\qty{10}{\watt}}{3,28} \approx \qty{3}{\watt}$

Comme on pouvait s'y attendre, nous arrivons ici au même résultat. Avec $\qty{3}{\watt}$, on est du côté sûr.

La question suivante pourrait de nouveau se résoudre avec le recueil de formules, en insérant $a=\qty{1}{\dB}$, mais elle se résout très simplement de tête. 

[question:EG505]

Comme décrit tout au début de la section, pour la puissance rayonnée EIRP, on prend en compte le gain d'antenne ($\qty{11}{\dBi}$) et la puissance qui arrive effectivement à l'antenne. La puissance d'émission est atténuée de $\qty{1}{\dB}$ par le câble ; l'ensemble du système d'antenne a réellement un gain de $\qty{10}{\dBi}$. Dans notre tableau [ref:e_dezibel_leistungsfaktoren] du recueil de formules, le facteur $\num{10}$ est indiqué pour $\qty{10}{\dB}$. La puissance d'émission de $\qty{100}{\watt}$ devient une puissance rayonnée de $\qty{1000}{\watt}$.

Pour la question suivante, il faut faire attention au fait que c'est une antenne dipôle qui est utilisée. Elle aussi peut se calculer très simplement de tête.

[question:EG506]

Le gain d'une antenne dipôle par rapport au radiateur sphérique est de $\qty{2,15}{\dB}$. Cela correspond au facteur $\num{1,64}$. Cela figure aussi dans le recueil de formules :

$P_\text{EIRP} = P_\text{ERP} + \qty{2,15}{\dB}$

respectivement, sous forme de facteur :

$P_\text{EIRP} = P_\text{ERP} \cdot 1,64$

où $P_\text{ERP}$ représente la puissance rayonnée rapportée au dipôle. 

Le gain du dipôle est de $\qty{2,15}{\dBi}$, ce qui correspond ici exactement à l'atténuation de câble de la question. Les deux se compensent donc. L'antenne dipôle rayonne $\qty{75}{\watt}$ EIRP.

Dans la question suivante, l'antenne est aussi de nouveau un dipôle. 

[question:EG507]

On cherche la puissance isotrope rayonnée équivalente $P_\text{EIRP}$. Il faut d'abord tenir compte de l'atténuation de câble. Une atténuation de $\qty{10}{\dB}$ correspond à un rapport de puissance de $\num{0,1}$. Avec ce facteur d'atténuation ainsi que le facteur de gain d'antenne du dipôle de $\num{1,64}$, on peut ensuite calculer la puissance rayonnée.

$P_\text{EIRP} = \qty{100}{\watt} \cdot 0,1 \cdot 1,64 = \qty{16,4}{\watt}$


Pour la question suivante, le recueil de formules contient aussi directement une formule applicable. Comme nous avons une antenne directive dont le gain est indiqué par rapport au dipôle (ERP), il faut encore ajouter $\qty{2,15}{\dB}$ pour le calcul de $P_\text{EIRP}$ :

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}}$

[question:EG508]

---

En insérant les valeurs dans la formule, on peut résoudre rapidement la question. Mais ici aussi, cela se fait de tête. Calculons le gain total du système et décomposons-le de nouveau en conséquence :

$\qty{-2}{\dB} + \qty{5}{\dB} + \qty{2,15}{\dB} = \qty{3}{\dB} + \qty{2,15}{\dB}$ 

Nous pouvons maintenant lire de nouveau les facteurs dans le tableau :

$P_\text{EIRP} = \qty{5}{\watt} \cdot 2 \cdot 1,64 = \qty{16,4}{\watt}$

La question suivante peut aussi se résoudre exactement de la même manière. Il faut seulement faire attention au fait que le gain est donné par rapport au dipôle. 

[question:EG509]

Nous calculons de nouveau le gain total et décomposons :

$\qty{-1}{\dB} + \qty{11}{\dB} + \qty{2,15}{\dB} = \qty{10}{\dB} + \qty{2,15}{\dB}$ 

Nous pouvons maintenant lire de nouveau les facteurs dans le tableau :

$P_\text{EIRP} = \qty{0,6}{\watt} \cdot 10 \cdot 1,64 = \qty{9,8}{\watt}$

Dans la question suivante, on indique une antenne avec un gain de $\qty{0}{\dB}$ par rapport au dipôle. Cela ne signifie rien d'autre que cette antenne est un dipôle. 

[question:EG510]

Ici encore, on peut utiliser la formule du recueil de formules :

$P_\text{EIRP} = P_\text{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{8,5}{\watt} \cdot 10^{\frac{\qty{0}{\dB}-\qty{1,5}{\dB}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{9,9}{\watt}$

De tête, on peut aussi l'estimer : si l'on calcule de nouveau le gain total du système, il n'est que de $\qty{0,65}{\dB}$, donc même pas $\qty{1}{\dB}$. Selon notre tableau [ref:e_dezibel_leistungsfaktoren], $\qty{1}{\dB}$ correspond à un facteur de $\num{1,26}$. La valeur cherchée doit donc se situer entre $\qty{8,5}{\watt}$ et $\qty{10,71}{\watt}$. Seuls les $\qty{9,9}{\watt}$ entrent donc en ligne de compte.
