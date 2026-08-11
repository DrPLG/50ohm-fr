Pour calculer les fréquences d'oscillateur nécessaires dans les transverters, la connaissance des fréquences d'entrée et de sortie souhaitées est indispensable. Il faut en outre savoir si l'oscillateur doit se situer en dessous ou au-dessus du signal utile.

<indepth>
Lorsque la fréquence de l'oscillateur se situe en dessous du signal utile, la position de la bande latérale d'un signal SSB (USB/LSB) est conservée.
Si la fréquence de l'oscillateur se situe au-dessus du signal utile, la position de la bande latérale d'un signal SSB est inversée (l'USB devient LSB et inversement).
</indepth>

Exemple de calcul :

Si la fréquence de l'oscillateur se situe en dessous du signal utile, alors à la fréquence supérieure du signal utile correspond aussi la fréquence supérieure du signal de sortie du convertisseur/transverter.

Si par ex. une plage de fréquences de $\qtyrange{438}{440}{\mega\hertz}$ doit être transposée sur une plage de fréquences de $\qtyrange{28}{30}{\mega\hertz}$ (en supposant que la fréquence de l'oscillateur se situe en dessous du signal utile), on a besoin d'une fréquence d'oscillateur de $\qty{440}{\mega\hertz} - \qty{30}{\mega\hertz}$ ou $\qty{438}{\mega\hertz} - \qty{28}{\mega\hertz}$, ce qui donne dans les deux cas $\qty{410}{\mega\hertz}$. Si cette fréquence d'oscillateur est produite par multiplication de fréquence, il faut encore en tenir compte par une division lors du calcul en retour vers la fréquence nécessaire de l'oscillateur à quartz.

Il en va de même pour la plage de fréquences de $\qtyrange{436}{438}{\mega\hertz}$, si celle-ci doit à nouveau être transposée sur une plage de fréquences de $\qtyrange{28}{30}{\mega\hertz}$ (également en supposant que la fréquence de l'oscillateur se situe en dessous du signal utile).
Il en résulte, par le calcul $\qty{438}{\mega\hertz}$ - $\qty{30}{\mega\hertz}$ respectivement $\qty{436}{\mega\hertz}$ - $\qty{28}{\mega\hertz}$, une fréquence d'oscillateur de $\qty{408}{\mega\hertz}$.

Si les $\qty{408}{\mega\hertz}$ respectivement $\qty{410}{\mega\hertz}$ calculés ci-dessus sont obtenus par multiplication par neuf de la fréquence de l'oscillateur à quartz, les deux fréquences de l'oscillateur à quartz s'établissent à $\frac{\qty{408}{\mega\hertz}}{9} = \qty{45,333}{\mega\hertz}$ et $\frac{\qty{410}{\mega\hertz}}{9} = \qty{45,556}{\mega\hertz}$ (arrondies dans chaque cas).

[question:AF501]
[question:AF502]

%TODO: Die Frage 1472 gehört aus unserer Sicht nicht hier her, da es sich um einen Sender handelt und diese Frage nichts mit Konvertern oder Transvertern zu tun hat. Müsste evtl. in das Kapitel Sender und Senderstufen verschoben werden
[question:AF301]