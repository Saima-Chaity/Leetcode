'''Maximum Product of Splitted Binary Tree https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the
product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        product = float('-inf')

        def getMaxProduct(root):
            nonlocal product
            if not root:
                return 0
            leftSum = getMaxProduct(root.left)
            rightSum = getMaxProduct(root.right)
            total_sum = leftSum + rightSum + root.val
            all_sums.append(total_sum)
            return total_sum

        all_sums = []
        total = getMaxProduct(root)
        for s in all_sums:
            product = max(product, s * (total - s))
        return product % (10 ** 9 + 7)