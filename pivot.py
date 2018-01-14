#pivot
#def compareLower(tocomp, i):
#	if i<0:
#		return True
#	elif int(array[i]) > tocomp:
#		return False
#	else:
#		return compareLower(tocomp, i-1)
		
#def compareUpper(tocomp, i):
#	if i==num:
#		return True
#	elif int(array[i]) < tocomp:
#		return False
#	else:
#		return compareUpper(tocomp, i+1)
	
	
num = int(input())
array_pivot = [0]*num
current_array = input().split()
c=0
array = [int(numeric_string) for numeric_string in current_array]

for i in range(0, num):
	
	num_to_compare = array[i]
	min = array[i]
	max= -1
	minrange =i-1
	#if max < num_to_compare: 
	#	max = num_to_compare
	for x in range (0, i): 
		if array[x]>max:
			max = array[x]
	#if min < num_to_compare:
	#	min = num_to_compare
	for y in range (i, num):
		
		if array[y]<min:
			min = array[y]
	
	if num_to_compare > min or num_to_compare < max and max!=-1:
		array_pivot[i] = -1
		c+=1
	#print("min {} , max {} , bad pivot count {}".format(min, max, c))
	


print(num-c)
		

	
	