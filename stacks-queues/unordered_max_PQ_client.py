from unordered_max_priorityQ import UnorderedMaxPQ

if __name__ == "__main__":
    numbers = [3, 4, 10, 1, 6, 5]

    priorityQueue = UnorderedMaxPQ(len(numbers))

    for number in numbers:
        priorityQueue.insert(number)

    print "BEFORE: ", 
    for i in range(0, priorityQueue.N):
        print priorityQueue.pq[i], 

    print 
    print "DELETED: " +str(priorityQueue.delMax())  

    print "AFTER: ", 
    for i in range(0, priorityQueue.N):
        print priorityQueue.pq[i],

    print 
    print "DELETED: " +str(priorityQueue.delMax())  

    print "AFTER: ", 
    for i in range(0, priorityQueue.N):
        print priorityQueue.pq[i],
