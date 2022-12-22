"""
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.


"""

from typing import List
from collections import defaultdict

def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
    adj_list = defaultdict(set)
    ans = [0] * N
    count = [1] * N
    for p,c in edges:
        adj_list[p].add(c)
        adj_list[c].add(p)

    def pre_order_dfs(node,pre):
        for n in adj_list[node]:
            if n != pre:
                ans[n] = ans[node] - count[n] + N - count[n]
                pre_order_dfs(n, node)
    def post_order_dfs(node,pre):
        for n in adj_list[node]:
            if n != pre:
                post_order_dfs(n, node) 
                count[node] += count[n]
                ans[node] += ans[n] + count[n]
                
    post_order_dfs(0,-1)
    pre_order_dfs(0,-1)
    return ans


"""
Time/Space : O(N)

"""