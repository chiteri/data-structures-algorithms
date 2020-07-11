from queue import Queue
import sys

if __name__ == "__main__":
    # max = int(sys.argv[1]) # Read arguments from the command line 
    queue = Queue()

    for x in range(1, len(sys.argv)): # Skip the first argument which is the file name
        item =  sys.argv[x]

        if item is "-":
            print queue.dequeue()
        else:
            queue.enqueue(item)

    # print stack.pop()
