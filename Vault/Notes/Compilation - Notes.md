# 09/01/2023

De Zoot a MIPS (RISC asm) in Java

Ressources:
	- Compilation des langages de programmation
	- Compilers: Principles, techniques, tools

Requierments:
	- Theories des langages
	- Grammaire 
	- Analyse lexicale
	- semantique des langages
	- Programmation assembleur
	- Traduction systematique
	- Paradigmes des langages de programmation
	- Gestion de la memoire, garbage collector
	- Optimisation
	- Allocation de registres

Books on ScholarVox:
	http://univ.scholarvox.com.bases-doc.univ-lorraine.fr/catalog/book/docid/88919695?searchterm=compilers
	http://univ.scholarvox.com.bases-doc.univ-lorraine.fr/catalog/book/docid/88809109?searchterm=compilers
	http://univ.scholarvox.com.bases-doc.univ-lorraine.fr/catalog/book/docid/88809585?searchterm=compilers
	http://univ.scholarvox.com.bases-doc.univ-lorraine.fr/catalog/book/docid/88853434?searchterm=compilers

Vocabulaire:
	Bloc: suite d'instructions a laquelle il est possible d'attacher une liste de declarations
	Declaration d'un identificateur: construction qui defini la nature de l'objet designe
	Portee d'une declaration: partie d'un programme dans laquelle une utilisation de l'identificateur se rapporte a cette declaration
	Espace de noms: pas de double declaration dans le meme espace, double declaration possible dans deux espaces differents
	Identification: mecanisme qui consiste a associer une utilisation d'identificateur a la declaration correspondante

# 16/01/2023

## Comment realiser un compilateur
application de regles de grammaire
application de la semantique
### Mesures de qualite
Equivalence cible source
	performance du code genere:
		- temps d'execution et place memoire requis pour le compilateur
		- temps d'execution et place memoire requis pour le texte cible (objet compile)
	Schema en T:
		mise en evidence du besoin de trois langages (y compris lui-meme) pour ecrire un compilateur
### Traitements:
Analyse:
	- #lexicale: former des motes a partir des caracteres du fichier source
	- #syntaxique: former des phrases a partir des mots ( #lexical ) en conformite avec la syntaxe du langage source
	- #semantique: verifier que les phrases respectent la semantique du langage source
Synthese:
	- generer le code cible
	- optimiser la production
Detection d'erreurs #lexicale, #syntaxique, #semantique 
### Representation intermediares
Structures:
	- Arbre syntaxique ou de derivation (arbre syntaxique simplifie)
	- Arbre abstrait: instructions
	- Table des symboles: declarations
### Methodes de conception
1. Calque sur le modele fonctionnel:
		- Subit une succession de traitements
2. Development iteratif
		- Traitement par implementation de fonctionnalites, toute la partie traitement est faite par fonctionnalites pour avoir un programme fonctionnel a chaque iteration
3. Chaines de compilation, par limitation de ressources a disposition, machine cible differente de la machine sur laquelle on developpe
		- Choisir le langage cible
		- Bootstrapper le compilateur
		- Optimiser perf compilateur
	Bootstrap: permet de resoudre probleme poule et oeuf vis a vis du point de depart (compilateur ou langage) en compilant la nouvelle version du compilateur avec l'ancienne

Zoot: source en Zoot -> compilateur Zoot -> cible en MIPS, no bootstrapping, compiler in Java
Compilateur en 4 passes:
	- Analyse lexicale et grammaticale:
		- Utiliser un analyseur lexical:
			- Defintion des expressions regulieres = unites lexicales (def d'automates)
			- Automate de reconnaissance des expressions regulieres et algo de parcours de cet automate
			- Utilisation de generateurs d'analyseurs lexicaux (Lex, JFlex, ANTLR ...)
		- Analyseur syntaxique:
			- Sur la base d'une grammaire
			- Analyse descendante (grammaire LL) ou ascendente (grammaire LR)
			- Utilisation de generateurs d'analyseurs syntaxiques: Yacc, Bison, JavaCupm ANTLR ...
			- Detection et gestion des erreurs
		- Verifier la conformite de la suite de mots par rapport a la grammaire du langage
		- Creer l'arbre abstrait des instructions
		- Memoriser les declarations dans la table des symboles
	- Analyse semantique:
		- Parcours l'arbre abstrait pour verifier les instructions
		- Utilise table des symboles pour retrouver les declarations
		- Decore l'arbre abstrait avec les informations necessaires pour la generation de code
	- Generation de code:
		- Parcours l'arbre abstrait decore
		- Application des modeles de traduction pour generer code cible
	- Optimisation de code

Generateur analyse lexical utilise: JFlex
Generateur analyse syntaxique ascendante utilise: JavaCup
Pas de gestion d'erreurs: la compilation s'arrete et produit un message d'erreur a la premiere erreur

Manque expression a type non terminal ArbreAbstrait sur diap JavaCup

### Automatisation de la construction du compilateur
Etapes de construction:
	1. Creation de l'analyseur syntaxique
	2. Creation de l'analyseur lexical
	3. Compilation de l'ensemble de classes

Utilisation de ant (another neat tool):
	- Automatisation de la construction de projets 
	- make de java

# 25/01/2023

Table des symboles:
	Informations dans la table:
		- Deplacement (addresse memoire) initial
		- Nom de chaque variable
		- Taille du bloc d'allocation en memoire
	Fonctions de TDS (singleton):
		- (Initialiser table
		- Calcul de la taille du bloc d'allocation en memoire)
		- Ajouter declaration de variable et lui donner un deplacement -> void ajouter(String idf)
			A chaque rencontre avec une nouvelle variable qui n'est pas deja presente dans la table, lors du parcours de l'analyseur syntaxique (classe ASynt)
		- Consulter la table -> int identifier(String idf)
			Lors de la construction de l'arbre semantique (classe variable)
			Si la variable n'est pas repertoriee dans la table: gestion d'erreur a faire
		- int getTailleZoneVariables()
			Dans la classe responsable de la generation du code afin de definir le deplacement maximal necessaire a prevoir
		- TDS()
	 Analyseur syntaxique va faire de la detection d'erreur semantique (double declaration de variables)
	 2 champs dans la classe et le singleton
	Ajout de booleens:
		- La taille de deplacement de variable est propre au type de variable rencontre
		- Verification -> identification du type et verification que la valeur attribuee correspond au type (bool = int en memoire)
		- ajouter fait correspondre l'identificateur au type -> ajouter(String idf, Symbole s)
		- Symbole identifier(String idf)
	void Verifier(){
		Symbole s = identifier(var);
		typeGauche.equals(typeDroit)
		typeGauche.concordeAvec(typeDroit)
	}


# 30/01/2023

## Controles semantiques
Contraintes:
	- verifiables par le compilateur
	- inverifiables par le compilateur -> verifies par du code genere par le compilateur

Typage statique:
	Association type a un identificateur de variable ou a un retour de fonction
		- Detecter erreur semantique avant execution
		- Eliminer information du code cible
		- Optimiser code cible

Verification:
	Utiliser declaration pour associer typage et variable et leur conformite
		Deux etapes:
			- Identification (retrouver la declaration associees a une variable)
				- Structure du programme
				- Presence de plusieurs espace des noms
			- Construction du type de l'expression

Inference (depuis langages fonctionnels):
	Compilateur retrouve le type de variables et fonctions a partir de leur usage
		- Utilise dans langages a typage statique

Langages a structures de blocs:
	Suite d'instruction clairement identifiee pour structurer un programme, possible d'attacher a des declarations a un block
		- Bloc sans nom
			- Aucun control specific
		- Fonctions, procedures

Espaces de noms:
	Identificateur peur signifier:
		- Un seul element
			- Negatif: Noms differents a tous les elements du code
			- Positif: Identification sur le nom uniquement
		- Plusieurs elements
			- Negatif: Identification sur le nom et l'espace de nom concerne
			- Positif: Nommage a la guise du programmeur (sur des blocs differents)

Table des symboles
	- Memoriser les informations des declarations
		- Variables: nom, type, deplacement en memoire, bloc de declaration
		- Fonction: profil, bloc de declaration
	- Association Symbole - Entree
	- Une entree par espace de nom