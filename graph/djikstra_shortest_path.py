# from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge # EdgeWeightedDigraph
from index_minPQ import IndexMinPriorityQueue

class DjikstraSP:
    def __init__(self, graph, source):
        self.edge_to = {} # edge_v[v] = last edge on shortest s->v path
        self.dist_to = {} # dist_to[v] = distance  of shortest s->v path 
        self.pq = IndexMinPriorityQueue(graph.V)

        for vertex in graph.adjacent:
            self.dist_to[vertex] = float('inf') # Positive infinity
            self.edge_to[vertex] = None # DirectedEdge(graph.V)
        self.dist_to[source] = 0.0 # Beginning vertex

        self.pq.insert(source, self.dist_to[source])

        # Relax vertices in order of distance from source
        while not self.pq.isEmpty():
            vertex = self.pq.delMin()

            for directed_edge in graph.adjacent[vertex]:
                self.relax(directed_edge)

    def relax(self, directed_edge):
        v = directed_edge.origin()
        w = directed_edge.to()

        if self.dist_to[w] > self.dist_to[v] + directed_edge.weight():
            self.dist_to[w] = self.dist_to[v] + directed_edge.weight()
            self.edge_to[w] = directed_edge

            # Update the priority queue
            if self.pq.contains(w):
                self.pq.decreaseKey(w, self.dist_to[w])
            else:
                self.pq.insert(w, self.dist_to[w])

    def distTo(self, vertex):
        return self.dist_to[vertex]

    # Return True if there is a path from source to vertex
    def hasPathTo(self, vertex):
        return self.dist_to[vertex] < float('inf')

    # Returns a shortest path from source vertex (s) to vertex (v)
    def pathTo(self, vertex):
        if not self.hasPathTo(vertex):
            return None 
        
        path = [] # stack of directed edges

        edge = self.edge_to[vertex]

        while edge is not None:
            path.append(edge)
            edge = self.edge_to[edge.origin()]

        return path 