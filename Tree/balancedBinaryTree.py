# Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/
'''Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.output = True
        def getDepth(root):
            if not root or not self.output:
                return 0
            left = getDepth(root.left)
            right = getDepth(root.right)
            if abs(left - right) > 1:
                self.output = False
            return 1 + max(left, right)
        getDepth(root)
        return self.output