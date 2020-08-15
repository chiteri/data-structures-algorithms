import sys
from djikstra_shortest_path import DjikstraSP
from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge
from djikstra_shortest_path import DjikstraSP

if __name__ == "__main__":
    edges = [[0, 1, 5.0], [0, 4, 9.0], [0, 7, 8.0], [1, 2, 12.0], [1, 3, 15.0], 
    [1, 7, 4.0], [2, 3, 3.0], [2, 6, 11.0], [3, 6, 9.0], [4, 5, 4.0], [4, 6, 20.0], 
    [4, 7, 5.0], [5, 2, 1.0], [5, 6, 13.0], [7, 5, 6.0], [7, 2, 7.0]]

    nodes = set()

    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])

    routes = EdgeWeightedDigraph(nodes)

    for edge in edges:
        e = DirectedEdge(edge[0], edge[1], float(edge[2]))
        routes.addEdge(e)

    source = int(sys.argv[1]) # Collect the destination from the command line
    optimal_routes = DjikstraSP(routes, source)
    
    print "ORIGIN: "+str(source)
    for vertex in routes.adjacent:
        if optimal_routes.hasPathTo(vertex):
            print "ROUTE: " + str(source) + " to " + str(vertex) + \
                ", Dist.:(" + str(optimal_routes.distTo(vertex)) + ")"

        # print optimal_routes.pathTo(vertex)
            paths = optimal_routes.pathTo(vertex)
            print "Shortest path: ", 
            while len(paths) > 0:
                directed_edge = paths.pop()
                print str(directed_edge.origin()) + " => "+ str(directed_edge.to()), 
                print " ", 

            print
