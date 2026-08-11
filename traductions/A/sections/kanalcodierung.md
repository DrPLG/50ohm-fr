La figure [ref:kanal] montre un émetteur et un récepteur, reliés entre eux par un canal. Des perturbations peuvent apparaître sur le canal, par exemple du fait de la météo, d'autres influences atmosphériques ou des émissions d'autres stations. Elles peuvent conduire à des erreurs lors de la transmission. 

<margin>
[picture:674:kanal:Canal]
</margin>

Contrairement au codage de source, le codage de canal ajoute délibérément de la redondance à l'information à transmettre, par exemple des répétitions ou des sommes de contrôle. À la différence de la redondance retirée lors du codage de source, cette redondance ajoutée de façon systématique peut servir à la détection ou à la correction automatique des erreurs de transmission.

---

La figure [ref:kanalcodierer] montre un symbole de codeur de canal. Le bloc représente le fait que de la redondance est ajoutée aux données.

<margin>
[picture:676:kanalcodierer:Codeur de canal]
</margin>

[question:AE409]

Nous distinguons deux types de codage de canal :

* Détection d'erreurs : on peut reconnaître qu'une erreur est survenue lors de la transmission et demander alors, p. ex., une nouvelle transmission.
* Correction d'erreurs directe : les erreurs apparues lors de la transmission sont corrigées chez le récepteur à l'aide de la redondance. 

Nous allons examiner ces deux types de plus près dans ce qui suit.