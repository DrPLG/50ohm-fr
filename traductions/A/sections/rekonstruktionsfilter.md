
Examinons maintenant d'un peu plus près la conversion des signaux numériques (les échantillons) en signaux analogiques par un convertisseur N/A. Les données numériques sont ici retraduites en échelons de tension dans le convertisseur N/A. Cela se produit à intervalles de temps fixes entre les échantillons. Ce processus est aussi appelé reconstruction.

Du fait de la résolution à temps discret imposée par la fréquence d'échantillonnage limitée d'un convertisseur N/A, il apparaît un signal en escalier, qui contient des fréquences plus élevées indésirables. Pour éliminer ces composantes indésirables et rétablir ainsi le signal d'origine, nous avons besoin, tout comme à l'entrée du convertisseur A/N, d'un filtre passe-bas ou passe-bande. Ce filtre de reconstruction doit supprimer efficacement toutes les composantes de signal situées au-dessus de la moitié de la fréquence d'échantillonnage. 

[question:AF624]
[question:AF625]
