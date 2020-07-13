from lsd_radix_sort import LSDRadixSort

if __name__ == "__main__":
    letters = ['dab', 'cab', 'fad', 'bad', 'dad', 'ebb', 'ace', 'add', 'fed', 'bed', 'fee', 'bee']
    print "ORIGINAL: ", 
    print letters
    indexer = LSDRadixSort()
    print "  SORTED: ",
    print indexer.sort(letters, 3)