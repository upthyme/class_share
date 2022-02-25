class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def setNext(self,newnext):
        self.next = newnext
        
    def getNext(self):
        return self.next

class UnorderedList:
    def __init__(self):
        self.head = None
           
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
   
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count   
            
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(100)
lengthList = mylist.length()
