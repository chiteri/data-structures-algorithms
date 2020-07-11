from node import Node 

# Extend the Node class from the regular Binary search tree
class RedBlackBSTNode(Node):
    # Colours for the links to nodes subtrees
    BLACK =  False 
    RED =  True
    def __init__(self, key, value, colour):
        Node.__init__(self, key, value)

        # Assign color to the node's parent link
        self.color = colour