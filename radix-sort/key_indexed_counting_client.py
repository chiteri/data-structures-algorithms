from key_indexed_counting import KeyIndexedCounting

if __name__ == "__main__":
    letters = ['d', 'a', 'c', 'f', 'f', 'b', 'd', 'b', 'f', 'b', 'd', 'e', 'a']
    print "ORIGINAL: ", 
    print letters
    indexer = KeyIndexedCounting()
    print "  SORTED: ",
    print indexer.sort(letters)