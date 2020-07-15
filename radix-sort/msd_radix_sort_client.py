from msd_radix_sort import MSDRadixSort

if __name__ == "__main__":
    words = ['she', 'sells', 'seashells', 'by', 'the', 'sea', 'shore', \
        'the', 'shells', 'she', 'sells', 'are', 'surely', 'seashells']
    print "ORIGINAL: ", 
    print words
    indexer = MSDRadixSort()
    print "  SORTED: ",
    indexer.sort(words)
    print words
