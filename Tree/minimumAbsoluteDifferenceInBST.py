# Minimum Absolute Difference in BST - https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''Given a binary search tree with non-negative values, find the minimum absolute difference
between values of any two nodes.

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

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
                minDiff = min(minDiff, abs(current.val - prev.val))
            prev = current
            current = current.right
        return minDiff