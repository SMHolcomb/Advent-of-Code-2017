
# Advent of Code Day 1

"""
PART I
The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

PART II

The goal is to find the only two numbers in each row where one evenly divides the other 
- that is, where the result of the division operation is a whole number. 
They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.


"""

import string

def checksum(seq_list):
	# iterate through each row to get min and max
	sum = 0
	#iterate through each row
	for x in range(0,len(seq_list)):
		l = len(seq_list[x])
		min = max = seq_list[x][0]

		#iterate through each column
		for y in range(1,l):
			if seq_list[x][y] < min:
				min = seq_list[x][y]
			if seq_list[x][y] > max:	
				max = seq_list[x][y]
		sum += (max - min)			
		
	return sum

def checksum2(seq_list):
	sum = 0
	# bruteforce to find result with no remainder
	#iterate through each row 
	for row in range(0, len(seq_list)):
		#for each number in the row
		for x in range(0,len(seq_list[row])):
			# look at all the other numbers in the row
			for y in range(0,len(seq_list[row])):
				# avoid dividing number by itself
				if y == x:
					continue
				if seq_list[row][x]%seq_list[row][y] == 0:
					sum += (seq_list[row][x] / seq_list[row][y])	
	return sum				

		
def main():
	
	# *** PART I ***
	"""
	seq_list = []
	
	#read in file
	with open('checksum.txt','r') as checkfile:
		for line in checkfile:
			row = [int(i) for i in line.strip().split(',')]
			seq_list.append(row)
	#print(seq_list)

	sum = checksum(seq_list)
	print(sum)
	"""

# *** PART II ***
	
	seq_list = []
	with open('checksum.txt','r') as checkfile:
		for line in checkfile:
			row = [int(i) for i in line.strip().split(',')]
			seq_list.append(row)

	sum = checksum2(seq_list)
	print(sum)

if __name__ == "__main__":
	main()