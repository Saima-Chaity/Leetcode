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

        totalLength = 0
        current = head
        while current:
            totalLength += 1
            current = current.next

        positionFromHead = totalLength - n
        current = head
        prev = None
        while positionFromHead != 0:
            positionFromHead -= 1
            prev = current
            current = current.next

        if prev:
            prev.next = current.next
        else:
            head = head.next
        return head


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
