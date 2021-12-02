'''Construct Binary Tree from String - https://leetcode.com/problems/construct-binary-tree-from-string/

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        if not s:
            return None

        def getValue(s, index):
            number = 0
            isNegative = False
            if s[index] == "-":
                isNegative = True
                index += 1

            while index < len(s) and s[index].isdigit():
                number = number * 10 + int(s[index])
                index += 1
            return number if not isNegative else -number, index

        root = TreeNode()
        stack = [root]
        index = 0
        while index < len(s):
            node = stack.pop()
            if s[index].isdigit() or s[index] == "-":
                value, index = getValue(s, index)
                node.val = value

                if index < len(s) and s[index] == "(":
                    stack.append(node)
                    node.left = TreeNode()
                    stack.append(node.left)
            elif node.left and s[index] == "(":
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)
            index += 1
        return stack.pop() if stack else root