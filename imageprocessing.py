# imageprocessing
# Author:		Debbie Macrohon
# Description:	

vars = [int(i) for i in input().split(" ")]
heightImage = vars[0]
widthImage = vars[1]
heightKer = vars[2]
widthKer = vars[3]

imageArray = [[0 for x in range(widthImage)] for y in range(heightImage)] 
kerArray = [[0 for x in range(widthKer)] for y in range(heightKer)] 

for h in (heightImage):
    tempImage = [int{i) for i in input().split(" ")]
    for t in (tempImage):
        imageArray[h][t] = tempImage[t]

for r in (heightKer):
    tempKernel = [int(i) for i in input().split(" ")]
    for k in (tempKernel):
        kerArray[r][k] = tempKernel[k]



