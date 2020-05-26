# Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along
the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        def getSum(node):
            nonlocal maxSum
            if not node:
                return 0

            leftMax = max(getSum(node.left), 0)
            rightMax = max(getSum(node.right), 0)

            totalSum = node.val + leftMax + rightMax
            maxSum = max(maxSum, totalSum)
            return node.val + max(leftMax, rightMax)

        maxSum = float('-inf')
        getSum(root)
        return maxSum

