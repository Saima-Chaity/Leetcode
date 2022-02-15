'''Longest Valid Parentheses - https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest
valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0'''

# Two pointer
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left = 0
        right = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif right > left:
                left = right = 0

        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left > right:
                left = right = 0
        return maxLength


# Using stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        stack.append(-1)
        maxLength = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLength = max(maxLength, i - stack[-1])
        return maxLength