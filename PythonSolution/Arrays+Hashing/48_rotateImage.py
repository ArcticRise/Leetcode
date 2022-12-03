"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""
from typing import List

def rotate( matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    #reverse then transpose
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


case1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate(case1)
print(case1)

"""
Time Complexity: O(M) m as in matrix cells
Space: O(1)

"""