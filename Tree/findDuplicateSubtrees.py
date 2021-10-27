# Find Duplicate Subtrees - https://leetcode.com/problems/find-duplicate-subtrees/
'''Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only
need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return None

        added = set()
        duplicate = set()
        output = []

        def postOrder(root):
            if not root:
                return "#"
            leftTree = postOrder(root.left)
            rightTree = postOrder(root.right)
            current = leftTree + rightTree + "#" + str(root.val)
            if current in duplicate and current not in added:
                added.add(current)
                output.append(root)
            else:
                duplicate.add(current)
            return current

        postOrder(root)
        return output


# Another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        count = collections.Counter()
        output = []

        def checkNode(node):
            if not node:
                return "#"
            current = "{},{},{}".format(node.val, checkNode(node.left), checkNode(node.right))
            count[current] += 1
            if count[current] == 2:
                output.append(node)
            return current

        checkNode(root)
        return output