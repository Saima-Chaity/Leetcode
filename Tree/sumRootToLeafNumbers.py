# Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, str(root.val))])
        summation = 0
        while queue:
            node, total = queue.popleft()
            if not node.left and not node.right:
                summation += int(total)
            if node.left:
                queue.append((node.left, total+str(node.left.val)))
            if node.right:
                queue.append((node.right, total+str(node.right.val)))
        return summation