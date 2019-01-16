# onechicken
# Author:		Debbie Macrohon
# Description:	
vars = [int(i) for i in input().split(" ")]
people = vars[0]
chicken = vars[1]

res = people-chicken 

if res == 1:
    print("Dr. Chaz needs {} more piece of chicken!".format(abs(res)))
elif res == -1:
    print ("Dr. Chaz will have {} piece of chicken left over!".format(abs(res)))
elif res < 0:
    print ("Dr. Chaz will have {} pieces of chicken left over!".format(abs(res)))
else:
    print("Dr. Chaz needs {} more pieces of chicken!".format(abs(res)))