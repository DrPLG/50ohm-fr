Dans la classe E, nous avons déjà fait connaissance avec le diviseur de tension *non chargé*. Dans la classe A, nous nous occupons du diviseur de tension *chargé*, dans lequel la tension de sortie $U_2$ est chargée par une résistance de charge $R_\mathrm{L}$. Cela signifie que la résistance de charge se trouve en parallèle de la résistance $R_2$, comme on le voit sur le schéma de la figure [ref:a_spannungsteiler_belastet].

<margin>
[picture:199:a_spannungsteiler_belastet:Diviseur de tension chargé]
</margin>

Pour un diviseur de tension chargé, il faut tenir compte du fait que le courant total augmente quand la charge est accrue, c'est-à-dire quand la résistance de charge $R_\mathrm{L}$ devient de plus basse impédance. Le mieux est d'expliquer les effets de la charge sur un exemple concret. Supposons que les résistances $R_1$ et $R_2$ aient chacune une valeur de $\qty{1}{\kilo\ohm}$ et que la tension totale $U_\mathrm{tot}$ soit de $\qty{12}{\volt}$.

Dans le cas non chargé, la résistance vaut $R_\mathrm{L}=\infty$ ; la résistance n'existe donc pas et aucun courant ne peut la traverser. La tension se répartit uniformément sur les deux résistances $R_1$ et $R_2$, c'est-à-dire qu'on peut mesurer $\qty{6}{\volt}$ aux bornes de chaque résistance. La résistance totale vaut $R_{\mathrm{tot}}=\qty{2}{\kilo\ohm}$. Le courant total vaut $I_1 = \frac{U_\mathrm{tot}}{R_{\mathrm{tot}}}=\qty{6}{\milli\ampere}$. Ce courant traverse aussi $R_2$. La puissance dissipée est de même valeur aux bornes des deux résistances : $P_1 = P_2 = \qty{6}{\volt} \cdot \qty{6}{\milli\ampere} = \qty{36}{\milli\watt}$.

Dans le cas chargé, la résistance de charge doit maintenant valoir elle aussi $R_\mathrm{L} = \qty{1}{\kilo\ohm}$. Le montage en parallèle de $R_2$ et $R_\mathrm{L}$ donne une résistance équivalente de $R_\mathrm{par}=\qty{500}{\ohm}$. La résistance totale du diviseur de tension ne vaut alors plus que $R_{\mathrm{tot}}=\qty{1,5}{\kilo\ohm}$. Un diviseur de tension de $\qty{1}{\kilo\ohm}$ à $\qty{500}{\ohm}$ agit maintenant, et la tension totale se répartit en conséquence. $\frac{2}{3}$ de la tension totale ($\qty{8}{\volt}$) peuvent être mesurés aux bornes de $R_1$ et $\frac{1}{3}$ de la tension totale ($\qty{4}{\volt}$) aux bornes de $R_\mathrm{par}$. 

Le courant $I_1$ vaut maintenant $I_1 = \frac{\qty{8}{\volt}}{\qty{1}{\kilo\ohm}}= \frac{\qty{12}{\volt}}{\qty{1,5}{\kilo\ohm}} = \qty{8}{\milli\ampere}$. Ce courant augmente donc. 

La puissance aux bornes de $R_1$ vaut maintenant $P_1 = U_1 \cdot I_1 = \qty{8}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{64}{\milli\watt}$ contre $\qty{36}{\milli\watt}$ dans le cas non chargé. Aux bornes de $R_\mathrm{par}$, la puissance vaut $P_\mathrm{par} = U_\mathrm{par} \cdot I_\mathrm{par} = \qty{4}{\volt} \cdot \qty{8}{\milli\ampere} = \qty{32}{\milli\watt}$ contre $\qty{36}{\milli\watt}$ dans le cas non chargé. Comme les ${32}{\milli\watt}$ se répartissent entre $R_2$ et $R_\mathrm{L}$, la puissance aux bornes de $R_2$ se réduit dans le cas chargé à $P_2 = \qty{4}{\volt} \cdot \qty{4}{\milli\ampere} = \qty{16}{\milli\watt}$.

En résumé : quand on charge un diviseur de tension avec une résistance, le courant $I_1$ augmente. $R_1$ devient ainsi plus chaud et $R_2$ moins chaud. Avec ces connaissances, nous pouvons facilement résoudre la question suivante.

[question:AD115]

Dans la question suivante, nous devons combiner nos connaissances sur le diviseur de tension et sur le montage en parallèle de résistances. Pour cela, nous décomposons l'exercice en étapes : on détermine d'abord la résistance équivalente du montage en parallèle de $R_2$ et $R_\mathrm{L}$. Le circuit peut ensuite être considéré comme un simple diviseur de tension et la tension de sortie $U_2$ en être calculée.

[question:AD114]
