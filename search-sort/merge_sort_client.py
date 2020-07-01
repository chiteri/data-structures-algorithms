from merge_sort import MergeSort

if __name__ == '__main__':
    # search_tokens = [1, 3, -4, -8, 10]
    search_tokens = [9, 0, 8, 6, 1, 2, 3, 5, 4]
    # search_tokens = ['john', 'anna', 'mark', 'angela', 'james']

    print "ORIGINAL:", 
    print search_tokens

    sorter = MergeSort()
    sorter.sort_helper(search_tokens)

    print "SORTED:", 
    print search_tokens 