Un procédé connu depuis des décennies trouve depuis quelque temps un usage croissant dans le service amateur : la *modulation polaire* [index:Modulation polaire].

Ce sujet ne fait l'objet d'aucune question d'examen. Mais la modulation polaire est un procédé passionnant, qui sera de plus en plus employé à l'avenir dans les équipements radioamateurs. Il est donc présenté ici brièvement, en guise d'ouverture. Qui veut n'apprendre que la matière de l'examen peut sauter ce sujet sans crainte.

La modulation polaire repose sur l'observation de ce qui se passe lorsqu'on zoome dans le temps sur un signal quelconque de largeur de bande assez étroite : le train d'ondes pris isolément ressemble à une sinusoïde.

Cette sinusoïde est définie par un petit nombre de grandeurs, à savoir la fréquence, la phase et l'amplitude. La fréquence et la phase sont d'ailleurs couplées entre elles : qui part d'une fréquence fondamentale donnée, puis décale à chaque train d'ondes la phase toujours dans le même sens, aboutit à une autre fréquence, décalée.

De ces considérations découle le procédé de *modulation polaire*. Il permet de produire des signaux quelconques de largeur de bande assez étroite, par exemple des signaux SSB. Il suffit pour cela que, à partir d'une fréquence fondamentale, la phase et l'amplitude du signal soient contrôlables simultanément.

La figure [ref:polar_modulator] montre le schéma fonctionnel par lequel cette idée est aujourd'hui habituellement mise en œuvre. Les deux composantes du signal $I(t)$ et $Q(t)$ (telles qu'elles ont été décrites au chapitre précédent) y sont converties en une amplitude instantanée $A(t)$ et une phase instantanée $\varphi(t)$ :

$A(t)=\sqrt{I^2(t)+Q^2(t)}$

$\varphi(t)=\operatorname{atan2}\left(Q(t),I(t)\right)$

L'information de phase $\varphi(t)$ module ensuite une porteuse HF dont l'amplitude est d'abord constante. Le signal obtenu, toujours d'amplitude constante, contient donc déjà l'information de phase complète. Il peut être amplifié par un amplificateur de puissance à commutation particulièrement efficace, par exemple un amplificateur de classe E. De tels amplificateurs atteignent souvent, en pratique, des rendements supérieurs à $\qtyrange{80}{90}{\percent}$.

Mais comment la modulation d'amplitude entre-t-elle en jeu ? Il suffit pour cela de manipuler en conséquence la tension d'alimentation de l'amplificateur de puissance. L'information d'amplitude $A(t)$ lui est appliquée au moyen d'un amplificateur d'enveloppe. L'amplitude de sortie varie ainsi conformément à l'amplitude requise à chaque instant, et l'on obtient l'enveloppe souhaitée. On retrouve en sortie le signal complet, modulé en amplitude et en phase :

$s(t)=A(t)\cos\left(\omega_\mathrm{p}t+\varphi(t)\right)$

Pour que le signal reste aussi peu distordu que possible, le trajet d'amplitude et le trajet de phase doivent être accordés dans le temps avec précision.

Pour l'amplificateur d'enveloppe, un amplificateur BF relativement lent suffit. La plage de fréquences qu'il doit couvrir dépend de la largeur de bande du signal à produire. Pour maintenir le rendement élevé, on emploie ici habituellement la technologie des alimentations à découpage (amplificateur BF de « classe D »).

Le rendement élevé fait qu'une faible part de la puissance électrique est convertie en chaleur. Cela économise de l'énergie, réduit le besoin de refroidissement et permet des appareils radio plus petits et plus légers, sans gros dissipateur métallique et avec des transistors de puissance moins coûteux. La modulation polaire convient particulièrement aux appareils radio QRP alimentés par batterie, mais elle est également employée dans des émetteurs-récepteurs commerciaux plus puissants.

<indepth>
Dans le service amateur, le procédé a été employé pour la première fois sous le nom de « HELAPS », à bord du satellite AO-7, au cours des années 1970. Tout était alors réalisé par des moyens analogiques. Aujourd'hui, l'amplificateur d'enveloppe et l'amplificateur de puissance restent classiquement analogiques ; le reste du travail est pris en charge par des algorithmes SDR. Les processeurs capables d'exécuter sans peine les tâches que cela représente coûtent aujourd'hui moins cher qu'une pizza.
</indepth>

<margin>
[picture:1117:polar_modulator:Modulateur polaire]
</margin>
