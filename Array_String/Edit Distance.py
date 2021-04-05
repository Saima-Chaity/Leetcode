'''Edit Distance - https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if word1 == word2:
            return 0

        length1 = len(word1)
        length2 = len(word2)

        if length1 * length2 == 0:
            return length1 + length2

        dp = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]

        # init boundary
        for i in range(length1 + 1):
            dp[0][i] = i
        for i in range(length2 + 1):
            dp[i][0] = i

        # Compute value
        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[j - 1] != word2[i - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)

        return dp[length2][length1]