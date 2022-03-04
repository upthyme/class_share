''' 
Using a stack to reverse text in a file.
Notes: 
    - See pull_text.py for the text we are reversing and the method of writing
    - https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python 
''' 
# TODO: figure out how to correctly use __init__.py to import python classes 
import os.path, time, platform  
from pull_text import write_to_file 
#import ../DataStructures/week_3/Stack.py # DataStructures/week_3/Stack.py 
class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

    def __str__(self):
        """ Prints the stack string representation (e.g print(browserhistory))
        """
        if self.is_empty():
            return("[]")
        s = "["
        s += ", ".join(self._items)
        s += "]"
        return(s)

if __name__ == "__main__":
    print("Start")
    directory = os.path.dirname(__file__) # place result in directory where script lives
    filename = "davidfosterwallace"
    if platform.system() == 'Windows':
        separator = "\\"
    separator = "/" 
    filepath = (separator.join([directory,filename]))
    if os.path.exists(filepath):
        print("Using stack on file {}".format(filepath))
        full_of_chars = Stack()
        reversedtext = ""
        with open(filepath, 'r') as f:
            timestart = time.time() # time the pushing 
            for char in f.read():
                full_of_chars.push(char) # push all the characters onto the stack
            timestop = time.time() 
        print('''
        Stack after pushing
        Empty: {}
        Size: {} 
        Time: {}
        '''.format(full_of_chars.is_empty(), full_of_chars.size(), timestop - timestart)) 
        timestart = time.time() # time the popping
        for char in range(full_of_chars.size()):
            reversedtext += full_of_chars.pop() # popping off the list
        timestop = time.time() 
        print('''
        Stack after popping
        Empty: {}
        Size: {}
        Time: {} 
        '''.format(full_of_chars.is_empty(), full_of_chars.size(), timestop - timestart))     
        write_to_file("{}_reversed".format(filename), reversedtext)
    else: 
        print("No file found")

    print("End")
