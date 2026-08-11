En classe E, nous avons déjà fait connaissance avec les sources de tension. Nous allons d'abord nous occuper de la source de courant, avant d'examiner plus précisément la résistance interne des sources de tension et de courant.

De façon analogue à la source de tension, une source de courant fait en sorte de fournir autant que possible un courant constant. La figure [ref:a_isource_schematic] montre son schéma équivalent.

<margin>
[picture:1058:a_isource_schematic:Schéma équivalent d'une source de courant, $R_i$ à haute impédance]
</margin>

<indepth>
Examen d'une source de courant constant à l'exemple d'une alimentation de laboratoire :

[photo:298:a_Strombegrenzung:Alimentation de laboratoire avec limitation de courant réglée sur $\qty{500}{\milli\ampere}$]

Une limitation de courant est intégrée aux alimentations de laboratoire, c'est-à-dire que si le courant de charge dépasse une intensité maximale, la tension aux bornes est abaissée de telle sorte que le courant de charge reste constant. Cela correspond à la fonction d'une source de courant constant -- en cas de court-circuit aux bornes de sortie, le courant maximal réglé circule.
</indepth>

Une source de courant constant idéale fournit un courant permanent constant indépendamment de la charge raccordée. En théorie, cela est possible avec une résistance interne infinie. En pratique, les sources de courant ont une résistance interne très élevée.

<margin>
[picture:1018:a_vsource_schematic:Schéma équivalent d'une source de tension]
</margin>

---

La figure [ref:a_vsource_schematic] montre un schéma équivalent d'une source de tension. La résistance interne $R_i$ est en série avec la source de tension idéale et devrait dans le cas idéal être de $\qty{0}{\ohm}$. En pratique, les sources de tension ont une petite résistance interne.

[question:AB201]

Lorsqu'une source de tension réelle est chargée par $R_L$, la tension aux bornes $U_k$ diminue. La raison en est la résistance interne $R_i$ présente dans cette source de tension. Elle crée pour ainsi dire un diviseur de tension. Comme la tension de source $U_q$ vaut à vide, c'est-à-dire sans charge, $U_q=U_L$, on l'appelle aussi tension à vide. 

La résistance interne n'est pas mesurable avec un multimètre, mais on peut la déterminer par le calcul au moyen de la loi d'Ohm (cf. recueil de formules) :

$R_i = \frac{\Delta U}{\Delta I}$

Deux cas de charge sont nécessaires au calcul :
1. À vide, sans charge : $I = \qty{0}{\ampere}$ et $U_L = U_q$
2. Chargée par $R_L$ : nous mesurons $I_L$ et $U_L$

À partir de la variation de tension ($\Delta U = U_q~-~U_L$) aux bornes et de la variation du courant de charge ($\Delta I = I_L~-~\qty{0}{\ampere}$), la résistance interne peut être calculée d'après la formule ci-dessus.

$R_i = \frac{\Delta U}{\Delta I} = \frac{U_q - U_L}{I_L-\qty{0}{\ampere}} = \frac{U_q - U_L}{I_L}$

Fort de ces connaissances, nous pouvons répondre aux questions d'examen suivantes :

[question:AB205]
[question:AB206]
[question:AB207]
[question:AB208]

Récapitulons :

* Les sources de tension doivent présenter une résistance interne très faible $R_i \ll R_L$, dans le cas idéal : $\qty{0}{\ohm}$ ; la tension de sortie reste alors inchangée en charge. Si la tension aux bornes reste constante en charge, on parle d'adaptation en tension.
* Les sources de courant doivent présenter une résistance interne très élevée $R_i \gg R_L$. Cas idéal : $\qty{\infty}{\ohm}$ ; le courant de charge reste alors constant lors d'une variation de la résistance de charge, c'est pourquoi on parle aussi d'adaptation en courant.

[question:AB203]
[question:AB204]

---

Lorsqu'une source de tension doit délivrer la puissance maximale à une charge, on parle d'adaptation en puissance. C'est également important par exemple pour un émetteur, qui doit transmettre le plus de puissance possible à une antenne.

Le transfert de puissance maximal est atteint lorsque

$R_i = R_L$

est vérifié, c'est-à-dire lorsque la résistance interne et la résistance de charge sont égales.

Dans ce cas, la tension de source se répartit uniformément entre la résistance interne et la charge. Il en résulte à la charge le produit maximal de la tension et du courant, et donc la plus grande puissance possible.

La figure [ref:a_Leistungsanpassung] montre la puissance normalisée à la charge en fonction du rapport $R_L/R_i$. Le maximum est atteint exactement pour $R_L/R_i = 1$, c'est-à-dire lorsque la résistance interne et la résistance de charge sont égales. Le rendement n'est cependant que de $\qty{50}{\percent}$ lors de l'adaptation en puissance, car la même puissance est dissipée aussi bien dans la charge que dans la résistance interne.

<margin>
[picture:1077:a_Leistungsanpassung:Adaptation en puissance optimale pour $R_i = R_L$, ici le quotient $\frac{R_L}{R_i}=1$ et la puissance maximale est donc délivrée à la charge. Le tracé est logarithmique.]
[picture:937:a_Leistungsanpassung:Puissance de sortie optimale pour une résistance de charge de $\qty{50}{\ohm}$ avec une résistance interne de $\qty{50}{\ohm}$. Le tracé n'est pas logarithmique.]
</margin>

<indepth>
Les sources de tension alternative, par ex. les générateurs sinusoïdaux, possèdent également une résistance interne, indiquée sur la prise de sortie.
[photo:292:Sinusgenerator 50 Ohm:Générateur sinusoïdal avec une résistance interne de 50 ohms]
</indepth>

% GGF muss das woanders hin? 
<indepth>
La valeur de $\qty{50}{\ohm}$, fréquemment utilisée en technique haute fréquence, est un compromis technique entre le transfert de puissance maximal et des pertes aussi faibles que possible dans les lignes.

Les câbles coaxiaux d'une impédance caractéristique d'environ $\qty{30}{\ohm}$ peuvent transmettre des puissances particulièrement élevées, car le courant est réparti de façon moins concentrée dans le câble. Les câbles d'environ $\qty{77}{\ohm}$ possèdent en revanche les pertes par atténuation les plus faibles et conviennent particulièrement bien à une transmission de signal à faibles pertes.

La valeur de $\qty{50}{\ohm}$, très répandue aujourd'hui, se situe entre les deux optima et constitue un bon compromis entre un transfert de puissance élevé, des pertes modérées et une construction de câble praticable. C'est pourquoi les $\qty{50}{\ohm}$ se sont imposés comme standard en technique radio.

Si un émetteur, un câble et une antenne sont chacun adaptés à $\qty{50}{\ohm}$, la puissance est transmise de façon optimale et les réflexions sur la ligne sont minimisées.

[picture:1078:a_50ohm:50 ohms comme compromis entre le transfert de puissance maximal et des pertes minimales en technique haute fréquence]

Tu sais maintenant aussi pourquoi notre plateforme s'appelle 50ohm.de : nous voulons t'aider à maîtriser les questions d'examen et donc à atteindre la puissance optimale à l'examen 🤓
</indepth>

[question:AG401]
[question:AB202]