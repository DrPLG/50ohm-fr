Il est également possible de répartir un flux de données sur plusieurs porteuses, situées sur des fréquences différentes mais voisines. Les porteuses ne peuvent toutefois pas être placées arbitrairement près les unes des autres, car elles présentent une certaine largeur du fait des bandes latérales qui apparaissent inévitablement.

Dans le multiplexage par répartition orthogonale de la fréquence (Orthogonal Frequency-Division Multiplexing, OFDM), les porteuses sont placées précisément à l'écartement pour lequel une perturbation mutuelle entre elles (ce que l'on appelle la « diaphonie ») est évitée autant que possible.

Plus la rapidité de modulation par porteuse est élevée, plus l'écartement des porteuses doit être grand. C'est pourquoi on choisit souvent une rapidité de modulation plus faible pour chaque porteuse prise isolément, afin que davantage de porteuses trouvent place. La quantité d'informations transmise reste ici la même, car même si chaque porteuse transporte moins d'informations, un plus grand nombre de porteuses peuvent être utilisées côte à côte. Un écartement des porteuses plus grand est par exemple utile pour rendre le signal plus tolérant aux erreurs de fréquence, que celles-ci proviennent d'écarts de fréquence entre l'émetteur et le récepteur ou de l'effet Doppler lorsque l'émetteur ou le récepteur est en mouvement.

Un avantage de cette approche est que les perturbations à bande étroite ne gênent qu'une seule porteuse ou quelques-unes. En association avec les procédés de correction d'erreurs à transmission redondante de données, que nous avons découverts quelques chapitres plus tôt, il est ainsi possible d'obtenir une transmission sans erreur malgré des perturbations à bande étroite.

<margin>
[picture:704:ofdm:Spectre de fréquence d'un signal OFDM simple]
</margin>

[question:AE421]

Un autre avantage découle de la plus faible rapidité de modulation de chaque porteuse. Du fait de cette rapidité de modulation plus faible, la durée de chaque symbole est plus longue. En cas de décalages temporels dus à la propagation par trajets multiples, la part de recouvrement entre les signaux (ce que l'on appelle l'interférence entre symboles ou diaphonie entre symboles) est alors d'autant plus faible. Il peut aussi arriver que certaines fréquences soient annulées, ou du moins fortement atténuées, par la propagation par trajets multiples (on parle alors de fading sélectif en fréquence). Cela peut être compensé par les mêmes mécanismes que les perturbations à bande étroite mentionnées plus haut. En cas de propagation par trajets multiples, l'OFDM est donc particulièrement avantageuse.

[question:AE422]