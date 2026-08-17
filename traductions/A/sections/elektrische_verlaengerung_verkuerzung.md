Pour les antennes, nous devons distinguer la longueur *mécanique* de la longueur *électrique*. La longueur mécanique est simplement la longueur réellement mesurable du fil d'antenne ou du brin rayonnant. La longueur électrique décrit en revanche la longueur à laquelle l'antenne agit électriquement à la fréquence considérée. Elle peut notamment être modifiée par des bobines et des condensateurs, sans qu'il faille changer la longueur mécanique du brin rayonnant.

Considérons d'abord les antennes au voisinage de leur résonance fondamentale. Un dipôle demi-onde est à peu près résonant pour une longueur totale de $\lambda/2$, une Groundplane à brin vertical unique à peu près pour une longueur de brin de $\lambda/4$. Si une telle antenne est trop courte pour la fréquence souhaitée, son impédance d'alimentation présente une composante réactive *capacitive*. Une bobine peut compenser cette composante réactive capacitive. On parle alors d'*allongement électrique* de l'antenne. Si l'antenne est en revanche trop longue pour la fréquence souhaitée, son impédance d'alimentation présente une composante réactive *inductive*. Celle-ci peut être compensée par un condensateur. On parle alors de *raccourcissement électrique*. Une bobine allonge donc électriquement une antenne, un condensateur la raccourcit électriquement. La longueur mécanique du brin rayonnant reste ce faisant inchangée.

<margin>
[picture:1134:a_5_8_lambda_strahlung:Diagrammes de rayonnement et répartitions du courant d'antennes verticales sur terre idéale]
</margin>

---

Un exemple intéressant est l'antenne verticale $\frac{5}{8}\lambda$, d'une longueur de $\qty{0.625}{\lambda}$ en équivalent (cf. figure [ref:a_5_8_lambda]). Le brin rayonnant est ainsi mécaniquement environ 2,5 fois plus long que celui d'une Groundplane $\frac{\lambda}{4}$ ordinaire ($\qty{0.25}{\lambda}$). Cette plus grande longueur de brin modifie avantageusement le diagramme de rayonnement vertical, comme le montre la figure [ref:a_5_8_lambda_strahlung] : une plus grande part de la puissance rayonnée est concentrée en direction de l'horizon, et une moindre part est rayonnée vers le haut ou vers le bas. Pour des liaisons terrestres, cela donne en règle générale une portée supérieure à puissance égale. Une longueur de brin d'environ $\frac{5}{8} \lambda$ est optimale pour cet effet : si l'on allonge davantage le brin, davantage de puissance se perd de nouveau vers le haut et vers le bas.

Cette antenne n'est toutefois pas résonante pour la longueur de brin $\frac{5}{8}\lambda=\qty{0.625}{\lambda}$. Pour obtenir la résonance, la longueur de brin devrait être raccourcie à $\frac{\lambda}{2}=\qty{0.5}{\lambda}$, ou allongée à $\frac{3}{4}\lambda=\qty{0.75}{\lambda}$. L'un comme l'autre conduiraient à moins de puissance vers l'horizon. Il est recommandé, en raison de la meilleure concentration, de laisser la longueur de brin à $\frac{5}{8}\lambda$ et d'établir la résonance par voie électrique, autrement dit d'allonger électriquement l'antenne. L'une des possibilités pour cela est une bobine de pied. La bobine fournit une composante réactive inductive, qui compense la composante réactive capacitive du brin $\frac{5}{8}\lambda$. L'impédance ainsi obtenue est très voisine de celle d'une antenne dont la longueur de brin serait $\frac{3}{4}\lambda=\qty{0.75}{\lambda}$.

<margin>
[picture:650:a_5_8_lambda:Antenne verticale $\frac{5}{8}\lambda$]
</margin>

[question:AG106]

---

Inversement, une antenne mécaniquement un peu trop longue au voisinage de sa résonance fondamentale peut être raccourcie électriquement par un condensateur (cf. figure [ref:a_verkuerzung]). Le condensateur fournit une composante réactive capacitive et compense ainsi la composante réactive inductive du brin trop long.

[question:AG107]

<margin>
[picture:563:a_verkuerzung:Antenne verticale avec condensateur de raccourcissement]
</margin>

---

Pour un dipôle également, on peut d'abord estimer d'après sa longueur mécanique si un allongement ou un raccourcissement électrique est nécessaire pour obtenir la résonance fondamentale souhaitée.

[question:AG108]
