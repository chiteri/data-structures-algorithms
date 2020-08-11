class DirectedDFS:
    # Constructor marks vertices reachable from a vertex v
    def __init__(self, graph, v):
        self.marked = {} # Keeps track of whether a vertex has been visited

        for vertex in graph.adjacent:
            self.marked[vertex] = False

        # Perform a dfs 
        self.dfs(graph, v)

    # Recursive dfs method
    def dfs(self, graph, node):
        self.marked[node] = True

        for vertex in graph.adjacent[node]:
            if not self.marked[vertex]:
                self.dfs(graph, vertex)

    # A client that asks whether any node is reachable from a vertex v
    def visited(self, vertex):
        return self.marked[vertex]
