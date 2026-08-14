# Défauts constatés dans les sources amont

Registre annoncé par le §6 de `CLAUDE.md` (« Défauts amont : préservés et
documentés, jamais corrigés silencieusement ») et par le `README`. Créé le
14/08/2026.

Chaque entrée décrit un défaut de la source allemande, l'effet observé, et ce
qui a été fait côté français. **Rien n'est corrigé en amont, et rien n'est
corrigé silencieusement côté français.** Ces défauts font l'objet d'un
signalement au DARC, rédigé en allemand.

Le §8 de `CLAUDE.md` porte un relevé antérieur (labels dupliqués, deux-points
dans les légendes, `\tikzstyle` déprécié, coquilles). Il reste à migrer ici ;
il n'a pas été recopié tel quel faute d'avoir été revérifié un par un.

---

## 1. Référence orpheline `a_zeppelinantenn` — `antennenformen_3`

**Constaté le** 14/08/2026, sur l'instantané amont du même jour.

La section `contents/sections/antennenformen_3.md` écrit :

```
On parle alors d'une *Zeppelinantenne* (vgl. Abbildung[ref:a_zeppelinantenn]).
```

alors que le dessin est déclaré quelques lignes plus bas sous l'ident
`a_zeppelinantenne`, avec le `e` final :

```
[picture:314:a_zeppelinantenne:Aufbau einer Zeppelinantenne]
```

Deux défauts distincts sur la même ligne : l'ident tronqué, et l'espace
manquant entre `Abbildung` et `[ref:`.

**Effet.** `build_book.py` lève « référence orpheline (\ref sans \label) » et
la référence sort en `??` dans le PDF. Le livre allemand est touché à
l'identique.

**Côté français.** L'ident est préservé verbatim, conformément au §6 qui impose
de conserver les idents « y compris les fautes d'orthographe allemandes
d'origine ». L'espace manquant, lui, relève de la typographie de la prose et
non de l'ident : la traduction écrit `cf. figure [ref:a_zeppelinantenn]` avec
l'espace normal.

**Conséquence de contrôle.** Le nombre de `??` attendus dans le PDF de la
classe A passe de 2 à 3. Le tableau du §4 de `CLAUDE.md` a été mis à jour.

---

## 2. Caractère accentué nu en mode mathématique — `antennenformen_3`

**Constaté le** 14/08/2026.

La même section écrit le rapport de transformation d'un transformateur ainsi :

```
mit einem Übersetzungsverhältnis von $ü = 1:7$
```

Le `ü` est placé **nu en mode mathématique**. LuaLaTeX le compose alors dans
l'italique mathématique (`cmmi8`), qui ne possède pas ce glyphe.

**Effet.** Le journal signale `Missing character: There is no ü (U+00FC) in
font cmmi8!` et **le caractère disparaît du PDF** : le lecteur lit
« rapport de transformation de = 1:7 ». Vérifié par extraction du texte du PDF
compilé. Le livre allemand est touché à l'identique.

**Côté français.** Formule préservée verbatim (§5 : « formules `$…$`
verbatim »). Le défaut est donc reproduit tel quel.

**À noter** : c'est la démonstration du mécanisme derrière la règle du §6
(« jamais d'accent dans `\mathrm{}` »), avec une frontière plus précise que
celle qui y est écrite. Un accent placé dans `\mathrm{}` ou `\text{}` **passe**
sans dommage, ces macros basculant sur une police de texte qui possède les
glyphes accentués ; c'est le caractère accentué **nu**, composé en italique
mathématique, qui disparaît.

---

## 3. `\qty{0.05}{\lambda}` — unité composée d'une macro mathématique

**Constaté le** 14/08/2026, dans `antennenformen_3` (contenu ajouté en amont
après notre traduction initiale).

```
oder ein Teil der koaxialen Zuleitung (mindests $\qty{0.05}{\lambda}$)
```

`\lambda` est passé à `siunitx` comme **unité**. siunitx la compose dans la
police de texte droite, où le glyphe U+1D706 (lambda mathématique) est absent
de Libertinus Serif.

**Effet.** `Missing character: There is no 𝜆 (U+1D706) in font
[LibertinusSerif-Regular.otf]` et **le lambda disparaît du PDF** : le lecteur
lit « au moins 0,05 », sans unité, ce qui ne veut rien dire. Vérifié par
extraction du texte. siunitx convertit par ailleurs correctement `0.05` en
`0,05` en français.

Même famille que le `\qty{120\pi}{\ohm}` du §8, contourné en v0.14 de
`build_book.py` par `fix_latex()`.

**Côté français. Contourné en v0.16 de `build_book.py`**, sur décision de
Pierre du 14/08/2026 et sur le modèle de la v0.14 :

```python
text = re.sub(r"\\qty\{([0-9.,]+)\}\{\\lambda\}", r"\\num{\1}\\,\\lambda", text)
```

`\num{}` est conservé plutôt que le nombre brut : c'est lui qui rend la virgule
décimale française. **La source amont n'est pas touchée** — la correction vit
dans le générateur, comme pour la v0.14. Vérifié après coup : zéro
« Missing character U+1D706 » au journal, et le PDF affiche « au moins
0,05 λ ». Le livre allemand, lui, reste affecté.

Coquille associée dans la même parenthèse : `mindests` pour `mindestens`.
