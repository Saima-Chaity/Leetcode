'''Smallest Subtree with all the Deepest Nodes -
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them,
so we return it.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        self.result = None
        self.maxDepth = float('-inf')

        def dfs(root, depth):
            if not root:
                return depth
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            self.maxDepth = max(self.maxDepth, left, right)
            if self.maxDepth == left == right:
                self.result = root
            return max(left, right)

        dfs(root, 1)
        return self.result