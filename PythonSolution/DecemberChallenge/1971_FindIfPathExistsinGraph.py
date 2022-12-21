"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2


"""

from typing import List
from collections import defaultdict,deque

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adj_list = defaultdict(list)
    for e,v in edges:
        adj_list[e].append(v)
        adj_list[v].append(e)

    visted = set()
    queue = deque([source])
    while queue:
        cur = queue.pop()
        if cur == destination:
            return True
        visted.add(cur)
        for i in adj_list[cur]:
            if i not in visted:
                visted.add(i)
                queue.append(i)      
    return False

n = 3 
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

print(validPath(n,edges,source,destination))

"""
Time Complexity : O(V+E)
Space: O(V+E)

"""