class IndexMinPriorityQueue:
    def __init__(self, maxN):
        if maxN >= 0:
            self.maxN = maxN # Maximum number of elements on PQ
            self.n = 0 # Number of elements on PQ
            self.keys = [''] * (self.maxN + 1) # keys[i] = priority of i
            self.pq = [0] * (self.maxN + 1) # Binary heap using 1-based indexing
            self.qp = [-1] * (self.maxN + 1) # inverse of pq - qp[pq[i]] = pq[qp[i]] = i

    # Returns True if this priority queue is empty
    def isEmpty(self):
        return self.n == 0

    # An index on this prirority queue?
    def contains(self, index):
        if self.validateIndex(index):
            return self.qp[index] != -1

    # Returns the number of keys on this priority queue 
    def size(self):
        return self.n 

    # Associates key with index 
    def insert(self, index, key):
        if self.validateIndex(index):
            if not self.contains(index):
                self.n += 1
                self.qp[index] = self.n
                self.pq[self.n] = index 
                self.keys[index] = key
                self.swim(self.n)

    # Returns an index associated with a minimum key
    def minIndex(self):
        if self.n > 0:
            return self.keys[self.pq[1]]

    # Removes a minimum key and returns its associated index 
    def delMin(self):
        if self.n > 0:
            min = self.pq[1]
            self.swap(1, self.n)
            self.n -= 1
            self.sink(1)

            if min == self.pq[(self.n + 1)]:
                self.qp[min] = -1 # delete 
                self.keys[min] = None # To help with garbage collection 
                self.pq[self.n + 1] = -1 # Not needed
                
                return min 

    # Returns the key associated with index 
    def keyOf(self, index):
        if self.validateIndex(index):
            if self.contains(index):
                return self.keys[index]

    # Change the key associated with index 
    def changeKey(self, index, key):
        if self.validateIndex(index):
            if self.contains(index):
                self.keys[index] = key
                self.swim(self.qp[index])
                self.sink(self.qp[index])

    # Decrease key associated with index 
    def decreaseKey(self, index, key):
        if self.validateIndex(index):
            if self.contains(index):
                if self.keys[index] > key:
                    self.keys[index] = key
                    self.swim(self.qp[index])

    # Increase the key associated with index
    def increaseKey(self, index, key):
        if self.validateIndex(index):
            if self.contains(index):
                if self.keys[index] < key:
                    self.keys[index] = key
                    self.swim(self.qp[index])

    # Remove key associated with index 
    def delete(self, index, key):
        if self.validateIndex(index):
            if self.contains(index):
                i = self.qp[index]                
                self.swap(i, self.n)
                self.n -= 1
                self.swim(i)
                self.sink(i)
                self.keys[index] = None
                self.qp[index] = -1

    # Find if an index is invalid 
    def validateIndex(self, index):
        if index < 0 or index >= self.maxN:
            return False

        return True

    # General helper functions 
    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def swap(self, i, j):
        temp = self.pq[i]

        self.pq[i] = self.pq[j]
        self.pq[j] = temp 

        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    # Heap helper functions 
    def swim(self, k):
        while k > 1 and self.greater(k/2, k):
            self.swap(k, k/2)
            k = k/2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k

            if j < self.n and self.greater(j, j+1):
                j += 1

            if not self.greater(k, j):
                break

            self.swap(k, j)
            k = j