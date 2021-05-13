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

        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                # If first string is empty, only option is to
                # insert all characters of second string
                if i == 0:
                    dp[i][j] = j
                # If second string is empty, only option is to
                # remove all characters of second string
                elif j == 0:
                    dp[i][j] = i
                # If last characters are same, ignore last char
                # and recur for remaining string
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If last character are different, consider all
                    # possibilities and find minimum
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[m][n]

# Another approach
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