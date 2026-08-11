Puisque nous venons de traiter la puissance rayonnée, faisons encore un bref détour par la puissance rayonnée maximale admissible pour les radioamateurs de classe N. Celle-ci s'exprime en effet en ERP ou EIRP : elle est de $\qty{10}{\watt}$ ERP dans la bande des $\qty{10}{\meter}$ et de $\qty{10}{\watt}$ EIRP dans les bandes des $\qty{2}{\meter}$ et des $\qty{70}{\centi\meter}$.

[question:VD724]

[question:VD743]

Voyons cela sur un exemple. Supposons qu'en tant que radioamateur de classe N, nous utilisions un portatif VHF de $\qty{5}{\watt}$ de puissance d'émission et que nous nous demandions si nous pouvons y raccorder une petite antenne Yagi-Uda. La réponse dépend du facteur de gain de l'antenne, et donc de la puissance isotrope rayonnée équivalente.

Rappelons-nous : la puissance rayonnée se calcule en multipliant la puissance d'émission par le facteur de gain. Si le facteur de gain rapporté à l'antenne isotrope est inférieur à $\num{2}$, nous obtenons une puissance rayonnée inférieure à $\qty{10}{\watt}$ EIRP et nous pouvons utiliser l'antenne. Si en revanche le facteur de gain rapporté à l'antenne isotrope est supérieur à $\num{2}$, nous obtenons une puissance rayonnée supérieure à $\qty{10}{\watt}$ EIRP et nous ne pouvons pas, en tant que radioamateur de classe N, utiliser cette antenne.

[question:VD726]

[question:VD725]

<france>
# En France, la puissance ne se compte pas en ERP

Cette section n'a pas d'équivalent français, et l'écart mérite qu'on s'y arrête, parce qu'il change la façon même de raisonner.

Le raisonnement allemand présenté ici est le suivant : la classe N est limitée en **puissance rayonnée**, donc le gain de l'antenne entre dans le calcul, et brancher une Yagi sur un portatif de 5 W peut faire franchir la limite.

Le raisonnement français est différent sur les deux plans. D'abord, il n'y a pas de classe N : une seule classe existe. Ensuite et surtout, la limite française est une **puissance en crête à la sortie de l'émetteur**, au sens de l'article 1.157 du Règlement des radiocommunications — 500 W, 250 W ou 120 W selon la bande, et 10 W sur 144 à 146 MHz pour les derniers titulaires de l'ex-classe 3. Le tableau complet figure au chapitre des bandes d'amateur.

Il en découle un point souvent mal compris : **le gain des antennes n'est pas limité en France**, puisque la réglementation s'arrête à la sortie de l'émetteur. Une antenne à fort gain est parfaitement licite et n'a pas à être déclarée en tant que telle. Autrement dit, gagner 10 dB en changeant d'antenne ne consomme aucun quota réglementaire.

Les seules exceptions sont les trois bandes où la limite est exprimée en PIRE — 137 kHz, 472 kHz et 60 m —, où le plafond porte sur la puissance rayonnée et intègre donc le gain, et le seuil de 5 W PAR qui déclenche la déclaration à l'ANFR, lequel n'est pas une limite d'émission mais une formalité.

Cela ne dispense évidemment pas de calculer la puissance rayonnée : elle reste ce qui détermine le champ auquel on expose son voisinage.
</france>
