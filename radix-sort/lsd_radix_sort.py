# The Least-significant-digit-first Radix Sort
class LSDRadixSort:
    def __init__(self):
        pass

    # String a[] with fixed strings of length W
    def sort(self, a, W):
        R = 256 # All potential characters in the ASCII character set
        N = len(a)
        aux = [0] * N

        # Do key-indexed counting for each digit from right to left 
        for d in range(W - 1, -1, -1):

            # Key indexed counting for each possible character
            count = [0] * (R+1)
            for i in range(0, N):
                index = ord(a[i][d]) - 97
                count[index + 1] += 1

            # Key indexed counting without replacement
            for r in range(0, R):
                count[r + 1] += count[r]

            # Perform the same replaement as key-indexed counting 
            for i in range(0, N):
                index = ord(a[i][d]) - 97 
                aux[count[index]] = a[i]
                count[index] += 1

            # Copy the ordered string back to the original 
            for i in range(0, N):
                a[i] = aux[i]