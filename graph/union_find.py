# UnionFind: An abstraction for solving the dynamic connectivity problem
class UnionFind:
    # Initialize UnionFind data structure with N objects (0 to N - 1)
    def __init__(self, nodes):
        self.id = {} # Empty dictionary
        self.size = {}

        for node in nodes:
            self.id[node] = node # Set id of each object to itself
            self.size[node] = 1

    # Chase pointers until you reach their root
    def _root(self, i):
        while i != self.id[i]:
            # Make every other node point up to its grandparent (thereby halving path length)
            self.id[i] = self.id[self.id[i]] # Add some path compression to improve performance
            i = self.id[i]

        return i

    # Check if p and q have the same root 
    def connected(self, p, q):
        return self._root(p) == self._root(q)

    # Change root of p to point to root of q
    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if i == j:
            return 
 
        if self.size[i] < self.size[j]:
            self.id[i] = j # Link root of smaller tree to root of larger tree
            self.size[j] += self.size[i] # Update the size array
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

    # Component identifier for p (0 to N - 1)
    def find(self, p):
        pass 

    # Number of components 
    def count(self):
        pass 