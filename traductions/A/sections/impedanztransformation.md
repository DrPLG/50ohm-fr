Toutes les antennes ne présentent pas à leur point d'alimentation exactement l'impédance requise pour le raccordement à une ligne d'alimentation ou à un émetteur donné. Si l'impédance s'écarte par exemple des $\qty{50}{\ohm}$ usuels, elle doit être adaptée en conséquence, afin que la puissance HF puisse être transmise avec le moins de pertes possible. L'impédance existante est pour cela *transformée* en une autre impédance, celle que l'on souhaite. C'est ce que l'on appelle la *transformation d'impédance*, ou encore l'*adaptation d'impédance*.

Il existe différentes possibilités pour l'adaptation ou la transformation d'impédance. On emploie fréquemment, par exemple :

* des transformateurs,
* des lignes $\frac{\lambda}{4}$ ou
* des réseaux d'adaptation à bobines et condensateurs.

Nous avons déjà rencontré les transformateurs avec l'antenne alimentée par l'extrémité et son Unun 1:49. Nous examinons donc de plus près, dans ce qui suit, deux autres possibilités : la transformation d'impédance par lignes $\frac{\lambda}{4}$ vue à la section précédente, et l'adaptation par réseaux LC. Revenons d'abord sur les lignes de transformation — peu importe d'ailleurs que nous employions une ligne d'alimentation symétrique ou une ligne coaxiale dissymétrique, la transformation fonctionne dans les deux cas :

Pour une ligne dont la longueur électrique vaut $\lambda/4$, les résistances actives inférieures à l'impédance caractéristique de la ligne deviennent des résistances supérieures à l'impédance caractéristique de la ligne. Inversement, les résistances actives supérieures à l'impédance caractéristique de la ligne deviennent des résistances inférieures à l'impédance caractéristique. On met p. ex. cette propriété à profit pour adapter des antennes à haute impédance à un système à basse impédance ($\qty{50}{\ohm}$).

[question:AG410]
[question:AG409]

Pour une longueur de ligne de $\lambda/2$, l'effet s'annule cependant de nouveau, si bien qu'aucune transformation d'impédance n'apparaît.

[question:AG412]
[question:AG416]

Pour les questions suivantes, rappelons-nous qu'un dipôle demi-onde est alimenté en courant (basse impédance) et qu'un dipôle onde entière est alimenté en tension (haute impédance).

[question:AG413]
[question:AG414]
[question:AG415]

Si l'on souhaite transformer vers une valeur de résistance déterminée, l'impédance caractéristique nécessaire est donnée par la moyenne géométrique de la résistance de charge $Z_\mathrm{A}$ et de la résistance d'alimentation souhaitée $Z_\mathrm{E}$ à l'autre extrémité du câble :

$Z = \sqrt{Z_\mathrm{E} \cdot Z_\mathrm{A}}$

[question:AG417]
[question:AG418]

---

Souvent, des bobines et des condensateurs sont toutefois aussi utilisés pour l'adaptation d'impédance. On rencontre fréquemment ce que l'on appelle le filtre en pi, qui, outre son effet de passe-bas, entraîne une transformation d'impédance. Un tel filtre en pi peut donc également servir de boîte d'accord d'antenne.

<indepth>
*Le nom « filtre en pi »* vient de la disposition des composants dans le schéma, qui rappelle la lettre grecque $\pi$, et n'a rien à voir avec le nombre $\pi$.
</indepth>

[question:AG406]
