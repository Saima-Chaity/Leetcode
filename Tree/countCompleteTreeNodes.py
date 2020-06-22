# Count Complete Tree Nodes - https://leetcode.com/problems/count-complete-tree-nodes/
'''Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def depth(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d

        count = 0
        while root:
            left_height = depth(root.left)
            right_height = depth(root.right)
            if left_height == right_height:
                count += 2 ** left_height
                root = root.right
            else:
                count += 2 ** right_height
                root = root.left
        return count
