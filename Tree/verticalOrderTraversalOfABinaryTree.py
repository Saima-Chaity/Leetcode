# Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
'''Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report
the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]'''

# DFS
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

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
            result.append(value for row, value in sorted(groups[x]))
        return result


# Partial sorting
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        group = defaultdict(list)
        q = deque([(root, 0, 0)])
        result = []
        min_x, max_x = float('inf'), float('-inf')
        while q:
            for _ in range(len(q)):
                node, x, y = q.popleft()
                if node:
                    group[x].append((y, node.val))
                    min_x = min(x, min_x)
                    max_x = max(x, max_x)
                    if node.left:
                        q.append((node.left, x - 1, y + 1))
                    if node.right:
                        q.append((node.right, x + 1, y + 1))

        for i in range(min_x, max_x + 1):
            result.append(value for y, value in sorted(group[i]))
        return result
