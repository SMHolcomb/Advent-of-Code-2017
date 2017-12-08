
# Advent of Code Day 6



"""
--- Part One ---
In this area, there are sixteen memory banks; each memory bank can hold any number of blocks. 
The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with 
the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks 
among the banks. To do this, it removes all of the blocks from the selected bank, then moves 
to the next (by index) memory bank and inserts one of the blocks. It continues doing this u
ntil it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks 
configuration is produced that has been seen before.

For example, imagine a scenario with only four memory banks:

The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so 
it is chosen for redistribution.
Starting with the next bank (the fourth bank) and then continuing to the first bank, the 
second bank, and so on, the 7 blocks are spread out over the memory banks. The fourth, 
first, and second banks get two blocks each, and the third bank gets one back. The final 
result looks like this: 2 4 1 2.
Next, the second bank is chosen because it contains the most blocks (four). Because there are 
four memory banks, each gets one block. The result is: 3 1 2 3.
Now, there is a tie between the first and fourth memory banks, both of which have three blocks. 
The first bank wins the tie, and its three blocks are distributed evenly over the other three 
banks, leaving it with none: 0 2 3 4.
The fourth bank is chosen, and its four blocks are distributed such that each of the four banks 
receives one: 1 3 4 1.
The third bank is chosen, and the same thing happens: 2 4 1 2.
At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite 
loop is detected after the fifth block redistribution cycle, and so the answer in this example is 5.


--- Part Two ---

The debugger would also like to know the size of the loop: starting from a state that has already been seen, 
how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

RESOURCE: https://stackoverflow.com/questions/6193498/pythonic-way-to-find-maximum-value-and-its-index-in-a-list
https://infohost.nmt.edu/tcc/help/pubs/python/web/divmod-function.html



"""

import math
from itertools import *
import operator

def readfile():
    with open('memallocdata.txt','r') as memfile:
        for line in memfile:
            orig_mem = [int(i) for i in line.strip().split('\t')]
            #orig_mem.append(num)
    return orig_mem



def allocate(orig_mem):

    #get maximum value in list and it's index
    max_idx, max_val = max(enumerate(orig_mem), key=operator.itemgetter(1))
   
    #set current block to 0
    orig_mem[max_idx] = 0
    # reallocate - wrap if needed
    # ideally would like to use itertools cycle()
    for _ in range(max_val):
        if max_idx+1 == len(orig_mem):
            max_idx=0
        else:
            max_idx +=1
        orig_mem[max_idx] +=1

    return orig_mem[:]


def main():

    # *** PART I ***

    # get data
    #orig_mem = [0, 2, 7, 0]
    orig_mem = readfile()
    
    # make a copy to be held static otherwise only references are stored
    #new_mem = orig_mem[:]
    new_mem = [orig_mem[:]]

    # loop through and reallocate
    # reallocate the memory
    for _ in count():

        realloc_mem = allocate(orig_mem)

        if realloc_mem in new_mem:
            print(len(new_mem))
            break

        else:
            new_mem.append(realloc_mem)

    # *** PART II ***

    # realloc_mem = What we're looking for
    #total length - where we found the first match
    print(len(new_mem) - new_mem.index(realloc_mem))



if __name__ == "__main__":
	main()