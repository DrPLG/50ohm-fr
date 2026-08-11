Un *filtre notch (filtre réjecteur, Kerbfilter)* est un filtre à bande très étroite destiné à supprimer une fréquence déterminée dans le spectre BF du signal reçu. Il sert par exemple à éliminer de manière ciblée une porteuse gênante dans une transmission, tout en laissant le reste de la transmission pratiquement inchangé. Les filtres notch peuvent être réalisés aussi bien dans le domaine BF que dans le domaine FI. Les filtres dans le domaine FI ont l'avantage de supprimer plus efficacement les signaux perturbateurs, en particulier les plus forts, et de pouvoir réduire leur influence sur l'AGC.

[question:EF215]

<margin>
[picture:242:frequenzverlauf_notchfilter:Caractéristique de filtrage d'un filtre notch]
</margin>

---

La caractéristique de filtrage d'un filtre notch est conçue de telle sorte que seule une petite partie des fréquences du signal BF est très fortement supprimée. Il en résulte une encoche dans le spectre. D'où le nom de filtre notch (« notch » signifie encoche).

[question:EF216]

<tip>
Beaucoup d'appareils modernes réalisent les filtres notch au moyen de la technologie de filtrage numérique. La largeur de bande ainsi que la caractéristique de filtrage et la fréquence peuvent alors souvent être paramétrées avec précision. Un autre avantage dans ce contexte est constitué par les filtres dits Auto-Notch, qui peuvent reconnaître automatiquement des composantes de porteuse fixes dans le signal BF et les éliminer automatiquement.
</tip>