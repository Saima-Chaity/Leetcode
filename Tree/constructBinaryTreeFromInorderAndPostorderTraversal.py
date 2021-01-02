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

        if not postorder or not inorder:
            return None

        def generateTree(postorder, inorder):
            if not postorder or not inorder:
                return None

            currentNode = postorder.pop()
            root = TreeNode(currentNode)
            inorderIndex = inorder.index(currentNode)
            if root:
                root.right = generateTree(postorder, inorder[inorderIndex + 1:])
                root.left = generateTree(postorder, inorder[:inorderIndex])
            return root

        return generateTree(postorder, inorder)



