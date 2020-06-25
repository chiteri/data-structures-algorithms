from graph import Graph

class BreadthFirstPaths:
    def __init__(self, graph):
        self.graph = graph
        self.marked = {}  
        self.edge_to = {} 

        for vertex in graph.adjacent:
            self.marked[vertex] = False
            self.edge_to[vertex] = 0

    def bfs(self, vertex):
        q = [] # A list to hold nodes adjacent to each vertex
        q.append(vertex)

        while len(q) > 0:
            node = q.pop() 

            for adjacent in self.graph.adjacent[node]:
                if not self.marked[adjacent]:
                    q.append(adjacent)
                    self.marked[adjacent] = True
                    self.edge_to[adjacent] = node 