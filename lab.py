import numpy as np
import random
import math



class Noeud:

    def __init__(self):
           self.x = int
           self.coutSuc = [int]
           self.heur = int

    def getXY(self):
            return self.x

    def getHeur(self):
            return self.heur

#?    def getRecompense(self,i):
#            return

#?    def getSucc(self,x):
#?            return

    def getCoutSucc(self):
            return self.coutSuc[:]

    def setXY(self,newX):
       self.x = newX

    def setHeuristique(self,newHeur):
       self.heur = newHeur

#?    def explorer(self,i):


class Labyrinthe:

    def __init__(self):
            self.listeNoeud = [Noeud]
            self.coutMatrice = [[]]

    def getNoeud(self,i):
            return self.listeNoeud[i]

    def getNoeuds(self):
            return self.listeNoeud

    def setNoeud(self):
            nb=random.randint(5,10)
            listeN=[]
            for i in range (0,nb):
                listeN.append(Noeud())
            self.listeNoeud = listeN

    def getCoutMatrice(self):
            return self.coutMatrice

    def setCoutMatrice(self):
            n=len(self.listeNoeud)
            self.coutMatrice = makeMat(n)


#Fonction de création de la matrice Labyrinthe
def makeMat(n):

#initialisaton M
    M=np.zeros([n,n])
    i=random.randint(0,n-1)
    j=random.randint(0,n-1)
    while (i==j):
    		j=random.randint(0,n-1)
    M[i][j]=1
    M[j][i]=1
    v=M[:][n-1]
#Tant que la derniere colonne est vide, soit la sortie n est pas reliée,
#on creer un chemin en iterant jusqu a celle ci.
    while (np.all(v==0)):
        ibis=random.randint(0,n-1)
        while ((ibis==i)or(ibis==j)):
               ibis=random.randint(0,n-1)
        M[ibis][j]=1
        M[j][ibis]=1
        jbis=j
        j=ibis
        i=jbis

#On rajoute des liaisons aleatoires pour créer d'autres chemins.
    nbModif=round(3*(n-1)/4)
    for it in range (0,nbModif):
        while ((M[i][j]==1) or (i==j)):
            i=random.randint(0,n-1)
            j=random.randint(0,n-1)
        M[i][j]=1
        M[j][i]=1
#si une piece du labyrinthe est isolee, soit une colonne de O, on la relie au reste.
    for col in range (0,n-1):
        v=M[:][col]
        if (np.all(v==0)):
            i=random.randint(0,n-1)
            while (i==col):
                i=random.randint(0,n-1)
            M[i][col]=1
            M[col][i]=1

    return M
