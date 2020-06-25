'''Construct Binary Tree from Preorder and Inorder Traversal -
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder and not inorder:
            return None

        def getTree(startIndex, endIndex):
            if startIndex > endIndex:
                return None

            currentRoot = preorder.pop(0)
            node = TreeNode(currentRoot)

            if startIndex == endIndex:
                return node

            inorderIndex = inorder.index(currentRoot)
            node.left = getTree(startIndex, inorderIndex - 1)
            node.right = getTree(inorderIndex + 1, endIndex)
            return node

        return getTree(0, len(inorder) - 1)