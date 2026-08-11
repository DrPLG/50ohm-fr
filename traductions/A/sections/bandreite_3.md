Pour l'appréciation des prescriptions légales relatives à la largeur de bande d'une émission, c'est, conformément au règlement allemand sur le service amateur, la puissance d'émission moyenne dans la plage de bande émise qui est considérée. Il faut alors que $\qty{99}{\percent}$ de la puissance d'émission se situent à l'intérieur des limites de la largeur de bande exigée. Ainsi, au maximum $\qty{0,5}{\percent}$ de la puissance d'émission peut se répartir sur les plages de bande adjacentes en dessous et au-dessus du signal émis. Cela est particulièrement important pour les émissions FM.

<margin>
[picture:1121:bandbreite_leistungsverteilung:Répartition de la puissance d'une émission]
</margin>

<tip>
Pour la mesure des composantes de puissance d'une émission et de sa largeur de bande, un analyseur de spectre est nécessaire. Les appareils modernes possèdent souvent des fonctions mathématiques intégrées, de sorte que la puissance moyenne à l'intérieur d'une largeur de bande déterminée peut être déterminée par le calcul (mesure de la puissance de canal, mesure de la puissance de canal adjacent). Des informations plus précises à ce sujet peuvent être trouvées dans le mode d'emploi de l'appareil concerné.
</tip>

[question:AE101]

<france>
# Un plafond chiffré, indépendant du mode

Là où le texte allemand raisonne en termes de bonne pratique, la réglementation française **plafonne la largeur de bande occupée** par des valeurs chiffrées, fonction de la seule fréquence d'émission. Le paragraphe 3 de l'annexe de la décision ARCEP n° 2012-1241 fixe :

| Fréquence d'émission | Largeur de bande occupée |
| --- | --- |
| en dessous de $\qty{28}{\mega\hertz}$ | $\qty{6}{\kilo\hertz}$ au plus |
| de $\qty{28}{\mega\hertz}$ à $\qty{144}{\mega\hertz}$ | $\qty{12}{\kilo\hertz}$ au plus |
| de $\qty{144}{\mega\hertz}$ à $\qty{225}{\mega\hertz}$ | $\qty{20}{\kilo\hertz}$ au plus |
| au-dessus de $\qty{225}{\mega\hertz}$ | aucune limite chiffrée |

Ces plafonds s'appliquent quel que soit le mode employé. Le calcul de largeur de bande que vous venez de mener n'est donc pas seulement une question de courtoisie entre opérateurs : c'est une vérification de conformité.

Deux applications directes de ce que vous venez d'apprendre. Une émission FM dont la formule de Carson donne $\qty{16}{\kilo\hertz}$ tient sur $\qty{144}{\mega\hertz}$, mais serait hors des clous sur $\qty{29}{\mega\hertz}$. Et la télévision d'amateur, qui réclame plusieurs mégahertz, n'est possible qu'au-dessus du seuil des $\qty{225}{\mega\hertz}$ — donc à partir de la bande $\qty{430}{\mega\hertz}$.

Le texte français reprend par ailleurs le principe de l'article 15.9 du Règlement des radiocommunications : la classe d'émission retenue doit entraîner le minimum de brouillage et réduire autant que possible la largeur de bande occupée. Le plafond chiffré n'est que la traduction nationale de ce principe.
</france>
