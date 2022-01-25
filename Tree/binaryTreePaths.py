# Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/
'''Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        queue = deque([(root, str(root.val))])
        output = []
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                output.append(path)
            if node.left:
                queue.append((node.left, path +"->"+ str(node.left.val)))
            if node.right:
                queue.append((node.right, path +"->"+ str(node.right.val)))
        return output


# Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []

        def buildTreePath(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    output.append(path)
                else:
                    path += "->"
                    buildTreePath(root.left, path)
                    buildTreePath(root.right, path)

        buildTreePath(root, '')
        return output