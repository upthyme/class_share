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

#alist = [ 1,5,7,9,10,12,15,17,18,20,21,22,25,32,35,40]
#print (binarySearch(alist,21) )

alist = [ 2,7,11,15,20,21,27,33 ]
print (binarySearch(alist,27) )
