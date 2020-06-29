# Flatten Binary Tree to Linked List - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6'''


# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left:
                rightMost = node.left
                while rightMost.right:
                    rightMost = rightMost.right
                rightMost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

# Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flattenTree(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node

            leftTail = flattenTree(node.left)
            rightTail = flattenTree(node.right)
            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            return rightTail if rightTail else leftTail

        return flattenTree(root)


