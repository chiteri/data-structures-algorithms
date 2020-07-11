from node import Node 

class Queue:
    # Create a queue
    def __init__(self):
        # Create an empty queue with an empty node
        self.first =  None
        self.last = None
        self.N = 0

    # Add items to the queue
    def enqueue(self, item):
        old_last = self.last # Save a link to the last node 
        self.last = Node(item) # Create a new node for the end
        self.last.next = None

        if self.isEmpty():
            # Special case for an empty queue
            self.first = self.last
        else: 
            old_last.next = self.last # Link new node to the end of the list

    # Remove and return item least recently enqueued
    def dequeue(self):
        # Identical to removing an item from a List's front 
        item = self.first.data 
        self.first = self.first.next 

        if self.isEmpty():
            # Special case for an empty queue
            self.last = None 

        return item

    # Is the queue empty 
    def isEmpty(self):
        return self.first is None

    # Return the number of items in the queue
    def size(self):
        return self.N