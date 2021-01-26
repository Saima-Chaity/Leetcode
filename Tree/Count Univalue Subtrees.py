# Count Univalue Subtrees - https://leetcode.com/problems/count-univalue-subtrees/
'''Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:

        if not root:
            return 0

        def isUniValue(root):
            if not root.left and not root.right:
                self.count += 1
                return True

            isUni = True
            if root.left:
                isUni = isUniValue(root.left) and isUni and root.left.val == root.val
            if root.right:
                isUni = isUniValue(root.right) and isUni and root.right.val == root.val

            self.count += isUni
            return isUni

        self.count = 0
        isUniValue(root)
        return self.count