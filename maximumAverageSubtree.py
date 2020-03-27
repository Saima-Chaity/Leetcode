from collections import deque

class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        self.total_value = val
        self.total_num = 1

class Solution:
    def maximumAverageSubTree(self, root: 'TreeNode') -> 'TreeNode':

        stack1 = deque([])
        stack2 = deque([])

        stack1.append(root)
        maxNode = None
        maxAverage = float('-inf')

        while stack1:
            visit = stack1.pop()
            stack2.append(visit)
            for child in visit.children:
                stack1.append(child)
        while stack2:
            visit = stack2.pop()
            if len(visit.children) > 0:
                for child in visit.children:
                    visit.total_value += child.total_value
                    visit.total_num += child.total_num
                currentAverage = visit.total_value / visit.total_num
                if currentAverage > maxAverage:
                    maxAverage = currentAverage
                    maxNode = visit
        return maxNode

# 		 20
# 	   /   \
# 	 12     18
#   /  |  \   / \
# 11   2   3 15  8
if __name__ == '__main__':
    n4 = TreeNode(11, [])
    n5 = TreeNode(2, [])
    n6 = TreeNode(3, [])
    n7 = TreeNode(15, [])
    n8 = TreeNode(8, [])
    n2 = TreeNode(12, [n4, n5, n6])
    n3 = TreeNode(18, [n7, n8])
    n1 = TreeNode(20, [n2, n3])

    s = Solution()
    print(s.maximumAverageSubTree(n1).val)


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