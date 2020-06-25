from graph import Graph
from connected_components import ConnectedComponents

def criticalNode(g1, g2):
    cc_before = ConnectedComponents(g1)

    cc_after = ConnectedComponents(g2)

    # Make sure that before you had one connected component which gets split 
    # by removal of node (2 or more components)
    return len( set( cc_before.component.values() ) ) == 1 and \
        len( set( cc_after.component.values() ) ) >= 2

if __name__ == '__main__':
    # links = [[1, 2], [2, 3], [3, 4], [4, 5], [6, 3]] # [2, 3, 4]
    links = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]] # [3, 4, 6]
    numRouters = 7 # 6 # 10
    numLinks =  7 # 5 # 13

    nodes = [x for x in range(1, numRouters +1)]

    network = Graph(numRouters, nodes)

    for link in links:
        network.add_edge(link[0], link[1])
        
    network.print_graph()
    
    critical_nodes = []
    
    for router in range(1, network.vertices +1):
        # Exclude a vertice from the graph 
        less_nodes = [x for x in range(1, numRouters +1)] 
        less_nodes.remove(router)
        
        # Build another network with fewer nodes 
        smaller_network = Graph(numRouters - 1, less_nodes)

        # Add the edges but skip those with excluded node
        for link in links:
            if link[0] is not router and link[1] is not router:
                smaller_network.add_edge(link[0], link[1])

        # smaller_network.print_graph()

        if criticalNode(network, smaller_network):
            critical_nodes.append(router)      

    print critical_nodes
