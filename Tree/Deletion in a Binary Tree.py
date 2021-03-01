'''Deletion in a Binary Tree
Given a binary tree, delete a node from it by making sure that tree shrinks from the bottom
'''

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

from collections import deque
def deletionBT(root, key):
    def deleteRightMostNode(root, deletedNode):
        q = deque([root])
        while q:
            node = q.popleft()
            if node.data == deletedNode:
                node = None
                return
            if node.left:
                if node.left.data == deletedNode:
                    node.left = None
                    return
                q.append(node.left)
            if node.right:
                if node.right.data == deletedNode:
                    node.right = None
                    return
                q.append(node.right)

    if not root:
        return None

    if not root.left and not root.right:
        if root.data == key:
            root = None
            return
        else:
            return root

    nodeToBeDeleted = None
    q = deque([root])
    while q:
        node = q.popleft()
        if node.data == key:
            nodeToBeDeleted = node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    if nodeToBeDeleted:
        rightMostNode = node.data
        deleteRightMostNode(root, rightMostNode)
        nodeToBeDeleted.data = rightMostNode
    return root


