En classe E, nous avons déjà fait connaissance avec les émissions non désirées sous la forme d'*harmoniques supérieures* et d'*émissions parasites*. Les harmoniques supérieures, ou harmoniques, d'un signal apparaissent toujours lorsque se forment des écarts par rapport à la courbe sinusoïdale idéale, et sont toujours des multiples entiers de la fréquence fondamentale, comme le représente la figure [ref:a_harmonische].

La question d'examen suivante en donne un exemple : lorsqu'un amplificateur est saturé, les crêtes de l'amplitude du signal sinusoïdal sont écrêtées — il apparaît de ce fait des harmoniques supérieures.

[question:AJ207]

<margin>
[picture:868:a_harmonische: Harmoniques supérieures (OW), harmoniques (Harm.) et émissions parasites (NA)]
</margin>

---

Lorsque l'on considère les multiples de la fréquence fondamentale d'un signal, nous distinguons les notions d'*harmonique et d'harmonique supérieure* du signal. Ces deux notions ne se distinguent que par leur définition et leur mode de comptage. La 1re harmonique d'un signal est sa fréquence fondamentale elle-même. La 2e harmonique correspond à la 1re harmonique supérieure d'un signal, la 3e harmonique à la 2e harmonique supérieure d'un signal, et ainsi de suite. Le tableau ci-contre [ref:a_harmonische] montre cette relation. 

<margin>
| l: Multiple de la fréquence fondamentale | l: Harmonique | l: Harmonique supérieure |
| $f_0$ | 1 | ~ |
| $2 \cdot f_0$ | 2 | 1 |
| $3 \cdot f_0$ | 3 | 2 |
| $4 \cdot f_0$ | 4 | 3 |
[table:a_harmonische:Harmoniques et harmoniques supérieures]
</margin>

---
  
[question:AJ203]
[question:AJ204]

<tip>
La radiodiffusion UKW est la radiodiffusion « classique » en ondes ultracourtes (UKW). La diffusion des programmes radio s'effectue dans la plage de fréquences de $\qtyrange{87,6}{107,9}{\mega\hertz}$.
</tip>

Si certaines harmoniques supérieures ou harmoniques d'un signal doivent être supprimées individuellement, cela peut se faire, outre par le filtre d'harmoniques classique (passe-bas), également au moyen de ce qu'on appelle des *circuits bouchons*. Un circuit bouchon supprime au maximum exactement une fréquence et laisse passer presque sans entrave toutes les autres.

[question:AJ210]

---

Selon le règlement allemand sur le service amateur (AFuV), les émissions non désirées doivent être limitées au niveau le plus faible possible. La [Verfügung 33](https://50ohm.de/vfg33) de 2007 fixe cependant des valeurs limites précises, qui doivent être respectées par le radioamateur mais aussi par les fabricants d'appareils commerciaux.

<margin>
[photo:319:a_vfg33:Extrait de la Verfügung 33 de 2007]
</margin>

Pour le domaine VHF/UHF/SHF de $\qtyrange{50}{1000}{\mega\hertz}$, les émissions parasites et les harmoniques supérieures doivent être atténuées d'au moins $\qty{60}{\dB}$ par rapport au niveau de crête maximal du signal émis (PEP), tant que la puissance de ces signaux se situe au-dessus d'un niveau de $\qty{0,25}{\micro\watt}$ (cf. figure [ref:a_uagw]).

[question:AJ225]

<margin>
[picture:918:a_uagw:Atténuation des harmoniques supérieures dans le domaine VHF/UHF/SHF]
</margin>

Pour le domaine décamétrique de $\qtyrange{1,7}{35}{\mega\hertz}$, les émissions parasites et les harmoniques supérieures doivent être atténuées d'au moins $\qty{40}{\dB}$ par rapport au niveau de crête maximal du signal émis (PEP), tant que la puissance de ces signaux se situe au-dessus d'un niveau de $\qty{0,25}{\micro\watt}$.

[question:AJ224]

%TODO BILD VON DL1COM EINBAUEN
Un analyseur de spectre permet, dans le mode spurious emissions, d'effectuer une mesure des harmoniques supérieures, ou harmoniques (angl. harmonics), comme le représente la figure [ref:a_uagw]. L'analyseur de spectre saisit ce faisant automatiquement le niveau de la porteuse ainsi que la réjection des harmoniques et les affiche en outre à l'écran. Lorsque l'on construit soi-même un appareil, il est décisif de s'assurer par des mesures que les valeurs limites prescrites sont respectées. Un fabricant commercial d'appareils radio atteste certes du respect de ces valeurs limites par la déclaration CE, il arrive néanmoins que certains appareils ne satisfassent pas aux exigences — dans de tels cas, la Bundesnetzagentur peut en interdire l'exploitation et la vente.

Les émissions non désirées ne naissent pas seulement des harmoniques supérieures : elles peuvent aussi apparaître dans l'élaboration de la fréquence des émetteurs — par exemple du fait de produits de mélange indésirables, de fluctuations de la tension d'alimentation ou d'une saturation du signal BF. C'est ce que nous allons maintenant examiner d'un peu plus près. 

Pour supprimer les produits de mélange indésirables — mais aussi les harmoniques supérieures — on emploie fréquemment un filtre passe-bande après les mélangeurs. En effet, dans les émetteurs monobande ainsi que dans les appareils pour les domaines VHF, UHF et SHF, ce sont des passe-bandes qui sont utilisés à la place des passe-bas classiques de réjection des harmoniques. Dans ces appareils radio, il faut souvent supprimer aussi des composantes de signal qui naissent déjà au sein de l'élaboration du signal d'émission et peuvent même se situer en dessous de la fréquence d'émission proprement dite.

[question:AJ211]
[question:AJ209]
[question:AJ208]

Des émissions non désirées peuvent aussi se trouver à proximité immédiate du signal émis. Celles-ci ne sont que difficilement, voire pas du tout, supprimables par l'emploi de filtres et devraient donc être efficacement supprimées, par des mesures appropriées, dès le début de l'élaboration du signal. De telles *émissions parasites*, également appelées *produits parasites* (couramment désignées aussi par le terme « splatter »), qui élargissent involontairement le signal émis, naissent fréquemment d'un réglage trop élevé de l'amplificateur de microphone d'un émetteur. Le signal BF s'en trouve distordu, ce qui a pour conséquence des émissions parasites indésirables. La figure [ref:a_harmonische] montre les émissions parasites. 

[question:AJ219]

Une tension d'alimentation insuffisamment stabilisée des étages finaux d'émission peut elle aussi engendrer des émissions non désirées. Une alimentation mal filtrée ou mal stabilisée (entachée de tension de ronflement) peut par exemple, du côté de la tension d'alimentation, conduire à des émissions AM de l'étage final. Des pénétrations de signaux BF du côté de l'alimentation secteur d'un émetteur peuvent également conduire à des émissions AM correspondantes. Cela se perçoit souvent, dans les émissions CW, comme une porteuse ou une note « ronflante », en particulier sur les émetteurs plus anciens.

[question:AJ222]
[question:AJ223]