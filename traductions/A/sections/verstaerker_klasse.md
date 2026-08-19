Comme nous l'avons vu dans les sections précédentes, les transistors possèdent une caractéristique qui représente la relation entre le signal d'entrée (tension base-émetteur ou grille-source) et le signal de sortie (courant de collecteur ou de drain). On distingue, sur cette caractéristique, différentes portions dans lesquelles le transistor présente un comportement linéaire ou non linéaire. Les portions de la caractéristique dans lesquelles une variation de la grandeur de commande provoque une variation proportionnelle de la grandeur de sortie sont dites linéaires. En représentation linéaire, ces portions se reconnaissent à leur tracé droit, sans courbure. Les autres portions de la caractéristique, dans lesquelles une variation de la grandeur de commande ne provoque **aucune** variation proportionnelle de la grandeur de sortie, sont dites non linéaires.

<margin>
[picture:1085:a_kennlinien_transistor_arbeitspunkt:Caractéristique d'entrée simplifiée d'un transistor, avec différents points de fonctionnement]  
</margin>

La tension de polarisation appliquée à la base ou à la grille fixe d'abord le point de repos du transistor. Conjointement avec l'amplitude du signal d'entrée, celui-ci détermine sur quelle portion de la caractéristique le transistor est excursionné et pendant quelle fraction d'une période du signal le courant circule. Il en résulte les classes d'amplificateurs A, A/B, B et C, dont les propriétés diffèrent en matière de rendement, de linéarité, d'angle de conduction et de taux d'harmoniques. La figure [ref:a_kennlinien_transistor_arbeitspunkt] montre les points de repos typiques des différentes classes d'amplificateurs, pour le fonctionnement en classe A, B, A/B et C. Par la conception de l'ensemble du montage amplificateur, on peut exploiter délibérément leurs avantages respectifs ou compenser en partie leurs inconvénients. Nous allons examiner dans ce qui suit les différentes classes d'amplificateurs. 

[question:AD416]

---

% A-Betrieb des Verstärkers:

En *classe A*, le point de fonctionnement est choisi de telle sorte que le transistor reste conducteur pendant toute la période du signal (angle de conduction de $\qty{360}{\degree}$). Pour obtenir une excursion aussi grande et aussi symétrique que possible, le point de repos se situe fréquemment à peu près au milieu de la droite de charge, donc entre le blocage et la saturation, de sorte que le transistor travaille entièrement dans la zone linéaire. L'amplification du signal d'entrée (cf. [ref:a_eingangsspannung]) s'effectue alors autour du point de fonctionnement souhaité, qui définit le centre de la plage de fonctionnement. Le choix du point de fonctionnement détermine un courant de repos correspondant ($I_\mathrm{A}$) du transistor (cf. [ref:a_ausgangsstrom_a]). Celui-ci circule même en l'absence de signal d'entrée. Le courant de repos influence de façon déterminante l'efficacité d'un amplificateur, car il augmente sa puissance dissipée thermique et réduit donc son rendement. En classe A, on atteint ainsi habituellement un rendement d'environ $\eta = \qty{40}{\percent}$, ce qui est une bonne valeur pour un amplificateur linéaire. Le taux d'harmoniques est très faible en classe A, puisque le transistor travaille entièrement dans la zone linéaire.

Tous les signaux dont l'information de modulation se trouve dans leur amplitude doivent en règle générale être amplifiés linéairement, afin de transmettre sans distorsion l'information véhiculée (SSB, AM, etc.). Il existe toutefois aussi des astuces de montage qui rendent le fonctionnement linéaire en classe A non indispensable. Les signaux dont l'information de modulation ne se trouve pas dans l'amplitude mais uniquement dans la fréquence peuvent aussi être amplifiés dans la zone non linéaire d'un amplificateur (FM, etc.) puis filtrés.

Résumé du fonctionnement en classe A :

- rendement d'environ $\qty{40}{\percent}$
- taux d'harmoniques très faible
- convient bien à l'AM et à la SSB
- un courant de sortie circule pendant toute la période (angle de conduction $\Theta =\qty{360}{\degree}$) du signal d'entrée

<margin>
[picture:1086:a_eingangsspannung:Exemple de tension d'entrée HF $U_\mathrm{BE}$ d'un transistor]
[picture:1087:a_ausgangsstrom_a:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en classe A]
</margin>

[question:AD419]

% B-Betrieb des Verstärkers:

Lorsque le point de fonctionnement est choisi pour la *classe B*, le transistor se trouve idéalement juste au point de blocage. En l'absence de signal d'entrée, il ne circule donc pratiquement aucun courant de repos. Pour une commande sinusoïdale, comme celle représentée sur la figure [ref:a_eingangsspannung], le transistor ne commence à conduire qu'à partir d'une certaine tension d'entrée. Un transistor seul n'est donc actif que pendant une alternance, c'est-à-dire sur un angle de conduction de $\qty{180}{\degree}$.
Comme la puissance absorbée au repos est presque nulle, le rendement théorique d'un amplificateur de classe B idéal peut atteindre environ $\qty{80}{\percent}$. L'allure du courant d'un transistor seul n'est cependant plus sinusoïdale et contient donc un taux d'harmoniques élevé. 

Pour réduire, voire supprimer les harmoniques, il existe en pratique différentes solutions :

- Une possibilité est un montage push-pull, en anglais *push-pull amplifier*, à deux transistors, comme le montre la figure [ref:a_gegentakt]. Chaque transistor amplifie alors une alternance, de sorte que les deux alternances sont recomposées en un signal sinusoïdal complet et que le taux d'harmoniques est nettement réduit.
- Outre un étage push-pull, on peut utiliser, pour les amplificateurs HF à bande étroite, un circuit oscillant accordé. Le transistor ne délivre alors des impulsions de courant que pendant une alternance. Le circuit oscillant emmagasine de l'énergie et continue d'osciller entre les impulsions de courant, de sorte qu'un signal à nouveau quasiment sinusoïdal apparaît en sortie sur la période complète. Autrement dit, le circuit oscillant agit comme un filtre qui supprime les composantes harmoniques. Cette solution ne convient toutefois qu'aux amplificateurs HF à bande étroite, car un circuit oscillant n'est résonant que dans une plage de fréquences restreinte.

<margin>
[picture:1089:a_ausgangsstrom_b:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en classe B]
[picture:1091:a_gegentakt:Étage push-pull à deux transistors, amplifiant chacun une alternance]
</margin>

Résumé du fonctionnement en classe B :
- faible tension de polarisation jusqu'à l'apparition du courant de collecteur
- courant de repos presque nul
- rendement pouvant atteindre environ $\qty{80}{\percent}$
- taux d'harmoniques faible avec un étage push-pull ou un circuit oscillant
- angle de conduction $\Theta = \qty{180}{\degree}$, c'est-à-dire qu'une seule alternance est amplifiée

[question:AD420]
[question:AD417]

---

% A/B-Betrieb des Verstärkers:

Une autre possibilité pour réaliser un amplificateur est le fonctionnement en classe A/B, dans lequel le point de fonctionnement se situe entre la classe A et la classe B. Le courant de repos ($I_\mathrm{A/B}$) y est plus élevé qu'en classe B, mais nettement plus faible qu'en classe A, comme le montre la figure [ref:a_ausgangsstrom_ab]. Le rendement se situe entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$ et le taux d'harmoniques est lui aussi faible avec une technique de montage appropriée.

Résumé du fonctionnement de l'amplificateur en classe A/B
- tension de polarisation plus élevée qu'en classe B, mais plus faible qu'en classe A
- courant de repos plus élevé qu'en classe B, mais nettement plus faible qu'en classe A
- rendement entre $\qty{50}{\percent}$ et $\qty{80}{\percent}$
- taux d'harmoniques faible
- angle de conduction : $\qty{180}{\degree} < \Theta < \qty{360}{\degree}$

En particulier lors du fonctionnement en classe A/B ou B d'un amplificateur, il faut éviter la saturation, car celle-ci peut rapidement conduire à des distorsions du signal. Celles-ci se manifestent en SSB sous la forme de splatter sur les fréquences voisines.
[question:AD423]

<margin>
[picture:1088:a_ausgangsstrom_ab:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en classe A/B]
</margin>

---

% C-Betrieb des Verstärkers:

Le fonctionnement dit en *classe C* est fortement non linéaire, car le transistor ne conduit que pendant une petite partie de l'oscillation d'entrée (cf. figure [ref:a_ausgangsstrom_c]). L'angle de conduction est inférieur à $\qty{180}{\degree}$ et, en l'absence de signal d'entrée, il ne circule idéalement aucun courant de repos. On peut ainsi atteindre des rendements élevés, typiquement de l'ordre de $\qtyrange{80}{87}{\percent}$.

Comme le transistor ne produit que de brèves impulsions de courant, son signal de sortie contient de fortes composantes harmoniques. Un circuit oscillant accordé ou un filtre placé en aval sélectionne la fréquence de sortie souhaitée et supprime les harmoniques indésirables. Comme ces harmoniques peuvent encore présenter des puissances considérables à l'intérieur de l'amplificateur de puissance et du filtre, le montage et ses liaisons doivent être réalisés et blindés avec soin, afin qu'aucun signal indésirable ne soit rayonné.

La classe C convient particulièrement aux signaux à enveloppe constante, par exemple à la FM et à la CW. Elle ne convient pas à l'AM et à la SSB sans mesures supplémentaires, car l'information d'amplitude serait distordue par l'amplification non linéaire. C'est pourquoi on utilise en règle générale, pour les amplificateurs AM et SSB, un fonctionnement en classe A, B ou A/B. Des procédés particuliers, comme la modulation polaire, permettent toutefois de produire aussi des signaux modulés en amplitude à l'aide d'amplificateurs non linéaires à haut rendement. Nous y reviendrons plus en détail dans une section ultérieure.

Résumé : fonctionnement de l'amplificateur en classe C
- sans tension de polarisation
- courant de repos nul
- rendement d'environ $\qtyrange{80}{87}{\percent}$
- produit, de toutes les classes d'amplificateurs, le taux d'harmoniques le plus élevé
- angle de conduction $\Theta < \qty{180}{\degree}$, c'est-à-dire qu'une petite partie seulement de l'onde sinusoïdale est amplifiée

<margin>
[picture:1090:a_ausgangsstrom_c:Exemple de courant de sortie HF $I_\mathrm{C}$ d'un transistor en classe C]
</margin>

[question:AD418]
[question:AD425]
[question:AD421]
[question:AD422]
[question:AJ218]
[question:AF402]
[question:AF403]

Résumons une dernière fois, dans un tableau d'ensemble, les classes d'amplificateurs étudiées :

| l: Propriété | X: Classe A | X: Classe B | X: Classe A/B | X: Classe C |
| Courant de repos | $I_\mathrm{A}$ | 0 | $I_\mathrm{A/B}$ | 0 |
| Rendement | $\qty{40}{\percent}$ | jusqu'à $\qty{80}{\percent}$ | $\qtyrange{50}{80}{\percent}$ | $\qtyrange{80}{87}{\percent}$ |
| Angle de conduction | $\Theta = \qty{360}{\degree}$ | $\Theta = \qty{180}{\degree}$ | $\qty{180}{\degree} < \Theta < \qty{360}{\degree}$ | $\Theta < \qty{180}{\degree}$ |
| Mesures contre les harmoniques | Filtre | Étage push-pull ou filtre | Étage push-pull ou filtre | Filtre |

La puissance de sortie d'un amplificateur peut être calculée approximativement par la connaissance du point de fonctionnement et donc de son rendement approximatif. On calcule d'abord la puissance en courant continu fournie à l'amplificateur, à partir du produit de la tension et du courant. On multiplie ensuite cette puissance par le facteur numérique du rendement, $\qty{100}{\percent}$ correspondant à un rendement de $1$. Par exemple, un rendement de $\qty{40}{\percent}$ correspond alors à un facteur de $0,4$. Essaie maintenant de résoudre les exercices suivants :

[question:AD424]

Outre les classes d'amplificateurs classiques A, B, AB et C, il existe d'autres classes à haut rendement, comme les classes D, E et F. Dans les amplificateurs de classe D et de classe E, le transistor est délibérément exploité en commutateur, de sorte que le moins de puissance possible soit perdue dans le transistor lui-même. Les amplificateurs de classe F utilisent en outre des réseaux accordés sur la fréquence fondamentale et sur des harmoniques choisies, afin de mettre en forme favorablement les allures du courant et de la tension au niveau du transistor. On peut atteindre de cette manière des rendements très élevés. De tels amplificateurs exigent toutefois une conception soignée du montage et ne conviennent souvent, dans le domaine HF, qu'à une plage de fréquences limitée. D'autres modes de fonctionnement, comme la classe J ou la classe S, poursuivent des objectifs analogues, mais ne sont pas pertinents pour l'examen radioamateur.
