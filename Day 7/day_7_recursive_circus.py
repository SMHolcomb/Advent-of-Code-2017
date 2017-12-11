
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


--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could get down, if they 
weren't expending all of their energy trying to keep the tower balanced. Apparently, one program 
has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of 
those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The 
weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl 
must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs 
above it must each match. This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. 
Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 
units lighter for its stack to weigh 243 and keep the towers balanced. If this change were 
made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?


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
    towers = dict()
    weights = dict()  # !! should have used a dictionary in the first place !!
    parent_nodes = []
    child_nodes = []
    with open('recursivedata_test.txt','r') as towerfile:
        for line in towerfile:
            line = line.strip('\n')
            #print(towers)
                
            split = line.split("->") # split line to parent and children (if any)
                        
            if len(split) == 1:  #no --> with children

                parent, weight = split[0].split()  # get parent and weight from first part of split
                #print("parent:",parent,"weight:",weight)
                #towers[parent] = []
                parent_nodes.append(parent)
                #print(parent_nodes)
                weights[parent] = weight

            else:   #contains "->" so has children
                
                parent, weight = split[0].split()  #separate program from weight
                children = split[1].split()   #get children from split on --> above
                children = [child.strip(',') for child in children]
                #print("parent:",parent,"weight:",weight,"children:",children)
                towers[parent] = children
                parent_nodes.append(parent)
                child_nodes.extend(children)
                weights[parent] = weight
            weights[parent] = int(weight.replace('(','').replace(')',''))
        print(weights)
        print(towers)
    return parent_nodes, child_nodes, weights, towers




def main():
  
  # import
  
  parent_nodes, child_nodes, weights, towers = readfile()
    
  # *** PART I ***
  base = findBase(parent_nodes, child_nodes)
  print(base)

  # *** PART II ***
  # loop through towers, get weight for each child of the parent
  
  for k,v in weights.items():
      print(k,v)













if __name__ == "__main__":
	main()