# Add Binary - https://leetcode.com/problems/add-binary/
'''Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        maxLength = max(len(a), len(b))
        a = a.zfill(maxLength)
        b = b.zfill(maxLength)
        carry = 0
        output = ""
        for i in range(maxLength - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                output += "1"
            else:
                output += "0"

            carry //= 2

        if carry:
            output += str(carry)
        return output[::-1]
