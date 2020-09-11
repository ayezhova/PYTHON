from Graphs.Graph import GraphNode, Graph
from Stack_Implementation.stack import Stack


def BFSRouteSearch(startNode, endNode):
    stack = Stack()
    stack.push(startNode)
    while not stack.isEmpty():
        node = stack.pop()
        node.visited = True
        if node == endNode:
            return True
        for nodeNeighbor in node.neighbors:
            if not nodeNeighbor.visited:
                stack.push(nodeNeighbor)
    return False


def RouteBetweenNodes(graph: Graph, node1: GraphNode, node2: GraphNode):
    # Clear Visited to reset visited flags of graphNodes
    graph.clearVisited()
    # Using a BFS to find whether a route exists
    # Since pathways for nodes are one way, have to check the path from both node1 to node2 and node2 to node1
    if BFSRouteSearch(node1, node2):
        return True
    # If there was no pathway between node1 and node2, there may still be a pathway from node2 to node1
    # Reset visited flags so that we can search again
    graph.clearVisited()
    if BFSRouteSearch(node2, node1):
        return True
    return False


def Test():
    #         A  ->  B
    #         ^
    #         |
    #         v
    #         C  <-  D  -> E
    nodeA = GraphNode('A')
    nodeB = GraphNode('B')
    nodeC = GraphNode('C')
    nodeD = GraphNode('D')
    nodeE = GraphNode('E')
    nodeA.neighbors = [nodeB, nodeC]
    nodeC.neighbors = [nodeA]
    nodeD.neighbors = [nodeC, nodeE]
    graph = Graph([nodeA, nodeB, nodeC, nodeD, nodeE])
    print("Is there a route between Node A and Node B?", RouteBetweenNodes(graph, nodeA, nodeB))
    print("Is there a route between Node B and Node D?", RouteBetweenNodes(graph, nodeB, nodeD))
    print("Is there a route between Node C and Node E?", RouteBetweenNodes(graph, nodeC, nodeE))
    print("Is there a route between Node A and Node A?", RouteBetweenNodes(graph, nodeA, nodeA))


Test()
