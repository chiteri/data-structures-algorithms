# A ternary search trie is a data structure that resolves 
# the problem of too much space used by an r-way trie
class Node:
    def __init__(self):
        self.value = None 
        self.letter = None 
        self.left = None
        self.middle = None 
        self.right = None 

class TernarySearchTrie:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self.insert(self.root, key, val, 0)

    def insert(self, x, key, val, d):
        index = ord(key[d]) - 97

        if x is None:
            x = Node()
            x.letter = index

        if index < x.letter:
            x.left = self.insert(x.left, key, val, d)
        elif index > x.letter:
            x.right = self.insert(x.right, key, val, d)
        elif d < len(key) - 1:
            x.middle = self.insert(x.middle, key, val, d+1)
        else:
            x.value = val

        return x

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        x = self.retrieve(self.root, key, 0)

        if x is None:
            return None

        return x.value

    def retrieve(self, x, key, d):
        if x is None:
            return None 

        index = ord(key[d]) - 97

        if index < x.letter:
            return self.retrieve(x.left, key, d)
        elif index > x.letter:
            return self.retrieve(x.right, key, d)
        elif d < len(key) - 1:
            return self.retrieve(x.middle, key, d+1)
        else:
            return x