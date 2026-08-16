Pourquoi existe-t-il un réseau de tension alternative à $\qty{230}{\volt}$ ? La tension alternative offre un avantage décisif par rapport à la tension continue : elle se transforme facilement, et avec de faibles pertes, en d'autres valeurs de tension à l'aide de transformateurs. Cela permet une adaptation efficace de la tension pour le transport et l'utilisation.

Grâce à l'auto-induction dans les bobines, on peut, en tension alternative, transférer de l'énergie entre deux bobines, comme le montre la figure [ref:e_netztrafo]. Un nouveau composant apparaît, le *transformateur* (en abrégé *transfo*). Il se compose de deux bobines couplées magnétiquement par un noyau de fer ou de ferrite. Pour distinguer les deux côtés, on parle du côté primaire, de nombre de spires $N_P$, et du côté secondaire, de nombre de spires $N_S$.

<margin>
[picture:1017:e_netztrafo:Symbole du transformateur]
</margin>

<margin>
[photo:239:e_Trafo mit getrennten Wicklungen:Transformateur à enroulements visiblement séparés]
</margin>

Un transformateur sert à convertir une tension alternative élevée, par exemple $\qty{230}{\volt}$, en une 
tension alternative plus basse, par exemple $\qty{13,8}{\volt}$. Un transformateur ne peut transmettre que des tensions alternatives. Si l'on applique indûment une tension continue à un transformateur, celui-ci se comporte comme un court-circuit en raison de la faible résistance ohmique de l'enroulement primaire. Le transformateur peut alors surchauffer fortement et, dans le pire des cas, griller.

---

Le rapport de transformation d'un transformateur s'exprime comme suit :

$m = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Le rapport des nombres de spires correspond donc au rapport des tensions. En transformant cette équation de base, on peut calculer aussi bien les tensions $U$ que les nombres de spires $N$ du côté primaire ou secondaire.

<indepth>
Ces relations valent pour le cas idéal d'un transformateur non chargé, c'est-à-dire le fonctionnement à vide. À vide signifie qu'aucune charge n'est raccordée au côté secondaire.
</indepth>

[question:EC401]

Nous calculons : 

$\begin{align*}m = \frac{15}{1} = 15 &= \frac{\qty{230}{\volt}}{U_S} &\quad\quad\quad &|~\cdot~U_S\\[1.5ex]15 \cdot U_S &= \qty{230}{\volt} &\quad\quad\quad &|~:~15\\[1.5ex]U_S &= \frac{\qty{230}{\volt}}{15} = \qty{15,33}{\volt}\end{align*}$

[question:EC402]

Nous constatons d'abord que $N_P = 5\cdot N_S$ et que $U_P = \qty{230}{\volt}$ sont donnés. On cherche de nouveau la tension $U_S$.

$m = \frac{5\cdot N_S}{N_S} = \frac{\qty{230}{\volt}}{U_S}$ 

Les $N_S$ se simplifient, il ne reste donc que :

$m = 5 = \frac{\qty{230}{\volt}}{U_S}$ 

Nous multiplions les deux membres par $U_S$ et divisons les deux membres par 5.

$U_S = \frac{\qty{230}{\volt}}{5}$ 

Dans la question suivante, on cherche le nombre de spires secondaire. 

[question:EC403]

On donne $N_P=600$, $U_P=\qty{230}{\volt}$ et $U_S=\qty{11,5}{\volt}$. On cherche le nombre de spires secondaire $N_S$.

$\frac{600}{N_S} = \frac{\qty{230}{\volt}}{\qty{11,5}{\volt}}$ 

Cela se simplifie en :

$\frac{600}{N_S} = 20$ 

Nous multiplions les deux membres par $N_S$ et divisons les deux membres par $20$.

$N_S = \frac{600}{20} = 30$

Le transformateur suivant élève la tension de sortie $U_S$ ; le nombre de spires secondaire doit donc être supérieur au nombre de spires primaire.

[question:EC404]

On donne $N_P= 150$, $U_P=\qty{45}{\volt}$ et  $U_S=\qty{180}{\volt}$. On cherche $N_S$.

Nous reportons :

$ \frac{150}{N_S} = \frac{\qty{45}{\volt}}{\qty{180}{\volt}}$

Cela se simplifie en 

$ \frac{150}{N_S} =0,25 $

Nous multiplions de nouveau les deux membres par $N_S$ et divisons les deux membres par $0,25$.

$ N_S= \frac{150}{0,25} = 600$
