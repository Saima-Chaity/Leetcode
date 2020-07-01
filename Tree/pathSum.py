# Path Sum - https://leetcode.com/problems/path-sum/
'''Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])
        while queue:
            node, total = queue.popleft()
            if total == sum and not node.left and not node.right:
                return True
            if node.left:
                queue.append((node.left, total + node.left.val))
            if node.right:
                queue.append((node.right, total + node.right.val))
        return False


# Path Sum II - https://leetcode.com/problems/path-sum-ii/
'''Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, root.val, [root.val])])
        output = []
        while queue:
            node, total, path = queue.popleft()
            if total == sum and not node.left and not node.right:
                output.append(path)
            if node.left:
                queue.append((node.left, total+node.left.val, path+[node.left.val]))
            if node.right:
                queue.append((node.right, total+node.right.val, path+[node.right.val]))
        return output