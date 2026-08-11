Dans la classe E, nous avons appris qu'un oscilloscope représente l'évolution temporelle de tensions. Nous pouvons donc vérifier des formes de signaux avec un oscilloscope. 

[question:AI301]

<margin>
[picture:1005:a_impulsbreite:Détermination de la largeur d'impulsion d'un signal rectangulaire non idéal]
</margin>

---

À côté des tensions alternatives sinusoïdales, la technique numérique fait aussi apparaître des tensions rectangulaires. Une évolution de tension exactement rectangulaire ne peut cependant pas exister. Les flancs sont toujours un peu obliques ou déformés. Le temps entre la montée et la descente d'un rectangle, que l'on appelle largeur d'impulsion ou durée d'impulsion, se mesure donc toujours à mi-hauteur, c'est-à-dire à 50 % de la tension. On garantit ainsi que, pour un même signal, tout le monde arrive au même résultat de mesure.

<indepth>
La raison de ces déformations tient aux capacités et inductances inévitables dans les lignes et les composants, qui agissent comme des filtres et atténuent les composantes de haute fréquence d'un signal rectangulaire.
</indepth>

[question:AI303]
[question:EI303]


Les oscilloscopes peuvent représenter des signaux aux fréquences et aux formes les plus diverses. Pour que ces signaux apparaissent stables à l'écran, les oscilloscopes possèdent un dispositif dit de déclenchement (en anglais trigger = « déclencher »). L'appareil surveille alors continuellement le signal d'entrée et démarre l'acquisition exactement lorsqu'une condition définie au préalable est remplie — par exemple lorsque le signal dépasse une certaine tension, appelée tension de déclenchement. À partir de cet instant commencent l'échantillonnage et l'enregistrement des valeurs mesurées, qui sont ensuite représentées sous forme de courbe à l'écran.


Grâce à ce procédé, chaque représentation démarre toujours au même état du signal, de sorte que les signaux périodiques comme les oscillations sinusoïdales ou les impulsions rectangulaires apparaissent comme figés et clairement reconnaissables. Les oscilloscopes numériques peuvent en outre afficher des images uniques, c'est-à-dire « geler » l'écran. Cela facilite l'analyse des signaux non périodiques. La touche prévue à cet effet porte le plus souvent l'inscription SINGLE. On peut par ailleurs superposer plusieurs mesures, par exemple pour rendre visibles les fluctuations temporelles d'un signal (en anglais jitter).

[question:AI302]

%<indepth>
%Abbildung [ref:a_oszilloskop_einzelbild] zeigt ein Einzelbild aus der Musikaufnahme von Abbildung [ref:a_oszilloskop_ueberlagerung]. Es wurde von einem älteren Oszilloskop abfotografiert, das hauptsächlich analog arbeitet und zusätzlich einen kleinen digitalen %Speicher besitzt.
%[photo:222:a_oszilloskop_einzelbild:Einzelbild aus einer Musikaufnahme]
%</indepth>

Toute ligne ne convient pas aux signaux haute fréquence — cela vaut aussi pour la liaison entre l'objet mesuré et l'oscilloscope. On utilise pour cela en règle générale ce qu'on appelle des sondes de mesure (Tastköpfe). Elles établissent la liaison et veillent à ce que le signal soit transmis avec le moins de déformation possible, sans charger fortement le circuit. À cette fin, elles réduisent la tension du signal (p. ex. dans un rapport 10:1), adaptent la résistance et la capacité et contiennent souvent une compensation pour les fréquences élevées.

Une sonde de mesure se compose d'un boîtier en forme de poignée, comparable à un stylo à bille. À sa pointe peuvent être fixés différents crochets ou aiguilles pour contacter le point de mesure. La liaison de masse s'effectue par une pince crocodile (voir figure [ref:a_oszilloskop_messung]). La figure [ref:a_oszilloskop_tastkoepfe] montre trois exemples de telles sondes. Les modèles de qualité sont chers en conséquence, car ils doivent offrir de larges bandes passantes, une déformation minimale du signal et une mécanique précise.

<margin>
[photo:224:a_oszilloskop_messung:Mesure avec une sonde. Entre les diodes D1 et D2 se voit la pointe de touche et, plus à gauche, la pince crocodile pour la liaison de masse.]
</margin>

<margin>
[photo:223:a_oszilloskop_tastkoepfe:Sondes de mesure avec différentes pointes de touche. Les pinces crocodiles ont été retirées pour cette prise de vue.]
</margin>

Les sondes les plus simples relient la pointe de touche directement à l'entrée de mesure. On parle de sondes 1:1, parce que la tension présente à la pointe parvient inchangée à l'oscilloscope. Les sondes pour fréquences élevées sont de construction plus élaborée. Elles divisent la tension d'entrée vers une valeur plus petite, souvent un dixième. Si l'on mesure avec une telle sonde 10:1 une tension de 10 volts, l'écran affiche 1 volt.

<indepth>
Sur certains oscilloscopes, on peut régler le rapport de division de la sonde. La tension réelle est alors affichée à l'écran. Les sondes passives 10:1 contiennent entre autres une résistance de $\qty{9}{\mega\ohm}$ placée sur le trajet du signal. Les oscilloscopes ont en règle générale une résistance interne de $\qty{1}{\mega\ohm}$. Il en résulte un diviseur de tension 10:1. En outre, un petit condensateur variable se trouve dans la sonde ou dans le connecteur. Il sert à adapter la capacité de la sonde et du câble à l'entrée de mesure et se règle de façon qu'un signal rectangulaire apparaisse à l'écran avec le moins de déformation possible. À côté des sondes passives décrites ici, il existe plusieurs autres variantes. Il y a par exemple des sondes avec câble coaxial adapté de $\qty{50}{\ohm}$. Elles conviennent particulièrement bien aux très hautes fréquences, mais n'ont qu'une résistance interne relativement faible. Les versions actives résolvent ce problème en amplifiant le signal directement dans la sonde.
</indepth>