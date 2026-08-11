Dans les deux prochains chapitres, nous nous intéressons à deux montages fondamentaux importants du transistor bipolaire. Nous examinons d'abord, dans ce chapitre, le *montage collecteur commun*, puis, dans le chapitre suivant, le *montage émetteur commun*. Les deux montages sont représentés sur la figure [ref:a_emitter_collector]. Ils possèdent des propriétés différentes et sont donc employés pour des applications différentes.

<margin>
[picture:1118:a_emitter_collector:Montages émetteur commun et collecteur commun, avec les désignations base (B), collecteur (C) et émetteur (E)]
</margin>

La dénomination des montages fondamentaux d'un transistor bipolaire dépend de la borne qui ne sert ni d'entrée ni de sortie du montage et qui constitue donc le point de référence commun au circuit d'entrée et au circuit de sortie. Dans le montage collecteur commun, c'est le collecteur. 

---

[question:AD401]

<tip>
Les montages amplificateurs à transistors bipolaires sont désignés d'après la borne à laquelle ne sont directement raccordées ni l'entrée ni la sortie (cf. figure [ref:a_emitter_collector]). 
</tip>

Comme le collecteur est habituellement relié à la tension d'alimentation et se trouve, pour les tensions alternatives, à un potentiel approximativement fixe, la tension à l'émetteur suit la tension à la base. Le montage collecteur commun est donc aussi souvent appelé *émetteur suiveur*.

Si la tension d'entrée augmente par exemple pendant une alternance positive, le courant d'émetteur croît. La chute de tension aux bornes de la résistance d'émetteur augmente alors, et la tension de sortie croît elle aussi. Le signal d'entrée et le signal de sortie sont donc en phase ; le déphasage vaut $\qty{0}{\degree}$. C'est pour cette raison que le montage collecteur commun est également appelé *émetteur suiveur*.

[question:AD405]

---

La figure [ref:a_collector_circuit] montre un montage collecteur commun simple, avec son alimentation, sa résistance d'émetteur et ses condensateurs de liaison. 

<margin>
[picture:140:a_collector_circuit:Montage collecteur commun avec alimentation, résistance d'émetteur et condensateurs de liaison]
</margin>

---

Pour le fonctionnement en amplificateur de courant linéaire, le transistor en montage collecteur commun a besoin d'un point de fonctionnement défini (BIAS), qui est normalement fixé par un diviseur de tension à la base.

La figure [ref:a_kennlinie] montre la caractéristique d'un transistor NPN, avec le point de fonctionnement établi par le diviseur de tension. La tension de polarisation de base est choisie de telle sorte que l'on travaille sur la partie linéaire de la caractéristique d'entrée. Cela implique aussi qu'un certain courant de repos circule toujours, même en l'absence de signal d'entrée. Nous examinerons cela de plus près dans le chapitre consacré aux classes d'amplificateurs. 

Si un signal d'entrée, par ex. une tension alternative sinusoïdale, est appliqué comme le montre la figure, ce signal est amplifié par la caractéristique d'entrée. On prendra garde ici à la graduation des axes : les microampères deviennent des milliampères. La tension résultante à la sortie peut elle aussi se lire sur cette caractéristique 

<margin>
[picture:1119:a_kennlinie:Caractéristique d'un transistor NPN avec point de fonctionnement et superposition du signal]
</margin>

La résistance d'émetteur convertit le courant qui traverse le trajet collecteur-émetteur en une chute de tension, prélevée à l'émetteur. Le courant d'émetteur du transistor circule (avec la composante de courant de base, normalement négligeable) via l'émetteur à travers la résistance d'émetteur vers la masse. Le courant qui traverse la résistance d'émetteur provoque, par la chute de tension qui en résulte, une élévation du potentiel d'émetteur (tension d'émetteur) et agit donc comme une contre-réaction pour la tension de base. Le point de fonctionnement du transistor s'en trouve en outre stabilisé, car les variations du courant de collecteur d'origine thermique sont ainsi régulées.

L'injection et le prélèvement des signaux à la base et à l'émetteur s'effectuent via des condensateurs dits de liaison. Ceux-ci ont pour tâche de tenir éloignées de l'étage amplificateur les composantes continues, qui conduiraient à une modification du point de fonctionnement.

Le condensateur de découplage placé sur la tension de service (+) sert à évacuer les signaux HF et BF indésirables, afin d'éviter les effets de réaction sur l'étage et sur la tension d'alimentation. De plus, le collecteur est, par le condensateur de découplage, mis en commun avec l'entrée et la sortie du point de vue du signal (pour la tension alternative).

Le gain en tension du montage collecteur commun se situe, pour un dimensionnement approprié, dans la plage de $\num{0,9}$ à $\num{0,98}$ et est toujours un peu inférieur à $1$. 

On pourrait se demander à quoi sert un amplificateur dont le gain en tension est inférieur à $1$. Le montage collecteur commun possède pourtant un avantage décisif, que nous examinons maintenant. 

[question:AD402]

Le montage collecteur commun présente un gain en courant important. Son impédance d'entrée est relativement élevée, car un faible courant seulement peut circuler dans la base. L'impédance de sortie est en revanche relativement faible. Si la tension de sortie est modifiée par une charge raccordée, la tension base-émetteur s'en trouve modifiée et le transistor réajuste son courant d'émetteur de manière à s'opposer à cette variation. Grâce à cette contre-réaction, le montage collecteur commun peut attaquer une charge de faible impédance sans que sa tension de sortie varie fortement.

[question:AD403]

C'est pour cette raison que le montage collecteur commun est fréquemment utilisé comme *étage tampon entre l'oscillateur et les autres parties du montage*, qui chargeraient sinon l'oscillateur en basse impédance, afin d'obtenir un découplage et une meilleure stabilisation en fréquence de l'oscillateur.

[question:AD404]
