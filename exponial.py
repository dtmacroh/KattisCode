# Exponial
# Author:		Debbie Macrohon
# Description:	using recursion

vars = [int(i) for i in input().split(" ")]
n = vars[0]
m = vars[1]

def rec(num):
    if num==1:
        return num
    else:
        return num**rec(num-1)

print(rec(n)%m)