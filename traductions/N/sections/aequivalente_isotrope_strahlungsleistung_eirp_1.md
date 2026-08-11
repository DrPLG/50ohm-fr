Souvent, la puissance rayonnée n'est cependant pas rapportée au dipôle demi-onde, mais à un *radiateur sphérique*, appelé dans le langage technique *antenne isotrope*.

L'antenne isotrope est une antenne qui n'existe qu'en théorie. Elle est infiniment petite — plus petite qu'une tête d'épingle. Les ondes radio en sont théoriquement rayonnées dans toutes les directions avec la même force. L'antenne isotrope n'a donc pas de direction principale de rayonnement.

<margin>
[picture:751:n_Kugelstrahler:Antenne isotrope au centre d'une sphère, produisant la même puissance rayonnée en tout point de la surface de la sphère]
</margin>

Quand la puissance rayonnée est rapportée à l'antenne isotrope, on parle de « puissance isotrope rayonnée équivalente ». Elle s'abrège EIRP, d'après l'anglais « equivalent isotropic radiated power » (en français, on trouve aussi PIRE).

---

Le calcul de l'EIRP suit le même principe que celui de l'ERP : si une antenne a un facteur de gain de $\num{3}$ rapporté à l'antenne isotrope, elle rayonne dans sa direction principale trois fois plus fort qu'une antenne isotrope dans n'importe quelle direction. Si l'on injecte $\qty{5}{\watt}$ de puissance d'émission dans une antenne au facteur de gain de $\num{3}$ par rapport à l'antenne isotrope, sa puissance rayonnée est de $\qty{15}{\watt}$ EIRP.

<indepth>
Un dipôle demi-onde a d'ailleurs un facteur de gain de $\num{1,64}$ par rapport à l'antenne isotrope. Cette valeur permet aussi de convertir entre le facteur de gain rapporté au dipôle demi-onde et celui rapporté à l'antenne isotrope. Si une antenne a un facteur de gain de $\num{2}$ par rapport au dipôle demi-onde, elle a un facteur de gain de $2 \cdot 1,64 = 3,28$ par rapport au radiateur sphérique.
</indepth>

[question:NG402]

<france>
# EIRP se dit PIRE

L'EIRP, *equivalent isotropically radiated power*, se dit en français **puissance isotrope rayonnée équivalente**, abrégée **PIRE** : la puissance qu'il faudrait fournir à un radiateur isotrope pour obtenir le même champ. Le rapport avec la PAR est celui que l'on connaît, le gain du dipôle demi-onde sur l'isotrope, soit 2,15 dB.

En France, la PIRE n'intervient pas comme critère général de puissance — c'est la puissance en crête à la sortie de l'émetteur qui sert de référence dans presque tout le tableau des bandes. Elle apparaît en revanche pour **trois bandes**, où c'est bien une PIRE maximale qui est fixée :

- 135,7 à 137,8 kHz : 1 W PIRE ;
- 472 à 479 kHz : 1 W PIRE ;
- 5351,5 à 5366,5 kHz : 15 W PIRE.

Sur ces trois bandes seulement, le gain de l'antenne entre donc directement dans le calcul de ce qui est autorisé. Ces valeurs viennent des notes 5.67A, 5.80A et 5.133B du Règlement des radiocommunications.
</france>
