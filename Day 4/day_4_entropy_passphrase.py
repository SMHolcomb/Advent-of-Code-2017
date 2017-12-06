
# Advent of Code Day 4

"""
PART I
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

PART II
Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.


RESOURCES:
https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
"""

import math
from itertools import *

def sort(pass_list):
	pass_sort = []
	for i in pass_list:
		pass_sort.append(sorted(i))	

	return pass_sort

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def main():
	
	
	pass_list = []
	count = 0  # running count valid phrases
	#read in passphrase file

	with open('passphrase.txt','r') as checkfile:
		for line in checkfile:
			row = [i for i in line.strip().split(' ')]
			pass_list.append(row)

	"""
	# *** PART I ***		
	pass_sort = sort(pass_list)

	for i in pass_sort:   #individual pass phrases
		valid = True
		for j in range(len(i)):		
			for k in range(j+1, len(i)):
				if i[j]==i[k]:
					valid = False

		if valid == True:
			count +=1	

	print(count)
	"""

	# *** PART II ***

	for sublist in pass_list:   #passphrase
		# print("  ")
		# print("**************")
		# print("  ")
		valid = True
		for j in range(len(sublist)):   # word
			# now get every combination of the word EXCEPT CURRENT WORD
			perms = []
			perms = [''.join(p) for p in permutations(sublist[j])]
			
			for perm in perms:
				#remove original word before doing compare
				# think this could be done to original sublist instead of making a copy
				sublist2 = [element for i, element in enumerate(sublist) if i != j]
				if perm in sublist2:
					valid = False
					continue
		
		if valid == True:
			count +=1	

	print(count)

if __name__ == "__main__":
	main()



