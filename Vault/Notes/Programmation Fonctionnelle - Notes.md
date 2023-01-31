[[https://en.wikipedia.org/wiki/Functional_programming]]

# 10/01/2023

Deux notes par TP, pas d'examen ecrit

Fonctions recursives - prac

Examples in slides

OCaml: cast explicite necessaire (ex: addition de deux flottants et deux entiers sont des operations differentes)

Has type inference [[https://en.wikipedia.org/wiki/Type_inference]]

a' -> function will use return type of whatever function it depends on

Comments -> (* comment *)

## Creer fonctions a la volee

Fonction creer dans block de code

lambda -> important mot cle utilise dans beaucoup de langages

Examples in slides

filter (python / js / ocaml?) -> recupere les donnees selon parametres en entree
where = equivalent en c#

## Variables

let ... in ... -> variable prend la valeur dans le cas du in
Variable declaration: initial declaration carries over ontop of all function declaration until next redeclaration and will persist on all function declarations prior to redeclaration

## Fonctions
Ordre de prio: sans parentheses la premiere valeur a cote de la declaration de la variable est evaluee dans la fonction

### Declaration de fonctions
1. let f x = x+1 -> f prend x et renvoi x+1 (pas de return)
2. g = (fun y -> y * 1) / let h = fun y -> y * 2
3.  let h = function y -> y * 2

## Types
unit = void -> entered with ()
int
bool
string
function

## Conditions
Pas de if sans else pour concordance des types

## Boucles
no
recursion -> yes, recursion defined with rec after let


## Definir une fonction f qui prend deux entiers x et y et qui renvoie la somme de tous les entiers entre x et y
example: mine
let rec f a b =
	if b > a then
		(if b = 1 then a + 1
		else (a + f (a b-1)))
	else
		((if a = 1 then b + 1
		else (b + f (a-1 b)))

example: correct
	let rec f x y = if x = y then x else x + f (x+1) y
	or
	let rec f x y = if x > y then 0 else y + f x (y-1)

## Somme d'elements
let somme = f 0 -> stack overflow problem quand le nombre est trop grand
ou
example avec accu: 
	mine:
	let rec somme_aux n accu = (somme de tous les entiers de 0 a n qu'on ajoute a la variable accu)
	if n = 0 then accu 
	else accu + somme_aux (n-1) accu
	correct:
	let rec somme_aux n accu = if n = 0 then accu else let accu = accu + n in somme_aux n-1 accu
	ou 
	let rec somme_aux n accu = if n = 0 then accu else somme_aux (n-1) (accu + n)
	let somme n = somme_aux n 0

bonne def de somme_aux:
	let somme n =
		let rec aux n accu = 
			if n = 0 then accu
			else let accu = accu + n in aux (n-1) accu
	in aux n 0
aux n'existe que dans la fonction somme et plus globalement


# 17/01/2023
Variants  = type algebrique

type somme = entier et boolean (type union en c)
type produit = struct en c

## Type produit
fst renvoi partie gauche couple
snd renvoi partie droite couple

transformer pair en arguments multiples:
	let pair2args f = let g x y = f(x, y)in g
ou let pair2args f = fun x y -> f(x, y)
ou let pair2args f x y = f(x, y)

## Type somme
Jamais utiliser les memes noms dans les constructeurs

different du switch en C, on regarde la construction de l'objet

function pattern match, mais pas fun

exemple type qui peut renvoyer rien:
	type peutetreunentier = Entier of int | Rien;;
	let x = Entier 4
	let y = Entier 8
	let z = Rien
	peutetreunentier -> peutetreunentier -> peutetreunentier
	let somme x y = match x with
		 Entier X -> match y with 
				 Entier Z -> X+Z	
				 Rien A -> Rien
		 Rien  Y-> Rien
	solution:
		let somme a b = match a with
		| Rien -> Rien
		| Entier n -> match b with
			| Rien -> Rien
			| Entier m -> Entier (n + m)
	let somme a b = match(a, b) with
		(Entier n, Entier m) -> Entier (n+m)
		(Rien, Entier m) -> Rien
		(Entier n, Rien) -> Rien
		(Rien, Rien) -> Rien
	let somme a b = match(a, b) with
		(Entier n, Entier m) -> Entier (n+m)
		_ -> Rien                                            # cas par defaut

diap 15: ou est un et
diap 16: les variables nommees ne sont pas les memes si elles sont dans le match ou en dehors

Dans d'autres langages: combiner struct et union


let x = Fin
let y = Encore (2, Fin) 
let z = Encore (1,  y)

let longueur x = match x with
	| Nul -> 0
	| Cons y -> 1+ longueur y
Solution:
	let rec longueur l = match l with
		| Nul -> 0
		| Cons(x, l') -> 1 + longueur l'
	let rec longueur l = match l with
		| Nul -> 0
		| Cons( _ , l') -> 1 + longueur l'
	let rec aux l somme = match l with
		| Nul -> somme
		| Cons(x, l') -> aux l' (somme+1)
	let longueur l = aux l 0

n a 1


let rec range n = match n with
	| 1 -> nul
	| _ -> cons(n, l) range (n-1)
Solution:
	let rec range n = 
		if n = 0 then Nul
		else Cons(n, range(n-1))
	let range n = 
		let rec aux m l = 
			if m = 0 then l
			else aux (m-1) (Cons(m, l)) in aux n Nul

Recursion terminale necessaire a partir d'un million d'elements

|> envoi de l'objet de gauche a droite

tous les operateurs peuvent etre redefinis

let x = Fin 1
let y = (Encore(Fin 1, Fin 4)

open(Liste) ouvrir bib liste

# 31/01/2023

Paradigm map/reduce

## Reduce ('a -> 'a -> 'a) -> 'a -> [ 'a list -> 'a ]
Construit une fonction

let somme = reduce somme2 0
let max = reduce max2 0

let reduce func i = 
	let rec func_new l = function
		| [] -> i 
		| x::l -> func x (func_new l)
Solution:
let redure f init = 
	let rec g l = match l with
		| [] -> init
		| x::l' -> f x (g l')
	in g
ou
let rec reduce f init l = match l with
	| [] -> init
	| x::l' -> f x (reduce f init l')
ou
let rec reduce f init l = function
	| [] -> init
	| x::l' -> f x (reduce f init l')

mystere1: renvoi le premier element entre x et y 
mystere2: renvoi 0

Proprietes:  - element neutre
			      - associativite 

let somme = let rec somme_aux i= function
	| [] -> i
	| x::l -> i + somme_aux i l
	in 
	somme_aux 0 l

let max = let rec max_aux i = function
	| [] -> i
	| x::l -> if x>i max_aux x l else max_aux i l
	in
	max_aux 0 l

## Folding