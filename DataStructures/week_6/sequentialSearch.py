import sys 

def sequentialSearch(alist, item):
    """ Goes through and finds an item in a list
        Return True/False and position of item in list when found
    """
    pos = 0
    found = False
    
    while pos < len(alist):
        if alist[pos] == item:
            found = True
            return (found, pos)
        else:
            pos = pos+1 

    return (found, None)

# driver?
if __name__ == "__main__": 
    list = [1,2,3,4,5]
    print(sequentialSearch(list, 3)) # True, 2
    print(sequentialSearch(list, 6)) # False, None

    # Get user input
    inputcol = 92 
    outputcol = 35
    sys.stdout.write('\033[' + str(inputcol)+ 'm ') # ASCII escape code for color
    
    userlist = [] 
    inputlist = input("List: ").split()
    for i in inputlist:
        userlist.append(i)
    
    sys.stdout.write('\033[' + str(inputcol)+ 'm ')
    item = input("Item: ")
    sys.stdout.write('\033[' + str(outputcol)+ 'm ' )
    print(sequentialSearch(userlist, item))
    sys.stdout.write('\033[' + str(0)+ 'm ' ) # reset the terminal 

    