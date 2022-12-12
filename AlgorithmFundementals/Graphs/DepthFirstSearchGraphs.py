from Graphs import Graph

my_graph = Graph(directed=True)
my_graph.insertEdges(0, 1)
my_graph.insertEdges(0, 2)
my_graph.insertEdges(1, 2)
my_graph.insertEdges(2, 3)

#Dfs is mostly done via Recursion, it can also be done using a stack!!
explored = set()
def dfs(start):

    print (start, end = " ")
    explored.add(start)
    for neighbor in my_graph.graph[start]:
        if neighbor not in explored:
            dfs(neighbor)

dfs(0)



"""

Time Complexity: O(V+E)
Space: O(N) -> space for explored

"""