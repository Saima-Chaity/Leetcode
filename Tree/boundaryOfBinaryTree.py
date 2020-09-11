# Boundary of Binary Tree - https://leetcode.com/problems/boundary-of-binary-tree/

'''Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes
left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the
right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.
Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists.
If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):

        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leafNode(node):
            if not node:
                return

            dfs_leafNode(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leafNode(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leafNode(root)
        dfs_rightmost(root.right)
        return boundary

# Another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []

        def isLeaf(node):
            return not node.left and not node.right

        def addLeafNodes(node):
            if isLeaf(node):
                result.append(node.val)
            else:
                if node.left:
                    addLeafNodes(node.left)
                if node.right:
                    addLeafNodes(node.right)

        if not isLeaf(root):
            result.append(root.val)
        current = root.left
        while current:
            if not isLeaf(current):
                result.append(current.val)
            if current.left:
                current = current.left
            else:
                current = current.right

        addLeafNodes(root)

        current = root.right
        stack = []
        while current:
            if not isLeaf(current):
                stack.append(current.val)
            if current.right:
                current = current.right
            else:
                current = current.left
        while stack:
            result.append(stack.pop())
        return result
