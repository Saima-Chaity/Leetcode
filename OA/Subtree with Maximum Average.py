'''
Subtree with Maximum Average
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. The average
value of a subtree is the sum of its values, divided by the number of nodes.

Example 1:

Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.
'''

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


