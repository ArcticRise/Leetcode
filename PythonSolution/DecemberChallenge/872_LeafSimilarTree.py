"""
Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    leaf1, leaf2 = [],[]
    def dfs(leaf,node):
        if not node:
            return

        #Leaves has no left or right child!
        if not node.left and not node.right:
            leaf.append(node.val)
            return
        if node.left:
            dfs(leaf,node.left)
        if node.right:
            dfs(leaf,node.right)
    dfs(leaf1,root1)
    dfs(leaf2,root2)
    return leaf1 == leaf2


"""
Time Complexity: O(T1+T2) -> because we're doing both trees one could be bigger than other
Space: O(N) -> Array to keep track of leaves

"""