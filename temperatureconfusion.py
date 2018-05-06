# temperatureconfusion.py
from fractions import Fraction
a,b = [int(i) for i in input().split("/")]

newT = (Fraction(a,b) -32) * (Fraction(5,9))
frac = newT
print("{}/{}".format(frac.numerator, frac.denominator))



