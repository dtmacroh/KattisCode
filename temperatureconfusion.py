# temperatureconfusion.py
from fractions import Fraction
from fractions import gcd
a,b = [int(i) for i in input().split("/")]
print(a,b)
newT = (Fraction(a,b) -32) * (Fraction(5,9))
frac = newT
print("{}/{}".format(frac.numerator, frac.denominator))



