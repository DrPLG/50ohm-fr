Une antenne ne crée pas de puissance : elle la **répartit** dans l'espace. Le **gain** [index:Gain d'antenne] d'une antenne dit combien elle rayonne plus fort dans sa **direction principale** qu'une antenne de référence alimentée avec la même puissance. Il se donne en décibels, avec deux références :

* l'**antenne isotrope** [index:Antenne isotrope], antenne théorique qui rayonne également dans toutes les directions : gain en $\unit{\dBi}$ ;
* le **dipôle demi-onde** : gain en $\unit{\dBd}$.

<margin>
[picture:751:harec_isotrope:Antenne isotrope au centre d'une sphère]
</margin>

Le dipôle demi-onde rayonne, perpendiculairement à son fil, $\qty{2,15}{\dB}$ de plus que l'isotrope (facteur $\num{1,64}$). D'où la conversion :

$g_\mathrm{i} = g_\mathrm{d} + \qty{2,15}{\dB}$

Un dipôle a donc un gain de $\qty{0}{\dBd}$, soit $\qty{2,15}{\dBi}$. Méfiance devant une fiche commerciale : le même gain paraît plus flatteur en $\unit{\dBi}$.

---

Le **diagramme de rayonnement** [index:Diagramme de rayonnement] reporte, dans un plan, le rayonnement dans chaque direction : plus la courbe s'éloigne du centre, plus l'antenne rayonne de ce côté. Un dipôle rayonne **perpendiculairement au fil**, en deux lobes, et presque rien dans l'axe du fil.

<margin>
[picture:1045:harec_diagramme_dipole:Diagramme d'un dipôle, fil vu en bout]
</margin>

Pour une antenne directive, deux grandeurs se lisent sur le diagramme :

* l'**angle d'ouverture** [index:Angle d'ouverture], ou largeur à mi-puissance : l'angle dans lequel le rayonnement reste à moins de $\qty{3}{\dB}$ sous le maximum. Plus le gain est élevé, plus l'ouverture est étroite ;
* le **rapport avant/arrière** [index:Rapport avant/arrière] : l'écart, en décibels, entre le rayonnement vers l'avant et vers l'arrière.

<margin>
[picture:266:harec_ouverture:Angle d'ouverture à mi-puissance]
[picture:1106:harec_avant_arriere:Rapport avant/arrière d'une antenne directive]
</margin>

<tip>
**Méthode — rapport avant/arrière.** Une Yagi rayonne $\qty{200}{\watt}$ équivalents vers l'avant et $\qty{2}{\watt}$ vers l'arrière. Le rapport des puissances vaut $100$, soit $10 \cdot \log_{10}(100) = \qty{20}{\dB}$. À retenir : $\qty{10}{\dB}$ = facteur 10, $\qty{20}{\dB}$ = facteur 100, $\qty{3}{\dB}$ = facteur 2.
</tip>
