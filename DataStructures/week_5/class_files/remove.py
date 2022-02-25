class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def setNext(self,newnext):
        self.next = newnext
        
    def getNext(self):
        return self.next
        
    def getData(self):
        return self.data

class UnorderedList:
    def __init__(self):
        self.head = None
           
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(100)
mylist.remove(77)
