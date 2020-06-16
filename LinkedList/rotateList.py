# Rotate List - https://leetcode.com/problems/rotate-list/
'''Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        if not head.next:
            return head

        length = 1
        oldTail = head
        # close the linked list into the ring
        while oldTail.next:
            length += 1
            oldTail = oldTail.next
        oldTail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        newTail = head
        for i in range(length - k % length - 1):
            newTail = newTail.next
        newHead = newTail.next

        # break the ring
        newTail.next = None
        return newHead