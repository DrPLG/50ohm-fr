Dans la classe N, nous avons déjà appris que l'exploitation à distance n'est autorisée qu'aux radioamateurs de la classe A. C'est pourquoi nous allons examiner ici quelques aspects techniques de l'exploitation à distance, pertinents pour la mise en œuvre et l'utilisation d'une station distante. 

Une station pour l'exploitation à distance (remote) se compose de plusieurs blocs fonctionnels logiquement séparables les uns des autres. Sur les appareils modernes, certains de ces blocs fonctionnels peuvent aussi être intégrés dans un seul appareil (par exemple un émetteur-récepteur avec raccordement réseau et interface remote).

Une installation pour l'exploitation à distance peut être représentée logiquement par les blocs fonctionnels suivants.

---

<margin>
[picture:501:a_remotebetrieb:Schéma fonctionnel de l'exploitation à distance]
</margin>

* *Ordinateur et panneau de commande de l'opérateur (bloc 1)* : il sert à commander la station distante. Les signaux audio ainsi que les signaux de commande y sont convertis localement en paquets réseau et transmis à la station distante. Les signaux de commande et les signaux audio reçus de la station distante (qui sont transmis par le réseau) sont de nouveau rendus audibles et visibles par l'ordinateur ou le panneau de commande.
* *Réseau* : réseau ou réseaux de liaison entre le site de l'opérateur et la station distante. Internet peut ici aussi servir de réseau entre les deux sites.
* *Ordinateur ou interface remote sur le site distant (bloc 2)* : il convertit les paquets réseau reçus de l'opérateur en signaux de commande et signaux audio destinés à la commande de l'émetteur-récepteur sur le site distant et transmet en retour, par le réseau, les signaux audio reçus par l'émetteur-récepteur vers l'opérateur. Les réglages de l'émetteur-récepteur ainsi que les signaux de commande en retour sont également transmis à l'opérateur par le réseau.
* *Émetteur-récepteur/amplificateur/boîte d'accord/rotor d'antenne (bloc 3)* : ces appareils sont commandés, avec retour d'état, par l'interface remote ou par un ordinateur situé sur le site distant, au moyen des signaux que l'opérateur transmet à l'interface remote par le réseau.

[question:AF701]
[question:AF702]
[question:AF704]
[question:AF703]
[question:AF705]

---

En exploitation à distance, les temps de propagation dans le réseau et les temps de traitement lors du codage et du décodage des signaux audio entraînent des retards. Il faut en tenir compte lors du trafic radio par stations distantes.

<tip>
[photo:342:a_remote_station:Station distante du DARC e. V.]

Le DARC e. V. exploite pour ses membres plusieurs stations-club distantes, réparties dans toute l'Allemagne. Sur [mein.darc.de](https://mein.darc.de/), les membres peuvent se connecter aux stations distantes et faire du trafic radio par Internet, s'ils sont titulaires d'une licence de classe A. Pour les classes N et E, seule l'écoute (SWL) est possible.

[Devenez membre du DARC dès maintenant !](https://50ohm.de/mw)
</tip>

[question:AF709]
[question:AF710]

Pour garantir qu'une station distante ne tombe pas dans un état ou un fonctionnement incontrôlé en cas de rupture ou de perturbation de la liaison de données entre l'utilisateur ou le panneau de commande et l'interface remote, une surveillance et un retour d'information permanents entre l'opérateur et la station distante sont nécessaires, au moyen de ce qu'on appelle un chien de garde (watchdog). Des paquets de données sont par exemple envoyés à intervalles de quelques secondes par la station distante à l'ordinateur de l'opérateur ; ils doivent être acquittés dans un temps déterminé par une réponse en retour. Si cette réponse en retour ne survient pas, la station distante sait que la liaison avec l'opérateur est interrompue et peut mettre d'elle-même l'émetteur-récepteur dans un état sûr défini (par exemple en mode réception) et interrompre une émission en cours.

[question:AF708]

Comme l'émetteur-récepteur lui-même peut aussi se retrouver dans un état indéfini (par exemple du fait d'une erreur logicielle ou matérielle dans l'appareil), la tension d'alimentation de l'émetteur-récepteur devrait pouvoir être coupée à distance. Cela peut se faire par exemple au moyen d'une prise IP, que l'opérateur peut commander par le réseau.

[question:AF707]

Lors de l'exploitation d'une station distante, il faut également tenir compte du fait, et s'attendre à ce, que des composants de la station distante puissent être perturbés par l'émetteur-récepteur situé sur le site de la station distante.

[question:AF706]