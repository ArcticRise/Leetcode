"""

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

"""
from typing import List

def uniquePathsIII(grid: List[List[int]]) -> int:
    ans = 0
    canMove = 1
    def dfs(i,j):
        nonlocal ans
        nonlocal canMove
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] < 0:
            return

        if grid[i][j] == 2:
            if canMove == 0:
                ans += 1
            return

        grid[i][j] = float("-inf")
        canMove -= 1
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i-1,j)
        grid[i][j] = 0
        canMove += 1
    
    row,col = len(grid),len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                start = (r,c)
            elif grid[r][c] == 0:
                canMove += 1
    dfs(start[0],start[1])
    return ans

print(uniquePathsIII(grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))

"""
Time: O(3^N)
Space: O(N)

"""