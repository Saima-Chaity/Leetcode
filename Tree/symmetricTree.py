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
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        result = False
        q = deque([(root.left, root.right)])
        while q:
            nodeLeft, nodeRight = q.popleft()
            if nodeLeft and nodeRight:
                result = nodeLeft.val == nodeRight.val
                q.append((nodeLeft.left, nodeRight.right))
                q.append((nodeLeft.right, nodeRight.left))
                if not result:
                    return False
            elif not nodeLeft and not nodeRight:
                result = True
            elif not nodeLeft or not nodeRight:
                return False
        return result


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

