
rounds = int(input(""))

for i in range (0, rounds):
    setPlace = set()
    sec_rounds = int(input(""))
    for x in range (0, sec_rounds): 
        setPlace.add(input(""))
    print(len(setPlace))

