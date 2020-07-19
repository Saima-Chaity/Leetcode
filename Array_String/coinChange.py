# Coin Change - https://leetcode.com/problems/coin-change/
'''You are given coins of different denominations and a total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1'''

from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount:
            return 0
        q = deque([(0, 0)])
        visited = [True] + [False] * amount

        while q:
            totalCoins, currentValue = q.popleft()
            totalCoins += 1
            for coin in coins:
                nextValue = currentValue + coin

                if nextValue == amount:
                    return totalCoins
                if nextValue < amount and not visited[nextValue]:
                    visited[nextValue] = True
                    q.append((totalCoins, nextValue))
        return -1

# Dynamic programming
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)  # 1 because we are comparing with one coin every time
        return dp[-1] if dp[-1] != float('inf') else - 1