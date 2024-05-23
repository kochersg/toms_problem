# toms-problem
*Gerrit Kocherscheidt, Mai 2024*

## Problemstellung
Es soll eine Wahrscheinlichkeitsverteilung *P(n,k,s)* für die Anzahl an Bewegungen zu einzelnen Lagerplätzen ermittelt werden. Es werden *n* eindeutige Artikel gleichmäßig über *k* Lagerplätze verteilt. Es werden in einem Lagersuchlauf *s* bestimmte Artikel entnommen. Wie groß ist die Wahrscheinlichkeit *P(n,k,s)*, dass *z* Lagerplätze abgesucht werden müssen. Hierbei liegt die Anzahl z zwischen 1 und *s*.

## Mathematische Formulierung

### Vorüberlegung
Für eine bekannte Konstellation von Artikeln, die aus den Lagerplätzen geholt werden sollen, kann die Wahrscheinlichkeit für das Auftreten exakt dieser Konstellation über eine hypergeometrische Verteilung beschrieben werden [[1]](https://www.mathe-seite.de/oberstufe/wahrscheinlichkeit-stochastik/hypergeometrische-verteilung/).

**Beispiel**
Ein Lager besteht aus 2 Lagerplätzen und es werden insgesamt 20 Artikel auf gleichmäßig auf diese Plätze verteilt. Es sollen 10 bestimmte Artikel kommissioniert werden. Auf Lagerplatz 1 liegen 5 Artikel, auf Lagerplatz 2 liegen weitere 5 Artikel.

Die Wahrscheinlichkeit für das Auftreten dieser Konstellation ist gegeben durch 
$$
P(L1:5, L2:5) = \frac{\binom{10}{5}\cdot\binom{10}{5}}{\binom{20}{10}}=\frac{252^2}{184756} \approx 0,344
$$
In diesem Fall lässt sich die Verteilung $P_S$, dass man entweder einen oder zwei Lagerplätze besuchen muss einfach berechnen. 

Für einen Lagerplatz müssen die Wahrscheinlichkeiten $P(L1:10)$ und $P(L2:10)$ addiert werden:
$$
P(L1:10) = P(L2:10) = \frac{{\binom{10}{10}}}{\binom{20}{10}} = \frac{1}{184756}
$$
Daraus folgt:
$$
P_S(1) = 2*P(L1:10) \approx 0.00001
$$
$$
P_S(2) = 1-P_S(1) \approx 0.99999
$$

### 

## Referenzen
[1] https://www.mathe-seite.de/oberstufe/wahrscheinlichkeit-stochastik/hypergeometrische-verteilung/
