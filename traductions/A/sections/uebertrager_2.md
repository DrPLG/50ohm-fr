Dans la classe E, nous avons déjà appris les bases du transformateur. Il se compose de deux bobines couplées magnétiquement par un noyau en fer ou en ferrite. Pour pouvoir distinguer les côtés, on parle du côté primaire avec le nombre de spires $N_P$ et du côté secondaire avec le nombre de spires $N_S$.

Le principe du transformateur repose sur un effet physique fondamental : l'induction électromagnétique. Si le champ magnétique dans une bobine varie — comme c'est le cas lors de l'application d'une tension alternative —, une tension électrique est induite dans une bobine voisine couplée magnétiquement. Conformément à la loi de l'induction, celle-ci est orientée de manière à s'opposer à la cause de sa naissance. On parle donc aussi d'*induction mutuelle*.

[question:AC301]

Dans la classe E, nous avons déjà rencontré la formule du rapport de transformation $ü$ :

$ü = \frac{N_P}{N_S} = \frac{U_P}{U_S}$

Pour les courants, la relation inverse s'applique :

$ü = \frac{N_P}{N_S} = \frac{I_S}{I_P} = \frac{U_P}{U_S}$

Avec cette formule, qui se trouve aussi dans le recueil de formules, la prochaine question peut être résolue :

[question:AC302]

---

Comme les lignes parcourues par un courant ne doivent pas s'échauffer excessivement, pour éviter des dommages à l'isolation ou même l'incandescence du conducteur, une intensité maximale donnée, dépendant de la section du conducteur, ne doit pas être dépassée. Si l'on rapporte l'intensité à la section du conducteur en $\unit{\milli\meter\squared}$, on obtient ce qu'on appelle la densité de courant $S$. Pour les transformateurs, selon les normes applicables, une densité de courant maximale d'environ $\qty{2,5}{\ampere\per\milli\meter\squared}$ ne devrait pas être dépassée.

La formule de calcul s'écrit (voir recueil de formules — mot-clé : capacité de charge des enroulements) :

$I = S \cdot A_\mathrm{fil}$

<unit>
Densité de courant $S = \frac{I}{A} $ en $\unit{\ampere\per\milli\meter\squared}$
</unit>

<indepth>
Selon la VDE, pour des conducteurs en cuivre posés à l'air libre, l'intensité maximale admissible est fixée à $\qty{12}{\ampere}$ pour une section de $\qty{0,75}{\milli\meter\squared}$. Dans les fusibles à fusion, la densité de courant peut atteindre jusqu'à $\qty{3000}{\ampere\per\milli\meter\squared}$.
</indepth>

Essaie maintenant de répondre à la question suivante. Il te faut pour cela la formule de la section d'un conducteur et la formule de la capacité de charge des enroulements. Veille à convertir correctement les unités.

[question:AC307]

---

L'un des domaines d'application les plus importants des transformateurs en technique des hautes fréquences est l'**adaptation d'impédance**. Les transformateurs y sont employés comme transformateurs d'adaptation.

Contrairement aux transformateurs secteur, le noyau de tels transformateurs n'est le plus souvent pas en fer massif, mais en poudre de fer comprimée ou en ferrite. Ces matériaux conviennent mieux aux fréquences élevées et réduisent les pertes.

<indepth>
Par *adaptation*, on entend que l'impédance d'une source (p. ex. un émetteur) est ajustée aussi exactement que possible à l'impédance de la charge (p. ex. une antenne). Ce n'est qu'avec une bonne adaptation que la puissance peut être transmise de manière optimale, sans qu'une partie de l'énergie soit réfléchie.
</indepth>

Un transformateur d'adaptation a donc pour tâche de convertir une impédance donnée en une autre, de sorte que la source et la charge s'accordent aussi bien que possible.

---

Nous trouvons dans le recueil de formules la formule du rapport de transformation $ü$ :

$ü = \sqrt{\frac{Z_p}{Z_s}} = \frac{N_p}{N_s} = \frac{U_p}{U_s}$

En élevant au carré les membres de l'équation, on obtient : 


$ü^2 = \frac {Z_p}{Z_s} = \left(\frac{N_p}{N_s}\right)^2 = \left(\frac{U_p}{U_s}\right)^2$

On y reconnaît que le rapport d'impédances est le carré du rapport de tensions et donc aussi le carré du rapport des nombres de spires. Ou, dit autrement, un rapport de spires donné conduit à un rapport d'impédances quadratiquement plus élevé.

<indepth>
Dérivation de la formule de transformation d'impédance :
$ P_p = P_s$
$U_p \cdot I_p = U_s \cdot I_s$
Pour $U$, insérer la loi d'Ohm : $U = I \cdot R$ ;
$R$ est remplacé par $Z$
$(I_p \cdot Z_p) \cdot I_p = (I_s \cdot Z_s) \cdot I_s$
Former le rapport d'impédances d'un côté :
$ \frac{Z_p}{Z_s} = \frac{{I_s}^2}{{I_p}^2} = ü^2$
Alternativement, pour $I$, insérer la loi d'Ohm :
$I = \frac{U}{R}$
$R$ est remplacé par $Z$
$\frac{U_p}{Z_p} \cdot U_p  = \frac{U_s}{Z_s} \cdot U_s$
Former le rapport d'impédances d'un côté :
$ \frac{Z_p}{Z_s} = \frac{{U_p}^2}{{U_s}^2} = ü^2$
</indepth>

---

Comme exemple, considérons une antenne alimentée en extrémité, que nous étudierons plus précisément dans un chapitre ultérieur. Son impédance d'entrée est d'environ $\qty{2450}{\ohm}$, donc nettement à haute impédance. Elle doit être adaptée à un émetteur avec une impédance de charge de $\qty{50}{\ohm}$.

<margin>
[picture:260:a_endgespeiste_antenne:Antenne alimentée en extrémité avec adaptation d'impédance par un transformateur]
</margin>

Pour la transformation d'impédance de $\qty{50}{\ohm}$ à $\qty{2450}{\ohm}$, le rapport est $Z_p:Z_s = \qty{50}{\ohm}:\qty{2450}{\ohm} = 1:49$. Cela signifie $ü^2 = 1:49$ et donc $ü=\sqrt{1}:\sqrt{49}=1:7$. Cela signifie que le côté primaire ne doit avoir qu'un septième des spires du côté secondaire pour que l'adaptation d'impédance réussisse, p. ex. $N_p=1$ et $N_s=7$. En pratique, on utilise habituellement un rapport de spires de $2:14$ (cf. figure [ref:a_unun]).

<margin>
[photo:332:a_unun:Exemple de transformateur unun avec un rapport de spires de 2 à 14, les côtés primaire et secondaire étant bobinés ensemble en bifilaire (torsadés)]
</margin>

L'exercice suivant correspond pour l'essentiel à l'exemple examiné précédemment. Pour un dipôle alimenté en extrémité, une impédance d'entrée d'environ $\qty{2,5}{\kilo\ohm}$ est indiquée ici. En pratique, cette valeur fluctue cependant, selon l'environnement et le montage, typiquement dans une plage d'environ $\qty{2}{\kilo\ohm}$ à $\qty{3}{\kilo\ohm}$. 
Avec un rapport de spires d'environ $1:7$, une adaptation suffisamment bonne à $\qty{50}{\ohm}$ peut néanmoins en règle générale être obtenue.

[question:AC306]

Essaie maintenant de résoudre par toi-même les questions suivantes avec tes connaissances.

[question:AC305]
[question:AC303]
[question:AC304]