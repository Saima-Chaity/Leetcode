# Sort List - https://leetcode.com/problems/sort-list/
'''Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(temp)

        return self.mergeList(l1, l2)

    def mergeList(self, l1, l2):
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
