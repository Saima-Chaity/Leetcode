'''Longest Line of Consecutive One in Matrix
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

Example 1:

Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3'''

from collections import defaultdict
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:

        row = defaultdict(int)
        col = defaultdict(int)
        ascending = defaultdict(int)
        descending = defaultdict(int)
        longest = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    row[i] = col[j] = ascending[i + j] = descending[j - i] = 0
                else:
                    row[i] += 1
                    col[j] += 1
                    ascending[i + j] += 1
                    descending[j - i] += 1
                    longest = max(longest, row[i], col[j], ascending[i + j], descending[j - i])
        return longest


# Another approach
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:

        def isStartngPoint(r, c, dx, dy):
            current_row = r - dx
            current_col = c - dy
            if current_row < 0 or current_col < 0 or current_row >= row or current_col >= col:
                return True
            return mat[current_row][current_col] == 0

        row = len(mat)
        col = len(mat[0])
        direction = [(0, 1), (1, 0), (1, 1), (1, -1)]
        longest = 0

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    for dx, dy in direction:
                        if isStartngPoint(i, j, dx, dy):
                            temp_row = i
                            temp_col = j
                            result = 0
                            while temp_row < row and temp_col < col and temp_row >= 0 and temp_col >= 0 and \
                                    mat[temp_row][temp_col] == 1:
                                temp_row += dx
                                temp_col += dy
                                result += 1
                            longest = max(longest, result)
        return longest

