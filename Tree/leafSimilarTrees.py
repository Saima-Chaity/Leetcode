# Leaf-Similar Trees - https://leetcode.com/problems/leaf-similar-trees/
'''Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf
value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        leafNodesOfRoot1 = []
        stack1 = []
        while stack1 or root1:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            root1 = stack1.pop()
            if not root1.left and not root1.right:
                leafNodesOfRoot1.append(root1.val)
            root1 = root1.right

        stack2 = []
        index = 0
        while stack2 or root2:
            while root2:
                stack2.append(root2)
                root2 = root2.left
            root2 = stack2.pop()
            if not root2.left and not root2.right and root2.val != leafNodesOfRoot1[index]:
                return False
            elif not root2.left and not root2.right and root2.val == leafNodesOfRoot1[index]:
                if index < len(leafNodesOfRoot1) - 1:
                    index += 1
            root2 = root2.right
        return True
