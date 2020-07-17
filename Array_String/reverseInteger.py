# Reverse Integer - https://leetcode.com/problems/reverse-integer/
'''Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321'''

class Solution:
    def reverse(self, x: int) -> int:
        maxInt = 2 ** 31 - 1
        minInt = - 2 ** 31
        reversedInt = 0

        if x < 0:
            x = -1 * x
            intToStr = str(x)
            reversedStr = "-" + intToStr[::-1]
            reversedInt = int(reversedStr)
        elif x > 0:
            intToStr = str(x)
            reversedStr = intToStr[::-1]
            reversedInt = int(reversedStr)

        if reversedInt > maxInt or reversedInt < minInt:
            return 0
        else:
            return reversedInt
