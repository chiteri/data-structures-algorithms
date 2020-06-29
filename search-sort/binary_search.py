class BinarySearch:
    def __init__(self):
        pass 

    def search_helper(self, key, haystack):
        return self.search(key, haystack, 0, len(haystack))
    
    # Get the index of string key inside the search string array 
    def search(self, key, search_string, low, high):
        if high <= low:
            return -1 
        
        middle = low + (high - low) /  2

        if key < search_string[middle]:
            # Search in the lower half
            return self.search(key, search_string, low, middle)

        if key > search_string[middle]:
            # Search in the upper half
            return self.search(key, search_string, middle + 1, high)

        if key == search_string[middle]:
            # Results found
            return middle