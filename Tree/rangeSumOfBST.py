# Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/
'''Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return -1
        stack = [root]
        totalSum = 0
        while stack:
            current = stack.pop()
            if current:
                if L <= current.val <= R:
                    totalSum += current.val
                if current.val > L:
                    stack.append(current.left)
                if current.val < R:
                    stack.append(current.right)
        return totalSum


# Recursive Implementation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        self.result = 0

        def inorder(root):
            if root:
                inorder(root.left)
                if root.val >= low and root.val <= high:
                    self.result += root.val
                inorder(root.right)

        inorder(root)
        return self.result



