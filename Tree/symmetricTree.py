# Symmetric Tree - https://leetcode.com/problems/symmetric-tree/
'''Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3'''

# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        stack = []
        while (1):
            while root1 and root2:
                if root1.val != root2.val:
                    return False
                stack.append(root1)
                stack.append(root2)
                root1 = root1.left
                root2 = root2.right

            if not (root1 is None and root2 is None):
                return False

            if len(stack) > 0:
                rootItem2 = stack.pop()
                rootItem1 = stack.pop()
                root1 = rootItem1.right
                root2 = rootItem2.left
            else:
                break
        return True


# Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and\
               self.isMirror(root1.left, root2.right) and\
               self.isMirror(root1.right, root2.left)

