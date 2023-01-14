
# 9/01/2023

## Intro

td rendus et notes
justifier absence aux td
final sur machine

rlang



Partie 1:

Data mining: Extraction de connaissances interessantes (règles, régularites, patterns, contraintes) à partir de donnees.

Connaissance: Suggestions de vidéos en lien avec la vidéo regardée (sur exemple de Youtube)

2005: changement de la dimension de traitement

Analyse (science) de donnees:
	- Ensemble de tech et methodes pour l'exploration de donnees
	- Extraction d'informations et des connaissances

Autres appelations:
		- Knowledge Discovery from Database

Applications:
	- Analyse de marché, de risques, detection de fraudes
	- Text Mining
	- Optimization de requetes

Processus d'extraction:
	- Entrepot de donnees
	- Extraction des donnees cibles
	- Preparation des donnees: mise en forme, regarder valeurs manquantes et comment les traiter (1)
	- Data mining / science: algorithmes
	- Presentation des donnees a experts pour analyse

Etapes:
	- Comprehension domaine
	- Creation de l'ensemble de donnees
	- Traitement des  donnnees brutes (1)
	- Choix des modeles d'analyse (classification, consolidation, regression, association, clustering)
	- Choix de l'algo d'extraction
	- Evaluation de modeles (visualisation, transformation, suppression de patterns redondants ...)
	- Utilisation de connaissance extraite

Methodologies:
	1. Identifier le probleme
	2. Preparer les donnees
	3. Explorer modeles
	4. Utiliser modele
	5. Suivre modele

Validation modele:
	Matrice de confusion

Techniques:
	1. Descriptives - Famille Geometrique - = recherche de patterns
		1. Analyse factorielle
		2. Classification automatique (typologie, segmentation, clustering, apprentissage non supervise)
		3. Recherche d'associations
	2. Predictives - Famille Modeles a bases de regles logiques OU Modeles a bases de fonctions mathematiques - = modelisation
		1. Classement/discrimination (cible qualitative)
			1. Analyse discriminante
			2. Arbre de decision
			3. Reseau de neurones
		2. Prediction
			1. Regression lineaire
			2. Arbre de decision
			3. Reseau de neurones

Programme:
	Stats
	Regression Lineaire
	Analyse en Composante Principale
	Analyse Factorielle des Correspondantes
	Analyse factorielle discriminante
	Classification
	Regression logistique

## Rlang

rstudio

objet = vecteur


# 11/01/2023

## Rappel des Statistiques

### [[Statistique descriptive]]
	Vocab:
		1. Population
		2. Individu
		3. Variable/feature
			- qualitative
				- discrete
				- continues
			- quantitative
		 frequence = ni/n
		4. Modalite
		5. Echantillon
	Pour etudier un caractere X avec des valeurs d'un ensemble sur une population P
	Mediane: **def**
	Quantile (empirique): **def**
#### Formules
Moyenne (empirique): **formula**
Variance (empirique): **formula**
Ecart type (empirique): **formula**
Frequence cumuleee (somme de toutes les frequences): **formula**
Repartition empirique: **formula**
Covariance(empirique): **formula**, **proprietes**, plus grande est la valeur, plus les deux proprietes sont lies
Correlation lineaire: **formula**

Correlation != causalite


	
### [[Statistical Inference]]

## Probabilite

### Definitions
Variables aleatoires
	1. discrete
	2. continues

### Loi d'une variable aleatoire discrete

### Densite et fonction de repartition d'une variable continue

### Formules
Probabilite conditionnelle: **formula**
Theoreme de Bayes: **formula**
Esperence discrete: **formula**
Esperence continue: **formula**
Variance: **formula**
Ecart type: **formula**

#### Proprietes Esperence

#### Proprietes Variance

### Variable centree reduite
Formule: **formula**

### Lois
- Loi normale
- Loi exponentielle
- loi de Ki sq
- loi de Student

### Estimation parametrique
1. Estimation ponctuelle
2. Estimation par intervalle de confiance

#### Tests statistiques





diap 9/10:  (1)comment le choix des classes est-il fait, (2)comment sont determinees les intervalles? 
(1): doit representer le domaine etudie
(2): emplitude de l'echantillon
diap 55: important -> Souvent, cette hypothèse est le contraire ce que l’on cherche à prouver (raisonnement par l’absurde)
diap 60: overlap entre les deux courbes = zone de confusion

