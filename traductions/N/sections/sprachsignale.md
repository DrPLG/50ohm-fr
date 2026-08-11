Dans la suite, nous nous intéressons surtout à la modulation de la voix. Il nous faut d'abord comprendre ce qui caractérise la voix. Quand nous parlons, il se produit une multitude de sons graves et aigus, faibles et forts, sous forme d'ondes sonores. Nous appelons cela un *signal vocal*.

Si nous parlons dans un microphone, celui-ci convertit le signal vocal. Les sons graves et aigus, faibles et forts, deviennent des oscillations électriques lentes et rapides, de petite et de grande amplitude. Le signal vocal n'existe plus sous forme d'onde sonore, mais d'oscillation électrique, et peut être traité dans le poste radio.

<webmargin>
[picture:742:n_sprachspektrum:La voix humaine dans le spectre d'amplitude ; à gauche les sons graves, à droite les aigus]
</webmargin>

La figure [ref:n_sprachspektrum] montre un signal vocal typique en spectre d'amplitude. La plage de fréquences de $\qtyrange{0}{20}{\kilo\hertz}$ est représentée. La courbe indique l'amplitude pour chaque fréquence. On voit bien que la voix ne contient pas des fréquences arbitrairement élevées. Pour les transmissions radio, on utilise même souvent une plage de fréquences encore plus restreinte.

[include:spektrum_sprachsignale]

---

<margin>
[picture:730:n_sprachspektrum_symbolisch:Représentation symbolique du spectre audio]
[picture:475:n_sprachspektrum_beispiel:Exemple de spectre audio]
</margin>

La figure [ref:n_sprachspektrum_symbolisch] montre la représentation symbolique d'un spectre vocal. L'axe X représente, de gauche à droite, les différentes fréquences. Les sons graves, de fréquences plus basses, se trouvent plus à gauche que les sons aigus, de fréquences plus hautes, situés plus à droite. L'axe Y représente, de bas en haut, le volume de chaque fréquence — techniquement, nous appelons cela l'amplitude. Plus on monte, plus le son est fort.

La figure [ref:n_sprachspektrum_beispiel] donne un exemple concret. On y lit une plage de fréquences utilisée de $\qtyrange{300}{2700}{\hertz}$. La « largeur » du signal s'appelle d'ailleurs la largeur de bande et s'exprime en hertz ($\unit{\hertz}$). Elle vaut ici $\qty{2700}{\hertz}$ - $\qty{300}{\hertz}$ = $\qty{2400}{\hertz}$.

Nous utiliserons ce signal vocal d'exemple pour moduler des porteuses. Un signal servant à moduler une porteuse s'appelle un *signal modulant*.
