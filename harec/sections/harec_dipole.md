L'antenne transforme le courant haute fréquence venu de l'émetteur en onde radio, et inversement à la réception. Sa forme de base est le **dipôle** [index:Dipôle] : deux brins conducteurs alignés, chacun relié à un conducteur de la ligne d'alimentation.

<margin>
[picture:589:harec_dipole_schema:Antenne dipôle]
</margin>

Le plus employé est le **dipôle demi-onde**, de longueur totale $\lambda/2$, soit deux brins de $\lambda/4$. À cette longueur, il est **résonant** : il rayonne au mieux la puissance reçue, et son impédance au centre est une simple résistance, voisine de $\qty{73}{\ohm}$.

<tip>
**Méthode — longueur d'un dipôle.** La longueur d'onde en mètres vaut $300$ divisé par la fréquence en mégahertz. À $\qty{14,2}{\mega\hertz}$ : $300 \div \num{14,2} \approx \qty{21,1}{\meter}$, donc $\lambda/2 \approx \qty{10,6}{\meter}$, soit deux brins de $\qty{5,3}{\meter}$. Le fil réel est **quelques pour cent plus court** (facteur de l'ordre de $\num{0,95}$), à cause de son diamètre et des effets d'extrémité : environ $\qty{10}{\meter}$ au total.
</tip>

---

Le réglage se fait au ROS-mètre :

* résonance **trop basse** : le dipôle est **trop long**, on raccourcit les deux brins de la même longueur ;
* résonance **trop haute** : il est **trop court**, on les allonge.

On coupe toujours le fil un peu trop long au départ : raccourcir est facile, allonger beaucoup moins.

---

Un dipôle demi-onde résonne aussi aux **multiples impairs** de sa fréquence fondamentale : un dipôle taillé pour $\qty{7}{\mega\hertz}$ fonctionne vers $\qty{21}{\mega\hertz}$. Aux multiples **pairs**, le centre tombe sur un nœud de courant, l'impédance devient très élevée, et le dipôle n'est pas utilisable tel quel.

---

<margin>
[picture:562:harec_dipole_replie:Dipôle replié]
</margin>

Le **dipôle replié** [index:Dipôle replié] referme les deux brins par un second conducteur parallèle. Il a la même longueur et le même diagramme que le dipôle simple, mais le courant au point d'alimentation est divisé par deux pour une tension double : l'impédance est **multipliée par quatre**, soit $\num{240}$ à $\qty{300}{\ohm}$. On l'alimente par une ligne bifilaire de $\qty{300}{\ohm}$, ou par un symétriseur 4:1 sur un coaxial de $\qty{75}{\ohm}$. C'est le radiateur habituel des antennes Yagi de télévision.
