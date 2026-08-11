<margin>
[picture:911:e_digitale_signalverarbeitung_blockschaltbild:Principe du traitement numérique du signal]
</margin>

Au cours des 25 dernières années, le monde a connu des transformations technologiques massives. La puissance de calcul des ordinateurs a été multipliée plusieurs fois, et de plus en plus de tâches dans les appareils techniques sont accomplies par des micropuces sur un espace minuscule. Cette évolution se poursuivra à un rythme effréné dans les années à venir. Tout cela change la manière dont les appareils sont réalisés, en particulier le traitement du signal dans les équipements radio modernes. Le traitement numérique du signal est désormais l'état de l'art, et tout appareil moderne repose sur cette technologie. Les processeurs de signal numériques et le principe fondamental du traitement numérique du signal y jouent un rôle essentiel.

Le traitement numérique du signal ne se rencontre d'ailleurs pas uniquement dans le domaine de la radiotechnique. De nombreux appareils, qu'il s'agisse de téléphones portables, de chaînes hi-fi, de systèmes d'imagerie dans le domaine médical ou de pratiquement toutes les applications radio modernes, profitent de cette technique fascinante, qui permet de réaliser à moindre coût des possibilités et des fonctions inédites dans ces appareils.

Dans le domaine de la radiotechnique, on parle, pour les appareils qui traitent les signaux au moyen du traitement numérique du signal, d'appareils dits SDR. Dans ces appareils, au moins une partie du traitement du signal est réalisée en logiciel.

[question:EF603]

Pour pouvoir traiter numériquement des signaux analogiques continus, ceux-ci doivent d'abord être échantillonnés au moyen d'un convertisseur analogique-numérique (convertisseur A/N) et convertis en valeurs numériques. On parle alors de numérisation du signal d'entrée analogique.

[question:EF602]

---
<margin>
[picture:411:e_digitale_signalverarbeitung:Représentation simple d'une onde sinusoïdale à partir de $\num{16}$ échantillons et $\num{7}$ valeurs]
</margin>

Le signal analogique y est échantillonné à intervalles de temps fixes et représenté dans une plage de valeurs numériques (par exemple de $\num{-128}$ à $\num{+127}$). Chaque valeur représente une tension de signal mesurée donnée, les valeurs négatives étant en règle générale associées aux tensions négatives et les valeurs positives aux tensions positives. On peut se représenter cela à peu près comme une caméra de cinéma qui prend des images d'une scène à intervalles fixes. Les images enregistrées ont toujours un écart temporel fixe par rapport à l'image précédente et à la suivante, et représentent la scène instantanée à de petits intervalles de temps. Ce processus s'appelle l'échantillonnage (sampling en anglais). Les différentes valeurs de signal mesurées sont appelées échantillons (samples). Dans la section suivante, nous examinerons ce processus d'un peu plus près.

Après la conversion A/N, les échantillons disponibles sous forme de valeurs numériques peuvent être traités à volonté au moyen du traitement numérique du signal.

À la suite du traitement numérique du signal, on voudra reconstituer, à partir des signaux traités numériquement, un signal analogique, par exemple pour la restitution par un haut-parleur ou pour l'émission par une antenne. Pour retransformer les valeurs numériques en signal analogique, on a besoin à cet endroit d'un convertisseur numérique-analogique (convertisseur N/A), qui constitue pratiquement le pendant du convertisseur A/N décrit précédemment. Le convertisseur N/A reconvertit les valeurs numériques en valeurs de tension analogiques et permet ainsi la reconstruction d'un signal analogique à partir des valeurs numériques.

[question:EF601]
