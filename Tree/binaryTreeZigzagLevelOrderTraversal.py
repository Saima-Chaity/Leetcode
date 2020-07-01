'''Binary Tree Zigzag Level Order Traversal -
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        output = []
        level = 0
        queue = deque([(root, level)])
        while queue:
            output.append([])
            for i in range(len(queue)):
                node, level = queue.popleft()
                if level % 2 == 0:
                    output[level].append(node.val)
                else:
                    output[level].insert(0, node.val)
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
            level += 1
        return output