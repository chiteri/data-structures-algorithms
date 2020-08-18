from union_find import UnionFind

if __name__ == "__main__":
    connections = [[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [8, 9], \
        [5, 0], [7, 2], [6, 1], [1, 0], [6, 7]]

    nodes = set([node for links in connections for node in links])

    union_find = UnionFind(nodes)

    for link in connections:
        p = link[0]
        q = link[1]

        if not union_find.connected(p, q):
            union_find.union(p, q)
            print str(p) + " " + str(q)

    print union_find.connected(0, 1) # (0, 8)