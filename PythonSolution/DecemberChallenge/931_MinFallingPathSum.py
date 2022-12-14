"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.


"""

from typing import List

def minFallingPathSum( matrix: List[List[int]]) -> int:

    def dfs(i,j):

        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return float('inf')
        if i == m-1:
            return matrix[i][j]
        if (i,j) in memo:
            return memo[(i,j)]
        result = matrix[i][j] + min(dfs(i+1, j), dfs(i+1, j+1), dfs(i+1, j-1))
        memo[(i,j)] = result
        return result

    m, n = len(matrix), len(matrix[0])
    memo = {}
    ans = float("inf")
    for i in range(len(matrix[0])):
        ans = min(ans, dfs(0, i))
    return ans


Case1 = [[2,1,3],[6,5,4],[7,8,9]]
print(minFallingPathSum(Case1))
