class Graph:
    def __init__(self, vertices, nodes):
        self.vertices = vertices # Number of nodes in the graph
        self.adjacent = {}
        # self.adjacent = {vertex:[] for vertex in range(1, self.vertices + 1)}

        for node in nodes:
            self.adjacent[node] = []

    def add_edge(self, u, v):
        # An undirected graph, so add vertices to each of their lists
        self.adjacent[u].append(v)

        # For a directed graph you can remove (or comment out) the line below
        self.adjacent[v].append(u)

    def print_graph(self):
        # print self.adjacent
        for key in self.adjacent:
           print str(key) + ' => ', 
           print self.adjacent[key]