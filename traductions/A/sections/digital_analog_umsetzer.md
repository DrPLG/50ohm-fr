Penchons-nous maintenant d'un peu plus près sur l'homologue du convertisseur A/N — le convertisseur N/A. Le convertisseur N/A produit à nouveau un signal analogique à partir d'un flux de données numériques (les échantillons). Le convertisseur N/A ne peut naturellement, tout comme le convertisseur A/N, produire des valeurs d'amplitude arbitrairement précises ; il possède, exactement comme le convertisseur A/N, une résolution maximale (en bits). Il existe donc là aussi un nombre fini de valeurs de signal analogiques que le convertisseur N/A peut produire. Le nombre d'échelons possibles se calcule comme déjà décrit précédemment pour le convertisseur A/N.

[question:AF609]

Un convertisseur N/A ne peut jamais générer que des tensions comprises dans une plage de tension donnée (p. ex. de $\qty{0}{\volt}$ à $\qty{1}{\volt}$, ou de $\qty{-2}{\volt}$ à $\qty{2}{\volt}$). Le nombre d'échelons décrit plus haut (la résolution du convertisseur N/A) se répartit ici sur la plage de tension, pour un convertisseur N/A à fonctionnement linéaire (linéaire signifie ici que l'écart entre les différents échelons est toujours le même). Si le convertisseur N/A a p. ex. une résolution de seulement $\qty{4}{\bit}$, nous disposons de $\num{16}$ échelons possibles. Ceux-ci se répartissent alors p. ex. sur une plage de tension (plage de valeurs) de $\qty{0}{\volt}$ à $\qty{1}{\volt}$. Pour calculer le pas séparant deux échelons, il suffit de diviser la plage de tension par le nombre de pas intermédiaires possibles. Attention : avec $16$ échelons, il n'y a que $15$ pas intermédiaires. Cela donne p. ex., dans notre exemple précédent, un écart (un pas) de $\frac{\qty{1}{\volt}}{16 - 1} \approx \qty{67}{\milli\volt}$.

[question:AF611]
[question:AF610]

