'''Design an Expression Tree With Evaluate Function
https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that
represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear
before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented
in the array postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree
will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not
remove the Node class; however, you can modify it as you wish, and you can define other classes to
implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of
a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond
to operands (numbers), and internal nodes (nodes with two children) correspond to the
operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations
are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to
support additional operators without making changes to your existing evaluate implementation?

Example 1:

Input: s = ["3","4","+","2","*","7","/"]
Output: 2
Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) = 14/7 = 2.
'''

import abc
from abc import ABC, abstractmethod

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class TreeNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def evaluate(self):
        if self.value not in "+-*/":
            return int(self.value)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if self.value == "+":
            return left + right
        if self.value == "-":
            return left - right
        if self.value == "*":
            return left * right
        return left // right


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for char in postfix:
            node = TreeNode(char)
            if char in "+-*/":
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        return stack.pop()


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
