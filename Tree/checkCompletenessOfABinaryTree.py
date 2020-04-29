# Check Completeness of a Binary Tree - https://leetcode.com/problems/check-completeness-of-a-binary-tree/
'''Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last
level ({4, 5, 6}) are as far left as possible.'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False

        q = [root]
        while q[0] != None:
            node = q.pop(0)
            q.append(node.left)
            q.append(node.right)

        while len(q) > 0 and q[0] == None:
            q.pop(0)
        return len(q) == 0

