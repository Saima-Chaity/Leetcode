'''Distance Between Nodes in BST
Given a list of unique integers nums.

Construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST)

Find the distance between two nodes node1 and node2.

Distance is the number of edges between two nodes.

If any of the given nodes does not appear in the BST, return -1.

Input
The input consists of three arguments:

nums: a list of integers representing the nodes list

node1: a integer representing the nodes

node2: a integer representing the nodes

Output
return a integer representing distance between two nodes node1 and node2

Examples
Example 1:
Input:
nums = [2, 1, 3]

node1 = 1

node2 = 3

Output: 2
'''


'''Time complexity: O(h), where h is the height of the tree.
Space complexity: O(h).'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def distanceBetweenTwoNodes(self, nums, node1, node2):

        def getDistance(source, destination):
            path = []
            while source:
                path.append(source.val)
                if source.val == destination:
                    return path
                elif source.val < destination:
                    source = source.right
                else:
                    source = source.left
            return None

        def getLCA(root, node1, node2):
            while True:
                if root.val > node1 and root.val > node2:
                    root = root.left
                elif root.val < node1 and root.val < node2:
                    root = root.right
                else:
                    return root

        def insertInBST(root, node):
            if not root:
                root = TreeNode(node)
            elif root.val > node:
                root.left = insertInBST(root.left, node)
            else:
                root.right = insertInBST(root.right, node)
            return root

        root = None
        for i in range(len(nums)):
            root = insertInBST(root, nums[i])

        lowestCommonAncestors = getLCA(root, node1, node2)
        node_1 = getDistance(lowestCommonAncestors, node1)
        node_2 = getDistance(lowestCommonAncestors, node2)
        return len(set(node_1).symmetric_difference(node_2)) if node_1 and node_2 else -1


nums = [2, 1, 3]
node1 = 1
node2 = 3
print(Solution.distanceBetweenTwoNodes((), nums, node1, node2)) # 2

nums = [2, 1, 3]
node1 = 1
node2 = 4
print(Solution.distanceBetweenTwoNodes((), nums, node1, node2)) # -1

nums = [2, 1, 3]
node1 = 3
node2 = 3
print(Solution.distanceBetweenTwoNodes((), nums, node1, node2)) # 0

nums = [1, 2, 3, 5, 6, 7, 8]
node1 = 1
node2 = 8
print(Solution.distanceBetweenTwoNodes((), nums, node1, node2)) # 8