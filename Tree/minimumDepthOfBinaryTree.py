# Minimum Depth of Binary Tree - https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        q = []
        q.append({'node': root, 'depth': 1})
        
        while (len(q) > 0):
            queueItem = q.pop(0)
            node = queueItem['node']
            depth = queueItem['depth']
            
            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                q.append({'node': node.left, 'depth': depth + 1})

            if node.right is not None:
                q.append({'node': node.right, 'depth': depth + 1})
