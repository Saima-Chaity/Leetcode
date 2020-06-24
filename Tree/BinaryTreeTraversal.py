# Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/
'''Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        current = root
        output = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            output.append(current.val)
            current = current.right
        return output


# Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/
'''Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        current = root
        output = []

        while current or stack:
            while current:
                output.append(current.val)
                stack.append(current)
                current = current.left

            current = stack.pop()
            current = current.right
        return output


# Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/
'''Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        stack = []
        output = []

        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            node = stack.pop()
            if stack and stack[-1] is node.right:
                root = stack.pop()
                stack.append(node)
            else:
                output.append(node.val)
        return output


# Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
'''Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        output = []
        level = 0
        queue = deque([root])
        while queue:
            output.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                output[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return output