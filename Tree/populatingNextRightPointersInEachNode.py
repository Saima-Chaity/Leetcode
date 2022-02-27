'''Populating Next Right Pointers in Each Node -
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has
two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next
pointer should be set to NULL.

Initially, all next pointers are set to NULL.'''

# Using previously established next pointers
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        leftMost = root
        while leftMost.left:
            head = leftMost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftMost = leftMost.left
        return root


# Level order traversal
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])
        while q:
            qLength = len(q)
            for i in range(qLength):
                node = q.popleft()
                if node:
                    if i < qLength-1:
                        node.next = q[0]
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return root


# Populating Next Right Pointers in Each Node II - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
'''Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]'''

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])
        while q:
            qLength = len(q)
            for i in range(qLength):
                node = q.popleft()
                if node:
                    if i < qLength-1:
                        node.next = q[0]
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return root


'''0(1) space'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        def processChild(childNode, prev, leftMost):
            if childNode:
                if prev:
                    prev.next = childNode
                else:
                    leftMost = childNode
                prev = childNode
            return prev, leftMost

        if not root:
            return root

        leftMost = root
        while leftMost:
            prev, current = None, leftMost
            leftMost = None
            while current:
                prev, leftMost = processChild(current.left, prev, leftMost)
                prev, leftMost = processChild(current.right, prev, leftMost)
                current = current.next
        return root


