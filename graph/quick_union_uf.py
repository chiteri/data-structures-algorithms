# QuickUnion: An abstraction for solving the dynamic connectivity problem
class QuickUnionUF:
    def __init__(self, nodes):
        self.id = {} # Empty dictionary

        for node in nodes:
            self.id[node] = node # Set id of each object to itself
    
    # Chase pointers until you reach their root
    def _root(self, i):
        while i != self.id[i]:
            i = self.id[i]

        return i

    # Check if p and q have the same root 
    def connected(self, p, q):
        return self._root(p) == self._root(q)

    # Change root of p to point to root of q
    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        self.id[i] = j