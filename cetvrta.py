x1Count,x2Count,y1Count,y2Count  = [0]*4
x1,x2,y1,y2=[-1]*4

for x in range (0,3):
    inp = input("").split()
    if x1==-1 and y1==-1:
        x1 = int(inp[0])
        x1Count=x1Count+1
        y1= int(inp[1])
        y1Count=y1Count+1
    else:
        if x1==int(inp[0]):
            x1Count=x1Count+1
        else:
            x2=int(inp[0])
            x2Count= x2Count+1
        if y1==int(inp[1]):
            y1Count=y1Count+1
        else:
            y2 = int(inp[1])
            y2Count=y2Count+1

#print(" x1:{} count:{} x2:{} count:{} y1:{} count:{} y2:{} count:{}".format(x1,x1Count,x2, x2Count,y1,y1Count, y2, y2Count) )
finalx,finaly=[0]*2
if x1Count==1:
    finalx=x1
else:
    finalx=x2
if y1Count==1:
    finaly=y1
else:
    finaly=y2
print("{} {}".format(finalx, finaly))


