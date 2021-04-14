'''Valid Parenthesis String - https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true'''


class Solution:
    def checkValidString(self, s: str) -> bool:

        leftCount, rightCount = 0, 0

        for char in s:
            if char in '(*':
                leftCount += 1
            else:
                leftCount -= 1

            if leftCount < 0:
                return False

        if leftCount == 0:
            return True

        for char in reversed(s):
            if char in '*)':
                rightCount += 1
            else:
                rightCount -= 1

            if rightCount < 0:
                return False

        return True