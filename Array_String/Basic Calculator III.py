# Basic Calculator III - https://leetcode.com/problems/basic-calculator-iii/
'''Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses )
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in
the range of [-2147483648, 2147483647].

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 6-4 / 2 "
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
Example 4:

Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12'''


class Solution:
    def calculate(self, s: str) -> int:

        def updateValue(sign, number):
            if sign == "+":
                stack.append(number)
            elif sign == "-":
                stack.append(-number)
            elif sign == "*":
                stack.append(stack.pop() * number)
            elif sign == "/":
                stack.append(int(stack.pop() / number))

        currentNumber = 0
        sign = "+"
        stack = []
        signs = set('+-/*')

        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                currentNumber = (currentNumber * 10) + int(char)
            elif char in signs or char == ")":
                updateValue(sign, currentNumber)
                currentNumber = 0
                sign = char
                if char == ")":
                    result = 0
                    while stack and stack[-1] not in signs:
                        result += stack.pop()
                    updateValue(stack.pop(), result)
            elif char == "(":
                stack.append(sign)
                currentNumber = 0
                sign = "+"

        updateValue(sign, currentNumber)
        return sum(stack)
