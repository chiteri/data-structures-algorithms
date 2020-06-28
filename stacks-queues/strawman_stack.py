# Fixed capacity collection taht behaves like a Stack if the data fits
class StrawmanStack:
    # Create an empty stack
    def __init__(self, max):
        self.items = ["0"] * max
        self.capacity = 0 

    # Insert a new item into stack
    def push(self, item):
        self.items[self.capacity] = item
        self.capacity += 1

    # Remove and return the item most recently added
    def pop(self):
        self.capacity -= 1 # Decrement first 
        return self.items[self.capacity]

    # Is the stack empty?
    def isEmpty(self):
        return self.capacity is 0

    # Number of items in the stack
    def size(self):
        self.capacity