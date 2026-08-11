Les tensions alternatives sinusoïdales changent continuellement de valeur. Pour mieux les décrire, nous allons examiner ci-dessous trois grandeurs caractéristiques importantes :

1. $\hat{U}$ : la valeur de crête d'une tension alternative
2. $U_\text{SS}$ : la valeur crête à crête
3. $U_\text{eff}$ : la valeur efficace

<margin>
[picture:834:e_wechselspannung_kenngroessen:Les trois grandeurs caractéristiques d'une tension alternative]
</margin>

---

La *valeur de crête* d'une tension alternative $\hat{U}$ correspond à l'amplitude, que nous avons déjà découverte en classe N (cf. figure [ref:e_wechselspannung_kenngroessen]). Elle est notamment importante pour la tenue en tension des condensateurs. La figure [ref:e_spannungsfestigkeit_elkos] montre deux condensateurs électrolytiques à fils sur lesquels est imprimée la tenue en tension admissible. La valeur de crête de la tension appliquée ne doit pas dépasser cette limite, sous peine de destruction du condensateur. On choisit souvent des composants dont la tenue en tension est plus élevée que nécessaire — soit pour des raisons de sécurité, soit pour prolonger leur durée de vie.

<margin>
[photo:198:e_spannungsfestigkeit_elkos:Condensateurs électrolytiques de tenue en tension 16 volts et 25 volts]
</margin>

Une autre grandeur caractéristique est la *valeur crête à crête*. C'est l'écart entre l'amplitude la plus haute et la plus basse. Pour les tensions alternatives sinusoïdales, on a :

$U_\text{SS} = 2\cdot \hat{U}$.
 
[question:EB406]
[question:EB407]

Lorsque ce n'est pas la tension qui importe, mais la puissance des appareils ou la charge thermique des composants et des lignes, la valeur de crête n'est pas d'un grand secours. Pour ce cas, on a défini la *valeur efficace*. La valeur efficace d'une tension alternative correspond à la valeur d'une tension continue qui échaufferait une résistance ohmique de la même manière.

---

Pour les tensions sinusoïdales, la valeur de crête (ou valeur maximale) est environ 1,4 fois plus grande que la valeur efficace (voir figure [ref:e_wechselspannung_kenngroessen]). Le calcul exact conduit à une formule simple :

$U_{eff} = \frac{\hat{U}}{\sqrt{2}}$ ou $\hat{U} = U_{eff} \cdot \sqrt{2}$

Lorsqu'une tension alternative est indiquée par la seule lettre $U$ sans complément, il s'agit en règle générale de la valeur efficace. L'exemple le plus connu est notre tension secteur de $\qty{230}{\volt}$ — il s'agit là aussi de la valeur efficace. La tension de crête est nettement plus élevée, à savoir

$\hat{U} = \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{325}{\volt}$.

<indepth>
La démonstration exacte de cette formule fait appel au calcul intégral et dépasse les connaissances requises pour l'examen radioamateur. Qui est familier du calcul intégral et que cela intéresse pourra en lire la démonstration ici : [Wikipedia](https://50ohm.de/ew)
</indepth>

[question:EB401]

La valeur de $U_\text{SS}$ pour la tension secteur donne alors le double de la valeur de crête :

$ U_\text{SS} = 2 \cdot \qty{230}{\volt} \cdot \sqrt{2} \approx \qty{651}{\volt}$

[question:EB402]

Les deux questions suivantes fonctionnent selon le même principe :

[question:EB403]
[question:EB404]

---

% TODO referenz auf das Leistungskapitel einfügen:

La question suivante interroge indirectement sur la valeur efficace de la tension. Si l'on sait que $\frac{1}{\sqrt{2}} \approx 0,7$, on peut lire directement les deux résultats.

<indepth>
Il est important que la tension continue $\qty{0,7}{\volt}$ aussi bien que la tension continue $\qty{-0,7}{\volt}$ conduisent au même résultat. Cela tient au fait qu'avec une tension négative, le signe du courant change également, ce qui conduit néanmoins à la même puissance — car on a $P = U \cdot I$.
</indepth>

[question:EB405]

D'ailleurs : tout ce qui est écrit ici à propos des tensions alternatives vaut de manière analogue pour les courants alternatifs.
