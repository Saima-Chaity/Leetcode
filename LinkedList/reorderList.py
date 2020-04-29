# Reorder List - https://leetcode.com/problems/reorder-list/
'''Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        def findMid(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseLinkedList(node):
            prev = None
            current = node

            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            return prev

        mid = findMid(head)
        reverseSecondHalf = reverseLinkedList(mid)

        l1 = head
        l2 = reverseSecondHalf

        while l2.next:
            temp1 = l1.next
            l1.next = l2
            l1 = temp1

            temp2 = l2.next
            l2.next = l1
            l2 = temp2
