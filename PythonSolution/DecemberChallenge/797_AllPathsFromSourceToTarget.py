"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

"""

from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    ans = []
    def dfs(node,path):
        if node == len(graph)-1:
            ans.append(path.copy())
        for i in graph[node]:
            path.append(i)
            dfs(i,path)
            path.pop()
                
    dfs(0,[0])
    return ans

graph = [[1,2],[3],[3],[]]
print(allPathsSourceTarget(graph))

"""
Time/Space: O(2^N)

"""