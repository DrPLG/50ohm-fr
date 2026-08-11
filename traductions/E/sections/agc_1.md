La régulation automatique de gain *(Automatic-Gain-Control, en abrégé AGC)* veille, dans les récepteurs, à ce que le signal de sortie BF (volume de réception) reste à peu près constant même lorsque le signal d'entrée HF au récepteur fluctue (par exemple à cause du fading), et à ce que les variations de volume soient réduites. Pour cela, le niveau de réception est mesuré à la sortie de la chaîne de réception et le gain HF est régulé en conséquence, de sorte que le volume de réception après démodulation peut ainsi être maîtrisé. L'AGC ne doit pas être confondue avec l'ALC (Automatic-Level-Control), qui se trouve dans la chaîne d'émission.

<margin>
[picture:1055:e_agc:AGC dans un récepteur superhétérodyne]
</margin>

---

Selon l'équipement du récepteur, l'AGC peut être ajustée en ce qui concerne son comportement de réponse (temps de réponse, temps de retombée). Les désignations usuelles sont AGC Slow, AGC Normal, AGC Fast, qui esquissent le comportement temporel de la régulation. Le réglage AGC-Slow ou Normal est normalement judicieux pour le trafic en SSB. En télégraphie (CW), le réglage AGC-Fast ou Normal est normalement judicieux, afin que des signaux forts ne puissent pas masquer des signaux faibles et que la régulation suive rapidement. Pour les procédés de transmission numériques, il peut être judicieux, le cas échéant, de désactiver l'AGC.

[question:EF211]
[question:EF212]

<tip>
Sur certains récepteurs, l'AGC peut aussi être complètement désactivée. Une commande du gain HF est alors possible, par exemple manuellement, en agissant sur le réglage RF-Gain. Ceci n'est toutefois judicieux que pour des applications particulières (par exemple saturation de l'étage d'entrée HF due à des signaux forts), ainsi que, le cas échéant, pour les procédés de transmission numériques.
</tip>