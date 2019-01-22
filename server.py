# Server
# Author:		Debbie Macrohon
# Description:	iteratively deduct times until total time - cumulative(times) become negative

vars = [int(i) for i in input().split(" ")]
n = vars[0]
T = vars[1]
times = [int(i) for i in input().split(" ")]

totTime = T
counter = 0
for i in range(len(times)):
    if times[i]<=totTime:
        totTime -= times[i]
        if totTime >=0:
            counter+=1

print(counter)