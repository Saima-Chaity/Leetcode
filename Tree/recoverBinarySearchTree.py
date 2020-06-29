# Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/
'''Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = predecessor = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if predecessor and root.val < predecessor.val:
                y = root
                if not x:
                    x = predecessor
                else:
                    break
            predecessor = root
            root = root.right
        x.val, y.val = y.val, x.val