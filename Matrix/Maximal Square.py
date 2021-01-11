# Maximal Square - https://leetcode.com/problems/maximal-square/
'''Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's
and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        maxSide = float('-inf')

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1 #Adding 1 because if
                    # matrix[i][j]=='1' and its surroundings (2x2 square), then we will increase the size of the square.
                    # Else, it will be a single square 1X1 square
                    if dp[i + 1][j + 1] > maxSide:
                        maxSide = dp[i + 1][j + 1]
        return maxSide * maxSide if maxSide != float('-inf') else 0