class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
           
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
      
            
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)