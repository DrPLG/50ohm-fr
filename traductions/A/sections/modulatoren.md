Nous avons déjà rencontré les diodes dans différents montages. Nous allons maintenant voir comment leur caractéristique non linéaire peut être mise à profit pour moduler un signal porteur haute fréquence par un signal utile basse fréquence.

Lorsqu'un signal HF et un signal BF sont appliqués ensemble à une diode, comme le montre la figure [ref:a_am_modulator], la tension BF influence la conductivité de la diode. Le signal HF est ainsi transmis avec une intensité variable selon la valeur instantanée de la BF. Son amplitude varie donc au rythme du signal BF.

À la sortie apparaissent ainsi, outre la porteuse HF d'origine, deux bandes latérales situées au-dessus et en dessous de la fréquence porteuse. Un circuit oscillant accordé sur la fréquence porteuse supprime les autres composantes de fréquence indésirables. On obtient ainsi, à la sortie, un signal modulé en amplitude (AM).

<margin>
[picture:772:a_am_modulator:Modulateur AM simple à diode et circuit oscillant]
</margin>

<webonly>
La simulation suivante montre le fonctionnement du modulateur AM ; les valeurs ont été choisies pour que la HF et la BF soient bien reconnaissables. La BF est à $\qty{500}{\hertz}$, la HF à $\qty{10}{\kilo\hertz}$. L'amplitude du signal HF varie au rythme de la BF. Le circuit oscillant est accordé sur la fréquence porteuse et supprime les composantes de fréquence indésirables. Si l'on retire le circuit oscillant, on observe une multitude de produits de mélange. On peut également régler la fréquence BF sur $\qty{1}{\kilo\hertz}$ pour voir comment les bandes latérales se déplacent.

[include:applet_am_modulator]
</webonly>

<indepth>
Un signal AM peut également être décrit mathématiquement. Considérons pour cela d'abord un signal BF sinusoïdal normalisé

$m(t)=\cos(\omega t)$

de pulsation $\omega=2\pi f_\mathrm{m}$. Avec son amplitude $\hat U_\mathrm{m}$ et une composante continue additionnelle $U_\mathrm{G}$, on obtient

$U_\mathrm{m}(t)=U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)$

Ce signal est maintenant multiplié par le signal porteur haute fréquence

$U_\mathrm{p}(t)=\cos(\Omega t)$

avec $\Omega=2\pi f_\mathrm{p}$. Il en résulte, pour le signal AM :

$U_\mathrm{AM}(t)=\left(U_\mathrm{G}+\hat U_\mathrm{m}\cdot\cos(\omega t)\right)\cdot\cos(\Omega t)$

En développant le produit, on obtient :

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\hat U_\mathrm{m}\cdot\cos(\omega t)\cdot\cos(\Omega t)$

Avec la relation

$\cos(a)\cdot\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$

le second terme peut être décomposé plus avant :

$U_\mathrm{AM}(t)=U_\mathrm{G}\cdot\cos(\Omega t)+\frac{\hat U_\mathrm{m}}{2}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

On reconnaît ainsi directement les trois composantes d'un signal AM : le premier terme décrit la *porteuse*, à la fréquence $\Omega$. Les deux autres termes forment la *bande latérale supérieure et la bande latérale inférieure*, aux fréquences $\Omega+\omega$ et $\Omega-\omega$.

La composante continue $U_\mathrm{G}$ est responsable du maintien de la porteuse. Même lorsque le signal utile est momentanément nul, un signal porteur continue d'être produit.

[picture:1127:a_am_modulation:Spectre d'un signal AM avec porteuse et deux bandes latérales]

</indepth>

Ce principe apparaît clairement dans la question suivante : une diode est attaquée simultanément par un signal BF et un signal HF, et le signal de sortie est filtré par un circuit oscillant LC.

[question:AD507]

---

Avec quatre diodes disposées en anneau, on peut construire un modulateur de telle sorte que la porteuse soit supprimée à la sortie. Un tel montage, nous l'avons déjà rencontré au chapitre « Mélangeur II » sous le nom de *mélangeur équilibré*. Il y servait à transposer un signal HF vers une fréquence intermédiaire. Dans l'émetteur, nous utilisons maintenant le même principe de base pour produire un signal modulé.

<margin>
[picture:759:a_balancemodulator:Modulateur équilibré à anneau de diodes]
</margin>

On reconnaît typiquement un mélangeur équilibré, ou modulateur équilibré, à son anneau de diodes, tel que représenté sur la figure [ref:a_balancemodulator]. L'anneau de diodes est piloté par le signal d'oscillateur $f_\mathrm{OSC}$. Selon la polarité du signal d'oscillateur, l'une ou l'autre des deux paires de diodes opposées devient conductrice.

Le signal BF est ainsi transmis alternativement vers la sortie avec la même polarité ou avec une polarité inversée. En simplifiant, on peut donc considérer que le signal BF est multiplié par le signal d'oscillateur.

L'avantage décisif du montage symétrique est la *suppression de la porteuse* : les composantes du signal d'oscillateur s'annulent idéalement entre elles à la sortie. En l'absence de signal BF, aucun signal de sortie n'apparaît donc. Si un signal BF est appliqué, la bande latérale supérieure et la bande latérale inférieure apparaissent en revanche, tandis que la porteuse reste supprimée.

Le signal de sortie est appelé *signal à double bande latérale avec porteuse supprimée* (DSB).

[question:AE206]
[question:AF302]
[question:AF308]
[question:AD510]

<indepth>
La suppression de la porteuse dans un modulateur équilibré peut être décrite de façon simplifiée à l'aide de deux branches symétriques :

$u_1(t)=\left(U_G+\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

$u_2(t)=\left(U_G-\hat U_\mathrm{m}\cos(\omega t)\right)\cos(\Omega t)$

À la sortie, les deux signaux sont soustraits l'un de l'autre :

$u_\mathrm{s}(t)=u_1(t)-u_2(t)$

On obtient ainsi :

$u_\mathrm{s}(t)=U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)-U_G\cos(\Omega t)+\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Les deux composantes de porteuse $U_G\cos(\Omega t)$ s'annulent. Il reste :

$u_\mathrm{s}(t)=2\hat U_\mathrm{m}\cos(\omega t)\cos(\Omega t)$

Avec $\cos(a)\cos(b)=\frac{1}{2}\left(\cos(a+b)+\cos(a-b)\right)$, il vient :

$u_\mathrm{s}(t)=\hat U_\mathrm{m}\left(\cos((\Omega+\omega)t)+\cos((\Omega-\omega)t)\right)$

Le signal de sortie ne contient donc plus que la bande latérale supérieure et la bande latérale inférieure. La porteuse à la fréquence $\Omega$ est supprimée.
</indepth>

---

Pour que le signal d'oscillateur s'annule le plus complètement possible à la sortie, le montage doit être symétrique, c'est-à-dire *équilibré*. De faibles différences d'amplitude ou de phase entre les deux voies de signal suffisent déjà à laisser subsister un résidu de porteuse à la sortie. La symétrie d'amplitude peut par exemple être ajustée à l'aide d'un potentiomètre. Pour l'ajustement de phase, certains montages utilisent en outre un condensateur ajustable. Le but de ce réglage est d'obtenir une suppression de la porteuse aussi élevée que possible, tout en conservant les deux bandes latérales de modulation.

<webonly>
L'applet suivant montre le réglage de la porteuse. Lorsque le curseur situé à droite est déplacé, la porteuse apparaît soudainement dans le spectre.

[include:applet_dsp]
</webonly>

[question:AF309]

---

Le modulateur équilibré constitue le premier étage d'un modulateur SSB et produit un signal DSB. Derrière le modulateur équilibré vient, comme second étage, un filtre passe-bande à bande étroite, comme le montre la figure [ref:a_ssb_modulation]. Celui-ci ne laisse passer qu'une seule des deux bandes latérales et supprime l'autre. Il en résulte, à la sortie, un signal à bande latérale unique (SSB).

<margin>
[picture:500:a_ssb_modulation:Schéma fonctionnel de la modulation SSB par la méthode du filtre]
</margin>

[question:AF306]
[question:AF304]
[question:AF303]
[question:AF305]

---

Une bonne façon de réaliser un émetteur-récepteur capable de produire aussi bien l'USB que la LSB consiste à concevoir le filtre passe-bande pour une plage de fréquences fixe. Le choix de la bande latérale filtrée, supérieure ou inférieure, ne se fait pas en modifiant le filtre, mais par la fréquence de l'oscillateur du modulateur équilibré. Deux oscillateurs à quartz différents sont disponibles à cet effet.

Si l'on choisit par exemple, pour l'USB, la fréquence d'oscillateur $\qty{8998,5}{\kilo\hertz}$, la modulation produit deux bandes latérales. La bande latérale supérieure est alors décalée exactement dans la bande passante du filtre fixe, tandis que la bande latérale inférieure se trouve en dehors de la bande passante et est supprimée.

Pour la LSB, on commute sur l'autre fréquence de quartz, $\qty{9001,5}{\kilo\hertz}$. L'ensemble du spectre DSB se décale alors de telle sorte que c'est maintenant la bande latérale inférieure qui tombe dans la bande passante du même filtre, tandis que la bande latérale supérieure est supprimée.

L'astuce décisive consiste donc à laisser le filtre inchangé et à décaler la position du signal DSB en jouant sur des fréquences d'oscillateur différentes. De façon similaire à la fréquence intermédiaire d'un récepteur, cela permet d'utiliser un filtre fixe et de haute qualité pour différentes positions de fréquence.

[question:AF307]

<margin>
<latexonly>
[picture:831:a_ssb_modulation_lsb:Fréquences avec la méthode du filtre en LSB]
[picture:940:a_ssb_modulation_lsb:Spectre avec la méthode du filtre en LSB]
[picture:832:a_ssb_modulation_usb:Fréquences avec la méthode du filtre en USB]
[picture:941:a_ssb_modulation_usb:Spectre avec la méthode du filtre en USB]
</latexonly>
<webonly>
[include:applet_dsp_filter]
</webonly>
</margin>

---

Pour produire un signal modulé en fréquence (FM), on peut utiliser une *diode à capacité variable*. Elle se reconnaît sur les schémas au petit symbole de condensateur accolé à celui de la diode, comme le montre la figure [ref:a_fm_modulator].

Une diode à capacité variable est polarisée en sens inverse. Sa capacité dépend alors de la tension inverse appliquée à ses bornes. Lorsqu'elle est utilisée comme élément du circuit oscillant déterminant la fréquence d'un oscillateur, une variation de cette tension modifie la fréquence de résonance du circuit oscillant, et donc la fréquence de l'oscillateur.

Pour la modulation de fréquence, le signal BF est superposé à la tension continue appliquée à la diode à capacité variable. Sa capacité varie alors au rythme du signal BF, et la fréquence de l'oscillateur se trouve décalée vers le haut et vers le bas en conséquence. On obtient ainsi un signal modulé en fréquence.

<margin>
[picture:155:a_fm_modulator:Modulateur FM à diode à capacité variable]
</margin>

[question:AD508]
[question:AF310]

---

Avec de grandes tensions BF, on peut aisément provoquer des variations de fréquence de l'oscillateur (« excursion » FM) bien plus grandes qu'il n'est permis. Une limitation de l'« excursion » par un réglage et une limitation de l'amplitude BF est donc nécessaire. Des diodes montées tête-bêche limitent la tension à environ la tension de coude des diodes. Les figures [ref:a_fm_modulator_hub1] et [ref:a_fm_modulator_hub2] en montrent un exemple.

<margin>
[picture:44:a_fm_modulator_hub1:Montage de limitation de l'excursion]
[picture:828:a_fm_modulator_hub2:Limitation du signal]
</margin>

[question:AD509]
