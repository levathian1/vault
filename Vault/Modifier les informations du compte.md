  
Résume: ce cas permet à un utilisateur inscrit de modifier certaines informations de son compte.
Date de création: 15/01/2023
Acteurs concernes: les utilisateurs de l'application
Responsables: Nacera Elarbi Tolehi

Scénario normal:
1. L'utilisateur se rend sur la page de modifications d'informations du compte.
2. Par le biais de champs de texte, l'utilisateur peut saisir des changements sur certaines informations de son compte.
	2.1. L'utilisateur saisit un nouveau mot de passe.
	2.2 L'utilisateur met à jour une information quant à sa possession de voiture
	2.3 L'utilisateur met à jour son numéro de téléphone
	2.4 L'utilisateur met à jour sa photo de profil
3. L'utilisateur clique sur le bouton "valider les changements
4. AmisGo effectue des vérifications quant à la validité des nouvelles informations saisies.
5. AmisGo prompte l'utilisateur à saisir son (ancien dans le cas 2.1) mot de passe afin d'enregistrer les changements
6. AmisGo enregistre les informations.
7. La page de modification est alors rafraichie et l'utilisateur peut maintenant voir la page avec les nouvelles informations.
8. L'utilisateur est prevenu des changements par mail

Précondition:
L'utilisateur est connecté à un compte valide sur l'application

Scénario alternatif

4a. Informations saisies incorrectes
1. AmisGo indique a l'utilisateur les champs erronés et invite l'utilisateur à rectifier les champs en ré-indiquant les procedures de saisies correctes
2. Le scénario reprend à partir du point 3.

5a. Mot de passe incorrect
1. AmisGo indique a l'utilisateur que le mot de passe saisit est erroné et invite l'utilisateur a retenter la saisie.
2. Le scénario reprend à partir du point 5.

6a. Informations non sauvegardées
1. AmisGo indique a l'utilisateur qu'une erreur est survenue lors de l'enregistrement des informations saisies et l'invite à retenter plus tard.
2. Le scénario reprend à partir du point 1.

Contraintes:
	Disponibilite: La page et la possibilite d'enregistrer des modifications doit etre disponible 24h/24
	Temps de reponse: gotta go fast
	Integrite: no break, break = bad
	Confidentialite: Auth always work, unless servers go kaboom