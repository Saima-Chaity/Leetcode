# Distribute Coins in Binary Tree - https://leetcode.com/problems/distribute-coins-in-binary-tree/
'''Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
(The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:

Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0

        def postOrder(current, parent):
            if not current:
                return None

            postOrder(current.left, current)
            postOrder(current.right, current)

            if current.val < 1:
                self.moves += 1 - current.val
                parent.val -= (1 - current.val)  # take coin from parent
            elif current.val > 1:
                self.moves += current.val - 1
                parent.val += (current.val - 1)  # give coin to parent

        postOrder(root, None)
        return self.moves