<margin>
[include:hamnet_map]
</margin>

Le HAMNET occupe une place particulière dans le radioamateurisme — un réseau réservé exclusivement aux radioamateurs. HAMNET (Highspeed Amateurradio Multimedia Network) est un réseau basé sur IP, développé et exploité par des radioamateurs. Dans son fonctionnement, il ressemble à Internet, mais utilise majoritairement des liaisons radio pour la transmission des données.

À l'origine, HAMNET a été conçu comme remplacement progressif du réseau Packet Radio existant depuis les années 1980, qu'il a entre-temps presque complètement supplanté. Les liaisons de données rapides entre les différents points d'accès et nœuds sont réalisées principalement sur les bandes micro-ondes 6 cm, 9 cm et 13 cm. Pour accéder au HAMNET, il faut une vue dégagée vers un nœud HAMNET avec accès utilisateur, ainsi qu'un émetteur-récepteur WLAN approprié muni d'une antenne directive.

---

<margin>
Le *DARC* propose à ses membres un accès VPN via la [HAMCloud](https://50ohm.de/hc). Cela permet l'accès au HAMNET même lorsqu'aucun accès direct par radio n'est possible.   

[Devenez membre du DARC dès maintenant !](https://50ohm.de/mw)
</margin>

On peut utiliser le Hamnet exactement comme Internet, dans le cas le plus simple avec un navigateur web. Cela est possible parce que le protocole Internet (IP), et tout ce qui repose sur lui, peut aussi être utilisé à d'autres fins que pour Internet.

[question:EE414]

Le Hamnet est, tout comme Internet, un assemblage de nombreux réseaux individuels. Si deux participants ne peuvent pas s'atteindre directement, les paquets de données sont alors relayés par d'autres nœuds.

[question:EE412]

Dans des ensembles aussi vastes, on met de l'ordre en numérotant tous les ordinateurs. Les numéros des participants s'appellent adresses IP. Il existe les versions IPv4 et IPv6. Pour notre hobby, il suffit la plupart du temps de s'occuper de la version 4, plus simple.

Les adresses IPv4 sont des nombres binaires d'une longueur de 32 bits. On écrit quatre nombres décimaux, dont chacun représente 8 bits, séparés par des points. Le plus grand nombre possible est 255, correspondant au nombre binaire 11111111.

Chez tous les ordinateurs qui se trouvent dans le même réseau, le début des adresses IP est identique. Cette partie réseau a une longueur variable. Les grands réseaux ont besoin de beaucoup des 32 bits pour numéroter leurs ordinateurs à la fin, dans ce qu'on appelle la partie hôte. Ils utilisent pour cela une partie réseau plus courte. Pour les petits réseaux, c'est exactement l'inverse. On connaît ce principe du réseau téléphonique. Les plus grandes villes ont des indicatifs à trois chiffres, par exemple 089, et les petits réseaux locaux des indicatifs à cinq ou six chiffres comme 038725.

---

La longueur de la partie réseau s'indique le plus simplement par une barre oblique derrière l'adresse IP. 141.17.5.18/24 signifie par exemple que la partie réseau est longue de 24 bits. Chez tous les ordinateurs du même réseau, l'adresse commence par 141.17.5. Pour numéroter toutes les stations, il ne reste que 8 des 32 bits. Il s'agit donc d'un réseau relativement petit.

<indepth>
On rattache parfois les réseaux à une classe, bien que ce système ait été abandonné depuis longtemps. La classe A signifiait /8, la classe B /16 et la classe C /24.
</indepth>


---

La plupart des équipements réseau exigent une autre écriture, à savoir le masque de sous-réseau (voir figure [ref:netzmaske]). Il s'agit de 32 bits dans la même notation que les adresses IP. Les bits qui représentent la partie réseau sont marqués par un 1, et les bits de la partie hôte par un 0. Le masque de réseau commence donc par autant de uns que la partie réseau est longue. Le reste est complété par des zéros. Les réseaux domestiques et les petits réseaux d'entreprise utilisent presque toujours le masque 255.255.255.0, qui signifie la même chose que /24.

Les équipements réseau ne peuvent communiquer directement entre eux qu'à l'intérieur de leur propre réseau local. Ils le reconnaissent au fait que leur propre adresse IP et leur masque de sous-réseau donnent la même partie réseau que chez le partenaire. Dans tous les autres cas, ils envoient les données à un routeur. C'est une station intermédiaire qui relie deux réseaux ou plus entre eux. Quand un équipement est directement relié à plusieurs réseaux, il possède une adresse IP propre dans chacun d'eux.

<margin>
[picture:699:netzmaske:Adresse IPv4 et masque de réseau en écriture décimale et binaire]
</margin>

<margin>
[picture:706:netzwerk:Extrait d'une infrastructure de réseau]
</margin>

Tous les participants d'un réseau doivent pouvoir utiliser le routeur quasi simultanément. C'est pourquoi, dans les réseaux IP, aucune liaison fixe n'est établie. À la place, les ordinateurs découpent tous les flux de données en paquets, c'est-à-dire en courts segments. Le relayage de ces paquets individuels s'appelle la commutation de paquets.

[question:EE413]