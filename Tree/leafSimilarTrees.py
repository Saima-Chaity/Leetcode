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

        if not root1 or not root2:
            return False
        
        def getLeafNodes(root):
            stack = []
            current = root
            output = []

            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left

                current = stack.pop()
                if not current.left and not current.right:
                    output.append(current.val)
                current = current.right
            return output
                
        
        root1_leafNodes = getLeafNodes(root1)
        root2_leafNodes = getLeafNodes(root2)
        
        return root1_leafNodes == root2_leafNodes
        
