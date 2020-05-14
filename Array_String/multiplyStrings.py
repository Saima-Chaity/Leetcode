# Multiply Strings - https://leetcode.com/problems/multiply-strings/
'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        length1 = len(num1)
        length2 = len(num2)

        output = [0] * (length1 + length2)

        for i in range(length1 - 1, -1, -1):
            num_i = num1[i]
            for j in range(length2 - 1, -1, -1):
                num_j = num2[j]
                product = int(num_i) * int(num_j)
                index = i + j + 1
                output[index] += product
                output[index - 1] += output[index] // 10
                output[index] %= 10

        # Remove trailing zero
        i = 0
        while i < (length1 + length2) and output[i] == 0:
            i += 1

        # In case the product is zero
        if i == length1 + length2:
            return "0"

        return "".join(map(str, output[i:]))
