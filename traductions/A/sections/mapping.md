Dans le cadre du traitement numérique du signal, le *mapping* désigne l'étape au cours de laquelle les données numériques sont converties en points de signal spécifiques (les symboles), qui peuvent être émis par le système de transmission. C'est un processus déterminant de la modulation, en particulier pour les modulations d'amplitude en quadrature (QAM) et les modulations par déplacement de phase telles que la QPSK (Quadrature Phase Shift Keying).

Pour visualiser les symboles, nous utilisons un *diagramme de constellation* comme celui de la figure [ref:a_konstellation], qui représente les points de signal possibles dans un espace à deux dimensions. On désigne souvent les axes par In-Phase (I) et Quadrature (Q). Chaque point du diagramme représente une amplitude et une phase déterminées, associées par le mapping à une combinaison de bits déterminée, comme le montre la figure [ref:a_qpsk].

<margin>
[picture:1060:a_konstellation:Diagramme de constellation]
</margin>

---

Examinons dans un premier temps la QPSK sur la figure [ref:a_qpsk] : en QPSK, les bits sont regroupés deux par deux en un symbole. Comme nous avons deux bits par symbole, il en résulte quatre combinaisons possibles ($\num{00}$, $\num{01}$, $\num{10}$, $\num{11}$). Chacune de ces combinaisons est associée à un point de signal spécifique, représenté par une phase déterminée.

<margin>
[picture:1059:a_qpsk:Diagramme I-Q d'un mapping QPSK]
</margin>

---

En QPSK, chaque symbole possède sa propre phase. Les phases sont typiquement définies par pas de $\qty{90}{\degree}$ et associées (« mappées ») aux quatre combinaisons de bits possibles, par exemple :

- $\num{11}$ correspond à $\qty{45}{\degree}$
- $\num{01}$ correspond à $\qty{135}{\degree}$
- $\num{00}$ correspond à $\qty{225}{\degree}$
- $\num{10}$ correspond à $\qty{315}{\degree}$

L'amplitude des signaux reste ici constante, et l'information est transmise exclusivement par la position de phase. C'est pourquoi les quatre points du diagramme de constellation de la QPSK se situent sur un cercle. 

<indepth>
À strictement parler, il existe aussi d'autres façons d'associer les phases aux combinaisons de bits, pour autant qu'elles soient univoques. Le mapping présenté ici n'est qu'un exemple. Dans l'exemple montré ici, les associations ont été choisies de sorte que peu de bits changent entre symboles voisins. Cela présente l'avantage que peu d'erreurs sur les bits apparaissent sous l'effet du bruit. On utilise pour cela le code de Gray, qui trouve son application dans la plupart des procédés de transmission numériques.
</indepth>

---

Chacun de ces points représente un symbole. Le récepteur peut déterminer, à partir de la position de phase, quelle combinaison de bits a été émise. Le diagramme de constellation de la QPSK montre quatre points de signal à angle droit les uns des autres, correspondant aux quatre phases utilisées. La grande séparation entre les différentes phases permet un décodage fiable, même dans des conditions bruitées.

Si, en plus de la phase, on fait aussi varier l'amplitude, on parle de modulation d'amplitude en quadrature (QAM). En QAM, l'amplitude comme la phase sont modifiées, afin de transmettre davantage de bits par symbole. Par exemple, en 16-QAM, chaque symbole peut représenter quatre bits, ce qui conduit à 16 points de signal possibles dans le diagramme de constellation. Un exemple de mapping 16-QAM est présenté à la figure [ref:a_qam].

<margin>
[picture:1061:a_qam:Diagramme I-Q d'un mapping 16-QAM]
</margin>