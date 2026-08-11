Jusqu'ici, nous ne connaissions les diodes à semi-conducteur que dans leur fonction de redresseur d'une tension alternative. Dans les modulateurs destinés à produire des signaux AM et SSB, les diodes jouent un nouveau rôle : sous l'effet d'une tension BF appliquée, leur résistance augmente ou diminue au rythme de la fréquence BF ; plus la tension BF est grande, plus le courant de diode est grand et plus la résistance résultante est petite. Dans un modulateur d'amplitude, cette résistance est mise à profit pour agir sur l'amplitude d'un signal HF (issu d'un oscillateur local) ; le courant HF traversant la diode devient grand lorsque la résistance de la diode est petite, et inversement. Le signal HF est ainsi « modulé » en amplitude au rythme du signal BF ! Dans le cas le plus simple, lorsque l'on n'utilise qu'une seule diode, le spectre du signal contient une porteuse (à la fréquence HF d'origine) et deux bandes latérales de modulation, situées au-dessus et en dessous de la fréquence porteuse, à une distance égale à la fréquence BF — un signal à modulation d'amplitude (AM). 

Ce principe apparaît clairement dans la question suivante : une diode est attaquée simultanément par un signal BF et un signal HF, et le signal de sortie est filtré par un circuit oscillant LC.

[question:AD507]

Avec un montage de quatre diodes disposées en anneau, la porteuse peut cependant elle aussi être supprimée, et il ne reste que les deux bandes latérales ; pour cela, l'anneau de diodes doit être intégré dans un montage push-pull, équilibré (c'est-à-dire symétrisé) de telle sorte que les courants du signal de porteuse s'annulent à la sortie. Au chapitre « Mélangeur II », un tel montage a déjà été présenté sous le nom de « mélangeur équilibré » (angl. « balanced mixer »), mais il s'agissait alors de transposer un signal HF d'entrée dans une position de fréquence intermédiaire. 

Le modulateur équilibré est le premier étage d'un modulateur à bande latérale unique — il produit, à partir d'un signal d'oscillateur local et d'un signal BF (modulation), un signal à double bande latérale (DSB). Vient ensuite un filtre passe-bande qui ne laisse passer qu'une seule des deux bandes latérales, et produit ainsi en sortie un signal SSB.  

Que l'on songe aux deux étages nécessaires du modulateur SSB.

[question:AE206]

[question:AF302]

---

On reconnaît un mélangeur équilibré, ou modulateur équilibré, à son anneau de diodes. Dans ce montage, l'attaque en push-pull n'est pas complète, puisqu'un seul transformateur est utilisé ; il existe toutefois un équivalent de la prise médiane d'un transformateur dans l'injection du signal d'oscillateur au point milieu d'un diviseur de tension (potentiomètre).

[question:AF308]

<indepth>
Dans l'émetteur, le mélangeur équilibré devient un modulateur équilibré par permutation des entrées : la modulation basse fréquence est injectée dans la branche du pont du montage push-pull, entre la prise médiane de T2 et la masse. Le signal de l'oscillateur local est injecté dans l'anneau de diodes par T1, et le signal à double bande latérale est prélevé par T2. En l'absence de tension de modulation, les paires de diodes D1, D2 et D3, D4 conduisent alternativement et forment ce faisant des diviseurs de tension 1:1, de sorte que leurs points milieux se trouvent au potentiel de la masse. Ainsi, l'extrémité supérieure et l'extrémité inférieure de l'enroulement de T2 se trouvent alternativement au potentiel de la masse, tandis que l'autre extrémité de l'enroulement reste sans liaison, du fait des diodes bloquées. Aucun courant ne circule donc dans l'enroulement et aucune tension n'apparaît du côté de la sortie — c'est en cela que consiste la « suppression de la porteuse » !

Lorsqu'une tension de modulation est appliquée, un courant supplémentaire traverse les diodes, de sorte que le potentiel du point milieu des diviseurs de tension est décalé — un courant peut alors circuler dans le transformateur T2 et un signal de sortie apparaît. La figure montre les allures de tension que l'on obtient lorsque le signal d'oscillateur est assimilé, par simplification, à une fonction rectangulaire.
</indepth>

---

La suppression de la porteuse a à voir avec l'annulation d'un signal indésirable — pour cela, un montage modulateur doit être « équilibré ».

[question:AD510]

C'est précisément à cet équilibrage qu'appartient un réglage des amplitudes (potentiomètre) et des phases (condensateur ajustable)

[question:AF309]

Un modulateur est « symétrisé » ou « équilibré » afin de supprimer la porteuse — les bandes latérales de modulation ne sont pas supprimées ce faisant.

[question:AF304]

[question:AF303]

Après le modulateur équilibré vient le deuxième étage d'un modulateur SSB.

[question:AF305]

[question:AF306]

Les quartz déterminent la fréquence de la porteuse supprimée par le modulateur équilibré. On le voit à la fréquence du quartz pour la bande latérale inférieure (LSB) : la porteuse se situe $\qty{1,5}{\kilo\hertz}$ au-dessus de la fréquence centrale du filtre de bande de $\qty{9}{\mega\hertz}$. Avec la fréquence BF maximale de $\qty{3}{\kilo\hertz}$, la bande latérale inférieure se situe alors $\qty{1,5}{\kilo\hertz}$ en dessous de la fréquence centrale, et la fréquence BF de $\qty{200}{\hertz}$ place alors la bande latérale à $\qty{1,3}{\kilo\hertz}$ au-dessus de la fréquence centrale du filtre. Pour la bande latérale supérieure (USB), c'est l'inverse qui s'applique.

[question:AF307]

Le symbole en croix, ou symbole X, dans le bloc fonctionnel situé après l'amplificateur BF représente la multiplication mathématique — les modulateurs, démodulateurs et montages mélangeurs sont ainsi désignés parce que leur fonction peut être décrite mathématiquement comme la multiplication de fonctions-signaux.

Un modulateur pour la modulation de fréquence (FM) utilise en revanche un autre type de diode, la diode à capacité variable (reconnaissable dans les schémas au petit symbole de condensateur accolé au symbole de la diode). La diode fait ici toujours partie d'un montage oscillateur dont la fréquence d'oscillation est déterminée par un circuit résonnant contenant la diode à capacité variable. La diode est polarisée en sens inverse par une tension continue, de sorte qu'il s'établit une capacité de diode fixe, et donc aussi une fréquence d'oscillateur. Le montage devient un modulateur de fréquence lorsqu'un signal BF est superposé à la tension continue — l'oscillateur change alors de fréquence au rythme du signal BF.


C'est ici qu'apparaît la diode à capacité variable — et le montage à transistor voisin est un oscillateur à circuit oscillant LC.

[question:AD508]

Une diode à capacité variable polarisée en inverse, attaquée d'un côté par la BF et se trouvant de l'autre côté en parallèle sur le circuit oscillant d'un montage oscillateur, agit sur la fréquence de l'oscillateur.

[question:AF310]

Avec de grandes tensions BF, on peut aisément provoquer des variations de fréquence de l'oscillateur (« excursion » FM) bien plus grandes qu'il n'est permis. Une limitation de l'« excursion » par un réglage et une limitation de l'amplitude BF est donc nécessaire. Des diodes montées tête-bêche limitent la tension à environ la tension de coude des diodes.

[question:AD509]

Il ne s'agit manifestement pas d'un modulateur — il n'y a qu'un seul signal ! Un condensateur chimique à la sortie de la diode indique une tension continue !

[question:AD503]

% TODO aus E hier her kopiert ... muss eingeflegt werden.
<margin>
[picture:500:e_ssb_modulation:Schéma fonctionnel de la modulation SSB par la méthode du filtre]
[picture:831:e_ssb_modulation_lsb:Fréquences avec la méthode du filtre en LSB]
[picture:940:e_ssb_modulation_lsb:Spectre avec la méthode du filtre en LSB]
[picture:832:e_ssb_modulation_usb:Fréquences avec la méthode du filtre en USB]
[picture:941:e_ssb_modulation_usb:Spectre avec la méthode du filtre en USB]
</margin>