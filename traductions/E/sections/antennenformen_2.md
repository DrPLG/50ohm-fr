Dans la classe N, nous avons déjà fait connaissance avec quelques formes d'antennes. Dans la classe E, nous voulons maintenant examiner de plus près les propriétés des différentes antennes. Les dipôles alimentés au centre sont des *antennes symétriques*. Par antenne symétrique, nous entendons une antenne qui, dans le cas idéal, présente en fonctionnement, à ses deux pôles (par exemple les points d'alimentation de chaque brin d'un dipôle), la même tension par rapport à la terre, au signe près. C'est le cas des dipôles, y compris le dipôle replié, ainsi que des antennes Yagi-Uda qui en dérivent. Une antenne Groundplane, en revanche, présente idéalement au point de raccordement des radians le potentiel de la terre (donc une tension nulle par rapport à la terre) et ne compte donc pas parmi les antennes symétriques.

<indepth>
Pour les câbles de transmission de signaux également, par exemple la ligne d'alimentation d'une antenne, on distingue les *câbles symétriques et asymétriques*. Ici aussi, la symétrie se rapporte aux tensions électriques par rapport à la terre régnant dans le cas idéal. Dans un câble coaxial, les courants devraient certes être symétriques, mais seul le conducteur intérieur devrait présenter une tension par rapport à la terre. Les câbles coaxiaux comptent donc parmi les lignes d'alimentation asymétriques. Comme nous l'apprendrons plus tard, ces lignes d'alimentation asymétriques ne devraient être raccordées à une antenne symétrique qu'au moyen d'un dispositif dit symétriseur (balun).
</indepth>

[question:EG213]

---

Une forme d'antenne appréciée est un fil d'une longueur totale d'environ une longueur d'onde, en forme de cercle, de carré, de triangle ou d'une forme similaire. On parle alors d'*antennes cadres* (antennes boucles) onde entière. En raison de sa construction simple, l'antenne dite Delta-Loop, qui, comme le grand delta (Δ) de l'alphabet grec, a la forme d'un triangle, est très appréciée.

<margin>
[picture:311:e_delta_loop:Exemple d'antenne Delta-Loop]
</margin>

[question:EG101]

<indepth>
La *forme* exacte n'a pas d'importance pour les antennes cadres onde entière, pour autant que la longueur du fil corresponde à environ une longueur d'onde. Selon la forme, on peut toutefois obtenir des résistances d'alimentation différentes ou des gains d'antenne légèrement meilleurs ou moins bons.
</indepth>

---

Des antennes cadres onde entière, il faut distinguer les *antennes boucles magnétiques* (Magnetic-Loops), qui présentent des dimensions beaucoup plus petites par rapport à la longueur d'onde et produisent un champ proche magnétique (cf. figure [ref:e_mag_loop]).

<margin>
[picture:977:e_mag_loop:Exemple d'antenne Magnetic-Loop]
</margin>

[question:EG105]

<indepth>
Bien que de telles antennes boucles magnétiques conviennent en principe aussi à l'émission, il est difficile d'obtenir un *rendement* élevé. Des rendements entre $\qty{1}{\percent}$ et $\qty{10}{\percent}$ sont habituels pour les antennes magnétiques en émission. Ces Magnetic-Loops peuvent néanmoins offrir des avantages par rapport à d'autres antennes : outre leur construction compacte, elles sont souvent moins perturbées par les objets électriquement conducteurs ou absorbants situés dans le champ proche, par exemple les murs ou les tuiles en cas de montage à l'intérieur ou sous un toit. 
</indepth>

---

Les *antennes alimentées en extrémité* sont alimentées par l'une de leurs extrémités. Leur longueur est le plus souvent d'une demi-longueur d'onde. On parle alors aussi de dipôle demi-onde alimenté en extrémité (en anglais : end fed half wave, EFHW). Une telle antenne nécessite une tension nettement plus élevée par rapport au courant, qui peut être produite par un dispositif d'adaptation approprié, par exemple un circuit de Fuchs. Les dipôles demi-onde alimentés en extrémité qui sont adaptés au moyen d'un circuit de Fuchs sont appelés en conséquence antennes Fuchs.

[question:EG104]
[question:EG103]

<margin>
[picture:310:e_fuchsantenne:Exemple d'antenne Fuchs]
</margin>

<person>
Le circuit de Fuchs et l'antenne Fuchs sont nommés d'après le *Dr Josef Fuchs* (indicatifs radioamateur OE1JF, UO1JF et EAAA), qui les a d'ailleurs fait breveter en 1927.
</person>

<indepth>
Une antenne alimentée en extrémité nécessite elle aussi un *contrepoids*, par exemple sous la forme d'un fil de $\lambda / 4$ ou d'une autre forme de mise à la terre HF. Toutefois, les courants qui apparaissent au point d'alimentation des EFHW sont nettement plus faibles, raison pour laquelle une mise à la terre moins bonne peut aussi suffire, par exemple un bout de fil court d'un dixième, voire d'un vingtième de la longueur d'onde seulement. Parfois, seuls le blindage de la ligne d'alimentation ou d'autres éléments métalliques (servant en réalité à d'autres fins) font office de mise à la terre.
  
À ne pas confondre avec les dipôles demi-onde alimentés en extrémité : les *antennes long-fil* alimentées en extrémité, dont la longueur dépasse nettement une longueur d'onde. La confusion vient de ce que les dipôles demi-onde alimentés en extrémité sont souvent aussi exploités sur des fréquences plus élevées, pour lesquelles ils constituent alors de facto une antenne long-fil.
</indepth>

---

La directivité d'une antenne peut être représentée dans un diagramme dit de rayonnement. Pour un plan donné, on y reporte dans chaque direction le gain, respectivement l'intensité de champ ou la puissance rayonnée. Plus le tracé du graphe est éloigné du centre, plus le gain est grand, respectivement plus l'intensité de champ et la puissance rayonnée en champ lointain sont élevées. Si aucune échelle avec des angles n'est utilisée, on représente aussi souvent la disposition mécanique de l'antenne dans le même diagramme, afin de montrer clairement quelle direction du diagramme correspond à quelle direction par rapport à la disposition de l'antenne.

Un dipôle ne rayonne pas, comme on pourrait le supposer à tort, dans la direction du fil, mais perpendiculairement à celui-ci. Considéré dans un plan et reporté sous forme de diagramme de rayonnement, on obtient des lobes correspondants (par exemple à gauche et à droite) de part et d'autre du dipôle (cf. figure [ref:e_dipol_strahlungsdiagramm]). Un dipôle suspendu verticalement rayonne donc par exemple vers la gauche et la droite ainsi que vers l'avant et l'arrière. Comme le diagramme de rayonnement ne considère qu'un seul plan, on ne voit par exemple qu'un lobe pour le rayonnement vers la gauche et un lobe pour le rayonnement vers la droite. Selon l'échelle, ces lobes peuvent paraître circulaires.

<margin>
[picture:1045:e_dipol_strahlungsdiagramm:Exemple de rayonnement du dipôle]
</margin>

<indepth>
Un *lobe de section circulaire* s'obtient, avec une échelle linéaire par rapport à l'intensité de champ, lorsqu'on considère un dipôle fortement raccourci (dipôle hertzien). Un dipôle demi-onde a en réalité un gain un peu plus élevé, correspondant à un lobe un peu plus étroit. Nous trouvons néanmoins dans les questions d'examen une représentation circulaire, qui n'est correcte qu'approximativement. Avec une échelle linéaire par rapport à la puissance rayonnée dans la direction considérée, le lobe devrait être encore plus étroit.
% TODO: ggf. Fragenbild korrigieren
</indepth>

[question:EG215]
[question:EG214]

---

En raison de la caractéristique de rayonnement perpendiculaire au dipôle, un dipôle demi-onde monté verticalement peut ainsi permettre un rayonnement à angle bas, ce qui peut être souhaité par exemple en trafic DX, mais aussi pour des contacts par onde directe ou onde de sol.

[question:EG219]

<margin>
[photo:316:e_vertikaldipol:Dipôle $\frac{\lambda}{2}$ vertical]
</margin>

---

Un cas particulier d'antenne verticale est l'antenne $5/8 \lambda$ excitée contre la terre (ou contre la carrosserie d'un véhicule) (cf. figure [ref:e_fuenf_achtel]). Ici, la longueur est choisie précisément de manière à obtenir un gain optimal.

[question:EG108]

<margin>
[picture:650:e_fuenf_achtel:Antenne $5/8 \lambda$]
</margin>

---

Une antenne Groundplane rayonne elle aussi perpendiculairement au brin rayonnant (et non aux radians). Comme le diagramme de rayonnement considère souvent l'antenne Groundplane vue de dessus, on obtient presque un rayonnement omnidirectionnel, qui présente un gain presque identique dans toutes les directions (cf. figure [ref:e_ground_plane_abstrahlung]). Les radians n'ont qu'une faible influence et peuvent légèrement « cabosser » le diagramme de rayonnement, ce qui correspond à un gain légèrement différent dans certaines directions.

<margin>
[picture:1046:e_ground_plane_abstrahlung:Rayonnement d'une antenne Groundplane]
</margin>

[question:EG216]

<indepth>
Même si le diagramme de rayonnement d'une antenne Groundplane avec radians est légèrement *« cabossé »*, cet écart est en théorie beaucoup plus petit que ce qui est souvent représenté. Une antenne Groundplane est donc effectivement un radiateur omnidirectionnel presque idéal dans le plan.
</indepth>

---

Les antennes directives (par exemple l'antenne Yagi-Uda) se caractérisent par un gain nettement plus élevé dans une direction que dans les autres, comme représenté sur la figure [ref:e_richtantenne_abstrahlung].

[question:EG217]

<margin>
[picture:1047:e_richtantenne_abstrahlung:Rayonnement d'une antenne directive]
</margin>

---

Aux fréquences plus élevées, par exemple dans le domaine UHF ou au-delà, on utilise aussi des cornets ou des antennes paraboliques (cf. [ref:e_parabolantenne]). De même, on trouve des antennes patch sur les circuits imprimés des petits appareils. Toutes ces formes d'antennes sont inhabituelles pour le domaine des ondes courtes, car elles atteindraient des tailles peu maniables. Il ne reste donc, pour les questions suivantes, que l'antenne long-fil, l'antenne Yagi-Uda, l'antenne dipôle, l'antenne Windom et l'antenne Delta-Loop.

[question:EG106]

<margin>
[picture:850:e_parabolantenne:Antenne parabolique]
</margin>

L'antenne à pot de blocage (Sperrtopfantenne) se compose d'un pot de longueur $\lambda / 4$ qui agit comme symétriseur, respectivement comme bloqueur d'ondes de gaine. Avec cette connaissance, la question suivante peut être résolue, car aussi bien un pot de blocage qu'une Yagi-Uda croisée seraient, tout comme un réflecteur parabolique, d'une taille peu maniable dans la bande des $\qty{80}{\meter}$.

[question:EG107]
