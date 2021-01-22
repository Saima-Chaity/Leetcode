# Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/
'''Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        resultList = dummy = ListNode(0)
        while l1 or l2:
            if not l2:
                while l1:
                    resultList.next = ListNode(l1.val)
                    resultList = resultList.next
                    l1 = l1.next
            elif not l1:
                while l2:
                    resultList.next = ListNode(l2.val)
                    resultList = resultList.next
                    l2 = l2.next
            elif l1.val < l2.val:
                resultList.next = ListNode(l1.val)
                resultList = resultList.next
                l1 = l1.next
            else:
                resultList.next = ListNode(l2.val)
                resultList = resultList.next
                l2 = l2.next
        return dummy.next


# Recursive approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def getSortedList(l1, l2):

            if not l1:
                return l2

            if not l2:
                return l1

            if l1.val <= l2.val:
                l1.next = getSortedList(l1.next, l2)
                return l1

            else:
                l2.next = getSortedList(l1, l2.next)
                return l2

        return getSortedList(l1, l2)
