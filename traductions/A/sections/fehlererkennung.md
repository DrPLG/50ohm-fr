La forme la plus simple de détection d'erreurs est réalisée en ajoutant un bit supplémentaire, le bit de contrôle. On l'appelle aussi *bit de parité* (Parity Bit). Il existe deux variantes de ce procédé. En parité paire (*Even Parity*), la valeur de ce bit est choisie, pour chaque bloc, de sorte que le nombre de bits mis à $\num{1}$ soit toujours pair. En parité impaire (*Odd Parity*), en revanche, ce nombre doit toujours être impair. L'émetteur et le récepteur doivent s'être accordés avant la transmission sur celle des deux variantes qui est utilisée.

<indepth>
Supposons que nous voulions transmettre l'octet suivant en parité paire :

[picture:677:byte:Un octet]

Nous comptons 5 uns, soit un nombre impair. Le bit de contrôle doit donc être mis à $\num{1}$, afin d'obtenir un nombre pair de uns :

[picture:678:even_parity:L'octet avec son bit de parité paire]

Si une erreur de transmission modifie alors *un* bit (de $\num{1}$ vers $\num{0}$ ou inversement), le nombre de uns devient impair. Le récepteur reconnaît à cela qu'une erreur est présente.

Voici un autre exemple : 

[picture:679:even_parity:Octet avec parité paire]

Dans l'octet initial, nous comptons 4 uns, ce qui correspond à un nombre pair. Nous devons donc insérer un $\num{0}$ comme bit de contrôle.
</indepth>

Ce procédé atteint rapidement ses limites, à savoir dès que plus d'une erreur survient lors de la transmission. Si deux bits sont modifiés pendant la transmission, le nombre de uns reste pair. Le récepteur ne peut plus reconnaître que des erreurs sont survenues. Si trois erreurs surviennent lors de la transmission, on obtient à nouveau un nombre impair de uns et le récepteur détecte les erreurs.

La parité impaire fonctionne en principe exactement de la même façon, à une seule différence près : le nombre de uns ne doit pas être pair, mais toujours impair. Pour la parité impaire comme pour la parité paire, seul un nombre impair de bits transmis de façon erronée est détecté. En revanche, une transmission sans erreur ne peut pas être distinguée d'un nombre pair d'erreurs.

[question:AE411]
[question:AE412]

Pour détecter les erreurs portant sur plusieurs bits, on peut ajouter d'autres bits de contrôle. Cela fonctionne très bien pour des messages de longueur fixe. Si la longueur des données est variable, on utilise souvent des procédés de somme de contrôle particuliers, comme le *contrôle de redondance cyclique (CRC)*, qui détectent les erreurs à une certaine probabilité résiduelle près. Des procédés analogues se rencontrent aussi dans la vie courante, par exemple pour les numéros de pièce d'identité ou l'IBAN.

[question:AE410]
