'''Diameter of N-Ary Tree - https://leetcode.com/problems/diameter-of-n-ary-tree/
Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree.
This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of
children is separated by the null value.)

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        maxDepth = 0

        def getDiameter(root):
            nonlocal maxDepth
            if len(root.children) == 0:
                return 0

            max_height1 = max_height2 = 0
            for child in root.children:
                parent_height = getDiameter(child) + 1
                if parent_height > max_height1:
                    max_height1, max_height2 = parent_height, max_height1
                elif parent_height > max_height2:
                    max_height2 = parent_height

            maxDepth = max(maxDepth, max_height1 + max_height2)
            return max(max_height1, max_height2)

        getDiameter(root)
        return maxDepth