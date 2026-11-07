Le gain de l'antenne et les pertes de la ligne se combinent dans une grandeur unique : la puissance qu'il faudrait fournir à une antenne de référence pour obtenir le même champ dans la direction principale.

* Référence le **dipôle demi-onde** : **puissance apparente rayonnée** [index:Puissance apparente rayonnée (PAR)], **PAR** (en anglais ERP).
* Référence l'**antenne isotrope** : **puissance isotrope rayonnée équivalente** [index:Puissance isotrope rayonnée équivalente (PIRE)], **PIRE** (en anglais EIRP).

On part de la puissance de l'émetteur, on retire les pertes de la ligne pour obtenir la puissance réellement fournie à l'antenne, puis on applique le gain :

$P_\mathrm{PAR} = P_\mathrm{emetteur} \cdot D \cdot G_\mathrm{d}$ et $P_\mathrm{PIRE} = P_\mathrm{PAR} \cdot \num{1,64}$

où $D$ est le facteur de pertes de la ligne (inférieur à 1) et $G_\mathrm{d}$ le gain par rapport au dipôle, tous deux en **facteurs**, et non en décibels.

<tip>
**Méthode — en décibels, tout s'additionne.** Émetteur de $\qty{100}{\watt}$, câble perdant $\qty{3}{\dB}$, Yagi de $\qty{10}{\dBd}$. Bilan : $-3 + 10 = \qty{7}{\dB}$. Par les facteurs : $100 \times \num{0,5} \times 10 = \qty{500}{\watt}$ PAR. Pour la PIRE, on ajoute $\qty{2,15}{\dB}$ : $500 \times \num{1,64} = \qty{820}{\watt}$ PIRE. Si le gain est donné en $\unit{\dBi}$, on retranche d'abord $\qty{2,15}{\dB}$ pour obtenir des $\unit{\dBd}$.
</tip>

---

Ces deux grandeurs ont un usage **réglementaire** en France, vu au chapitre *Réglementation nationale* :

* la **PAR** fixe le seuil de **déclaration** des stations fixes à l'ANFR, au-delà de $\qty{5}{\watt}$ ;
* la **PIRE** fixe la puissance maximale sur trois bandes seulement : $\qty{1}{\watt}$ sur $\qty{137}{\kilo\hertz}$ et sur $\qty{472}{\kilo\hertz}$, $\qty{15}{\watt}$ sur $\qty{5}{\mega\hertz}$. Partout ailleurs, la limite porte sur la puissance **à la sortie de l'émetteur**.

Une antenne raccourcie a un gain **négatif** : sur $\qty{472}{\kilo\hertz}$, où un demi-onde mesurerait plus de $\qty{300}{\meter}$, des gains de $\qty{-20}{\dBd}$ sont courants. $\qty{-20}{\dB}$, c'est un facteur $\num{0,01}$ : $\qty{50}{\watt}$ à l'antenne donnent $\qty{0,5}{\watt}$ PAR.
