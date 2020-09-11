class GraphNode:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
    visited = False


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def addNode(self, node: GraphNode):
        self.nodes.append(node)

    def clearVisited(self):
        for node in self.nodes:
            node.visited = False
