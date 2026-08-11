Toute installation radioamateur fixe doit, à partir d'une puissance isotrope rayonnée équivalente (EIRP) de $\qty{10}{\watt}$ ou plus, être déclarée à la BNetzA, conformément au § 9 BEMFV. Cela doit être fait avant le début du trafic radio. Le radioamateur doit alors apporter la preuve qu'il respecte les valeurs limites, qu'il a déterminé les distances de sécurité nécessaires à cet effet et qu'elles se situent à l'intérieur de la zone contrôlée. Dans le langage courant, les radioamateurs appellent cela l'*auto-déclaration* (Selbsterklärung).

On ne peut renoncer à une auto-déclaration que si la puissance isotrope rayonnée équivalente (EIRP) est *inférieure* à $\qty{10}{\watt}$ EIRP — et non $\qty{10}{\watt}$ de puissance d'émission, ni $\qty{10}{\watt}$ ERP !

Même sans calcul précis, on voit rapidement que la combinaison de $\qty{6}{\watt}$ de puissance d'émission et d'un gain d'antenne de $\qty{13}{\dBd}$ (facteur $\num{20}$) dans la question suivante dépasse nettement la valeur limite de $\qty{10}{\watt}$ EIRP.

<indepth>
Pour s'exercer, on peut malgré tout le calculer : nous utilisons de nouveau la formule du recueil de formules : 

$P_\mathrm{EIRP} = P_\mathrm{Sender} \cdot 10^{\frac{g_d-a+\qty{2,15}{\dB}}{\qty{10}{\dB}}} = \qty{6}{\watt} \cdot 10^{\frac{\qty{13}{\dBd}+\qty{2,15}{\dB}}{\qty{10}{\dB}}} \approx \qty{197}{\watt}$

Ce calcul se fait aussi de nouveau facilement de tête, en décomposant le gain total en parties judicieuses :
  
$\qty{13}{\dBd} + \qty{2,15}{\dB} = \qty{10}{\dBd} + \qty{3}{\dB} + \qty{2,15}{\dB}$

On obtient ainsi :

$P_\mathrm{EIRP} = \qty{6}{\watt} \cdot 10 \cdot 2 \cdot 1,64 \approx \qty{197}{\watt}$
</indepth>

[question:EK104]
  
Dans les [instructions relatives à la déclaration des installations radioamateur fixes selon le § 9 de la BEMFV](https://50ohm.de/abemfv), il est précisément défini ce qu'il faut entendre par distance de sécurité. La distance de sécurité liée au site décrit la distance requise entre l'antenne de référence et la zone dans laquelle les valeurs limites en vigueur doivent être respectées. Les intensités de champ pertinentes des installations radio fixes environnantes doivent également être prises en compte.

Point important : la distance de sécurité ne se rapporte pas à un point unique de l'antenne, mais à l'ensemble de la structure de l'antenne. En d'autres termes, pour chaque point de l'antenne, il faut s'assurer que les valeurs limites sont respectées au-delà de la distance de sécurité calculée.

[question:EK107]
