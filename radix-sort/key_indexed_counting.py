class KeyIndexedCounting:
    def __init__(self):
        pass 
        # self.items = a

    # Sort an array a[] of N integers between 0 and R - 1
    def sort(self, a):
        N = len(a)
        aux = [0] * N # Copy of the original items in ordered fashion

        R = len(set(a)) # The number of unique items in the list

        # Count the frequencies of each letter using key as index
        count = [0] * (R+1)
        
        # This process tells us how to distribute the keys in the output
        for i in range(0, N):
            index = ord(a[i]) - 97  # 97 is the Integer value of a lower case 'A'
            count[index +1] += 1

        # Compute frequency cumulates which specify destination
        for r in range(0, R):
            count[r+1] += count[r]

        # Access cumulates using keys as index to move items 
        for i in range(0, N):
            index = ord(a[i]) - 97
            aux[count[index]] = a[i]
            count[index] += 1 # Increment the value of count after each iteration

        # Copy ordered items back into the original array 
        for i in range(0, N):
            a[i] = aux[i]

        return a