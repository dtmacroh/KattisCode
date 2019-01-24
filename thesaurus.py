# thesaurus
# Author:		Debbie Macrohon
# Description:	

def findMin(newPhraseFull,c):
    newPhraseArray = newPhraseFull.split(" ")

   
    if newPhraseArray[c] in thesaurus and c >=0:
        newPhraseArray[c] = thesaurus[newPhraseArray[c]]
        newPhraseAfter = ''.join(newPhraseArray)
        
        return newPhraseAfter
    return min(len(findMin(newPhraseFull,c-1)),len(findMin(newPhraseAfter,c-1)))

vars = [int(i) for i in input().split(" ")]
n = vars[0]
m = vars[1]
thesaurus = {}

phrase = input()
for i in range(m):
    thes = input().split(" ")
    key = thes[0]
    val = thes[1]
    thesaurus[key] = val

phrasewords = phrase.split()
print(thesaurus)
leastCount = len(''.join(phrasewords))
for i in phrasewords:
    res = findMin(phrase,len(phrasewords)-1)
    if leastCount>len(res):
        leastCount = len(res)
print(res,leastCount)