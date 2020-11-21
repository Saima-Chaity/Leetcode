# Interleaving String - https://leetcode.com/problems/interleaving-string/
'''Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
'''

# Recursion with memoization
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def dfs(s1_index, s2_index, s3_index, s1, s2, s3):
            if s3_index == len(s3):
                if s1_index == len(s1) and s2_index == len(s2):
                    return True
                else:
                    return False

            if s1_index == len(s1) and s2_index == len(s2) and s3_index != len(s3):
                return False

            if (s1_index, s2_index) in cache:
                return True if cache[s1_index, s2_index] == 1 else False

            result1 = False
            result2 = False
            if s1_index < len(s1):
                if s1[s1_index] == s3[s3_index]:
                    result1 = dfs(s1_index + 1, s2_index, s3_index + 1, s1, s2, s3)

            if s2_index < len(s2):
                if s2[s2_index] == s3[s3_index]:
                    result2 = dfs(s1_index, s2_index + 1, s3_index + 1, s1, s2, s3)

            cache[s1_index, s2_index] = 1 if (result1 or result2) else 0
            return cache[s1_index, s2_index]

        cache = {}
        return dfs(0, 0, 0, s1, s2, s3)


# Dynamic programming
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                                dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[len(s1)][len(s2)]
