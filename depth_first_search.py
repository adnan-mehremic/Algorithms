# Depth first search


class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacenciesList = []
        self.visited = False
        self.predecessor = None


class DepthFirstSearch(object):

    def dfs(self, node):
        node.visited = True
        print("%s " % node.name)

        for n in node.adjacenciesList:
            if not n.visited:
                self.dfs(n)
