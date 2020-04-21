# Inorder Successor in BST - https://leetcode.com/problems/inorder-successor-in-bst/

'''Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        current = root
        stack = []
        inorder = float('-inf')

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if inorder == p.val:
                return current
            inorder = current.val
            current = current.right

        return None

        # current = root
        # candidate = None
        # while current:
        #     if current.val > p.val:
        #         candidate = current
        #         current = current.left
        #     else:
        #         current = current.right
        # return candidate