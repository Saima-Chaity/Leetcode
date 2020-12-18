# Add Strings - https://leetcode.com/problems/add-strings/
'''Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        result = []
        while p1 >= 0 or p2 >= 0:
            x = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            y = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            total = x + y + carry
            summation = total % 10
            carry = total // 10
            result.append(summation)
            p1 -= 1
            p2 -= 1

        if carry:
            result.append(carry)

        result = result[::-1]
        return "".join(str(x) for x in result)

