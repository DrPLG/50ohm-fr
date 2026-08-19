Dans le chapitre précédent, nous avons fait connaissance avec le montage collecteur commun d'un transistor bipolaire. Dans ce chapitre, nous examinons le *montage émetteur commun*.

<margin>
[picture:1118:a_emitter_collector:Montages émetteur commun et collecteur commun, avec les désignations base (B), collecteur (C) et émetteur (E)]

Résumons brièvement les propriétés des montages collecteur commun et émetteur commun dans le tableau suivant : 

| l: Propriété | X: Montage émetteur commun | X: Montage collecteur commun |
| Déphasage | $\qty{180}{\degree}$ | $\qty{0}{\degree}$ |
| Gain en tension | $\num{100}\dots\num{300}$ | $\num{0,9}\dots\num{0,98}$ |
| Impédance d'entrée | élevée | élevée |
| Impédance de sortie | élevée | faible |
</margin>

Comme nous l'avons appris au chapitre précédent, la dénomination des montages fondamentaux d'un transistor bipolaire dépend de la borne qui ne sert ni d'entrée ni de sortie du montage et qui constitue donc le point de référence commun au circuit d'entrée et au circuit de sortie. Dans le montage émetteur commun, c'est l'émetteur. 

---

[question:AD409]

<tip>
Les montages amplificateurs à transistors bipolaires sont désignés d'après la borne à laquelle ne sont directement raccordées ni l'entrée ni la sortie (cf. figure [ref:a_emitter_collector]). 
</tip>

---

La figure [ref:a_emitterschaltung] montre un montage émetteur commun simple, avec son alimentation, sa résistance de collecteur et ses condensateurs de liaison.

Pour le fonctionnement en amplificateur de tension linéaire, le transistor en montage émetteur commun a besoin d'un point de fonctionnement défini (de l'anglais *bias*, tension de polarisation), qui est normalement fixé par un diviseur de tension à la base.

<margin>
[picture:136:a_emitterschaltung:Montage émetteur commun]
</margin>

[question:AD411]

La résistance de collecteur convertit le courant qui traverse le trajet collecteur-émetteur en une chute de tension, prélevée au collecteur. Le courant de collecteur du transistor circule (avec la composante de courant de base, normalement négligeable) via l'émetteur à travers la résistance d'émetteur vers la masse. Le courant qui traverse la résistance d'émetteur provoque, par la chute de tension qui en résulte, une élévation du potentiel d'émetteur (tension d'émetteur) et agit donc comme une contre-réaction pour la tension de base. Le point de fonctionnement du transistor s'en trouve en outre stabilisé, car les variations du courant de collecteur d'origine thermique sont ainsi régulées.

L'injection et le prélèvement des signaux à la base et au collecteur s'effectuent via des condensateurs dits de liaison. Ceux-ci ont pour tâche de tenir éloignées de l'étage amplificateur les composantes continues, qui conduiraient à une modification du point de fonctionnement.

[question:AD412]

Le condensateur de découplage placé sur la tension de service (+) sert à évacuer les signaux HF et BF indésirables, afin d'éviter les effets de réaction sur l'étage et sur la tension d'alimentation.

Le déphasage entre le signal d'entrée et le signal de sortie est, pour le montage émetteur commun, de $\qty{180}{\degree}$, car lors d'une alternance positive de la tension d'entrée à la base, le courant de collecteur augmente et donc la chute de tension aux bornes de la résistance de collecteur croît. La tension aux bornes du condensateur de sortie diminue ainsi. Il en résulte une alternance négative à la sortie de l'étage amplificateur.

[question:AD407]
[question:AD408]

Le gain en tension du montage émetteur commun se situe, pour un dimensionnement approprié, dans la plage de $100\dots 300$ et est donc très élevé par rapport à celui du montage collecteur commun.

[question:AD410]

Le condensateur placé à l'émetteur shunte la résistance d'émetteur pour les tensions alternatives, ce qui réduit la contre-réaction et augmente le gain en tension alternative, tandis que le point de fonctionnement en courant continu reste inchangé.

[question:AD413]

Si l'on retire cependant le condensateur d'émetteur, le facteur d'amplification du montage diminue considérablement (par ex. de $\num{100}$ à $\num{10}$). Il n'est en fin de compte plus défini que par le rapport de la résistance de collecteur à la résistance d'émetteur.

[question:AD414]
[question:AD415]

Lorsqu'un montage émetteur commun est exploité, comme dans la question suivante, sans préréglage du point de fonctionnement par un diviseur de tension, la commande du transistor s'effectue uniquement par le signal d'entrée appliqué. Ce n'est que lorsque celui-ci dépasse la valeur d'env. $\qty{0,6}{\volt}$ que le trajet base-émetteur du transistor devient passant. De ce fait, un courant de collecteur ne circule que dans les crêtes de tension, ce qui provoque une chute de tension à la sortie. Comme signal de sortie apparaît la tension d'alimentation, qui chute aux instants où le transistor entre dans la zone conductrice. C'est ainsi que s'explique le signal de sortie correspondant.

[question:AD406]
