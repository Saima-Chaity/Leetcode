# Binary Tree Longest Consecutive Sequence - https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
'''Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along
the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.'''

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:

        if not root:
            return 0

        q = deque()
        q.append((root, 1))
        longestLength = float('-inf')

        while q:
            node, length = q.popleft()
            longestLength = max(longestLength, length)
            if node:
                if node.left:
                    if node.val + 1 == node.left.val:
                        q.append((node.left, length + 1))
                    else:
                        q.append((node.left, 1))
                if node.right:
                    if node.val + 1 == node.right.val:
                        q.append((node.right, length + 1))
                    else:
                        q.append((node.right, 1))
        return longestLength


# Binary Tree Longest Consecutive Sequence II - https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
'''
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] 
are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be 
in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        def getLongestLength(node):
            nonlocal longestLength
            if not node:
                return 0, 0
            increament = 1
            decreament = 1
            left_increament, left_decreament = getLongestLength(node.left)
            right_increament, right_decreament = getLongestLength(node.right)
            if node.left:
                if node.val + 1 == node.left.val:
                    increament = max(increament, left_increament + 1)
                if node.val - 1 == node.left.val:
                    decreament = max(decreament, left_decreament + 1)

            if node.right:
                if node.val + 1 == node.right.val:
                    increament = max(increament, right_increament + 1)
                if node.val - 1 == node.right.val:
                    decreament = max(decreament, right_decreament + 1)

            longestLength = max(longestLength, increament + decreament - 1)
            return (increament, decreament)

        longestLength = float('-inf')
        getLongestLength(root)
        return longestLength
