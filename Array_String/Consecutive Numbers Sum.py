'''Consecutive Numbers Sum - https://leetcode.com/problems/consecutive-numbers-sum/
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3
Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
'''


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        '''Approach: The idea is to represent N as a sequence of length L+1 as:
        N = a + (a+1) + (a+2) + .. + (a+L)
        => N = (L+1)*a + (L*(L+1))/2
        => a = (N- L*(L+1)/2)/(L+1)
        We substitute the values of L starting from 1 till L*(L+1)/2 < N
        If we get ‘a’ as a natural number then the solution should be counted.
        '''

        count = 1
        L = 1
        while L * (L + 1) / 2 < n:
            number = (1.0 * n - (L * (L + 1) / 2)) / (L + 1)
            if number - int(number) == 0:
                count += 1
            L += 1
        return count


# Sliding window TLE
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        if n < 3:
            return 1

        array = []
        for i in range(1, (n // 2) + 2):
            array.append(i)

        left = 0
        count = 1
        sumSofar = 0
        for right in range(0, len(array)):
            sumSofar += array[right]
            while sumSofar > n:
                sumSofar -= array[left]
                left += 1
            if sumSofar == n:
                count += 1
        return count

