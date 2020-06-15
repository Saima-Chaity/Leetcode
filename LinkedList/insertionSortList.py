# Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/
'''Sort a linked list using insertion sort.
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs
within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        tail = head.next
        dummy.next.next = None

        while tail:
            prev = dummy
            current = dummy.next
            nextNode = tail.next

            while current:
                if current.val >= tail.val:
                    prev.next = tail
                    tail.next = current
                    break
                prev = current
                current = current.next
            else:
                prev.next = tail
                tail.next = None
            tail = nextNode
        return dummy.next