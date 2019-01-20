# pet
# Author:		Debbie Macrohon
# Description:	


vars1 = [int(i) for i in input().split(" ")]
vars2 = [int(i) for i in input().split(" ")]
vars3 = [int(i) for i in input().split(" ")]
vars4 = [int(i) for i in input().split(" ")]
vars5 = [int(i) for i in input().split(" ")]

winner = 0
points = 0
array =[[0 for x in range(4)] for y in range(5)]  
array[0] = vars1
array[1] = vars2
array[2] = vars3
array[3] = vars4
array[4] = vars5

for r in range(0,5):
    totalrow = 0
    for c in range(0,4):
        #print(array[r][c])
        totalrow +=array[r][c]
    #print("total row {}".format(totalrow))
    if points < totalrow:
        winner = r+1
        points = totalrow 

print("{} {}".format(winner, points))