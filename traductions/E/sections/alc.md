L'*Automatic-Level-Control (ALC)* (régulation automatique de niveau) régule l'excitation de l'étage final d'émission du poste et réduit, en cas de saturation de celui-ci, l'amplitude du signal dans la chaîne d'émission. L'ALC ne doit pas être confondue avec l'AGC (Automatic-Gain-Control), qui se trouve dans la chaîne de réception (voir figure [ref:e_alc]).

<margin>
[picture:914:e_alc:Automatic-Level-Control dans un émetteur]
</margin>

L'ALC mesure la puissance de sortie de l'étage final d'émission et la compare à une valeur maximale prédéfinie. En cas de dépassement de cette valeur limite, l'ALC délivre une tension de régulation correspondante à l'étage amplificateur HF situé en amont dans la chaîne d'émission et réduit ainsi l'amplitude du signal d'émission.

Tant que l'indicateur d'ALC ne réagit pas, on peut considérer que la régulation n'intervient pas et que l'émetteur n'est pas saturé par un signal BF trop fort. Dès que l'indicateur d'ALC réagit, on peut considérer que la régulation devient, au moins partiellement, active.

Pour les émissions en SSB, une légère intervention de l'ALC est tout à fait souhaitable, car elle compense les variations de volume de la voix et assure une utilisation optimale de la puissance d'émission disponible. Beaucoup d'émetteurs-récepteurs possèdent un indicateur d'ALC correspondant, sur lequel on peut le plus souvent voir jusqu'à quel degré l'ALC peut réagir (zone verte) et à partir de quelle zone se produit une excitation trop forte, que l'ALC ne peut plus compenser sans distorsion (zone rouge).

<margin>
[picture:915:e_alc_trx:ALC sur l'afficheur d'un poste radio]
</margin>

<tip>
En pratique, on peut trouver le point optimal, où l'ALC n'intervient tout juste pas encore, en augmentant lentement le niveau BF jusqu'au point où l'ALC réagit. On réduit ensuite un peu le niveau BF, de sorte que l'ALC ne réagisse tout juste plus et que l'indicateur de puissance d'émission affiche encore la puissance de sortie souhaitée (éventuellement un peu moins).
</tip>

---

Pour les émissions avec des procédés de transmission numériques comme par exemple le FT8 ou le WSPR, la réaction de l'ALC est souvent l'indice que le signal audio provenant du PC est trop fort et qu'il y a saturation. Cela peut conduire à du *splatter* indésirable sur la bande. C'est pourquoi le signal audio devrait toujours être soigneusement contrôlé avec ces procédés de transmission.

<indepth>
Le [manuel](https://50ohm.de/wsjtx) du logiciel WSJTX donne à ce sujet une bonne recommandation : dans un premier temps, on passe l'émetteur-récepteur en émission en appuyant sur la touche TUNE, afin de produire une tonalité régulière. Cette tonalité peut être vérifiée à l'oreille avec la fonction Monitor de l'appareil, ou contrôlée visuellement dans la cascade du TRX. Aucune distorsion, aucun clic ni autre perturbation ne devrait alors apparaître. On abaisse ensuite lentement le réglage PWR depuis son maximum jusqu'à ce que la sortie HF de l'émetteur diminue légèrement — cela est généralement considéré comme un bon niveau pour l'excitation audio. L'indicateur d'ALC ainsi que la puissance de sortie de l'émetteur-récepteur peuvent également aider à trouver le niveau de signal BF optimal.
</indepth>

[question:EF305]