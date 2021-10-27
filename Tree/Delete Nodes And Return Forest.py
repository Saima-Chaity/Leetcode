'''Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 '''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        forest = set([root])
        to_delete = set(to_delete)

        def preorder(root):
            if root.val in to_delete:
                if root in forest:
                    forest.remove(root)
                if root.left:
                    forest.add(root.left)
                if root.right:
                    forest.add(root.right)

            if root.left:
                preorder(root.left)
                if root.left.val in to_delete:
                    root.left = None
            if root.right:
                preorder(root.right)
                if root.right.val in to_delete:
                    root.right = None
            return root

        preorder(root)
        return list(forest)

# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        forest = set([root])
        to_delete = set(to_delete)
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            if root.left:
                stack.append(root.left)
                if root.left.val in to_delete:
                    root.left = None

            if root.right:
                stack.append(root.right)
                if root.right.val in to_delete:
                    root.right = None

            if root.val in to_delete:
                if root in forest:
                    forest.remove(root)
                if root.left:
                    forest.add(root.left)
                if root.right:
                    forest.add(root.right)

        return list(forest)


