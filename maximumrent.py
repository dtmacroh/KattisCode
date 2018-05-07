#maximumrent.py

a,b = [int(i) for i in input().split()]
m, n = [int(i) for i in input().split()] 

if a>b:
    x = m-1
    y = 1
    while (2*x+y <n):
        y+=1
        x-=1
else:
    x = 1
    y = m-1
    while (2*x+y <n):
        y-=1
        x+=1
print(x*a+b*y)