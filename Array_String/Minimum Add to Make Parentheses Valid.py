'''Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    count += 1

        count += len(stack)
        return count


# Another approach
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        opening, closing = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                opening += 1
            elif s[i] == ")":
                if opening:
                    opening -= 1
                else:
                    closing += 1
        return opening + closing
