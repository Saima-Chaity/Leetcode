# N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/
'''The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4'''


class Solution:
    def tribonacci(self, n: int) -> int:

        T = dict()
        T[0] = 0
        T[1] = 1
        T[2] = 1

        for i in range(3, n + 1):
            T[i] = T[i - 1] + T[i - 2] + T[i - 3]
        return T[n]


# Space optimization
class Solution:
    def tribonacci(self, n: int) -> int:

        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for i in range(3, n + 1):
            x, y, z = y, z, x + y + z
        return z