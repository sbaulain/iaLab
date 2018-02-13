import numpy as np
import random
import math



class Node:

    def __init__(self):
            self.x = int
            self.heuristic = int
            self.children = []
            self.estimate = int
            self.costSoFar = 0
            self.heuristics =[]
            self.already = False

    def getX(self):
            return self.x

    def setX(self,name):
            self.x = name
           
    def getHeuristic(self):
            return self.heuristic
        
    def setHeuristic(self,h):
            self.heuristic = h
       
    def getChildren(self):
            return self.children
        
    def setChildren(self,x):
            self.children.append(x)

    def getEstimate(self):
            return self.estimate

    def setEstimate(self):
            self.estimate = self.heuristic + self.costSoFar

    def getCostSoFar(self):
            return self.costSoFar

    def setCostSoFar(self,x):
            self.costSoFar=x

    def setHeuristics(self,h):
            self.heuristics.append(h)
       
    def getHeuristics(self):
            return self.heuristics

    def setAlready(self,h):
            self.already=h
       
    def getAlready(self):
            return self.already

             
        


class Labyrinthe:

    def __init__(self):
            self.coutMatrice = [[]]

    def getCoutMatrice(self):
            return self.coutMatrice

    def setCoutMatrice(self):
            n=random.randint(5,10)
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
















    
