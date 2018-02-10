import numpy as np
import random
import math
import operator
from lab import *


def print_list(listi):
    temp=[]
    for j in range (0,len(listi)):
        temp.append(listi[j].getX())
    print (temp)
            
def estimate(listi):
    for j in range (0,len(listi)):
        listi[j].setEstimate()

def checkFrontier(start,frontier):
    for j in frontier:
        if start.getEstimate() > j.getEstimate():
            start=j

def changeMatrice(mat):
    n=len(mat)
    index=[]
    for i in range(0,n):
        for j in range (0,n):
            if i>j:
                mat[i,j]=0

    for l in range(0,n):
        temp=False
        for k in range (0,n):
            if mat[l,k]==1:
                temp = True
        if temp==False: #toute les lignes a zero
            index.append(l)
    
    d=0
    for p in index :
        if index[d]==n-1:
            mat[index[d],n-1]=1
        else :
            rand=random.randint(p+1, n-1)
            mat[index[d],rand]=1      
        d=d+1
         
         
         
        

        
class AStar:
    
    def __init__(self,mon_lab):
        self.list_nodes =[]
        
    def setListNodes(self,mon_lab,sommetInit):

        mat=mon_lab.getCoutMatrice()
        changeMatrice(mat)
        
        #mat = mon_lab.getExemple()
        
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

        return mat

    def a_star_search(self,mon_lab,sommetInit,mat):
        closedlist=[]
        
    
        n=len(mat)
        
        print(mat)
        start=self.list_nodes[sommetInit]
        goal=self.list_nodes[n-1]
        
        frontier = []
        x=0
        y=0
        start.setCostSoFar(0)
        it=0

        closedlist.append(start)

        while (goal.getX()!=start.getX() and it<10):
            #cost=start.getCostSoFar()
            start.setEstimate()
            for i in start.getChildren():           
                i.setCostSoFar(mat[start.getX(),i.getX()]+it)
                i.setEstimate()
                #print("IIIIII",i.getX(),i.getCostSoFar(),i.getHeuristic(),i.getEstimate())
                if frontier.count(i)==0:
                    frontier.append(i)                
    
                #print (start.getX(),frontier[i].getX(),frontier[i].getEstimate())

            print("frontiere:")
            print_list(frontier)

            estimate(frontier)

            
            candidate=self.getBestChild(start,goal)
            print(candidate.getX(),"candidate")
            
            checkFrontier(start,frontier)

            start = candidate
            it=it+1

            closedlist.append(candidate)
            frontier.remove(candidate)
            print("------------",it)

        print("Le chemin est :")    
        print_list(closedlist)

    def getBestChild(self,node,goal):
        found = False
        best = node.getChildren()[0]
        print("esti",0,best.getEstimate())
        for i in range (1,len(node.getChildren())):
            print("esti",i,node.getChildren()[i].getEstimate())
            if node.getChildren()[i].getEstimate()<best.getEstimate() and not (len(node.getChildren()[i].getChildren())==0) and found==False:
                best = node.getChildren()[i]
            if node.getChildren()[i].getX()==goal.getX():
                best = node.getChildren()[i]
                found = True

        return best

    
