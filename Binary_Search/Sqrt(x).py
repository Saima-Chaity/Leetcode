# Sqrt(x) - https://leetcode.com/problems/sqrtx/
'''Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part
of the result is returned.

Input: 4
Output: 2'''

class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        return right

