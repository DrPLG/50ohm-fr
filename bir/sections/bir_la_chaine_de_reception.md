Un récepteur reçoit à son antenne une multitude d'ondes à la fois : toutes les stations de toutes les fréquences, fortes ou faibles. Son travail est d'en choisir une seule, de la rendre assez forte, puis d'en retirer le message.

Pour comprendre comment il s'y prend, on le dessine en *schéma-bloc* [index:Schéma-bloc] : chaque bloc remplit une fonction, sans entrer dans le détail des composants.

<margin>
[picture:736:bir_schema_recepteur:Le schéma-bloc d'un récepteur simple]
</margin>

---

Suivons le signal de gauche à droite, dans l'ordre des numéros de la figure [ref:bir_schema_recepteur] :

1. **L'antenne** capte les ondes et les change en petits courants électriques.
2. **Le filtre** ne laisse passer que la plage de fréquences voulue, et arrête les autres.
3. **L'amplificateur haute fréquence** renforce ce signal, encore très faible.
4. **Le démodulateur** fait l'inverse de la modulation : il retire de la porteuse le signal de la voix, de la musique ou des données.
5. **L'amplificateur basse fréquence** renforce ce signal pour qu'il puisse faire vibrer le haut-parleur.
6. **Le haut-parleur** le change en son.

---

Deux qualités font un bon récepteur. Sa *sensibilité* [index:Sensibilité] : il entend des signaux très faibles. Sa *sélectivité* [index:Sélectivité] : il sépare nettement la station écoutée d'une station voisine, sans que l'une déborde sur l'autre. Les postes modernes y parviennent par des montages plus élaborés que celui de la figure, et souvent par le calcul, dans un processeur : c'est le principe des récepteurs SDR que nous utilisons depuis la séance 8.

[question:RB1701]
[question:RB1702]
[question:RB1703]
[question:RB1704]
