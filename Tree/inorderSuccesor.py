# Inorder Successor in BST - https://leetcode.com/problems/inorder-successor-in-bst/
'''Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        current = root
        stack = []
        inorder = float('-inf')

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if inorder == p.val:
                return current
            inorder = current.val
            current = current.right

        return None

# Another approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if not root:
            return None

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val > p.val:
                return root
            else:
                root = root.right
        return None


# Inorder Successor in BST II - https://leetcode.com/problems/inorder-successor-in-bst-ii/
'''Given a node in a binary search tree, find the in-order successor of that node in the BST.
If that node has no in-order successor, return null.
The successor of a node is the node with the smallest key greater than node.val.
You will have direct access to the node but not to the root of the tree. 
Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 
Follow up:
Could you solve it without looking up any of the node's values?

Example 1:
Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of 
Node type.'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Node has right child
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # Node doesn't have right child
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent