Comme nous l'avons appris, la largeur de bande occupée à l'émission dépend du type de modulation et, en FM, également de l'excursion. Pour chaque bande radioamateur, des largeurs de bande maximales admissibles sont fixées. On les trouve dans l'[annexe 1](https://50ohm.de/a1) du règlement sur le radioamateurisme, dont nous avons déjà tiré les limites de bandes. Ces largeurs de bande ne doivent pas être dépassées. Chaque radioamateur est lui-même responsable de leur respect.

<webmargin>
| l: Plages de fréquences | l: Statut | X: Cond. suppl. d'utilisation |
| $\qtyrange{135,7}{137,8}{\kilo\hertz}$| S | 1 2 10 |
| $\qtyrange{472}{479}{\kilo\hertz}$| S | 1 |
| $\qtyrange{3500}{3800}{\kilo\hertz}$ | P | 3 |
| $\qtyrange{10100}{10150}{\kilo\hertz}$ | S | 1 10 12 |
| $\qtyrange{28}{29,7}{\mega\hertz}$ | P | 4 13 |
| $\qtyrange{144}{146}{\mega\hertz}$ | P | 6 13 |
| $\qtyrange{430}{440}{\mega\hertz}$ | P | 7 13 |
[table:n_tab_afuv:Extrait de l'annexe 1 de l'AFuV]
</webmargin>

<webmargin>
Les numéros des conditions supplémentaires d'utilisation dans le tableau ci-dessus signifient (les numéros non repris sont sans importance pour la largeur de bande) :
* *1* Largeur de bande occupée maximale admissible d'une émission radioamateur : $\qty{800}{\hertz}$.
* *3* Largeur de bande occupée maximale admissible d'une émission radioamateur : $\qty{2,7}{\kilo\hertz}$.
* *4* Largeur de bande occupée maximale admissible d'une émission radioamateur en dessous de $\qty{29}{\mega\hertz}$ : $\qty{7}{\kilo\hertz}$ ; au-dessus de $\qty{29}{\mega\hertz}$ : $\qty{40}{\kilo\hertz}$.
* *6* Largeur de bande occupée maximale admissible d'une émission radioamateur : $\qty{40}{\kilo\hertz}$.
* *7* Largeur de bande occupée maximale admissible d'une émission radioamateur : $\qty{2}{\mega\hertz}$ ; pour les émissions de télévision modulées en amplitude : $\qty{7}{\mega\hertz}$.
</webmargin>

Les questions suivantes se résolvent toutes à l'aide des notes de bas de page de l'annexe 1 du règlement sur le radioamateurisme, qui — comme déjà mentionné — est disponible comme document d'aide pendant l'examen. Nous recommandons de se familiariser avec l'annexe avant l'examen !

[question:VD738]
[question:VD739]
[question:VD740]
[question:VD741]
[question:VD742]

---

Il faut être particulièrement vigilant lors d'émissions à proximité des limites des bandes radioamateur. Un exemple : supposons qu'un signal FM occupe une largeur de bande de $\qty{15}{\kilo\hertz}$ et que nous réglions l'émetteur sur la limite inférieure de la bande des $\qty{70}{\centi\meter}$, soit $\qty{430}{\mega\hertz}$. Le signal d'émission s'étend autour de la fréquence de la porteuse, soit $\qty{7,5}{\kilo\hertz}$ de part et d'autre. Il irait donc de $\qty{429,9925}{\mega\hertz}$ à $\qty{430,0075}{\mega\hertz}$. Comme le signal serait ainsi pour moitié hors de la bande, nous ne devons pas appuyer sur le PTT ! En FM, mais aussi en AM, il faut donc toujours respecter, par rapport à la limite de bande, une distance d'au moins la moitié de la largeur de bande occupée.

<indepth>
[picture:908:n_bandbreite_falsch:Incorrect — émission au-delà des limites de bande]
[picture:909:n_bandbreite_richtig:Correct — émission à l'intérieur des limites de bande]
</indepth>

<indepth>
En SSB, la situation à la limite de bande est un peu différente. Le signal ne se trouve ici que d'un seul côté de la fréquence (supprimée) de la porteuse. En LSB, le signal est entièrement au-dessous de la fréquence de la porteuse ; en USB, entièrement au-dessus. Si l'on règle par exemple la fréquence d'émission sur la limite supérieure de la bande, on pourrait tout à fait émettre en LSB, car tout le signal reste dans la bande. En USB, en revanche, on ne pourrait pas y émettre, car tout le signal serait hors de la bande.
</indepth>

[question:NE305]

<france>
# La largeur de bande est plafonnée par le texte

Voici une règle française sans équivalent dans la réglementation allemande, et qui vaut d'être retenue : l'annexe de la décision ARCEP n° 2012-1241 **plafonne la largeur de bande occupée**, en fonction de la seule fréquence d'émission.

- 6 kHz au plus en dessous de 28 MHz ;
- 12 kHz entre 28 et 144 MHz ;
- 20 kHz entre 144 et 225 MHz ;
- aucune limite fixée au-delà de 225 MHz.

Ces plafonds s'appliquent quel que soit le mode. Une BLU tient très largement dedans, une FM à large bande de 25 kHz sur 2 m n'y tiendrait pas — c'est l'une des raisons pour lesquelles l'excursion réduite s'est imposée en VHF. Et la télévision d'amateur, qui réclame plusieurs mégahertz, n'est donc possible qu'au-dessus de 430 MHz, première bande ouverte au-delà du seuil des 225 MHz.

Un corollaire à ne pas perdre de vue : le signal émis doit rester **entièrement à l'intérieur de la bande attribuée**. Régler son émetteur en bande latérale unique sur 3500 kHz exactement placerait une partie du spectre occupé hors de la bande.

Le texte français reprend par ailleurs le principe de l'article 15.9 du Règlement des radiocommunications : la classe d'émission choisie doit entraîner le minimum de brouillage, ce qui implique de réduire autant que possible la largeur de bande occupée. Le plafond chiffré n'est que la traduction de ce principe.
</france>
