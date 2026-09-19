Nous avons jusqu'à présent découvert l'ASK et la PSK. Il semble d'abord judicieux, pour ces deux procédés, de choisir un nombre de symboles aussi grand que possible, afin que le plus d'informations possible soient transmises par symbole. Mais un récepteur doit alors être capable de distinguer, p. ex., de nombreuses amplitudes différentes. Le procédé devient ainsi plus sensible aux perturbations.

Pour atténuer ce problème, on peut recourir à une astuce : au lieu de modifier un seul paramètre (p. ex. l'amplitude), on modifie deux paramètres par symbole, à savoir l'amplitude et la phase. Un symbole correspond alors à la combinaison d'une amplitude déterminée avec une phase déterminée. On obtient ainsi, malgré un petit nombre d'amplitudes et de phases différentes, un nombre de symboles plus élevé. À rapidité de modulation égale, davantage de bits peuvent donc être transmis par seconde. Ce procédé est appelé *modulation d'amplitude en quadrature* (QAM).

La figure [ref:a_8qam] montre un signal 8-QAM en représentation temporelle. Chaque symbole possède une amplitude déterminée, une phase déterminée et une suite de 3 bits, fixée par le mapping. Chaque symbole permet ainsi de transmettre trois bits. La figure [ref:a_16qam] montre un mapping 16-QAM dans le diagramme de constellation. Chaque symbole correspond à la combinaison d'une amplitude déterminée et d'une phase déterminée. Chaque symbole permet ainsi de transmettre quatre bits.

<margin>
[picture:702:a_8qam:Allure du signal d'un signal 8QAM, chaque symbole portant une amplitude ($\num{0,5}$ ou $\num{1}$), une phase et une suite de 3 bits]
[picture:1061:a_16qam:Diagramme I/Q d'un mapping 16-QAM]
</margin>

[question:AE403]

---

Après avoir découvert la représentation I/Q, le diagramme de constellation et la modulation d'amplitude en quadrature, la question se pose de savoir comment un tel signal peut être produit techniquement. On peut employer pour cela ce que l'on appelle un *modulateur I/Q*.

Un modulateur I/Q travaille avec deux porteuses de même fréquence, déphasées de $\qty{90}{\degree}$ l'une par rapport à l'autre. La première porteuse est pondérée par le signal I, et la porteuse déphasée de $\qty{90}{\degree}$ par le signal Q. La figure [ref:a_iq_modulator] montre le schéma fonctionnel d'un modulateur I/Q.

Les deux porteuses modulées sont ensuite additionnées. Selon les valeurs que prennent I et Q, il en résulte un signal d'amplitude et de phase déterminées. Si les valeurs de I et de Q sont modifiées, l'amplitude comme la phase du signal résultant peuvent donc changer.

<margin>
[picture:196:a_iq_modulator:Schéma fonctionnel d'un modulateur I/Q]
</margin>

<webonly>
<indepth>
Le tout se décrit facilement en termes mathématiques. Pour la somme d'une porteuse en cosinus et d'une autre porteuse en cosinus déphasée de $\qty{90}{\degree}$, on a la relation suivante :

$ I(t)\cdot \cos\left(\omega t\right) + Q(t)\cdot \cos\left(\omega t + \qty{90}{\degree}\right)=A \cdot \cos\left(\omega t+\phi\right) $

Il apparaît donc un nouveau signal en cosinus, d'amplitude

$A=\sqrt{I(t)^2 + Q(t)^2}$ 

et de déphasage

$ \phi = \operatorname{atan2}\left(Q(t),I(t)\right)$

[include:applet_iq]
</indepth>
</webonly>

[question:AF632]
[question:AE404]

Dans un système numérique, les valeurs de I et de Q peuvent être produites très simplement en logiciel. Un microcontrôleur, un processeur de signal ou un SDR associe par exemple à chaque symbole à transmettre deux valeurs numériques, pour I et pour Q. Un point de signal du diagramme de constellation correspond ainsi directement à un couple de valeurs $(I,Q)$.

Dans une 16-QAM, on pourrait par exemple employer quatre valeurs différentes pour I et pour Q. Leur combinaison fait naître les $\num{16}$ points de signal différents. Le logiciel n'a plus qu'à délivrer, pour chaque symbole, les valeurs de I et de Q correspondant au point de signal souhaité.

Les valeurs numériques de I et de Q, d'abord numériques, peuvent ensuite être converties en tensions analogiques par deux convertisseurs N/A et appliquées au modulateur I/Q. On peut ainsi produire par logiciel pratiquement n'importe quel point souhaité du diagramme de constellation. Les *Software Defined Radios* (SDR) modernes utilisent exactement ce principe : une grande partie de la modulation n'est plus fixée par des circuits analogiques câblés en dur, mais par le calcul des signaux I et Q en logiciel.

---

Un modulateur I/Q n'est nullement limité aux procédés de modulation numériques comme la QPSK ou la QAM. Au lieu de valeurs de I et de Q fixes et isolées, le logiciel peut aussi calculer pour I et pour Q des allures de signal variant continûment. Cela permet de produire également des procédés de modulation analogiques.

Dans une modulation d'amplitude, c'est par exemple la longueur du vecteur de signal résultant qui est modifiée. Dans une modulation de phase, c'est son angle qui est modifié. Dans une modulation de fréquence également, la phase du vecteur de signal est modifiée continûment, la vitesse de cette variation de phase déterminant la fréquence instantanée. Deux signaux I et Q produits de façon appropriée permettent en outre de produire un signal à bande latérale unique (SSB).

Un même modulateur I/Q permet donc de produire, entre autres, l'AM, la FM, la PM, la SSB, la PSK et la QAM. Seuls les signaux I et Q doivent être calculés différemment dans chaque cas. 

Le modulateur I/Q est ainsi, en quelque sorte, le « couteau suisse des modulateurs ». C'est aussi une raison essentielle de la grande souplesse de la technique SDR moderne : le procédé de modulation employé est déterminé pour une grande part par le logiciel, tandis que le matériel haute fréquence peut rester largement inchangé.
