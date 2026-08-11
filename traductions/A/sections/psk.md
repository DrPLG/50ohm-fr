La modulation par déplacement de phase (Phase Shift Keying, PSK) est un procédé de modulation numérique utilisé pour la transmission de données en télécommunications et dans le service amateur. La PSK repose sur la variation de la phase d'un signal porteur afin de représenter différents états des données. Comparée à la modulation d'amplitude ou de fréquence, la PSK est moins sensible au bruit d'amplitude et permet, à largeur de bande égale, d'atteindre un débit de données plus élevé.

[picture:705:psk:Modulation par déplacement de phase (Phase-shift Keying)]

Principe de la modulation par déplacement de phase (PSK)

Dans sa forme la plus simple, la **BPSK (Binary Phase Shift Keying)**, il existe deux angles de phase, p. ex. $\qty{0}{\degree}$ et $\qty{180}{\degree}$. Chaque angle de phase représente une valeur binaire ($\num{0}$ ou $\num{1}$). Lors d'un changement de valeur binaire, la phase de la porteuse varie de $\qty{180}{\degree}$.

Pour des débits de données plus élevés, il existe des variantes comme la **QPSK (Quadrature Phase Shift Keying)** et la **8-PSK**, qui utilisent respectivement quatre et huit positions de phase pour transmettre plusieurs bits par symbole :
- **QPSK** : utilise quatre phases ($\qty{0}{\degree}$, $\qty{90}{\degree}$, $\qty{180}{\degree}$ et $\qty{270}{\degree}$) pour coder deux bits par symbole.
- **8-PSK** : utilise huit phases pour coder trois bits par symbole.

Les signaux en représentation temporelle

Dans la représentation temporelle d'un signal PSK, la modulation par déplacement de phase se manifeste par un changement abrupt de l'angle de phase du signal porteur, tandis que l'amplitude reste constante. C'est une différence nette avec la modulation d'amplitude ou de fréquence, car la hauteur et la fréquence du signal restent identiques ; seule la phase change à chaque changement de symbole.

Exemple : la BPSK en représentation temporelle
- En BPSK, le signal est scindé en deux phases : p. ex. amplitude positive pour une phase ($\qty{0}{\degree}$) et amplitude négative pour la phase opposée ($\qty{180}{\degree}$).
- Sur un diagramme temporel, on voit donc à chaque changement de bit un saut du signal, p. ex. du positif vers le négatif ou inversement.

Exemple : la QPSK en représentation temporelle
- On voit ici quatre angles de phase différents. Les transitions peuvent également être abruptes, mais l'amplitude ne change pas.
- Comme plusieurs angles de phase sont utilisés ici, les sauts de phase sont plus petits et la courbe présente une allure un peu plus « lissée » que celle de la BPSK.

Comment reconnaître les signaux

Sur un oscilloscope ou un diagramme de phase, les transitions de phase sont visibles :
- **Dans le domaine temporel** : un basculement abrupt de la phase du signal (du positif vers le négatif, ou entre différentes positions de phase).
- **Dans le diagramme de phase** (souvent présenté sous forme de diagramme de constellation) : chaque angle de phase est représenté par un point sur un cercle, correspondant aux différents états (bits). Pour un signal propre, les points restent stables à des positions fixes.

La PSK est particulièrement utile en communication numérique, car elle permet des débits de données élevés avec une transmission relativement robuste. La variation de la phase à amplitude constante aide à mieux reconnaître le signal, même en présence de bruit et d'interférences, et permet ainsi une transmission plus stable.

[question:AE401]