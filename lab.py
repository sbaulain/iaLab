import numpy as np
import random
import math

class Noeud:# pour moi

    def __init__(self):
           self.x = int
           self.Children = []
           self.BestChild = int
           self.costFromStart = int #g
           self.heuristic = int #h
           self.estimateCost = int #f 

    def getX(self):
            return self.x

    def getChildren(self):
            return self.heur
        
    def getEstimateCost(self):
            return self.getHeuristic() + self.getCostFromStart()

    def getBestChild(self):
            return self.BestChild

    def setChildren(self,x):
            return self.Children.append(x)

    def getBestChild(self,newX):
           self.x = newX

    def checkFrontier(self,newHeur):
           self.heur = newHeur



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

#Fonction de creation de la matrice Labyrinthe
def makeMat(n):

    M=np.zeros([n,n])
    i=random.randint(0,n-1)
    j=random.randint(0,n-1)
    while (i==j):
    		j=random.randint(0,n-1)
    M[i][j]=1
    M[j][i]=1
    v=M[:][n-1]
#Tant que la derniere colonne est vide, soit la sortie n est pas reliee,
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

#On rajoute des liaisons aleatoires pour creer d'autres chemins.
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
