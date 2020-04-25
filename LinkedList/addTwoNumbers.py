# Add Two Numbers - https://leetcode.com/problems/add-two-numbers/
'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        resultList = dummy = ListNode(0)
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            summation = x + y + carry
            carry = summation // 10
            resultList.next = ListNode(summation % 10)
            resultList = resultList.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            resultList.next = ListNode(carry)
        return dummy.next


# Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/
'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(node):
            if not node:
                return None
            current = node
            prev = None
            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            return prev

        carry = 0
        resultList = dummy = ListNode(0)
        l1 = reverse(l1)
        l2 = reverse(l2)
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            summation = x + y + carry
            carry = summation // 10
            resultList.next = ListNode(summation % 10)
            resultList = resultList.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            resultList.next = ListNode(carry)
            resultList = resultList.next
        return reverse(dummy.next)


#Using stack
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(node):
            if not node:
                return None
            current = node
            prev = None
            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            return prev

        carry = 0
        resultList = dummy = ListNode(0)
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            summation = x + y + carry
            carry = summation // 10
            resultList.next = ListNode(summation % 10)
            resultList = resultList.next

        if carry > 0:
            resultList.next = ListNode(carry)
            resultList = resultList.next
        return reverse(dummy.next)
