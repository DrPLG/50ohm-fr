Comme nous l'avons déjà appris, les piles fournissent une tension électrique parce que des charges y sont séparées. Cela est obtenu par des processus électrochimiques. Ceux-ci se déroulent dès que le circuit électrique est fermé. Les accumulateurs, appelés en abrégé accus, fonctionnent de manière très similaire. Ils ont toutefois la particularité d'être rechargeables. Pour cela, une tension est appliquée à l'accu et la réaction électrochimique se déroule en sens inverse. La décharge peut ensuite recommencer. Les piles, en revanche, ne peuvent pas être rechargées : elles ne sont utilisables qu'une seule fois.

Dans les appareils radio portatifs, on utilise le plus souvent des accus, mais parfois aussi des piles. Pour exploiter des stations radio indépendamment du réseau électrique, par exemple lors d'un fieldday, on utilise fréquemment des accus.

Le marquage imprimé sur les piles (figure [ref:n_Bat_AA]) indique par exemple le pôle plus et le pôle moins et rappelle qu'il faut respecter la polarité. Sur les piles, l'avertissement « non rechargeable » doit toujours être respecté.

La figure [ref:n_schaltzeichen_batt] montre le symbole électrique d'une pile ou d'un accu. Le trait long du symbole désigne le pôle plus, le trait court le pôle moins. Comme moyen mnémotechnique : un signe plus nécessite 2 traits, un signe moins un seul.

[question:NB201]
[question:NB203]

<margin>
[photo:89:n_Bat_AA:Une pile avec marquage des pôles et avertissements]
</margin>

<margin>
[picture:517:n_schaltzeichen_batt:Symbole électrique d'une pile]
</margin>

<webindepth>
Il existe les piles et accus les plus divers, avec différentes tensions, capacités et formes :
* Les tensions fréquemment indiquées sur les piles ou accus sont par exemple $\qty{1,5}{\volt}$ ou $\qty{9}{\volt}$. Mais il en existe aussi avec d'autres tensions. Les voitures radiocommandées utilisent par exemple le plus souvent $\qty{7,2}{\volt}$. Dans les outils sur accu, on trouve souvent des accus de $\qty{18}{\volt}$, $\qty{20}{\volt}$ ou $\qty{40}{\volt}$.
* La capacité d'une pile ou d'un accu est exprimée en ampères-heures ($\unit{\ampere\hour}$). Si un accu a une capacité de $\qty{5}{\ampere\hour}$, il peut faire circuler un courant d'un ampère pendant 5 heures — ou encore, par exemple, un courant de 0,5 ampère pendant 10 heures, ou un courant de $\qty{5}{\ampere}$ pendant une heure seulement. Sur les piles, la capacité n'est souvent pas indiquée. Les piles domestiques usuelles ont souvent une capacité de moins de $\qty{5}{\ampere\hour}$. Les gros accus peuvent atteindre une capacité de $\qty{100}{\ampere\hour}$ ou plus. Sur les accus, contrairement aux piles, la capacité est pratiquement toujours indiquée.
* Concernant les formes, les cellules cylindriques AA et AAA, utilisées dans la plupart des appareils domestiques, sont très connues. Mais il existe, surtout pour les accus, toutes sortes de formes. Souvent même des formes qui ne conviennent qu'à un seul appareil.
</webindepth>

<margin>
[photo:209:batterien_und_akkus_sammlung:Différentes piles et différents accus]
</margin>

<attention>
Les accus ne devraient jamais être complètement déchargés. Cette décharge dite profonde peut endommager l'accu. En pratique, la décharge se reconnaît au fait que la tension de l'accu baisse peu à peu légèrement. Le prélèvement de courant doit être arrêté avant que la tension minimale indiquée par le fabricant ne soit franchie à la baisse.
</attention>

De nombreux appareils nécessitent plusieurs piles. En règle générale, cela sert à augmenter la tension, lorsque la tension d'une seule pile, par exemple $\qty{1,5}{\volt}$, ne suffit pas au fonctionnement. Dans le compartiment à piles de l'appareil, elles sont montées en série, de sorte que le pôle moins de la pile précédente rencontre le pôle plus de la suivante. La tension aux extrémités de cette chaîne se calcule ainsi :

$\text{Tension totale} = \text{Nombre de piles} \cdot \text{Tension d'une pile}$

[question:NB204]

---

De manière générale, il faut éviter tout court-circuit avec les piles et les accus. Avec les accus modernes puissants en particulier, il existe un risque de surchauffe. Ils peuvent prendre feu ou provoquer un incendie par le courant de court-circuit qui en résulte.

<danger>
Alors que sur les alimentations secteur un fusible peut arrêter le passage du courant en cas de défaut, ce mécanisme de protection fait le plus souvent défaut sur les piles et les accus. L'intensité que les piles et les accus peuvent fournir dépasse souvent plusieurs fois le courant maximal des alimentations secteur. C'est particulièrement vrai pour les accus de grande capacité, comme les batteries automobiles, qui peuvent fournir brièvement $\qty{1000}{\ampere}$ et plus. Lors de l'utilisation d'accus externes de grande capacité, il faut impérativement prévoir un fusible supplémentaire, comme celui montré par exemple dans la figure [ref:n_Bat_Sicherung] !
[photo:90:n_Bat_Sicherung:Boîtier de raccordement avec fusibles automobiles et sorties protégées contre les inversions de polarité pour la protection d'accus puissants]
</danger>

[question:ND110] 

Les accus font appel aux technologies les plus diverses, basées sur différentes réactions électrochimiques : depuis de nombreuses décennies, des batteries au plomb sont utilisées dans les automobiles. Les petits appareils portables utilisaient autrefois des accus au nickel-cadmium (NiCd), puis la technologie nickel-hydrure métallique (NiMH). Dans les téléphones mobiles, les appareils photo numériques ou les ordinateurs portables dominent aujourd'hui les accus à technologie lithium-ion. Dans le radioamateurisme, on utilise aussi de plus en plus des compositions lithium-fer-phosphate (LiFePO4).

Les différences entre les réactions électrochimiques doivent être prises en compte lors de la charge de ces différents types d'accus. Il faut utiliser des chargeurs spécialement adaptés à chaque technologie. Des processus de charge et de décharge inappropriés peuvent conduire à une surchauffe des accus. En cas de contact, des brûlures dangereuses peuvent alors se produire. Des explosions des accus et des incendies sont également possibles par surchauffe. Les liquides libérés peuvent provoquer des brûlures chimiques ou des intoxications.

<attention>
Les piles et les accus doivent toujours être éliminés de manière appropriée. Ils n'ont pas leur place dans les ordures ménagères ! Cela est signalé par le symbole de la poubelle barrée (voir figure [ref:n_Bat_AA]).
</attention>

[question:NK306] 

<latexonly>
\newpage
</latexonly>
