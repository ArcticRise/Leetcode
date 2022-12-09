"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l3 = ListNode(-1)
    cur = l3
    while l1 and l2:
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return l3.next

"""
Time Complexity: O(N)
Space: O(N) -> created new linked lIst


"""