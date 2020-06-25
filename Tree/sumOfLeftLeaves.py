# Sum of Left Leaves - https://leetcode.com/problems/sum-of-left-leaves/
'''Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.'''

# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0

        def isLeafNode(node):
            return node and not node.left and not node.right

        stack = [root]
        leftLeavesSum = 0
        while stack:
            node = stack.pop()
            if isLeafNode(node.left):
                leftLeavesSum += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leftLeavesSum


#Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def subTree(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if isLeft else 0
            return subTree(node.left, True) + subTree(node.right, False)
        return subTree(root, False)