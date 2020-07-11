from red_black_tree import RedBlackTree

if __name__ == "__main__":
    items = [3, 4, 10, 1, 6, 5]
    # items = ['T', 'P', 'R', 'N', 'H', 'O', 'A', 'E', 'I', 'G']

    symbol_table = RedBlackTree() 

    for item in items:
        if symbol_table.contains(item):
            symbol_table.put(item, symbol_table.get(item) + 1)
        else:
            symbol_table.put(item, 1)
        # red_black_tree.put(item, item)

    print "BEFORE: ", 
    print symbol_table.keys()
