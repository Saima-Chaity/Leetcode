# Climbing Stairs - https://leetcode.com/problems/climbing-stairs/
'''You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps'''

class Solution:
    def climbStairs(self, n: int) -> int:
        mapping = dict()
        mapping[1] = 1
        mapping[2] = 2
        for step in range(3, n + 1):
            mapping[step] = mapping[step - 1] + mapping[step - 2]
        return mapping[n]

# Recursion with Memoization
class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def _climbStairs(i, n):
            if i > n:
                return 0

            if i == n:
                return 1

            if i in memo:
                return memo[i]

            memo[i] = _climbStairs(i + 1, n) + _climbStairs(i + 2, n)
            return memo[i]

        return _climbStairs(0, n)