import sys 

class Fibonacci:
    def __init__(self):
        self.series = []

    def F(self, n):
        self.series = [0] * (n + 1)
        return self.FD(n) 

    def FD(self, n):
        self.series[0] = 0
        self.series[1] = 1

        for i in range(2, len(self.series)):
            self.series[i] = self.series[i - 1] + self.series[i - 2]

        return self.series[n] 

if __name__ == "__main__":
    number = int(sys.argv[1])

    print Fibonacci().F(number)
