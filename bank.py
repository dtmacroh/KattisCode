#bank.py

rounds, minutes = [int(i) for i in input("").split() ]
listI=[]
for r in range (0, rounds):
    mon, min = [int (i) for i in input("").split()]
    listI.append((mon,min))

listI.sort(key=lambda tup: (tup[1]))
amt =  listI[0][0]
gndTotal = 0
maxWait= minutes
counterWait = 0
#print(listI)
for x in range (0, len(listI)):
    currWait =  listI[x][1]
    currAmt =  listI[x][0]
    if (counterWait < maxWait):
        if currWait== counterWait and currAmt>= amt:
            amt = currAmt
            
        if x==len(listI)-1 and listI[x-1][1]!=currWait:
            gndTotal = gndTotal + currAmt
        elif x==len(listI)-1 and listI[x-1][1]==currWait :
            if currAmt > amt:
                gndTotal = gndTotal + currAmt
            else:
                gndTotal = gndTotal + amt
        elif currWait > counterWait :
            counterWait = counterWait +1
           # print("counterwait {}".format(counterWait))
           # print("amt {}".format(amt))
            gndTotal = gndTotal + amt
            amt = currAmt
            
           # print("gndTotal as of now {}".format(gndTotal))

     
    
print(gndTotal)