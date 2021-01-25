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

'''The steps we need to do are:

Find the end of the first half.
Reverse the second half.
Determine whether or not there is a palindrome.
Restore the list.
Return the result.'''

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        firstHalf = self.endOfFirstHalf(head)
        secondHalf = self.reverse(firstHalf.next)

        result = True
        firstPosition = head
        secondPosition = secondHalf

        while result and secondPosition is not None:
            if firstPosition.val != secondPosition.val:
                result = False
            firstPosition = firstPosition.next
            secondPosition = secondPosition.next

        firstHalf.next = self.reverse(secondHalf)
        return result

    def endOfFirstHalf(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prevNode = None
        currentNode = head

        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        return prevNode

