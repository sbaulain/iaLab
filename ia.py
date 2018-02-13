import numpy as np
import random
import math
import matplotlib.pyplot as plt
from lab import *
from qLearn import *
from aStar import *
from statistics import mean


class Ia:

    def __init__(self):
           self.labyrinthe = Labyrinthe()

    def getLabyrinthe(self):
            return self.labyrinthe

    def setLabyrinthe(self):
       self.labyrinthe = Labyrinthe()



    def resolveIA(self,lab,sommetInit):

        #print("Avec apprentissage par renforcement :")

        
        
        mon_q=QLearning(mon_lab)
        mon_q.testQGammas(mon_lab,sommetInit)

        print("Avec l'algorithme A star :")

        mon_a=AStar(mon_lab)
        newM= mon_a.setListNodes(mon_lab,sommetInit)
        mon_a.a_star_search(mon_lab,sommetInit,newM)
        
        #print("Exemple d'execution du rapport:")




if __name__ == "__main__":

    mon_ia=Ia()
    mon_lab=mon_ia.labyrinthe
    mon_lab.setCoutMatrice()
    CM=mon_lab.getCoutMatrice()
    print(CM)
    
    sommetInit=random.randint(0,len(CM)-2)
    print('nous partirons du sommet :', sommetInit)
    mon_ia.resolveIA(mon_lab,sommetInit)


    print('fin')
