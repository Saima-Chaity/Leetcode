'''Construct Binary Tree from Inorder and Postorder Traversal -
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def getTree(startIndex, endIndex):

            if startIndex > endIndex:
                return None

            currentRoot = postorder.pop()
            node = TreeNode(currentRoot)

            if startIndex == endIndex:
                return node

            inorderIndex = inorder.index(currentRoot)

            node.right = getTree(inorderIndex + 1, endIndex)
            node.left = getTree(startIndex, inorderIndex - 1)

            return node

        return getTree(0, len(inorder) - 1)



