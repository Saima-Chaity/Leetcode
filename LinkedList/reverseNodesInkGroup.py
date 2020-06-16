# Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/
'''Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is
not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        newHead = None
        kthTail = None
        current = head

        while current:
            count = 0
            current = head
            while count < k and current:
                current = current.next
                count += 1
            if count == k:
                reverseHead = self.reverseLinkedList(head, k)
                if not newHead:
                    newHead = reverseHead
                if kthTail:
                    kthTail.next = reverseHead
                kthTail = head
                head = current
        if kthTail:
            kthTail.next = head
        return newHead if newHead else head

    def reverseLinkedList(self, head, k):
        prevNode = None
        currentNode = head

        while k:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            k -= 1
        return prevNode