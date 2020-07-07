# A binary heap used to implement all the operations of a priority queue quickly
class BinaryHeap:
    #
    def __init__(self, capacity):
        self.N = 0 # Number of elements in PQ, empty
        self.pq = [0] * (capacity + 1) # An empty list with N + 1 elements, position 0 is unused

    # Insert a new element into a heap
    def insert(self, x):
        self.N += 1
        self.pq[self.N] = x
        self.swim(self.N) # Maitain the heap order

    # Exchange key  in child with key in parent
    def swim(self, k):
        # Check after the first element
        while k > 1 and self.less(k/2, k):
            self.swap(k, k/2) 
            
            # Repeat until heap order is restored
            k = k/2 
    
    # Parent key is smaller than the child's (or both children's), 
    # Exchange key in parent with key in larger child 
    def sink(self, k):
        while 2 * k <= self.N:
            # Children of node at k are 2k and 2k + 1
            j = 2 * k

            if j < self.N and self.less(j, j+1):
                j += 1

            if not self.less(k, j):
                break

            self.swap(k, j)

            k = j

    def delMax(self):
        # Exchange root with node at end then sink it down
        max = self.pq[1] # First element (root) is always largest
        self.swap(1, self.N) # Exchange root with last item
        self.N -= 1 # Reduce length of priority queue
        self.sink(1) # Find if root is smaller than its children
        self.pq[self.N + 1] = None # Prevent loitering by Null-ing vacated position

        return max

    # Swap two elements in a list or an array 
    def swap(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    # Find if child's key is larger than its parent's key
    def less(self, parent, child):
        return self.pq[parent] < self.pq[child]

    # 
    def isEmpty(self):
        return self.N == 0