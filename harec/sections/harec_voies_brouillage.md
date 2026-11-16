Même un émetteur parfaitement propre peut perturber un appareil voisin. On distingue la **perturbation**, quand la station dépasse les limites d'émissions non désirées, de l'**influence perturbatrice**, quand la station est conforme mais que l'appareil voisin réagit au **signal utile** lui-même.

Le signal HF entre dans l'appareil perturbé par trois **voies de pénétration** [index:Voie de pénétration], seules ou combinées :

* par **son antenne de réception** (téléviseur, radio, récepteur satellite) ;
* par **rayonnement direct** dans un boîtier mal blindé ;
* par **conduction** le long des câbles : secteur, haut-parleurs, téléphone, réseau, antenne.

<margin>
[picture:747:harec_conduction:Pénétration du signal par les câbles de raccordement]
</margin>

---

Une fois dans l'appareil, le signal agit de trois façons.

* **Saturation, blocage.** Près d'une antenne d'émission, le champ peut être très fort. L'étage d'entrée d'un récepteur voisin sature : sa sensibilité chute, ou la réception cesse. Télécommandes de portail et lampes à capteur tactile y sont sensibles.
* **Intermodulation** [index:Intermodulation]. Deux signaux forts $f_1$ et $f_2$ entrent dans un étage **non linéaire**, qui se comporte comme un mélangeur : il fabrique des fréquences $m \cdot f_1 \pm n \cdot f_2$. Les plus gênantes sont celles du **troisième ordre**, $2f_1 - f_2$ et $2f_2 - f_1$, car elles tombent près des signaux d'origine, souvent dans la bande reçue. Ces « signaux fantômes » n'existent qu'en présence des deux signaux. La **transmodulation** [index:Transmodulation] est voisine : la modulation d'un émetteur puissant se retrouve imprimée sur le signal qu'on écoute.
* **Détection dans les circuits audio.** Une jonction de transistor, ou un contact oxydé, **redresse** la HF : la modulation devient audible dans une chaîne hi-fi, un interphone, un téléphone, parfois même un amplificateur éteint. Le même effet de redressement dans un contact rouillé, près de l'antenne d'émission, peut fabriquer et **rayonner** des produits de mélange : c'est « l'effet rouille ».

<margin>
[picture:1095:harec_intermodulation:Produits d'intermodulation de deux signaux, troisième ordre en évidence]
</margin>

<tip>
**Méthode — produits du troisième ordre.** Deux émetteurs à $\qty{145,0}{\mega\hertz}$ et $\qty{145,5}{\mega\hertz}$ : $2 \times \num{145,0} - \num{145,5} = \qty{144,5}{\mega\hertz}$ et $2 \times \num{145,5} - \num{145,0} = \qty{146,0}{\mega\hertz}$. Les produits sont espacés de l'écart des deux signaux, de part et d'autre.
</tip>
