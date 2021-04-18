# Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return None

        current = head
        while current:
            if current.next and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
'''Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers 
from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = prev = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next
        return dummy.next
