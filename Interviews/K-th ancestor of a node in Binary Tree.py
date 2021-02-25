'''K-th ancestor of a node in Binary Tree

Given a binary tree in which nodes are numbered from 1 to n. Given a node and a positive integer K.
We have to print the K-th ancestor of the given node in the binary tree. If there does not exist any
such ancestor then print -1.
'''

from collections import deque
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getAncestors(root, ancestors):
    ancestors[root.data] = -1
    q = deque([root])
    while q:
        node = q.popleft()
        if node.left:
            ancestors[node.left.data] = node.data
            q.append(node.left)

        if node.right:
            ancestors[node.right.data] = node.data
            q.append(node.right)


def kthAncestor(root, length, k, node):
    ancestors = [0] * (length + 1)
    getAncestors(root, ancestors)
    count = 0
    print(ancestors)
    while node != -1:
        node = ancestors[node]
        count += 1
        if count == k:
            break
    return node


if __name__ == '__main__':
    # Let us create binary tree shown
    # in above diagram
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)

    k = 1
    node = 4

    # prkth ancestor of given node
    print(kthAncestor(root, 5, k, node))