from kruskal_mst import KruskalMinimumSpanningTree
from weighted_graph import WeightedGraph
from weighted_edge import Edge

if __name__ == "__main__":
    edges = [[0, 7, 0.16], [2, 3, 0.17], [1, 7, 0.19], [0, 2, 0.26], [5, 7, 0.28], 
    [1, 3, 0.29], [1, 5, 0.32], [2, 7, 0.34], [4, 5, 0.35], [1, 2, 0.36], [4, 7, 0.37], 
    [0, 4, 0.38], [6, 2, 0.4], [3, 6, 0.52], [6, 0, 0.58], [6, 4, 0.93]]

    nodes = set()

    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])

    routes = WeightedGraph(nodes)

    for edge in edges:
        e = Edge(edge[0], edge[1], float(edge[2]))
        routes.addEdge(e)

    # source = int(sys.argv[1]) # Collect the destination from the command line
    minimum_spanning_tree = KruskalMinimumSpanningTree(routes)
    
    print "Minimum spanning tree: "
    for edge in minimum_spanning_tree.edges():
        # for edge in edges:
        print str(edge.v) +" => "+str(edge.w)+", Weight: (" + str(edge.weight)+")"