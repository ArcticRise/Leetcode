"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.


"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return
        if node.val >= low and node.val <= high:
            ans += node.val
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
    dfs(root)
    return ans


"""
Time Complexity: O(N) where n is nodes in tree
Space: O(1)

"""