Un composant très important et fréquemment utilisé en radiotechnique et en électronique est le condensateur. Comme le montre la figure [ref:e_kondensator_aufbau], un condensateur se compose en principe de deux surfaces conductrices (plaques, couches ou électrodes) séparées l'une de l'autre par un isolant — le diélectrique.


<margin>
[picture:922:e_kondensator_aufbau:Constitution de principe d'un condensateur]
</margin>

Les dimensions géométriques déterminent une propriété importante du condensateur : l'aptitude à stocker des charges. Cette aptitude est appelée capacité et on lui associe la lettre $C$. Plus la capacité est grande, plus on peut stocker de charges électriques $Q$. Lorsque la tension appliquée augmente, davantage de charges sont également stockées.

La formule suivante montre cette relation.

$Q = C \cdot U $ 

Cette formule ne figure pas dans le formulaire et n'est pas non plus nécessaire pour l'examen.

<unit>
L'unité de la charge $Q$ est l'$\unit{\ampere\second}$
</unit>

<unit>
L'unité de la capacité $C$ est l'$\unit{\ampere\second\per\volt}$, ou en abrégé le *farad* $\unit{\farad}$, en l'honneur du naturaliste anglais Michael Faraday (1791 - 1867). $\qty{1}{\farad}$ est la capacité d'un condensateur dans lequel une charge de $\qty{1}{\ampere\second}$ est stockée sous une tension de $\qty{1}{\volt}$.
</unit>

[question:EA101]

Lorsqu'une tension est appliquée à un condensateur, un champ électrique $E$ apparaît entre les plaques conductrices. Nous avons déjà découvert cette relation dans le chapitre sur le champ électrique : plus la tension appliquée est élevée et plus l'écartement entre les plaques est faible, plus le champ électrique est intense. Mathématiquement, cela s'exprime par :

$E = \frac{U}{d}$

Pour calculer la capacité du condensateur à partir de ses dimensions, on utilise la formule suivante, tirée du formulaire :

---

$C = \frac{\varepsilon_0 \cdot \varepsilon_r \cdot A}{d}$

Les différentes grandeurs de la formule sont détaillées ci-dessous :

- $A$ est la surface en regard des plaques conductrices
- $d$ est l'écartement entre les surfaces
- $\varepsilon_0 = \qty{0,855e-11}{\ampere\second\per\volt\meter}$ est la constante électrique (permittivité du vide), une constante universelle
- $\varepsilon_r$  (prononcer : « epsilon r ») est une propriété particulière de l'isolant (diélectrique) : c'est ce que l'on appelle la permittivité relative, qui dépend du matériau utilisé. Le tableau [ref:e_Dielektrizitätszahl], avec les valeurs des matériaux, figure aussi dans le formulaire.

<margin>
| Matériau | $\varepsilon_r$  |
| Air (sec) | 1,00059 |
| PE plein (polyéthylène) | 2,29 |
| PE expansé | 1,5 |
| PTFE (téflon) | 2,0 |
[table:e_Dielektrizitätszahl:Permittivité relative $\varepsilon_r$ ]
</margin>

À l'aide de la formule, on peut déjà résoudre une série de questions d'examen. On constate d'abord que la tension $U$ n'apparaît pas dans la formule.

[question:EC205]

La capacité d'un condensateur diminue lorsque l'écartement des plaques augmente.

[question:EC204]
[question:EC203]

---

Considérons d'abord le condensateur dans le cas du courant continu. La figure [ref:e_stromkreis_kondensator] représente un montage pour charger un condensateur. On suppose que le condensateur $C$ est d'abord déchargé, c'est-à-dire qu'il n'a encore stocké aucune charge électrique. Lorsqu'on ferme l'interrupteur, le condensateur $C$ est relié à une source de tension continue (batterie) à travers une résistance $R$.

La tension appliquée fait apparaître un champ électrique entre les plaques du condensateur. Ce champ provoque un réarrangement des charges : des électrons sont poussés du pôle négatif de la source de tension vers la plaque du condensateur qui y est raccordée, si bien qu'il s'y forme un excédent d'électrons. Simultanément, des électrons sont retirés de la plaque opposée vers le pôle positif de la source de tension, ce qui y crée un déficit d'électrons. Bien qu'aucun courant ne traverse le diélectrique, cette séparation des charges conduit à la charge du condensateur.

<margin>
[picture:1015:e_stromkreis_kondensator:Circuit pour charger un condensateur]
</margin>

---

Cela signifie qu'au début, un courant élevé circule, limité uniquement par la résistance $R$. Avec le temps, de plus en plus de charges sont stockées dans le condensateur. Le courant diminue donc continuellement, tandis que la tension $U_C$ aux bornes du condensateur augmente, jusqu'à ce que celui-ci soit entièrement chargé. Dans cet état, plus aucun courant ne circule.

Ce processus ne se produit toutefois pas brutalement, mais avec un retard dans le temps. La tension du condensateur croît alors selon une fonction dite exponentielle, comme le montre la figure [ref:e_ladekurve_c]. La durée de cette charge dépend de la résistance placée en amont : plus la résistance est grande, plus il faut de temps pour que le condensateur soit « entièrement » chargé. Avec un oscilloscope, comme le montre la figure [ref:e_lade_entladespannung_mit_oszilloskop] et que nous avons déjà découvert, on peut observer et étudier concrètement cette évolution dans le temps.

<margin>
[picture:185:e_ladekurve_c:Tension de charge d'un condensateur]
</margin>

<margin>
[photo:247:e_lade_entladespannung_mit_oszilloskop:Tensions de charge et de décharge d'un condensateur]  
</margin>
 
Lors de la décharge, le courant circule en sens inverse du courant de charge et la tension aux bornes du condensateur décroît lentement.

[question:EC201]

Dans le cas des courants et tensions alternatifs, nous devons prendre en compte un autre aspect important : un condensateur se comporte comme une résistance dépendante de la fréquence. Celle-ci se décrit par la relation

$|X_C| = \frac{1}{\omega\cdot C} = \frac{1}{2\pi\cdot f \cdot C}$

et est appelée réactance capacitive $X_C$ (cf. formulaire).

Les fondements physiques précis ne seront abordés qu'en classe A. Pour la classe E, il est toutefois déjà important de savoir que la résistance d'un condensateur dépend de la fréquence de façon inversement proportionnelle : si l'on diminue la fréquence, la réactance capacitive $X_C$ augmente. Si au contraire on augmente la fréquence, la résistance diminue en conséquence.

[question:EC202]

---

Nous avons maintenant découvert quelques propriétés électriques fondamentales d'un condensateur ; dans ce qui suit, nous allons encore nous intéresser aux différentes formes de construction. La figure [ref:e_kondensatorvarianten] montre différentes variantes de condensateurs.

<margin>
[photo:206:e_kondensatorvarianten:Variantes de condensateurs]
</margin>

Comme diélectrique, c'est-à-dire comme couche isolante, différents matériaux peuvent être utilisés :

1.  l'air, dans le condensateur variable à air ou l'ajustable à air
2. le film plastique, dans le condensateur bobiné à film
3. la céramique, pour les condensateurs HF à grand facteur de qualité et pour les condensateurs SMD
4. l'oxyde métallique, dans le condensateur électrolytique.

Selon la construction, on distingue en outre :

* les condensateurs fixes, sous forme de condensateurs céramique, de condensateurs à film et de condensateurs électrolytiques
* les condensateurs variables, sous forme de condensateurs variables (à rotor) et de condensateurs ajustables

---

Les *condensateurs à air* et les *condensateurs céramique*, comme le montre la figure [ref:e_aufbau_keramik_c], sont par exemple volontiers utilisés pour les filtres HF. 
[question:ED216] 

<margin>
[picture:923:e_aufbau_keramik_c: Condensateur céramique]
</margin>

Les *condensateurs électrolytiques* (en abrégé ELKO, en français « chimique ») contiennent une fine feuille d'aluminium dépolie, plongée dans un électrolyte (par exemple du borax). L'électrolyte provoque une oxydation chimique de la surface de l'aluminium. La couche d'oxyde qui se forme est très mince, si bien que la capacité augmente très fortement pour un faible encombrement. Toutefois, la couche mince n'a qu'une tenue en tension limitée, indiquée sur le condensateur.
Les condensateurs électrolytiques ne doivent être utilisés qu'en tension continue. Il faut donc respecter la polarité, sans quoi la couche d'oxyde se dégrade et la tenue en tension diminue. Le condensateur est détruit. Tous les autres condensateurs peuvent aussi être raccordés en tension alternative.
[question:EC207]

%<margin>
%TODO: Bild Elko
%</margin>

Pour les condensateurs bobinés à film, des matières plastiques sont transformées par des procédés spéciaux en films extrêmement minces, munies d'électrodes, puis soit enroulées en un bobineau, soit empilées en couches individuelles et assemblées en un condensateur, comme le montre la figure [ref:e_aufbau_wickel_c]. Avec les condensateurs céramique et électrolytiques, ils comptent parmi les types de condensateurs les plus utilisés.

<margin>
[picture:49:e_aufbau_wickel_c:Condensateur bobiné à film]
</margin>

Les condensateurs variables sont souvent utilisés dans les étages de puissance et les réseaux d'adaptation. Chez eux, la capacité peut être réglée : une partie des plaques est montée sur un axe isolé et tourne entre des plaques fixes. La surface de recouvrement efficace des plaques, et donc la capacité, s'en trouve modifiée, comme le montre la figure [ref:e_drehkondensator]. Les condensateurs ajustables fonctionnent selon un principe similaire, mais ne sont pas prévus pour un réglage régulier. Ils servent plutôt à un réglage unique ou occasionnel des montages, par exemple lors de la mise en service ou de l'étalonnage.

[question:EC206]

<margin>
 [picture:840:e_drehkondensator:Constitution d'un condensateur variable]
</margin>

Les symboles utilisés pour les différents condensateurs diffèrent aussi, comme le montre la figure [ref:e_kondensator_schaltzeichen].

<margin>
[picture:924:e_kondensator_schaltzeichen:Symboles des différents types de condensateurs]

Correspondance des symboles : 
a) condensateur fixe 
b) condensateur polarisé / condensateur électrolytique (chimique) / condensateur au tantale
c) condensateur variable 
d) condensateur ajustable pour le réglage
</margin>
