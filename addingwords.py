#addingwords.py

try:
    d = {}
    while True:
        inp = input().split()

        if inp[0]=="clear":
            d.clear()
        if inp[0] =="def":
            d[inp[1]] = inp[2]
        if inp[0] == "calc":
            unknown = False
            eq = []
            for c in inp[1:-1]:
                if c in d:
                    eq.append(d[c])
                elif c in ("+", "-"):
                    eq.append(c)
                else:
                    unknown = True
            
            if unknown:
                print(" ".join(inp[1:]), "unknown")
            else:
                res = str(eval(''.join(eq)))
                found = False
                item = ''
                for name, val in d.items():
                    if res ==val:
                        found = True
                        item = name
                if found:
                    print(" ".join(inp[1:]),item)
                else:
                    print(" ".join(inp[1:]),"unknown")
         
except EOFError as e:
    pass