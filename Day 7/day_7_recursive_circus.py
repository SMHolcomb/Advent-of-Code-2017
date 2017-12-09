
# Advent of Code Day 7



"""
--- Part One ---

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)

to 

               gyxo
              /     
         ugml - ebii
       /      \     
      |         jptl
      |        
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |             
      |         ktlj
       \      /     
         fwft - cntj
              \     
                xhth


bottom program = 'tknk'

"""

import math
from itertools import *
import operator

def findBase(parent_nodes, child_nodes):
    # iterate through parents and find the one that is not in children
    #print("children:",child_nodes)
    #print("parents:",parent_nodes)
    for parent in parent_nodes:
        if parent not in child_nodes:
            return parent
        
    #return  parent




def readfile():

    parent_nodes = []
    child_nodes = []
    with open('recursivedata.txt','r') as towerfile:
        for line in towerfile:
            towers = line.strip('\n')
            #print(towers)
                
            split = towers.split("->") # split line to parent and children (if any)
                        
            if len(split) == 1:  #no --> with children

                parent, weight = split[0].split()  # get parent and weight from first part of split
                #print("parent:",parent,"weight:",weight)
                parent_nodes.append(parent)
                #print(parent_nodes)

            else:   #contains "->" so has children
                
                parent, weight = split[0].split()  #separate program from weight
                children = split[1].split()   #get children from split on --> above
                children = [child.strip(',') for child in children]
                #print("parent:",parent,"weight:",weight,"children:",children)
                parent_nodes.append(parent)
                child_nodes.extend(children)
                #parent_nodes.extend(parent)
   
    return parent_nodes, child_nodes
    #base_program = findBase(parent_nodes, child_nodes)
    #print(base_program)



def main():

    # *** PART I ***
    # import
    # determine longest list(s)
    # if a tie, then loop through and figure out which one is not in the others. That is the bottom program
  
    parent_nodes, child_nodes = readfile()
    base = findBase(parent_nodes, child_nodes)
    print(base)



if __name__ == "__main__":
	main()