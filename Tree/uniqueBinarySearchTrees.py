# Unique Binary Search Trees - https://leetcode.com/problems/unique-binary-search-trees/
'''Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3'''


class Solution:
    def numTrees(self, n: int) -> int:

        T = [0] * (n + 1)
        T[0] = 1
        T[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                T[i] += T[j - 1] * T[i - j]
        return T[n]


# Unique Binary Search Trees II - https://leetcode.com/problems/unique-binary-search-trees-ii/
'''Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate_tree(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                leftTree = generate_tree(start, i - 1)
                rightTree = generate_tree(i + 1, end)
                for left in leftTree:
                    for right in rightTree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        allTrees.append(root)
            return allTrees
        return generate_tree(1, n) if n else []