#tolower.py

def main():
    p, t = [int(i) for i in input().split()]
    testC = 0
    count = 0
    for x in range (0, p):
        upperFlag = False
        for y in range(0, t):
            inp = list(input())
            inp[0] = inp[0].lower()
            for l in range(0,len(inp)):
                if not inp[l].islower():
                    upperFlag = True
                    break
        if not upperFlag:
            count+=1
    print(count)
main()