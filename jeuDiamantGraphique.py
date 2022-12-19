from tkiteasy import *
import time

#de base a 1200
L = 1200
#de base 800
H = 800
#de base a 20 pour une largeur de 1200 et une hauteur de 800
TAILLEPOLICE = (L*H) // 48000


#######################################
#FENETRE DE LANCEMENT DU JEU
#######################################

def lancerFenetreJeu(L, H):
    '''
    création de la fenetre de lancement
    '''
    g = ouvrirFenetre(L, H)
    g.dessinerRectangle(0, 0, L, H, "beige")
    return g





######################
#Acceuil du jeu
######################

def afficheBienvenue(g, col="black"):
    '''
    affiche simplement Diamant
    '''
    g.afficherTexte("Diamant", L//2, H//5, col, 3*TAILLEPOLICE)


def afficheSelecNbJoueur(g, col="black"):
    '''
    affiche le fait de select le nombre de joueur
    '''
    g.afficherTexte("Selectionnez le nombre \n          de joueurs", L//4, H//2.5, col, TAILLEPOLICE)


def afficheSelecNbRobots(g, col="black"):
    '''
    affiche le fait de select le nombre de robot dans le jeu
    '''
    g.afficherTexte("Selectionnez le nombre \n          de robots", L//1.3, H//2.5, col, TAILLEPOLICE)


def affichageDesLignesNombres(g, nbC, nbL, coordX, coordY, col="black", lCase = L // 12, hCase = H // 10):
    '''
    affiche les nombres a sélectionner.
    ex :
        3   4   5
        6   7   8
    aux coordonnées corespondante, pour les joueurs et les robots

    Params:
        nbC (int) : nombre de colonne
        nbL (int) : nombre de ligne
        coordX (int) : coord en haut a gauche du tableau de ligne et colonne en x
        coordY (int) : coord en haut a gauche du tableau de ligne et colonne en y
    Returns:
        coordList (list de list) : liste des coord en haut a gauche poru les choix de joueurs : 1,2,3 et 4, pour trouver les autres il faudra simplement augmenter coordList[x][1] + hauteurCarte
    '''
    coordList = []
    for x in range(nbC):
        g.dessinerLigne(coordX + lCase * x, coordY, coordX + lCase * x, coordY + hCase * (nbL-1), col)
        coordList.append([int(coordX + lCase * x), int(coordY)])
    for y in range(nbL):
        g.dessinerLigne(coordX, coordY + hCase * y, coordX + lCase * (nbC-1), coordY + hCase * y, col)
    
    return coordList


def affichageSelecNombre(g):
    '''
    affiche toutes les sélections des nombres possibles de joueurs ou de robots

    Returns:
        coordListX_J (list de list), coordListX_R (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut)
    '''
    coordXJ = L//13
    coordYJ = H//2
    #on affiche les lignes pour choisir le nombre de joueurs que l'on souhaite
    coordListX_J = affichageDesLignesNombres(g, 5, 3, coordXJ, coordYJ)
    coordXR = L//1.65
    coordYR = H//2
    #on affiche les pour choisir le nombre de robots que l'on souhaite
    coordListX_R = affichageDesLignesNombres(g, 5, 3, coordXR, coordYR)
    return coordListX_J, coordListX_R


def affichageNumero(g, coordListX_R, lCase = L // 12, hCase = H // 10, col="black"):
    '''
    affiche simplement les numéros 1,2,3,4,5,6,7,8 pour les joueurs et les robots
    Params:
        coordListX_R (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut)
    '''
    for iJoueur in range(len(coordListX_R) - 1):
         g.afficherTexte(str(iJoueur + 1), coordListX_R[iJoueur][0] + lCase//2, coordListX_R[iJoueur][1] + hCase//2, col, TAILLEPOLICE)
         if iJoueur == len(coordListX_R) - 3:
            for iJoueur in range(len(coordListX_R) - 1):
                g.afficherTexte(str(iJoueur + 5), coordListX_R[iJoueur][0] + lCase//2, coordListX_R[iJoueur][1] + hCase + lCase//2, col, TAILLEPOLICE)


def affichageNumJ_et_R(g, coordListX_J, coordListX_R):
    '''
    affiche des num des joueurs et robots

    Params:
        coordListX_J (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les joueurs
        coordListX_R (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les robots
    '''
    affichageNumero(g, coordListX_J)
    affichageNumero(g, coordListX_R)


def affichageBoutonStart(g):
    '''
    affiche le boutton start
    '''
    g.dessinerCercle(L//2, H//1.2, 50, "black")
    g.afficherTexte("START", L//2, H//1.2, "red", TAILLEPOLICE)




#######################
#execute clique
#######################

def rechercheSurColonne(c, coordListX_J):
    '''
    recherche du chiffre sur colonne chez les robots

    Params:
        coordListX_J (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les joueurs
    '''
    if c.x < coordListX_J[1][0]:
        iVal = 0
    elif c.x < coordListX_J[2][0]:
        iVal = 1
    elif c.x < coordListX_J[3][0]:
        iVal = 2
    else:
        iVal = 3
    return iVal


def rechercheSurLigne(c, coordListX_J, hCase):
    '''
    recherhce du chiffre par ligne

    Params:
        coordListX_R (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les robots
        hCase (int) : hauteur d'une case de sélection du nombre (1,2,3,4,5,6,7 ou 8)
    '''
    if c.y < (coordListX_J[0][1] + hCase):
        return 0
    else:
        #si le clique est en bas alors on augmente iVal de 3 pour pouvoir atteindre les chiffres du bas du tableau
        return 4


def analyseClique(c, coordListX_J, hCase):
    '''
    regarde quel est le num de joueur que l'on a cliqué

    Params:
        coordListX_J (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les joueurs
        hCase (int) : hauteur d'une case de sélection du nombre (1,2,3,4,5,6,7 ou 8)
    '''
    diffVal = [1,2,3,4,5,6,7,8]
    iVal = rechercheSurColonne(c, coordListX_J)
    iVal += rechercheSurLigne(c, coordListX_J, hCase)
    return diffVal[iVal]


def affichePrblNbrJ_et_R(g, col="black"):
    '''
    affiche simplement qu'il y a un prbl de nombre de joueurs sélectionner
    '''
    g.afficherTexte("Veuillez sélectionner un nombre de joueurs \n         compris entre 3 et 8 inclus", L//2, H//1.05, col, TAILLEPOLICE//2)


def effacePrblNbrJ_et_R(g, fond="beige"):
    '''
    efface le mesage releveant le probleme de nombre de joueurs
    '''
    g.dessinerRectangle(L//2.55, H//1.1, L//4.6, H//14, "beige")


def cDansStart(g, c, nJoueur, nRobot):
    '''
    return True si on appuie environ sur le bouton start

    Params:
        c : clique du joueur
        nJoueur (int) : nombre de joueur
        nRobot (int) : nombre de robot
    Returns:
        bool : True si c entre 3 et 8 et False sinon
    '''
    if c.x > L//2.16 and c.y > H//1.27 and c.x < (L//2.16 + L//13) and c.y < (H//1.27 + H//10):
        if nbMinMaxJoueur(nJoueur, nRobot):
            return True
        else:
            affichePrblNbrJ_et_R(g)
    return False


def analyseJ_et_R(g, c, coordListX_J, coordListX_R, hCase, numJ, numR):
    '''
    execute le clique en parametre

    Params:
        coordListX_J (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les joueurs
        coordListX_R (list de list) : les coord représentant le haut gauche du carré ou le joueur a cliqué (seulement les coord des carrés en haut) pour les robots
        hCase (int) : hauteur d'une case de sélection du nombre (1,2,3,4,5,6,7 ou 8)
        numJ (int) : nombre de joueur
        numR (int) : nombre de robot
    Returns:
        numJ (int), numR (int) : le nombre de joueur ou de robot choisi
    '''
    #clique dans la partie des joueurs
    cInJoueur = c.x > coordListX_J[0][0] and c.y > coordListX_J[0][1] and  c.x < coordListX_J[-1][0] and c.y < (coordListX_J[-1][1] + 2 * hCase)

    #clique dans la partie des robots
    cInRobot = c.x > coordListX_R[0][0] and c.y > coordListX_R[0][1] and  c.x < coordListX_R[-1][0] and c.y < (coordListX_R[-1][1] + 2*hCase)

    #L//2.3, H//1.7, L//7, H//9
    cInReinitialiser = c.x > L//2.3 and c.y > H//1.7 and c.x < L//2.3 + L//7 and c.y < H//1.7 + H//13

    if cInJoueur:
        numJ = analyseClique(c, coordListX_J, hCase)
        effacePrblNbrJ_et_R(g)
    elif cInRobot:
        numR = analyseClique(c, coordListX_R, hCase)
        effacePrblNbrJ_et_R(g)
    elif cInReinitialiser:
        #si on appuie sur reinitialisé, alors on met 0 et 0 au nombre de joueurs et de robots
        numJ, numR = 0, 0

    return numJ, numR
    

def nbMinMaxJoueur(joueur, robot):
    '''
    renvoie true si joueur + robot <= 8
    '''
    return (joueur+robot) > 2 and (joueur+robot) < 9


def afficheNombreChoisi(g, numJ, numR, nC, col="black", fond="beige"):
    '''
    affiche le nombre de joueurs et de robots choisis

    Params:
        numJ (int) : nombre de joueurs
        numR (int) : nombre de robots
        nC (int) : nombre de clique
    '''
    if nC > 0:
        g.dessinerRectangle(L//5.5, H//1.35, L//7, H//15, fond)
        g.dessinerRectangle(L//1.4, H//1.35, L//8, H//15, fond)

    g.afficherTexte("Joueurs : " + str(numJ), L//4, H//1.3, col, TAILLEPOLICE)
    g.afficherTexte("Robots: " + str(numR), L//1.3, H//1.3, col, TAILLEPOLICE)


def tracerBouton(g, hautGauche, hautDroit, basGauche, basDroit, col="black"):
    '''
    tracage du bouton

    Params:
        correspond a tous les encroit du tracage du carré (fait avec des lignes) pour le bouton
        hautGauche (int)
        hautDroit (int)
        basGauche (int)
        basDroit (int)
    '''
    g.dessinerLigne(hautDroit[0], hautDroit[1], hautGauche[0], hautGauche[1], col)
    g.dessinerLigne(hautGauche[0], hautGauche[1], basGauche[0], basGauche[1], col)
    g.dessinerLigne(basGauche[0], basGauche[1], basDroit[0], basDroit[1], col)
    g.dessinerLigne(basDroit[0], basDroit[1], hautDroit[0], hautDroit[1], col)
    g.afficherTexte("Réinitialiser", L//1.985, H//1.6, col, TAILLEPOLICE)


def afficheReinitialiserNumJ_R(g):
    '''
    fait un bouton réinitialiser du nombre de joueurs a 0 et 0 pour les joueurs et robots
    '''
    
    hautGauche = L//2.3, H//1.7
    hautDroit = L//2.3 + L//7, H//1.7
    basGauche = L//2.3, H//1.7 + H//13
    basDroit = L//2.3 + L//7, H//1.7 + H//13
    tracerBouton(g, hautGauche, hautDroit, basGauche, basDroit)


def touteTypeEcrtiture(g):
    afficheBienvenue(g)
    afficheSelecNbJoueur(g)
    afficheSelecNbRobots(g)
    afficheReinitialiserNumJ_R(g)
    affichageBoutonStart(g)


def ouvrirAcceuil(g, couleurfond="beige"):
    '''
    tous l'affichage du programme de l'acceuil
    '''

    #fond
    g.dessinerRectangle(0, 0, L, H, couleurfond)
    lCase, hCase = L // 12, H // 10 

    #ecrit tous ce qui faut dans la fenetre d'acceuil
    touteTypeEcrtiture(g)

    #numéro
    coordListX_J, coordListX_R = affichageSelecNombre(g)
    affichageNumJ_et_R(g, coordListX_J, coordListX_R)
    

    #lesCliques
    nJoueur, nRobot = 0, 0
    lancer = False
    nC = 0
    while not lancer:
        afficheNombreChoisi(g, nJoueur, nRobot, nC, col="black", fond="beige")
        c = g.attendreClic()
        nJoueur, nRobot = analyseJ_et_R(g, c, coordListX_J, coordListX_R, hCase, nJoueur, nRobot)
        nC += 1
            
        lancer = cDansStart(g, c, nJoueur, nRobot)

    return nJoueur, nRobot

'''
#TEST SUR L'ACCUEIL DU JEU
#Lancer les deux lignes de codes si dessous pour lancer l'accueil seulement

g = ouvrirFenetre(L, H)
ouvrirAcceuil(g)
'''





##############################################
#affiche la carte qui vient juste d'être tirée
##############################################

def afficheCarteTiree(g, lesCartesTirees, couleuCarte, largeurCarte, hauteurCarte):
    '''
    affiche la carte tirée a gauche des cartes tirées dans la partie de la manche
    correspond a la toute derniere carte tirée

    Params:
        lesCartesTirees (int) : derniere carte tirée
        couleuCarte (str) : couleur de la carte que l'on va posée
        largeurCarte (int) : largeur de la carte
        hauteurCarte (int) : hauteur de la carte
    '''
    coordX = L//100
    coordY = (H*120)//800
    if len(lesCartesTirees) == 0:
        g.afficherTexte("Pas encore de \n   carte tirée", (L*50)//1200, (H*90)//800, "black", TAILLEPOLICE//2)
    else:
        g.afficherTexte("Deniere carte \n     tirée :", (L*50)//1200, (H*90)//800,"black", int(TAILLEPOLICE // 1.7))
        print(lesCartesTirees[-1])
        afficheLaCarte(g, -1, coordX, coordY, largeurCarte, hauteurCarte, lesCartesTirees, couleurEcriture="black")
        #g.dessinerRectangle(coordX, coordY, largeurCarte, hauteurCarte, couleuCarte)
        #g.afficherTexte(lesCartesTirees[-1], coordX + largeurCarte//2, coordY + hauteurCarte//2, "black", int(TAILLEPOLICE*2))






######################################
#affiche toutes les cartes tirées
######################################


def afficheLaCarte(g, carte, coordX, coordY, largeurCarte, hauteurCarte, lesCartesTirees, couleurEcriture="black"):
    '''
    affiche la carte tirée passées en argument, dans la liste des cartes

    Params:
        carte (int) : id de la carte dans les cartes tirées
        coordX (int) : coord de la carte en haut a gauche pour les x
        coordY (int) :  coord de la carte en haut a gauche pour les y
        largeurCarte (int)
        hauteurCarte (int)
        couleuCarte (int) : couleur de la carte 
        lesCarteTirees (list) : liste des cartes tirées au cours d'une partie de la manche
    '''
    police = int(TAILLEPOLICE//1.4)
    if lesCartesTirees[carte] == "#0":
        g.dessinerRectangle(coordX, coordY, largeurCarte, hauteurCarte, "blue")
        g.afficherTexte("Relique\n   prise", coordX + largeurCarte//2, coordY + hauteurCarte//2, couleurEcriture, police)
    elif lesCartesTirees[carte] > 0:
        g.dessinerRectangle(coordX, coordY, largeurCarte, hauteurCarte, "orange")
        g.afficherTexte("   " + str(lesCartesTirees[carte]) + "\nrubis", coordX + largeurCarte//2, coordY + hauteurCarte//2, couleurEcriture, police)
    elif lesCartesTirees[carte] < 0:
        g.dessinerRectangle(coordX, coordY, largeurCarte, hauteurCarte, "brown")
        g.afficherTexte("Danger\nnuméro\n     " + str(abs(lesCartesTirees[carte])), coordX + largeurCarte//2, coordY + hauteurCarte//2, couleurEcriture, police)
    else:
        g.dessinerRectangle(coordX, coordY, largeurCarte, hauteurCarte, "cyan")
        g.afficherTexte("Relique", coordX + largeurCarte//2, coordY + hauteurCarte//2, couleurEcriture, police)


def afficheCarteTirees(g, lesCarteTirees, couleuCarte, largeurCarte, hauteurCarte, ecartCarte):
    '''
    affiche les cartes tirées durant une partie de manche

    Params:
        lesCarteTirees (list) : liste des cartes tirées
        couleuCarte (str) : couleur de la carte
        largeurCarte (int) : largeur de la carte en graphique
        hauteurCarte (int) : hauteur de la carte en graphique
        ecartCarte (int) : ecart entre chaque carte que l'on va poser sur la "table"
    '''
    debutPremiereCarteX = (L//100) + largeurCarte + (L//100)
    nbCarteTirees = len(lesCarteTirees)
    g.afficherTexte("Cartes tirées :", L//6, H//40,"black", TAILLEPOLICE)
    for carte in range(nbCarteTirees):
        if carte <= 12:
            #coordonnées des cartes que l'on pose
            coordX = debutPremiereCarteX + (ecartCarte + largeurCarte) * carte
            coordY = (H*40)//800

        else:
            #coordonnées des cartes que l'on pose
            coordX = debutPremiereCarteX + (ecartCarte + largeurCarte) * ((carte % 12)-1)
            coordY = H//20 + ecartCarte + hauteurCarte

        afficheLaCarte(g, carte, coordX, coordY, largeurCarte, hauteurCarte, lesCarteTirees)







##################################################################################
#affiche le num de la manche et le surplus de rubis pas encore distribué
##################################################################################

def afficheNumManche(g, numManche, largeurCarte, hauteurCarte):
    '''
    affiche a quelle manche on est actullement sous forme graphique

    Params:
        numManche (int) : num de la manche actuelle
        largeurCarte (int) : largeur de la carte
        hauteurCarte (int) : hauteur de la carte
    '''
    coordX = largeurCarte
    coordY = 2.5*hauteurCarte
    affiche = "Manche n°" + str(numManche)
    g.afficherTexte(affiche, coordX, coordY, "black", TAILLEPOLICE)


def afficheSurplusRubis(g, surplusRubis, largeurCarte, hauteurCarte):
    '''
    affiche le surplus de rubis que l'on a dans une partie de la manche

    Params:
        surplusRubis (int) : le surplus de rubis de la partie de la manche
        largeurCarte (int) : largeur de la carte
        hauteurCarte (int) : hauteur de la carte
    '''
    affiche = "Surplus de rubis : " + str(surplusRubis)
    coordX = 5*largeurCarte
    coordY = 2.5*hauteurCarte
    g.afficherTexte(affiche, coordX, coordY, "black", TAILLEPOLICE)






###############################################################################
#Fonction permetttant de calculer la largeur et l'écart entre chaque case
###############################################################################

def repartitionCaseEnFonctionDeNombreJoueur(scorePartieJoueurs):
    '''
    return la largeur d'une case et l'écart au'il y a entre deux case pour remplit toute la largeur de la fenetre

    Params
        scorePartieJoueurs (dict) : score des joueurs de la partie => on peut donc savoir il y a cbs de joueurs dans l'entiereté d la partie
    Returns:
        largeurCase (int) : largeur de la case
        ecartCase (int) : ecart entre chaque carte et les bords
    '''
    if len(scorePartieJoueurs) <= 6:
        #si ya moins de 6 joueurs
        largeurCase = L//4
        ecartCase = (L - 3*largeurCase) // 4

    else:
        #si y'en a plus de 6
        largeurCase = L//5
        ecartCase = (L - 4*largeurCase) // 5
    return largeurCase, ecartCase







###########################################################################################
# fonctions concernant l'afficahge des scores, des status des joueurs...
###########################################################################################

def affichageDuTexte(g, largeurCase, hauteurCarte, couleurCase, joueur, couleurEcriture, scorePartieJoueurs, scoreMancheJoueurs, coordX, coordY, J_ou_R):
    '''
    affiche tout ce qu'on a créer:
        -le nom du joueur
        -son score de la partie
        -son score de la manche
    Params:
        largeurCase (int) : largeur de la case
        hauteurCarte (int) : hauteur de la case
        couleurCase (str) : couleur de fond de la case
        joueur (int) : le joueur pour lequel on créé la case
        couleurEcriture (str) : la couleur d'écriture de l'intérieur de la case
        scorePartieJoueurs (dict) : score de la partie de chaque joueur
        scoreMancheJoueurs (dict) : score de la manche de chaque joueur
        coordX (int) : coord x en haut a gauche
        coordY (int) : coord y en haut a gauche
        J_ou_R (str) : nous donne directement "joueur n" ou "Robot n"
    '''
    g.dessinerRectangle(coordX, coordY, largeurCase, hauteurCarte, couleurCase)
    g.afficherTexte(J_ou_R, coordX + largeurCase//2, coordY + hauteurCarte//12, couleurEcriture, int(TAILLEPOLICE//1.3))
    g.afficherTexte("Score partie : "+ str(scorePartieJoueurs[joueur]) + " rubis.", coordX + largeurCase//2.5, coordY + hauteurCarte//4, couleurEcriture, int(TAILLEPOLICE//1.4))
    g.afficherTexte("Score manche : "+ str(scoreMancheJoueurs[joueur]) + " rubis.", coordX + largeurCase//2.25, coordY + hauteurCarte//2.5, couleurEcriture, int(TAILLEPOLICE//1.4))


def avoirCoordcase(joueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs):
    '''
    donne les coordonnées de la case pour le joueurs en parametre (case en haut a gauche)

    Params:
        joueur (int) : id du joueur
        ecartCase (ecart entre chaque case)
        largeurCase (int) : largeur pour une seule case
        hauteurCarte (int) : hauteur pour une seule case
        scorePartieJoueurs (dict) : score de la partie des joueurs
    Returns:
        coordX, coordY (int) : les coords en haut a gauche de la case d'un joueur
    '''
    if len(scorePartieJoueurs) <= 6:
            #si y'en a plus on calucl les coordonnées de la case de chaque joueur en fonction du nombre de joueurs
            coordX, coordY = coordCaseJoueurInf6(joueur, ecartCase, largeurCase, hauteurCarte)

    else:
        #si y'en a plus on calucl les coordonnées de la case de chaque joueurs en focntion du nombre de joueurs
        coordX, coordY = coordCaseJoueurSup6(joueur, ecartCase, largeurCase, hauteurCarte)

    return int(coordX), int(coordY)


def coordCaseJoueurInf6(joueur, ecartCase, largeurCase, hauteurCarte):
    ''' 
    donne les coordonées de cases si il y a un nombre de joueur inf à 6
    parcque les case ne sont pas répartie de la meme facon s'il y a moins de 6 joueurs ou plus

    Params:
        joueur (int) : id du joueur
        ecartCase (ecart entre chaque case)
        largeurCase (int) : largeur pour une seule case
        hauteurCarte (int) : hauteur pour une seule case
    Returns:
        coordX, coordY (int) : les coords en haut a gauche de la case d'un joueur
    '''
    if joueur <= 2:
        coordX = ecartCase + (largeurCase + ecartCase) * joueur
        coordY = (H - H//2.2)

    else:
        coordX = ecartCase + (largeurCase + ecartCase) * (joueur - 3)
        coordY = (H - H//2.2) + H//40 + hauteurCarte

    return coordX, coordY


def coordCaseJoueurSup6(joueur, ecartCase, largeurCase, hauteurCarte):
    ''' 
    donne les coordonées de cases si il y a un nombre de joueur sup à 6
    parcque les case ne sont pas répartie de la meme facon s'il y a moins de 6 joueurs ou plus

    Params:
        joueur (int) : id du joueur
        ecartCase (ecart entre chaque case)
        largeurCase (int) : largeur pour une seule case
        hauteurCarte (int) : hauteur pour une seule case
    Returns:
        coordX, coordY (int) : les coords en haut a gauche de la case d'un joueur
    '''
    if joueur <= 3:
        coordX = ecartCase + (largeurCase + ecartCase) * joueur
        coordY = (H - H//2.2)
        
    else:
        coordX = ecartCase + (largeurCase + ecartCase) * (joueur - 4)
        coordY = (H - H//2.2) + H//40 + hauteurCarte

    return coordX, coordY


def afficheScoreJoueur(g, scorePartieJoueurs, scoreMancheJoueurs, largeurCase, ecartCase, hauteurCarte, couleurCase, couleurEcriture, NBJOUEURS, NBROBOTS):
    '''
    affiche le score des joueurs dans sa globalité
    le score de la partie et de la manche en cours

    Params:
        scorePartieJoueurs (dict) : score de la partie des joueurs
        scoreMancheJoueurs (dict) : score de la manche des joueurs
        hauteurCarte (int) hauteur d'une carte posée (les cartes tresors, danger et relique)
        couleurCase (str) : couleur d'une case du score d'un joueur, le fond seulememt
        NBJOUEURS (int) : nombre de joueurs dans la partie
        NBROBOTS (int) : nombre de robots dans la partie
    '''
    #on affiche une case pour chaque joueur qui va représenter son score
    for joueur in scorePartieJoueurs:
        coordX, coordY = avoirCoordcase(joueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)
        #affiche finale de la partie avec les bonnes coordonnées
        if joueur < len(scorePartieJoueurs) - NBROBOTS:
            #affiche les joueurs en premier
            affichageDuTexte(g, largeurCase, hauteurCarte, couleurCase, joueur, couleurEcriture, scorePartieJoueurs, scoreMancheJoueurs, coordX, coordY, ("Joueur " + str(joueur + 1)))
        else:
            #affiche les robots en deuxieme
            robotNum = joueur - NBJOUEURS
            affichageDuTexte(g, largeurCase, hauteurCarte, couleurCase, joueur, couleurEcriture, scorePartieJoueurs, scoreMancheJoueurs, coordX, coordY, ("Robot " + str(robotNum + 1)))


def afficheJoueurCamp(g, scorePartieJoueurs, joueurDansMine, ecartCase, largeurCase, hauteurCarte, couleur="red"):
    '''
    affiche "Au camp", ci ce joueur a quité la mine

    Params:
        scorePartieJoueurs (dict) : score des joueurs de la partie
        joueurDansMine (list) : list des joueurs encore dans la mine
        ecartCase (int) : ecart entre chaque case de joueur
        largeurCase (int) : largeur de la case du score d'un joueur
        hauteurCarte (int) : hauteur de n'importe quelle type de carte
        couleur (str) : couleur de l'écriture
    Returns:
        
    '''
    for joueur in scorePartieJoueurs:
        if joueur not in joueurDansMine:
            coordX, coordY = avoirCoordcase(joueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)
            g.afficherTexte("Au camp", coordX + largeurCase//2, coordY + hauteurCarte//1.4, couleur, int(TAILLEPOLICE))


def afficheLaPartie(g, lesCarteTirees, surplusRubis, scorePartieJoueurs, scoreMancheJoueurs, numManche, joueursDansMine, largeurCarte, hauteurCarte, ecartCarte, NBJOUEURS, NBROBOTS, largeurCase, ecartCase, couleurArrierePlan = "beige", couleurCarte = "brown", couleurCase = "white", couleurEcriture = "black"):
    '''
    affiche le déroulé de la partie

    Params:
        lesCarteTirees (list) : toutes les cartes tirées au cours d'un partie de la manche
        surplusRubis (int) : surplus de rubis a un certain moment donnée la manche
        scorePartieJoueurs (dict) : score de la partie des joueurs
        scoreMancheJoueurs (dict) : scofre de la manche des joueurs
        numManche (int) : a quelle manche on est
        joueursDansMine (list) : liste des joueurs dans la mine restant
        largeurCarte (int) : largeur d'une carte
        hauteurCarte (int) : hauteur d'une carte
        ecartCarte (ecart entre chaque carte)
        NBJOUEURS (int) : nombre de joueurs dans la partie
        NBROBOTS (int) : nombre de robots dans la partie
        largeurCase (int) : largeur de la case
        ecartCase (int) : ecart entre chque case de joueur
    '''
    g.dessinerRectangle(0, 0, L, H, couleurArrierePlan)

    afficheCarteTirees(g, lesCarteTirees, couleurCarte, largeurCarte, hauteurCarte, ecartCarte)

    afficheCarteTiree(g, lesCarteTirees, couleurCarte, largeurCarte, hauteurCarte)

    afficheNumManche(g, numManche, largeurCarte, hauteurCarte)

    afficheSurplusRubis(g, surplusRubis, largeurCarte, hauteurCarte)

    afficheScoreJoueur(g, scorePartieJoueurs, scoreMancheJoueurs, largeurCase, ecartCase, hauteurCarte, couleurCase, couleurEcriture, NBJOUEURS, NBROBOTS)

    afficheJoueurCamp(g, scorePartieJoueurs, joueursDansMine, ecartCase, largeurCase, hauteurCarte)


#MES TEST POUR LA FONCTION afficheLaPartie()
#changer les valeurs pour voir si ca focntionner toujours
'''
carteTiree=[14]
lesCarteTirees=[7,7,6,9,3,-6,4,7,3,14]
surplusRubis=3
scorePartieJoueurs={0:2, 1:3, 2:5, 3:5, 4:5, 5:5, 6:5, 7:5}
scoreMancheJoueurs={0:1, 1:2, 2:5, 3:5, 4:5, 5:5, 6:5, 7:5}
numManche=2
joueursDansMine=[0,1,2,3]

#des valeurs qui changent pas
largeurCarte=(L//15.3)
hauteurCarte=(H//5)
ecartCarte = (L//200)
largeurCase, ecartCase = repartitionCaseEnFonctionDeNombreJoueur(scorePartieJoueurs)

g = ouvrirFenetre(L,H)
afficheLaPartie(g, lesCarteTirees, surplusRubis, scorePartieJoueurs, scoreMancheJoueurs, numManche, joueursDansMine, largeurCarte, hauteurCarte, ecartCarte)
g.attendreClic()
'''







##############################################
#Partie sur l'intérogation des joueurs
##############################################

def dessineCarreeVertRouge(g, coordX, coordY, largeurCase, hauteurCarte):
    '''
    dessine des case en vert et rouge dans la case du joueur en parametre
    la case en veert va représenter le fait que le joueur souhaire rester
    au contraire si la case est rouge alors le joueur souhaite partir.

    Params:
        coordX (int) : coord x du début de la case d'un certain joueur
        coordY (int) : coord y du début de la case d'un certain joueur
        largeurCase (int) : largeur de la case du score des joueurs
        hauteurCarte (int) : hauteur de la case du score des joueurs
    '''
    #coord du carré vert en haut a gauche
    xVert = coordX + largeurCase // 6
    yVert = coordY + hauteurCarte // 1.7

    #coord du carré rouge en haut a gauche
    xRouge = coordX + largeurCase // 1.68
    yRouge = coordY + hauteurCarte // 1.7

    #dessin vert, RESTER
    g.dessinerRectangle(xVert, yVert, largeurCase//4, hauteurCarte//4, "green")
    g.afficherTexte("RESTER", xVert + largeurCase//8, yVert + hauteurCarte//8, "black", TAILLEPOLICE//2)

    #dessin rouge, SORTIR
    g.dessinerRectangle(xRouge, yRouge, largeurCase//4, hauteurCarte//4, "red")
    g.afficherTexte("SORTIR", xRouge + largeurCase//8, yRouge + hauteurCarte//8, "black", TAILLEPOLICE//2)


def afficheDemandeJoueur(g, scorePartieJoueurs, joueursDansMine, ecartCase, largeurCase, hauteurCarte, NBROBOTS, NBTOTO):
    '''
    demande au joueurs dans la mine s'ils veulent rester dans la mine ou pas
    on va juste mettre un carré vert pour oui et rouge pour non.
    des qu'il a choisi on enleve les cartes de couleurs et on met une carte noire pour dire qu'il a choisi.
    
    Params:
        scorePartieJoueurs(dict) : score des joueurs de la partie
        joueursDansMine (list) : liste des joueurs encore dans la mine
        ecartCase (int) : ecart entre chaque case de score de joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
        NBROBOTS (int) : nombre de robots dans la partie
        NBTOTO (int) : nombre de personne jouant au total (joueurs + robots)
    '''
    for joueur in scorePartieJoueurs:
        if joueur in joueursDansMine:
            if joueur < NBTOTO - NBROBOTS:
                coordX, coordY = avoirCoordcase(joueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)
                #affiche les carrés vert(oui) et en rouge(non) pour le joueur actuel de la boucle
                dessineCarreeVertRouge(g, coordX, coordY, largeurCase, hauteurCarte)


def dicoCoordCaseJoueur(scorePartieJoueurs, ecartCase, largeurCase, hauteurCarte):
    '''
    donne un dico contenant les coords en haut a gauche de la case d chaque joueur dans un dico

    Params:
        scorePartieJoueurs (dict) : score de la partie de chaque joueur
        ecartCase (int) : ecart entre chaque case de score de joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
    Returns:
        dicoCaseJoueur (dict) : dico contenant les coords des case de chaque joueur dans la partie, on prend de la case en haut a gauche
    '''
    dicoCaseJoueur = {}
    for joueur in scorePartieJoueurs:
        coordX, coordY = avoirCoordcase(joueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)
        dicoCaseJoueur[joueur] = [coordX, coordY]
    return dicoCaseJoueur

    
def couleurCliqueVertRouge(c, dicoCaseJoueur, joueur, largeurCase, hauteurCarte):
    '''
    renvoie vert ou rouge dependant de la couleur sur laquelle il clique

    Params:
        c : x et y
        dicoCaseJoueur (dict) : dico contenant les coords des case de chaque joueur dans la partie, on prend de la case en haut a gauche
        joueur (int) : le num du joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
    Returns:
        str : "vert" ou "rouge"
    '''
    #coord du carré vert en haut a gauche
    xVert = int(dicoCaseJoueur[joueur][0] + largeurCase // 6)
    yVert = int(dicoCaseJoueur[joueur][1] + hauteurCarte // 1.7)

    #coord du carré rouge en haut a gauche
    xRouge = int(dicoCaseJoueur[joueur][0] + largeurCase // 1.68)
    yRouge = int(dicoCaseJoueur[joueur][1] + hauteurCarte // 1.7)

    if (c.x >= xVert) and (c.y >= yVert) and (c.x <= xVert + largeurCase//4) and (c.y <= yVert + hauteurCarte//4):
        return "vert"
    elif (c.x >= xRouge) and (c.y >= yRouge) and (c.x <= xRouge + largeurCase//4) and (c.y <= yRouge + hauteurCarte//4):
        return "rouge"


def retireCouleurPourChoix(g, joueur, dicoCaseJoueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs, couleurArrierePlan = "white"):
    '''
    retire les carrés rouge et vert des joueurs passés en argument

    Params:
        joueur (int) : le num du joueur
        dicoCaseJoueur (dict) : dico contenant les coords des case de chaque joueur dans la partie, on prend de la case en haut a gauche
        ecartCase (int) : ecart entre chaque case de score de joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
        scorePartieJoueurs (dict) : score des joueurs de la partie
    '''
    xCoord, yCoord = avoirCoordcase(joueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)

    xHautGauche = int(dicoCaseJoueur[joueur][0] + largeurCase // 6)
    yHautGauche = int(dicoCaseJoueur[joueur][1] + hauteurCarte // 1.7)
    xlong = int((dicoCaseJoueur[joueur][0] + largeurCase // 1.68 + largeurCase//4) - xHautGauche)
    ylong = int((dicoCaseJoueur[joueur][1] + hauteurCarte // 1.7 + hauteurCarte//4) - yHautGauche)

    g.dessinerRectangle(xHautGauche, yHautGauche, xlong, ylong, couleurArrierePlan)


def cliqueDansCaseJoueur(c, dicoCaseJoueur, joueur, largeurCase, hauteurCarte):
    '''
    return Trus si le clique est dans une case d'un joueur (n'importe laquelle)

    Params:
        dicoCaseJoueur (dict) : dico contenant les coords des case de chaque joueur dans la partie, on prend de la case en haut a gauche
        joueur (int) : le num du joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
    '''
    return (c.x > dicoCaseJoueur[joueur][0]) and (c.y > dicoCaseJoueur[joueur][1]) and (c.x < dicoCaseJoueur[joueur][0] + largeurCase) and (c.y < dicoCaseJoueur[joueur][1] + hauteurCarte)


def cliqueDansJoueurMine(joueur, nbChoix, joueursDansMine):
    '''
    return True si le clique est dans la case d'un des joueurs dans la mine ET que celui-ci n'a pas encore fait un choix

    Params:
        joueur (int) : id du joueur
        nbChoix (list) : liste des joueurs n'ayant pas encore choisi
        joueursDansMine (list) : liste des joueurs encore présent dans la mine
    Returns:
        bool
    '''
    return (joueur in joueursDansMine) and (joueur in nbChoix)


def appliqueCouleurRouge(g, joueur, nbChoix, dicoCaseJoueur, joueursDansMine, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs, joueursPartant):
    '''
    -retire la personne de la liste des joueurs n'ayant pas encore choisi
    -retire les carrés vert et rouge

    Params:
        joueur (int) : id du joueur
        nbChoix (list) : liste contenant tous les joueurs n'ayant pas fait leur choix
        dicoCaseJoueur (dict) : dico contenant les coordonnées des cases des scores des joueurs (en haut a gauche)
        joueursDansMine (list) : liste des joueurs dans la mine
        ecartCase (int) : ecart entre chaque case de score de joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
        scorePartieJoueurs (dict) : score des joueurs de la partie
        joueursPartant (list) : liste des joueurs partant a un certain moment de la mine
    '''
    joueursDansMine.remove(joueur)
    nbChoix.remove(joueur)
    joueursPartant.append(joueur)
    retireCouleurPourChoix(g, joueur, dicoCaseJoueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)
    

def appliqueCouleurVert(g, joueur, nbChoix, dicoCaseJoueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs):
    '''
    -enleve la personne de la liste des joueurs dans la mine
    -retire la personne de la liste des joueurs n'ayant pas encore choisi
    -retire les carrés vert et rouge

    Params:
        joueur (int) : id du joueur
        nbChoix (list) : liste contenant tous les joueurs n'ayant pas fait leur choix
        dicoCaseJoueur (dict) : dico contenant les coordonnées des cases des scores des joueurs (en haut a gauche)
        ecartCase (int) : ecart entre chaque case de score de joueur
        largeurCase (int) : largeur de chaque case de score de joueur
        hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
        scorePartieJoueurs (dict) : score des joueurs de la partie
    '''
    nbChoix.remove(joueur)
    retireCouleurPourChoix(g, joueur, dicoCaseJoueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)


def executeDemandeJoueur(g, scorePartieJoueurs, joueursDansMine, ecartCase, largeurCase, hauteurCarte, joueursPartant, NBROBOTS, NBTOTO):
    '''
    attend jusqua ce que tous les joueurs dans la liste finissent de choisir oui ou non (sur le fait de rester ou pas dans la mine)
    si oui alors on enleve les cases verte et rouge
    si non alors on enelve les cases verte et rouge, puis on l'enleve de la liste des joueurs restant dans la mine

    Params:
    scorePartieJoueurs (dict) : score des joueurs de la partie
    joueursDansMine (list) : joueurs restant dans la mine
    ecartCase (int) : ecart entre chaque case de score de joueur
    largeurCase (int) : largeur de chaque case de score de joueur
    hauteurCarte (int) : hauteur de chaque case de score de joueur (c'est la meme que la hauteur d'une carte tirée)
    joueursPartant (list) : liste des joueurs partant a un certain moment de la mine
    NBROBOTS (int) : nombre de robots dans la partie
    NBTOTO (int) : nombre de joueurs au total dans la partie
    '''
    #liste des joueurs n'ayant pas encore fait leur choix initialisé a partir de la liste des joueur encore dans la mine
    nbChoix = [joueur for joueur in joueursDansMine if joueur < NBTOTO - NBROBOTS]
    #dico contenant en clé la valeur du num du joueur, et en valeur, les coordonnées d'en haut a gauche de la case pour chaque joueur
    dicoCaseJoueur = dicoCoordCaseJoueur(scorePartieJoueurs, ecartCase, largeurCase, hauteurCarte)

    #tant que tous les joueurs n'ont pas encore choisi
    while len(nbChoix) > 0:
        c = g.attendreClic()
        for joueur in dicoCaseJoueur: #if joueurQuiJoue >= NBJOUEURTOTO - NBROBOTS: 
            if joueur < NBTOTO - NBROBOTS:
                #regarde si on clique bien dans une case d'un des joueurs
                if cliqueDansCaseJoueur(c, dicoCaseJoueur, joueur, largeurCase, hauteurCarte):
                    #regarde si le joueur cliqué est dans la liste de ceux qui sont dans la mine
                    if cliqueDansJoueurMine(joueur, nbChoix, joueursDansMine):
                        #ragarde quelle couleur il a cliqué
                        couleur = couleurCliqueVertRouge(c, dicoCaseJoueur, joueur, largeurCase, hauteurCarte)
                        if couleur == "rouge":
                            appliqueCouleurRouge(g, joueur, nbChoix, dicoCaseJoueur, joueursDansMine, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs, joueursPartant)
                            break
                        elif couleur == "vert":
                            appliqueCouleurVert(g, joueur, nbChoix, dicoCaseJoueur, ecartCase, largeurCase, hauteurCarte, scorePartieJoueurs)
                            break




###############################################################
#affichage finale, une fois que les 5 manches sont effectuées
###############################################################

def afficheUnSeulGagnant(g, listeMeilleurJoueurs, scoreMax, NBROBOTS, NBTOTO):
    '''
    fait l'affiche si il y a un seul gangnant

    Params:
        listeMeilleurJoueurs (list) : liste conteant les meilleur joueurs de la partie
        scoreMax (int) : meilleur score de la partie
    '''
    if listeMeilleurJoueurs[0] < NBTOTO-NBROBOTS:
        g.afficherTexte("Le gagnant de cette partie est le", L//2, H//3, "black", TAILLEPOLICE)
        g.afficherTexte("Joueur " + str(listeMeilleurJoueurs[0] + 1), L//2, H//2.5, "black", TAILLEPOLICE)
        g.afficherTexte("avec un score de " + str(scoreMax), L//2, H//2.2, "black", TAILLEPOLICE)
    else:
        numRobot = listeMeilleurJoueurs[0] - (NBTOTO-NBROBOTS) + 1
        g.afficherTexte("Le gagnant de cette partie est le", L//2, H//3, "black", TAILLEPOLICE)
        g.afficherTexte("Robot " + str(numRobot), L//2, H//2.5, "black", TAILLEPOLICE)
        g.afficherTexte("avec un score de " + str(scoreMax), L//2, H//2.2, "black", TAILLEPOLICE)


def chainePlsGagnant(iGagnant, lenListeGagnant, joueurChaine, listeMeilleurJoueurs, NBROBOTS, NBTOTO):
    '''
    met a jour la chaine de caractere contenant les joueurs gangnant avec les "," et les "et"

    Params:
        gagnant (int) : num du gagnant dans la liste des joueurs ayant gagnés
        lenListeGagnant (int) : cbs de gagnant
        joueurChaine (str) : va faire "Joueur"
        listeMeilleurJoueurs (list) : liste conteant les meilleur joueurs de la partie
    Returns:
        joueurChaine (str) : chaine conteant les "," et les "et" s'il en faut avec le num des joueurs correspondant
    '''
    if listeMeilleurJoueurs[iGagnant] < NBTOTO-NBROBOTS:
        #gagnant remis a 0

        #on met rien a la fin, puisque c'et le dernier joueur iGagnant a afficher
        if iGagnant == lenListeGagnant - 1:
            joueurChaine += "Joueur " + str(listeMeilleurJoueurs[iGagnant] + 1)
        
        #on met un et a la fin puisque c'est l'avant dernier joueur
        elif iGagnant == lenListeGagnant - 2:
            joueurChaine += ("Joueur " +  str(listeMeilleurJoueurs[iGagnant] + 1) + " et " )
            
        #on met une virgule a la fin du joueur dans tous les cas
        else:
            joueurChaine += ("Joueur " + str(listeMeilleurJoueurs[iGagnant] + 1) + ", " )
    else:
        numRobot = listeMeilleurJoueurs[iGagnant] - (NBTOTO-NBROBOTS) + 1
        #on met rien a la fin, puisque c'et le dernier robot iGagnant a afficher
        if iGagnant == lenListeGagnant - 1:
            joueurChaine += "Robot " + str(numRobot)
        
        #on met un "et" a la fin puisque c'est l'avant derniere personne
        elif iGagnant == lenListeGagnant - 2:
            joueurChaine += ("Robot " +  str(numRobot) + " et " )
            
        #on met une virgule a la fin du robot dans tous les cas
        else:
            joueurChaine += ("Robot " + str(numRobot) + ", " )
        
    return joueurChaine
 

def affichePlsGagnants(g, listeMeilleurJoueurs, scoreMax, NBROBOTS, NBTOTO):
    '''
    fait l'affiche si il y a plusieurs gagnants

    Params:
        listeMeilleurJoueurs (list) : liste conteant les meilleur joueurs de la partie
        scoreMax (int) : meilleur score de la partie
    '''
    g.afficherTexte("Les gagnants de cette partie sont les :", L//2, H//3, "black", TAILLEPOLICE)
    joueurChaine = ""
    lenListeGagnant = len(listeMeilleurJoueurs)
    for iGagnant in range(lenListeGagnant):
        joueurChaine = chainePlsGagnant(iGagnant, lenListeGagnant, joueurChaine, listeMeilleurJoueurs, NBROBOTS, NBTOTO)
            
    g.afficherTexte(joueurChaine, L//2, H//2.5, "black", TAILLEPOLICE)
    g.afficherTexte("avec un score de " + str(scoreMax), L//2, H//2.2, "black", TAILLEPOLICE)


def affichageFinPartie(g, listeMeilleurJoueurs, scoreMax, NBROBOTS, NBTOTO, couleurArrierePlan="beige"):
    '''
    affichage de la fin de la partie

    Params:
        listeMeilleurJoueurs (list)
        scoreMax (int) : le score max du/des joueurs ayant gagnés
        NBROBOTS (int): cbs de robots dans la partie
        NBTOTO (int) : cbs de joueurs au total
    '''
    g.dessinerRectangle(0, 0, L, H, couleurArrierePlan)
    print(listeMeilleurJoueurs)
    if len(listeMeilleurJoueurs) == 1:
        afficheUnSeulGagnant(g, listeMeilleurJoueurs, scoreMax, NBROBOTS, NBTOTO)
    else:
        affichePlsGagnants(g, listeMeilleurJoueurs, scoreMax, NBROBOTS, NBTOTO)
    g.attendreClic()


'''
#TEST SUR LA FONCTION affichageFinPartie()

g = lancerFenetreJeu(L, H)
affichageFinPartie(g, [3], 15, 2, 5)
affichageFinPartie(g, [0,1,2], 20, 2, 5)
affichageFinPartie(g, [1,2], 42, 2, 5)
affichageFinPartie(g, [1,2,3], 0, 2, 5)
affichageFinPartie(g, [0,2,3,4], 0, 3, 5)
'''





######################
#les transitions
######################

def mancheVersManche(g):
    '''
    affiche simplement "Appuyer pour passer a la manche suivante"
    '''
    x = L//2
    y = H//3
    g.afficherTexte("Appuyer de nouveau pour passer à \n           la manche suivante", x, y, "black", int(TAILLEPOLICE * 2.5))
    g.attendreClic()


def mancheVersFin(g):
    '''
    affiche simplement : "Appuyer de nouveau pour passer aux résultat de la partie"
    '''
    x = L//2
    y = H//3
    g.afficherTexte("Appuyer de nouveau pour passer aux \n           résultats de la partie", x, y, "black", int(TAILLEPOLICE * 2.5))
    g.attendreClic()


def transition(g, numManche, nbTotalManche):
    '''
    applique la bonne transition
    - manche vers une nouvelle manche
    -manche vers l'ecran de fin de jeu
    Params:
        numManche (int) : a quelle manche on est
        nbTotalManche (int) : cbs de manches dans la partie
    '''
    if numManche == nbTotalManche:
        mancheVersFin(g)
    else:
        mancheVersManche(g)


#TEST SUR LA FONCTION transition()
'''
g = lancerFenetreJeu(L, H)
#transition(g, 3, 5)
#transition(g, 5, 5)
transition(g, 0, 5)
'''
