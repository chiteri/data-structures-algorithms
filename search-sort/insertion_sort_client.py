from insertion_sort import InsertionSort

if __name__ == '__main__':
    # search_tokens = [1, 3, -4, -8, 10]
    search_tokens = ['john', 'anna', 'mark', 'angela', 'james']

    print "UNSORTED:", 
    print search_tokens

    sorter = InsertionSort(search_tokens)
    sorter.sort()

    print "SORTED:", 
    print search_tokens 