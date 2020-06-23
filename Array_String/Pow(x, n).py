# Pow(x, n) - https://leetcode.com/problems/powx-n/
'''Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000'''

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        powerOfX = 1
        while n:
            if n % 2:
                powerOfX *= x
            x *= x
            n //= 2
        return powerOfX