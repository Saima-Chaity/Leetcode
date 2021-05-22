'''Count Good Nodes in Binary Tree - https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from root to X there
are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.'''

# Time Complexity - O(n) and space complexity O(n)
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        parent = {}
        parent[root] = float('-inf')
        count = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if node and parent[node] == float('inf') or parent[node] <= node.val:
                count += 1
            if node.left:
                parent[node.left] = max(node.val, parent[node])
                q.append(node.left)
            if node.right:
                parent[node.right] = max(node.val, parent[node])
                q.append(node.right)
        return count


