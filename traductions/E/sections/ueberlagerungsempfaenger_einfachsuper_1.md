Nous avons découvert au chapitre précédent le récepteur à détecteur, le plus simple des récepteurs. Le récepteur à détecteur est ce qu'on appelle un récepteur à amplification directe (Geradeaus-Empfänger), que nous connaissons déjà de la classe N. Dans le récepteur à amplification directe, comme le montre la figure [ref:e_geradeausempfänger], le signal est simplement démodulé après réception et, le cas échéant, amplification. Ce concept de récepteur présente toutefois l'inconvénient d'une mauvaise sélectivité (Trennschärfe). Pour l'améliorer, on pourrait combiner plusieurs filtres dans le bloc de filtrage d'entrée (2) afin d'augmenter la sélectivité. Mais il faudrait alors, à chaque changement de fréquence de réception, réajuster tous ces filtres, ce qui est très laborieux. C'est pour cette raison qu'a été développé le *récepteur à changement de fréquence* (Überlagerungsempfänger, cf. figure [ref:ueberlagerungsempfaenger_einfachsuper]), également appelé dans le langage technique *superhétérodyne* ou *superhet*.

<margin>
[picture:736:e_geradeausempfänger:Récepteur à amplification directe]
</margin>

<margin>
[picture:803:ueberlagerungsempfaenger_einfachsuper:Récepteur superhétérodyne avec amplificateurs]
</margin>

---

L'idée du récepteur superhétérodyne est aussi simple que géniale. Au lieu de filtres accordables, on utilise un oscillateur variable (VFO), à l'aide duquel le signal reçu est d'abord transposé sur une fréquence fixe, appelée fréquence intermédiaire $f_z$ (souvent appelée FI, en allemand ZF). Pour cette fréquence intermédiaire fixe, on peut réaliser des filtres très sélectifs et de grande qualité. La figure [ref:ueberlagerungsempfaenger_einfachsuper_filter] illustre ce principe.

<margin>
[picture:913:ueberlagerungsempfaenger_einfachsuper_filter:Récepteur superhétérodyne avec filtres]
</margin>

Le filtre d'entrée ne laisse d'abord passer que la plage de fréquences souhaitée, par exemple la gamme des ondes courtes. Ensuite, un mélangeur transpose le signal d'entrée, avec la fréquence du VFO, sur la fréquence intermédiaire constante, par exemple $\qty{455}{\kilo\hertz}$. Dans l'exemple concret, le VFO peut être réglé entre $\qty{3,455}{\mega\hertz}$ et $\qty{30,455}{\mega\hertz}$ pour pouvoir transposer vers le bas l'ensemble de la gamme des ondes courtes. L'avantage décisif du récepteur superhétérodyne par rapport au récepteur à amplification directe réside précisément dans cette fréquence intermédiaire constante : le filtrage du signal peut être optimisé pour une fréquence fixe, ce qui permet d'atteindre une très haute sélectivité.

---

Comme les filtres n'ont pas besoin d'être accordables, ils peuvent être optimisés de manière ciblée en termes de largeur de bande et de raideur des flancs, par exemple en utilisant des filtres à quartz, céramiques ou numériques. On peut ainsi utiliser, par exemple pour la transmission de la parole (SSB), des filtres d'une largeur de bande d'environ $\qty{2,4}{\kilo\hertz}$ et, pour la télégraphie (CW), des filtres à bande étroite d'environ $\qty{300}{\hertz}$. Des filtres adaptés peuvent également être utilisés pour d'autres procédés de transmission comme l'AM, la FM ou les modes numériques.

Grâce à ce concept, le récepteur superhétérodyne atteint une sélectivité nettement supérieure à celle du récepteur à amplification directe. Un autre avantage est que tous les étages suivants travaillent toujours avec la même fréquence intermédiaire et n'ont donc pas non plus besoin d'être accordables, ce qui simplifie la construction et améliore la qualité de réception.

[question:EF102]

Les récepteurs superhétérodynes peuvent travailler avec une ou plusieurs fréquences intermédiaires. Dans le cas le plus simple, il s'agit d'un récepteur à conversion directe, dans lequel la fréquence intermédiaire est la fréquence BF recherchée. À cette fin, la fréquence de l'oscillateur doit être très proche de la fréquence de réception.

[question:EF208]

Un récepteur superhétérodyne présente cependant aussi quelques inconvénients, en particulier l'apparition de ce qu'on appelle les fréquences images (Spiegelfrequenzen). Cette problématique, ainsi que des concepts de récepteurs plus avancés comme le superhétérodyne à changements de fréquence multiples, ne seront traités en détail qu'en classe A.

<indepth>
L'inventeur du récepteur superhétérodyne ne peut pas être désigné avec certitude. Cela tient notamment au fait que son développement se situe à l'époque de la Première Guerre mondiale, durant laquelle toutes les parties belligérantes travaillaient intensivement à l'amélioration de la radiotechnique. Vers 1918, plusieurs chercheurs se sont penchés indépendamment les uns des autres sur ce principe de fonctionnement, parmi lesquels Edwin Armstrong aux États-Unis, Lucien Lévy en France et Walter Schottky en Allemagne.
  
Le terme hétérodyne, ou superhétérodyne, est un néologisme. Il se compose du latin super (« au-dessus ») ainsi que des mots grecs hetero (« différent ») et dynamis (« force » ou « action »). Ce nom décrit le principe de fonctionnement fondamental du récepteur à changement de fréquence : le mélange de deux signaux de fréquences différentes pour produire une nouvelle fréquence.
</indepth>