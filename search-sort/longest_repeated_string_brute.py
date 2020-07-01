class LongestRepeatedStringBrute:
    def __init__(self):
        pass 

    def lcs(self, s, t):
        N = min(len(s), len(t))

        # Use the shorter of the two strings' length to loop
        for i in range(0, N):
            if s[i] is not t[i]:
                return s[0:i] # Give the substring back if you miss a match

        return s[0:N]

    def lrs(self, s):
        N = len(s)
        lrs = ''

        for i in range(0, N):
            for j in range(i+1, N):
                x = self.lcs(s[i:N], s[j:N])

                if len(x) > len(lrs):
                    lrs = x

        return lrs