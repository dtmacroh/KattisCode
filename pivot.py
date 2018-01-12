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
	
	num_to_compare = int(array[i])
	
	for x in range (0, i):
		if num_to_compare < array[x] :
			
			array_pivot[i] = -1
			x=i
			c+=1
			break
	
	if array_pivot[i]==0: 
		for y in range (i, num):
			if num_to_compare > array[y] :
				array_pivot[i] = -1
				y=num
				c+=1
				break
			
	#c1 = compareLower(num_to_compare, i)
	#c2 = compareUpper(num_to_compare, i)
	
	#if (c1 and c2):
	#	count+=1

#print(count)		
	

# for z in range (0,num):
	# if array_pivot[z]!=-1:
		# count+=1
print(num-c)
		

	
	