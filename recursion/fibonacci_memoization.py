import sys 

class FibonacciM:
    def __init__(self):
        self.memo = []

    def F(self, n):
        self.memo = [0] * n
        # Invoke the recursive function 
        return self.FM(n)

    def FM(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        if self.memo[n - 1] == 0:
            self.memo[n - 1] = self.FM(n - 1) + self.FM(n - 2)

        return self.memo[n -1]


if __name__ == "__main__":
    number = int(sys.argv[1]) # Collect parameter from the command line 
    print FibonacciM().F(number)
