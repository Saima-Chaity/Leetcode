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

        def max_gain(root):
            if not root:
                return 0
            
            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(root.left), 0)
            right_gain = max(max_gain(root.right), 0)
            
            max_so_far = root.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, max_so_far)
            return root.val + max(left_gain, right_gain)

        self.max_sum = float('-inf')
        max_gain(root)
        return self.max_sum
