# All Possible Full Binary Trees - https://leetcode.com/problems/all-possible-full-binary-trees/
'''A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is
the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, N: int) -> List[TreeNode]:

        if N not in self.memo:
            result = []
            for l in range(1, N, 2):
                for left in self.allPossibleFBT(l):
                    for right in self.allPossibleFBT(N - 1 - l):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
            self.memo[N] = result
        return self.memo[N]