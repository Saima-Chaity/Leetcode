# Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/
'''Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5'''


class Solution:
    def calculate(self, s: str) -> int:

        s = s.strip()
        result = 0
        currentNumber = 0
        sign = "+"
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char.isdigit() and char != " ":
                currentNumber = (currentNumber * 10) + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(currentNumber)
                elif sign == "-":
                    stack.append(-currentNumber)
                elif sign == "*":
                    stack.append(stack.pop() * currentNumber)
                elif sign == "/":
                    stack.append(math.trunc(stack.pop() / currentNumber))

                currentNumber = 0
                sign = char

        while stack:
            result += stack.pop()
        return result

# Without stack
class Solution:
    def calculate(self, s: str) -> int:

        result = 0
        currentNumber = 0
        temp = 0
        sign = "+"

        for i in range(len(s)):
            char = s[i]
            if char.isdigit() and char != " ":
                currentNumber = (currentNumber * 10) + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    result += temp
                    temp = currentNumber
                elif sign == "-":
                    result += temp
                    temp = -currentNumber
                elif sign == "*":
                    temp *= currentNumber
                elif sign == "/":
                    temp = math.trunc(temp / currentNumber)

                currentNumber = 0
                sign = char
        return result + temp






