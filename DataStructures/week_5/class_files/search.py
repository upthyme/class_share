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
        
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
   
   
            
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(100)
found = mylist.search(77)
