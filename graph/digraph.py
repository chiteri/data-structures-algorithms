class Graph:
    def __init__(self, vertices, nodes):
        self.vertices = vertices # Number of nodes in the graph
        self.adjacent = {} # Adjacency list for each vertex

        for vertex in nodes:
            self.adjacent[vertex] = []

    def add_edge(self, u, v):
        # A directed graph, so add one-way edges their lists
        self.adjacent[u].append(v)

    def print_graph(self):
        for vertex in self.adjacent:
           print str(vertex) + ' => ', 
           print self.adjacent[vertex]
