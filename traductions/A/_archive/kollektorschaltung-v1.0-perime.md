La dénomination du montage fondamental d'un transistor bipolaire dépend de la borne (base, collecteur ou émetteur) qui est traversée en commun par le signal d'entrée et le signal de sortie.

Dans le *montage collecteur commun*, le signal d'entrée circule de la source via la base, le *collecteur* et la tension d'alimentation pour revenir à la source. Le signal de sortie circule du collecteur à travers la charge (puits) et via la tension d'alimentation pour revenir dans le *collecteur*.

[question:AD401]

Pour le fonctionnement en amplificateur de courant linéaire, le transistor en montage collecteur commun a besoin d'un point de fonctionnement défini (BIAS), qui est normalement fixé par un diviseur de tension à la base.

La résistance d'émetteur convertit le courant qui traverse le trajet collecteur-émetteur en une chute de tension, prélevée à l'émetteur. Le courant d'émetteur du transistor circule (avec la composante de courant de base, normalement négligeable) via l'émetteur à travers la résistance d'émetteur vers la masse. Le courant qui traverse la résistance d'émetteur provoque, par la chute de tension qui en résulte, une élévation du potentiel d'émetteur (tension d'émetteur) et agit donc comme une contre-réaction pour la tension de base. Le point de fonctionnement du transistor s'en trouve en outre stabilisé, car les variations du courant de collecteur d'origine thermique sont ainsi régulées.

L'injection et le prélèvement des signaux à la base et à l'émetteur s'effectuent via des condensateurs dits de liaison. Ceux-ci ont pour tâche de tenir éloignées de l'étage amplificateur les composantes continues, qui conduiraient à une modification du point de fonctionnement.

Le condensateur de découplage placé sur la tension de service (+) sert à évacuer les signaux HF et BF indésirables, afin d'éviter les effets de réaction sur l'étage et sur la tension d'alimentation. De plus, le collecteur est, par le condensateur de découplage, mis en commun avec l'entrée et la sortie du point de vue du signal (pour la tension alternative).

Le déphasage entre le signal d'entrée et le signal de sortie est, pour le montage collecteur commun, de $\qty{0}{\degree}$, car lors d'une alternance positive de la tension d'entrée, le courant d'émetteur augmente et donc la chute de tension aux bornes de la résistance d'émetteur croît. La tension aux bornes du condensateur de sortie augmente ainsi. Il en résulte une alternance positive à la sortie de l'étage amplificateur.

Le gain en tension du montage collecteur commun se situe, pour un dimensionnement approprié, dans la plage de $\num{0,9}$ à $\num{0,98}$ et est toujours un peu inférieur à $1$. Le gain en courant du montage collecteur commun est en revanche très élevé, car l'impédance d'entrée du montage est relativement élevée. L'impédance de sortie est en revanche très faible par rapport à l'impédance d'entrée.

[question:AD405]
[question:AD402]
[question:AD403]

Le *montage collecteur commun est fréquemment utilisé comme étage tampon entre l'oscillateur et les autres parties du montage*, qui chargeraient sinon l'oscillateur en basse impédance, afin d'obtenir un découplage et une meilleure stabilisation en fréquence de l'oscillateur.

[question:AD404]

