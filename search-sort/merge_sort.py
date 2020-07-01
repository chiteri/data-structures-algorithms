class MergeSort:
    def __init__(self):
        self.aux = [] # An auxilliary list to hold the results

    def sort_helper(self, original):
        self.aux = [0] * len(original) # Reserve space for the list
        self.sort(original, 0, len(original))

    def sort(self, original, low, high):
        N = high - low
        
        if N <= 1:
            return

        middle = low +  N / 2

        self.sort (original, low, middle)
        self.sort(original, middle, high)
        self.merge(original, low, middle, high)


    def merge(self, original, lo, mid, high):
        low = lo
        middle = mid
        N = high - low

        # Rearrange items in the temporary list 
        for k in range(0, N):
            if low == mid:
                self.aux[k] = original[middle]
                middle += 1
            elif middle == high:
                self.aux[k] = original[low]
                low += 1
            elif original[middle] < original[low]:
                self.aux[k] = original[middle] # "Middle" element is smaller, move it 
                middle += 1
            else:
                self.aux[k] = original[low] # "Low" element is smaller, move it
                low += 1

        # COpy content back to the original 
        for k in range(0, N):
            original[lo + k] = self.aux[k]
