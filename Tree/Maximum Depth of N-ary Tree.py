'''Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated
by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        result = 0
        while q:
            for i in range(len(q)):
                node, depth = q.popleft()
                result = max(result, depth)
                for child in node.children:
                    q.append((child, depth+1))
        return result


# Recursion
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        def getMaxDepth(root, depth):
            if not root:
                return 0

            for child in root.children:
                getMaxDepth(child, depth + 1)
            self.max_depth = max(self.max_depth, depth)

        self.max_depth = 0
        getMaxDepth(root, 1)
        return self.max_depth