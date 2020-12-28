# Pow(x, n) - https://leetcode.com/problems/powx-n/
'''Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000'''

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1/x
            n = abs(n)

        result = 1
        currentProduct = x
        while n:
            if n % 2 == 1:
                result = result * currentProduct
            currentProduct *= currentProduct
            n = n // 2
        return result