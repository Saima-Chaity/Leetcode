# Find Mode in Binary Search Tree - https://leetcode.com/problems/find-mode-in-binary-search-tree/
'''Given a binary search tree (BST) with duplicates, find all the mode(s)
(the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.'''

from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        mapping = Counter()

        def dfs(root):
            if root:
                mapping[root.val] += 1
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        maxValue = max(mapping.values())
        return [key for key, value in mapping.items() if value == maxValue]