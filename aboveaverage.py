# above_average
# Author:		Debbie Macrohon
# Description:	Getting the average of the scores
#				and counting the percentage of students who are 
#				above this value.
rounds = int(input())
array = [""]*rounds
for i in range (0, rounds):
	array[i] = input()

for i in range (0, rounds):
	inputs = array[i].split()
	students = int(inputs[0])
	sum = 0
	above_av = 0
	
	for x in range(1,students+1):
		sum += float(inputs[x])
	avg = float(sum/students)
	for y in range(1,students+1):
		if float(inputs[y]) > avg:
			above_av += 1
	result = float(float(above_av)/float(students)*100)
	
	print("{0:.3f}% ".format(result))

		