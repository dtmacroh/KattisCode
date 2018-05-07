#nastyhacks.py

rounds = int(input())

for _ in range(0, rounds):
    r,e,c = [int(i) for i in input().split()]
    if r>e-c:
        print("do not advertise")
    elif r< e-c:
        print("advertise")
    else:
        print("does not matter")