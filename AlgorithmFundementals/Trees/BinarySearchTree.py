
class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():

    def __init__(self) -> None:
        self.root = None
        self.num_nodes = 0
    
    #Inserting into a Binary Search Tree
    def insert(self,val) -> None:
        tree_node = TreeNode(val)
        #If tree is empty set the tree_node as root
        if self.root == None:
            self.root = tree_node
            self.num_nodes += 1
        else:
            #In case of its not empty
            cur_node = self.root
            #Traverse Tree
            while cur_node.left != tree_node and cur_node.right != tree_node:
                # Right side of tree
                if cur_node.val < tree_node.val:
                    if cur_node.right == None:
                        cur_node.right = tree_node
                    else:
                        cur_node = cur_node.right
                else:
                    #Left side Tree
                    if cur_node.left == None:
                        cur_node.left = tree_node
                    else:
                        cur_node = cur_node.left
            self.num_nodes += 1
            
    def remove(self,val):
        if not self.root:  # Tree is empty
            return "Tree Is Empty"
        cur_node = self.root
        parent_node = None
        while cur_node:
            if cur_node.val > val:
                parent_node = cur_node
                cur_node = cur_node.left
            elif cur_node.val < val:
                parent_node = cur_node
                cur_node = cur_node.right
            else:
                #We have a match!

                #There is only a left child
                if not cur_node.right:
                    if not parent_node:
                        self.root = cur_node.left
                        return
                    else:
                        #If parent > cur_val, make current a left child of parent
                        if parent_node.val > cur_node.val:
                            parent_node.left = cur_node.left
                        else:
                            #if parent < cur_val, make left child a right child of parent
                            parent_node.right = cur_node.left
        
                #There is only a right child
                elif not cur_node.right:
                    if not parent_node:
                        self.root = cur_node.right
                        return
                    else:
                        #If parent > cur_val, make current a right child of parent
                        if parent_node.val > cur_node.val:
                            parent_node.left = cur_node.right
                        else:
                            #if parent < cur_val, make left child a right child of parent
                            parent_node.right = cur_node.right
                
                # Node has both left and right child
                elif cur_node.left and cur_node.right:
                    del_node = cur_node.right
                    del_node_parent = cur_node.right
                    while del_node.left:  # Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    cur_node.data = del_node.data  # The value to be replaced is copied
                    if del_node == del_node_parent:  # If the node to be deleted is the exact right child of the current node
                        cur_node.right = del_node.right
                        return
                    if not del_node.right:  # If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return

                #Node has no child
                elif not cur_node.left and not cur_node.right:
                    if not parent_node:
                        cur_node = None
                        return
                    if parent_node.val > cur_node.val:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return
                return 'Not Found'
                