from stack import Stack

import sys

if __name__ == "__main__":
    # max = int(sys.argv[1]) # Read arguments from the command line 
    stack = Stack()

    for x in range(1, len(sys.argv)): # Skip the first argument which is the file name
        item =  sys.argv[x]

        if item is "-":
            print stack.pop()
        else:
            stack.push(item)

    # print stack.pop()
