from binary_search import BinarySearch 

if __name__ == '__main__':
    names = ['angela', 'anna', 'james', 'john', 'mark']

    name = 'james'

    search_help = BinarySearch()
    print search_help.search_helper(name, names)