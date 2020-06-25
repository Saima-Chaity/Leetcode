# Invert Binary Tree - https://leetcode.com/problems/invert-binary-tree/
'''Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1'''


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()
            left = node.left
            right = node.right
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            node.left = right
            node.right = left
        return root