# Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/
'''Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert
the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the
new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after
insertion. You can return any of them.

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        x = root
        y = None
        while x is not None:
            y = x
            if x.val > val:
                x = x.left
            else:
                x = x.right

        if y is None:
            y = new_node
        elif y.val > val:
            y.left = new_node
        else:
            y.right = new_node
        return root if root else y