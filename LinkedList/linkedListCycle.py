# Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/
'''Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slowPtr = head
        firstPtr = head

        while firstPtr and firstPtr.next:
            slowPtr = slowPtr.next
            firstPtr = firstPtr.next.next

            if slowPtr == firstPtr:
                return True
        return False


# Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/
'''Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findIntersection(self, head):
        slowPtr = head
        firstPtr = head

        while firstPtr and firstPtr.next:
            slowPtr = slowPtr.next
            firstPtr = firstPtr.next.next

            if slowPtr == firstPtr:
                return slowPtr

    def detectCycle(self, head: ListNode) -> ListNode:

        if not head:
            return None

        intersect = self.findIntersection(head)
        if not intersect:
            return None
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

