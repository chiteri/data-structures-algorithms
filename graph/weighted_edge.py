class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    # Either end-point of the edge
    def either(self):
        return self.v

    # Other endpoint 
    def other(self, vertex):
        if self.v == vertex:
            return self.w 
        else:
            return self.v

    # Compares edges by weight
    def compareTo(self, edge):
        if self.weight < edge.weight: # Smaller
            return -1
        elif self.weight > edge.weight: # Larger
            return 1 
        else:
            return 0 # Same weight
