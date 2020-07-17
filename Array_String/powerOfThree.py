# Power of Three - https://leetcode.com/problems/power-of-three/
'''Given an integer, write a function to determine if it is a power of three.

Input: 27
Output: true'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 0:
            return False

        while (n % 3 == 0):
            n = n / 3
        return n == 1