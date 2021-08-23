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
        minInt = -2 ** 31

        s = s.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == "." or s[0].isalpha():
            return 0

        result = ""
        for index, char in enumerate(s):
            if char.isdigit():
                result += char
            elif char in "+-":
                if not result:
                    result += char
                else:
                    break
            elif char == " " or char == "." or char.isalpha():
                break

        if result == "" or result == "+" or result == "-":
            return 0

        number = int(result)
        if number < minInt:
            return minInt
        elif number > maxInt:
            return maxInt
        else:
            return number

