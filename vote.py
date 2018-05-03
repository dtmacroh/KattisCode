
rounds = int(input(""))

for i in range (0, rounds):
   
    sec_rounds = int(input(""))
    gndTotal = 0
    mostVote = 0
    candidate = 0
    nowinner = False
    for x in range (0, sec_rounds): 
        currVote = int(input(""))
        if mostVote < currVote:
            mostVote = currVote
            candidate = x+1
            nowinner = False
        elif mostVote == currVote:
            nowinner = True
           
        gndTotal = gndTotal + currVote
    
    if (nowinner):
        print('no winner')
    elif (mostVote/gndTotal >0.5):
        print("majority winner {}".format(candidate))
    elif  (mostVote/gndTotal <=0.5 and mostVote/gndTotal >0):
         print("minority winner {}".format(candidate))
  
       
    