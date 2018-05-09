#simon

rounds = int(input())
for _ in range(0, rounds):
    inp = input().split()
    if len(inp)>2:
        if inp[0]=="simon" and inp[1]=="says":
            print(" ".join(inp[2:]))
        else:
            print()
    else:
        print()