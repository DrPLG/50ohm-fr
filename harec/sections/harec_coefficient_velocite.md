Dans le vide, et à peu près dans l'air, longueur d'onde et fréquence sont liées par la vitesse de la lumière $c = \qty{300000}{\kilo\meter\per\second}$ :

$\lambda = \dfrac{c}{f}$

Le long d'une ligne ou d'un fil d'antenne, l'onde va moins vite. Le **coefficient de vélocité** [index:Coefficient de vélocité] $k_\mathrm{v}$ (inférieur à 1) est le rapport de sa vitesse dans la ligne à sa vitesse dans le vide. La longueur d'onde sur la ligne est donc plus courte :

$\lambda_\mathrm{ligne} = k_\mathrm{v} \cdot \dfrac{c}{f}$

Dans un **câble coaxial**, l'onde voyage dans l'isolant, et seul celui-ci compte :

$k_\mathrm{v} = \dfrac{1}{\sqrt{\epsilon_\mathrm{r}}}$

| l: Ligne | l: Ordre de grandeur de $k_\mathrm{v}$ |
| coaxial au polyéthylène plein ($\epsilon_\mathrm{r} = \num{2,29}$) | $\num{0,66}$ |
| coaxial à isolant mousse | $\num{0,8}$ à $\num{0,85}$ |
| ligne bifilaire, isolant surtout d'air | proche de $\num{1}$ |
| fil d'antenne | environ $\num{0,95}$ |
[table:harec_coefficients:Coefficients de vélocité usuels]

Pour un fil d'antenne, la correction vient de ce que le fil n'est pas infiniment fin : une antenne se coupe environ **5 % plus courte** que la demi-onde ou le quart d'onde calculé dans le vide.

<tip>
**Méthode — couper un dipôle ou un tronçon de câble.** Pour un dipôle demi-onde à $\qty{14,2}{\mega\hertz}$ : $\lambda = 300 \div \num{14,2} \approx \qty{21,1}{\meter}$, la demi-onde fait $\qty{10,56}{\meter}$, et avec $k_\mathrm{v} = \num{0,95}$ on coupe $\qty{10,0}{\meter}$ en tout. Pour un quart d'onde de RG-58 à $\qty{145}{\mega\hertz}$ : $\lambda = 300 \div 145 \approx \qty{2,07}{\meter}$, le quart fait $\qty{0,517}{\meter}$, multiplié par $\num{0,66}$ : $\qty{0,34}{\meter}$ de câble. Astuce : $300$ divisé par la fréquence en $\unit{\mega\hertz}$ donne $\lambda$ en mètres.
</tip>
