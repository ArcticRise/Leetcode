"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    oddp = head
    temp = evenp = head.next
    while oddp and oddp.next and evenp and evenp.next:
        oddp.next=oddp.next.next
        evenp.next=evenp.next.next
        oddp=oddp.next
        evenp=evenp.next
    oddp.next = temp
    return head


"""
Time Complexity: O(N)
Space: O(1)

[1,2,3,4,5]
Algos work but seting odd to  1 and even to 2 then we iterate via .next.next
set odd and even to the next elem....
to get 3 then 4 then odd; can go one more time to 5 but even ends

odd is now 1,3,5 and even is 2,4 but remember theres the temp var that is pointed to head.next which needs to be used, since even is now None(Reached End of LinkedList)
we set oddp.next = temp to get ans

"""