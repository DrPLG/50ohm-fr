L'idée fondamentale de la télégraphie Morse — transmettre les caractères d'un texte un à un — s'appelle la télégraphie, et elle n'a cessé d'être perfectionnée. Une étape marquante fut de raccorder des téléscripteurs aux postes radio au moyen d'un modem. Le radiotélétype était ainsi inventé, permettant d'émettre et de recevoir des textes de façon automatisée par radio. L'abréviation RTTY, de l'anglais radio teletype, sert encore aujourd'hui à le désigner. De nos jours, la tâche du radiotélétype est en général assurée par l'ordinateur. On peut ainsi, à côté du procédé RTTY classique, utiliser bien d'autres procédés de transmission numériques, également appelés digimodes.

<indepth>
Un *téléscripteur* est un appareil servant à transmettre des messages sous forme de texte au moyen de signaux électriques.
</indepth>

<margin>
[photo:92:n_computersteuerung_funkfernschreiber:Radiotélétype]
</margin>

---

Il faut d'abord relier un ordinateur approprié au poste radio. Dans le cas le plus simple, la liaison peut se faire directement par la prise audio ou l'interface USB. On a fondamentalement besoin d'une liaison audio et, le cas échéant, de signaux de commande. La figure [ref:n_computersteuerung_verbindungen] présente quelques variantes. Une prise de signaux de commande fréquente sur les émetteurs-récepteurs est l'interface dite CAT. CAT signifie Computer Aided Tuning ou Computer Aided Transceiver. Par cette interface, tu peux commander l'émetteur-récepteur et interroger des valeurs, par exemple la fréquence, la puissance d'émission et l'état du PTT.

<margin>
[picture:630:n_computersteuerung_verbindungen:Exemples de liaisons entre l'ordinateur et le poste radio]
</margin>

La liaison entre l'ordinateur et l'émetteur-récepteur peut toutefois entraîner des perturbations des signaux transmis ou des réactions du poste sur le PC. Différentes interfaces digimode, comme solution matérielle, simplifient le raccordement et intègrent des mesures contre ce genre de problèmes. On peut aussi utiliser de telles interfaces à d'autres fins, par exemple pour le trafic à distance ou pour enregistrer le trafic avec le logiciel adéquat. Pour certains procédés, il existe aussi des modems matériels, où la conversion entre données et signaux audio se fait dans un appareil dédié.

[question:NF114]
[question:NF116]

Il existe encore d'autres effets indésirables. L'ordinateur pourrait passer en émission de façon inattendue, ou émettre les sons de notification d'autres programmes en cours. On entend parfois, par exemple, des radioamateurs émettre par mégarde le son de démarrage de leur système d'exploitation. Si le poste émet de façon inattendue, cela peut mettre en danger des personnes en train de travailler sur l'installation d'antenne ou se trouvant par hasard à proximité immédiate.

[question:NF117]

---

Pour certains procédés de transmission, la prise microphone du poste est inadaptée, car les étages d'amplification et de filtrage qui suivent sont optimisés pour la voix et traitent différemment les sons aigus et graves. C'est pourquoi les postes disposent souvent d'une prise de données analogique dédiée, étiquetée par exemple DATA ou 9600. L'utilisation de cette prise spéciale permet de contourner certains étages d'amplification et de filtrage et de transmettre les signaux avec le moins de distorsion possible.

<indepth>
La désignation *9600* vient de ce que cette prise a été introduite pour le Packet-Radio, jadis très utilisé, afin de transmettre les données à $\qty{9600}{\baud}$. Aujourd'hui, la prise sert p. ex. à la transmission numérique de la voix, parfois aussi à plus grande vitesse.
</indepth>

[question:NF115]
