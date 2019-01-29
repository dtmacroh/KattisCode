# Exponial
# Author:		Debbie Macrohon
# Description:	using modular exponentiation and euler's totient
#               
vars = [int(i) for i in input().split(" ")]
n = vars[0]
m = vars[1]

def rec(num):
    if num==1:
        return num
    elif num <=5:
        z = rec(num-1)%m
        # return (num**(z+m))%m
        return (num**z)%m
    else:
        z =(num**(rec(num-1)))%phi(m)
        return z
        # return (num**(z+m))%m
        #print(phi(m))
        #return (num**(phi(m)+z))%m

def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
  
# A simple method to evaluate 
# Euler Totient Function 
def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

if (n > 5):
    z = rec(n)
    #print(z)
    print((n**(phi(m)+z))%m)
else:
    print(rec(n))