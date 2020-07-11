from red_black_bst_node import RedBlackBSTNode

# The left-leaning Red-Black binary search tree is an implementation   
# of 2-3 search trees for representing symbol table operations efficiently
class RedBlackTree:
    def __init__(self):
        self.root = None

    def get(self, key):
        x = self.root 

        while x is not None:
            if key < x.key:
                # Less, look to the left subtree
                x = x.left 
            elif key > x.key:
                # Greater, look to the right subtree
                x = x.right 
            else:
                # key found 
                return x.val 

        return None # Key not found, worst case

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, value):
        self.root = self.insert(self.root, key, value)

    # A helper for the PUT method
    def insert(self, h, key, value):
        if h is None:
            return RedBlackBSTNode(key, value, RedBlackBSTNode.RED)

        if key < h.key:
            # Lesser value, goes to the left subtree
            h.left = self.insert(h.left, key, value)
        elif key > h.key:
            # Larger value, goes to the right subtree
            h.right = self.insert(h.right, key, value)
        else:
            # Value found in current node
            h.val = val 

        # Ensure that the new node is leaning to the left and there are no double links
        if self.isRed(h.right) and not self.isRed(h.left):
            # Lean the subtree to the left
            h = self.rotateLeft(h)
        if self.isRed(h.left) and self.isRed(h.left.left):
            # Balance a 4-node subtree
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.flipColors(h)

        return h

    def isRed(self, node):
        if node is None:
            return False # Null links are black
        return node.color == RedBlackBSTNode.RED

    # Orient (temporarily) a right-leaning red link to lean left
    # while maintaining symmetric order and perfect black balance
    def rotateLeft(self, h):
        if self.isRed(h.right):
            x = h.right # The new root of the tree node
            h.right = x.left 
            x.left = h 
            x.color = h.color 
            h.color = RedBlackBSTNode.RED 
            return x  

    # Orient a left-leaning red link to (temporarily) lean right
    # while maintaining symmetric order and perfect black balance
    def rotateRight(self, h):
        if self.isRed(h.left): 
            x = h.left 
            h.left = x.right 
            x.right = h 
            x.color = h.color 
            h.color = RedBlackBSTNode.RED
            return x

    # Re-color to split a (temporary) 4-node 
    # while maintaining symmetric order and perfect black balance
    def flipColors(self, h):
        if not self.isRed(h) and self.isRed(h.left) and self.isRed(h.right):
            h.color = RedBlackBSTNode.RED 
            h.left.color = RedBlackBSTNode.BLACK 
            h.right.color = RedBlackBSTNode.BLACK

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

    def keys(self):
        queue = [] # A list to hold keys
        self.inorder(self.root, queue)
        return queue
