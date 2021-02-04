# Maximum Average Subtree - https://leetcode.com/problems/maximum-average-subtree/
'''Given the root of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its 
values, divided by the number of nodes.)'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maximumAverageSubtreeInBinaryTree(self, root: TreeNode) -> float:
        self.maxAverage = float('-inf')

        def findMax(root):
            if not root:
                return [0, 0]
            left_sum, left_count = findMax(root.left)
            right_sum, right_count = findMax(root.right)
            total_sum, total_count = left_sum + right_sum + root.val, left_count + right_count + 1
            self.maxAverage = max(self.maxAverage, total_sum / total_count)
            return [total_sum, total_count]

        findMax(root)
        return self.maxAverage


# 		 5
# 	   /   \
# 	  6     1

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(1)

    s = Solution()
    print(s.maximumAverageSubtreeInBinaryTree(root))