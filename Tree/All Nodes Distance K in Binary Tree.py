# All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
'''We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 '''

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        def dfs(node, parent):
            if not node:
                return -1

            nodeArr = [parent, -1, -1]  # Adjacent list of a node [parent, left, right value]
            if node.left:
                nodeArr[1] = node.left.val
                dfs(node.left, node.val)
            if node.right:
                nodeArr[2] = node.right.val
                dfs(node.right, node.val)
            mapping[node.val] = nodeArr

        mapping = {}
        dfs(root, -1)
        if target.val not in mapping:
            return []

        q = deque([(target.val, 0)])
        seen = set()
        output = []
        while q:
            node, steps = q.popleft()
            if node not in seen:
                seen.add(node)
                if steps == K and node > -1:  # parent of root node is -1
                    output.append(node)
                elif steps < K:
                    if node in mapping:
                        for neighbour in mapping[node]:
                            if neighbour not in seen:
                                q.append((neighbour, steps + 1))
        return output


