Si l'impédance caractéristique d'un câble d'alimentation n'est pas identique à la résistance de la charge, une transformation d'impédance peut également se produire, en plus de l'onde stationnaire qui apparaît. Cela signifie qu'une source de signal « voit », à une extrémité du câble, une résistance différente de celle qui est raccordée à l'autre extrémité.

Deux cas en particulier sont importants : la ligne $\lambda/4$, destinée à une transformation d'impédance délibérée, ainsi que les lignes $\lambda/2$ et leurs multiples, qui n'opèrent aucune transformation d'impédance, indépendamment de leur impédance caractéristique.

Pour une ligne dont la longueur électrique vaut $\lambda/4$, les résistances actives inférieures à l'impédance caractéristique de la ligne deviennent des résistances supérieures à l'impédance caractéristique de la ligne. Inversement, les résistances actives supérieures à l'impédance caractéristique de la ligne deviennent des résistances inférieures à l'impédance caractéristique. On met p. ex. cette propriété à profit pour adapter des antennes à haute impédance à un système à basse impédance ($\qty{50}{\ohm}$).

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
