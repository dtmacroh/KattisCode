#above_average

rounds = int(input())
array = [""]*rounds
arranged = {}
for i in range (0, rounds):
	array[i] = input()

for i in range (0, rounds):
	inputs = array[i].split()
	try:
		num = int(inputs[1])
		color = inputs[0]
	except:
		num = int(inputs[0])/2
		
		color = inputs[1]
	arranged[num] = color
for key in sorted(arranged):
	print("{} ".format(arranged[key]))