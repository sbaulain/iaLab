import numpy as np
import random
import math
import operator
from lab import *
from statistics import mean


#Fonction recursive qui permet de calculer une bonne heuristique
def recur_heur(node):
    
    if node.getChildren():
        for n in node.getChildren():
            if n.getAlready()==False:
                n.setHeuristics(1+min(node.getHeuristics()))
                #Le "cocher" si on y passe
                n.setAlready(True)
                recur_heur(n)
                
def set_heur(listi):    
    for i in listi:
        i.setHeuristics(10)
        
def set_all(listi,b):    
    for i in listi:
        i.setAlready(b)

#parametrage de la bonne heuristique
def set_heuristic_perfect(listi,n):
    #On effectue la fonction récursive plusieurs fois pour prendre le MINIMUM des heuristiques calculees
    for i in range (0,len(listi[n-1].getChildren())):
        listi[n-1].setAlready(True)
        random.shuffle(listi[n-1].getChildren())
        recur_heur(listi[n-1])
        set_all(listi[n-1].getChildren(),False)            
    for i in listi:
        i.setHeuristic(min(i.getHeuristics()))
    listi[n-1].setHeuristic(0)

#parametrage de la bonne heuristique biaisee    
def set_heuristic_biaised(listi,n):
    for i in range (0,len(listi[n-1].getChildren())):
        listi[n-1].setAlready(True)
        random.shuffle(listi[n-1].getChildren())
        recur_heur(listi[n-1])
        set_all(listi[n-1].getChildren(),False)    
    for i in listi:
        i.setHeuristic(mean(i.getHeuristics()))
    listi[n-1].setHeuristic(0)

#parametrage d'une heuristique simple qui
#est égale au nombre de laisons sortantes du noeud
def set_heuristic_len(listi,n):
    for i in listi:
        i.setHeuristic(n-len(i.getChildren()))
    listi[n-1].setHeuristic(0)

def print_list(listi):    
    temp=[]
    for j in range (0,len(listi)):
        temp.append(listi[j].getX())
    print (temp)
            
def estimate(listi):    
    for j in range (0,len(listi)):
        listi[j].setEstimate()

#fonction qui regarde la frontiere et renvoie un meilleur candidat si il existe
def checkFrontier(start,frontier):
        temp=start
        for j in frontier:
            if start.getEstimate() > j.getEstimate():
                temp=j
        return temp        
         

class AStar:

    #initialisation
    def __init__(self,mon_lab):
        self.list_nodes =[]

    #parametrer la liste des noeud grace a la matrice de cout   
    def setListNodes(self,mon_lab,sommetInit,p):
        mat=mon_lab.getCoutMatrice()        
        n=len(mat)#nb de noeuds     
        for j in range (0,n):
            temp=Node()
            temp.setX(j)
            self.list_nodes.append(temp)
        #parametrage des enfants en fonction des liaisons
        for i in range (0,n):
            for l in range (0,n):
                if mat[i,l]!=0:
                    self.list_nodes[i].setChildren(self.list_nodes[l])
        self.list_nodes[n-1].setHeuristics(0)        
        set_heur(self.list_nodes)
        #choix de l'heuristique
        if p==1:
            set_heuristic_perfect(self.list_nodes,n)
        if p==2:
            set_heuristic_biaised(self.list_nodes,n)
        if p==3:
            set_heuristic_len(self.list_nodes,n)
        return mat

    def a_star_search(self,mon_lab,sommetInit,mat):
        n=len(mat)
        closedlist=[]
        #parametrage entree sortie
        start=self.list_nodes[sommetInit]
        goal=self.list_nodes[n-1]       
        frontier = [] #ou liste ouverte
        start.setCostSoFar(0)
        it=0
        closedlist.append(start)#on a deja parcouru le depart

        while (goal.getX()!=start.getX() and it<10):
            start.setEstimate()
            #ajout des enfants de start a la frontiere
            for i in start.getChildren():
                    i.setCostSoFar(mat[start.getX(),i.getX()]+it)
                    i.setEstimate()
                    #gestion des doublons et de ceux qui ont deja ete parcouru
                    if frontier.count(i)==0 and closedlist.count(i)==0:
                        frontier.append(i)                
            #calcul du meilleur candidat, celui avec la fonction d'estimation la plus faible
            candidate=self.getBestChild(start,goal,closedlist)
            if candidate==0:#cul de sac
                if frontier :
                    candidate=frontier[-1]
                else :
                    #lorsqu'on est tombe sur une boucle infini
                    print("Labyrinthe impossible a resoudre en partant de ",sommetInit)
                    break
            #on regarde si il y a mieux dans la frontiere
            temp=checkFrontier(candidate,frontier)
            if temp!=candidate:
                print("On a verifier la frontiere et le candidat est passe de",temp.getX(),"à",candidate.getX())
                candidate=tem
            closedlist.append(candidate)
            frontier.remove(candidate)
            start = candidate
            it=it+1

        print("Le chemin parcouru par A*est :")    
        print_list(closedlist)

    #methode pour trouver l'enfant avec l'estimation la plus faible
    def getBestChild(self,node,goal,closedlist):
        found = False
        best=0
        for i in node.getChildren():
            #si tous les enfants du noeud ont deja ete parcouru, on doit passer a un autre noeud de la frontiere(programme principal)
            if closedlist.count(node.getChildren()[0])==0:
                best = node.getChildren()[0]
                break             
        for i in node.getChildren():
            if best !=0:
                if i.getEstimate()<best.getEstimate() and closedlist.count(i)==0 and found==False:
                    best = i
                if i.getX()==goal.getX():
                    best = i
                    found=True
        return best

    
    
