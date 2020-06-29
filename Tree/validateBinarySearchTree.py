# Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/
'''Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        stack = []
        minValue = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            poppedItem = stack.pop(-1)
            if poppedItem.val <= minValue:
                return False
            minValue = poppedItem.val
            root = poppedItem.right
        return len(stack) == 0