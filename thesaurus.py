# thesaurus
# Author:		Debbie Macrohon
# Description:	


vars = [int(i) for i in input().split(" ")]
n = vars[0]
m = vars[1]
map = {}

phrase = input()
for i in range(m):
    thes = input().split(" ")
    key = thes[0]
    val = thes[1]
    map[key] = val

print(map)
# def findMin(newPhrase):
#     if len(newPhrase)<len(phrase):
#         return newPhrase
#     else:
#         return min(findMin(),findMin())
