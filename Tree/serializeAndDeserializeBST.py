# Serialize and Deserialize BST - https://leetcode.com/problems/serialize-and-deserialize-bst/
'''Serialization is the process of converting a data structure or object into a sequence of bits so
that it can be stored in a file or memory buffer, or transmitted across a network connection link to
be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how
your serialization/deserialization algorithm should work. You just need to ensure that a binary search
tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        def preOrder(root):
            return [root.val] + preOrder(root.left) + preOrder(root.right) if root else []

        return ",".join(map(str, preOrder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        splitedData = data.split(',')
        root = None
        for value in splitedData:
            if value != "":
                root = self.deserializeTree(root, int(value))
        return root

    def deserializeTree(self, root, value):
        if not root:
            return TreeNode(value)
        if root.val > value:
            root.left = self.deserializeTree(root.left, value)
        if root.val < value:
            root.right = self.deserializeTree(root.right, value)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))