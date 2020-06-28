# Trim a Binary Search Tree - https://leetcode.com/problems/trim-a-binary-search-tree/
'''Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements
lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the
trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
'''

#Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def trim(node):
            if not node:
                return None
            if node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return node

        return trim(root)

#Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        #Preorder Traversal
        if not root:
            return None
        nodeWithinRange = []
        stack = []
        while root or stack:
            while root:
                if L <= root.val <= R:
                    nodeWithinRange.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right

        #Construct Binary Search Tree from Preorder Traversal
        root = TreeNode(nodeWithinRange[0])
        stack = [root, ]
        for i in range(1, len(nodeWithinRange)):
            node, child = stack[-1], TreeNode(nodeWithinRange[i])
            while stack and stack[-1].val < child.val:
                node = stack.pop()
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root