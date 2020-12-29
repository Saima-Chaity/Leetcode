# Basic Calculator - https://leetcode.com/problems/basic-calculator/
'''Given a string s representing an expression, implement a basic calculator to evaluate it.

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''


class Solution:
    def calculate(self, s: str) -> int:

        def evaluateExpression(stack):
            total = 0
            topElement = str(stack[-1])
            if len(stack) == 1 and topElement[0] == "-":  # cases when stack = [-1]
                if topElement[1].isdigit():
                    total = stack.pop()
            if stack and topElement.isdigit():
                total = stack.pop()
            while stack and stack[-1] != ")":
                sign = stack.pop()
                if sign == "+":
                    total += stack.pop()
                elif sign == "-":
                    total -= stack.pop()
            return total

        result = 0
        number = 0
        stack = []
        n = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char.isdigit():
                # Forming the number - in reverse order.
                number = (10 ** n * int(char)) + number
                n += 1
            elif char != " ":
                if n:
                    stack.append(number)
                    n = 0
                    number = 0
                if char == "(":
                    result = evaluateExpression(stack)
                    stack.pop()
                    stack.append(result)
                else:
                    stack.append(char)
        if n:
            stack.append(number)
        return evaluateExpression(stack)
