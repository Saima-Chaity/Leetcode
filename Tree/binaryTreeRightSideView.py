# Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/
'''Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [(root, 0)]
        rightView = dict()
        maxLevel = -1
        while q:
            node, level = q.pop(0)
            if node:
                maxLevel = max(maxLevel, level)
                q.append((node.right, level + 1))
                q.append((node.left, level + 1))
                if level not in rightView:
                    rightView[level] = node.val

        return [rightView[key] for key in range(maxLevel+1)]