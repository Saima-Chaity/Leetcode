# Longest Palindromic Subsequence - https://leetcode.com/problems/longest-palindromic-subsequence/
'''Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        if len(s) == 1:
            return 1

        def backTrack(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]: # first and last character are same
                memo[(i, j)] = 2 + backTrack(i + 1, j - 1)
            else: # first and last character are not same, branches off into 2 paths
                memo[(i, j)] = max(backTrack(i + 1, j), backTrack(i, j - 1))
            return memo[(i, j)]

        self.length = 0
        memo = {}
        return backTrack(0, len(s) - 1)

# DP
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        if len(s) == 1:
            return 1

        n = len(s)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        s1 = s[::-1]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]
