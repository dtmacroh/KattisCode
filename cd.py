# works with Python 2.7

while True:
    jack, jill = [int(i) for i in raw_input().split()]
    sell=0
    if jack==0 and jill==0:
        break
    jackList =set(int(raw_input()) for _ in range(jack))
    jillList =set(int(raw_input()) for _ in range(jill))
    diff = jackList&jillList
    print(len(diff))