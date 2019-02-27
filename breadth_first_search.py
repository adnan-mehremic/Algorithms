#

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class BreadthFirstSearch(object):

    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print("%s " % actualNode.data)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)