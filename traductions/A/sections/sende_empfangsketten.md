Les différentes étapes d'une chaîne d'émission et de réception sont décrites dans la section suivante. La figure [ref:a_sdr_sender] montre à titre d'exemple un émetteur SDR pour la communication en phonie. Dans un premier temps, le signal du microphone est numérisé par un convertisseur A/N. Le signal numérique est ensuite comprimé par un codeur de source, afin de réduire la largeur de bande nécessaire. À l'étape suivante, un codeur de canal dote délibérément le signal comprimé de redondance, de sorte que les erreurs de transmission puissent être détectées et corrigées. Les données codées sont enfin converties en symboles par un mapper, puis modulées par un modulateur I/Q, sur lequel nous reviendrons plus en détail dans un chapitre ultérieur. La chaîne d'émission se termine par un amplificateur de puissance ainsi que par l'antenne, par laquelle le signal est rayonné.

<margin>
[picture:1062:a_sdr_sender:Émetteur SDR pour la communication en phonie]
</margin>

Les blocs mis en évidence en bleu sur la figure [ref:a_sender] représentent les étapes de traitement du signal qui peuvent être mises en œuvre, par exemple, de façon purement logicielle ou à l'aide d'un FPGA. L'ordre de ces étapes de traitement est toujours le suivant pour un émetteur et doit être bien mémorisé en vue des questions d'examen :

1. Codeur de source : comprimer les données
2. Codeur de canal : ajout de redondance pour la détection et la correction d'erreurs
3. Mapper : associer les données binaires à des symboles, p. ex. amplitude et phase pour la QAM

[question:AF626]
[question:AF627]

---

Pour un récepteur, l'ensemble fonctionne à l'envers : l'antenne reçoit le signal, qui est amplifié par un amplificateur de puissance. La démodulation est ensuite assurée par un démodulateur I/Q, afin d'extraire les symboles. Le dé-mapper associe à nouveau ces symboles aux données binaires d'origine. Le décodeur de canal se charge ensuite de détecter et de corriger les erreurs qui auraient pu apparaître pendant la transmission. Pour finir, le décodeur de source décomprime les données afin de reconstituer le signal d'origine, qui est alors reconverti en signal analogique par un convertisseur N/A et peut être restitué, par exemple, sur un haut-parleur au travers d'un amplificateur.

Nous résumons le traitement numérique du signal dans le récepteur en les trois étapes suivantes :

1. Dé-mapper : associer les symboles à des données binaires
2. Décodeur de canal : détecter et corriger les erreurs
3. Décodeur de source : décomprimer les données

<margin>
[picture:1063:a_sdr_empfänger:Récepteur SDR pour la communication en phonie]
</margin>

[question:AF628]
[question:AF629]
