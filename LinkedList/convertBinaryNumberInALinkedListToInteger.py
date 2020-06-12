'''Convert Binary Number in a Linked List to Integer -
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        if not head:
            return 0

        nodes = []
        output = 0

        while head:
            nodes.insert(0, head.val)
            head = head.next

        for index, node in enumerate(nodes):
            if node:
                output += 2 ** index
        return output