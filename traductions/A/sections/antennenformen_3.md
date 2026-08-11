Comme nous l'avons déjà appris, un dipôle demi-onde peut aussi être alimenté à l'une de ses extrémités. La résistance d'alimentation est à haute impédance (env. $\qtyrange{2000}{2500}{\ohm}$) pour une longueur de fil de $\lambda / 2$ ou un multiple de celle-ci. Une possibilité d'adaptation est le circuit de Fuchs, déjà évoqué.

[question:AG419]

---

Une autre possibilité est un transformateur ayant un rapport de transformation de $ü = 1:7$. Comme la tension aussi bien que le courant sont multipliés ou divisés par le facteur $\num{7}$, il en résulte pour la résistance une transformation de $1:7^2 = 1:49$, soit $(1 \cdot \qty{50}{\ohm}) : (49 \cdot \qty{50}{\ohm}) = \qty{50}{\ohm} : \qty{2450}{\ohm}$.

<attention>
Pour ce qui est de la *transformation d'impédance* (transformation de la résistance), le rapport de spires d'un transformateur intervient au carré, c'est-à-dire qu'un transformateur ayant un rapport de spires de 1:7 assure une transformation d'impédance de 1:49. Pour les baluns et les ununs, il n'est souvent pas précisé s'il s'agit du rapport de spires ou du rapport d'impédances. Il y a donc un risque de confusion. L'usage est d'indiquer le rapport d'impédances. Pour un transformateur ayant un rapport de spires ($ü$) de 1:7, on parle alors p. ex. d'un unun 1:49.
</attention>

Comme contrepoids, on utilise souvent un court brin de fil (au moins un vingtième de la longueur d'onde) ou une partie de la ligne coaxiale d'alimentation. Un bloqueur d'ondes de gaine (en abrégé MWS) empêche que la suite du câble d'alimentation ne devienne une partie de l'antenne.

[question:AG123]
[question:AG124]

Au lieu d'un circuit de Fuchs ou d'un transformateur, on peut aussi utiliser une ligne bifilaire de longueur $\lambda / 4$. On parle alors d'une *antenne Zeppelin*.

%TODO namensherkunft zeppelin

[question:AG120]

---

Tout comme pour un dipôle demi-onde alimenté en extrémité, une ligne d'alimentation d'impédance caractéristique différente peut également servir à l'adaptation d'autres formes d'antennes. Pour la classe E, nous avons déjà découvert les antennes cadres onde entière, dont la Delta-Loop et l'antenne Quad. Une antenne Delta-Loop dont les côtés sont de même longueur a une impédance d'alimentation d'environ $\qty{100}{\ohm}$. L'insertion d'une ligne $\lambda / 4$ d'impédance caractéristique $\qty{75}{\ohm}$ permet une transformation vers les $\qty{50}{\ohm}$ usuels dans le service amateur.

[question:AG117]

<indepth>
La valeur optimale de l'impédance caractéristique d'une ligne d'alimentation $\lambda / 4$ utilisée pour l'adaptation se calcule par la *moyenne géométrique* des deux impédances, p. ex. $\qty{50}{\ohm}$ et $\qty{100}{\ohm}$, soit $\sqrt{\qty{50}{\ohm} \cdot \qty{100}{\ohm}} \approx \qty{70,7}{\ohm}$.
</indepth>

Si l'on réalise le cadre onde entière sous forme de carré, la longueur de chaque côté doit alors être égale au quart de la longueur d'onde.

[question:AG119]

<attention>
Comme pour le dipôle, la longueur mécanique d'une antenne cadre onde entière diffère de sa longueur électrique. Contrairement au coefficient de vélocité des dipôles, il existe en revanche pour les cadres onde entière, de façon surprenante, un *facteur d'allongement*, c'est-à-dire que l'antenne doit être de quelques pour cent plus longue qu'une longueur d'onde dans l'espace libre.
</attention>

---

Comme les bandes de fréquences présentent des conditions de propagation différentes selon l'heure de la journée, la saison et le moment du cycle solaire, les radioamateurs souhaitent volontiers pouvoir trafiquer sur le plus grand nombre possible de bandes. Deux exemples d'antennes multibandes sont l'*antenne G5RV à deux brins de même longueur* avec une ligne bifilaire, ainsi que l'*antenne Windom à excitation asymétrique* ; des dimensions bien choisies y font apparaître de nombreuses résonances et permettent ainsi une utilisation sur le plus grand nombre possible de bandes radioamateurs.

[question:AG121]
[question:AG122]

---

% TODO: Darstellung von $5/8 \lambda$ prüfen

Le fait qu'une antenne soit résonante ne signifie pas encore qu'elle présente aussi une bonne caractéristique de rayonnement. Il est souvent souhaitable d'obtenir un rayonnement aussi rasant que possible. Pour les antennes verticales excitées par rapport à la terre, une longueur d'env. $5/8 \lambda$ constitue l'optimum.

<indepth>
Un simple fil ayant la terre pour pôle opposé n'est pas résonant à une longueur de $5/8 \lambda$. Les résonances n'apparaissent qu'à $1/4$, $3/4$, $5/4$, etc. Une adaptation est donc nécessaire. On y parvient en règle générale en insérant une bobine, qui allonge la longueur électrique de $5/8$ à $6/8$ (soit $3/4$). On voit souvent de telles bobines sur les antennes destinées à l'automobile.
% TODO: Bild VHF oder CB-KFZ-Antenne
</indepth>

<attention>
L'optimum de $5/8 \lambda$ ne vaut que pour les antennes excitées par rapport à la terre. Si l'on considère par exemple des dipôles alimentés au centre, situés soit dans l'espace libre, soit verticalement, juste au-dessus du sol, l'optimum se situe alors à $5/4 \lambda$.
% TODO: Frage ist falsch, siehe 2. Review von DL9JBE.
</attention>

[question:AG223]
