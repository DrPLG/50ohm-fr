Lors de la déclaration d'une installation radioamateur fixe, les distances de protection des personnes nécessaires peuvent être déterminées selon différents procédés. Outre le calcul en champ lointain décrit ci-dessus, les mesures et les simulations sont également admises. Les valeurs limites usuelles pour ces procédés, nous les avons déjà rencontrées dans la classe E.

Comme des mesures et des simulations se prêtent mal à un examen écrit, les questions d'examen qui suivent se limitent à des calculs avec la formule approchée. Dans tous les exercices, la condition nécessaire $d > \frac{\lambda}{2\pi}$ est remplie. La vérification de cette condition a déjà été traitée dans les questions de la classe E. Essaie maintenant de résoudre les exercices suivants à l'aide de la formule approchée du chapitre précédent.

---

[question:AK106]

Pour le calcul, on a besoin de la puissance d'émission ($P_\mathrm{S}$), du facteur de gain de l'antenne rapporté au radiateur isotrope ($G_\mathrm{i} = 1,64$) et de la valeur limite de l'intensité de champ $(E = \qty{28}{\volt\per\meter})$ dans le champ lointain d'une antenne. La longueur d'onde ($\qty{10}{\meter}$) n'est indiquée que pour déterminer le début du champ lointain.

$\begin{split} d &=\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{A} \cdot G_\mathrm{i}}}{E}\\ d &=\dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{100}{\watt} \cdot 1,64}}{\qty{28}{\volt\per\meter}}\\ d &\approx \qty{2,50}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

$\begin{split}d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{10}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{1,59}{\meter}\end{split}$

La distance de sécurité de $\qty{2,50}{\meter}$ se situe nettement dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK108]

Cette question ressemble à la précédente. Ici, il faut en plus tenir compte de l'atténuation du câble.

Il est judicieux de calculer d'abord l'EIRP.

$P_\mathrm{EIRP} = P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
Pour une antenne directive, la valeur de $g_\mathrm{d}$ doit être indiquée. Un simple dipôle n'a de gain que par rapport à un radiateur isotrope. Ici, $g_\mathrm{d} = \qty{0}{\dBd}$.
$\begin{split}P_\mathrm{EIRP} &= \qty{300}{\watt}\cdot {10^\dfrac{\qty{0}{\dBd} −  \qty{0,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{300}{\watt}\cdot {10^\dfrac{\qty{1,65}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{300}{\watt}\cdot {10^{0,165}}\\ P_\mathrm{EIRP} &\approx \qty{438,65}{\watt}\end{split}$

La distance de sécurité peut maintenant être calculée.

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,65}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{4,10}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

$\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{20}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{3,18}{\meter}\end{split}$

La distance de sécurité de $\qty{4,10}{\meter}$ se situe ici aussi dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK109]

On peut procéder exactement comme pour la question précédente.
$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{700}{\watt}\cdot {10^\dfrac{\qty{0}{\dBd} −  \qty{0,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{700}{\watt}\cdot {10^\dfrac{\qty{1,65}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{700}{\watt}\cdot {10^{0,165}}\\ P_\mathrm{EIRP} &\approx \qty{1023,52}{\watt}\end{split}$

$\begin{split} d & =\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1023,52}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{6,26}{\meter}\end{split}$

[question:AK110]

Ici, la distance de sécurité doit être calculée pour une antenne directive. Le gain vaut $g_\mathrm{d} = \qty{11,5}{\dBd}$.

$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{75}{\watt}\cdot {10^\dfrac{\qty{11,5}{\dB} −  \qty{1,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{75}{\watt}\cdot {10^\dfrac{\qty{12,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{75}{\watt}\cdot {10^{1,215}}\\ P_\mathrm{EIRP} &\approx \qty{1230,44}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,44}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{6,86}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

$\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{2}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,32}{\meter}\end{split}$

La distance de sécurité de $\qty{6,86}{\meter}$ se situe ici aussi dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK111]

La démarche est analogue à celle de la question précédente.

$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{100}{\watt}\cdot {10^\dfrac{\qty{10,5}{\dBd} −  \qty{1,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{100}{\watt}\cdot {10^\dfrac{\qty{11,15}{\dBd}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{100}{\watt}\cdot {10^{1,115}}\\ P_\mathrm{EIRP} &\approx \qty{1303,17}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,17}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{7,1}{\meter}\end{split}$

La distance de sécurité de $\qty{7,1}{\meter}$ se situe ici aussi dans le champ lointain (champ proche rayonnant).

[question:AK112]

La bande des $\qty{13}{\centi\meter}$ s'étend de $\qtyrange{2320}{2450}{\mega\hertz}$. Pour la gamme de fréquences $\qtyrange{2000}{300000}{\mega\hertz}$, la valeur limite de l'intensité de champ électrique est $\qty{61}{\volt\per\meter}$.

$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{40}{\watt}\cdot {10^\dfrac{\qty{18}{\dBd} −  \qty{2}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{40}{\watt}\cdot {10^\dfrac{\qty{18,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{40}{\watt}\cdot {10^{1,815}}\\ P_\mathrm{EIRP} &\approx \qty{2612,52}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,52}{\watt}}} {\qty{61}{\volt\per\meter}}\\ d &\approx \qty{4,6}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

$\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{0,13}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,02}{\meter}\end{split}$

La distance de sécurité de $\qty{4,6}{\meter}$ se situe nettement dans le champ lointain (champ proche rayonnant).

<indepth>
Pourquoi les questions de cette section font-elles référence aux procédés de modulation RTTY et FM ?
Lors de la déclaration d'une installation radioamateur fixe (selon le § 9 de la BEMFV), il faut saisir dans la configuration le facteur de conversion $\textrm{Faktor}_\textrm{FmodPers}$.

Ce facteur convertit la puissance de crête (PEP) indiquée en puissance moyenne $P$. La puissance ainsi corrigée peut être introduite dans la formule de champ lointain pour le calcul de la distance de protection des personnes.

RTTY et FM ont le facteur $\num{1}$, comme la plupart des procédés de modulation.
</indepth>

Le § 8 de la BEMFV établit entre autres que la distance de sécurité liée au site doit se situer à l'intérieur de la zone contrôlable. Souvent, cette distance est fixée par les contraintes locales et ne peut pas être modifiée. Dans ces cas, la puissance d'émission maximale doit être adaptée.

[question:AK107]

Dans la puissance rayonnée intervient, outre la puissance d'émission, le gain d'antenne exprimé en $\unit{\dBi}$. Il est indiqué $\qty{6}{\dBd}$. Rapporté au radiateur isotrope, cela fait $\qty{6}{\dBd} + \qty{2,15}{\dB}$. Il en résulte un facteur de gain de $G_i = 4 \cdot 1,64 = 6,56$.

La puissance d'émission maximale peut maintenant être déterminée. Pour cela, il faut réarranger la formule de l'intensité de champ dans le champ lointain d'une antenne :
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E \cdot d &= \sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}\\ E^2 \cdot d^2 &= \qty{30}{\ohm}\cdot P_A\cdot G_i\\ \dfrac{E^2 \cdot d^2}{\qty{30}{\ohm}\cdot G_i} &= P_A\\ P_A &= \dfrac{E^2 \cdot d^2}{\qty{30}{\ohm}\cdot G_i}\\ P_A &= \qty{\dfrac{28^2 \cdot 5^2}{30 \cdot 6,56}}{\watt}\\ P_A &\approx \qty{99,59}{\watt}\end{split}$
La puissance d'émission doit être limitée à env. $\qty{100}{\watt}$.

Par simple sécurité, l'équation aux dimensions. Le résultat a pour unité le watt.
$\begin{split} \unit{\watt} &= \dfrac{\left(\unit{\volt\per\meter}\right)^2 \cdot \unit{m\squared}}{\unit{\volt\per\ampere}}\\ \unit{\watt} &= \dfrac{\unit{\volt} \cdot \unit{\volt} \cdot \unit{m\squared} \cdot A}{\unit{\volt} \cdot \unit{m\squared}}\\ \unit{\watt} &= \unit{\volt} \cdot \unit{\ampere}\\ \unit{\watt} &= \unit{\watt}\end{split}$

La formule de l'intensité de champ ne vaut que pour le champ lointain. On peut vérifier rapidement si c'est le cas pour les $\qty{5}{\meter}$ donnés.

$\begin{split}d &> \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{2,06}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,33}{\meter}\end{split}$
La distance de sécurité de $d=\qty{5}{\meter}$ est nettement dans le champ lointain.

Pour les trois questions suivantes, la démarche est plus ou moins la même.
Pour le calcul de l'intensité de champ électrique, on a besoin de la puissance au point d'alimentation de l'antenne, du facteur de gain et de la distance.

[question:AK113]

$P_A$, puissance au point d'alimentation : $\qty{250}{\watt}$ (pas de câble, alimentation directe)

$G_i$, facteur de gain : $\qty{12,15}{\dBi}$ ou $\qty{10}{\dBi}$ et $\qty{2,15}{\dBi}$, ce qui correspond aux facteurs $10 \cdot 1,64 = 16,4$

$d$, distance : $\qty{30}{\meter}$

La formule ne vaut que pour le champ lointain. On peut le vérifier avec $d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{250}{\watt}\cdot 16,4}}{\qty{30}{\meter}}\\ E &\approx \qty{11,7}{\volt\per\meter}\end{split}$

[question:AK114]

$P_A$, puissance au point d'alimentation : $\qty{10}{\watt}$ (pas de câble, alimentation directe)

$G_i$, facteur de gain : $\qty{2,15}{\dBi}$, ce qui correspond au facteur $\num{1,64}$ (dipôle comme antenne)

$d$, distance : $\qty{10}{\meter}$

La formule ne vaut que pour le champ lointain. On peut le vérifier avec $ d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{10}{\watt}\cdot 1,64}}{\qty{10}{\meter}}\\ E &\approx \qty{2,2}{\volt\per\meter}\end{split}$

[question:AK115]

$P_A$, puissance au point d'alimentation : $\qty{100}{\watt}$ (puissance rayonnée en ERP)

$G_i$, facteur de gain : $\qty{2,15}{\dBi}$, ce qui correspond au facteur $\num{1,64}$ (puissance rayonnée en ERP, facteur pour l'EIRP)

$d$, distance : $\qty{100}{\meter}$

La formule ne vaut que pour le champ lointain. On peut le vérifier avec $ d > \dfrac{\lambda}{2 \cdot \pi}$.
$\begin{split}E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot P_A\cdot G_i}}{d}\\ E &= \dfrac{\sqrt{\qty{30}{\ohm}\cdot \qty{100}{\watt}\cdot 1,64}}{\qty{100}{\meter}}\\ E &\approx \qty{0,7}{\volt\per\meter}\end{split}$

<france>
# Le calcul reste le même, le dossier n'existe pas

Tout ce que vous venez de calculer garde sa valeur de ce côté-ci du Rhin : les niveaux de référence français découlent de la même recommandation européenne 1999/519/CE que la 26. BImSchV allemande, transposée par le décret n° 2002-775 du 3 mai 2002. Les $\qty{28}{\volt\per\meter}$ de la plage $\qtyrange{10}{400}{\mega\hertz}$, la moyenne sur six minutes, la formule du champ lointain : rien ne change.

Ce qui change, c'est la procédure administrative — et le plus simple est de dire qu'il n'y en a pas. La France ne connaît **ni fiche de site, ni attestation d'emplacement, ni déclaration préalable** pour une station radioamateur. L'article 5 du décret prévoit uniquement la communication d'un dossier justificatif **à la demande** de l'administration ; l'ANFR est l'autorité qui procède aux contrôles.

Cette absence de formalité ne doit pas être lue comme une absence d'obligation. L'obligation est de résultat : l'exposition du public doit rester sous les valeurs limites, et il faut pouvoir le démontrer. Le calcul que vous venez d'apprendre est donc exactement l'outil dont vous aurez besoin — simplement, vous le conservez chez vous au lieu de le déposer.

Deux points appellent une vigilance particulière :

* **Le cumul.** L'article 3 du décret raisonne en exposition globale, toutes sources confondues. Une station voisine d'un émetteur professionnel ne s'apprécie pas isolément.
* **Le champ proche.** La formule du champ lointain n'a de sens qu'au-delà de $\lambda/2\pi$. En deçà, elle sous-estime le champ, et aucun texte français ne fournit de méthode de substitution : la prudence commande alors d'écarter le public de la zone plutôt que de produire un chiffre rassurant mais faux.

La justification peut s'appuyer soit sur une déclaration de conformité aux normes dont les références sont publiées au Journal officiel, soit sur un mesurage effectué selon le protocole officiel.
</france>
