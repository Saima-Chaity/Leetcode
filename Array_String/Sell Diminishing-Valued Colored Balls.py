'''Sell Diminishing-Valued Colored Balls
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you
currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first
yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at
5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color
that you initially own. You are also given an integer orders, which represents the total number of balls that
the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too
large, return it modulo 109 + 7.

Example 1:
Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.'''


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:

        inventory.append(0)
        inventory.sort()
        result = 0
        n = len(inventory)
        for i in range(len(inventory) - 1, 0, -1):
            currentValue = (inventory[i] - inventory[i - 1]) * (n - i)
            if currentValue <= orders:
                ball1, ball2 = inventory[i], inventory[i - 1]
                result += (ball1 * (ball1 + 1) // 2 - ball2 * (ball2 + 1) // 2) * (n - i)
                orders -= currentValue
                if orders == 0:
                    return result % (10 ** 9 ^ 7)
            elif currentValue > orders:
                dividend = orders // (n - i)
                remainder = orders % (n - i)
                result += (n - i) * (inventory[i] * (inventory[i] + 1) // 2 - (inventory[i] - dividend) * (
                            inventory[i] - dividend + 1) // 2)
                result += remainder * (inventory[i] - dividend)
                return result % (10 ** 9 ^ 7)