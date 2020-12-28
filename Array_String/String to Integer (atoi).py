# String to Integer (atoi) - https://leetcode.com/problems/string-to-integer-atoi/
'''Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace
character is found. Then, starting from this character takes an optional initial plus or minus sign
followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are
ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no
such sequence exists because either str is empty or it contains only whitespace characters, no
conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231
is returned.

Example 1:

Input: str = "42"
Output: 42'''

class Solution:
    def myAtoi(self, s: str) -> int:

        maxInt = 2 ** 31 - 1
        minInt = - 2 ** 31
        s = s.strip()
        if not s:
            return 0
        if s and s[0] == "." or s[0].isalpha():
            return 0

        newString = ""
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                newString += char
            elif char in "+-":
                if not newString:
                    newString += char
                else:
                    break
            elif char == " " and len(newString) > 0:
                break
            elif char.isalpha() or char == "." and len(newString) > 0:
                break

        if newString == "" or newString == "+" or newString == "-":
            return 0
        else:
            result = int(newString)
            if result > maxInt:
                return maxInt
            elif result < minInt:
                return minInt
            return result
