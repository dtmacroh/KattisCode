

rounds = int(input())
array= [""]*rounds
for i in range(0, rounds):
	array[i]=input()

for i in range(0, rounds):
	possible = False
	nums = array[i].split()
	num1 = int(nums[0])
	num2 = int(nums[1])
	num3 = int(nums[2])
	#addition case
	if num1 + num2==num3:
		possible = True		
	#subtraction case
	elif abs(num1-num2)==num3:
		possible = True
	#multiplication case
	elif num1*num2 == num3:
		possible = True
	#division case
	elif num1/num2==num3:
		possible = True
	elif num2/num1==num3:
		possible = True
	
	if (possible):
		print("Possible")
	else:
		print("Impossible")

