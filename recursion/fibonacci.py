import sys 

class Fibonacci:
    def F(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.F(n - 1) + self.F(n - 2)


if __name__ == "__main__":
    number = int(sys.argv[1]) # Collect parameter from the command line 
    print Fibonacci().F(number)
