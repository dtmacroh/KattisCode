# character development
# Author:		Debbie Macrohon
# Description:	2^n for all possible subsets within n. 
#               we subtract 1 for the single node case,
#               e.g. n=1, and subtract n for all single nodes 
#               thereafter.

nodes = int(input())
print((2**nodes)-nodes-1) 


