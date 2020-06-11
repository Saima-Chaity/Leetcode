# Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
'''Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        length = len(lists)
        if length == 0: return None
        interval = 1
        while interval < length:
            for i in range(0, length - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if length > 0 else lists

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        resultList = head = ListNode(0)
        while l1 or l2:
            if l1 is None:
                while l2:
                    resultList.next = ListNode(l2.val)
                    resultList = resultList.next
                    l2 = l2.next
            elif l2 is None:
                resultList.next = ListNode(l1.val)
                resultList = resultList.next
                l1 = l1.next

            elif l1.val <= l2.val:
                resultList.next = ListNode(l1.val)
                resultList = resultList.next
                l1 = l1.next
            elif l1.val > l2.val:
                resultList.next = ListNode(l2.val)
                resultList = resultList.next
                l2 = l2.next
        return head.next


#Using PriorityQueue

from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        q = PriorityQueue()
        currentNode = dummy = ListNode(None)
        for index, node in enumerate(lists):
            if node:
                q.put((node.val, index, node))

        while q.qsize() > 0:
            poppedItem = q.get()
            currentNode.next, index = poppedItem[2], poppedItem[1]
            currentNode = currentNode.next
            if currentNode.next:
                q.put((currentNode.next.val, index, currentNode.next))
        return dummy.next