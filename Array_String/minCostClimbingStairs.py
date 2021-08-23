# Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/
'''On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost
to reach the top of the floor, and you can either start from the step with index 0, or the
step with index 1.

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [1] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])
        return min(dp[-1], dp[-2])

# 0(1) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1], cost[-2])