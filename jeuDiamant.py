from  jeuDiamant import*


if __name__ == "__main__":
    g = lancerFenetreJeu(L, H)
    NBJOUEURS, NBROBOTS = ouvrirAcceuil(g)
    rejouer = lancementJeu(g, NBJOUEURS, NBROBOTS)
