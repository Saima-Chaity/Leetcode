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


from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque([root])
        output = []
        max_so_far = float('-inf')
        while q:
            qSize = len(q)
            for i in range(qSize):
                node = q.popleft()
                if node:
                    max_so_far = max(max_so_far, node.val)
                    if i == qSize - 1:
                        output.append(max_so_far)
                        max_so_far = float('-inf')
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return output