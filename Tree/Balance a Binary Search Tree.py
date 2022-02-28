'''Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/

Given the root of a binary search tree, return a balanced binary search tree with the same node values.
If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def balanceTree(root, nums):
            if len(nums) == 0:
                return
            mid = len(nums) // 2
            root = nums[mid]
            root.left = balanceTree(root.left, nums[:mid])
            root.right = balanceTree(root.right, nums[mid + 1:])
            return root

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            output.append(root)
            inorder(root.right)

        output = []
        inorder(root)

        return balanceTree(root, output)

