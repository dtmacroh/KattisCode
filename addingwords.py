#addingwords.py

d = {}
while True:
    rawinp = input()
    inp = rawinp.split()
    if inp[0]=="clear":
        break
    if inp[0] =="def":
        d[inp[1]] = int(inp[2])
    if inp[0] == "calc":
        unknown = False
        eq = []
        for c in range(1, len(inp)-1):
            if c%2==1: #if c is odd.. which means its a variable
                if inp[c] in d:
                    eq.append(str(d[inp[c]]))
            else:
                eq.append(inp[c])
        try:
            num = eval(''.join(eq))
        except:
            unknown = True
        if not unknown:
            found = False
            for name, value in d.items():
                if num == value:
                    print(' '.join(inp[1:]),name)
                    found = True
                    break
            if not found:
                print(' '.join(inp[1:]),"unknown")
        else:
            print(' '.join(inp[1:]), "unknown")
