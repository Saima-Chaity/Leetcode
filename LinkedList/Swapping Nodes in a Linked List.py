'''Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None

        length = 0
        current = head
        frontNode = None
        while current:
            length += 1
            if length == k:
                frontNode = current
            current = current.next

        if length == 1:
            return head

        endNode = head
        for i in range(1, length - k + 1):
            endNode = endNode.next

        endNode.val, frontNode.val = frontNode.val, endNode.val
        return head

