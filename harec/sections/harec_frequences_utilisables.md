Entre deux lieux donnés, l'ionosphère ne renvoie qu'une **plage** de fréquences. Deux limites la bornent.

La **MUF** [index:MUF] (*maximum usable frequency*, fréquence maximale utilisable) est la fréquence la plus haute encore renvoyée vers la Terre pour cette distance. Au-dessus, l'onde traverse l'ionosphère et part vers l'espace — c'est d'ailleurs pourquoi on contacte la station spatiale ISS sur la bande des $\qty{2}{\meter}$, bien au-dessus de toute MUF. La MUF monte avec l'ionisation : elle est plus haute de jour que de nuit, et plus haute au maximum du cycle solaire.

La **LUF** [index:LUF] (*lowest usable frequency*, fréquence minimale utilisable) est la fréquence la plus basse encore utilisable. En dessous, l'absorption de la région D, traversée deux fois à chaque saut, est trop forte. Cette absorption croît comme le carré de l'inverse de la fréquence : diviser la fréquence par deux multiplie l'absorption par quatre. La LUF dépend aussi de la station (puissance, antenne, sensibilité du récepteur). Quand la LUF dépasse la MUF, plus aucune liaison par onde d'espace n'est possible sur ce trajet.

<margin>
[picture:991:harec_prevision_muf_luf:Prévision de la MUF et de la LUF sur une journée]
</margin>

---

<margin>
[picture:870:harec_angles_muf:Angles servant au calcul de la MUF]
</margin>

Les ionosondes mesurent la **fréquence critique** $f_\text{c}$ (souvent notée $f_\text{oF2}$ pour la région F2) : la fréquence la plus haute renvoyée quand on émet **verticalement**. C'est le cas le plus défavorable, car l'onde doit faire demi-tour complet. Plus l'onde aborde l'ionosphère de façon rasante, plus la fréquence renvoyée est élevée :

$\mathrm{MUF} \approx \frac{f_\text{c}}{\sin(\alpha)}$

où $\alpha$ est l'angle de rayonnement de la figure [ref:harec_angles_muf] (formule valable pour $\alpha > \qty{40}{\degree}$). La MUF est donc toujours supérieure à $f_\text{c}$, et en incidence très rasante elle atteint environ **trois fois** la fréquence critique.

Pour les liaisons professionnelles, on vise la **FOT** (*fréquence optimale de travail*), qui passe 90 % des jours :

$f_\text{opt} \approx \num{0,85} \cdot \mathrm{MUF}$

Le radioamateur en quête de DX choisit plutôt la bande la plus haute encore ouverte, au plus près de la MUF, où le bruit est le plus faible.

<tip>
**Méthode — calculer une MUF à la calculatrice.** Avec $f_\text{c} = \qty{5}{\mega\hertz}$ et un angle de $\qty{45}{\degree}$, on tape $5 \div \sin(45)$, calculatrice en **degrés** : $\mathrm{MUF} \approx \qty{7,1}{\mega\hertz}$. La bande des $\qty{40}{\meter}$ passe, celle des $\qty{30}{\meter}$ non. La FOT vaut alors $\num{0,85} \times \num{7,1} \approx \qty{6}{\mega\hertz}$. Vérifier l'ordre de grandeur : la MUF doit être plus grande que $f_\text{c}$.
</tip>
