from Graphs import Graph

my_graph = Graph(directed=True)
my_graph.insertEdges(0, 1)
my_graph.insertEdges(0, 2)
my_graph.insertEdges(1, 2)
my_graph.insertEdges(2, 3)

from collections import deque
def bfs(start):

    explored = set()
    queue = deque([start])
    while queue:
        curNode = queue.pop()
        explored.add(curNode)
        print (curNode, end = " ")
        for neighbor in my_graph.graph[curNode]:
            if neighbor not in explored:
                queue.append(neighbor)
                explored.add(neighbor)

bfs(0)

"""

Time Complexity: O(V+E)
Space: O(N) -> space for explored

"""


