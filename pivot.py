#pivot
def compareLower(tocomp, i):
	if i<0:
		return True
	elif int(array[i]) > tocomp:
		return False
	else:
		return compareLower(tocomp, i-1)
		
def compareUpper(tocomp, i):
	if i==num:
		return True
	elif int(array[i]) < tocomp:
		return False
	else:
		return compareUpper(tocomp, i+1)
	
	
num = int(input())
array_pivot = [0]*num
current_array = input().split()
count=0
c=0
array = [int(numeric_string) for numeric_string in current_array]

for i in range(0, num):
	
	num_to_compare = array[i]
	min = array[i]
	max= -1
	minrange =i-1
	 
	for x in range (i-1, i): 
		if array[x]>max:
			max = array[x]

	for y in range (i, num):
		
		if array[y]<min:
			min = array[y]
	
	if num_to_compare > min or num_to_compare < max and max!=-1:
		array_pivot[i] = -1
		c+=1
	#print("min {} , max {} , bad pivot count {}".format(min, max, c))
			
	#c1 = compareLower(num_to_compare, i)
	#c2 = compareUpper(num_to_compare, i)
	
	#if (c1 and c2):
	#	count+=1

#print(count)		
	

# for z in range (0,num):
	# if array_pivot[z]!=-1:
		# count+=1
print(num-c)
		

	
	