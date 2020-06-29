class BinarySearch:
    def __init__(self):
        pass # Empty constructor

    def search_helper(self, key, items):
        return self.search(key, items, 0, len(items))
    
    # Get the index of string key inside the search array 
    def search(self, needle, haystack, low, high):
        if high <= low:
            return -1 
        
        middle = low + (high - low) /  2

        # Perform a comparison of items in the search list / array 
        # (lexicographic comparison in case of strings)
        if needle < haystack[middle]:
            # Search in the lower half
            return self.search(needle, haystack, low, middle)

        if needle > haystack[middle]:
            # Search in the upper half
            return self.search(needle, haystack, middle + 1, high)

        if needle == haystack[middle]:
            # Results found
            return middle