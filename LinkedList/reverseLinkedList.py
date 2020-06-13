# Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/
'''Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prevNode = nextNode = None
        currentNode = head

        if head is None:
            return None;

        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        return prevNode


# Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/
'''Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head:
            return None

        current = head
        prev = None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        while m > 1:
            prev = current
            current = current.next
            m -= 1
            n -= 1

        # The two pointers that will fix the final connections.
        temp = prev
        tail = current

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
            n -= 1

        # Adjust the final connections
        if temp:
            temp.next = prev
        else:
            head = prev
        tail.next = current
        return head