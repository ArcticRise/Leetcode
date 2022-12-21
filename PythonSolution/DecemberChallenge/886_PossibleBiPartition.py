"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].


"""

from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


def possibleBipartition( n: int, dislikes: List[List[int]]) -> bool:
    uf = UnionFind(n+1)
    adj_list = defaultdict(list)
    for p,c in dislikes:
        adj_list[p].append(c)
        adj_list[c].append(p)
    
    for i in range(1,n+1):
        for neigh in adj_list[i]:
            if uf.find(i) == uf.find(neigh):
                return False
            uf.merge(adj_list[i][0],neigh)
    return True


n = 4 
dislikes = [[1,2],[1,3],[2,4]]

print(possibleBipartition(4,dislikes))

"""
Time Complexity : O(V + E)
Space: O(V+E)

"""