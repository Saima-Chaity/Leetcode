# Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()[]{}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        map = { ")": "(", "}":"{", "]":"["}
        for bracket in s:
            if bracket in map.values():
                stack.append(bracket)
            elif bracket in map.keys():
                if len (stack) == 0 or map[bracket] != stack.pop():
                    return False
        return len(stack) == 0

