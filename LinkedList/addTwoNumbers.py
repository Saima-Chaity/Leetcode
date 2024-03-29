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


# Complexity Analysis
# Time complexity : O(max(m, n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m, n) times.
# Space complexity : O(max(m, n)). The length of the new list is at most max(m,n)+1.


# Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/
'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

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
        carry = 0
        dummy = None
        
        stack1 = self.fillUpStack(l1, [])
        stack2 = self.fillUpStack(l2, [])
        
        while stack1 or stack2:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            total = x + y + carry
            carry = total // 10
            resultList = ListNode(total % 10)
            resultList.next = dummy
            dummy = resultList
        
        if carry:
            resultList = ListNode(carry)
            resultList.next = dummy
            dummy = resultList
        return dummy
    
    def fillUpStack(self, node, stack):
        while node:
            stack.append(node.val)
            node = node.next
        return stack


# Without reverse the input linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = 0
        n2 = 0
        current1 = l1
        current2 = l2
        while current1 or current2:
            if current1:
                n1 += 1
                current1 = current1.next
            if current2:
                n2 += 1
                current2 = current2.next

        current1 = l1
        current2 = l2
        head = None
        while n1 and n2:
            value = 0
            if n1 >= n2:
                value += current1.val
                n1 -= 1
                current1 = current1.next

            if n1 < n2:
                value += current2.val
                n2 -= 1
                current2 = current2.next

            current = ListNode(value)
            current.next = head
            head = current

        current1 = head
        head = None
        carry = 0
        while current1:
            value = (current1.val + carry) % 10
            carry = (current1.val + carry) // 10

            current = ListNode(value)
            current.next = head
            head = current

            current1 = current1.next

        if carry:
            current = ListNode(carry)
            current.next = head
            head = current
        return head
