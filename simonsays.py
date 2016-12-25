userinput = eval(input())

while (userinput > 0):

	simonsay = input()
	simonstring = simonsay[0:10]
	if simonstring == "Simon says":
		print(simonsay[11:])
	
	userinput = userinput -1;
