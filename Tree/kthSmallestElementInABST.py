# Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3'''

# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


# Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def inorder(node):
            if node:
                inorder(node.left)
                self.k -= 1
                if not self.k:
                    self.output = node.val
                    return
                inorder(node.right)
        self.k = k
        inorder(root)
        return self.output