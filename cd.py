def main():
    run = True
    while run:
        jack, jill = [int(i) for i in input("").split()]
        if jack==0 and jill==0:
            run = False
            break
        jackList = jack*[0]
        common = 0
        for ja in range (0, jack):
            jackList[ja] = int(input(""))
        jackList.sort()
        for ji in range (0, jill):
            comp = int(input(""))
            if binarySearch(jackList, comp):
                common = common+1
            elif common ==jack:
                break
        print("{}".format(common))

#binary search algorithm from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
main()