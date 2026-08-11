Les oscillateurs dont la fréquence peut être commandée peuvent être réalisés de différentes manières. Une possibilité est l'*oscillateur commandé en tension VCO - Voltage controlled oscillator*.

[question:AD601]

---

Pour que la fréquence de l'oscillateur devienne variable, on peut insérer dans son circuit oscillant une diode à capacité variable, dont la capacité peut être influencée par une tension continue (cf. figure [ref:a_vco_schaltung]). Une variation de cette tension continue conduit alors à une variation correspondante de la fréquence de l'oscillateur. L'oscillateur devient ainsi accordable au moyen d'une tension de commande. 

<margin>
[picture:752:a_vco_schaltung:Montage VCO avec diode à capacité variable]
</margin>

La diode à capacité variable est exploitée en sens inverse. Plus la tension inverse de la diode est élevée, plus sa capacité est faible, celle-ci étant déterminée par l'étendue de la couche d'arrêt (jonction P-N). La couche d'arrêt s'élargit lorsque la tension inverse appliquée augmente, ce qui diminue la capacité et fait donc augmenter la fréquence du circuit oscillant conformément à la formule de Thomson.

Inversement, la couche d'arrêt de la diode à capacité variable se réduit lorsque la tension inverse appliquée diminue, ce qui augmente la capacité et fait donc diminuer la fréquence du circuit oscillant. La tension inverse peut par ex. être produite par un potentiomètre ou par un circuit de commande.

%TODO: Evtl. Grafik zu Sperrschicht und Verhalten in Kapazitätsdiode.

[question:AD218] 

Pour tous les montages d'oscillateur, indépendamment de leur réalisation, des réactions indésirables peuvent conduire à des instabilités de fréquence. Cela vaut aussi bien pour les VCO que pour les VFO (par ex. à condensateurs variables) ainsi que pour d'autres oscillateurs.

[question:AD611]