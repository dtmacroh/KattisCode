#not done yet

tech, bus, time, incTech, incBus = [int(i) for i in input().split()]
companies = int(input())
compNeeds= [] 
for _ in range (0, companies):
    x,y = [int(i) for i in input().split()]
    compNeeds.append((x,y))

newTech = tech
newBus = bus

for c in range (0, time*time):
    newTech + 1

