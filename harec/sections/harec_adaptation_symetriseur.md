Pour raccorder une antenne dont l'impédance n'est pas $\qty{50}{\ohm}$, on **transforme** son impédance : c'est l'**adaptation d'impédance** [index:Adaptation d'impédance]. Trois moyens courants : un **transformateur**, une **ligne quart d'onde**, un **réseau de bobines et de condensateurs** (la boîte d'accord, section suivante).

Le **transformateur quart d'onde** [index:Transformateur quart d'onde] est un tronçon de ligne de longueur électrique $\lambda/4$. Il **inverse** les impédances autour de sa propre impédance caractéristique : une charge plus basse que la ligne devient plus haute, et inversement. Pour adapter une charge $Z_\mathrm{A}$ à une entrée $Z_\mathrm{E}$, il faut une ligne d'impédance égale à leur **moyenne géométrique** :

$Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$

<tip>
**Méthode — ligne quart d'onde.** Un cadre de $\qty{100}{\ohm}$ à raccorder à $\qty{50}{\ohm}$ : $\sqrt{50 \times 100} \approx \qty{71}{\ohm}$. Un tronçon $\lambda/4$ de coaxial $\qty{75}{\ohm}$ convient. Sa longueur **mécanique** tient compte du coefficient de vélocité : à $\qty{14}{\mega\hertz}$, $\lambda/4 \approx \qty{5,36}{\meter}$, soit environ $\qty{3,5}{\meter}$ de câble à $k_\mathrm{v} = \num{0,66}$. Une ligne $\lambda/2$, elle, ne transforme rien : elle répète l'impédance de son extrémité.
</tip>

---

Un dipôle est une antenne **symétrique** ; le coaxial est une ligne **asymétrique**. Branché directement, le courant ne se partage plus également : une partie revient par la **face extérieure du blindage**. Ce sont les **ondes de gaine** [index:Ondes de gaine] : le câble rayonne, devient un morceau d'antenne, déforme le diagramme, **perturbe les appareils voisins** à l'émission et ramène les parasites de la maison à la réception.

<margin>
[picture:633:harec_ondes_gaine:Ondes de gaine sur le blindage d'un coaxial]
</margin>

On les empêche par un **symétriseur** [index:Symétriseur], ou **balun** (*balanced–unbalanced*), placé au point d'alimentation. La forme la plus simple est le **bloqueur d'ondes de gaine** : quelques tours de coaxial sur un tore de ferrite. Le signal utile, dont les courants sont égaux et opposés dans l'âme et le blindage, le traverse sans effet ; le courant de gaine y rencontre une forte impédance. Certains baluns transforment aussi l'impédance (4:1 pour un dipôle replié, par exemple).
