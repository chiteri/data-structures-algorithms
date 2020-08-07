from graph import Graph
from bfs import BreadthFirstPaths

if __name__ == '__main__':
    # edges = [['A', 'B'], ['B', 'C], ['C', 'D'], ['D', 'E'], ['F', 'C']] # ['B', 'C', 'D']
    edges = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D'], ['C', 'F'], ['F', 'G'], ['D', 'E']] # ['C', 'D', 'F']
    numNodes = 7 # 6 # 10
    numConnections =  7 # 5 # 13

    # nodes = [x for x in range(1, numNodes +1)]
    nodes = set([y for x in edges for y in x])

    network = Graph(numNodes, nodes)

    for edge in edges:
        network.add_edge(edge[0], edge[1])
        
    network.print_graph()

    bfs_client = BreadthFirstPaths(network)
    bfs_client.bfs('D')
    print bfs_client.edge_to