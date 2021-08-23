'''Minimum Insertion Steps to Make a String Palindrome
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
'''

# dp
class Solution:
    def minInsertions(self, s: str) -> int:

        if len(s) == 1:
            return 0

        s1 = s[::-1]
        n = len(s)
        m = len(s1)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == s1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return (n - dp[m][n])


# Recursion
class Solution:
    def minInsertions(self, s: str) -> int:

        if len(s) == 1:
            return 0

        def backTrack(i, j):

            if i >= j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            answer = 0
            if s[i] == s[j]:
                answer = backTrack(i + 1, j - 1)
            else:
                answer = 1 + min(backTrack(i, j - 1), backTrack(i + 1, j))

            dp[i][j] = answer
            return dp[i][j]

        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return backTrack(0, len(s) - 1)