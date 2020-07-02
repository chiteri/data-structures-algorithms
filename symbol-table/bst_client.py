from binary_search_tree import BinarySearchTree

if __name__ == "__main__":
    symbol_table = BinarySearchTree()

    keys = ["It", "was", "the", "best", "days", "of", "our", "life", "the", "the"]
    # keys = [9, 0, 8, 6, 1, 2, 3, 5, 4]

    for key in keys:
        if symbol_table.contains(key):
            symbol_table.put(key, symbol_table.get(key) + 1)
        else:
            symbol_table.put(key, 1)

    for index in symbol_table.keys():
        print str(index), # Print key
        print str(symbol_table.get(index)) # Print value
