La **puissance électrique** [index:Puissance électrique] est le produit de la tension par le courant, $P = U \cdot I$, en watts. Avec la loi d'Ohm $U = R \cdot I$, on en tire les deux formes utiles quand on connaît la résistance :

$P = \dfrac{U^2}{R} = R \cdot I^2$

En alternatif, ces formules valent avec les **valeurs efficaces** : $U_\mathrm{eff} = \hat{U} / \sqrt{2}$, où $\hat{U}$ est la tension de crête.

<tip>
**Méthode — puissance dans une charge.** Une tension efficace de $\qty{100}{\volt}$ sur une charge de $\qty{50}{\ohm}$ : $100^2 \div 50 = \qty{200}{\watt}$. Mesurée à l'oscilloscope, la même tension se lit $\qty{141}{\volt}$ en crête, $\qty{283}{\volt}$ crête à crête : on divise d'abord la crête par $\num{1,41}$.
</tip>

---

Une source a toujours une **résistance interne** $R_\mathrm{i}$. Elle fournit la puissance la plus grande possible à sa charge quand la résistance de charge est **égale** à sa résistance interne : c'est le **transfert maximal de puissance** [index:Transfert maximal de puissance], ou **adaptation**. Les émetteurs, les câbles et les antennes sont donc construits autour d'une même impédance, $\qty{50}{\ohm}$. À l'adaptation, la moitié de la puissance se perd dans la résistance interne.

---

<margin>
[picture:1120:harec_flux_puissance:Puissance fournie, puissance HF de sortie et puissance dissipée d'un amplificateur]
</margin>

Un amplificateur prend une puissance continue à son alimentation et n'en rend qu'une partie en haute fréquence ; le reste chauffe les transistors et le radiateur. Le **rendement** [index:Rendement] est le rapport des deux :

$\eta = \dfrac{P_\mathrm{sortie}}{P_\mathrm{entree}} \cdot \qty{100}{\percent}$

<tip>
**Méthode — rendement et chaleur.** Un émetteur alimenté sous $\qty{13,8}{\volt}$ consomme $\qty{20}{\ampere}$ et délivre $\qty{100}{\watt}$. Puissance absorbée : $\num{13,8} \times 20 = \qty{276}{\watt}$. Rendement : $100 \div 276 \approx \qty{36}{\percent}$. Le radiateur doit évacuer $276 - 100 = \qty{176}{\watt}$.
</tip>
