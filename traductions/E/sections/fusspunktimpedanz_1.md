Pour un dipôle demi-onde résonant alimenté au centre dans l'espace libre, l'impédance d'alimentation se situe, de manière idéalisée, à environ $\qty{73,1}{\ohm}$, donc approximativement à $\qty{75}{\ohm}$. Cette valeur est certes déjà de l'ordre de grandeur des $\qty{50}{\ohm}$ souhaités, mais ne coïncide pas exactement avec eux. Si un tel dipôle est exploité directement avec une ligne d'alimentation de $\qty{50}{\ohm}$, il en résulte donc une légère désadaptation. Pour un transfert de puissance optimal, respectivement un SWR aussi bas que possible, une adaptation peut donc être judicieuse même pour un dipôle. Cela vaut en principe aussi pour des hauteurs d'installation d'environ une longueur d'onde ou plus, l'impédance d'alimentation réelle pouvant légèrement varier selon l'épaisseur du fil, l'environnement et la hauteur d'installation, comme nous allons le voir.

<margin>
[picture:788:e_fusspunktimpedanz_dipol:Impédance au point d'alimentation d'un dipôle en fonction de la hauteur d'installation (simulation avec NECPP)]
</margin>

[question:EG207]

En cas d'interaction avec le sol due à une hauteur d'installation plus faible, l'impédance d'alimentation d'un dipôle alimenté au centre se situe dans la plage de $\qty{40}{\ohm}$ à $\qty{90}{\ohm}$, comme représenté sur la figure [ref:e_fusspunktimpedanz_dipol]. 

[question:EG208]
[question:EG209]

Si l'on réalise un dipôle sous forme de dipôle replié, la tension appliquée double et le courant nécessaire est divisé par deux, en raison des sections d'antenne montées en série mais partiellement guidées en parallèle. Cela correspond à un quadruplement de l'impédance d'alimentation. C'est pourquoi un dipôle replié a une impédance au point d'alimentation de $\qtyrange{240}{300}{\ohm}$.

[question:EG210]

---

Pour une antenne Groundplane, en revanche, l'un des brins du dipôle est supprimé et remplacé par une terre de résistance aussi faible que possible. On arrive donc ici à une résistance d'alimentation de $\frac{\qty{73,1}{\ohm}}{2} \approx \qty{37}{\ohm}$, ce qui correspond à la moitié de la résistance d'alimentation d'un dipôle dans l'espace libre. Pour les antennes Groundplane dont les radians sont inclinés vers le bas de $\qty{45}{\degree}$, on obtient, grâce au rayonnement supplémentaire des radians, une résistance d'alimentation d'exactement $\qty{50}{\ohm}$, de sorte qu'aucune adaptation supplémentaire aux câbles coaxiaux usuels n'est nécessaire. C'est pourquoi l'impédance au point d'alimentation d'une Groundplane se situe entre $\qtyrange{30}{50}{\ohm}$.

<indepth>
En cas de mauvaise mise à la terre ou d'interaction avec le sol, une antenne Groundplane peut aussi présenter, même avec des radians posés horizontalement (par exemple à la surface du sol), une résistance d'alimentation supérieure à $\qty{37}{\ohm}$. La résistance supplémentaire résulte alors des pertes dans le sol.
</indepth>

[question:EG211]
