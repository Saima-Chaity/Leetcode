# Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.'''

#Two pass
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        length = 0
        dummy = ListNode(0)
        dummy.next = head
        current = head
        while current:
            length += 1
            current = current.next

        current = dummy
        length -= n
        while length > 0:
            current = current.next
            length -= 1
        current.next = current.next.next
        return dummy.next


# One pass
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
