Dans la classe E, nous avons déjà fait connaissance avec les convertisseurs et les transverters, qui sont employés dans le service amateur pour ouvrir, avec des appareils existants, des plages de fréquences supplémentaires que ces appareils ne couvrent pas à l'origine. Comme le montre la figure [ref:a_konverter_2], il faut pour cela un oscillateur, un mélangeur et un filtre de bande.  

[question:AF301]

Un problème se pose alors, que nous voulons maintenant approfondir : les bandes radioamateur ont des largeurs différentes. Ainsi, la bande des $\qty{70}{\centi\meter}$, de $\qtyrange{430}{440}{\mega\hertz}$, avec une largeur de $\qty{10}{\mega\hertz}$, est nettement plus large que la bande des $\qty{10}{\meter}$, de $\qtyrange{28}{29,7}{\mega\hertz}$, avec une largeur de $\qty{1,7}{\mega\hertz}$. Il en résulte qu'un convertisseur transposant la plage de fréquences de $\qtyrange{430}{440}{\mega\hertz}$ sur la plage de $\qtyrange{28}{30}{\mega\hertz}$ ne peut pas couvrir la totalité de la largeur de bande des $\qty{70}{\centi\meter}$.

<margin>
[picture:651:a_konverter_2:Convertisseur élévateur pour QO-100]
</margin>

---

C'est pourquoi un convertisseur doit le cas échéant être commutable, comme le montre la figure [ref:a_konverter], afin de pouvoir transposer de plus grandes plages de fréquences. Si l'on veut par exemple transposer une plage de $\qtyrange{436}{440}{\mega\hertz}$, soit $\qty{4}{\mega\hertz}$ de largeur de bande, sur une plage de $\qtyrange{28}{30}{\mega\hertz}$ de $\qty{2}{\mega\hertz}$ (en supposant que la fréquence de l'oscillateur se situe en dessous du signal utile), il faut deux plages de fréquences commutables : la première de $\qtyrange{436}{438}{\mega\hertz}$ et la seconde de $\qtyrange{438}{440}{\mega\hertz}$. 

<margin>
[picture:85:a_konverter:Convertisseur avec commutation de la fréquence de l'oscillateur]
</margin>

<indepth>
Lorsque la fréquence de l'oscillateur se situe en dessous du signal utile, la position de la bande latérale d'un signal SSB (USB/LSB) est conservée.
Si la fréquence de l'oscillateur se situe au-dessus du signal utile, la position de la bande latérale d'un signal SSB est inversée (l'USB devient LSB et inversement).
</indepth>

Pour la première sous-plage, de $\qtyrange{436}{438}{\mega\hertz}$, on peut calculer la fréquence d'oscillateur suivante : 

$f_\mathrm{OSC} = \qty{436}{\mega\hertz}$ - $\qty{28}{\mega\hertz} = \qty{408}{\mega\hertz}$

$f_\mathrm{OSC} = \qty{438}{\mega\hertz}$ - $\qty{30}{\mega\hertz} = \qty{408}{\mega\hertz}$

Pour les deux limites de bande, il vient logiquement une fréquence d'oscillateur de $\qty{408}{\mega\hertz}$.

Pour la seconde sous-plage, de $\qtyrange{438}{440}{\mega\hertz}$, il vient la fréquence d'oscillateur suivante :

$f_\mathrm{OSC} = \qty{440}{\mega\hertz} - \qty{30}{\mega\hertz} = \qty{438}{\mega\hertz} - \qty{28}{\mega\hertz} = \qty{410}{\mega\hertz}$.

Si cette fréquence d'oscillateur est produite par multiplication de fréquence, il faut encore en tenir compte par une division lors du calcul en retour vers la fréquence nécessaire de l'oscillateur à quartz.

Si les $\qty{408}{\mega\hertz}$ et $\qty{410}{\mega\hertz}$ calculés ci-dessus sont obtenus par multiplication par neuf de la fréquence de l'oscillateur à quartz, les deux fréquences de l'oscillateur à quartz s'établissent à $f_\mathrm{quartz,1}=\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ et $f_\mathrm{quartz,2}=\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrondies dans chaque cas).

Fort de ces connaissances, nous pouvons maintenant traiter les exercices suivants.

[question:AF501]
[question:AF502]
