
while True:
    jack, jill = [int(i) for i in input().split()]
    sell=0
    if jack==0 and jill==0:
        break
    jackList =frozenset(int(input()) for _ in range(jack))
    jillList =frozenset(int(input()) for _ in range(jill))
    com = 0
    diff = jackList&jillList
            

    print(len(diff))

