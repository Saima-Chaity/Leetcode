# Path Sum - https://leetcode.com/problems/path-sum/
'''Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])
        while queue:
            node, total = queue.popleft()
            if total == sum and not node.left and not node.right:
                return True
            if node.left:
                queue.append((node.left, total + node.left.val))
            if node.right:
                queue.append((node.right, total + node.right.val))
        return False


# Path Sum II - https://leetcode.com/problems/path-sum-ii/
'''Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, root.val, [root.val])])
        output = []
        while queue:
            node, total, path = queue.popleft()
            if total == sum and not node.left and not node.right:
                output.append(path)
            if node.left:
                queue.append((node.left, total+node.left.val, path+[node.left.val]))
            if node.right:
                queue.append((node.right, total+node.right.val, path+[node.right.val]))
        return output


# Path Sum III - https://leetcode.com/problems/path-sum-iii/
'''You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards 
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11'''

# Iterative
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root:
            return 0

        count = 0
        sum_dict = defaultdict(int)
        sum_dict[0] = 1
        stack = [(root, 0, False)]
        while stack:
            node, currentSum, backTrack = stack.pop()
            if backTrack:
                sum_dict[currentSum] -= 1
                continue
            currentSum += node.val
            count += sum_dict[currentSum - sum]
            sum_dict[currentSum] += 1
            stack.append((None, currentSum, True))
            if node.left:
                stack.append((node.left, currentSum, False))
            if node.right:
                stack.append((node.right, currentSum, False))
        return count

# Recursive
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def preOrder(root, current_sum):
            if not root:
                return
            
            # current prefix sum
            current_sum += root.val
            
            # situation 1:
            # continuous subarray starts 
            # from the beginning of the array
            if current_sum == target:
                self.count += 1
            
            # situation 2:
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            self.count += mapping[current_sum - target]
            
            # add the current sum into hashmap
            # to use it during the child nodes processing
            mapping[current_sum]  += 1
            
            preOrder(root.left, current_sum)
            preOrder(root.right, current_sum)
            
            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            mapping[current_sum] -= 1
        
        self.count = 0
        target = sum
        mapping = defaultdict(int)
        preOrder(root, 0)
        return self.count