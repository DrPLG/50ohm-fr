---
%Frequenzabhängigkeit des Personenschutzabstands:

L'[Office fédéral de protection contre les rayonnements (Bundesamt für Strahlenschutz)](https://50ohm.de/bfs) informe sur son site des effets biologiques des champs haute fréquence sur le corps humain.
  
* Les champs électromagnétiques haute fréquence sont absorbés par le corps.
* L'intensité de l'absorption d'énergie dépend de l'intensité et de la fréquence des champs électromagnétiques.
* Des effets de force et un effet thermique des champs haute fréquence sont clairement démontrés.
* L'effet thermique est déterminant pour les effets possibles sur la santé humaine.

Ce qui importe pour répondre à la question, c'est ici le point 2 : l'absorption d'énergie du corps humain dépend de la fréquence.

[question:EK101]

% Zeitabhängigkeit des Personenschutzabstand:

Dans le [règlement sur les champs électromagnétiques (26. BImSchV)](https://50ohm.de/BImSchV), les valeurs limites sont décrites dans l'annexe 1 (tableaux 1a et 1b) ainsi que dans l'annexe 3. On distingue trois cas :

* Valeur de crête instantanée (en $\unit{\kilo\volt\per\meter}$ en fonction des $\unit{\hertz}$, cf. figure [ref:e_grenzwerte_max])
* Intervalles de 6 minutes (en $\unit{\volt\per\meter}$ en fonction des $\unit{\mega\hertz}$, cf. figure [ref:e_grenzwerte_avg])
* Champs pulsés (calculés à partir des deux premiers et de facteurs dépendant de la fréquence, cf. figure [ref:e_grenzwerte_pulse])


<margin>
[picture:980:e_grenzwerte_max:Visualisation des valeurs limites de la 26. BImSchV, tableau 1a, valeur de crête instantanée]
[picture:979:e_grenzwerte_avg:Visualisation des valeurs limites de la 26. BImSchV, tableau 1b, intervalles de 6 minutes]
[picture:981:e_grenzwerte_pulse:Visualisation des valeurs limites de la 26. BImSchV, annexe 3, champs pulsés]
</margin>

---

Comme on n'émet pas en permanence, nous utilisons en règle générale la moyenne quadratique de l'intensité de champ ($\unit{\volt\per\meter}$), moyennée sur une durée de 6 minutes. Une valeur importante ici est $\qty{28}{\volt\per\meter}$, qui est valable pour la plage de $\qtyrange{10}{400}{\mega\hertz}$, donc pour un grand nombre de bandes radioamateur, et qui apparaît dans plusieurs des questions d'examen suivantes sur la protection des personnes.

<tip>
Les valeurs limites n'ont pas besoin d'être apprises par cœur pour l'examen ; elles sont toujours indiquées dans la question à l'examen.
</tip>

[question:EK102]

Les aides médicales actives (par exemple stimulateurs cardiaques, pompes à insuline, implants cochléaires) constituent ici une exception, car dans certains cas ce sont les valeurs instantanées maximales qui doivent être retenues.

[question:EK103]

<france>
# Les mêmes valeurs, une tout autre procédure

Les valeurs limites françaises et allemandes ont la même origine : la recommandation 1999/519/CE du Conseil de l'Union européenne du 12 juillet 1999. La 26. BImSchV la transpose côté allemand, le décret n° 2002-775 du 3 mai 2002 côté français. Les niveaux de référence sont donc identiques, à commencer par les $\qty{28}{\volt\per\meter}$ de la plage $\qtyrange{10}{400}{\mega\hertz}$, que vous venez de rencontrer.

Les niveaux de référence utiles aux bandes radioamateur, tels qu'ils figurent à l'annexe du décret, la fréquence $f$ étant exprimée en $\unit{\mega\hertz}$ :

| Gamme de fréquences | Champ électrique | Champ magnétique |
| --- | --- | --- |
| $\qtyrange{1}{10}{\mega\hertz}$ | $87/\sqrt{f}$ | $0{,}73/f$ |
| $\qtyrange{10}{400}{\mega\hertz}$ | $\qty{28}{\volt\per\meter}$ | $\qty{0,073}{\ampere\per\meter}$ |
| $\qtyrange{400}{2000}{\mega\hertz}$ | $1{,}375\sqrt{f}$ | $0{,}0037\sqrt{f}$ |
| $\qtyrange{2}{300}{\giga\hertz}$ | $\qty{61}{\volt\per\meter}$ | $\qty{0,16}{\ampere\per\meter}$ |

Comme en Allemagne, ces niveaux se moyennent sur six minutes entre $\qty{100}{\kilo\hertz}$ et $\qty{10}{\giga\hertz}$.

La différence est ailleurs, et elle est de taille. Il n'existe en France **aucun équivalent de la fiche de site allemande** — ni déclaration préalable, ni attestation à établir avant de mettre la station en service. L'obligation est de résultat, non de forme : l'article 5 du décret prévoit seulement que l'exploitant communique, **à la demande** de l'administration, un dossier justifiant le respect des valeurs limites. Ce dossier peut s'appuyer sur une déclaration de conformité aux normes, ou sur un mesurage effectué selon le protocole publié au Journal officiel. C'est l'ANFR qui procède aux contrôles.

Autrement dit, un radioamateur français n'a rien à déposer avant d'émettre, mais il doit être en mesure de justifier son installation si l'administration le lui demande — ce qui suppose d'avoir fait le calcul, exactement comme le fait ici votre collègue allemand.

Un point mérite attention : lorsque plusieurs installations rayonnent au même endroit, l'article 3 du décret impose que ce soit **l'exposition globale** qui reste sous les valeurs limites. Une antenne installée à proximité d'un relais de téléphonie mobile n'échappe donc pas à la règle sous prétexte que sa contribution propre serait faible.
</france>
