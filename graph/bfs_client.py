from graph import Graph
from bfs import BreadthFirstPaths

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

    bfs_client = BreadthFirstPaths(network)
    bfs_client.bfs(4)
    print bfs_client.edge_to