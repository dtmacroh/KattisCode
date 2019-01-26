# primesieve
# Author:		Debbie Macrohon
# Description:	attempting to use sieve of eratosthenes for this solution


def getPrimeCount(num):
    p=2
    # 1. create a list of consecutive integers from 2 to n: (2,3.. n)
    # 2. let p=2, the first prime number
    # 3. starting from p^2, count up in increments of p and mark each of 
    # these numbers greater than or equal to p^2 itself in the list
    # 4. Find the first number greater than p in the list that is not marked. 
    # If there was no such number, stop. Otherwise let p now equal this number which is the next prime, and repeat from step 3.
    primeCount = 1
    while (p * p <=n):
        if (prime[p] ==1):
            for i in range (p*p, n+1, p):
                prime[i] = 0
        p+=1
     # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            primeCount+=1   
    return primeCount
vars = [int(i) for i in input().split(" ")]
n = vars[0]
q = vars[1]
prime = [1 for i in range(n+1)]
print(getPrimeCount(n))


