Le document a pour but de montrer la procédure a suivre pour lancer le jeu et y jouer.

Cette première SAE, la SAE1.01 Diamants, a pour but de nous faire réaliser un jeu sous forme graphique si possible. Notre binôme est composé de RODIER Matis et de NORAT Maaz, INF1-A

## Présentation et déroulement Jeu :

Nous nous sommes rendus au niveau 3 des attendues SAE, avec le bonus des IA rudimentaires. Cependant, nous n'avons pas pu ajouter d'images dans notre jeu car nous devions installer la librairie PIL chez nous pour pouvoir l'utiliser. Il nous était impossible de la télécharger pour x raison. Nous avons pour l'entièreté de notre programme, utilisé la libraire TKITEASY, que nous avons reçu en cours. C'est à dire, que nous n'avons pas utilisé les fonctions directement intégrées dans la bibliothèque TKINTER.

Pour lancer notre jeu, il suffit d'aller dans le fichier "main.py" et de lancer le programme. Il n'y a donc aucune librairie à installer. Une fois le jeu lancer, vous devriez pouvoir choisir le nombre de joueurs et d'IA que vous souhaitez intégrer à la partie. Une fois votre décision prise, il suffit d'appuyer sur lancer.

Durant la partie, le choix de rester dans la mine ou non est représenter par des cases rouges pour "non" et verte pour "oui". Tous les joueurs doivent donc faire leur choix. S'il y a des IA, les choix sont exécutés très rapidement, donc s'il n'y plus de joueur "normaux" dans la mine, il est normal que la manche actuelle se termine extrêmement vite. Une fois toute les IA rentrée au campement, l'affichage de fin de manche intervient, vous pourrez donc examiner les cartes tomber lors de cette phase passée très rapidement.

Les cartes trésors sont représentées en orange en graphique, les dangers, eux sont en marrons, les reliques pas encore prises sont en bleu ciel et les reliques prises sont en simplememt en bleu.

Pour finir, une fois les cinq manches terminées, l'affichage de fin de partie intervient, vous pourrez donc voir qui est/sont le/les gagnant(s).

Pour sortir du jeu, il suffit d'appuyer à n'importe quel endroit de la fenêtre.

## Problèmes rencontrés :

Nous n'avons pas réussi à intégrer des images, car la librairie PIL n'était pas utilisable de chez nous. Nous avons demandé l'aide d'autres groupes, sans réussite. Nous nous sommes alors concentrés sur une version sans images.

Lorsque nous avons essayé de relier le graphique, que l'on avait testé en amont, nous avons rencontré de léger problème que l'on a pu régler dans l'heure.

Un autre problème était de faire en sorte que la taille de toutes les cartes, case des scores des joueurs, s'adapte à la largeur, hauteur de la fenêtre. Nous avons cependant appliqué ce principe sur le déroulement du jeu global.

## Les bugs rencontrés : 

Lorsque l'on ferme le jeu avec la croix en haut a gauche, le jeu se ferme, cependant il y a une erreur, il faut donc aller au bout de la partie, et fermer la fenêtre proprement.

Si l'on change la taille de la largeur de de la hauteur, il peut y avoir quelques problèmes d'affichage.

## Idées :

Nous pensions perfectionner nos IA. Cependant nous n'avons pu qu'en réaliser des rudimentaires par manque de temps.

Nous voulions aussi ajouter des images, mais le problème de librairie nous a arrêté sur notre lancer.

Et bien sûr, développer encore notre interface graphique dans sa globalité.
