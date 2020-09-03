import sys

class Hanoi:
    def __init__(self):
        pass

    def solve(self, disks, left):
        if disks == 0:
            return " "
        
        move = ""

        if left:
            move = str(disks) + "L"
        else:
            move = str(disks) + "R"

        return self.solve(disks - 1, not left) + move + self.solve(disks -1, not left)

if __name__ == "__main__":
    disks = int(sys.argv[1])
    print Hanoi().solve(disks, False)