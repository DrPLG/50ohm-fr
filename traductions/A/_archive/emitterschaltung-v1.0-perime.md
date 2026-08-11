La dénomination du montage fondamental d'un transistor bipolaire dépend de la borne (base, collecteur ou émetteur) qui est traversée en commun par le signal d'entrée et le signal de sortie.

Dans le *montage émetteur commun*, le signal d'entrée circule de la source via la base, l'*émetteur* et la masse pour revenir à la source. Le signal de sortie circule du collecteur à travers la charge (puits) et via la masse pour revenir dans l'*émetteur*.

[question:AD409]

%TODO: Schaubild mit Stromläufen evtl. einfügen.

Fonctionnement d'un amplificateur en montage émetteur commun :

%TODO: Bild Emitterschaltung mit Spannungsteiler und Koppelkondensatoren einfügen

Pour le fonctionnement en amplificateur de tension linéaire, le transistor en montage émetteur commun a besoin d'un point de fonctionnement défini (BIAS), qui est normalement fixé par un diviseur de tension à la base.

[question:AD411]

La résistance de collecteur convertit le courant qui traverse le trajet collecteur-émetteur en une chute de tension, prélevée au collecteur. Le courant de collecteur du transistor circule (avec la composante de courant de base, normalement négligeable) via l'émetteur à travers la résistance d'émetteur vers la masse. Le courant qui traverse la résistance d'émetteur provoque, par la chute de tension qui en résulte, une élévation du potentiel d'émetteur (tension d'émetteur) et agit donc comme une contre-réaction pour la tension de base. Le point de fonctionnement du transistor s'en trouve en outre stabilisé, car les variations du courant de collecteur d'origine thermique sont ainsi régulées.

Afin de maintenir la contre-réaction aussi faible que possible pour l'amplification des signaux de tension alternative, la résistance d'émetteur est shuntée de façon capacitive (par un condensateur).

[question:AD413]

L'injection et le prélèvement des signaux à la base et au collecteur s'effectuent via des condensateurs dits de liaison. Ceux-ci ont pour tâche de tenir éloignées de l'étage amplificateur les composantes continues, qui conduiraient à une modification du point de fonctionnement.

[question:AD412]

Le condensateur de découplage placé sur la tension de service (+) sert à évacuer les signaux HF et BF indésirables, afin d'éviter les effets de réaction sur l'étage et sur la tension d'alimentation.

Le déphasage entre le signal d'entrée et le signal de sortie est, pour le montage émetteur commun, de $\qty{180}{\degree}$, car lors d'une alternance positive de la tension d'entrée, le courant de collecteur augmente et donc la chute de tension aux bornes de la résistance de collecteur croît. La tension aux bornes du condensateur de sortie diminue ainsi. Il en résulte une alternance négative à la sortie de l'étage amplificateur.

[question:AD407]
[question:AD408]

Lorsqu'un montage émetteur commun est exploité, comme dans la question suivante, sans préréglage du point de fonctionnement par un diviseur de tension, la commande du transistor s'effectue uniquement par le signal d'entrée appliqué. Ce n'est que lorsque celui-ci dépasse la valeur d'env. $\qty{0,6}{\volt}$ que le trajet base-émetteur du transistor devient passant. De ce fait, un courant de collecteur ne circule que dans les crêtes de tension, ce qui provoque une chute de tension à la sortie. Comme signal de sortie apparaît la tension d'alimentation, qui chute aux instants où le transistor entre dans la zone conductrice. C'est ainsi que s'explique le signal de sortie correspondant.

[question:AD406]

Le gain en tension du montage émetteur commun se situe, pour un dimensionnement approprié, dans la plage de $100\dots 300$ et est donc élevé. Si l'on retire cependant le condensateur d'émetteur, le facteur d'amplification du montage diminue considérablement. Il n'est en fin de compte plus défini que par le rapport de la résistance de collecteur à la résistance d'émetteur.

[question:AD414]
[question:AD415]
[question:AD410]









