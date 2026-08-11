<margin>
[picture:804:mischer_linear_vs_nichtlinear:Résistance linéaire et diode non linéaire]
</margin>

Les caractéristiques de commande des modules ou des composants peuvent avoir un caractère linéaire, non linéaire, ou mixte par intervalles. Une résistance, par exemple, a une caractéristique linéaire, alors que celle d'une diode est non linéaire [ref:mischer_linear_vs_nichtlinear].

Dans la partie linéaire des caractéristiques de commande, aucune distorsion des signaux d'entrée ne se produit, car à toute variation d'un signal d'entrée correspond une variation du signal de sortie de même pourcentage. Mathématiquement, cela correspond à un comportement linéaire (addition). La résistance est un exemple de caractéristique de commande linéaire sur toute son étendue. Sur une caractéristique linéaire, ou dans la partie linéaire d'une caractéristique, il ne se produit **aucun** processus de mélange.

Dans la partie non linéaire des caractéristiques de commande, les signaux d'entrée subissent des distorsions, car la variation d'un signal d'entrée ne provoque pas une variation du signal de sortie de même pourcentage. Mathématiquement, cela correspond à un comportement non linéaire dans lequel a lieu une multiplication des grandeurs d'entrée ; il apparaît de ce fait des produits de mélange supplémentaires (dépendant de la forme de la caractéristique). C'est pourquoi un processus de mélange a toujours lieu dans la partie non linéaire des caractéristiques de commande. Les produits de mélange créent toujours des fréquences supplémentaires dans le signal de sortie, qui s'y présentent principalement sous forme de sommes et de différences des fréquences d'entrée.

En pratique, il se forme cependant aussi de nombreux produits de mélange indésirables d'ordre supérieur, qu'il faut supprimer de façon ciblée par des mesures techniques telles que le filtrage.

%TODO EVTL. VERWEIS AUF WEITERE LITERATUR ODER MATHEMATISCHEN HINTERGRUND

[question:AF212]

---
<margin>
[picture:805:mischer_ringmischer:Mélangeur équilibré, mélangeur en anneau ou encore modulateur en anneau]
</margin>

Le but d'un mélangeur est que seuls les produits de mélange souhaités apparaissent idéalement à sa sortie, et que les produits de mélange indésirables ainsi que les signaux d'entrée y soient supprimés au maximum.

C'est avec un mélangeur équilibré que l'on atteint le mieux cet objectif. Celui-ci est constitué de 4 diodes ou transistors montés en anneau [ref:mischer_ringmischer]. Grâce à sa structure ainsi symétrique, les signaux d'entrée sont supprimés au maximum dans la sortie. Les autres formes de mélangeurs, comme par exemple le mélangeur à double diode, le mélangeur à double transistor ou le mélangeur additif à diode, laissent toujours passer aussi l'un des signaux d'entrée vers la sortie, du fait de leur structure dissymétrique.

<indepth>
Fonctionnement d'un mélangeur en anneau :

L'oscillateur local ($U_2$ sur le schéma) rend toujours conductrices deux diodes opposées pendant une alternance, tandis que les deux autres diodes sont bloquées. À l'alternance suivante de l'oscillateur local, la situation s'inverse exactement. Pour cela, l'amplitude de l'oscillateur local ($U_2$) doit être suffisamment élevée pour que les diodes puissent être suffisamment commandées pendant les alternances positives et négatives.

L'anneau de diodes travaille ainsi comme un inverseur de polarité pour le signal présent à l'entrée ($U_1$).
Pour obtenir un bon résultat de mélange du point de vue des produits de mélange indésirables et de la suppression du signal d'entrée, l'amplitude de ce dernier doit être nettement plus faible que celle de l'oscillateur local.
Les valeurs optimales sont atteintes avec les mélangeurs en anneau dits « high level », dont le niveau d'entrée de l'oscillateur local peut atteindre $\qty{10}{\milli\watt}$.
</indepth>

<tip>
Il importe de savoir distinguer le mélangeur en anneau du montage d'un redresseur à diodes, qui lui ressemble beaucoup : dans le mélangeur en anneau, les diodes sont montées les unes derrière les autres en anneau (la cathode de chacune est reliée à l'anode de la diode suivante). Dans le redresseur, en revanche, ce sont toujours 2 cathodes et 2 anodes qui sont reliées entre elles.
</tip>
  
Le mélangeur équilibré, que l'on appelle aussi mélangeur en anneau ou modulateur en anneau, est le mieux adapté pour supprimer les signaux de sortie indésirables.

% FEEDBACK: Wie funktioniert das ganze? Das wird nicht klar! Zusätlich: Hinweis zur verwechslung mit Brückengleichrichter!
% FEEDBACK-ANTWORT: Wir haben den Artikel um einen Tipp und Vertiefung hinsichtlich der angesprochenen Punkte erweitert.

[question:AF213]
[question:AF214]