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

#Typical BFS implementation using queue as its processing one node at a time
def bfs(my_tree) -> List:

    #Check if empty
    if not my_tree.root:
        return None
    else:
        #Queue the root
        Nodes_traverse =[]
        queue = deque([my_tree.root])
        while queue:
            cur_node = queue.pop()
            Nodes_traverse.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        return Nodes_traverse 

print(bfs(my_tree))
#[1, 38, 62, 7, 13, 10, 5, 0]

"""

Time Complexity: O(N) as im traversing each tree node


"""
            