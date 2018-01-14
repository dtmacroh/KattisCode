# Cups
# Author:		Debbie Macrohon
# Description:	Using Python's dictionary structure 
#				and sorting the keys for the right solution 

rounds = int(input())	# initial input = number of rounds
array = [""]*rounds		# initializing an empty array
arranged = {}			# initializing an empty dictionary

for i in range (0, rounds):
	array[i] = input()

for i in range (0, rounds):
	inputs = array[i].split()
	# using a try-catch block to input radius and color 
	try:
		num = int(inputs[1])
		color = inputs[0]
	except:
		num = int(inputs[0])/2	# dividing number by 2 if number is in front of color
		color = inputs[1]
	arranged[num] = color
for key in sorted(arranged):
	print("{} ".format(arranged[key]))