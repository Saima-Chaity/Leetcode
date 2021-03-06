# Binary Tree Vertical Order Traversal- https://leetcode.com/problems/binary-tree-vertical-order-traversal/
'''Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
Examples 1:
Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
'''

from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        group = defaultdict(list)
        q = deque([(root, 0, 0)])
        while q:
            node, x, y = q.popleft()
            group[x].append((node.val, y))
            if node:
                if node.left:
                    q.append((node.left, x - 1, y + 1))
                if node.right:
                    q.append((node.right, x + 1, y + 1))

        results = []
        for x in (sorted(group)):
            results.append(group[x])

        for index, item in enumerate(results):
            item.sort(key=lambda x: x[1])
            results[index] = [value for value, depth in item]
        return results
