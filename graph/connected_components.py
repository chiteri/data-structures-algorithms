from graph import Graph #,Vertex  

class ConnectedComponents:
    def __init__(self, graph):
        self.marked = {}

        self.component = {}

        # Initialize all the marked components to 0, the first connected component
        self.count = 0

        # Init all vertices in graph as not marked
        for vertex in graph.adjacent:
            self.marked[vertex] = False
            self.component[vertex] = self.count            

        for vertex in graph.adjacent:
            if not self.marked[vertex]:
                # Run dfs from one vertex in each component
                self.dfs(graph, vertex)
                self.count += 1      

    # Find if two vertices, v and w are connected
    def connected(self, v, w):
        # Whether the two vertices are in the same connected component
        return self.component[v] == self.component[w]

    # Number of connected components
    def count(self):
        return self.count

    # Component identifier for v
    def id(self, v):
        return self.component[v]

    def dfs(self, g, v):
        self.marked[v] = True

        # All neighbours discovered in the same dfs call have the same connected component id
        self.component[v] = self.count 

        for neighbour in g.adjacent[v]:
            # print neighbour 
            if not self.marked[neighbour]:
                self.dfs(g, neighbour)
