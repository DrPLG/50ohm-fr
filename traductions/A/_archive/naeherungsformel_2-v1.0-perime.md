%Um die Feldstärke einer Antenne im Fernfeld ($d>\frac \lambda {2 \pi}$) zu berechnen gibt es die folgende Näherungsformel:

%$E=\frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{A} \cdot G_\mathrm{i}}} {d}=\frac {\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}} d$

%mit der Leistung an der Antenne $P_\mathrm{A}$, dem Gewinnfaktor bezogen auf den Isotropen Strahler %$G_\mathrm{i}$, und dem Abstand $d$

%Für den Gewinnfaktor von Antennen ist gegeben:

%$G_\mathrm{i}=G_\mathrm{d} \cdot 1,64$ 

%bzw.

%$g_\mathrm{i} = g_\mathrm{d}+2,15\text{ dB}$

%Es ist in der Prüfung der Grenzwert für den Personenschutzabstand angegeben. Um den Personenschutzabstand dann zu berechnen, muss daher die Formel umgestellt werden zu

%$d=\frac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{A} \cdot G_\mathrm{i}}} {E}$

%Jedoch ist meist nicht die Leistung an der Antenne angegeben, und genauso wenig der Gewinn gegenüber einem Isotropen Strahler. Entsprechend muss dies mit berücksichtigt werden. Dies ergibt dann:

%$d=\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{Transceiver} \cdot G_\mathrm{Kabel} \cdot G_\mathrm{d} \cdot 1,64}} {E}$

%Mit der Leistung am Transceiver $P_\mathrm{Transceiver}$, dem "Gewinn" des Kabels $G_\mathrm{Kabel}$ (hier entsprechend mit negativem Vorzeichen einsetzen) und dem Gewinn gegenüber dem Dipol $G_\mathrm{d}$.

%Der "Gewinn" des Kabels kann z.B. berechnet werden für ein Kabel mit einer Dämpfung von $2 \text{ dB}$:
%$G_\mathrm{Kabel} = 10^{\frac {-2 \text{ dB}} {10 \text{ dB}}} = 10^{-0,2}= 0,631$

% DD4UQ
Lors de la déclaration d'une installation radioamateur fixe, les distances de sécurité peuvent être déterminées selon différents procédés. L'un d'eux est le calcul en champ lointain.
Pour le calcul, on a besoin de la puissance d'émission ($P_\mathrm{S}$), du facteur de gain de l'antenne rapporté au radiateur isotrope ($G_\mathrm{i} = 1,64$) et de la valeur limite de l'intensité de champ $(E = \qty{28}{\volt\per\meter})$ dans le champ lointain d'une antenne. La longueur d'onde ($\qty{10}{\meter}$) n'est indiquée que pour déterminer le début du champ lointain.

$\begin{split} d &=\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{A} \cdot G_\mathrm{i}}}{E}\\ d &=\dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{100}{\watt} \cdot 1,64}}{\qty{28}{\volt\per\meter}}\\ d &\approx \qty{2,50}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

 $\begin{split}d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{10}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{1,59}{\meter}\end{split}$
 
 La distance de sécurité de $\qty{2,50}{\meter}$ se situe nettement dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK106]

La question AK108 ressemble à la question précédente. Ici, il faut en plus tenir compte de l'atténuation du câble.

Il est ici judicieux de calculer d'abord l'EIRP.

$P_\mathrm{EIRP} = P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}$
Pour une antenne directive, la valeur de $g_\mathrm{d}$ doit être indiquée. Un simple dipôle n'a de gain que par rapport à un radiateur isotrope. Ici, $g_\mathrm{d} = \qty{0}{\dBd}$.
$\begin{split}P_\mathrm{EIRP} &= \qty{300}{\watt}\cdot {10^\dfrac{\qty{0}{\dBd} −  \qty{0,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{300}{\watt}\cdot {10^\dfrac{\qty{1,65}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{300}{\watt}\cdot {10^{0,165}}\\ P_\mathrm{EIRP} &\approx \qty{438,65}{\watt}\end{split}$

La distance de sécurité peut maintenant être calculée.

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{438,65}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{4,10}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

 $\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{20}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{3,18}{\meter}\end{split}$
 
 La distance de sécurité de $\qty{4,10}{\meter}$ se situe ici aussi dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK108]

On peut procéder ici exactement comme pour la question précédente.
$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{700}{\watt}\cdot {10^\dfrac{\qty{0}{\dBd} −  \qty{0,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{700}{\watt}\cdot {10^\dfrac{\qty{1,65}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{700}{\watt}\cdot {10^{0,165}}\\ P_\mathrm{EIRP} &\approx \qty{1023,52}{\watt}\end{split}$

$\begin{split} d & =\dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1023,52}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{6,26}{\meter}\end{split}$

[question:AK109]

Pour la question suivante, la distance de sécurité doit être calculée pour une antenne directive. Le gain $g_\mathrm{d} = \qty{11,5}{\dBd}$.

$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{75}{\watt}\cdot {10^\dfrac{\qty{11,5}{\dB} −  \qty{1,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{75}{\watt}\cdot {10^\dfrac{\qty{12,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{75}{\watt}\cdot {10^{1,215}}\\ P_\mathrm{EIRP} &\approx \qty{1230,44}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1230,44}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{6,86}{\meter}\end{split}$

 La distance est-elle dans le champ lointain (champ proche rayonnant) ?

 $\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{2}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,32}{\meter}\end{split}$
 
 La distance de sécurité de $\qty{6,86}{\meter}$ se situe ici aussi dans le champ lointain (champ proche rayonnant) et est donc valable.

[question:AK110]

La démarche est analogue à celle de la question précédente.

$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{100}{\watt}\cdot {10^\dfrac{\qty{10,5}{\dBd} −  \qty{1,5}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{100}{\watt}\cdot {10^\dfrac{\qty{11,15}{\dBd}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{100}{\watt}\cdot {10^{1,115}}\\ P_\mathrm{EIRP} &\approx \qty{1303,17}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{1303,17}{\watt}}} {\qty{28}{\volt\per\meter}}\\ d &\approx \qty{7,1}{\meter}\end{split}$

La distance de sécurité de $\qty{7,1}{\meter}$ se situe ici aussi dans le champ lointain (champ proche rayonnant).

[question:AK111]

La bande des $\qty{13}{\centi\meter}$ s'étend de $\qtyrange{2320}{2450}{\mega\hertz}$. Pour la gamme de fréquences $\qtyrange{2000}{300000}{\mega\hertz}$, la valeur limite de l'intensité de champ électrique est $\qty{61}{\volt\per\meter}$.

$\begin{split} P_\mathrm{EIRP} &= P_\mathrm{S} \cdot {10^\dfrac{g_\mathrm{d}  −  a  +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{40}{\watt}\cdot {10^\dfrac{\qty{18}{\dBd} −  \qty{2}{\dB} +  \qty{2,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{40}{\watt}\cdot {10^\dfrac{\qty{18,15}{\dB}}{\qty{10}{\dB}}}\\ P_\mathrm{EIRP} &= \qty{40}{\watt}\cdot {10^{1,815}}\\ P_\mathrm{EIRP} &\approx \qty{2612,52}{\watt}\end{split}$

$\begin{split} d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot P_\mathrm{EIRP}}}{E}\\ d &= \dfrac{\sqrt{\qty{30}{\ohm} \cdot \qty{2612,52}{\watt}}} {\qty{61}{\volt\per\meter}}\\ d &\approx \qty{4,6}{\meter}\end{split}$

La distance est-elle dans le champ lointain (champ proche rayonnant) ?

$\begin{split} d &= \dfrac{\lambda}{2 \cdot \pi}\\ d &= \dfrac{\qty{0,13}{\meter}}{2 \cdot \pi}\\ d &\approx \qty{0,02}{\meter}\end{split}$

La distance de sécurité de $\qty{4,6}{\meter}$ se situe nettement dans le champ lointain (champ proche rayonnant).

[question:AK112]

<indepth>
Pourquoi les questions de cette section font-elles référence aux procédés de modulation RTTY et FM ?
Lors de la déclaration d'une installation radioamateur fixe (selon le § 9 de la BEMFV), il faut saisir dans la configuration le facteur de conversion $\textrm{Faktor}_\textrm{FmodPers}$.
Ce facteur convertit la puissance de crête (PEP) indiquée en puissance moyenne $P$. La puissance ainsi corrigée peut être introduite dans la formule de champ lointain pour le calcul de la distance de protection des personnes.

RTTY et FM ont le facteur $\num{1}$, comme la plupart des procédés de modulation.
</indepth>