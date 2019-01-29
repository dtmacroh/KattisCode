# elevatortrouble
# Author:		Debbie Macrohon
# Description:	greedy algorithm

vars = [int(i) for i in input().split(" ")]
floors = vars[0]
start = vars[1]
goal = vars[2]
up = vars[3]
down = vars[4]

pushes = 0
going = start

#going up while loop
while (goal>going) and up >0:
    going= going + up
    pushes +=1

#going down while loop
while (going > goal) and down >0:

    going = going-down
    pushes +=1

if going==goal:
    print(pushes)
else:
    print("use the stairs")

    