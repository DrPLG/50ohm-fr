Pour les signaux sinusoïdaux en courant alternatif, la puissance se calcule à partir des valeurs efficaces du courant et de la tension. On ne doit donc pas y substituer simplement la tension crête à crête $U_\text{SS}$ ou la tension de crête $\hat{U}$.

<margin>
[picture:834:a_wechselstrom_leistung:Valeurs efficaces pour le calcul de la puissance]
</margin>

Il en résulte pour le calcul de la puissance
$P_\text{alt} = U_\text{eff} \cdot I_\text{eff} = \dfrac{{U_\text{eff}}^2}{R} = I_\text{eff}^2 \cdot R$


Pour les signaux sinusoïdaux, on a cependant aussi :

$U_\text{eff} = \dfrac {\hat{U}} {\sqrt{2}} = \dfrac {U_\text{SS}} {2 \cdot \sqrt{2}}$ 
$I_\text{eff} = \dfrac {\hat{I}} {\sqrt{2}} = \dfrac {I_\text{SS}} {2 \cdot \sqrt{2}}$ 

Il en découle, pour les signaux sinusoïdaux, les relations suivantes, qui permettent de calculer aussi avec les valeurs de crête et les valeurs crête à crête :

$\begin{split} P_\text{alt} &=  U_\text{eff} \cdot I_\text{eff} \\ &= \frac{\hat{U}\cdot\hat{I}}{\sqrt{2}\cdot\sqrt{2}} = \frac{\hat{U} \cdot \hat{I}}{2} \\ &= \frac{U_\text{eff}^2}{R} = \left(\frac{\hat{U}}{\sqrt{2}}\right)^2 \cdot \frac{1}{R} = \frac{\hat{U}^2}{2 \cdot R} \\ &= I_\text{eff}^2 \cdot R = \left(\frac{\hat{I}}{\sqrt{2}}\right)^2 \cdot R = \frac{\hat{I}^2\cdot R}{2} \end{split}$

La question suivante se résout très facilement avec ces considérations ($I_\mathrm{max}$ n'est là qu'une autre désignation de $\hat{I}$) :

[question:AB301]

Dans le domaine du radioamateurisme, nous avons affaire à des tensions de fréquences (p. ex. kilo- ou gigahertz) et de formes d'onde (tension rectangulaire, tension sinusoïdale, tension continue) différentes. Celles-ci peuvent aussi être déformées et ne pas se présenter, p. ex., comme une tension sinusoïdale pure. Ces différentes tensions produisent dans un circuit des courants électriques différents. En principe, il faudrait alors divers appareils pour pouvoir mesurer cette étendue de courants électriques avec une précision de mesure raisonnable. 

C'est pourquoi, dans le domaine du radioamateurisme, on utilise souvent ce qu'on appelle un *thermoconvertisseur* (Thermoumformer).
On exploite ici le fait que le passage du courant échauffe le fil conducteur (cf. résistance des fils). Plus il circule de courant, plus le fil s'échauffe. L'échauffement est donc proportionnel à l'intensité du courant. Le thermoconvertisseur mesure cet échauffement et l'affiche comme intensité de courant. Il faut noter qu'avec cette méthode de mesure, nous obtenons la *valeur efficace* de l'intensité. L'avantage est alors que l'intensité peut se déterminer de manière quasi *indépendante* de la forme d'onde ou de la fréquence. Le thermoconvertisseur peut ainsi couvrir une grande étendue de signaux. 

[question:AI105]