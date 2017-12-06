
# Advent of Code Day 5



"""
PART I
The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3
Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example, these offset values will be written all on one line, with the current instruction marked in parentheses. The following steps would be taken before an exit is found:

(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
In this example, the exit is reached in 5 steps.

PART II:
Now, the jumps are even stranger: after each jump, if the offset was three or more, 
instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, 
and the offset values after finding the exit are left as 2 3 2 3 -1.



"""

import math
from itertools import *

def readfile():
    with open('jumpdata.txt','r') as jumpfile:
        for line in jumpfile:
            seq_list = [int(line) for line in jumpfile]
    return seq_list

def main():

    # *** PART I ***
    steps = 0  # jump count

    #read in file
    seq_list = readfile()
    curr_idx = curr_val = jump = 0

    while curr_idx >=0 and curr_idx < len(seq_list):
        # if positive, move forward and offset by 1
        # if negative, move backward and offset by 1
        jump = seq_list[curr_idx]
        seq_list[curr_idx]+=1
        curr_idx+=jump 
        steps += 1
    print(steps)
    
    
    # *** PART II ***
    steps = 0  # jump count

    #read in file
    seq_list = readfile()
    curr_idx = curr_val = jump = 0

    while curr_idx >=0 and curr_idx < len(seq_list):
        #print(curr_idx, jump, seq_list[curr_idx])
        # if offset >= 3 increment value by 1 else decrement by 1
        jump = seq_list[curr_idx]
        if jump >=3:
            seq_list[curr_idx]-=1
        else:
            seq_list[curr_idx]+=1
        
        curr_idx+=jump 
        steps += 1
    print(steps)
    

if __name__ == "__main__":
	main()