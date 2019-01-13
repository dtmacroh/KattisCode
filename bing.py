# Bing
# Author:		Debbie Macrohon
# Description:	Using Python's dictionary structure 
#				and sorting the keys for the right solution 

rounds = int(input())	# initial input = number of rounds
array = [""]*rounds		# initializing an empty array


for i in range (0, rounds):
	array[i] = input()

for st in range (0, len(array)):
	count = 0
		
	for r in range(0, st):
			
		if array[st]==array[r][0:len(array[st])]: 
			#print("yes")
			count=count+1
				
	print(str(count))


#print("hi")