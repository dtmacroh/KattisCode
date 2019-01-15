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
        # z = rec(num-1)%m
        # return (num**(z+m))%m
        return (num**rec(num-1))%m

print(rec(n))