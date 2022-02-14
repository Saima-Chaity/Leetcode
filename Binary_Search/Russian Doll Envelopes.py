'''Russian Doll Envelopes - https://leetcode.com/problems/russian-doll-envelopes/

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width
and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are
greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def binerySearch(low, high, value, dp):
            while low <= high:
                mid = low + (high - low) // 2
                if dp[mid] == value:
                    return mid
                if dp[mid] > value:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        dp[0] = envelopes[0][1]
        length = 1
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > dp[length - 1]:
                dp[length] = envelopes[i][1]
                length += 1
            else:
                position = binerySearch(0, length - 1, envelopes[i][1], dp)
                dp[position] = envelopes[i][1]
        return length