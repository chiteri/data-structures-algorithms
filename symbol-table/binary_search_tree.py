# A binary search tree has been chosen to implement a symbol table 
# (or an associative array) with the following design goals in mid
# 1) Order of growth of running time for put(), get() and contains() is logarithmic
# 2) Memory usage is linear in the size of the collection, when it is non-empty
# 3) No limits within the code on the collection size 
from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.insert(self.root, key, value) 

    def get(self, key):
        return self.search(self.root, key) 

    def contains(self, key):
        return self.get(key) is not None

    def isEmpty(self):
        return self.root is None

    def keys(self):
        queue = [] # A list to hold keys
        self.inorder(self.root, queue)
        return queue

    #  A helper for the GET method 
    def search(self, node, key):
        if node is None:
            return None # Empty tree
        if key < node.key:
            # Recursively check the left subtree
            return self.search(node.left, key)
        elif key > node.key:
            # Recursively check the right subtree
            return self.search(node.right, key)
        else:
            # Value has been found
            return node.value

    # A helper for the PUT method 
    def insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self.insert(node.left, key, value)
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
        else:
            node.value = value

        return node

    # A helper for the KEYS method
    def inorder(self, node, queue):
        if node is None:
            return
        
        # Visit left subtree with lower values recursively
        self.inorder(node.left, queue)

        # Add root since it has the median value 
        queue.append(node.key)

        # Visit right subtree with higher values recursively
        self.inorder(node.right, queue)