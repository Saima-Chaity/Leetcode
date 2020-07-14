# Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share
of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        minBuy = float('inf')
        for i in range(1, len(prices)):
            buy = prices[i - 1]
            sell = prices[i]
            if buy < sell:
                minBuy = min(minBuy, buy)
            maxProfit = max(maxProfit, sell - minBuy)
        return maxProfit if maxProfit != float('-inf') else 0

# Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock 
before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            buy = prices[i-1]
            sell = prices[i]
            if buy < sell:
                maxProfit += sell - buy
        return maxProfit if maxProfit != float('-inf') else 0

# Another approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell = prices[i]
            max_profit += sell - buy
        return max_profit