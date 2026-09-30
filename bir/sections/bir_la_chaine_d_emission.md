L'émetteur fait le chemin inverse du récepteur : il part d'un son et fabrique une onde radio. Son schéma-bloc reprend des blocs que nous connaissons déjà, et en ajoute d'autres.

<margin>
[picture:735:bir_schema_emetteur:Le schéma-bloc d'un émetteur simple]
</margin>

---

Suivons le signal dans l'ordre des numéros de la figure [ref:bir_schema_emetteur] :

1. **Le microphone** change la voix en signal basse fréquence.
2. **L'amplificateur basse fréquence** renforce ce signal.
3. **Le mélangeur** combine la voix avec la porteuse : c'est lui qui module.
4. **L'oscillateur** fabrique la porteuse, une sinusoïde à la fréquence d'émission.
5. **Un filtre** ne garde, à la sortie du mélangeur, que le signal voulu.
6. **L'amplificateur haute fréquence** porte le signal à la puissance d'émission.
7. **Un filtre passe-bas** élimine les fréquences indésirables produites par l'amplification.
8. **L'antenne** rayonne l'onde.

---

Dans un émetteur-récepteur, émetteur et récepteur partagent l'antenne, l'alimentation et souvent une partie de leurs circuits. La touche PTT commande un commutateur : relâchée, l'antenne est reliée au récepteur ; enfoncée, elle passe à l'émetteur.

[question:RB1801]
[question:RB1802]
[question:RB1803]
