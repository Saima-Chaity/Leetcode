# Multiply Strings - https://leetcode.com/problems/multiply-strings/
'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1_length = len(num1)
        num2_length = len(num2)
        output = [0] * (num1_length + num2_length)

        for i in range(num1_length - 1, -1, -1):
            for j in range(num2_length - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                index = i + j + 1
                output[index] += product
                output[index - 1] += output[index] // 10  # bring out carry number to the left array
                output[index] %= 10  # remove the carry out from the current array

        # Remove trailing zero
        i = 0
        while i < (num1_length + num2_length) and output[i] == 0:
            i += 1

        # In case the product is zero
        if i == (num1_length + num2_length):
            return "0"
        return "".join(map(str, output[i:]))
