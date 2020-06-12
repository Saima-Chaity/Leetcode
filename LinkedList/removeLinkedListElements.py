# Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/
'''Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return None

        while head and head.val == val:
            head = head.next

        current = head
        prev = None

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return head