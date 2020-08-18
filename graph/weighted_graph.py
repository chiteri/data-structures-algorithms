class WeightedGraph:
    # Create an empty graph with V vertices
    def __init__(self, nodes):
        self.V = len(nodes) # Number of vertices
        self.adjacent = {} # Adjacency list

        for vertex in nodes:
            self.adjacent[vertex] = []

    # Add weighted edge to this graph 
    def addEdge(self, e):
        v = e.either()
        w = e.other(v)

        # Add edge to both adjacency lists 
        self.adjacent[v].append(e)
        self.adjacent[w].append(e)

    # Edges incident to v 
    def adj(self, v):
        return self.adjacent[v]