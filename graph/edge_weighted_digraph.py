class EdgeWeightedDigraph:
    def __init__(self, nodes):
        self.V = len(nodes) # Number of vertices
        self.adjacent = {} # Adjacency list

        for node in nodes:
            self.adjacent[node] = []

    def addEdge(self, e):
        # Add edge e - v -> w only to v's adjacency list
        v = e.from()
        self.adjacent[v].add(e)

    def adjacent(self, v):
        return self.adjacent[v]