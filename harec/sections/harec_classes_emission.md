Une **classe d'émission** [index:Classe d'émission] décrit en trois caractères la façon dont un émetteur transmet l'information. Le code est celui de l'**appendice 1 du Règlement des radiocommunications**, auquel renvoie la décision ARCEP n° 2012-1241.

| l: Position | l: Ce qu'elle décrit | X: Valeurs principales |
| 1re lettre | modulation de la porteuse principale | **N** porteuse non modulée, **A** amplitude double bande latérale, **H** BLU porteuse complète, **R** BLU porteuse réduite, **J** BLU porteuse supprimée, **F** fréquence, **G** phase |
| chiffre | nature du signal modulant | **1** numérique sans sous-porteuse, **2** numérique avec sous-porteuse modulante, **3** analogique |
| 2e lettre | type d'information transmise | **A** télégraphie auditive, **B** télégraphie automatique, **C** fac-similé, **D** données, **E** téléphonie, **F** télévision |
[table:harec_code_emission:Les trois caractères d'une classe d'émission]

Les classes courantes :

* $\mathrm{A1A}$ : télégraphie Morse par tout ou rien, reçue à l'oreille ;
* $\mathrm{A3E}$ : téléphonie en modulation d'amplitude double bande ;
* $\mathrm{J3E}$ : téléphonie en bande latérale unique à porteuse supprimée ;
* $\mathrm{F3E}$ : téléphonie en modulation de fréquence ;
* $\mathrm{G3E}$ : téléphonie en modulation de phase.

<tip>
**Méthode — décoder une classe.** Lire les trois caractères un par un, dans l'ordre : comment la porteuse est modulée, par quel signal, pour transmettre quoi. $\mathrm{F2A}$ : modulation de fréquence, signal numérique sur une sous-porteuse, télégraphie auditive — un Morse transmis par une tonalité en FM. Pour retrouver une classe à partir d'une description, faire l'inverse.
</tip>

---

Le même appendice prévoit, devant la classe, quatre caractères pour la **largeur de bande nécessaire**. Trois chiffres et une lettre, la lettre tenant lieu de virgule et donnant l'unité : **H** hertz, **K** kilohertz, **M** mégahertz, **G** gigahertz. Ainsi $\mathrm{2K70}$ signifie $\qty{2,7}{\kilo\hertz}$, $\mathrm{6M00}$ signifie $\qty{6}{\mega\hertz}$, et $\mathrm{2K70J3E}$ désigne une BLU téléphonique de $\qty{2,7}{\kilo\hertz}$.

---

**Autorisations.** Toutes les classes d'émission sont ouvertes au titulaire du certificat actuel, dans la limite de la largeur de bande occupée de chaque bande. La décision n° 2012-1241 a été prise, entre autres, pour permettre les **modes numériques**. Seuls les titulaires de l'ex-classe 3 restent limités à six classes : $\mathrm{A1A}$, $\mathrm{A2A}$, $\mathrm{A3E}$, $\mathrm{F3E}$, $\mathrm{G3E}$ et $\mathrm{J3E}$.

Le principe de l'article 15.9 du RR s'applique à tous : choisir la classe d'émission qui cause le **minimum de brouillage**, et réduire autant que possible la largeur de bande occupée.
