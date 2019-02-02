# autori
# Author:		Debbie Macrohon
# Description:	split string to get initial first char of each word

var = input().split('-')
mainstring = ""
for c in var:
    mainstring +=c[0] 
print(mainstring)