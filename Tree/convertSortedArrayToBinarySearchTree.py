# Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None

        def convertToBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            if left == right:
                return node
            node.left = convertToBST(left, mid - 1)
            node.right = convertToBST(mid + 1, right)
            return node
        return convertToBST(0, len(nums) - 1)


# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        root = TreeNode(0)
        stack = []
        stack.append(root)
        stack.append(left)
        stack.append(right)

        while stack:
            right = int(stack.pop())
            left = int(stack.pop())
            node = stack.pop()
            mid = left + ((right - left) // 2)
            node.val = nums[mid]

            if left <= mid - 1:
                node.left = TreeNode(0)
                stack.append(node.left)
                stack.append(left)
                stack.append(mid - 1)

            if right >= mid + 1:
                node.right = TreeNode(0)
                stack.append(node.right)
                stack.append(mid + 1)
                stack.append(right)
        return root


