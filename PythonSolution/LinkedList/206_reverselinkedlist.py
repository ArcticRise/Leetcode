"""
Given the head of a singly linked list, reverse the list, and return the reversed list.


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = None
    temp = head
    while temp:
        temp_node = temp.next
        temp.next = cur
        cur = temp
        temp = temp_node
    return cur

"""

Time Complexity: O(N)
Space: O(1)

"""
