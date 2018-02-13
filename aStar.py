import numpy as np
import random
import math
import operator
from lab import *
from statistics import mean


def recur_heur(node):
    
    if node.getChildren():
        for n in node.getChildren():
            if n.getAlready()==False:
                n.setHeuristics(1+min(node.getHeuristics()))
                n.setAlready(True)
                recur_heur(n)
                
def set_heur(listi):    
    for i in listi:
        i.setHeuristics(10)
        
def set_all(listi,b):
    
    for i in listi:
        i.setAlready(b)

def set_heuristic_perfect(listi,n):

    for i in range (0,len(listi[n-1].getChildren())):
        listi[n-1].setAlready(True)
        random.shuffle(listi[n-1].getChildren())
        recur_heur(listi[n-1])
        set_all(listi[n-1].getChildren(),False)
            
    for i in listi:
        i.setHeuristic(min(i.getHeuristics()))

    listi[n-1].setHeuristic(0)
    
def set_heuristic_biaised(listi,n):

    for i in range (0,len(listi[n-1].getChildren())):
        listi[n-1].setAlready(True)
        random.shuffle(listi[n-1].getChildren())
        recur_heur(listi[n-1])
        set_all(listi[n-1].getChildren(),False)
            
    
    for i in listi:
        i.setHeuristic(mean(i.getHeuristics()))

    listi[n-1].setHeuristic(0)

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

def checkFrontier(start,frontier):
    
        temp=start
        for j in frontier:
            if start.getEstimate() > j.getEstimate():
                temp=j
        return temp        
         
        

        
class AStar:
    
    def __init__(self,mon_lab):
        self.list_nodes =[]
        
    def setListNodes(self,mon_lab,sommetInit):

        mat=mon_lab.getCoutMatrice()
        
        n=len(mat)#nb of nodes      
        for j in range (0,n):
            temp=Node()
            temp.setX(j)
            self.list_nodes.append(temp)
        
        for i in range (0,n):
            for l in range (0,n):
                if mat[i,l]!=0:
                    self.list_nodes[i].setChildren(self.list_nodes[l])

        self.list_nodes[n-1].setHeuristics(0)
        
        set_heur(self.list_nodes)

        set_heuristic_len(self.list_nodes,n)
               
        return mat

    def a_star_search(self,mon_lab,sommetInit,mat):
        closedlist=[]
        
    
        n=len(mat)

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

            #set frontier
            for i in start.getChildren():
                    i.setCostSoFar(mat[start.getX(),i.getX()]+it)
                    i.setEstimate()
                    #doublons
                    if frontier.count(i)==0 and closedlist.count(i)==0:
                        frontier.append(i)                
    
            print("frontiere:")
            print_list(frontier)
            
            candidate=self.getBestChild(start,goal,closedlist)

            if candidate==0:#cul de sac
                if frontier :
                    candidate=frontier[-1]
                else :
                    print("Labyrinthe impossible a resoudre")
                    break
         
            print(candidate.getX(),"candidate avant check")
            
            temp=checkFrontier(candidate,frontier)
            if temp!=candidate:
                candidate=temp
                print("check frontier")

            print(candidate.getX(),"candidate apres check")

            closedlist.append(candidate)
            frontier.remove(candidate)

            start = candidate
            it=it+1

            
            print("LISTE FERME:")
            print_list(closedlist)
            print("------------",it)

        print("Le chemin est :")    
        print_list(closedlist)

    def getBestChild(self,node,goal,closedlist):
        found = False
        best=0

        for i in node.getChildren():
            if closedlist.count(node.getChildren()[0])==0:
                best = node.getChildren()[0]
                break     
        
        for i in node.getChildren():
            if best !=0:
                print("esti",i.getX(),i.getEstimate())
                if i.getEstimate()<best.getEstimate() and closedlist.count(i)==0 and found==False:
                    best = i
                if i.getX()==goal.getX():
                    best = i
                    found=True

        return best

    
    
