https://en.wikipedia.org/wiki/Functional_programming

# 10/01/2023

Deux notes par TP, pas d'examen ecrit

Fonctions recursives - prac

Examples in slides

OCaml: cast explicite necessaire (ex: addition de deux flottants et deux entiers sont des operations differentes)

Has type inference [[https://en.wikipedia.org/wiki/Type_inference]]

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


