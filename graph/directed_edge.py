class DirectedEdge:
    # Weighted edge v -> w
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
        pass

    # Vertex v 
    def from(self):
        return self.v

    # Vertex w
    def to(self):
        return self.w

    # Weight of this edge 
    def weight(self):
        return self.weight