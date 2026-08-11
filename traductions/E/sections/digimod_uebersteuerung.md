Chacun a certainement déjà entendu un amplificateur saturé ou un enregistrement sonore saturé. Si, lors de l'enregistrement ou de la lecture, le volume est trop poussé, des distorsions peuvent apparaître.

Si, par exemple, un signal audio trop fort est appliqué à l'entrée d'un émetteur, des harmoniques peuvent naître et être rayonnées. La figure [ref:uebersteuerung_ft8] montre un signal FT8 ainsi saturé dans le diagramme en cascade : à gauche, en jaune, le signal souhaité, et à sa droite les harmoniques indésirables.

<margin>
[picture:720:uebersteuerung_ft8:Un signal FT8 saturé, tout à gauche le signal souhaité, à sa droite les harmoniques indésirables]
[photo:328:uebersteuerung_ft8_wsjtx:Un signal FT8 saturé dans la cascade du logiciel WSJTX]
</margin>

Des distorsions par saturation peuvent aussi se produire dans l'amplificateur d'émission. Pour l'empêcher, beaucoup de postes radio disposent d'une régulation automatique de niveau (en anglais : Automatic Level Control, ALC). Elle peut intervenir en réduisant le gain.

---

Pour les émissions avec des procédés de transmission numériques à amplitude constante comme par exemple FT8, WSPR ou RTTY, la réaction de l'ALC est souvent l'indice que le signal audio provenant du PC est trop fort et qu'il y a saturation. Cela peut conduire à du *splatter* indésirable sur la bande. C'est pourquoi le signal audio devrait toujours être soigneusement contrôlé avec ces procédés de transmission. Une réduction du niveau par l'ALC serait en soi d'abord sans gravité, puisque dans ces procédés l'information réside dans le déplacement de fréquence. Le déclenchement de l'ALC est néanmoins un indice fort que le signal BF est déjà saturé.

<indepth>
Le [manuel](https://50ohm.de/wsjtx) du logiciel WSJTX donne à ce sujet une bonne recommandation : dans un premier temps, on passe l'émetteur-récepteur en émission en appuyant sur la touche TUNE, afin de produire une tonalité régulière. Cette tonalité peut être vérifiée à l'oreille avec la fonction Monitor de l'appareil, ou contrôlée visuellement dans la cascade du TRX. Aucune distorsion, aucun clic ni autre perturbation ne devrait alors apparaître. On abaisse ensuite lentement le réglage PWR depuis son maximum jusqu'à ce que la sortie HF de l'émetteur diminue légèrement — cela est généralement considéré comme un bon niveau pour l'excitation audio. L'indicateur d'ALC ainsi que la puissance de sortie de l'émetteur-récepteur peuvent également aider à trouver le niveau de signal BF optimal.
</indepth>

Avec les procédés de transmission numériques à amplitude variable (par exemple PSK31, QPSK, 16-QAM), l'ALC peut cependant conduire à de nouveaux problèmes. Selon le volume ou la fréquence, le signal pourrait déclencher l'ALC à des instants différents et avec une intensité différente, et ainsi modifier de manière indésirable l'amplitude au fil du temps. Autrement dit, notre signal utile se retrouve en plus modulé en amplitude. Il en résulte des composantes de fréquence supplémentaires, qui sont rayonnées comme émissions parasites. D'une part, d'autres radioamateurs ou services radio sur des fréquences voisines peuvent en être perturbés. D'autre part, le décodage chez le correspondant est rendu plus difficile.

La survenue de problèmes dus à l'ALC et leur ampleur dépendent de nombreux facteurs. Outre le procédé de transmission utilisé, la réalisation concrète de l'ALC dans l'émetteur-récepteur, par exemple en ce qui concerne les temps de réaction et de maintien, joue aussi un rôle. L'affichage de l'ALC diffère également d'un appareil à l'autre. Un coup d'œil dans le manuel peut renseigner sur le moment où la régulation de niveau intervient et sur la façon dont cela est affiché. On peut cependant dire de manière générale : si l'ALC n'intervient pas, elle ne crée pas non plus de problèmes.

À retenir : avec les procédés de transmission numériques par signal BF, il faut veiller à maintenir le niveau BF suffisamment bas pour qu'aucune saturation ne se produise et que la régulation automatique de niveau n'intervienne pas.

[question:EJ218]
[question:EJ217]
[question:EJ219]