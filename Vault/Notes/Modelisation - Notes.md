
# 13/01/2023

## Chap 1

### 1.1 Definitions
Definition 1.1: Un graphe G = (V, E) est un couple ou V = {x1, -, xn} est un ensemble (fini) de sommets (vextex), E inclu dans V x V est un ensemble d'arcs (edge). On note gamme+(u) = {V | (u, v) appartient a E}.
On note gamma-(u) {v | (v, u) appartient a E}
d+(u) = |gamma+(u)| : degre sortant de u
d-(u) = |gamma-(u)| : degre entrant de u

fig 1

### 1.2 Parcours en profondeur
Definition 1.2: Un chemin dans un graphe g=(V, E) entre deux sommets u et v est une suite de sommets u0, u1, u2, ..., uk tel que:
	- u0 = u
	- u1 = v
	- Pour tout i, (ui, u(i+1)) appartient a E
Un chemin est dite elementaire si tous les sommets du chemin (sauf eventuellement les extremites) sont differents. Sauf indication contraire, dans la suite tous les chemins sont elementaires. Un circuit est un chemin dont les extremites sont identiques.
Chemin elementaire: tous les sommets (excepte eventuellement les extremites) sont differents
Un circuit est un chemin (u0, ..., un) ou u0 = un
L'algo classique pour prouver ou chercher l'existence d'un chemin entre u et v est le parcours en profondeur d'abord (DFS)

### 1.3 Graphes sans circuits
#### 1.3.1 Tri topologique
Definition 1.3: Un tri topologique d'un graphe G = (V, E) est une **numerotation** *numero* des sommets de sorte que s'il y a une arete de u a v alors numero[u] < numero[v]
Definition 1.4: Un graphe est un DAG (Directed Acyclic Graph) si il est sans circuits
Theoreme 1.2: Un tri topologique existe sur le grapje G si et seulement si G est un DAG.

Comment obtenir un tri topologique?

Theoreme 1.3: La numerotation des sommets signifie que s'il existe une arete de u a v alors numero[u] > numero[v] : les numeros sont dans **l'ordre inverse** de l'ordre donne
 - last 3 lines of dfs cause it

Definition 1.5: Une sources dans un graphe G = (V, E) est un sommet s tel que gamma-(s) = {Ensemble vide} (aucun arc n'arrive sur s)
Un puit est un sommet p appartenent a V tel que gamma+(p) = {ensemble vide}

Theoreme 1.4: Dans un DAG, il existe au moins une source et un puit.

Preuve: Supposons le contraire. On part d'un sommet quelconque s. Comme s n'est pas un puit, alors s possede un voisin "sortant" s1. Comme s1 n'est pas un puit, alors s1 possede un voisin "sortant" s2. Comme le nombre de sommets est fini, on est oblige de boucler a un moment donné.
Or G est un DAG. = Contradiction.
On obtient un autre algorithme pour trouver un tri topologique: tant qu'il existe une source s, on la selectionne puis on la supprime.

Defintion 1.6: (rang)
Dans un DAG, le rang d'un sommet u est la longueur du **plus long chemin** arrivant en u.
Recursivement: rang(u) = 0 si u est une source. rang(u) = 1+max{rang(v) | (v, u) appartient a E}
Pour calculer le rang, il suffit de calculer le rang dans l'ordre donné par un tri topologique
exemple: la plus longue sous-suite strictement croissante dans 5, 2, 8, 6, 3, 6, 9, 7

#### 1.3.2 Chemins dans le DAG
Theoreme 1.5: Soit G un DAG muni d'un tri topologique. Soit u un sommet de G. Le plus court chemin T[v] (en nombre d'aretes) entre u et v peut-etre calculé comme suit:
	- T[u] = 0
	- T[v] = 1+min{T[w] | (w, v) appartient a E}
On initialise T a +inf et on evalue T dans l'ordre donné par un tri topologique.

Theoreme 1.6: Soit G un DAG muni d'un tri topologique. Soit u un sommet de G. Le plus long chemin T[v] (en nombre d'aretes) entre u et v peut-etre calculé comme suit:
	- T[u] = 0
	- T[v] = 1+max{T[w] | (w, v) appartient a E}
On initialise T a -1 et on calcule T dans l'ordre donné par un tri topologique.


## Chap 2

### 2.1 Numerotation des sommets
On peut distinguer les sommets par 3 couleurs:
	- blanc quand ils n'ont pas encore été vus
	- gris quand ils sont en cours de traitement
	- noir quand ils ont finis d'etre traités
graphe p7-8

Theoreme 2.1: 
	- Soit u un sommet. Le sommet v sera visite au cours de l'appel recursif de dfs(u) si et seulement si il existe un chemin de u a v constitué **uniquement de sommets blancs** (u et v compris) au moment ou dfs(u) est appelé. 
	- En particulier, si debut[u] < debut[v] et fin[u] > fin[v], alors il existe un chemin de u a v.

add global d, global f to dfs

Corollaire 2.2: Dans un DAG, s'il existe une arete de u a v, alors fin[u] > fin[v]
Preuve: deux cas:
	- debut[v] < debut[u]. Par contradiction, si fin(v) > fin(u), alors on aurait un chemin de v a u et donc un cycle
	- debut[u] < debut[v]. Au moment de l'appel a dfs[u], il existe une arete de u a v, qui sont tous les deux **blancs**, donc un chemin blanc entre u et v et donc v va etre visité lors de l'appel dfs(u) ce qui implique que fin[u] > fin[v]

### 2.2 Classification des aretes
Theoreme 2.3: G un DAG, s un sommet. Soit V' l'ensemble des sommets qui deviennent noirs a l'appel de dfs(s). E' l'ensemble des aretes qui ont conduit a un appel de dfs(w). Alors G' = (V', E') est un **arbre**, ou les fleches pointent a l'opposé de s(racine) . Si on appelle dfs sur tout les sommets non visités, les aretes forment une foret.