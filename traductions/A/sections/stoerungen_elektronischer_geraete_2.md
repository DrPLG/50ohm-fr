Dans les leçons des classes N et E, nous avons déjà fait connaissance avec les influences perturbatrices typiques sur les appareils et installations électroniques — par exemple par pénétration directe par rayonnement dans le boîtier ou par couplage dans les câbles de raccordement — ainsi qu'avec les contre-mesures et les comportements appropriés. En classe A, ces aspects sont encore un peu approfondis. 

[question:AJ105]

Lorsque des perturbations de réception apparaissent sur des récepteurs numériques de construction personnelle, une cause possible peut en être un mauvais blindage du récepteur. Il est alors indiqué de monter le circuit imprimé du récepteur dans un boîtier métallique relié à la terre. Sur les récepteurs SDR en particulier, ou sur les réalisations personnelles en technique SDR, un bon blindage est absolument nécessaire pour éviter les pénétrations par rayonnement. Inversement, les rayonnements indésirables de ces appareils s'en trouvent également réduits.

[question:AJ103]

---

En classe E, nous nous sommes déjà occupés des couplages dans les lignes secteur. Il existe toutefois une autre contre-mesure, que nous allons examiner de plus près ci-après. Si des perturbations pénètrent par conduction par la ligne d'alimentation secteur, il est indiqué d'installer un filtre secteur sous la forme d'un filtre passe-bas (cf. figure [ref:a_netzfilter] et figure [ref:a_netzfilter_draw]). Ces filtres sont disponibles sous forme d'appareils tout faits, conformes aux prescriptions VDE. 

[question:AJ116]
[question:AJ117]
[question:AJ118]

<margin>
[photo:244:a_netzfilter:Filtre secteur]
[picture:367:a_netzfilter_draw:Schéma d'un filtre secteur]
</margin>

Les différents procédés de transmission ont, du fait de leur caractéristique de modulation, des effets différents en matière d'influence perturbatrice sur les appareils et les câbles. Les types de modulation CW et SSB en particulier (dans lesquels l'amplitude varie rapidement) conduisent souvent à des influences perturbatrices dans les câbles de haut-parleur, suivies d'un redressement de la HF sur les jonctions base-émetteur dans la partie BF des amplificateurs. La jonction base-émetteur se comporte ici comme une diode et redresse la HF. La BF ainsi démodulée devient de ce fait audible dans les haut-parleurs.

[question:AJ107]
[question:AJ106]

Pour protéger les récepteurs DVB-T des signaux forts d'un émetteur radioamateur VHF/UHF situé à proximité immédiate, il convient de monter un filtre passe-haut dans le câble d'antenne du récepteur DVB-T. Cela n'est toutefois efficace qu'avec des antennes de réception passives. Les préamplificateurs d'antenne TV non sélectifs en particulier sont rapidement saturés par les signaux d'émission voisins, car ils amplifient une large plage de fréquences.
Avec des antennes de réception actives, un filtre passe-haut doit être monté en amont du préamplificateur d'antenne de l'antenne.
Lors du montage de filtres, il faut aussi tenir compte de l'atténuation d'insertion des filtres dans leur bande passante. Celle-ci devrait être aussi faible que possible et ne pas dépasser $\qtyrange{2}{3}{\dB}$, afin de laisser passer le plus librement possible le signal de réception souhaité.

[question:AJ113]
[question:AJ114]
[question:AJ108]

D'une manière générale, il est judicieux d'installer, après un émetteur décamétrique puissant, un filtre passe-bas de fréquence de coupure comprise entre $\qtyrange{30}{40}{\mega\hertz}$. L'emploi d'une boîte d'accord d'antenne en configuration passe-bas (filtre en Pi ou LC) permet également d'obtenir un effet passe-bas, qui supprime efficacement les émissions d'harmoniques supérieures.

[question:AJ112]
[question:AJ104]

Les signaux d'émission puissants d'une station radioamateur peuvent provoquer, sur les récepteurs DAB, TV et FM, des perturbations de réception, des bruits parasites ou des coupures, artefacts et silences (en particulier sur les récepteurs numériques tels que DAB/DVB-T). Ces perturbations sont souvent provoquées par la saturation de l'entrée du récepteur du fait de fortes intensités de signal au lieu de réception, et conduisent à une diminution de la sensibilité du récepteur ou à la saturation de son étage d'entrée.

[question:AJ110]
[question:AJ111]
[question:AJ109]

Pour éviter les problèmes précités, le radioamateur ne devrait donc toujours travailler qu'avec la puissance d'émission minimale nécessaire à une communication satisfaisante.

[question:AJ101]

Pour découpler les perturbations HF dans les montages et les appareils, on utilise souvent des condensateurs de découplage. Ceux-ci doivent avoir la propriété d'écouler la HF vers la masse aussi efficacement que possible. Les condensateurs céramiques en particulier s'y prêtent très bien. Les condensateurs électrolytiques et les condensateurs à film plastique sont inadaptés, car ils possèdent, du fait de leur structure bobinée, une inductance propre élevée. Sur les condensateurs au tantale, on monte souvent un condensateur céramique en parallèle, du fait des meilleures propriétés d'écoulement HF de ce dernier, car les premiers ne conviennent seuls que pour les fréquences HF moyennes jusqu'à environ $\qty{30}{\mega\hertz}$, tandis que les condensateurs céramiques peuvent découpler des fréquences bien plus élevées.
Pour écouler efficacement les perturbations HF, il faut disposer d'une mise à la terre efficace, à basse impédance.

[question:AJ119]
[question:AJ102]

Dans les lignes d'alimentation des étages HF, on emploie souvent des selfs de choc haute fréquence. Celles-ci représentent une impédance série pour la haute fréquence et bloquent efficacement les pénétrations par conduction de haute fréquence dans les étages, ainsi que les retours de HF dans l'alimentation des étages.
Du fait de leur structure bobinée, ces selfs de choc possèdent aussi des capacités propres, de sorte qu'elles forment, en liaison avec leur inductance, des points de résonance indésirables (circuits oscillants). Il peut de ce fait apparaître dans les étages HF des *résonances secondaires* indésirables, provoquées par les *résonances propres* des selfs de choc HF. Les résonances secondaires peuvent influencer négativement la caractéristique des étages HF. Il peut en résulter des effets de contre-réaction indésirables, en particulier dans les amplificateurs, ainsi que des creux dans la caractéristique de puissance des étages HF.

[question:AJ214]

<france>
# Le matériel d'auto-construction est hors du champ CEM

En France, c'est l'Agence nationale des fréquences qui instruit les cas de brouillage et procède aux contrôles ; il n'existe pas d'équivalent de la procédure allemande.

Le décret n° 2015-1084 modifié relatif à la compatibilité électromagnétique **exclut de son champ les équipements radioélectriques utilisés par les radioamateurs, à moins qu'ils ne soient mis à disposition sur le marché**, et le texte prend soin de préciser que les kits de composants destinés à être assemblés par les radioamateurs, comme les équipements mis à disposition sur le marché puis modifiés par et pour les radioamateurs, ne sont pas réputés mis à disposition sur le marché.

C'est le pendant réglementaire du droit à l'auto-construction : votre montage personnel, ou le kit que vous assemblez, n'a pas à suivre la procédure de conformité CEM ni à en porter le marquage. L'appareil acheté en l'état, lui, y reste soumis, la charge en incombant à son fabricant.

L'exemption porte sur la conformité du matériel, non sur son fonctionnement. Les niveaux de rayonnements non essentiels de l'appendice 3 du Règlement des radiocommunications s'appliquent, et l'obligation de ne pas causer de brouillage préjudiciable reste entière — c'est d'ailleurs à ce titre que l'ANFR peut demander à un opérateur des précisions sur les logiciels et protocoles qu'il emploie.
</france>
