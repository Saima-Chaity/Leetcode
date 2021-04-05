# Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/
'''Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = predecessor = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if predecessor and root.val < predecessor.val:
                y = root
                if not x:
                    x = predecessor
                else:
                    break
            predecessor = root
            root = root.right
        x.val, y.val = y.val, x.val


# Another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorderTraversal(node):
            stack = []
            nodes = []

            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left

                node = stack.pop()
                nodes.append(node.val)
                node = node.right
            return nodes

        def findSwappedNode(nodes):
            x = y = -1
            for i in range(len(nodes) - 1):
                if nodes[i + 1] < nodes[i]:
                    y = nodes[i + 1]
                    if x == -1:  # first swap occurence
                        x = nodes[i]
                    else:  # second swap occurence
                        break
            return x, y

        def recoverBST(root, x, y, count):
            if root:
                if root.val == x:
                    root.val = y
                    count -= 1
                elif root.val == y:
                    root.val = x
                    count -= 1
                if count == 0:
                    return

                recoverBST(root.left, x, y, count)
                recoverBST(root.right, x, y, count)

        nodes = inorderTraversal(root)
        x, y = findSwappedNode(nodes)
        recoverBST(root, x, y, 2)


# 0(1) space using Morris Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        x = y = predecessor = pred = None
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right
            else:
                if pred and root.val < pred.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
                root = root.right

        x.val, y.val = y.val, x.val
