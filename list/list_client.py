from list import Node, List

if __name__ == "__main__":
    names = List()
    names.head = Node("Carol") 

    names.push("Bob")
    names.push("Alice")

    names.traverse()