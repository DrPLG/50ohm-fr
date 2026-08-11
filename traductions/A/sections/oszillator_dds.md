La *synthèse numérique directe*, en anglais *Direct Digital Synthesis* ou en abrégé DDS [index:Synthèse numérique directe] [index:DDS], sert à produire des signaux périodiques dont la fréquence se règle très finement. Elle est aujourd'hui fréquemment employée dans les appareils radioamateur modernes, à côté de la synthèse de fréquence par circuits PLL. Un avantage essentiel d'une DDS tient à ce que la fréquence de sortie se règle numériquement avec une très haute résolution. En outre, le passage d'une fréquence à une autre est très rapide, car aucune boucle de régulation n'a besoin de se verrouiller sur la nouvelle fréquence, comme c'est le cas avec une PLL classique.

<margin>
[picture:1082:a_dds_aufbau:Schéma fonctionnel d'une DDS (Direct Digital Synthesizer)]
</margin>

La structure fondamentale d'une DDS est représentée en [ref:a_dds_aufbau]. Un générateur d'horloge produit un signal d'horloge de fréquence fixe $f_\mathrm{horloge}$. À chaque coup d'horloge, un accumulateur de phase [index:DDS:Accumulateur de phase], appelé aussi, de façon simplifiée, compteur d'adresses, augmente sa valeur de phase courante de l'incrément de phase $K$ :

$\varphi_{n+1} = \varphi_n + K$

L'incrément de phase $K$ est également appelé *tuning word*. Il détermine de combien de pas de phase l'accumulateur de phase avance à chaque coup d'horloge. La valeur courante de l'accumulateur de phase sert d'adresse pour une table de valeurs, appelée aussi *table de correspondance* (lookup table). Pour produire une oscillation sinusoïdale, cette table contient les valeurs d'amplitude numériques d'une période complète de sinusoïde. À chaque valeur de phase correspond une valeur d'amplitude, lue dans la table de sinus. La grandeur de l'incrément de phase $K$ détermine la vitesse à laquelle la table de sinus est parcourue, et donc la fréquence du signal de sortie. L'incrément de phase peut par exemple être commandé par un microcontrôleur. Un registre reprend la valeur d'amplitude numérique en synchronisme avec le signal d'horloge et la transmet à un convertisseur N/A. Celui-ci convertit la suite des valeurs d'amplitude numériques en un signal analogique, d'abord en escalier. Un filtre passe-bas placé en aval élimine les composantes indésirables de haute fréquence et lisse le signal de sortie.

---

L'exemple suivant le rend concret. Pour un incrément de phase $K=1$, la valeur de phase est augmentée d'exactement un pas à chaque coup d'horloge ($\varphi_{n+1} = \varphi_n + 1$). La table de sinus est ainsi parcourue pas à pas. Lorsqu'une période complète a été produite, le compteur d'adresses est remis à zéro et l'accumulateur de phase repart du début. Le signal de sortie qui en résulte est représenté en [ref:a_dds_phaseninkrement_k1].

<margin>
[picture:1083:a_dds_phaseninkrement_k1:Signal de comparaison]
</margin>

---

Si l'incrément de phase est doublé à $K=2$, la valeur de phase augmente de deux pas à chaque coup d'horloge ($\varphi_{n+1} = \varphi_n + 2$). Une valeur de phase sur deux seulement est ainsi appelée, et la table de sinus est parcourue deux fois plus vite. La période du signal de sortie est divisée par deux et sa fréquence est doublée. C'est ce que montre [ref:a_dds_phaseninkrement_k2].

<margin>
[picture:1084:a_dds_phaseninkrement_k2:Incrément de phase doublé et fréquence de sortie doublée]
</margin>

[question:AD620]

<indepth>
Si l'accumulateur de phase a une largeur de $N$ bits, il peut représenter $2^N$ valeurs de phase différentes. Lorsque la valeur maximale est dépassée, le compteur déborde et recommence au début :

$\varphi_{n+1} = \left(\varphi_n + K\right) \bmod 2^N$

Ce débordement correspond au passage de $\qty{360}{\degree}$ à $\qty{0}{\degree}$. L'incrément de phase $K$ peut être choisi de façon quasiment quelconque et n'a pas besoin d'être une puissance de deux. Il est ainsi possible de produire aussi des fréquences de sortie qui ne sont pas des sous-multiples entiers de la fréquence d'horloge.

Une DDS n'est en outre pas limitée aux oscillations sinusoïdales. Si la table de valeurs contient par exemple les valeurs d'amplitude d'une oscillation triangulaire ou en dents de scie, la DDS peut également produire ces formes de signal.

La qualité du signal de sortie dépend avant tout de la stabilité et de la gigue [index:Jitter] du générateur d'horloge, ainsi que de la résolution et de la linéarité du convertisseur N/A. Le nombre limité de valeurs de phase et d'amplitude engendre des erreurs de quantification et des composantes spectrales supplémentaires. Un filtre passe-bas placé en aval supprime une grande partie de ces composantes indésirables.
</indepth>
