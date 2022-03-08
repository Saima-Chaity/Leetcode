# Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.'''

# Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1


# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        depth = 0
        stack = []
        stack.append((root, 1))
        while stack:
            node, currentDepth = stack.pop()
            if node:
                depth = max(depth, currentDepth)
                stack.append((node.left, currentDepth + 1))
                stack.append((node.right, currentDepth + 1))
        return depth


# Another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        self.max_depth = float('-inf')

        def getMaxDepth(root):
            if not root:
                return 0

            leftDepth = getMaxDepth(root.left)
            rightDepth = getMaxDepth(root.right)
            self.max_depth = max(self.max_depth, max(leftDepth, rightDepth) + 1)
            return max(leftDepth, rightDepth) + 1

        getMaxDepth(root)
        return self.max_depth