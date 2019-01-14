# Bing It On
# Author:		Debbie Macrohon
# Description:	Tree structure using Python's Dictionary
#				structure
rounds = int(input())			# initial input = number of rounds
arrayOfWords = [""]*rounds		# initializing an empty array
dictio = {'W':rounds}			# dictionary simulating a tree

for i in range (0, rounds):
	arrayOfWords[i] = input()

for i in range(0,rounds):
	count = 0
	d = dictio
	
	for letter in arrayOfWords[i]:
		if letter not in d:
			d[letter] = {'W':1} #w is the weight of the node
		d = d[letter]
		d['W'] +=1 		#add one to weight of node for exact matches 
		count = d['W']
	print(count-2)

