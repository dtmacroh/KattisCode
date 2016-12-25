list = input("")
x = [int(i) for i in list.split()]


x[0] = (1- x[0])
x[1] = (1- int(x[1]))
x[2] = (2- int(x[2]))
x[3] = (2- int(x[3]))
x[4] = (2- int(x[4]))
x[5] = (8-int(x[5]))

for y in range(0,6):
	print(str(x[y]), end=" ") 

	
#print(x)