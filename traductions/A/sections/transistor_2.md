Nous avions déjà discuté du transistor bipolaire dans les supports de formation de la classe E. Dans la classe A, nous allons approfondir le sujet et examiner aussi un autre transistor.

Le transistor bipolaire se compose de trois zones semi-conductrices alternativement dopées n et p. Les zones sont désignées comme émetteur, base et collecteur. Dans le *transistor npn*, l'émetteur est dopé n, la base p et le collecteur n. Dans le transistor pnp, il s'agit en conséquence d'un émetteur p, d'une base n et d'un collecteur p. 

La figure [ref:a_bipolartransistor_aus] montre un transistor npn à l'état bloqué.
Dès que la tension base-émetteur $U_\mathrm{BE}$ est appliquée par fermeture de l'interrupteur (typiquement $\approx \qtyrange{0,6}{0,7}{\volt}$ pour le silicium), la diode base-émetteur devient passante. Il circule alors un petit courant de base $I_\mathrm{B}$ (cf. figure [ref:a_bipolartransistor_ein]).

Ce petit courant de base fait que de nombreux électrons sont injectés depuis l'émetteur dans la base, mince. Comme la base est très étroite, la plupart de ces porteurs de charge parviennent jusqu'au collecteur. Ils y sont « aspirés » par la tension collecteur-émetteur $U_\mathrm{CE}$ appliquée ; le courant de collecteur $I_\mathrm{C}$ circule. Il est plus grand que le courant de base d'un facteur $B$, où $B$ est ce qu'on appelle le gain en courant du transistor. Les valeurs typiques de $B$ se situent dans la plage de $\num{20}$ à $\num{500}$.

<margin>
[picture:1071:a_bipolartransistor_aus:Transistor bipolaire NPN à l'état bloqué]
[picture:1072:a_bipolartransistor_ein:Transistor bipolaire NPN à l'état passant]
</margin>

[question:AC503]

Il est recommandé de mémoriser p. ex. le transistor NPN. Pour le PNP, tout est alors inversé.

[question:AC504]

Physiquement, la tension base-émetteur $U_{BE}$ commande le courant de collecteur $I_C$, et ce de manière exponentielle. Pour le transistor npn, on a par exemple :

$I_C = I_S \cdot e^{\frac{U_{BE}}{U_T}}$

$I_S$ est le courant de saturation, qui dépend fortement du type de construction du transistor. Il est à relever dans la fiche technique. $U_T$ est ce qu'on appelle la tension thermique, qui vaut environ $\qty{26}{\milli\volt}$ à température ambiante.

Une différence avec le transistor à effet de champ, examiné plus loin, est que, dans le transistor bipolaire, un courant circule toujours aussi dans l'entrée (la base) : le courant de base $I_B$. Lui aussi dépend exponentiellement de $U_{BE}$, avec un $I_S$ plus petit d'un facteur $B$ que pour le courant de collecteur.

$I_B = \frac{I_S}{B} \cdot e^{\frac{U_{BE}}{U_T}}$

Le facteur $B$ est donc le quotient du courant de collecteur et du courant de base :

$B = \frac{I_C}{I_B}$

Même si le transistor bipolaire est physiquement commandé par $U_\mathrm{BE}$, on le désigne comme *commandé en courant*, parce qu'il ne conduit que lorsqu'un courant de base circule.

[question:AC501]

Un transistor est dit « passant » en « sens direct » lorsqu'un courant de collecteur significatif circule. Pour cela, la diode base-émetteur doit toujours être polarisée en sens direct, donc $U_{BE}$ positive pour les transistors npn et négative pour les pnp. La diode collecteur-base, en revanche, doit être bloquée, car aucun porteur de charge ne doit être injecté du collecteur dans la base.

[question:AC505]

Dans ce qui suit, nous examinons encore quelques circuits simples à base de transistor bipolaire.

---

[question:AC515]

Le point de fonctionnement souhaité est réglé en imposant un courant de base à travers $R_1$. Le courant de base est plus petit que le courant de collecteur du gain en courant donné de $\num{298}$. Aux bornes de la résistance chute la différence entre la tension d'alimentation et le potentiel de base. Le potentiel de base est donné à $\qty{0,6}{\volt}$. Nous calculons donc :

$R_1 = 298 \cdot \frac{\qty{12}{\volt} - \qty{0,6}{\volt}}{\qty{0,005}{\ampere}} \approx \qty{680}{\kilo\ohm}$

<indepth>
Ce circuit a cependant en pratique un inconvénient énorme : le gain en courant d'un transistor bipolaire n'est pas particulièrement bien contrôlé. Prenons comme exemple le populaire BC547B. Son gain en courant peut, selon la spécification, se situer entre $\num{200}$ et $\num{450}$. Le courant de collecteur peut donc, avec ce circuit, s'écarter de la conception de bien plus d'un facteur $2$.
</indepth>

Pour obtenir une meilleure stabilité du point de fonctionnement, le point de fonctionnement du transistor bipolaire est en règle générale réglé par un diviseur de tension. Ce qu'on appelle le courant transversal est le courant qui circule ici à travers $R_2$. Il devrait être au moins dix fois plus élevé que le courant de base, afin que le courant de base n'ait pas une grande influence sur le point de fonctionnement. 

---

[question:AC516]

<indepth>
Ce circuit non plus n'est pas très recommandable du point de vue pratique. D'une part, le courant de collecteur dépend exponentiellement de la tension base-émetteur. Les résistances ont une tolérance qui peut faire dévier quelque peu le potentiel de base de sa valeur de consigne — avec un grand effet sur le courant de collecteur. En outre, la tension de seuil de la diode base-émetteur, avec environ $\qty{-2}{\milli\volt\per\kelvin}$, dépend assez fortement de la température. Ce circuit aura donc une forte dérive en température du courant de collecteur. Cela peut parfois être souhaité, mais il faut le garder à l'œil. Nous ferons encore connaissance avec un circuit contenant une contre-réaction qui stabilise le point de fonctionnement.
</indepth>

Il y a aussi un exercice de calcul pour ce circuit :

[question:AC518]

Le diviseur de tension $R_1$ et $R_2$ règle le potentiel de base, qui, l'émetteur étant à la masse, doit valoir environ $\qty{0,6}{\volt}$. Pour un courant de collecteur de $\qty{2}{\milli\ampere}$ et un gain en courant de $\num{200}$, le courant de base est $\qty{2}{\milli\ampere} / 200 = \qty{10}{\micro\ampere}$. Le courant à travers $R_2$ doit être dix fois le courant de base ; à travers $R_1$ circule $11 \cdot \qty{10}{\micro\ampere} = \qty{110}{\micro\ampere}$. La résistance $R_1$ vaut alors :

$R_1 = \frac{\qty{10}{\volt} - \qty{0,6}{\volt}}{\qty{110}{\micro\ampere}} = \qty{85,5}{\kilo\ohm}$

Le circuit suivant montre un réglage typique du point de fonctionnement pour le transistor bipolaire, tel qu'il est aussi utilisé en pratique.

---

[question:AC517]

<indepth>
C'est un bon circuit, également souvent utilisé en pratique, parce que le courant de collecteur est fixé avant tout par la résistance d'émetteur $R_E$, qui constitue une contre-réaction série :

Si le courant de collecteur $I_C$ monte, le courant d'émetteur $I_E$ monte aussi. Une tension plus grande chute alors aux bornes de la résistance d'émetteur $R_E$. L'émetteur devient donc plus positif. Comme la tension de base reste presque constante grâce au diviseur de tension formé de $R_1$ et $R_2$, la tension base-émetteur $ U_{BE} = U_B - U_E $ diminue.

Une tension base-émetteur plus petite signifie que le transistor devient moins conducteur. Le courant qui avait initialement monté est ainsi de nouveau réduit.

Le circuit s'oppose donc automatiquement aux variations du courant. C'est pourquoi on parle d'une contre-réaction. Si le courant monte, le transistor est un peu « refermé ». Si le courant baisse, le transistor redevient plus conducteur. Le point de fonctionnement du circuit se stabilise ainsi.
</indepth>

Le potentiel de base est fixé par le diviseur de tension $R_1$ et $R_2$. Comme $\qty{1}{\volt}$ doit chuter aux bornes de la résistance d'émetteur $R_E$, le potentiel de base doit valoir $\qty{1,6}{\volt}$. Pour un courant de collecteur de $\qty{2}{\milli\ampere}$ et un gain en courant de $\num{200}$, le courant de base vaut $\qty{10}{\micro\ampere}$. Comme le courant à travers $R_2$ doit être dix fois le courant de base, il circule à travers $R_1$ onze fois le courant de base, donc $\qty{110}{\micro\ampere}$. Aux bornes de $R_1$ chute la différence entre la tension d'alimentation ($\qty{10}{\volt}$) et le potentiel de base, donc $\qty{8,4}{\volt}$. Nous pouvons maintenant déterminer $R_1$ :

$R_1 = \frac{\qty{8,4}{\volt}}{\qty{110}{\micro\ampere}} = \qty{76,4}{\kilo\ohm}$

[question:AC519]

Si, du fait du défaut, $R_1$ n'est parcouru par aucun courant, aucune tension ne chute aux bornes de $R_2$ — la base est au potentiel de la masse. Alors $U_{BE} \geq \qty{0,6}{\volt}$ n'est pas satisfait, et le transistor est sans courant. Comme aucune tension ne chute aux bornes de la résistance de collecteur $R_C$, le potentiel de collecteur monte jusqu'à la tension d'alimentation.

[question:AC520]

Dans le scénario de défaut donné ici, $R_2$ est sans courant. La base est reliée à la tension d'alimentation via $R_1$. Par ce chemin, un courant de base est injecté. Avec le dimensionnement habituel (le courant transversal est dix fois le courant de base régulier), le courant de base est 11 fois plus élevé que le courant de base régulier — le courant de collecteur va monter très fortement, la chute de tension aux bornes de $R_C$ augmente fortement, la tension collecteur-émetteur descend jusqu'à la valeur de saturation d'environ $\qty{0,1}{\volt}$. Le courant de collecteur n'est limité que par $R_C$.

---

Dans le prochain exercice, il s'agit d'un relais commuté par le transistor npn représenté en série (cf. figure [ref:a_relais_schaltung]). Supposons que le transistor soit d'abord passant : un courant circule à travers la bobine du relais, le relais est enclenché.

<margin>
[picture:426:a_relais_schaltung:Circuit de relais avec transistor npn et diode de roue libre]
</margin>

Le transistor se bloque maintenant, le passage du courant s'effondre. La forte variation du courant induit toutefois brièvement dans la bobine du relais une haute tension négative, qui peut conduire à la destruction du transistor.

Pour empêcher cela, nous branchons une diode de roue libre *en parallèle*. Elle est branchée de manière à ne conduire aucun courant en fonctionnement normal (transistor passant) — elle doit donc être montée en sens inverse. La tension négative qui apparaît brièvement à l'effondrement du courant fait passer la diode en sens direct ; la tension qui en résulte est limitée (pour les diodes au silicium) à $\qty{-0,7}{\volt} \ldots \qty{-0,8}{\volt}$.

[question:AC524]

---

Les transistors à effet de champ ont un principe de commande tout à fait différent des transistors bipolaires. Alors que, pour les transistors bipolaires, il faut considérer aussi bien les électrons que les électrons manquants (« trous ») (d'où « bipolaire »), une seule sorte de porteurs de charge est impliquée dans le transistor à effet de champ (« unipolaire »). Il peut s'agir soit d'électrons (*transistor à effet de champ à canal n*), soit de trous (*transistor à effet de champ à canal p*).

Les électrodes du FET, représentées sur la figure [ref:a_fet_schnitt_aus], sont désignées comme suit :

* *Source* : c'est la « source » (angl. source) des porteurs de charge dans le canal. Ne pas se laisser troubler : le sens conventionnel du courant est défini à l'opposé du sens d'écoulement des porteurs de charge !
* *Drain* : c'est l'écoulement (angl. drain) des porteurs de charge dans le canal.
* *Grille* : la grille (angl. gate, « portail ») commande le flux des porteurs de charge dans le canal.

[question:AC512]

Ce qui est commun à tous les transistors à effet de champ (ou *FET*), c'est qu'en fonctionnement normal, aucun courant ne circule dans l'entrée, l'électrode de grille. La commande de la charge dans le canal (la région entre *source* et *drain*) dépend exclusivement de la tension grille-source.

<margin>
[picture:1073:a_fet_schnitt_aus:FET en coupe, non conducteur]
[picture:1074:a_fet_schnitt_ein:FET en coupe, conducteur]
</margin>

Les figures [ref:a_fet_schnitt_aus] et [ref:a_fet_schnitt_ein] montrent la coupe d'un MOSFET à canal n à l'état bloqué et à l'état conducteur. Sur l'image du haut, aucune tension grille-source $U_{GS}$ suffisante n'est appliquée. Entre les régions dopées n de la source et du drain se trouve le substrat dopé p, de sorte qu'aucun canal conducteur n'existe. Le transistor bloque, et aucun courant ne peut circuler entre source et drain.

Si une tension positive par rapport à la source est appliquée à la grille (cf. figure [ref:a_fet_schnitt_ein]), un champ électrique se forme à travers la couche isolante de SiO$_2$. Ce champ attire des électrons à la surface du substrat dopé p, directement sous la grille. Il s'y forme ainsi un canal n conducteur qui relie la source et le drain. Le MOSFET devient conducteur, et un courant peut circuler entre drain et source.

L'important est que la grille est électriquement isolée par la couche d'oxyde. Dans le cas idéal, aucun courant de grille ne circule donc ; le MOSFET n'est pas commandé par un courant de commande, mais par le champ électrique à la grille. C'est pourquoi on le désigne aussi comme un composant *commandé en tension*.

[question:AC502]

[question:AC513]

[question:AC514]

Comme nous l'avions déjà constaté, le FET est un composant *commandé en tension*, dans lequel aucun courant de grille ne circule. La réponse attendue est que la tension grille-source commande la *résistance du canal*. Toutefois, le comportement du canal ne peut être décrit comme une résistance que pour de très petites tensions drain-source ; en ce sens, la réponse est formulée de manière un peu malheureuse. Il serait plus juste de dire : la tension grille-source commande le courant du canal.

---

La ligne verticale symbolise le canal, contacté en haut (drain) et en bas (source). À gauche se voit la grille — la flèche, avec le trait vertical, rappelle une diode. Il s'agit donc d'un FET, plus précisément d'un FET à jonction. La figure [ref:a_fet_overview] montre une vue d'ensemble des différents types de FET avec leurs symboles.

<margin>
[picture:1075:a_fet_overview:Vue d'ensemble des FET avec leurs symboles]
</margin>

[question:AC506]

Les questions suivantes consistent à associer certains types de FET à leur symbole. Pour cela, quelques règles de base :

* Le courant dans le canal peut être porté soit par des électrons, soit par des trous. Nous parlons dans le premier cas d'un *FET à canal n*, dans le second cas d'un *FET à canal p*.
* Nous pouvons aussi distinguer les FET selon qu'un courant circule ou non dans le canal pour une tension grille-source $U_{GS}=0$. Ils sont alors dits soit *normalement passants* (selbstleitend), soit *normalement bloqués* (selbstsperrend). 
* Enfin, nous pouvons distinguer les FET selon que l'électrode de grille est une diode ou une structure de condensateur. Si la grille est une diode, nous parlons d'un FET à jonction. Des exemples en sont le JFET (junction field effect transistor) et le MESFET (metal semiconductor field effect transistor). Dans le MESFET, la diode de grille est une diode Schottky. Dans un *FET à grille isolée*, l'électrode de grille est séparée du canal par un isolant (un diélectrique). La tension appliquée commande la densité de porteurs de charge dans le canal. Si l'isolant est un oxyde, par exemple du dioxyde de silicium, nous parlons aussi d'un MOSFET (metal oxide semiconductor FET). En raison de leur utilisation dans les circuits numériques, les MOSFET sont de très loin les types de transistors les plus fréquents.

La flèche indique s'il s'agit d'un FET à canal n ou à canal p. Comme pour la diode, la flèche pointe vers la cathode, donc la région dopée n. Si la flèche pointe donc vers le canal, il s'agit d'un FET à canal n. Dans le FET à jonction, la grille porte le canal ; dans le FET à grille isolée, la flèche se voit entre le canal et la couche dite bulk, qui se trouve sous le canal et est le plus souvent reliée en interne à l'électrode de source.

Dans le FET à grille isolée, la grille et le canal forment aussi graphiquement un condensateur.

Dans le FET normalement passant, la ligne entre source et drain est continue, tandis qu'elle est interrompue dans le FET normalement bloqué.

[question:AC507]
[question:AC508]
[question:AC509]
[question:AC510]
[question:AC511]

Dans ce qui suit, nous voulons aussi examiner quelques circuits à MOSFET qui s'appuient sur les questions précédentes.

[question:AC521]

Aucun courant continu ne circule dans la connexion de grille d'un MOSFET. Il s'agit donc d'un diviseur de tension *non chargé* et on a :

$U_{GS} = \frac{R_2}{R_1 + R_2} \cdot U_B = \frac{\qty{1}{\kilo\ohm}}{\qty{11}{\kilo\ohm}} \cdot \qty{44}{\volt} = \qty{4}{\volt}$

[question:AC522]

Ici aussi, il s'agit d'un diviseur de tension non chargé. Comme les tensions sont données, le plus simple est de poser :

$\frac{R_2}{R_1} = \frac{\qty{2,8}{\volt}}{\qty{44}{\volt} - \qty{2,8}{\volt}} \rightarrow R_2 = 0,068 \cdot \qty{10}{\kilo\ohm} = \qty{680}{\ohm}$

[question:AC523]

Le MOSFET de puissance est ici complètement passant ; le canal peut être représenté comme une résistance ohmique de (selon l'énoncé) $R_\mathrm{DSon} = \qty{4}{\milli\ohm}$. Il circule un courant de $\qty{25}{\ampere}$. Nous calculons simplement la puissance dissipée d'après la formule de puissance bien connue :

$P_V = I^2 \cdot R_{\mathrm{DSon}} = \qty{2,5}{\watt}$