# Reverse Only Letters - https://leetcode.com/problems/reverse-only-letters/
'''Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.

Input: "ab-cd"
Output: "dc-ba"'''


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        stringwithLetter = ""
        stack = []
        for index, char in enumerate(S):
            if char.isalpha():
                stack.append(char)

        S = list(S)

        for char in S:
            if char.isalpha():
                stringwithLetter += stack.pop()
            else:
                stringwithLetter += char
        return stringwithLetter
