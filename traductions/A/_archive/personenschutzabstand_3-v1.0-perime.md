% In Bearbeitung! Um was geht es denn hier???
% Das habe ich mir alles aus den Fingern gezogen!

Dans le recueil de formules, on trouve au point 6.2, Symboles, constantes et tableaux, également la formule de $Z_{F0}$, l'impédance d'onde de l'espace libre (vide).
$Z_{F0} = \sqrt{\dfrac{\mu_0}{\varepsilon_0}}$

$\mu_0$ la constante magnétique, $\varepsilon_0$ la constante électrique

L'**intensité de champ magnétique** évoquée dans la question se calcule à l'aide de la constante magnétique, de la densité de flux magnétique et de l'aimantation. La relation entre la constante électrique et l'**intensité de champ électrique** est nettement plus complexe.

Dans un milieu (par ex. l'air), l'impédance d'onde $Z_{F}$ dépend de $\mu$, la constante magnétique, et de $\varepsilon$, la constante électrique du milieu.

$Z_{F} = \sqrt{\dfrac{\mu}{\varepsilon}}$

Il existe une dépendance entre l'impédance d'onde, l'intensité de champ électrique et l'intensité de champ magnétique. Ainsi, l'intensité de champ électrique et magnétique dépend elle aussi de l'impédance d'onde du milieu.


[question:AK102]

% Wie errechnen Sie die Leistung am Einspeisepunkt der Antenne (Antenneneingangsleistung) bei bekannter Senderausgangsleistung?

La puissance au point d'alimentation de l'antenne résulte de la puissance de sortie de l'émetteur et de l'atténuation de la ligne d'alimentation. Toute atténuation peut être convertie en un facteur d'atténuation. Par exemple, pour une atténuation de $\qty{10}{\dB}$, le facteur vaut $\num{0,1}$.
Le calcul est simple : $P_{Ant} = D \cdot P_{Sender}$ (D représente le facteur d'atténuation)

[question:AK104]
% In Bearbeitung!
 Le § 8 de la BEMFV établit entre autres que la distance de sécurité liée au site doit se situer à l'intérieur de la zone contrôlable. Souvent, cette distance est fixée par les contraintes locales et ne peut pas être modifiée. Dans ces cas, la puissance d'émission maximale doit être adaptée.
 
Dans la puissance rayonnée intervient, outre la puissance d'émission, le gain d'antenne exprimé en $\unit{\dBi}$. Il est indiqué $\qty{6}{\dBd}$. Rapporté au radiateur isotrope, cela fait $\qty{6}{\dBd} + \qty{2,15}{\dB}$. Il en résulte un facteur de gain de $G_i = 4 \cdot 1,64 = 6,56$.

La puissance d'émission maximale peut maintenant être déterminée. Pour cela, il faut réarranger la formule de l'intensité de champ dans le champ lointain d'une antenne :
 $\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E \cdot d &= \sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}\\ E^2 \cdot d^2 &= \qty{30}{\ohm}\cdot P_A\cdot G_i\\ \dfrac{E^2 \cdot d^2}{\qty{30}{\ohm}\cdot G_i} &= P_A\\ P_A &= \dfrac{E^2 \cdot d^2}{\qty{30}{\ohm}\cdot G_i}\\ P_A &= \qty{\dfrac{28^2 \cdot 5^2}{30 \cdot 6,56}}{\watt}\\ P_A &\approx \qty{99,59}{\watt}\end{split}$
La puissance d'émission doit être limitée à env. $\qty{100}{\watt}$.
  
  Par simple sécurité, l'équation aux dimensions. Le résultat a pour unité le watt.
 $\begin{split} \unit{\watt} &= \dfrac{\left(\unit{\volt\per\meter}\right)^2 \cdot \unit{m\squared}}{\unit{\volt\per\ampere}}\\ \unit{\watt} &= \dfrac{\unit{\volt} \cdot \unit{\volt} \cdot \unit{m\squared} \cdot A}{\unit{\volt} \cdot \unit{m\squared}}\\ \unit{\watt} &= \unit{\volt} \cdot \unit{\ampere}\\ \unit{\watt} &= \unit{\watt}\end{split}$
 
 La formule de l'intensité de champ ne vaut que pour le champ lointain. On peut vérifier rapidement si c'est le cas pour les $\qty{5}{\meter}$ donnés.

$\begin{split}d &> \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{2,06}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,33}{\meter}\end{split}$
La distance de sécurité de $d=\qty{5}{\meter}$ est nettement dans le champ lointain.

[question:AK107]

Pour les trois questions suivantes, la démarche est plus ou moins la même.
Pour le calcul de l'intensité de champ électrique, on a besoin de la puissance au point d'alimentation de l'antenne, du facteur de gain et de la distance.

$P_A$, puissance au point d'alimentation : $\qty{250}{\watt}$ (pas de câble, alimentation directe)

$G_i$, facteur de gain : $\qty{12,15}{\dBi}$ ou $\qty{10}{\dBi}$ et $\qty{2,15}{\dBi}$, ce qui correspond aux facteurs $10 \cdot 1,64 = 16,4$

$d$, distance : $\qty{30}{\meter}$

La formule ne vaut que pour le champ lointain. On peut le vérifier avec $d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{250}{\watt}\cdot 16,4}}{\qty{30}{\meter}}\\ E &\approx \qty{11,7}{\volt\per\meter}\end{split}$

[question:AK113]

$P_A$, puissance au point d'alimentation : $\qty{10}{\watt}$ (pas de câble, alimentation directe)

$G_i$, facteur de gain : $\qty{2,15}{\dBi}$, ce qui correspond au facteur $\num{1,64}$ (dipôle comme antenne)

$d$, distance : $\qty{10}{\meter}$

La formule ne vaut que pour le champ lointain. On peut le vérifier avec $ d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{10}{\watt}\cdot 1,64}}{\qty{10}{\meter}}\\ E &\approx \qty{2,2}{\volt\per\meter}\end{split}$

[question:AK114]
% AK115: Eine Amateurfunkstelle sendet in FM mit einer äquivalenten Strahlungsleistung (ERP) von 100 W. Wie groß ist die Feldstärke im freien Raum in einer Entfernung von 100 m?

$P_A$, puissance au point d'alimentation : $\qty{100}{\watt}$ (puissance rayonnée en ERP)

$G_i$, facteur de gain : $\qty{2,15}{\dBi}$, ce qui correspond au facteur $\num{1,64}$ (puissance rayonnée en ERP, facteur pour l'EIRP)

$d$, distance : $\qty{100}{\meter}$

La formule ne vaut que pour le champ lointain. On peut le vérifier avec $ d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{100}{\watt}\cdot 1,64}}{\qty{100}{\meter}}\\ E &\approx \qty{0,7}{\volt\per\meter}\end{split}$

[question:AK115]