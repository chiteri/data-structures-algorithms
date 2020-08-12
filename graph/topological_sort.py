# A topological sort is a digraph processing application, that is it is 
# used to perform precedence scheduling to ensure tasks take place with 
# specific precedence constraints i.e tasks are scheduled in the correct order.
class DepthFirstOrder:
    def __init(self, diGraph):
        self.marked = {} 
        self.reverse_post = [] # stack to store vertices in reverse postorder

        for vertex in diGraph.adjacent:
            self.marked[vertex] = False

        for vertex in diGraph.adjacent:
            if not self.marked[vertex]:
                self.dfs(diGraph, vertex)

    def dfs(self, diGraph, vertex):
        self.marked[vertex] = True

        for neighbour in diGraph.adjacent[vertex]:
            if not self.marked[neighbour]:
                self.dfs(diGraph, neighbour)

        self.reverse_post.append(v)

    # Returns all vertices in "reverse DFS postorder"
    def reversePost(self):
        return self.reverse_post
