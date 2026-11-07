L'**impédance au point d'alimentation** [index:Impédance au point d'alimentation] (ou résistance d'alimentation) est le rapport de la tension au courant à l'endroit où la ligne rejoint l'antenne. Pour que toute la puissance passe, elle doit être égale à l'impédance caractéristique de la ligne, en général $\qty{50}{\ohm}$.

| l: antenne | l: impédance typique |
| dipôle demi-onde au centre, espace libre | $\qty{73}{\ohm}$, environ $\qty{75}{\ohm}$ |
| dipôle demi-onde réel, selon la hauteur | $\num{40}$ à $\qty{90}{\ohm}$ |
| dipôle replié | $\num{240}$ à $\qty{300}{\ohm}$ |
| ground-plane, radians horizontaux | environ $\qty{37}{\ohm}$ |
| ground-plane, radians inclinés à $\qty{45}{\degree}$ | environ $\qty{50}{\ohm}$ |
| demi-onde alimenté en bout | $\num{2000}$ à $\qty{2500}{\ohm}$ |
[table:harec_impedances_antennes:Impédances au point d'alimentation à retenir]

<margin>
[picture:788:harec_impedance_hauteur:Impédance d'un dipôle selon sa hauteur au-dessus du sol]
</margin>

Le sol modifie l'impédance d'un dipôle : près du sol, elle oscille entre $\num{40}$ et $\qty{90}{\ohm}$ selon la hauteur ; à partir d'une longueur d'onde de hauteur, elle se rapproche de la valeur en espace libre. Un dipôle sur un coaxial de $\qty{50}{\ohm}$ présente donc souvent un léger désaccord, sans gravité.

---

**À la résonance**, l'impédance est une **résistance pure** : les réactances de la bobine et du condensateur équivalents s'annulent, courant et tension sont en phase. **Hors résonance**, une réactance s'ajoute :

* en dessous de la résonance, l'antenne est trop courte et **capacitive** ;
* au-dessus, elle est trop longue et **inductive**.

Cette résistance d'alimentation se compose de la **résistance de rayonnement**, qui représente la puissance réellement rayonnée, et de la **résistance de pertes** (fil, isolateurs, sol). Le **rendement** de l'antenne est la part de la puissance qui va au rayonnement : il chute sur les antennes très raccourcies, dont la résistance de rayonnement devient faible devant les pertes.
