class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = w 

    # Either end-point of the edge
    def either(self):
        return v

    # Other endpoint 
    def other(self, vertex):
        if vertex == v:
            return w 
        else:
            return v

    # Compares edges by weight
    def compareTo(self, edge):
        if self.weight < edge.weight: # Smaller
            return -1
        elif self.weight > edge.weight: # Larger
            return 1 
        else:
            return 0 # Same weight