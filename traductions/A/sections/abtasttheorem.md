Examinons à présent d'un peu plus près le processus d'échantillonnage et rappelons-nous l'exemple, déjà cité, de la caméra qui prend des images d'une scène à intervalles réguliers. Supposons par exemple que notre caméra prenne 24 images par seconde d'une scène donnée. Si l'on imagine maintenant que nous filmons un coureur en train de courir, nous constaterons qu'entre les différentes images, les jambes et le corps de notre coureur effectuent toujours un mouvement saccadé par rapport à l'image précédente. Si nous faisons défiler les images rapidement les unes après les autres, il en résulte un déroulement de mouvement visuellement continu. L'information que nous saisissons à 24 images par seconde est cependant limitée dans le temps (retenons : à temps discret). Que se passerait-il si, entre 2 images successives, une mouche traversait soudain rapidement le champ de l'objectif de notre caméra ? Pourrions-nous encore le percevoir ? Cela dépend du fait que la mouche choisisse ou non le bon instant, entre deux images, pour sa traversée. Si elle n'entrait dans le champ de vision de la caméra qu'après la prise d'une image et l'avait déjà quitté avant la prise de l'image suivante, nous ne pourrions pas retrouver cet événement dans les images que nous avons prises. Une information nous resterait cachée.

<webonly>
<margin>
[include:applet_nyquist]
</margin>
</webonly>

Il en va exactement de même pour l'échantillonnage des signaux analogiques. Si ceux-ci sont saisis (échantillonnés) à une fréquence d'échantillonnage $f_\text{s}$ donnée, nous risquons de ne plus pouvoir saisir les variations rapides du signal entre 2 échantillons. L'échantillonnage signifie donc toujours aussi une perte d'information temporelle. On peut alors se demander quelle résolution temporelle est nécessaire pour échantillonner un signal analogique d'une fréquence donnée (nombre de variations de l'amplitude du signal par seconde) sans perte d'information (toutes les variations doivent être saisies). On peut mener pour cela le raisonnement suivant. Pour pouvoir saisir sans faute au moins chaque variation du signal, il faut (comme dans notre exemple précédent avec la caméra) être en mesure de garantir qu'un échantillon est prélevé au moins avant et après chaque variation du signal. Dans le cas de notre mouche qui traverse l'image, la condition serait que la mouche ne puisse traverser l'image qu'à une vitesse telle qu'elle soit visible sur 2 images au moins. Sinon, on ne pourrait pas dire d'où elle a traversé l'image ni dans quelle direction. Si cette condition n'est pas remplie, cette information nous échappe. On dit aussi, dans ce cas, qu'une reconstruction sans erreur n'est pas possible.

On peut montrer mathématiquement que, pour saisir un signal dont la plus haute fréquence présente est $f_{\mathrm{max}}$, la fréquence d'échantillonnage $f_\text{s}$ doit valoir plus du double, donc un peu plus que $f_\text{s} > 2 \cdot f_{\mathrm{max}}$, pour que nous puissions reconstruire notre signal sans faute. Ce résultat s'appelle, en traitement numérique du signal, le théorème d'échantillonnage ; il est également connu, d'après ses découvreurs Nyquist et Shannon, sous le nom de théorème d'échantillonnage de Nyquist-Shannon ou de condition de Nyquist. Le théorème d'échantillonnage détermine donc la fréquence d'échantillonnage $f_\text{s}$ minimale théoriquement nécessaire à une reconstruction sans erreur d'un signal.

[question:AF618]

[question:AF616]

---

Si le théorème n'est pas respecté, il apparaît ce que l'on appelle des effets d'alias, ou effets de repliement (aliasing). 

[question:AF617]

<webonly>
L'applet ci-contre permet d'expérimenter avec la fréquence d'échantillonnage. Si la fréquence d'échantillonnage descend en dessous de $\qty{2}{\kilo\hertz}$, la condition de Nyquist n'est plus remplie et le signal ne peut plus être reconstruit de façon univoque.
Il est également intéressant de noter que, même à une fréquence d'échantillonnage d'exactement $\qty{2}{\kilo\hertz}$, la reconstruction ne fonctionne pas de manière fiable. C'est pourquoi on choisit habituellement une fréquence d'échantillonnage située un peu au-dessus de la condition de Nyquist, afin de garantir une reconstruction sûre du signal.
</webonly>

<indepth>
Prenons un exemple pratique, celui d'un lecteur de CD, qui travaille p. ex. à une fréquence d'échantillonnage de $\qty{44,1}{\kilo\sps}$. Si l'on se fonde sur le théorème d'échantillonnage décrit ci-dessus, cela signifie qu'avec une fréquence d'échantillonnage de $\qty{44,1}{\kilo\sps}$, seules des fréquences inférieures à $\qty{22,05}{\kilo\hertz}$ peuvent être représentées. Des fréquences allant jusqu'à env. $\qty{22}{\kilo\hertz}$ peuvent donc encore être représentées correctement. Cela correspond à la plage de fréquences HiFi des bonnes chaînes stéréo. 
</indepth>

L'exercice suivant te permet de tester tes connaissances sur le théorème d'échantillonnage.

[question:AF619]
