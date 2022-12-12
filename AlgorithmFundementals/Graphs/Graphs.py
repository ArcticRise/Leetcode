"""
This is my graph structure file

"""

from collections import defaultdict
class Graph():

    def __init__(self,directed=False) -> None:
        #This is going to keep track of the graph vertices and edges
        self.graph = defaultdict(list)
        self.directed = directed
    
    #Insert Edges
    def insertEdges(self,v,e):
        self.graph[v].append(e)
        if not self.directed:
            self.graph[e].append(v)

