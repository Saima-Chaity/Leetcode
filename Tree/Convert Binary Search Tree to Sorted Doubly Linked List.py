'''Convert Binary Search Tree to Sorted Doubly Linked List -
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a
doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last
element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node
should point to its predecessor, and the right pointer should point to its successor. You should return
the pointer to the smallest element of the linked list.

Example 1:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None

        prev = dummy = TreeNode(0)
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    prev.right = root
                    root.left = prev
                    prev = root
                    root = root.right
            else:
                prev.right = root
                root.left = prev
                prev = root
                root = root.right

        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right

# Recursion
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        dummy = prev = Node(0)
        def inorder(root):
            nonlocal prev
            if root:
                inorder(root.left)
                node = root
                prev.right = node
                node.left = prev
                prev = node
                inorder(root.right)

        inorder(root)
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right

# Another approach
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None

        prev = dummy = TreeNode(0)
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            current = root
            prev.right = current
            current.left = prev
            prev = current
            root = root.right

        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right