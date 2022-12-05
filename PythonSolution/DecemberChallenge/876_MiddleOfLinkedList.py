"""

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Input: head = [1,2,3,4,5]
Output: [3,4,5]

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


"""

Time Complexity: O(N)
Space: O(1)


"""

