L'**antenne Yagi-Uda** [index:Antenne Yagi-Uda], ou simplement **Yagi**, est l'antenne **directive** la plus répandue. Elle concentre l'onde dans une direction, comme le réflecteur d'une lampe de poche, et on l'oriente vers le correspondant. Elle porte le nom de ses inventeurs japonais, Hidetsugu Yagi et Shintaro Uda (1926).

<margin>
[picture:1048:harec_yagi_elements:Antenne Yagi à trois éléments — réflecteur, radiateur, directeur]
</margin>

Elle se compose d'éléments parallèles fixés sur une poutre, le *boom* :

* le **radiateur** [index:Radiateur], dipôle simple ou replié, seul relié à la ligne ;
* le **réflecteur** [index:Réflecteur], derrière, **un peu plus long** ;
* un ou plusieurs **directeurs** [index:Directeur], devant, **un peu plus courts**.

Réflecteur et directeurs ne sont reliés à rien : ce sont des **éléments parasites**. L'onde du radiateur y induit des courants, et ils rayonnent à leur tour avec un déphasage. Vers l'avant, les ondes s'ajoutent ; vers l'arrière, elles s'annulent en partie. Moyen mnémotechnique : on rayonne **vers le plus court**.

---

<margin>
[picture:1049:harec_yagi_diagramme:Diagramme de rayonnement d'une Yagi]
</margin>

Le diagramme montre un **lobe principal** vers l'avant, un petit **lobe arrière** et des **lobes secondaires**. Ajouter des directeurs, et donc allonger le boom, augmente le **gain** : la puissance se concentre davantage dans le lobe principal, qui devient **plus étroit**. L'antenne ne crée pas d'énergie, elle la répartit autrement.

Les éléments parasites modifient aussi l'impédance du radiateur, souvent nettement en dessous de $\qty{50}{\ohm}$ : c'est une raison fréquente d'employer un dipôle replié ou un adaptateur.

---

La **polarisation** d'une Yagi est celle de ses éléments : horizontale s'ils sont horizontaux. Deux Yagi croisées à $\qty{90}{\degree}$ sur le même boom, alimentées avec un déphasage de $\qty{90}{\degree}$, donnent une polarisation **circulaire**, appréciée pour le trafic par satellite.
