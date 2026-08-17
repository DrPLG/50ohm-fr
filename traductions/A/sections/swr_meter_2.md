Dans la classe E, nous avons déjà fait connaissance avec le SWR-mètre et son utilisation. Dans la classe A, nous voulons comprendre comment un appareil de mesure d'ondes stationnaires fonctionne intérieurement. Un SWR-mètre se compose en règle générale de deux coupleurs directifs. Familiarisons-nous d'abord avec leur principe de fonctionnement.

Un *coupleur directif* sert à prélever une petite partie d'un signal HF circulant dans une ligne d'alimentation. Sa particularité est qu'il peut distinguer, ce faisant, dans quel sens l'onde se propage sur la ligne. Pour cela, le signal est saisi de deux manières différentes. Un couplage capacitif fournit une tension $U_C$, qui dépend de la tension présente sur la ligne d'alimentation. Simultanément, le couplage inductif engendre une tension $U_I$, qui dépend du courant circulant dans la ligne d'alimentation. Le coupleur directif est dimensionné de telle sorte que les composantes du signal obtenues par voie capacitive et par voie inductive soient d'égale amplitude à ses sorties. Aux deux sorties, ces composantes sont toutefois combinées avec des signes différents.

Pour une onde qui se propage dans un sens déterminé sur la ligne, p. ex. de la gauche vers la droite comme le montre la figure [ref:a_richtkoppler_rechts_links], les tensions obtenues par voie capacitive et par voie inductive s'additionnent à l'une des sorties. À l'autre sortie, elles sont en opposition et s'annulent mutuellement dans le cas idéal. Le signal n'apparaît donc principalement qu'à l'une des deux sorties.

<margin>
[picture:1109:a_richtkoppler_rechts_links:Coupleur directif, l'onde se propage de la gauche vers la droite]
</margin>

---

Si le sens de propagation de l'onde s'inverse, p. ex. de la droite vers la gauche comme le montre la figure [ref:a_richtkoppler_rechts_links], le sens du courant s'inverse lui aussi par rapport à la tension. La tension $U_I$ obtenue par couplage inductif change alors de signe, tandis que la tension $U_C$ obtenue par couplage capacitif suit la tension de la ligne.

<margin>
[picture:1110:a_richtkoppler_rechts_links:Coupleur directif, l'onde se propage de la droite vers la gauche]
</margin>

Les deux sorties du coupleur directif se trouvent ainsi permutées : la sortie où les deux composantes s'additionnaient auparavant est maintenant très largement annulée, tandis qu'elles s'additionnent à l'autre sortie.

De cette manière, un coupleur directif peut distinguer une *onde directe*, en direction de l'antenne, d'une *onde réfléchie*, en direction de l'émetteur.

---

Cette propriété des coupleurs directifs est mise à profit dans un *appareil de mesure d'ondes stationnaires*, autrement dit un *SWR-mètre* : on mesure pour cela les tensions de sortie de deux coupleurs directifs insérés dans la ligne, exploités en sens opposés. Les tensions HF présentes aux sorties des coupleurs directifs sont redressées par des diodes, puis lissées. Il en résulte des tensions continues, que l'on peut afficher au moyen d'un instrument de mesure.

[question:AI401]

La figure [ref:a_rswr_meter] montre la constitution de principe d'un appareil de mesure d'ondes stationnaires à deux coupleurs directifs. Nous supposons ici que l'émetteur se trouve du côté gauche et l'antenne du côté droit.

[question:AI402]

Le conducteur supérieur fait partie de la ligne d'alimentation entre l'émetteur et l'antenne. Deux grandeurs y sont saisies : le couplage capacitif prélève une petite fraction de la tension HF ; le couplage inductif fournit simultanément une composante qui dépend du courant circulant dans la ligne d'alimentation.

Le côté de la ligne de couplage qui ne sert pas à la mesure est fermé sur une *résistance de terminaison*. Cette résistance correspond approximativement à l'impédance caractéristique $Z_0$ de la ligne de couplage. La puissance HF qui y parvient est ainsi absorbée, et non renvoyée dans la ligne de couplage. De telles réflexions dégraderaient la séparation entre onde directe et onde réfléchie.

Ces deux composantes du signal sont combinées dans le coupleur directif. Pour une onde qui va de l'émetteur vers l'antenne, elles s'additionnent dans l'un des deux coupleurs, tandis qu'elles s'annulent très largement dans l'autre. Pour une onde de sens opposé, c'est exactement l'inverse.

Les deux parties du circuit, de constitution presque symétrique, peuvent ainsi saisir des sens de propagation différents :

* L'un des coupleurs directifs délivre un signal proportionnel à l'*onde directe*, de l'émetteur vers l'antenne.
* L'autre coupleur directif délivre un signal proportionnel à l'*onde réfléchie*, de l'antenne vers l'émetteur.

Les signaux prélevés sont d'abord des tensions alternatives HF. Les diodes les redressent et les condensateurs les lissent. Il en résulte des tensions continues, que l'on peut afficher au moyen des deux mouvements d'un instrument à aiguilles croisées, ou mesurer par un microcontrôleur muni d'un convertisseur analogique-numérique. Les résistances ajustables servent au réglage, autrement dit à l'étalonnage de l'affichage. Elles sont à distinguer des résistances de terminaison des lignes de couplage, qui assurent une terminaison peu réfléchissante sur $Z_0$.

<margin>
[picture:499:a_rswr_meter:SWR-mètre à deux coupleurs directifs]
</margin>
