class Graph:
    def __init__(self, vertices, nodes):
        self.vertices = vertices # Number of nodes in the graph
        self.adjacent = {} # Adjacency list for each vertex
        # self.adjacent = {vertex:[] for vertex in range(1, self.vertices + 1)}

        for vertex in nodes:
            self.adjacent[vertex] = []

    def add_edge(self, u, v):
        # An undirected graph, so add vertices to each of their lists
        self.adjacent[u].append(v)

        # For a directed graph you can remove (or comment out) the line below
        self.adjacent[v].append(u)

    def print_graph(self):
        # print self.adjacent
        for vertex in self.adjacent:
           print str(vertex) + ' => ', 
           print self.adjacent[vertex]
