# Print Binary Tree - https://leetcode.com/problems/print-binary-tree/
'''Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row
it can be put. The column and the row where the root node belongs will separate the rest space into
two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom
part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part
should have the same size. Even if one subtree is none while the other is not, you don't need to print
anything for the none subtree but still need to leave the space as large as that for the other subtree.
However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.

Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]'''

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        row = height(root)
        col = 2 ** row - 1
        output = [["" for i in range(col)] for j in range(row)]
        q = deque([(root, 0, col - 1, 0)])
        while q:
            q_length = len(q)
            for i in range(q_length):
                node, startIndex, endIndex, rowIndex = q.popleft()
                mid = startIndex + (endIndex - startIndex) // 2
                output[rowIndex][mid] = str(node.val)
                if node.left:
                    q.append((node.left, startIndex, mid - 1, rowIndex + 1))
                if node.right:
                    q.append((node.right, mid + 1, endIndex, rowIndex + 1))
        return output

