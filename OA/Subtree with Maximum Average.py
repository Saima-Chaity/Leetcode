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



'''Given a M-ary tree, find the subtree with the maximum average. Return the root of the subtree.

A subtree of a tree is any node of that tree plus all its descendants. The average value of a subtree 
is the sum of its values, divided by the number of nodes.

NOTE: The answer may be 0, i.e. removing the entire string.

Examples
Example 1:
Input:


Output: 13
Example 2:
Input:


Output: 21
Explanation: For the node with value = 1 we have an average of (- 5 + 21 + 5 - 1) / 5 = 4.

For the node with value = -5 we have an average of (-5 / 1) = -5.

For the node with value = 21 we have an average of (21 / 1) = 21.

For the node with value = 5 we have an average of (5 / 1) = 5.

For the node with value = -1 we have an average of (-1 / 1) = -1.

So the subtree of 21 is the maximum.

'''
class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maximumAverageSubTreeM(self, root: 'TreeNode') -> 'TreeNode':
        res = (float('-inf'), None)
        # -> (sum, num_nodes)
        def dfs(node) :
            nonlocal res
            rec = [dfs(c) for c in node.children if c]
            s = node.val + sum(t[0] for t in rec)
            n = 1 + sum(t[1] for t in rec)
            res = max(res, (s / n, node.val))
            return s, n

        dfs(root)
        return res[1]

    # def maximumAverageSubTree(self, root: 'TreeNode') -> 'TreeNode':
    #     q = deque([(root, root.val, 1)])
    #     maxNode = None
    #     maxValue = float('-inf')
    #     while q:
    #         node, value, count = q.popleft()
    #         if len(node.children) > 0:
    #             for child in node.children:
    #                 q.append((child, value + child.val, count + 1))
    #         else:
    #             if value / count > maxValue:
    #                 maxValue = value / count
    #                 maxNode = node.val
    #     return maxNode



# 		 20
# 	   /   \
# 	 12     18
#   /  |  \   / \
# 11   2   3 15  8
if __name__ == '__main__':
    # n4 = TreeNode(11, [])
    # n5 = TreeNode(2, [])
    # n6 = TreeNode(3, [])
    # n7 = TreeNode(15, [])
    # n8 = TreeNode(8, [])
    # n2 = TreeNode(12, [n4, n5, n6])
    # n3 = TreeNode(18, [n7, n8])
    # n1 = TreeNode(20, [n2, n3])

    # 		  1
    # 	   / | \ \
    # 	 5  21 -5 1
    n8 = TreeNode(-4, [])
    n7 = TreeNode(2, [])
    n6 = TreeNode(2, [])
    n5 = TreeNode(1, [])
    n4 = TreeNode(4, [])
    n2 = TreeNode(13, [n7, n8])
    n3 = TreeNode(-5, [n5, n6])
    n1 = TreeNode(1, [n2, n3, n4])

    s = Solution()
    print(s.maximumAverageSubTreeM(n1)) # Output: 21