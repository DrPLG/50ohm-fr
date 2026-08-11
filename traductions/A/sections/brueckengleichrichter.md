De par sa simplicité, le redresseur en pont est un montage redresseur fréquemment utilisé. Il nécessite pour cela un transformateur et 4 diodes.

<latexonly>
Sur la figure [ref:a_brueckenlgeichrichter] est représenté un tel redresseur en pont.

<margin>
[picture:965:a_brueckenlgeichrichter:Redresseur en pont]
</margin>
</latexonly>

<webonly>
Dans l'applet ci-contre est représenté un tel redresseur en pont. On peut, pour la polarité représentée de la tension du transformateur $U_a$ respectivement $U_s$, suivre le courant de charge dans son parcours et constater que celui-ci circule toujours dans le même sens à travers la résistance de charge $R$.

<margin>
[include:applet_gleichrichter_2]
</margin>
</webonly>

<tip>
[picture:67:a_brueckenlgeichrichter_2:Disposition des diodes dans le redresseur en pont]
Dans le redresseur en pont, les diodes pointent avec leurs cathodes vers le pôle positif et les anodes vers le pôle négatif. On peut donc retenir : les « barres » des diodes se rejoignent à la sortie positive. Cette disposition ne doit pas être confondue avec un mélangeur en anneau à diodes, que nous découvrirons plus tard. 
</tip>

[question:AD305]

---

Si l'on installe après le redresseur en pont un condensateur de charge $C_L$ et une cellule de filtrage LC (cf. figure [ref:a_netzteil_Ucs]), on obtient ainsi une amplitude plus faible dans la tension continue de sortie pulsée. Nous avons ainsi une alimentation conventionnelle. 

<margin>
[picture:66:a_netzteil_Ucs:Montage redresseur avec filtrage]
</margin>

Avec le redresseur en pont également, le condensateur se charge à la tension de crête $\hat{U}$ de la tension secondaire $U_{\mathrm{sec}}$ du transformateur.

$\hat{U}=U_{\mathrm{eff}}\cdot\sqrt{2}$

Nous devons en outre vérifier si le transformateur présente un rapport de transformation $ü$. Fort de ces connaissances, nous pouvons résoudre l'exercice suivant.

[question:AD306]

<indepth>
[photo:296: Brückengleichrichter Bauformen: Formes de construction de redresseurs en pont]
Il faut prêter attention au marquage des bornes.

1. Redresseur en pont de forte intensité 26 MB 20 A ($\qty{200}{\volt}$, $\qty{25}{\ampere}$) en boîtier métallique pour montage direct sur un dissipateur thermique
2. B80 C 5000/3300 signifie : tension de service maximale $\qty{80}{\volt}$, C charge capacitive max. $\qty{2500}{\micro\farad}$ avec résistance de protection $R = \qty{1}{\ohm}$, courant de charge permanent maximal : $\qty{5000}{\milli\ampere}$ avec dissipateur thermique, $\qty{3300}{\milli\ampere}$ sans dissipateur thermique
3. BY 225 redresseur en pont - boîtier particulier
4. forme de construction ronde d'un redresseur en pont B 80 C 1000
5. B40 C 1500 - il faut prêter attention à l'ordre modifié des bornes
6. FPU 4M ($\qty{1000}{\volt}$, $\qty{4}{\ampere}$)
7. ordre des bornes gravé dans le plastique
</indepth>
