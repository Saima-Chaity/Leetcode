# Same Tree - https://leetcode.com/problems/same-tree/
'''Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        stack = [(p, q)]
        while stack:
            root1, root2 = stack.pop()
            if root1 and root2 and root1.val == root2.val:
                stack.extend([
                    (root1.left, root2.left),
                    (root1.right, root2.right)
                ])
            elif root1 or root2:
                return False
        return True