<margin>
[picture:804:mischer_linear_vs_nichtlinear:Résistance linéaire et diode non linéaire]
</margin>


Les composants et les modules peuvent se comporter de façon *linéaire* ou *non linéaire*. Dans un composant linéaire, la grandeur de sortie suit la grandeur d'entrée selon une relation fixe. Une résistance idéale possède par exemple une caractéristique linéaire. La caractéristique d'une diode est en revanche non linéaire (voir [ref:mischer_linear_vs_nichtlinear]).

Un comportement purement linéaire ne suffit pas à un processus de mélange. Lorsque plusieurs signaux sont transmis par un montage linéaire, ils peuvent certes être amplifiés, atténués ou additionnés entre eux, mais ils ne s'influencent pas mutuellement. Il n'apparaît de ce fait aucune composante de fréquence nouvelle.

Pour qu'un mélange puisse avoir lieu, les signaux d'entrée doivent être combinés entre eux. Cela peut se produire par exemple grâce à la caractéristique non linéaire d'une diode ou d'un transistor. Une autre possibilité fréquemment employée consiste à allumer et éteindre rapidement le signal d'entrée, ou à en inverser la polarité, à l'aide du signal de l'oscillateur. Une telle commutation n'est pas non plus un processus linéaire et fait que les deux signaux sont combinés entre eux.

C'est précisément cette propriété qui est exploitée de façon délibérée dans un mélangeur. C'est pourquoi les étages mélangeurs travaillent avec des composants non linéaires, ou avec des montages dans lesquels des transistors ou des diodes sont commutés par le signal de l'oscillateur.
En pratique, il se forme cependant aussi de nombreux produits de mélange indésirables d'ordre supérieur, qu'il faut supprimer de façon ciblée par des mesures techniques telles que le filtrage.

[question:AF212]

Le but d'un mélangeur est que seuls les produits de mélange souhaités apparaissent idéalement à sa sortie, et que les produits de mélange indésirables ainsi que les signaux d'entrée y soient supprimés au maximum.

On atteint le mieux ce but à l'aide de ce qu'on appelle un mélangeur équilibré. Celui-ci est constitué de 4 diodes ou transistors montés en anneau [ref:mischer_ringmischer]. Grâce à sa structure ainsi symétrique, les signaux d'entrée sont supprimés au maximum dans la sortie. D'autres formes de mélangeurs, comme par ex. le mélangeur à double diode, le mélangeur à double transistor ainsi que le mélangeur additif à diode, laissent toujours passer aussi vers la sortie, du fait de leur structure dissymétrique, l'un des signaux d'entrée.

<indepth>
Fonctionnement d'un mélangeur en anneau :

L'oscillateur local ($U_2$ sur le schéma) rend toujours conductrices deux diodes opposées pendant une alternance, tandis que les deux autres diodes sont bloquées. À l'alternance suivante de l'oscillateur local, la situation s'inverse exactement. Pour cela, l'amplitude de l'oscillateur local ($U_2$) doit être suffisamment élevée pour que les diodes puissent être suffisamment commandées pendant les alternances positives et négatives.

L'anneau de diodes travaille ainsi comme un inverseur de polarité pour le signal présent à l'entrée ($U_1$).
Pour obtenir un bon résultat de mélange du point de vue des produits de mélange indésirables et de la suppression du signal d'entrée, l'amplitude de ce dernier doit être nettement plus faible que celle de l'oscillateur local.
Les valeurs optimales sont atteintes avec les mélangeurs en anneau dits « high level », dont le niveau d'entrée de l'oscillateur local peut atteindre $\qty{10}{\milli\watt}$.

<webonly>
[include:applet_ringmodulator]
</webonly>
<latexonly>
[picture:805:mischer_ringmischer:Mélangeur équilibré, mélangeur en anneau ou encore modulateur en anneau]
</latexonly>
</indepth>

<tip>
Il importe de savoir distinguer le mélangeur en anneau du montage d'un redresseur à diodes, qui lui ressemble beaucoup : dans le mélangeur en anneau, les diodes sont montées les unes derrière les autres en anneau (la cathode de chacune est reliée à l'anode de la diode suivante). Dans le redresseur, en revanche, ce sont toujours 2 cathodes et 2 anodes qui sont reliées entre elles.
</tip>
  
Le mélangeur équilibré, que l'on appelle aussi mélangeur en anneau ou modulateur en anneau, est le mieux adapté pour supprimer les signaux de sortie indésirables.

[question:AF213]
[question:AF214]
