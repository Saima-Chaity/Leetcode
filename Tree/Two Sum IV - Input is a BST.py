# Two Sum IV - Input is a BST - https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True'''


### Queue and HashSet
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None

        mapping = set()
        q = []
        q.append(root)

        while q:
            if q[-1] is not None:
                node = q.pop(0)
                if node is not None:
                    if (k - node.val) in mapping:
                        return True
                    mapping.add(node.val)
                    q.append(node.left)
                    q.append(node.right)
            else:
                q.pop()
        return False


###BST
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None
        output = []
        self.inorder(root, output)

        left = 0
        right = len(output) - 1
        while left < right:
            if output[left] + output[right] == k:
                return True
            elif output[left] + output[right] > k:
                right -= 1
            else:
                left += 1
        return False

    def inorder(self, node, output):
        if not node:
            return None

        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)


# Two Sum BSTs - https://leetcode.com/problems/two-sum-bsts/
'''Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second 
tree whose values sum up to a given integer target.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return None

        stack = []
        mapping = set()
        while root1 or stack:
            while root1:
                stack.append(root1)
                root1 = root1.left
            root1 = stack.pop()
            mapping.add(target - root1.val)
            root1 = root1.right

        while root2 or stack:
            while root2:
                stack.append(root2)
                root2 = root2.left
            root2 = stack.pop()
            if root2.val in mapping:
                return True
            root2 = root2.right
        return False

