# primesieve
# Author:		Debbie Macrohon
# Description:	attempting to use sieve of eratosthenes for this solution


vars = [int(i) for i in input().split(" ")]
n = vars[0]
q = vars[1]

getPrimeCount(n)

for i in range(0,q):
    

def getPrimeCount(num):
    # 1. create a list of consecutive integers from 2 to n: (2,3.. n)
    # 2. let p=2, the first prime number
    # 3. starging from p^2, count up in increments of p and mark each of 
    # these numbers greater than or equal to p^2 itself in the list
    # 4. Find the first number greater than p in the list that is not marked. 
    # If there was no such number, stop. Otherwise let p now equal this number which is the next prime, and repeat from step 3.
