Dans la classe E, nous avons déjà fait connaissance avec la capacité d'un condensateur ainsi qu'avec son comportement qualitatif en tension alternative : un condensateur se comporte comme une résistance dépendant de la fréquence. Nous avions d'abord retenu que la réactance capacitive est inversement proportionnelle à la fréquence. Si l'on diminue la fréquence, la réactance $X_C$ augmente. Si l'on augmente au contraire la fréquence, la résistance diminue en conséquence. Le comportement d'un condensateur en tension alternative peut se décrire par la formule de la réactance capacitive $X_C$ :

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

Dans la classe A, nous voulons maintenant examiner ce comportement de plus près et apprendre aussi pourquoi cette résistance est appelée « réactance » (Blindwiderstand). Mais nous devons d'abord encore retenir que la réactance d'un condensateur est aussi négative, pour pouvoir résoudre la question suivante : 

[question:AC102]

<indepth>
Pourquoi la réactance capacitive est-elle négative ? L'arrière-plan se trouve dans le calcul complexe des courants alternatifs, qui n'est pas strictement nécessaire pour l'examen radioamateur.

Pour les lectrices et lecteurs ayant des connaissances en nombres complexes, notons cependant que la représentation correcte de la réactance capacitive s'écrit en fait

$X_C = \frac{1}{j\omega C}$

où $j$ représente l'unité imaginaire $\sqrt{-1}$.

En multipliant haut et bas cette expression par $j$, on obtient :

$X_C = \frac{1}{j\omega C} = \frac{1 \cdot j}{j\omega C \cdot j} =\frac{-j}{\omega C}$

Il en ressort que la réactance capacitive est non seulement négative, mais aussi complexe. Le signe négatif décrit la relation de phase entre courant et tension aux bornes du condensateur, que nous examinerons encore plus précisément dans ce chapitre.
</indepth>

---

Des appareils de mesure modernes et bon marché, que les radioamateurs emploient volontiers de nos jours, sont les analyseurs d'antenne ou les analyseurs de réseau vectoriels (VNA). Ils mesurent la variation de la réactance $X_C$ en fonction de la fréquence et peuvent aussi représenter graphiquement le résultat de la mesure.
La figure [ref:a_kapazitiver_Blindwiderstand] montre la variation de la réactance capacitive (courbe bleue) d'un condensateur Styroflex de $\qty{1500}{\pico\farad}$ dans la plage de fréquences de $\qtyrange{1}{4,5}{\mega\hertz}$. 

<margin>
[photo:248:a_kapazitiver_Blindwiderstand:Réactance capacitive $X_C$ (courbe bleue) et phase (courbe rouge) d'un condensateur Styroflex de $\qty{1500}{\pico\farad}$ dans la plage de fréquences de $\qtyrange{1}{4,5}{\mega\hertz}$.]
</margin>


Essaie maintenant de répondre aux questions suivantes à l'aide de la formule ci-dessus. Fais particulièrement attention aux unités et aux puissances de dix pour obtenir les bons résultats.

[question:AC104]
[question:AC105]
[question:AC106]
[question:AC107]

Dans la question suivante, c'est la capacité qui est cherchée. Essaie pour cela de transformer la formule afin de pouvoir calculer la capacité $C$ :

[question:AC108]

---

Si l'on effectue une mesure simultanée du courant et de la tension aux bornes d'un condensateur avec un oscilloscope à deux voies (cf. [ref:a_strom_eilt_vor]), il apparaît un résultat d'abord surprenant : entre le courant et la tension existe un déphasage de $\qty{90}{\degree}$, le courant étant en avance sur la tension.

Cela signifie que le courant atteint déjà sa valeur maximale alors que la tension est encore en train de monter. Ce comportement caractéristique est une propriété fondamentale des condensateurs et joue un rôle important dans la technique des courants alternatifs, en particulier pour les filtres et les circuits oscillants.
La ligne rouge de la figure [ref:a_kapazitiver_Blindwiderstand] représente la phase de la réactance capacitive, quasi constante à $\qty{-90}{\degree}$.

[question:AC101]

<margin>
[photo:268:a_strom_eilt_vor:Déphasage entre tension et courant aux bornes d'un condensateur]
</margin>

<tip>
Moyen mnémotechnique : au condensateur, le courant court devant — dans un C, I devance U !
</tip>

---

Le déphasage entre tension et courant est donc de $\qty{90}{\degree}$, le courant (rouge) étant en avance sur la tension (bleu), comme le montre la figure [ref:a_blindleistung_kondensator]. Si l'on considère la puissance instantanée avec $P = U \cdot I$, il en résulte une courbe de puissance (verte) qui oscille symétriquement autour de la ligne du zéro, également représentée sur la figure [ref:a_blindleistung_kondensator].

<margin>
[picture:943:a_blindleistung_kondensator:Le produit $U \cdot I$ donne la courbe de puissance verte]
</margin>

La valeur moyenne de cette puissance est nulle, c'est-à-dire qu'aucune puissance active n'est convertie. Au lieu de cela, de l'énergie est périodiquement stockée dans le champ électrique du condensateur puis restituée à la source. C'est pourquoi on parle, pour un condensateur idéal sans pertes, de puissance réactive et de réactance.

Seule une résistance ohmique absorbe de la puissance active, car chez elle tension et courant sont en phase, c'est-à-dire qu'il n'y a pas de déphasage. Cela signifie que tension et courant sont simultanément positifs ou négatifs, de sorte que la puissance instantanée $P = U \cdot I$ est toujours positive.

Une réactance idéale, en revanche, n'absorbe aucune puissance active et ne chauffe donc pas non plus dans le cas idéal. Au lieu de cela, l'énergie est périodiquement stockée puis restituée à la source.

[question:AC111]

[question:AC103]

---

Si un condensateur s'échauffe malgré tout dans des applications haute fréquence, c'est un indice de pertes dans le composant. Un condensateur idéal ne convertirait aucune énergie en chaleur ; les condensateurs réels possèdent cependant des propriétés parasites qui conduisent à des pertes.

Ces pertes se reconnaissent dans le schéma équivalent : la résistance $R_\text{ESR}$ (Equivalent Series Resistance) décrit les pertes ohmiques dans le condensateur, tandis que $R_\text{isolant}$ modélise les pertes dans le diélectrique. S'y ajoute l'inductance parasite $L_\text{ESL}$, qui influence le comportement aux fréquences élevées.

Pour l'évaluation technique de ces pertes, on utilise le facteur de qualité $Q$ (Quality Factor) ainsi que le facteur de pertes $\tan\delta$. Les deux grandeurs décrivent à quel point un condensateur réel s'écarte du comportement idéal.

Entre les deux grandeurs existe une relation directe :

$Q = \frac{1}{\tan\delta}$

À retenir : des pertes élevées conduisent à un faible facteur de qualité $Q$ et donc à un grand facteur de pertes $\tan\delta$. Plus la fréquence est élevée, plus ces pertes se font sentir, car la réactance $X_C$ diminue quand la fréquence augmente, tandis que les résistances parasites restent constantes.

<margin>
[picture:1065:a_ersatzchaltbild_kondensator:Schéma équivalent d'un condensateur réel avec pertes parasites.]
</margin>

---

[question:AC109]

[question:AC110]

<indepth>
Grâce au calcul complexe des courants alternatifs, on peut représenter la réactance $X_C$ avec les pertes parasites $R$ sous forme d'un diagramme de Fresnel : 
[picture:1066:a_tan_delta:$\tan\delta$ dans le diagramme de Fresnel complexe]

La tangente décrit en effet le rapport du côté opposé au côté adjacent, donc dans ce cas les pertes $R$ rapportées à la réactance capacitive sans pertes $X_C$. 

$\tan\delta = \frac{R}{|X_C|}$

Plus les pertes sont grandes, plus l'angle $\delta$ est grand, et donc aussi le facteur de pertes $\tan\delta$. Un condensateur idéal présenterait un angle de $\delta = 0$ degré, puisqu'il n'a pas de pertes.

Par cette addition complexe ou géométrique s'obtient la grandeur $Z$. Elle est appelée *impédance* et décrit la résistance complexe totale d'un composant. Le module de l'impédance $|Z|$ correspond à ce qu'on appelle l'*impédance apparente* (Scheinwiderstand).
</indepth>
