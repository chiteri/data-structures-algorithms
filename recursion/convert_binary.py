import sys

class Binary:
    def __init__(self):
        pass

    def convert(self, n):
        if n == 1:
            return "1"
        else:
            return self.convert(n / 2) + str(n % 2)

if __name__ == "__main__":
    number = int(sys.argv[1])
    print Binary().convert(number)


