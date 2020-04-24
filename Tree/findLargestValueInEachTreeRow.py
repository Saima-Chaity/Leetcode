# Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/
'''You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [root]
        output = []
        maxValue = float('-inf')

        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node:
                    maxValue = max(maxValue, node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            output.append(maxValue)
            maxValue = float('-inf')
        return output