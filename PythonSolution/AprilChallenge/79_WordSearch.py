"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def dfs(i, j, index, word):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or index > len(word):
            return False

        prune = False
        if word[index] == board[i][j]:
            temp_char = board[i][j]
            board[i][j] = '#'
            prune = dfs(i + 1, j, index + 1, word) or dfs(i - 1, j, index + 1, word) \
                    or dfs(i, j + 1, index + 1,word) or dfs(i, j - 1,index + 1, word)
            board[i][j] = temp_char

        return prune

    row, col = len(board), len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == word[0]:
                if dfs(i, j, 0, word):
                    return True
    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))

"""
    Time: O(N * (3 ^ L))
    Space: O(L)
    let N be the number of cells in the board.
    Let L be the length of the word
"""