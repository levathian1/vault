
# Links
https://en.wikipedia.org/wiki/Hypergraph

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
Theoreme 2.3: Soit s un sommet. Soit V' l'ensemble des sommets qui deviennent noirs a l'appel de dfs(s). E' l'ensemble des aretes qui ont conduit a un appel de dfs(w). Alors G' = (V', E') est un **arbre**, ou les fleches pointent a l'opposé de s(racine) . Si on appelle dfs sur tout les sommets non visités, les aretes forment une foret, appelee **foret d'exploration** du graphe.

On classifie en 4 categories les aretes du graphe d'origine:
	- arete(u, v) de l'arbre qui a permis de visiter de nouveau sommets lors de l'exploration
	- arete avant (u, v) telle que (u, v) n'est pas une arete de l'arbre d'exploration, v est un descendant de u **dans la foret** => v est noir au moment ou l'arete (u, v) est traitee (vert sur pdf)
	- arete arriere (u, v) telle que u est un descendant de v dans la foret. v est gris au moment ou l'arete (u, v) est traitee (bleu sur pdf)
	- arete croisee (u, v) telle que u n'est pas descendant de v et v n'est pas descendant de u, dans la foret. v est noir au moment ou (u, v) est traitee et debut[v] < debut[u] (rouge sur pdf)

Theoreme 2.4: Un graphe est un DAG si et seulement si le DFS ne rencontre **aucune arete arriere**
On peut simplifier un graphe en regroupant ensemble les **composantes fortement connexes** => utilite: on obtient ainsi un DAG

# 17/01/2023

### 2.3 Composantes fortement connexes
Definition 2.1: Un graphe est fortement connexe si pour tous sommets u et v de G, il existe un chemin de u vers v dans G.
Une composante fortement connexe de G est un **sous-graphe maximal** fortement connexe de G 
u et v appartienent a la meme composante fortement connexe si et seulement si il existe un chemin de u vers v et un chemin de v vers u dans G (soit un cycle passant par u et v)

Definition 2.2: Soit G un graphe, le graphe reduit Gr de G est le graphe dont les sommets sont les composantes fortement connexes de G et il existe une arete de S a T dans Gr si et seulement si il existe s appartenant a S et t appartenant a T tels que (s, t) appartient a E.

Theoreme 2.5: Le graphe reduit est sans circuit.
	Preuve: Soit S1, S2, ..., Sn = S1 un circuit dans le graphe reduit
	Il existe s1 appartenant a S1 et t1 appartenant a S2 tel que  (s1, t1) appartient a E
	Il existe s2 appartenant a S2 et t2 appartenant a S3 tel que (s2, t2) appartient a E
	...
	Il existe sn-1 appartient a Sn-1 et tn-1 appartient a Sn = S1 tels que (sn-1, tn-a) appartient a E
	Donc s1 et t1 sont dans la meme composante fortement connexe => contradiction

Comment calculer les composantes fortement connexes?
Theoreme 2.6: 
	1. effectuer un DFS en numerotant les sommets par ordre suffixe(quand ils deviennent noirs)
	2. effectuer un DFS sur le graphe mirroir G' = (V', E') (V= V' et (u,v) appartient a E <=> (v, u) appartient a E') en procedant dans **l'ordre inverse** de l'ordre suffixe
		Chaque arbre de la foret d'exploration du second DFS est un composante fortement connexe


### 2.4 Fermeture transitive
Definition 2.3: La fermeture transitive d'un graphe G=(V, E) est le graphe Gbarre = (V', E') V' = V, (u, v) appartient a E' si et seulement si il existe u = u0, un dans V tels que u0, un appartient a E

Calcul de la fermeture transitive:
	Algo le plus simple: T[u, v, k] = True si et seulement si il existe un chemin de u a v dans G de longueur exactement k
	T[u, v, 1] = True ssi (u, v) appartient a E
	T[u, v, k] = OU (pour tout les w appartenant a V) T[u, w, k-1] et T[w, v, 1]
	W[u, v] = OU (pour k < n) T [u, v, k]
	Un autre algo: avec le graphe reduit
		1. Calculer le graphe reduit de G
		2. Calculer la fermeture transitive Gbarre(r)de Gr
		3. Il existe une arete de u a v dans Gbarre ssi il existe une arete de la composante fortement connexe de u a la composante fortement connexe de v dans Gbarre(r)
Calculer la fermeture transitive du graphe Gbarre(r), ie un DAG
	On calcule L[u] : l'ensemble des sommets v atteignables a partir de u
		L[u] = Union (v appartient a delta+(u)) L[u] union delta+(u)
	et peut se calculer dans l'ordre inverse donne par un tri topologique
	Complexite: O(mn)

## Chap 3
### 3.1
Definition 3.1: Un graphe pondere est un graphe G = (V, E) muni d'une fonction c: E -> R qui associe a chaque arete e un cout c(e)
Le cout d'un chemin constitue des aretes e1, e2, ..., en est somme(i) c(ei)
Principe d'optimalite de Bellman:	
	Theoreme 3.1: Soit s = u0, u1, ..., un = t le CCM de s a t dans G = (V, E) pondere. Alors pour tout i, u0, u1, ..., ui est un CCM de s a t
Notons T[u] le cout du CCM entre s et u
Theoreme 3.2: Il existe (u, v) appartient a E => T[u] + c(u, v)
En fait on a:
	T[v] = min {T[u] + c(u, v) | u appartient a delta-(v)}

Algo de Ford:
	Tant qu'il existe une arete (u, v) tel que T[v] > T[u] + c(u, v) alors faire T[v] <- T[u] + c(u, v)
Algo revisite:
	Tpow(k) [u]: le cout du CCM entre s et u de longueur <= k
	T[u] = Tpow(n-1)[u] 
	pour tout k entre 0 et n-1:
		Tpow(k)[s] = 0
		pour tout u != s:
			Tpow(k) [v] = min (u appartient a delta-[v]) Tpow(k-1)[u] c(u, v)
On peut encore ameliorer:
	1. on peut arreter des que l'on stagne (Tpow(k-1) = Tpow(k))
	2. a l'etape k, il suffit de considerer les sommets u qui sont successeurs de sommets qui ont change de valeur a l'etape k-1 (les autres ne bougeront pas)

Algo de Bellman (sur DAG):
Theoreme 3.3: si G est un DAG, le cout du CCM entre s et t peut se calculer par la formule: 
						T[v] = min {T[u] + c(u, v) | u appartient a delta-(v)}
en evaluant les sommets dans l'ordre d'un tri topologique


### 3.2 Chemin de cout minimal contraint
On suppose certaines aretes rouges. On s'interesse aux CCM entre s et d qui passent par au plus une arete rouge

Principe d'optimalite de Bellman
	Theoreme 3.4:
		Soit s = u0, u1, ..., ul = ; un CCM de s a t utilisant moins au plus une arete rouge
		Pour tout i appartenant a {0, 1, ..., n}, in a le chemin de u0, ..., uk est un CCM de s a uk pour ceux qui n'utilisent pas plus d'aretes rouges que u0 -> ui

Ce principe d'optimatlite conduit a:
	- T0[u] est le CCM entre s et u qui n'utilise aucune arete rouge
	- T1[u] utilise exactement une arete rouge

Theoreme 3.5
	T0[v] = min{T0[u] + c(u, v) | u appartient a gamma-(v) est une arete non rouge}
	T1[v] = min{min{T0[u] + c(u, v) | u appartient a gamma-(v) est une arete rouge}, T1[u] + c(u, v) | u appartient a gamma-(v) est une arete non rouge}	

### 3.3 Chemin de cout minimal contraint
On se place: des couts sur les aretes. on ajoute des ressources

Choisir une arete engendre un consommation de ressources r(e)>= 0
plusieurs types de contraintes
	- Contraintes finales: sur la quantite totale de ressources utilisees
	- Contraintes par sommets: pour chaque sommet u, deux parametres au et bu on peut passer par u si la consommation de la ressource est entre ai et bi

Theoreme 3.6: Soit s = u0 -> uk = t le CCM de s a t utilisant moins de K ressources. Pour chaque sommet ui du chemin, soit ki la consommation de ressources sur le chemin u0 -> ui
Pour tout i u0 -> ui est un CCM de s a ui parmi ceux qui n'utilisent pas plus de ki ressources

Principe de Bellman => pour chaque sommet ui, il faut a priori retenir pour chaque valeur k, la valeur de plus petit chemin de s a ui consommant k ressources 

Theoreme 3.7: Soit T[u, k] le CCM de s a u consommant k ressources
	T[u, k] verifie: 1. T[s, k] = 0
						   2. T[v, k] = min{T[u, k - r(u, v)] + c(u, v) | u appartient a gamma- (v)}

Definition 3,2:
	Soit s = u0, u1, ..., ui un chemin
	L'etiquette du chemin est le couple (c, u) contient le cout du chemin et la consommation de la ressource
Definition 3.3:
	Une etiquette E = (c, r) est dominee par une etiquette E = (c', r') si c >= c' et r >= r'
Soit S un ensemble d'etiquettes. L'ensemble des etiquettes de S qui sont domines par aucune etiquette de S est appelee enveloppe de Pareto de S, notee Env(S)

On ne va retrouver que les etiquettes dominees par aucune.

Theoreme 3.8:
	Soit S[u] l'ensemble des etiquettes possibles de s a u.
	T = Env(s) verifie:
		1. T[s] = {(0, 0)}
		2. T[v] = Env{Union(T[s] + c(u, v), r(u, v) | u appartient a gamma-(u))}

## Chap 4

Definition 4.1: Un reseau (de flots) N est un graphe G = (V, E) ou chaque arete est munie d'une capacite, c(e).
Remarque: on ne distinguera pas les aretes de capacite nulle avec les aretes inexistantes
	- Une fonction de balance est une fonction b: V -> R. Si b(u) > 0 on a que u est sommet d'offre. Si b(u) < 0, alors on dit que u est un sommet de demande.
	- Un float sur un reseau est une fonction phi: E->R telle que 0 <= phi(e) <= c(e)
	- On dit que le flot phi satisfait la balance b si en chaque sommet v: Somme(phi(v, u) | u appartenant a gamma+(v)) = Somme(phi(u, v) | u appartenant a gamma-(v)) = b(v)
	- Une circulation est un float de balance nulle
	- Un float de s a t est un flot de balance nulle partout sauf pour s et t avec b(s) = -b(t) > 0

### 4.1 Flot max
#### 4.1.1 Def et graphe residuel

