class DirectedEdge:
    # Weighted edge v -> w
    def __init__(self, v, w, weigh):
        self.v = v
        self.w = w
        self.weigh = weigh

    # Vertex v 
    def origin(self):
        return self.v

    # Vertex w
    def to(self):
        return self.w

    # Weight of this edge 
    def weight(self):
        return self.weigh