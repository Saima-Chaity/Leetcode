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

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        group = defaultdict(list)
        q = [(root, 0, 0)]
        while q:
            node, x, y = q.pop(0)
            group[x].append((node.val, y))
            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))

        result = []
        for x in sorted(group):
            result.append(group[x])

        for index, item in enumerate(result):
            item.sort(key=lambda x: x[0])
            item.sort(key=lambda x: x[1])
            result[index] = [val for val, depth in item]
        return result


# Another approach
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        groups = []
        q = deque([(root, 0, 0)])
        while q:
            node, x, y = q.popleft()
            if node:
                groups.append((x, y, node.val))
                q.append((node.left, x - 1, y + 1))
                q.append((node.right, x + 1, y + 1))

        groups.sort()
        results = defaultdict(list)
        for x, y, value in groups:
            if x in results:
                results[x].append(value)
            else:
                results[x] = [value]
        return results.values()