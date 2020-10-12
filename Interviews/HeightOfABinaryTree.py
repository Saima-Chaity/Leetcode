# Height of a Binary Tree
# The height of a binary tree is the number of edges between the tree's 
# root and its furthest leaf. For example, the following binary tree is of height.

from collections import deque
def height(root):
    if not root:
        return 0
    q = deque([(root, 0)])
    depth = 0
    while q:
        node, level = q.popleft()
        if node:
            depth = max(depth, level)
            q.append((node.right, level+1))
            q.append((node.left, level+1))
    return depth