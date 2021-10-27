'''Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

You have planned some train traveling one year in advance. The days of the year in which you will travel are
given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
'''

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0] * (days[-1] + 1)
        days = set(days)
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[max(i - 1, 0)] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


# Another approach
from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            output = float('inf')
            j = i
            for cost, duration in zip(costs, durations):
                while j < n and days[j] < days[i] + duration:
                    j += 1
                output = min(dp(j) + cost, output)
            return output

        return dp(0)
