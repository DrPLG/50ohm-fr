% TODO: Wenn der Fragenkatalog 4 kommt, dann fallen hier einige Fragen weg! 

Nous avons déjà découvert la résistance électrique en lien avec la loi d'Ohm. Les résistances peuvent être réalisées à partir de différents matériaux. Pour cette raison, on distingue divers matériaux de résistance, par exemple :

- les résistances bobinées
- les résistances à couche de carbone
- les résistances à couche métallique
- les résistances à couche d'oxyde métallique
- ...

<margin>
| l: Résistance | X: Propriété |
| Résistances bobinées | Résistances de forte charge pour basses fréquences |
| Résistances à couche métallique | Faibles tolérances de fabrication et faible dépendance en température, résistances de précision |
| Résistances à couche d'oxyde métallique | Pour les fréquences supérieures à $\qty{30}{\mega\hertz}$ |
[table:e_eigenschaften_widerstaende:Aperçu des propriétés]
</margin>

Dans ce qui suit, nous détaillons ces matériaux — un récapitulatif figure dans le tableau [ref:e_eigenschaften_widerstaende].

Les *résistances bobinées* comptent parmi les formes les plus anciennes de résistances électriques. En raison de leurs propriétés avantageuses — comme une grande capacité de surcharge et un faible coefficient de température — elles sont encore utilisées aujourd'hui. On les appelle souvent aussi résistances à enroulement, car un fil résistif isolé au vernis, par exemple en manganin ou en constantan, est enroulé sur un corps de bobinage en céramique. Une résistance bobinée à enroulement simple agit toutefois toujours aussi comme une bobine et possède donc une inductance relativement élevée. Nous reviendrons plus en détail sur les bobines dans un chapitre ultérieur ; disons d'emblée que cela rend l'impédance de la résistance dépendante de la fréquence. En radiotechnique, ce comportement est en règle générale indésirable. C'est pourquoi les résistances bobinées conviennent surtout comme résistances de forte charge pour le courant continu ou pour des applications à basses fréquences.

%EC101 Hochlast niedrige Frequenz -> Drahtwiderstand
[question:EC101]

Dans les résistances à couche de carbone, une fine couche de carbone est déposée par évaporation sur un support en guise de matériau résistif. Les résistances à couche de carbone sont bon marché, mais présentent une tolérance de fabrication relativement grande.

Dans les *résistances à couche d'oxyde métallique*, le matériau résistif est appliqué en une fine couche sur un matériau support. Ce type de résistance est largement exempt d'inductance et présente une bonne stabilité en température, ce qui le rend particulièrement adapté à un emploi aux fréquences plus élevées, au-dessus de $\qty{30}{\mega\hertz}$.

%EC103 induktionsarm 30Mhz - >Metalloxid
[question:EC103]

Les résistances à *couche métallique* peuvent être fabriquées avec une grande précision, c'est-à-dire avec une faible tolérance de fabrication. Elles conviennent comme résistances de précision. Elles sont indépendantes de la température, mais moins exemptes d'inductance.

%EC102 Präzisionswiderstand >Metallschichtwiderstand
[question:EC102]


Nous avons déjà découvert les antennes artificielles, c'est-à-dire les charges fictives (dummy loads), en classe N. Pour les fréquences élevées (par exemple VHF), il est recommandé de construire une charge fictive de préférence à partir de résistances à couche d'oxyde métallique non enroulées. Pour les fréquences plus basses (par exemple $\qty{50}{\mega\hertz}$ ou $\qty{28}{\mega\hertz}$), des résistances à couche de carbone peuvent toutefois aussi être utilisées. L'essentiel est avant tout que la résistance ne comporte pas d'enroulements, donc pas d'inductance propre, et n'agisse donc pas comme une bobine parasite, car une telle inductance rendrait la valeur de la résistance dépendante de la fréquence — ce qui est justement indésirable pour une charge fictive. La résistance doit toujours valoir environ $\qty{50}{\ohm}$ indépendamment de la fréquence. C'est pourquoi il ne faut _pas_ utiliser de résistances bobinées. La capacité propre devrait elle aussi, pour cette raison, être aussi faible que possible. De plus, les résistances employées doivent être suffisamment résistantes à la température, car elles transforment en chaleur la puissance absorbée.

%EC107 DL
[question:EC107]
%EC104 DL
[question:EC104]

Pour résoudre les questions suivantes, il faut savoir que dix résistances de $\qty{500}{\ohm}$ chacune montées en parallèle donnent ensemble une résistance totale de $\qty{50}{\ohm}$. Nous reviendrons plus en détail sur cette relation dans un chapitre ultérieur, lorsque nous parlerons des montages en série et en parallèle de résistances.

%EC106
[question:EC106]
%EC105 DL
[question:EC105]
