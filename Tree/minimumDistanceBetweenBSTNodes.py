# Minimum Distance Between BST Nodes - https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the
values of any two different nodes in the tree.

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2,
also between node 3 and node 2.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        stack = []
        current = root
        minDiff = float('inf')
        prev = None
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev:
                minDiff = min(minDiff, current.val - prev.val)
            prev = current
            current = current.right
        return minDiff
