# The Mosst-significant-digit-first Radix Sort
class MSDRadixSort:
    def __init__(self):
        pass
    
    # Treat strings as if they had an extra char at the end (smaller than any char)
    def charAt(self, s, d):
        if d == len(s):
            return -1

        return ord(s[d]) - 97

    def sort(self, a):
        aux = [""] * len(a)
        self.sort_helper(a, aux, 0, len(a) - 1, 0)

    def sort_helper(self, a, aux, low, high, d):
        R = 256 # All potential characters in the alphabet
        if high <= low:
            return 

        count = [0] * (R + 2)

        # Proceed with key-index counting
        for i in range(low, high + 1):
            index = self.charAt(a[i], d)
            count[index + 2] += 1

        for r in range(0, R + 1):
            count[r + 1] += count[r]

        for i in range(low, high + 1):
            index = self.charAt(a[i], d)
            aux[count[index + 1]] = a[i]
            count[index + 1] += 1

        for i in range(low, high + 1):
            a[i] = aux[i - low]

        # Sort R subarrays recursively 
        for r in range(0, R):
            self.sort_helper(a, aux, low + count[r], low + count[r + 1] - 1, d + 1)