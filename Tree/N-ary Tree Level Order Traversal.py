# N-ary Tree Level Order Traversal - https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of
children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]'''

from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        output = []
        level = 0
        queue = deque([root])
        while queue:
            output.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                output[level].append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)
            level += 1
        return output