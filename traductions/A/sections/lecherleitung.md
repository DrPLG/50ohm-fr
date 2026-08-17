Une *ligne de Lecher* est constituée de deux conducteurs parallèles sur lesquels se forment des ondes HF stationnaires, par superposition de l'onde directe et de l'onde réfléchie. Son extrémité peut être soit ouverte (cf. figure [ref:a_lecherleitung_offen]), soit court-circuitée (cf. figure [ref:a_lecherleitung_kurzgeschlossen]). Dans les deux cas apparaissent des répartitions caractéristiques du courant et de la tension, que l'on peut utiliser par exemple pour déterminer la longueur d'onde.

<margin>
[picture:1112:a_lecherleitung_offen:Ligne de Lecher à extrémité ouverte]
</margin>

Sur une ligne de Lecher *ouverte* à son extrémité, aucun courant ne peut circuler au bout de la ligne. Il s'y trouve donc un minimum de courant et, simultanément, un maximum de tension. De la loi d'Ohm

$R=\frac{U}{I}$

il découle qu'en cet endroit le rapport de la tension au courant devient, de façon idéalisée, infiniment grand, soit $R=\infty$. Le courant et la tension sont décalés spatialement l'un par rapport à l'autre de $\frac{\lambda}{4}$ le long de la ligne. À une distance de $\frac{\lambda}{4}$ de l'extrémité ouverte de la ligne se trouve donc un maximum de courant et, simultanément, un minimum de tension. Comme la tension y tend idéalement vers zéro, il vient d'après la loi d'Ohm $R=0$. Tous les $\frac{\lambda}{4}$ suivants, maximum de courant et maximum de tension alternent. Après un trajet de $\frac{\lambda}{2}$, on retrouve la même répartition du courant et de la tension, comme le montre la figure [ref:a_lecherleitung_offen].

---

Sur une ligne de Lecher *court-circuitée* à son extrémité, les deux conducteurs ne peuvent pas présenter de tension différente au bout de la ligne. Il y règne donc $U=0$. Il s'y trouve un minimum de tension et, simultanément, un maximum de courant. Avec $R=\frac{U}{I}$, il vient donc, de façon idéalisée, $R=0$. À une distance de $\frac{\lambda}{4}$ du court-circuit se trouve en revanche un maximum de tension et, simultanément, un minimum de courant. Comme le courant y tend idéalement vers zéro, le rapport $\frac{U}{I}$ devient très grand et l'on a, de façon idéalisée, $R=\infty$. Sur la ligne de Lecher court-circuitée aussi, les maxima de courant et de tension alternent tous les $\frac{\lambda}{4}$. Après un trajet de $\frac{\lambda}{2}$, on retrouve la même répartition du courant et de la tension, comme le montre la figure [ref:a_lecherleitung_kurzgeschlossen].


<margin>
[picture:1111:a_lecherleitung_kurzgeschlossen:Ligne de Lecher à extrémité court-circuitée]
</margin>

La fréquence à laquelle une ligne de Lecher entre en résonance dépend pour l'essentiel de sa longueur. Si la longueur de la ligne change, sa fréquence de résonance change avec elle.

[question:AG320]

Pour une longueur de ligne de $\frac{\lambda}{2}$, la répartition du courant et de la tension se répète intégralement. Une impédance de charge placée au bout de la ligne se retrouve donc à l'entrée de la ligne avec la même valeur.

Un cas particulier spécialement important se présente lorsque la ligne de Lecher possède, à la fréquence considérée, une longueur électrique d'exactement $\frac{\lambda}{4}$. Comme nous l'avons vu sur les répartitions du courant et de la tension, un maximum de courant et un maximum de tension s'échangent sur un trajet de $\frac{\lambda}{4}$. Une impédance élevée s'en trouve donc transformée en une impédance faible, et inversement.

Sur une ligne $\frac{\lambda}{4}$ *ouverte* à son extrémité, l'impédance au bout de la ligne est idéalement infiniment grande. Après un trajet de $\frac{\lambda}{4}$, on trouve en revanche à l'entrée de la ligne un minimum de tension et un maximum de courant. L'impédance d'entrée est donc quasiment nulle ($Z_\mathrm{in} \approx \qty{0}{\ohm}$). Une extrémité de ligne ouverte est ainsi transformée approximativement en un court-circuit par une ligne longue de $\frac{\lambda}{4}$.

---

[question:AG411]

Inversement, une ligne *court-circuitée* à son extrémité présente au bout de la ligne l'impédance $\qty{0}{\ohm}$. Après un trajet de $\frac{\lambda}{4}$, on trouve à l'entrée de la ligne un maximum de tension et un minimum de courant. L'impédance d'entrée y devient donc très grande ($Z_\mathrm{in} \rightarrow \infty$). Un court-circuit au bout de la ligne est ainsi transformé approximativement en un circuit ouvert par une ligne longue de $\frac{\lambda}{4}$.

<indepth>
Le comportement d'une ligne $\frac{\lambda}{4}$ peut aussi se comparer à celui de circuits oscillants. Une ligne $\frac{\lambda}{4}$ ouverte présente à son entrée une impédance très faible et s'y comporte à la manière d'un *circuit oscillant série à la résonance*. Une ligne $\frac{\lambda}{4}$ court-circuitée présente en revanche à son entrée une impédance très élevée et se comporte à la manière d'un *circuit oscillant parallèle à la résonance*.
</indepth>

Dans la section suivante, nous examinerons comment réaliser délibérément des transformations d'impédance à l'aide de lignes $\frac{\lambda}{4}$.
