Une boucle à verrouillage de phase (PLL) peut par exemple synchroniser un VCO variable et potentiellement instable avec un oscillateur de référence stable (G). Pour cela, elle compare les phases des deux signaux et réajuste le VCO de telle sorte qu'une fréquence de sortie stable soit produite. Dans le service amateur, les PLL sont employées avant tout pour l'élaboration stable et précise des fréquences dans les émetteurs et les récepteurs, par exemple pour le choix du canal, pour la production de fréquences de mélange et pour la synchronisation d'oscillateurs.

Une PLL se compose pour l'essentiel des composants suivants :

* *Comparateur de phase* : compare les phases des signaux du VCO et de l'oscillateur de référence.
* *Filtre passe-bas* : convertit les impulsions produites par le comparateur de phase en une tension continue.
* *VCO* : produit le signal de sortie, dont la fréquence est commandée par la tension continue délivrée par le filtre passe-bas.

[question:AD701]

En option, la PLL peut être complétée par un *diviseur de fréquence*, afin de synchroniser la fréquence du VCO sur des multiples de la fréquence de référence.

<margin>
[picture:45:a_oszillator_pll:Représentation d'une boucle à verrouillage de phase (PLL)]  
</margin>

---

Le comparateur de phase mesure la différence de phase entre les signaux du VCO ($f_\mathrm{out}$) et de l'oscillateur de référence ($f_\mathrm{ref}$). En cas d'écart de phase, il délivre des impulsions correspondant à l'erreur. Ces impulsions sont lissées par le filtre passe-bas et converties en une tension continue proportionnelle. La tension continue produite sert de signal de commande pour le VCO, dont elle réajuste la fréquence de telle sorte que la différence de phase se réduise progressivement à zéro. Lorsque cet état est atteint, on dit que la PLL est « verrouillée » (locked), donc dans un *état stable*. Dans l'état stable de la PLL, les fréquences et les positions de phase des deux signaux sont identiques. On a alors :

$f_\mathrm{ref}=\frac{f_\mathrm{out}}{n}$

La fréquence de sortie est stable et correspond pour l'essentiel à la fréquence de référence ou à ses multiples (selon le rapport de division choisi pour le diviseur de fréquence).

Le principe de fonctionnement apparaît clairement sur un exemple simple, à la figure [ref:a_oszillator_pll]. L'oscillateur de référence délivre au point A une fréquence de $f_\mathrm{ref}=\qty{10}{\mega\hertz}$. La fréquence de sortie du VCO est divisée au point C par le diviseur de fréquence, avec un rapport de division $n=100$. Si la PLL est verrouillée, donc dans l'*état stable*, les fréquences aux points A et B sont égales. Il en résulte, pour la fréquence de sortie :

$f_\mathrm{out}=n\cdot f_\mathrm{ref}=100\cdot\qty{10}{\mega\hertz}=\qty{1}{\giga\hertz}$

Le VCO produit ainsi une fréquence de $\qty{1}{\giga\hertz}$, qui est ramenée par le diviseur de fréquence à $\qty{10}{\mega\hertz}$ et comparée à la fréquence de référence.

<indepth>
Une PLL peut être réalisée en technique analogique, en technique numérique ou sous une forme mixte. Dans les appareils radio, on combine fréquemment des comparateurs de phase et des diviseurs de fréquence numériques avec un filtre de boucle et un VCO analogiques.
</indepth>

[question:AD702]

La précision et la stabilité de la fréquence de sortie de la PLL dépendent en premier lieu de la qualité de l'oscillateur de référence, qui est habituellement un oscillateur à quartz.

[question:AD705]

Pour régler une PLL sur différentes fréquences, on peut agir sur le diviseur de fréquence. Il devient ainsi possible de produire la fréquence de sortie comme un multiple entier de la fréquence de référence. Le plus petit intervalle de fréquence sélectionnable correspond alors à la fréquence de l'oscillateur de référence, car la division ne peut s'effectuer que par pas entiers. Pour un appareil radio FM ayant un pas de canal de $\qty{12,5}{\kilo\hertz}$, on peut donc utiliser une fréquence de comparaison de $\qty{12,5}{\kilo\hertz}$. Si le rapport de division $n$ est augmenté ou diminué d'une unité, la fréquence de sortie varie en conséquence de $\qty{12,5}{\kilo\hertz}$. La PLL peut ainsi être réglée sur chacun des canaux radio.

[question:AD703]

Pour atteindre une fréquence de sortie déterminée à partir d'une fréquence de référence donnée, le facteur de division est choisi de telle sorte que la même fréquence soit présente aux entrées du comparateur de phase. On peut ainsi calculer le rapport de division nécessaire pour la fréquence de sortie souhaitée.

[question:AD704]
