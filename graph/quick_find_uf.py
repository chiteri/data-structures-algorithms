# QuickFind: An abstraction for solving the dynamic connectivity problem
class QuickFindUF:
    def __init__(self, nodes):
        self.id = {} # Empty dictionary

        for node in nodes:
            self.id[node] = node # Set id of each object to itself

    # Check whether p and q are in the same connected component 
    def connected(self, p, q):
        return self.id[p] == self.id[q]

    # Change root of p to point to root of qd
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        # Change all entries with id[p] to id[q]
        for key in self.id:
            if self.id[key] == pid:
                self.id[key] = qid 
