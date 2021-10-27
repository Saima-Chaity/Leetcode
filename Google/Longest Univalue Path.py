'''Longest Univalue Path - https://leetcode.com/problems/longest-univalue-path/

Given the root of a binary tree, return the length of the longest path, where each node in
the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        self.count = 0

        def getCount(root):
            if not root:
                return 0

            leftLength = getCount(root.left)
            rightLength = getCount(root.right)
            leftCount = rightCount = 0
            if root.left and root.val == root.left.val:
                leftCount = leftLength + 1
            if root.right and root.val == root.right.val:
                rightCount = rightLength + 1
            self.count = max(self.count, leftCount + rightCount)
            return max(leftCount, rightCount)

        getCount(root)
        return self.count