Une ligne d'alimentation peut se représenter comme un circuit formé d'une multitude de petites inductances et capacités, comme le montre la figure [ref:a_wellenwiderstand]. De ces inductances dites linéiques $L'$ en $\unit{\henry\per\meter}$ et de ces capacités linéiques $C'$ en $\unit{\farad\per\meter}$ résulte l'impédance caractéristique $Z$ de la ligne. De façon générale :

$Z_0 = \sqrt{\frac{L'}{C'}}.$

<margin>
[picture:1108:a_wellenwiderstand:Impédance caractéristique d'une ligne d'alimentation]

| X: Propriété                 | l: Valeur                             |
| Impédance                    | $\qty{50}{\ohm}$                      |
| Plage de fréquences          | $ < \qty{1}{\giga\hertz}$             |
| Capacité linéique            | $\qty{100}{\pico\farad\per\meter}$    |
| Inductance linéique          | $\qty{0,25}{\micro\henry\per\meter}$  |
| Vitesse de propagation       | $\qty{0,66}{\percent}$                |
[table:a_rg58:Données techniques issues de la fiche d'un câble coaxial RG-58]
</margin>

Le tableau [ref:a_rg58] donne les données techniques d'un câble coaxial RG-58. L'impédance caractéristique vaut $\qty{50}{\ohm}$, la capacité linéique $\qty{100}{\pico\farad\per\meter}$ et l'inductance linéique $\qty{0,25}{\micro\henry\per\meter}$. À partir de ces valeurs, l'impédance caractéristique se calcule avec la formule ci-dessus :

$Z_0 = \sqrt{\frac{\qty{0,25}{\micro\henry\per\meter}}{\qty{100}{\pico\farad\per\meter}}} = \sqrt{2500} = \qty{50}{\ohm}$

Si ces capacités et inductances linéiques ne sont pas connues, le recueil de formules propose des formules fondées sur les dimensions géométriques de la ligne et sur la permittivité relative du diélectrique.

L'impédance caractéristique $Z_0$ d'une ligne bifilaire symétrique dépend p. ex. de l'entraxe des conducteurs ($a$) et de leur diamètre ($d$), ainsi que de la permittivité relative $\epsilon_\mathrm{r}$ du diélectrique situé entre eux. L'équation donnée dans le recueil de formules vaut pour $a/d > 2,5$ :

$Z_0 = \dfrac{\qty{120}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{2\cdot a}{d}\right)}$

Ici, $\ln$ est le logarithme népérien.

[question:AG305]

L'impédance caractéristique $Z_0$ d'une ligne coaxiale dépend du rapport entre le diamètre intérieur du conducteur extérieur ($D$) et le diamètre du conducteur intérieur ($d$), ainsi que du diélectrique situé entre eux. Le recueil de formules nous donne :

$Z_0 = \dfrac{\qty{60}{\ohm}}{\sqrt{\epsilon_\mathrm{r}}} \cdot \ln{\left(\dfrac{D}{d}\right)}$

Ici, $\ln$ est le logarithme népérien et $\epsilon_\mathrm{r}$ la permittivité relative du diélectrique.

[question:AG306]
[question:AG307]

Lorsqu'une ligne est fermée sur son impédance caractéristique, c'est-à-dire lorsqu'on raccorde à l'une de ses extrémités un composant ou une antenne présentant exactement la même résistance que l'impédance caractéristique de la ligne, on parle d'adaptation. Dans ce cas, les ondes ne sont pas réfléchies à cette extrémité du câble.

[question:AG304]
