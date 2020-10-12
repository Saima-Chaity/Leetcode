# Top View of Binary Tree
# Given a pointer to the root of a binary tree, print the top view of the binary tree.

# The tree as seen from the top the nodes, is called the top view of the tree.

# For example :

#    1
#     \
#      2
#       \
#        5
#       /  \
#      3    6
#       \
#        4
# Top View : 1 2 5 6

from collections import deque
def topView(root):
    #Write your code here
    stack = []
    q = deque([(root, 0)])
    output = {}
    while q:
        node, horizontalDistance = q.popleft()
        if node:
            if horizontalDistance not in output:
                output[horizontalDistance] = node.info
            if node.left:
                q.append((node.left, horizontalDistance-1))
            if node.right:
                q.append((node.right, horizontalDistance+1))

    for i in sorted(output): 
        print(output[i], end = " ")  