# Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/
'''Given an integer n, return the number of trailing zeroes in n!.

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n > 0:
            n //= 5
            result += n
        return result
