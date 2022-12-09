"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6


"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    def mergeList(l1,l2):
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
    
    if len(lists) == 0:
        return None
    if len(lists) <= 1:
        return lists[0]
    
    merged_list = mergeList(lists[0],lists[1])

    for i in range(2,len(lists)):
        merged_list = mergeList(merged_list,lists[i])

    return merged_list


"""
Time Complexity: O(N)
Space: O(N) created new linked lIST
"""