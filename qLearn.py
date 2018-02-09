import numpy as np
import random
import math
import operator
import matplotlib.pyplot as plt
from lab import *



def first(sommet,q,r,gamma):
    listSom=[]
    listChosenSom=[]
    n=len(q)
    maxrec=0
    for nextSom in range (0,n):
        if (r[nextSom][sommet]>=0):
            listSom.append(nextSom)
    chosenSom=random.choice(listSom)
    for nextSom in range (0,n):
        if (r[chosenSom][nextSom]>=0):
            listChosenSom.append(nextSom)
    maxSom=max(q[chosenSom][:])
    newrec=round(r[sommet][chosenSom]+gamma*maxSom)
    q[sommet][chosenSom]=newrec
    return q,chosenSom

def keepGoing(q,r):
    n=len(q)
    done=False
    for i in range (0,n):
        for j in range (0,n):
            if (q[i][j]<=0) and (r[i][j]>=0):
                done=True
    return done


class QLearning:

    def __init__(self,mon_lab):
            n=len(mon_lab.getCoutMatrice())
            self.q = np.zeros([n,n])
            self.r = np.zeros([n,n])
            self.conv = []
            self.gamma = []

    def set_r(self,mon_lab):
        newCM=mon_lab.getCoutMatrice()
        n=len(newCM)
        for j in range (0,n):
            for i in range (0,n):
                if (j==n-1) and (newCM[i][j]==1):
                        newCM[i][j]=100
                else:
                        if (newCM[i][j]==1):
                            newCM[i][j]=0
                        else :
                            newCM[i][j]=-1
        self.r=newCM

    def get_r(self):
        return self.r


    def testQ(self):
        n=len(self.q)-1
        it=0
        while (keepGoing(self.q,self.r)==True) and (it<504):
            som=random.randint(0,n)
            while True:
                [self.q,newSom]=first(som,self.q,self.r,0.5)
                som=newSom
                if (som!=n):
                    break
            it=it+1
        self.conv.append(it)


    def setQinit(self):
            self.q=np.zeros([len(self.q),len(self.q)])

    def setgamma(self,newGamma):
            self.gamma=newGamma

    def traceChemin(self,i):
            n=len(self.q)
            sommet=self.q[i][:]
            chemin=[i]
            jmax=0
            while (i!=n-1) :
                coutMax=0
                for j in range (0,n):
                    cout=self.q[i][j]
                    if (cout>coutMax):
                        coutMax=cout
                        jmax=j
                self.q[i][jmax]=0
                i=jmax
                chemin.append(i)
            print('le chemin a suivre est : ',chemin)


    def testQGammas(self,mon_lab,sommetInit):
        self.set_r(mon_lab)
        x=[]
        for i in range (1,9):
              self.setQinit()
              self.setgamma(i*0.1)
              self.testQ()
              x.append(i*0.1)
        print('Pour le QLearning nous obtenons la matrice solution :')
        print(self.getQ())
        self.traceChemin(sommetInit)
        fig = plt.figure()
        plt.plot(x,self.conv)
        fig.suptitle('Nombres d iterations jusqu a convergence en fonction des valeurs de gamma', fontsize=20)
        plt.xlabel('gamma', fontsize=18)
        plt.ylabel('Nb itérations', fontsize=16)
        fig.savefig('convergence.jpg')
        #plt.show()



    def getQ(self):
            return self.q
