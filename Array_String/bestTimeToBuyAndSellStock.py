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
        
        for i in range(len(prices)-1):
            buy = prices[i]
            sell = prices[i+1]
            if buy < sell:
                maxProfit += sell-buy
        return maxProfit 

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



# Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        oneBuy = float('inf')
        oneBuyOneSell = float('-inf')
        twoBuy = float('inf')
        twoBuyTwoSell = float('-inf')
        for price in prices:
            oneBuy = min(oneBuy, price) # Find the lowest buy
            oneBuyOneSell = max(oneBuyOneSell, price - oneBuy) # Find the maximum profit 
            twoBuy = min(twoBuy, price-oneBuyOneSell) # Mimimize the buy price again
            twoBuyTwoSell = max(twoBuyTwoSell, price-twoBuy) # Find the maximum profit 
        return twoBuyTwoSell


# Best Time to Buy and Sell Stock IV - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) 
and sell on day 6 (price = 3), profit = 3-0 = 3.
 '''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        '''The complexity of this is O(nk) and space complexity is O(nk).'''

        if not prices or not k:
            return 0

        if 2 * k >= len(prices):
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

        output = [0] * len(prices)
        for _ in range(k):
            current = 0
            for i in range(1, len(output)):
                current = max(output[i], current + prices[i] - prices[i - 1])
                output[i] = max(output[i - 1], current)
        return output[-1]

