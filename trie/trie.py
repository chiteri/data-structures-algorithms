# This is an implementation of a symbol table specialized to string keys
# A trie (reTRIEval) is a data structure for searching with string keys
class Node:
    def __init__(self):
        self.R = 256 # Characters in extended ASCII
        self.value = None
        self.next = [None] * self.R # All links point to null to begin with

class Trie:
    def __init__(self):
        self.R = 256 # Characters in extended ASCII
        self.root = Node()

    def put(self, key, val):
        self.insert(self.root, key, val, 0)

    def insert(self, x, key, val, d):
        if x is None:
            x = Node()
        if d == len(key):
            x.value = val
            return x
        
        c = key[d]
        index = ord(c) - 97
        x.next[index] = self.insert(x.next[index], key, val, d+1)

        return x

    def contains(self, key):
        return self.get(key) is not None 

    def get(self, key):
        x = self.retrieve(self.root, key, 0)

        if x is None:
            return None

        return x.value # Cast needed at times, in statically typed languages

    def retrieve(self, x, key, d):
        if x is None:
            return None

        if d == len(key):
            return x

        index = ord(key[d]) - 97
        # c = key[d]

        return self.retrieve(x.next[index], key, d+1)

    def delete(self, key):
        pass