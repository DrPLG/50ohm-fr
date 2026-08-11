
Examinons dans ce qui suit le fonctionnement du convertisseur A/N de plus près. Nous savons, d'après la leçon sur le théorème d'échantillonnage, que pour pouvoir échantillonner l'information d'un signal sans perte d'information, nous devons échantillonner au moins à un peu plus du double de la fréquence contenue dans le signal à échantillonner. Or, nous recevons en règle générale, par une antenne, toutes sortes de signaux — y compris des signaux situés au-dessus de la fréquence maximale que nous voulons traiter. Que se passe-t-il alors lorsque de tels signaux parviennent au convertisseur A/N ? Rappelons-nous à ce sujet l'exemple de la mouche qui traverse l'image. Ces signaux ne peuvent plus être saisis, faute d'une fréquence d'échantillonnage suffisante, et apparaissent dans nos échantillons sous la forme de fréquences saisies de façon erronée. On les appelle aussi des alias (soit, en gros, des pseudonymes). Un signal situé légèrement au-dessus de la fréquence d'entrée maximale apparaîtrait comme un alias à une fréquence légèrement inférieure à la fréquence d'entrée maximale de notre convertisseur A/N et représenterait donc un signal qui, en réalité, n'existe pas du tout. Pour empêcher cela, nous devons placer, en amont de l'entrée du convertisseur A/N, un filtre anti-repliement (en règle générale un filtre passe-bas ou un filtre passe-bande), de sorte que les fréquences indésirables, susceptibles de conduire à des alias, soient efficacement supprimées avant que le signal n'atteigne le convertisseur A/N.

Le convertisseur A/N a en outre besoin, pour sa tâche, d'un générateur d'horloge, que l'on appelle aussi générateur de fréquence d'échantillonnage, afin de pouvoir produire à intervalles réguliers des échantillons du signal d'entrée, qu'il transmet ensuite sous forme de flux de données numériques aux autres parties d'un montage. La cadence peut être réglée de façon fixe ou être pilotée par des informations de commande provenant p. ex. d'un microcontrôleur.

[question:AF620]

Comme un convertisseur A/N travaille toujours avec un nombre limité de valeurs numériques possibles, susceptibles de représenter la grandeur du signal d'entrée analogique, la saisie des valeurs d'amplitude se fait par échelons. Souvenons-nous de l'exemple précédent du variateur et du commutateur à crans. Du fait que le signal d'entrée analogique ne peut désormais être saisi que par échelons déterminés, il apparaît des erreurs de quantification.

[question:AF607]

Le nombre d'échelons possibles d'un convertisseur A/N est aussi appelé sa résolution. On indique souvent ce nombre en bits ($\unit{\bit}$). Si un convertisseur peut distinguer $\num{256}$ échelons (par exemple de $\num{-128}$ à $\num{+127}$), il a $\qty{8}{\bit}$. Un convertisseur $\qty{16}{\bit}$ peut déjà distinguer $\num{65536}$ échelons. En règle générale, la moitié des valeurs est ici utilisée pour la plage de signal positive et l'autre moitié pour la plage de signal négative.

[question:AF608]

Une autre propriété importante d'un convertisseur A/N consiste à saisir le signal d'entrée le plus exactement possible, en évitant les erreurs dans les intervalles de temps séparant les différents échantillons. Ce qui est déterminant pour cela, c'est un générateur de fréquence d'échantillonnage aussi stable que possible, produisant une cadence temporelle exacte pour le convertisseur A/N. Malheureusement, cela demande souvent techniquement beaucoup d'efforts, si bien qu'il peut toujours subsister une légère différence entre les flancs du signal d'horloge. C'est ce que l'on appelle le jitter (soit, en gros, la gigue). Il en résulte un bruit supplémentaire dans le résultat de l'échantillonnage (le flux de données numériques) du convertisseur A/N.

[question:AF621]

