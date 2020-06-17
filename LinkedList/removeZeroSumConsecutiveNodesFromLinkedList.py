'''Remove Zero Sum Consecutive Nodes from Linked List -
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until
there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current:
            summation = 0
            while head:
                summation += head.val
                if summation == 0:
                    current.next = head.next
                head = head.next
            current = current.next
            if current:
                head = current.next
        return dummy.next