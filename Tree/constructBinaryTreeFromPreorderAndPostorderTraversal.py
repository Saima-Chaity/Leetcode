'''Construct Binary Tree from Preorder and Postorder Traversal -
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]'''

# Iterative
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        stack = [TreeNode(pre[0])]
        postIndex = 0
        for i in pre[1:]:
            node = TreeNode(i)
            while stack[-1].val == post[postIndex]:
                stack.pop()
                postIndex += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

# Recursive
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    postIndex = 0
    preIndex = 0
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        if root.val != post[self.postIndex]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[self.postIndex]:
            root.right = self.constructFromPrePost(pre, post)
        self.postIndex += 1
        return root
