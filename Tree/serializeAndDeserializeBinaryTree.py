'''Serialize and Deserialize Binary Tree -
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
be serialized to a string and this string can be deserialized to the original tree structure.

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"'''

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        result = ""
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
            else:
                result += 'None,'
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        splitedData = data.split(",")
        root = TreeNode(int(splitedData[0]))
        q = deque([root])
        i = 1
        while q and i < len(splitedData):
            node = q.popleft()
            if splitedData[i] != 'None':
                left = TreeNode(int(splitedData[i]))
                node.left = left
                q.append(node.left)
            i += 1
            if splitedData[i] != 'None':
                right = TreeNode(splitedData[i])
                node.right = right
                q.append(node.right)
            i += 1
        return root

# Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))