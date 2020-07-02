# Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and
node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this
node's descendants. The tree s could also be considered as a subtree of itself.

Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True

        def checkTree(s, t):
            if not s and not t:
                return True
            elif not s and t or s and not t:
                return False
            elif s.val != t.val:
                return False
            return checkTree(s.left, t.left) and checkTree(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False
            if s.val == t.val and checkTree(s, t):
                return True
            return dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)

