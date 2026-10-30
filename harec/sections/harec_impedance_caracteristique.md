Une ligne de transmission se modélise comme une suite de petites inductances et de petites capacités. L'**inductance linéique** $L'$ (en $\unit{\henry\per\meter}$) et la **capacité linéique** $C'$ (en $\unit{\farad\per\meter}$) fixent son **impédance caractéristique** [index:Impédance caractéristique] :

$Z_0 = \sqrt{\frac{L'}{C'}}$

Elle ne dépend pas de la longueur de la ligne.

<margin>
[picture:1108:harec_modele_ligne:Modèle d'une ligne par inductances et capacités linéiques]
</margin>

<tip>
**Méthode — impédance d'un câble à partir de sa fiche.** Un RG-58 annonce $L' = \qty{0,25}{\micro\henry\per\meter}$ et $C' = \qty{100}{\pico\farad\per\meter}$. On entre les valeurs en unités de base : $\sqrt{\num{0,25} \times 10^{-6} \div (100 \times 10^{-12})} = \sqrt{2500} = \qty{50}{\ohm}$. Le piège est dans les préfixes : micro $= 10^{-6}$, pico $= 10^{-12}$.
</tip>

Elle dépend aussi de la géométrie et de l'isolant, de permittivité relative $\epsilon_\mathrm{r}$ :

* câble **coaxial** (diamètre intérieur du blindage $D$, diamètre de l'âme $d$) : $Z_0 = \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}$ ;
* ligne **bifilaire** (entraxe $a$, diamètre des fils $d$, pour $a/d > \num{2,5}$) : $Z_0 = \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2\cdot a}{d}\right)}$.

Les valeurs usuelles sont $\qty{50}{\ohm}$ (coaxial d'émission), $\qty{75}{\ohm}$ (télévision) et $\num{300}$ à $\qty{600}{\ohm}$ (lignes bifilaires).

Une ligne **fermée sur son impédance caractéristique** est **adaptée** : l'onde n'est pas réfléchie au bout, et le ROS vaut 1.
