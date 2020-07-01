from merge_sort import MergeSort

class LongestRepeatedString:
    def __init__(self):
        pass 

    def lcp(self, s, t):
        N = min(len(s), len(t))

        # Use the shorter of the two strings' length to loop
        for i in range(0, N):
            if s[i] is not t[i]:
                return s[0:i] # Give the substring back if you miss a match

        return s[0:N]

    def lrs(self, s):
        N = len(s)

        # Form suffix strings 
        suffixes = [''] * N
        for i in range(0, N):
            suffixes[i] = s[i:N]

        # Next sort the suffix strings 
        sorter = MergeSort()
        sorter.sort_helper(suffixes)

        # Find longest LCP among adjacent entries
        lrs = ''

        for i in range (0, N-1):
            x = self.lcp(suffixes[i], suffixes[i+1])

            if len(x) > len(lrs):
                lrs = x 

        return lrs