'''Decode Ways - https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).'''


class Solution:
    def numDecodings(self, s: str) -> int:
        def decodeWays(index, s):
            if index > len(s):
                return 0
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index in memo:
                return memo[index]
            output = decodeWays(index + 1, s)
            if int(s[index:index + 2]) <= 26:
                output += decodeWays(index + 2, s)
            memo[index] = output
            return memo[index]

        memo = {}
        return decodeWays(0, s)


# Iterative
class Solution:
    def numDecodings(self, s: str) -> int:

        if s and s[0] == '0':
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            two_digit = s[i - 2:i]
            if int(two_digit) >= 10 and int(two_digit) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]

# 0(1) space
class Solution:
    def numDecodings(self, s: str) -> int:

        if s and s[0] == '0':
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = one_back
            two_digit = s[i - 1:i + 1]
            if int(two_digit) >= 10 and int(two_digit) <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        return one_back


