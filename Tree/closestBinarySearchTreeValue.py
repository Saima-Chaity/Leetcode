# Closest Binary Search Tree Value - https://leetcode.com/problems/closest-binary-search-tree-value/
'''Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        # Iterative Inorder Traversal
        if not root:
            return -1

        minValue = float('-inf')
        current = root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if minValue <= target and target < current.val:
                return min(minValue, current.val, key=lambda x: abs(target - x))
            minValue = current.val
            current = current.right
        return minValue

        # BST
        closestValue = root.val
        while root:
            closestValue = min(root.val, closestValue, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closestValue

