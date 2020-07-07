from binary_heap import BinaryHeap

if __name__ == "__main__":
    items = [3, 4, 10, 1, 6, 5]
    # items = ['T', 'P', 'R', 'N', 'H', 'O', 'A', 'E', 'I', 'G']

    priorityQueue = BinaryHeap(len(items)) 

    for item in items:
        priorityQueue.insert(item)

    print "BEFORE: ", 
    for i in range(1, len(priorityQueue.pq)):
        print priorityQueue.pq[i], 

    print 
    print "DELETED: " +str(priorityQueue.delMax())  

    print "AFTER: ", 
    for i in range(1, priorityQueue.N+1):
        print priorityQueue.pq[i],

    print 
    print "DELETED: " +str(priorityQueue.delMax())  

    print "AFTER: ", 
    for i in range(1, priorityQueue.N+1):
        print priorityQueue.pq[i],
