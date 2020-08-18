# Kruskal's algorithm (1956) is a special case of the greedy MST algorithm
from index_minPQ import IndexMinPriorityQueue
from union_find import UnionFind

class KruskalMinimumSpanningTree:
    def __init__(self, graph):
        self.graph = graph
        self.pq = IndexMinPriorityQueue(graph.V)
        self.mst = [] # Empty list of edges

        # Build a priority queue
        for edge in graph.adjacent:
            # for edge in graph.adj(edges):
            self.pq.insert(edge, graph.adj(edge))

        union_find = UnionFind(graph.adjacent.keys())

        while not self.pq.isEmpty() and len(self.mst) < graph.V - 1:
            edges = self.pq.minIndex()
            self.pq.delMin()

            # Greedily add edges to MST
            for edge in edges:
                v = edge.either()
                w = edge.other(v)

                # Edge v-w does not create a cycle 
                if not union_find.connected(v, w):
                    union_find.union(v, w) # Merge sets
                    self.mst.append(edge) # Add edge to MST

    # Edges in MST
    def edges(self):
        return self.mst

    # Weight of MST
    def weight(self):
        pass