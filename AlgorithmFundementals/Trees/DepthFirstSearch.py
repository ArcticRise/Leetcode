from BinarySearchTree import BinarySearchTree
from collections import deque

from typing import List

my_tree = BinarySearchTree()
my_tree.insert(1)
my_tree.insert(38)
my_tree.insert(7)
my_tree.insert(5)
my_tree.insert(13)
my_tree.insert(62)
my_tree.insert(0)
my_tree.insert(10)


"""
Depth First search looks at all possible paths! for this im going to just implement dfs via the three main tree traversals in, pre and post!

"""

inorder = []
def inOrderDfs(node):
    if not node:
        return
    if node.left:
        inOrderDfs(node.left)
    inorder.append(node.val)
    if node.right:
        inOrderDfs(node.right)

inOrderDfs(my_tree.root)
print(inorder)

preOrder = []
def preOrderDfs(node):
    if not node:
        return
    preOrder.append(node.val)
    if node.left:
        preOrderDfs(node.left)
    if node.right:
        preOrderDfs(node.right)

preOrderDfs(my_tree.root)
print(preOrder)


postOrder = []
def postOrderDfs(node):
    if not node:
        return
    if node.left:
        postOrderDfs(node.left)
    if node.right:
        postOrderDfs(node.right)
    postOrder.append(node.val)

postOrderDfs(my_tree.root)
print(postOrder)

"""

Time Complexity for All algorithms would be O(N) -> As we are hitting each tree node
Space: O(N) if the tree is not balanced (Skewed), If the Tree is balanced then the best case would be O(Log N)


"""