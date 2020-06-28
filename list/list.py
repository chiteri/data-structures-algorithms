class Node:    
    def __init__(self, item):
        self.data = item
        self.next = None

class List:
    def __init__(self):
        self.head = None

    # Remove and return first item
    def pop(self):
        item = self.head.data 

        # Advance the head by one item
        self.head = self.head.next 
        return item

    # Add an item to the beginning of the list 
    def push(self, item):
        second = self.head
        self.head = Node(item)
        self.head.next = second 

    # Go through every node in the list 
    def traverse(self):
        current = self.head 

        while current is not None:
            print str(current.data),
            
            if current.next is not None:
                print "->",

            current = current.next 