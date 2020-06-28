from ..list.list import List

# This is an improvement of the StrawmanStack implementation with 
# the following perfomance specification 
# 1) All operations take constant time
# 2) Memory use is linear in the size of the collection, when it is non-empty
# 3) No limits within the code on the collection size 
class Stack:
    # Create an empty stack
    def __init__(self):
        self.items = List()
        self.capacity = 0 

    # Insert a new item into stack
    def push(self, item):
        self.items.push(item)
        self.capacity += 1

    # Remove and return the item most recently added
    def pop(self):
        self.capacity -= 1 
        return self.items.pop()

    # Is the stack empty?
    def isEmpty(self):
        return self.first is None

    # Number of items in the stack
    def size(self):
        return self.capacity