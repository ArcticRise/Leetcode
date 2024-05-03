"""

Implementation of a simple Singly Linked List

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

        # Added in fields just for cycle stuff!
        self.pos = None
        self.prev = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # insert a node at the head, O(1)
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.pos = 0
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    #Insert at an index given, O(n)
    def insert_at_index(self, data, index):
        new_node = Node(data)
        cur_node = self.head
        cur_pos = 0
        #Index is Zero so we can just call insert at head since zero is first
        if cur_pos == index:
            self.insert_at_head(data)
        else:
            while cur_node and cur_pos+1 != index:
                cur_pos += 1
                cur_node = cur_node.next

            if cur_node != None:
                new_node.next = cur_node.next
                cur_node.next = new_node
            else:
                print("Index is not present")

    #Insert at end of linked list , O(1)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node

    #Remove head of linked list, O(1)
    def remove_head(self):
        if self.head is None:
            return

        self.head = self.head.next

    #Remove the tail of linked list, O(n)
    def remove_tail_node(self):
        if self.head is None:
            return
        cur_node = self.head
        while cur_node.next.next:
            cur_node = cur_node.next

        cur_node.next = None

    # Method to remove at given index, O(n)
    def remove_at_index(self, index):
        if self.head is None:
            return

        cur_node = self.head
        cur_pos = 0
        if cur_pos == index:
            self.remove_head()
        else:
            while cur_node is not None and cur_pos != index:
                cur_pos += 1
                cur_node = cur_node.next

            if cur_pos is not None:
                cur_node.next = cur_node.next.next
            else:
                print("Index not present")

    # Method to remove a given node, O(n)
    def remove_certain_node(self, data):
        cur_node = self.head

        if cur_node.val == data:
            self.remove_head()
            return

        while cur_node is not None and cur_node.next.val != data:
            cur_node = cur_node.next

        if cur_node is None:
            return
        else:
            cur_node.next = cur_node.next.next

    #Overridden string function to return a list instead of SinglyLinkedList object
    def __str__(self, ):
        seen = set()
        my_linked_list = []
        cur_node = self.head
        while cur_node.next and cur_node.pos not in seen:
            my_linked_list.append(str(cur_node.val))
            cur_node = cur_node.next
            if cur_node.pos is not None:
                seen.add(cur_node.pos)
        my_linked_list.append(str(cur_node.val))
        return str(my_linked_list)

    def create_cycle(self):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = self.head
        self.head.prev = cur_node

    def remove_cycle(self):
        cur_node = self.head.prev
        cur_node.next = None




