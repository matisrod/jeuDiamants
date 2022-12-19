from random import *
from jeuDiamantGraphique import *

####################
#lisibilité terminal
####################

def espaceTerminal(nbEspaces):
    '''
    saute simplement n lignes
    créer de l'espace => plus lisible
    '''
    for i in range(nbEspaces):
        print()





###############################
#affichage du score des manches
###############################

def afficheScorePartieTerminal(scorePartieJoueurs):
    '''
    affiche dans le terminal le score de la partie de chaque joueurs

    Params:
        scorePartieJoueurs (dict) : score de chaque joueur
    '''
    print("Score de la partie :")
    for joueur in scorePartieJoueurs:
        print("Joueur_" + str(joueur) + ": " + str(scorePartieJoueurs[joueur]), end="    ")


def afficheScoreMancheTerminal(scoreMancheJoueurs, numManche):
    '''
    affiche dans le terminal le score de la manche X de chaque joueurs

    Params:
        scoreMancheJoueurs (dict) : score de chaque joueur
    '''
    print("Score de la manche n°" + str(numManche) + " :")
    for joueur in scoreMancheJoueurs:
        print("Joueur_" + str(joueur) + ": " + str(scoreMancheJoueurs[joueur]), end="    ")


def afficheJoueurRestantMine(joueursDansMine):
    '''
    affiche dans le terminal les joueurs encore présents dans la mine

    Params:
        joueursDansMine(dict) : score de chaque joueur
    '''
    if len(joueursDansMine) > 0:
        print("Joueurs restants dans la mine :")
        for joueur in joueursDansMine:
            print("Joueur_" + str(joueur), end="    ")
    else:
        print("In n'y a pasplus de joueur dans la mine")


def afficheCarteSortiees(listeCartesSorties):
    '''
    affiche les cartes sorties dans la manche

    Params:
        listeCartesSorties (list) : liste des cartes sorties
    '''
    if listeCartesSorties == []:
        print("Pas encore de cartes tirées.")
    else:
        print("Liste des cartes tirées :")
        for carte in listeCartesSorties:
            print(carte, end=" ")


def afficheJeuTerminal(scorePartieJoueurs, scoreMancheJoueurs, joueursDansMine, listeCartesSorties, surplusRubis, numManche):
    '''
    affiche la partie actuelle dans le terminal : 
        le nombre de joueur qu'il reste dans la mine
        le nombre de rubis que chaque personne a, correspond au coffre final (en indiquant quel joueur)
        le nombre de rubis que chaque personne tant qu'ils ne sont pas sortis de la mine (en indiquant quel joueur)
        le type de carte deja sortie du paquet => utile pour les joueurs

    Params:
        scorePartieJoueurs (dict) : dico avec en clé le num du joueur et en valeur son nombre de rubis de la partie
        scoreMancheJoueurs (dict) : dico avec en clé le num du joueur et en valeur son nombre de rubis de la manche
        joueursDansMine (list) : liste des joueurs encore présent dans la mine
        joueursRestants (list) : liste de tous les joueurs restants dans la mine
        listeCartesSorties (list) : liste des cartes sorties du paquet
        surplusRubis (int) : le surplus de rubis pas distribué
        numManche (int) : quelle manche on est
    '''
    afficheScorePartieTerminal(scorePartieJoueurs)
    espaceTerminal(2)

    afficheScoreMancheTerminal(scoreMancheJoueurs, numManche)
    espaceTerminal(2)

    afficheJoueurRestantMine(joueursDansMine)
    espaceTerminal(2)

    afficheCarteSortiees(listeCartesSorties)
    espaceTerminal(2)

    print("Surplus de rubis :" + str(surplusRubis))
    espaceTerminal(1)


def test_afficheJeuTerminal():
    '''
    test de la fonction afficheJeuTerminal
    '''
    afficheJeuTerminal({0:1, 1:4, 2:8}, {0:1, 1:4, 2:8}, [0,1,2], [1,2,3,4,5], 2, 3)
    print("---------------------")
    afficheJeuTerminal({0:1, 1:4, 2:8}, {0:1, 1:4, 2:1}, [], [1,2,3,4,5,3,4,7,4,2], 0, 0)
    print("---------------------")
    afficheJeuTerminal({0:1, 1:4, 2:8}, {0:6, 1:2, 2:0}, [1], [], 1, 1)
    

#test_afficheJeuTerminal()




###############################################
#affichage finale de la partie dans le terminal
###############################################

def rechercheMeilleurJoueur(scorePartieJoueurs):
    '''
    renvoie une liste contenant une liste des joueurs gagnants et le score qu'ils ont effectué

    Params:
        scorePartieJoueurs
    Returns:
        listeMeilleurJoueurs (list) : liste des joueurs gagnants
        scoreMax (int) : score du/des joueur(s) ayant le plus grand nombre de rubis
    '''
    #liste des joueurs ayant le meilleur score
    listeMeilleurJoueurs = []
    #score max de base est initialisé en se référant au joueur 0
    scoreMax = scorePartieJoueurs[0]

    #on compare le score de tous les joueurs
    for joueur in scorePartieJoueurs:
        #si il est égal alors on le met execo  avec le joueurs ayany le max score
        if scorePartieJoueurs[joueur] == scoreMax:
            listeMeilleurJoueurs.append(joueur)

        #si son score est suppérieur alors on change le score max et on met dans la liste des joueurs ayant le meilleur score le joueur actuel
        elif scorePartieJoueurs[joueur] > scoreMax:
            scoreMax = scorePartieJoueurs[joueur]
            listeMeilleurJoueurs = [joueur]

    return listeMeilleurJoueurs, scoreMax


def plusieursGagnants(listeMeilleurJoueurs, scoreMax):
    '''
    affiche dans le terminale les numéro des joueurs ayant gagné la partie

    Params:
        listeMeilleurJoueurs (list) : liste conenant les meilleur joueurs de la partie
    Retuns:
        scoreMax (int) le score maximal que c'est joueur on réalisé
    '''
    print("Les gagnants sont les joueurs :", end=" ")
    for gagnants in range(len(listeMeilleurJoueurs)):
        if gagnants < len(listeMeilleurJoueurs) - 1:
            print(str(listeMeilleurJoueurs[gagnants] + 1), end=", ")
        else:
            print(str(listeMeilleurJoueurs[gagnants] + 1), end=" ")
        
    print(" avec un score de " + str(scoreMax))


def unSeulGagnant(listeMeilleurJoueurs, scoreMax):
    '''
    affichage pour une seul gagnant

    Params:
        listeMeilleurJoueurs (list) : liste conenant les meilleur joueurs de la partie
    Retuns:
        scoreMax (int) le score maximal que c'est joueur on réalisé
    '''
    print("Le gagnant est le joueur_" + str(listeMeilleurJoueurs[0] + 1) + " avec un score de " + str(scoreMax))


def affichageFinalTerminal(scorePartieJoueurs):
    '''
    affiche le score final en disant qui a gagné et tout

    Params:
        scorePartieJoueurs (dict) : dico contenant le score de la partie de tout les joueurs
    '''
    listeMeilleurJoueurs, scoreMax = rechercheMeilleurJoueur(scorePartieJoueurs)
    if len(listeMeilleurJoueurs) > 1:
        plusieursGagnants(listeMeilleurJoueurs, scoreMax)
    else:
        unSeulGagnant(listeMeilleurJoueurs, scoreMax)


def test_affichageFinalTerminal():
    '''
    fonction test de l áffichage finale dans la console
    '''
    affichageFinalTerminal({0:1, 1:4, 2:8})
    affichageFinalTerminal({0:1, 1:8, 2:8})
    affichageFinalTerminal({0:8, 1:8, 2:8})

#test_affichageFinalTerminal()





############################
#création du paquet de carte
############################

def insererDangers(paquet):
    '''
    ajoute les dangers dans le paquet

    Params (list) : le paquet de carte de la manche
    '''
    listeDanger = [danger for danger in range(-1, -6, -1) for danger2 in range(3)]
    for danger in listeDanger:
        #danger représentés par des nombres négatifs de -5 a -1
        paquet.append(danger)


def insererReliques(paquet, reliqueSortieJeu, numManche):
    '''
    on met les reliques dans le paquet de carte

    Params:
        paquet (list) : le paquet de carte de la manche
        reliqueSortieJeu (int) : nmbre de relique sortie du jeu
        numManche (int) : quelle manche on est
    '''
    if numManche > 5:
        numManche = 5

    listeRelique = [relique for relique in range(numManche - reliqueSortieJeu)]
    for relique in listeRelique:
        #relique représenté par le nombre 0
        paquet.append(0)


def suppDangerApparus(paquet, listeSuppDanger):
    '''
    supprime les danger deja apparu au cours de la partie

    Params:
        paquet (list) : le paquet de carte de la manche
        listeSuppDanger (list) : correspond a la liste des danger sortie qui sont deja sortie en double, il peut en avoir deux fois le meme
    '''
    for danger in listeSuppDanger:
        paquet.remove(danger)


def melangerPaquet(paquet, nbMelanges):
    '''
    melange le paquet n fois

    Params:
        paquet (list) : le paquet pour une n manche
        nbMelanges (int) : nombre correspondant au nombre de fois que l'on shouaite mélanger le paquet
    '''
    for x in range(nbMelanges):
        #comme ça on est sur que c'est bien mélanger :D
        shuffle(paquet)


def creationPaquet(listeSuppDanger, reliqueSortieJeu, numManche):
    '''
    cree un paquet de carte contenant 15 cartes tresors, 5 fois 3 types de dangers, et enfin 5 cartes reliques.
    puis le melange aleatoirement.
    carte trésors : nombre entier positif avec le nb de rubis directement (1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17)
    carte danger : nombre entier négatif de -1 a -5 car il y a 5 danger différents
    carte réplique : repréenté par le 0

    Params:
        listeSuppDanger (list) : correspond a la liste des danger sortie qui sont deja sortie en double, il peut en avoir deux fois le meme
        reliqueSortieJeu (int) : nmbre de relique sortie du jeu
        numManche (int) : quelle manche on est
    Returns:
        paquet (list) : paquet de carte melangé, contenant toutes les cartes
    '''
    # n met d'abord les trésors
    paquet = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]

    insererDangers(paquet)
    insererReliques(paquet, reliqueSortieJeu, numManche)
    suppDangerApparus(paquet, listeSuppDanger)
    melangerPaquet(paquet, 5) #on le mélange 5 fois comme ça on est plus sur :D
    return paquet



def test_creationPaquet():
    '''
    test de la fonction creationPaquet avec tous les cas de figure
    '''
    assert sorted(creationPaquet([], 0, 2)) == [-5, -5, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 0, 1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    assert sorted(creationPaquet([], 2, 3)) == [-5, -5, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    assert sorted(creationPaquet([-1], 2, 3)) == [-5, -5, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, -1, 0, 1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    assert sorted(creationPaquet([-1, -1], 2, 3)) == [-5, -5, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, 0, 1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    assert sorted(creationPaquet([-1, -1, -5], 2, 3)) == [-5, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, 0, 1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
    assert sorted(creationPaquet([-1, -1, -5], 2, 5)) == [-5, -5, -4, -4, -4, -3, -3, -3, -2, -2, -2, -1, 0, 0, 0, 1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]

test_creationPaquet()


#############################################
#choix des joueurs et ce qu'il se passe apres
#############################################

def choixJoueur(joueur):
    '''
    demande au joueur s'il veut continuer cette manche ou pas
    il repond par oui/non dans le shell
    si oui renvoie True
    False sinon

    Params:
        joueur (int) : correspond au joueur qui va choisir
    Returns:
        (bool) : True/False en fonction du choix
    '''
    choix = input("Joueur "+ str(joueur) +"! Voulez-vous restez dans la mine ? o/n : ")
    return choix == "o"


def interrogationJoueur(joueursDansMine, joueursPartant):
    '''
    modifie la liste des joueurs présents dans la mine, et ajoute ceux qui partent dans la liste de ceux qui partent de la mine 

    Params:
        joueursDansMine (list) : contient la liste des joueurs présents dans la mine
        joueursPartant (list) : liste des joueurs quittant le mine a une certaine partie de la manche
    '''
    for joueurQuijoue in joueursDansMine:
        if not choixJoueur(joueurQuijoue):
            #(retire de la liste des joueurs dans la mine) et (le met dans la liste des joueurs ayant quités la mine a ce moment)
            joueursPartant.append(joueurQuijoue)

    espaceTerminal(2)
    for joueur in joueursPartant:
        joueursDansMine.remove(joueur)


def executionChoixRobot(joueursDansMine, joueursPartant, NBROBOTS, NBJOUEURTOTO, choixAlea=70):
    '''
    regarde les choix des robots s'il y en a

    joueursDansMine (list) : liste contenant tous les joueurs dans la mine
    joueursPartant (list) : liste contenant tous les joueurs partant de la mine a un certain moment
    NBROBOTS (int) : nombre de robots dans la partie
    NBJOUEURTOTO (int) : nombre de joueurs au total (joueur + robot)
    choixAlea (int) : xhoix du robot compris entre 0 et 100, plus le choixAlea est élevé, plus le robot restera dans la mine
    '''
    #on créé une nouvelle liste, comme ca ya pas de prbl avec l'autre liste des joueurs partant
    joueursPartant2 = []
    if NBROBOTS > 0:
        for joueurQuiJoue in joueursDansMine:
            if joueurQuiJoue >= NBJOUEURTOTO - NBROBOTS:   
                #si le joueur est un robot, alors on l'interoge :
                if randint(0, 100) > choixAlea:
                    joueursPartant2.append(joueurQuiJoue)

        for joueur in joueursPartant2:
            joueursDansMine.remove(joueur)
            joueursPartant.append(joueur)


def unJoueurQuittantMine(joueursPartant, scoreMancheJoueurs, surplusRubis, listeValeursRelique, listeCartesTirees):
    '''
    applique ce qu'il doit se passer s'il n'y a qu'un joueur qui quitte la mine

    Params:
        joueursPartant (list) : liste des joueurs partant de la mine a un moment donné
        scoreMancheJoueurs (dict) : dico du score de chaque joueur au cours d'une certaine manche
        surplusRubis (int) : correspond au nb de rubis qui n'ont pas pu être distribués lors de la répartition
        listeValeursRelique (list) : liste des valeurs que prennent les reliques
        listeCartesTirees (list) : list des cartes tirees au cours de la manche
    Returns:
        0
    '''
    scoreMancheJoueurs[joueursPartant[0]] += surplusRubis
    joueurPrendRelique(joueursPartant, scoreMancheJoueurs, listeValeursRelique, listeCartesTirees)
    #surplus de rubis = 0 | car il a tout pris, il est tous seul a partir
    return 0


def plusieursJoueursQuittantMine(joueursPartant, scoreMancheJoueurs, surplusRubis):
    '''
    applique ce au'il doit se passer s'il y a pls joueurs qui partent de la mine

    Params:
        joueursPartant (list) : liste des joueurs partant de la mine a un moment donné
        scoreMancheJoueurs (dict) : dico du score de chaque joueur au cours d'une certaine manche
        surplusRubis (int) : correspond au nb de rubis qui n'ont pas pu être distribués lors de la répartition
    '''
    for joueurQuiPart in joueursPartant:
        scoreMancheJoueurs[joueurQuiPart] += surplusRubis // ( len(joueursPartant) )
    #renvoie les rubis qui n'ont pas pu être distribué
    return (surplusRubis % len(joueursPartant))


def scoreJoueurQuittantMine(joueursPartant, scoreMancheJoueurs, surplusRubis, listeValeursRelique, listeCartesTirees):
    '''
    change le score de la partie pour les joueurs qui partent de la mine => si ils partent pas dans tous les cas ils perdent leur rubis
    il prennent donc seulement les rubis en surplus

    Params:
        joueursPartant (list) : liste des joueurs partant de la mine a un moment donné
        scoreMancheJoueurs (dict) : dico du score de chaque joueur au cours d'une certaine manche
        surplusRubis (int) : correspond au nb de rubis qui n'ont pas pu être distribués lors de la répartition
    '''
    if len(joueursPartant) == 1:
        #il prend la carte replique si il y en a une, et prend tous les rubis en surplus (que l'on a pas pu distribuer)
        surplusRubis = unJoueurQuittantMine(joueursPartant, scoreMancheJoueurs, surplusRubis, listeValeursRelique, listeCartesTirees)

    elif len(joueursPartant) > 1:
        #si il y a une carte relique, alors elle est supprimée de la manche, puis se distribuent en part égal le nombre de rubis en surplus
        surplusRubis = plusieursJoueursQuittantMine(joueursPartant, scoreMancheJoueurs, surplusRubis)
    
    return surplusRubis






##############################################
#tirage de la carte et application de celle-ci
##############################################

def tirageCarte(paquet):
    '''
    tire la carte au dessus du paquet, on va partir du principe que le haut du paquet est le dernier élément de la liste du paquet

    Params:
        paquet (list) : est la liste du paquet de carte
    Returns:
        carteTiree (int) : le met directe dans le return (donc pas de création inutile de variable dans la fontion)
    '''
    if len(paquet) == 0:
        return None
    else:
        return paquet.pop()


def appliqueTypeTresor(carteTiree, scoreMancheJoueurs, joueursDansMine):
    '''
    ajoute la répartition des trésor dans le score des joueurs par manche si la carte est un trésor

    Params:
        carteTiree (int) : numéro de la carte tiree, si cést positif, c'est forcément un trésor, si 0 c'est une relique, si négatif alors danger.
        scoreMancheJoueurs (dict) : ex => {0:x, 1:y, 2:z}
        joueursDansMine (list) : liste des joueurs encore dans la mine
    Returns:
        si il y a des joueurs dans la mine on renvoie le surplus de rubis que l'on a pas pu distribuer
    '''
    if len(joueursDansMine) == 0:
        pass
    else:

        repartitionRubis = carteTiree // len(joueursDansMine)
        surplusRubis = carteTiree % len(joueursDansMine)

        for joueur in joueursDansMine:
            scoreMancheJoueurs[joueur] += repartitionRubis
        
        return surplusRubis


def deuxiemeDanger(carteTiree, listeCartesTirees, joueursDansMine, scoreMancheJoueurs, listeSuppDanger):
    '''
    regarde si dans le paquet de carte il y a deux fois la meme carte danger
    True si oui
    False sinon

    Params:
        carteTiree (int) : correspond a la derniere carte tiree
        listeCartesTirees (list) : toutes les cartes tirée durant la manche actuelle
        joueursDansMine (list) : liste des joueurs dans la mine
        scoreMancheJoueurs (dict) : dico des joueurs avec le nbr de rubis qu'ils ont chacun
        listeSuppDanger (list) : liste des cartes dangers ayant deja été tirée
    Returns:
        bool : True si il y a 
    '''
    #on remet a 0 le score des joueurs encore présents dans la mine
    if carteTiree in listeCartesTirees[:-1]:
        for joueur in joueursDansMine:
            scoreMancheJoueurs[joueur] = 0
        listeSuppDanger.append(carteTiree)
        return True
    return False


def test_deuxiemeDanger():
    assert deuxiemeDanger(-2, [1,2,3,4,5,6,-2], [0,1,2], {0:1, 1:4, 2:6}, []) == False
    assert deuxiemeDanger(-2, [1,2,-2,4,5,6,-2], [0,1,2], {0:1, 1:4, 2:6}, []) == True
    assert deuxiemeDanger(-2, [1,-2,3,4,5,6,-2], [0], {0:1, 1:4, 2:6}, []) == True
    assert deuxiemeDanger(-2, [1,2,3,4,5,6,-2,-2], [1], {0:1, 1:4, 2:3}, []) == True
    assert deuxiemeDanger(-1, [1,2,-2,4,5,6,-1], [0,1,2], {0:1, 1:4, 2:6}, []) == False
    assert deuxiemeDanger(-2, [1,2,3,4,5,6], [0,1,2], {0:1, 1:4, 2:6}, []) == False

#test_deuxiemeDanger()


def supprimeJoueursDansMine(joueursDansMine):
    '''
    supprime les joueurs encore présent dans la mine

    Params:
        joueursDansMine (list) : liste des joueurs dans la mine
    '''
    for joueur in range(len(joueursDansMine)):
        joueursDansMine.pop()


def appliqueTypeCarte(carteTiree, scoreMancheJoueurs, joueursDansMine, listeCartesTirees, listeSuppDanger):
    '''
    applique le cas de figure de la carte retournée
    on ne traite pas ici le cars de la relique

    Params:
        carteTiree (int) : indique quelle carte est tirée en fontion de son numéro
        scoreMancheJoueurs (dict) : dico des joueurs avec le nbr de rubis qu'ils ont chacun
        joueursDansMine (list) : liste des joueurs dans la mine
        listeCartesTirees (list) : liste de toutes les cartes tirées durant la manche
        listeSuppDanger (list) : liste des cartes dangers ayant deja été tirée
    Returns:
        surplusRubis (int) : les rubis n'ayant pas pu etre partagés entre les joueurs, ceux en trop
    '''
    surplusRubis = 0
    if len(joueursDansMine) != 0:
        if carteTiree > 0:
            #c'est un trésor on distribue donc tous les rubis au nombre de joueurs respectif + si pas assez => dans le surplus de rubis
            surplusRubis += appliqueTypeTresor(carteTiree, scoreMancheJoueurs, joueursDansMine)

        elif carteTiree < 0:
            #c'est une carte danger
            #on regarde si c'est le deuxieme meme danger, si oui manche terminée
            if deuxiemeDanger(carteTiree, listeCartesTirees, joueursDansMine, scoreMancheJoueurs, listeSuppDanger):
                supprimeJoueursDansMine(joueursDansMine)

    #on return le si c un danger ou une relique puisque ya pas de rubis nen plus dans le jeu
    return surplusRubis






##############################
#création score + augmentation score partie
##############################

def scoreJoueurs(NBJOUEUR, NBROBOTS):
    '''
    créer un dictionnaire avec le nombre de joueur correspondant dans les clés et en initialisant chaque valeur a 0, soit le nb de rubis

    Params:
        NBJOUEURS (int) : donne le nombre de joueur qu'il y a dans la partie
        NBROBOTS (int) : nombre de robots dans la partie
    Returns:
        score (dict) : dico renvoyer, contenant le score mis a 0 pour tous les joueurs
    '''
    score = {}
    for joueur in range(NBJOUEUR + NBROBOTS):
        score[joueur] = 0

    return score


def changerScorePartie(scorePartieJoueurs, scoreMancheJoueurs):
    '''
    augmente le score de la partie en fonction du score de la manche qui vient de finir

    Params:
        scorePartieJoueurs (dict) : ajoute le nb de rubis dans les clés de chaque joueurs en fontion des clés de l'autre dico
        scoreMancheJoueurs (dict) : nbr de rubis dans les valeurs du dico de la manche pour chaque joueurs
    '''
    for joueur in scoreMancheJoueurs:
        scorePartieJoueurs[joueur] += scoreMancheJoueurs[joueur]






#################################
#fin de la manche et de la partie
#################################

def finPartie(numManche, NBMANCHES):
    '''
    regarde si le nombre de manche restante est egal a 0, si oui arrete la partie, si non continue

    Params:
        numManche (int) : numéro de la manche actuelle
        NBMANCHES (int) : le nombre de manche max de la partie
    Returns:
        finPartie (bool) : True ou False dependant du nb de manches
    '''
    return numManche == NBMANCHES


def finManche(joueursDansMine, scoreMancheJoueurs, scorePartieJoueurs):
    '''
    si plus personne dans la liste des joueurs restant dans la manche alors ça l'arrete
    créer un affichage qui montre que c'est la fin de la manche


    Params:
        joueursDansMine (list) : joueurs encore dans la mine
        scoreMancheJoueurs (dict) : dico contenant le score de tous les joueurs de la manche
        scorePartieJoueurs (dict) : dico contenant le score de tous les joueurs de la partie
    Returns:
        (bool) : True/False => vrai aucun des aucun des joueurs n'est dans la liste
    '''
    if joueursDansMine == []:
        #des que la manche est finie, on met le score de chaque joueur dans leur score Partie
        for joueur in scoreMancheJoueurs:
            scorePartieJoueurs[joueur] += scoreMancheJoueurs[joueur]
        return True
    else:
        return False


def test_finManche():
    '''
    test de la fonction finManche()
    '''
    assert finManche([0,1,2], {0:8, 1:8, 2:8}, {0:8, 1:8, 2:8}) == False
    assert finManche([0], {0:8, 1:8, 2:8}, {0:8, 1:8, 2:8}) == False
    assert finManche([], {0:8, 1:8, 2:8}, {0:8, 1:8, 2:8}) == True
    assert finManche([], {0:8, 1:8, 2:2}, {0:1, 1:3, 2:8}) == True

#test_finManche()






#########################################
#suppression des reliques déja retournées + nb relique dans paquet
#########################################

def donneIdRelique(listeCartesTirees):
    '''
    donne l'id de l'indice des reliques dans les cartes tirés

    Params:
        listeCartesTirees (list) : listes des cartes tirées dans la manche
    Returns:
        listeIndiceRelique (list) : liste des indice des relique dans le paquet
    '''
    listeIndiceRelique = []

    for iCarte in range(len(listeCartesTirees)):
        if listeCartesTirees[iCarte] == 0:
            listeIndiceRelique.append(iCarte)
    return listeIndiceRelique


def joueurPrendRelique(joueursPartant, scoreMancheJoueurs, listeValeursRelique, listeCartesTirees):
    '''
    le seul joueur qui quitte le mine prend la ou les reliques si il y en a

    joueursPartant (list) : liste des joueurs partis a un certain moment de la manche => si on arrive ici, c'est qu'il y a qu'une personne dans la liste
    scoreMancheJoueurs (dict) : score de la manche de chaque joueur
    listeValeursRelique (list) : liste des valeurs de des reliques [10,10,5,5,5] au fur et a mesure
    listeCartesTirees (list) : liste des cartes tirées dans la manche
    '''
    listeIndiceRelique = donneIdRelique(listeCartesTirees)
    for iRelique in range(len(listeIndiceRelique)):
        scoreMancheJoueurs[joueursPartant[0]] += listeValeursRelique.pop()
        listeCartesTirees[listeIndiceRelique[iRelique]] = "#0"


def nbrReliquePaquet(paquet):
    '''
    donne le nombre de relique dans le paquet de carte

    Params:
        paquet (list) : liste du paquet de carte
    Returns:
        nbrelique (int) : nombre de relique dans le paquet de carte de la manche
    '''
    nbRelique = 0
    for carte in paquet:
        if carte == 0 or carte == "#0":
            nbRelique += 1

    return nbRelique

def test_nbrReliquePaquet():
    '''
    test la fonction nbrReliquePaquet()
    '''
    assert nbrReliquePaquet([1,4,3,5,2,6]) == 0
    assert nbrReliquePaquet([1,4,3,0,2,6]) == 1
    assert nbrReliquePaquet([0,4,3,5,2,0]) == 2
    assert nbrReliquePaquet([1,4,3,5,"#0",6]) == 1
    assert nbrReliquePaquet([1,"#0",3,5,0,6]) == 2
    assert nbrReliquePaquet([1,4,3,"#0","#0",6]) == 2
    assert nbrReliquePaquet([1,4,3,"#0","#0",6,6,0,6]) == 3

#test_nbrReliquePaquet()


#############################
#déroulement principal du jeu
#############################
def lancementJeu(g, NBJOUEURS, NBROBOTS):
    '''
    lancement du jeu dans sa globalité
    mis sous forme de fonction pour que l'on est au final qu'un autre tout petit fichier pour lancer le jeu "main.py", au lieu d'aller sur le code entier

    Params:
        NBJOUEURS (int) : nombre de joueurs dans la partie
        NBROBOTS (int) : nombre de robots dans la partie
    '''
    #parametre de l'avant jeu
    #peut etre modifier a chaque debut de partie
    NBMANCHES = 5

    #pour ce qui est graphique la largeur des cartes posées sur le plateau
    largeurCarte=L//15.3
    hauteurCarte=H//5
    ecartCarte=L//200

    #demarage du jeu, preparation du tableau des scores des joueurs, soit leurs trésors => le nbr de rubis
    scorePartieJoueurs = scoreJoueurs(NBJOUEURS, NBROBOTS)
    numManche = 0
    #intégration d'une liste correspondant au carte danger à retirer du paquet après sa création
    listeSuppDanger = []
    listeValeursRelique = [10, 10, 5, 5, 5]
    reliqueSortieJeu = 0
    
    while not finPartie(numManche, NBMANCHES):
        #on dit directement que le nombre de manche diminue
        numManche += 1
        #préparation au debut de la Xeme manche
        #===>

        #créer un nouveau paquet a chaque debut de manche
        #on supprime du paquet de carte les dangers déja apparus dans la partie
        paquetCarte = creationPaquet(listeSuppDanger, reliqueSortieJeu, numManche)
        #réinitialisation de la variable contenant tous les joueurs de la partie dans la mine
        joueursDansMine = list(range(NBJOUEURS + NBROBOTS))
        #reinitialisation des cartes tirées => aucune pour le moment
        listeCartesTirees = []
        #reinitialisation du score de la manche de chaque joueur
        scoreMancheJoueurs = scoreJoueurs(NBJOUEURS, NBROBOTS)
        #préparation des rubis sorties de la mine et des surplus(les non distribués)
        surplusRubis = 0
        
        #<===
        #fin préparation de la Xeme manche
        
        #début de la manche X ===>
        while not finManche(joueursDansMine, scoreMancheJoueurs, scorePartieJoueurs):
            #la hauteur case sera la hauteur d'une carte du jeu, on calcul donc seulement la largeur et l'écart entre les cases
            largeurCase, ecartCase = repartitionCaseEnFonctionDeNombreJoueur(scorePartieJoueurs)

            #affiche le déroulé de la partie dans le terminale
            afficheLaPartie(g, listeCartesTirees, surplusRubis, scorePartieJoueurs, scoreMancheJoueurs, numManche, joueursDansMine, largeurCarte, hauteurCarte, ecartCarte, NBJOUEURS, NBROBOTS, largeurCase, ecartCase, couleurArrierePlan = "beige", couleurCarte = "brown", couleurCase = "white", couleurEcriture = "black")
            #liste de joueur partant de la mine => sera vide a chaque fois qu'on réinterroge les joueurs pour savoir s'il veulent partir ou pas => bonne distribution des diamands
            joueursPartant = []

            #on interroge tous les joueurs
            afficheDemandeJoueur(g, scorePartieJoueurs, joueursDansMine, ecartCase, largeurCase, hauteurCarte, NBROBOTS, (NBROBOTS+NBJOUEURS))
            executeDemandeJoueur(g, scorePartieJoueurs, joueursDansMine, ecartCase, largeurCase, hauteurCarte, joueursPartant, NBROBOTS, (NBROBOTS+NBJOUEURS))
            executionChoixRobot(joueursDansMine, joueursPartant, NBROBOTS, (NBROBOTS+NBJOUEURS))

            #distribution des rubis restant pour les joueurs qui partent de l'exploration de la X manche
            surplusRubis = scoreJoueurQuittantMine(joueursPartant, scoreMancheJoueurs, surplusRubis, listeValeursRelique, listeCartesTirees)

            #tire une carte
            listeCartesTirees.append(tirageCarte(paquetCarte))
            carteTiree = listeCartesTirees[-1]

            #applique le type de la carte retournée, cad si c'est un trésor, un danger ou une relique, et on met a jour le surplus de rubis
            surplusRubis += appliqueTypeCarte(carteTiree, scoreMancheJoueurs, joueursDansMine, listeCartesTirees, listeSuppDanger)
        
        #affiche la partie, comme ca on voit quand meme quelle carte est/serai tombée en dernier
        afficheLaPartie(g, listeCartesTirees, surplusRubis, scorePartieJoueurs, scoreMancheJoueurs, numManche, joueursDansMine, largeurCarte, hauteurCarte, ecartCarte, NBJOUEURS, NBROBOTS, largeurCase, ecartCase, couleurArrierePlan = "beige", couleurCarte = "brown", couleurCase = "white", couleurEcriture = "black")
        #transition vers la manche suivante, ou si derniere manche vers l'écran de fin
        transition(g, numManche, NBMANCHES)

        #pour savoir si le nombre qu'il y a dans les cartes tirées
        reliqueSortieJeu += nbrReliquePaquet(listeCartesTirees[:-1])
    
    #affichage de fin de partie
    listeMeilleurJoueurs, scoreMax = rechercheMeilleurJoueur(scorePartieJoueurs)

    #on regarde si les joeurs veulent rejouer
    affichageFinPartie(g, listeMeilleurJoueurs, scoreMax, NBROBOTS, (NBROBOTS+NBJOUEURS))
