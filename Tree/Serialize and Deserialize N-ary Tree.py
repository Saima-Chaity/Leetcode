'''Serialize and Deserialize N-ary Tree
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node
has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to
the original tree structure.

For example, you may serialize the following 3-ary tree

as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated
by the null value.

For example, the above tree may be serialized as
[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

'''

from collections import deque

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''

        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node != ",":
                result.append(str(node.val))
                for child in node.children:
                    q.append(child)
                q.append(",")
            else:
                result.append(",")
        return "#".join(result)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        spiltedData = data.split("#")
        index = 1
        root = Node(int(spiltedData[0]), [])
        q = deque([root])
        while q:
            node = q.popleft()
            while spiltedData[index] != ",":
                child = Node(int(spiltedData[index]), [])
                node.children.append(child)
                q.append(child)
                index += 1
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))