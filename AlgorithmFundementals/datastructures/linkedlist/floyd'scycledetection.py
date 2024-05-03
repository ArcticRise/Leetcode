"""
This is a simple implementation of Floyd's tortoise and hare algorithm to detect a cycle in a sequence

uses two pointer techiqnue a fast and slow pointers

"""

from SinglyLinkedList import SinglyLinkedList

# Create our Singly linked List
linkedList = SinglyLinkedList()
linkedList.insert_at_head(1)
linkedList.insert_at_index(2, 1)
linkedList.insert_at_index(3, 2)
linkedList.insert_at_tail(4)
linkedList.create_cycle()


# 1 -> 2 -> 3 -> 4 -> 1 cycle at 1

#Space O(1), Runtime O(n) n represents size of list
def check_cycle(head) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False


"""

Feel free to make any improvements, i just made the cycle to always be at the head as its easier 
just for demo purposes.

"""

print("Linked List with Cycle--------")
print(linkedList)
print(check_cycle(linkedList.head))
linkedList.remove_cycle()

print("Linked List without Cycle--------")
print(linkedList)
print(check_cycle(linkedList.head))
