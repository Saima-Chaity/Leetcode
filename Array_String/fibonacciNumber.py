# Fibonacci Number - https://leetcode.com/problems/fibonacci-number/
'''The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.'''

class Solution:
    def fib(self, N: int) -> int:
        
        if N <= 1:
            return N
        
        memo = [0] * (N+1)
        memo[0] = 0
        memo[1] = 1
        for i in range(2, N+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[N]


# Space optimization
class Solution:
    def fib(self, n: int) -> int:

        if n < 3:
            return 1 if n else 0

        x, y, = 0, 1
        for i in range(2, n + 1):
            x, y = y, x + y
        return y