Dans les procédés de transmission numériques, les bits à transmettre doivent être associés aux différents symboles possibles. Cette association est appelée *mapping*. Le bloc qui procède à cette association est appelé *mapper*. Le symbole fonctionnel d'un mapper est représenté à la figure [ref:a_mapper]. Le mapper reçoit un flux binaire numérique et associe les combinaisons de bits qu'il contient aux symboles correspondants dans un diagramme de constellation.

<margin>
[picture:1102:a_mapper:Schéma fonctionnel d'un mapper]
</margin>

---

Pour découvrir le principe du mapping, considérons d'abord la *modulation par déplacement d'amplitude* (*Amplitude-Shift Keying*, ASK), déjà connue de la classe E. La figure [ref:a_ask] montre une ASK binaire en représentation temporelle. L'amplitude du signal porteur y est commutée entre deux valeurs. Une grande amplitude peut par exemple représenter le bit $1$, et une petite amplitude le bit $0$.

<margin>
[picture:700:a_ask:ASK (Amplitude-Shift Keying) en représentation temporelle]
</margin>

---

Les deux symboles possibles peuvent aussi être représentés dans le diagramme de constellation découvert précédemment. Comme, dans cet exemple, seule l'amplitude change et que la phase reste la même, les deux points de signal se situent sur l'axe I. La différence de distance à l'origine correspond aux deux amplitudes différentes. Une valeur binaire est maintenant associée à chacun des deux points de signal par le mapping.

<margin>
[picture:1128:a_ask_mapping:ASK (Amplitude-Shift Keying) dans le diagramme de constellation]
</margin>

---

Une modulation par déplacement d'amplitude n'est pas limitée à deux amplitudes possibles. Si l'on emploie par exemple quatre amplitudes différentes, on dispose de quatre symboles différents. Comme deux bits permettent de former quatre combinaisons de bits différentes, chaque symbole peut se voir attribuer l'une des combinaisons $00$, $01$, $10$ ou $11$.

La figure [ref:a_4_ask] montre une telle *4-ASK*, à quatre amplitudes différentes, en représentation temporelle. On peut par exemple employer $\qty{25}{\percent}$, $\qty{50}{\percent}$, $\qty{75}{\percent}$ et $\qty{100}{\percent}$ de l'amplitude maximale. Chaque symbole permet ainsi de transmettre deux bits.

<margin>
[picture:701:a_4_ask:Modulation par déplacement d'amplitude quaternaire (Quaternary Amplitude-Shift Keying)]
</margin>

Le diagramme de constellation comporte lui aussi désormais quatre points de signal possibles. Comme seule l'amplitude continue de changer, les quatre points se situent dans cet exemple sur l'axe I. Une combinaison de bits déterminée est associée à chaque point.

<margin>
[picture:1129:a_4_ask_mapping:Modulation par déplacement d'amplitude quaternaire (Quaternary Amplitude-Shift Keying) dans le diagramme de constellation]
</margin>
