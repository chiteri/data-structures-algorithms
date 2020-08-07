from graph import Graph
from connected_components import ConnectedComponents

def essentialNode(g1, g2):
    cc_before = ConnectedComponents(g1)

    cc_after = ConnectedComponents(g2)

    # Make sure that before you had one connected component which gets split 
    # by removal of node (2 or more components)
    return len( set( cc_before.component.values() ) ) == 1 and \
        len( set( cc_after.component.values() ) ) >= 2

if __name__ == '__main__':
    # edges = [['A', 'B'], ['B', 'C], ['C', 'D'], ['D', 'E'], ['F', 'C']] # ['B', 'C', 'D']
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D'], ['C', 'F'], ['F', 'G'], ['D', 'E']] # ['C', 'D', 'F']
    numNodes = 7 # 6 # 10
    numConnections =  7 # 5 # 13

    nodes = set([y for x in edges for y in x])

    network = Graph(numNodes, nodes)

    for edge in edges:
        network.add_edge(edge[0], edge[1])
        
    network.print_graph()
    
    essential_nodes = []
    
    for node in set([y for x in edges for y in x]):
        # Exclude a vertice from the graph 
        less_nodes = set([y for x in edges for y in x])
        less_nodes.remove(node)
        
        # Build another network with fewer nodes 
        smaller_network = Graph(numNodes - 1, less_nodes)

        # Add the edges but skip those with excluded node
        for edge in edges:
            if edge[0] is not node and edge[1] is not node:
                smaller_network.add_edge(edge[0], edge[1])

        if essentialNode(network, smaller_network):
            essential_nodes.append(node)      

    print essential_nodes
