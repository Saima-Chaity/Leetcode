'''All Elements in Two Binary Search Trees - https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

Given two binary search trees root1 and root2, return a list containing all the integers from both trees
sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        output = []
        stack1 = []
        stack2 = []
        while stack1 or stack2 or root1 or root2:
            while root1:
                stack1.append(root1)
                root1 = root1.left

            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right

        return output