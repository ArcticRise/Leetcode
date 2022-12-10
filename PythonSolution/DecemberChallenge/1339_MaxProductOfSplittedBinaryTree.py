"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxProduct(root: Optional[TreeNode]) -> int:

    res = total = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res,left*(total-left),right*(total-right))
        return left + right + node.val
    total = dfs(root)
    dfs(root)
    return res % (1000000000 + 7)

"""
Time Complexity: O(N)
Space: O(H) 

Get Total Sum
then get the right and left max sum - total

"""