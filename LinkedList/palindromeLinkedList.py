# Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/
'''Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(node):
            prev = None
            while node:
                nextNode = node.next
                node.next = prev
                prev = node
                node = nextNode
            return prev

        def find(node):
            slow = node
            fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        secondHalf = find(head)
        reverseSecondHalf = reverse(secondHalf)
        while reverseSecondHalf:
            if head.val != reverseSecondHalf.val:
                return False
            reverseSecondHalf = reverseSecondHalf.next
            head = head.next
        return True