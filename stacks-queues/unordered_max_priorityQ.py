class UnorderedMaxPQ:
    def __init__(self, capacity):
        self.N = 0 # Number of elements in PQ, empty
        self.pq = [0] * capacity

    def isEmpty(self):
        return self.N == 0

    def insert(self, x):
        self.pq[self.N] = x 
        self.N += 1

    def delMax(self):
        max = 0 

        for i in range(self.N):
            if self.pq[max] < self.pq[i]:
                max = i 

        # Exchange max and the last item on the list 
        self.swap(self.pq, max, self.N-1)

        self.N -= 1 # Reduce the size of list 

        return self.pq[self.N]

    # Swap two elements in a list or an array 
    def swap(self, haystack, i, j):
        temp = haystack[i]
        haystack[i] = haystack[j]
        haystack[j] = temp