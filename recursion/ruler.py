import sys

class Ruler:
    def __init__(self):
        pass

    def ruler(self, n):
        if n == 0:
            return " "
        return str(self.ruler(n - 1)) + str(n) + str(self.ruler(n -1))

if __name__ == "__main__":
    number = int(sys.argv[1])

    print Ruler().ruler(number)