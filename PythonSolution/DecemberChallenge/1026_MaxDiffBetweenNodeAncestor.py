
"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(root):
        nonlocal res
        if not root: 
            return float("inf"), float("-inf")
        left_min, left_max = dfs(root.left)
        right_min, right_max = dfs(root.right)
        cur_min, cur_max = min(root.val, left_min, right_min), max(root.val, left_max, right_max)
        res = max(res, abs(root.val - cur_min), abs(cur_max - root.val))
        return cur_min, cur_max
    dfs(root)
    return res


"""
Time Complexity: O(N)
Space: O(H) -> Height of tree but in a perfect tree O(Log N)

"""