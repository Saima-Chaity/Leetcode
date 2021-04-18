# Reverse Only Letters - https://leetcode.com/problems/reverse-only-letters/
'''Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.

Input: "ab-cd"
Output: "dc-ba"'''


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        left = 0
        right = len(S) - 1
        S = list(S)
        while left < right:
            if S[left].isalpha() and S[right].isalpha():
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
            elif not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
        return "".join(S)
