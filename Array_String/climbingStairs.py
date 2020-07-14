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
        self.memo = [0] * (n + 1)
        return self.climb_stairs(0, n)

    def climb_stairs(self, step, n):
        if step > n:
            return 0
        if step == n:
            return 1
        if self.memo[step] > 0:
            return self.memo[step]
        self.memo[step] = self.climb_stairs(step + 1, n) + self.climb_stairs(step + 2, n)
        return self.memo[step]