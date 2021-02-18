'''Divide Two Integers - https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example,
truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer
range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        HALF_MIN_INT = -(2 ** 31) // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []
        powersOfTwo = []
        powerOfTwo = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor
            powerOfTwo += powerOfTwo

        quotient = 0

        # Go from largest double to smallest, checking if the current double fits.
        # into the remainder of the dividend.
        for i in range(len(doubles) - 1, -1, -1):
            if doubles[i] >= dividend:
                # If it does fit, add the current powerOfTwo to the quotient.
                quotient += powersOfTwo[i]
                # Update dividend to take into account the bit we've now removed.
                dividend -= doubles[i]
        return quotient if negatives != 1 else -quotient

