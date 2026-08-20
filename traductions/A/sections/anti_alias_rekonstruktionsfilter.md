Lors de la conversion A/N et N/A, traitement analogique et traitement numérique du signal sont reliés l'un à l'autre. Des filtres analogiques sont alors nécessaires aussi bien avant le convertisseur A/N qu'après le convertisseur N/A. La figure [ref:a_adc_dac_filter] montre l'ensemble de la chaîne du signal. Du côté de l'entrée se trouve, en amont du convertisseur A/N, un *filtre anti-repliement*. Il limite la plage de fréquences du signal d'entrée analogique avant que celui-ci ne soit échantillonné. Après le traitement numérique du signal, le convertisseur N/A produit de nouveau un signal analogique. Un *filtre de reconstruction* placé en aval élimine alors les composantes de signal à fréquence élevée indésirables. Nous examinons dans la section suivante pourquoi ces deux filtres sont nécessaires.

<margin>
[picture:1131:a_adc_dac_filter:Conversion A/N et N/A avec filtres anti-repliement et de reconstruction]
</margin>

---

Nous savons, d'après la leçon sur le théorème d'échantillonnage, qu'un signal doit être échantillonné à une fréquence d'échantillonnage suffisamment élevée. Pour un signal dont la plus haute fréquence à saisir est $f_\mathrm{max}$, la fréquence d'échantillonnage doit être supérieure à $2\cdot f_\mathrm{max}$.

Par une antenne, nous recevons cependant en règle générale de nombreux signaux différents — y compris des signaux dont les fréquences se situent au-dessus de la plage de fréquences que nous voulons effectivement traiter. Si de telles composantes de signal parviennent au convertisseur A/N alors que sa fréquence d'échantillonnage n'est pas suffisante pour ces fréquences, elles peuvent apparaître dans le signal numérique sous la forme d'autres fréquences, en réalité inexistantes. On les appelle des *alias*.

Pour empêcher cela, on place un *filtre anti-repliement* en amont de l'entrée du convertisseur A/N. Il s'agit, selon l'application, par exemple d'un filtre passe-bas ou d'un filtre passe-bande. Un filtre passe-bande pourrait p. ex. être utilisé pour la parole. Le filtre doit supprimer suffisamment les composantes de signal indésirables susceptibles de conduire à du repliement lors de l'échantillonnage. En particulier, les composantes de fréquence situées au-dessus de la moitié de la fréquence d'échantillonnage ne doivent pas parvenir sans entrave au convertisseur A/N.

[question:AF622]
[question:AF623]

<indepth>
Un exemple parlant de *repliement* se présente aussi à nous dans la vie courante, avec les images numériques. Si l'on photographie avec un appareil des structures très fines et régulièrement répétées, par exemple un grillage à mailles serrées, un tissu à fines rayures ou une moustiquaire, de plus grands motifs peuvent soudain apparaître dans l'image, alors qu'ils n'existent pas du tout dans l'original. On les appelle des *motifs de moiré*.

La cause est semblable à celle rencontrée lors de l'échantillonnage d'un signal électrique. Un capteur d'appareil photo ne peut pas saisir une image en un nombre quelconque d'endroits ; il ne possède qu'un nombre fini de points d'image. Si une structure est plus fine que la résolution spatiale du capteur, elle n'est plus échantillonnée de façon univoque. De la structure fine réellement présente peut ainsi naître, en apparence, une autre structure, plus grossière.

Dans le convertisseur A/N, le même principe se produit sur l'axe du temps : si une fréquence de signal trop élevée est échantillonnée à une fréquence d'échantillonnage trop basse, une autre fréquence, plus basse, apparaît dans le signal numérisé, alors qu'elle n'existait pas du tout à l'origine.

Un motif de moiré peut donc être considéré comme un exemple visible de la façon dont un échantillonnage insuffisant fait naître de nouvelles structures apparentes.

% TODO: Bild besorgen
%<margin>
%[picture:XXXX:a_moire:Moiré-Muster als Beispiel für räumliches Aliasing]
%</margin>
</indepth>

---

Le convertisseur A/N a en outre besoin d'un générateur d'horloge, que l'on appelle aussi générateur d'horloge d'échantillonnage. Celui-ci fixe les instants auxquels le signal d'entrée est échantillonné et détermine ainsi la fréquence d'échantillonnage. La fréquence d'échantillonnage peut être réglée de façon fixe ou être pilotée par exemple par un microcontrôleur.

<margin>
[picture:1132:a_anit_alias:Filtre anti-repliement, convertisseur A/N et générateur d'horloge]
</margin>

[question:AF620]

---

De l'autre côté du traitement numérique du signal, le convertisseur N/A assure l'opération inverse. Il reconvertit les échantillons numériques en valeurs de tension analogiques. Comme les différentes valeurs ne sont délivrées qu'à intervalles de temps fixes, l'allure du signal obtenue à la sortie du convertisseur N/A n'est d'abord pas parfaitement lisse.

La sortie à temps discret fait naître, à côté du signal utile souhaité, des composantes de signal indésirables à fréquence plus élevée (p. ex. à la figure [ref:a_adc_4bit], les transitions rapides entre les valeurs discrètes du signal de sortie contiennent les composantes à fréquence élevée). Pour supprimer celles-ci, on place un *filtre de reconstruction* en aval du convertisseur N/A. Là encore, on peut utiliser selon l'application par exemple un filtre passe-bas ou un filtre passe-bande.

Le filtre de reconstruction laisse passer la plage de fréquences utile souhaitée et supprime les composantes de signal à fréquence plus élevée indésirables du convertisseur N/A. Il en résulte de nouveau, à la sortie, un signal analogique aussi propre que possible (cf. figure [ref:a_adc_12bit], le filtre de reconstruction lisse le signal).

[question:AF624]
[question:AF625]

<margin>
[picture:300:a_adc_4bit:Signal avant le filtre de reconstruction]
[picture:299:a_adc_12bit:Signal après le filtre de reconstruction]
</margin>
