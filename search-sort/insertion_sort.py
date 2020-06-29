class InsertionSort:
    def __init__(self, haystack):
        self.haystack = haystack 

    def sort(self, ):
        for i in range(1, len(self.haystack)):
            for j in range(i, 0, -1):
                if self.haystack[j-1] > self.haystack[j]:
                    self.swap(self.haystack, j-1, j)
                else:
                    break

        return self.haystack

    # Swap two elements in a list or an array 
    def swap(self, haystack, i, j):
        temp = haystack[i]
        haystack[i] = haystack[j]
        haystack[j] = temp