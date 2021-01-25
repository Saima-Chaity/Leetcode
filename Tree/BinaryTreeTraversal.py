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
                # push nodes: right -> node -> left
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            node = stack.pop()
            # if the right subtree is not yet processed
            if stack and stack[-1] is node.right:
                root = stack.pop()
                stack.append(node)
            # if we're on the leftmost leaf
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


# Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        levels = []
        if not root:
            return levels

        def _levelOrder(root, level):

            if len(levels) == level:
                levels.append([])

            levels[level].append(root.val)
            if root.left:
                _levelOrder(root.left, level + 1)
            if root.right:
                _levelOrder(root.right, level + 1)

        _levelOrder(root, 0)
        return levels


# Binary Tree Level Order Traversal II - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return output[::-1]

# Another solution - using array.insert()
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        output = []
        while q:
            output.insert(0, [])
            for i in range(len(q)):
                node = q.pop(0)
                output[0].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return output