# Book implementation of a queue
# https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementingaQueueinPython.html

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

    def __str__(self): 
        if self.is_empty(): 
            return "[]"
        s = '['
        for item in self._items[:-1]:
            s += '{},'.format(item)
        s += '{}]'.format(self._items[-1])
        return(s) 