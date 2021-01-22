# Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/
'''Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prevNode = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            prevNode = firstNode
            head = firstNode.next

        return dummy.next


# Another approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        i = 1
        current = head
        prev = head
        while current:
            current = current.next
            i += 1
            if i == 2 and current:
                prev.val, current.val = current.val, prev.val
                current = current.next
                i = 1
                prev = current
        return head


# Recursive approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swapNode(node):
            if node and node.next:
                node.val, node.next.val = node.next.val, node.val
                swapNode(node.next.next)

        current = head
        swapNode(current)
        return head