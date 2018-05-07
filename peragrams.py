#peragrams.py

import string
d = dict.fromkeys(string.ascii_lowercase, 0) #put every letter of alphabet into a dictionary

for l in input():
    d[l]+=1

sum = 0
for c in d:
    if d[c]% 2 ==1:
        sum +=1
print(max(0,sum-1))