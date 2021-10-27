'''Remove Outermost Parentheses - https://leetcode.com/problems/remove-outermost-parentheses/

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses
strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into
s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where
Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
'''


class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        openingBracket = 0
        closingBracket = 0
        result = ""
        new_string = ""
        for i in range(len(list(s))):
            if s[i] == "(":
                openingBracket += 1
                new_string += s[i]
            else:
                closingBracket += 1
                new_string += s[i]
                if openingBracket == closingBracket:
                    current = new_string[1:len(new_string) - 1]
                    result += current
                    new_string = ""
                    openingBracket = 0
                    closingBracket = 0
        return result