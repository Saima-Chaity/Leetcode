'''Find Leaves of Binary Tree - https://leetcode.com/problems/find-leaves-of-binary-tree/

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level
it does not matter the order on which elements are returned.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []

        def getLeaves(root):
            if not root.left and not root.right:
                output[-1].append(root.val)
                root = None
                return root
            if root.left:
                root.left = getLeaves(root.left)
            if root.right:
                root.right = getLeaves(root.right)
            return root

        while root:
            output.append([])
            root = getLeaves(root)
        return output