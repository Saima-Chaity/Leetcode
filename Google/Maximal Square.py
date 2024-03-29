# Maximal Square - https://leetcode.com/problems/maximal-square/
'''Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's
and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4'''

# Brute force
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        maxLength = 0
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    currentLength = 1
                    flag = True
                    while currentLength + i < row and currentLength + j < col and flag:
                        for k in range(j, currentLength + j + 1, 1):
                            if matrix[i + currentLength][k] == "0":
                                flag = False
                                break

                        for k in range(i, currentLength + i + 1, 1):
                            if matrix[k][j + currentLength] == "0":
                                flag = False
                                break

                        if flag:
                            currentLength += 1

                    maxLength = max(maxLength, currentLength)

        return maxLength * maxLength


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxLength = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
                    maxLength = max(maxLength, dp[i][j])
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1 #Adding 1 because if
                    # matrix[i][j]=='1' and its surroundings (2x2 square), then we will increase the size of the square.
                    # Else, it will be a single square 1X1 square
                    maxLength = max(maxLength, dp[i][j])
        return maxLength * maxLength


# 0(n) space
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        dp = [0 for _ in range(col + 1)]
        maxLength = float('-inf')
        prev = 0

        for i in range(row):
            for j in range(col):
                temp = dp[j + 1]
                if matrix[i][j] == "1":
                    dp[j + 1] = min(dp[j], dp[j + 1], prev) + 1
                    maxLength = max(maxLength, dp[j + 1])
                else:
                    dp[j + 1] = 0
                prev = temp
        return maxLength * maxLength if maxLength != float('-inf') else 0


# Another approach
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        maxsqlen = 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(row):
            dp[i][0] = int(matrix[i][0])
            maxsqlen = max(maxsqlen, dp[i][0])
        for i in range(col):
            dp[0][i] = int(matrix[0][i])
            maxsqlen = max(maxsqlen, dp[0][i])
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen * maxsqlen

