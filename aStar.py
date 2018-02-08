import numpy as np
import random
import math
import operator
from lab import *




def checkFrontier(start,frontier):  
    for j in frontier:
        if start.getEstimate() > j.getEstimate():
            return j
        else :
            return False

def changeMatrice(mat,sommetInit):
    n=len(mat)
    for j in range(0,n):
        mat[j,sommetInit]=mat[j,0]*10

        
class AStar:
    
    def __init__(self,mon_lab):
        self.list_nodes =[]
        
    def setListNodes(self,mon_lab,sommetInit):
        mat=mon_lab.getCoutMatrice()
        changeMatrice(mat,sommetInit)#On multiplie par 1à les cout de retour en arrière
        n=len(mat)#nb of nodes      
        for j in range (0,n):
            temp=Node()
            temp.setX(j)
            self.list_nodes.append(temp)
        #creer la liste de successeur pour chaque noeud
        
        for i in range (0,n):
            for l in range (0,n):
                if mat[i,l]!=0:
                    self.list_nodes[i].setChildren(self.list_nodes[l])
            #heuristic nodes
            h=len(self.list_nodes[i].getChildren())
            self.list_nodes[i].setHeuristic(h)
        self.list_nodes[sommetInit].setHeuristic(0)
        self.list_nodes[n-1].setHeuristic(0)

    def a_star_search(self,mon_lab,sommetInit):
        mat=mon_lab.getCoutMatrice()
        changeMatrice(mat,sommetInit)
        n=len(mat)
        
        print(mat)
        start=self.list_nodes[sommetInit]
        goal=self.list_nodes[n-1]
        
        frontier = []
        x=0
        y=0
        start.setCostSoFar(0)
        j=0
        

        while (goal.getX()!=start.getX() and j<2):
            #cost=start.getCostSoFar()
            start.setEstimate()
            for i in range (0,len(start.getChildren())):           
                start.getChildren()[i].setCostSoFar(mat[sommetInit,start.getChildren()[i].getX()]+j)
                frontier.append(start.getChildren()[i])
                frontier[i].setEstimate()
                print (start.getX(),frontier[i].getX(),frontier[i].getEstimate())
               
            candidate=self.getBestChild(start)
            #print(candidate.getX(),"can")
            
            if checkFrontier(start,frontier) != False :
                 candidate = checkFrontier(start,frontier)

            #candidate.setCostSoFar(1+start.getCostSoFar())#rajout du chemin parcouru
            start = candidate
            j=j+1
            print("------------",j)
            del(frontier[:])


    def getBestChild(self,node):
        best = node.getChildren()[0]
        print("esti",node.getX(),best.getEstimate())
        for i in range (1,len(node.getChildren())):
            print("esti",node.getX(),node.getChildren()[i].getEstimate())
            if node.getChildren()[i].getEstimate()<best.getEstimate() and not (len(node.getChildren()[i].getChildren())==0):
                best = node.getChildren()[i] 
        return best

    
