# Minimum Remove to Make Valid Parentheses - https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
'''Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""

        while stack:
            char, index = stack.pop()
            s[index] = ""

        return "".join(s)


# Without stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def removeInvalid(s, open_parentheses, close_parentheses):
            output = []
            invalidCount = 0
            for i in range(len(s)):
                if s[i] == open_parentheses:
                    invalidCount += 1
                elif s[i] == close_parentheses:
                    if invalidCount == 0:
                        continue
                    invalidCount -= 1
                output.append(s[i])
            return "".join(output)

        s = removeInvalid(s, "(", ")")
        s = removeInvalid(s[::-1], ")", "(")
        return s[::-1]