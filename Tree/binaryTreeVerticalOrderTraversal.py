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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        group = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            for _ in range(len(q)):
                node, x = q.popleft()
                if node:
                    group[x].append(node.val)
                    if node.left:
                        q.append((node.left, x - 1))
                    if node.right:
                        q.append((node.right, x + 1))

        result = []
        for key, value in sorted(group.items()):
            result.append(value)
        return result


# Without sorting
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
        q = deque([(root, 0)])
        minX = maxX = 0
        while q:
            for _ in range(len(q)):
                node, x = q.popleft()
                if node:
                    group[x].append(node.val)
                    minX = min(x, minX)
                    maxX = max(x, maxX)
                    if node.left:
                        q.append((node.left, x - 1))
                    if node.right:
                        q.append((node.right, x + 1))

        result = []
        for i in range(minX, maxX + 1):
            result.append(group[i])
        return result


# DFS
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        groups = defaultdict(list)
        min_x = float('inf')
        max_x = float('-inf')

        def getVerticalOrder(node, x, y):
            nonlocal max_x, min_x
            if node:
                groups[x].append((y, node.val))
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                getVerticalOrder(node.left, x - 1, y + 1)
                getVerticalOrder(node.right, x + 1, y + 1)

        getVerticalOrder(root, 0, 0)
        result = []
        for x in range(min_x, max_x + 1):
            groups[x].sort(key=lambda x: x[0])
            result.append(value for row, value in groups[x])
        return result

