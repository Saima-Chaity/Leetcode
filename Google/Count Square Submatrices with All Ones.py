'''Count Square Submatrices with All Ones - https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
'''


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        row = len(matrix)
        col = len(matrix[0])
        copy_matrix = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            copy_matrix[i][0] = matrix[i][0]
        for i in range(col):
            copy_matrix[0][i] = matrix[0][i]
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j]:
                    copy_matrix[i][j] = 1 + min(copy_matrix[i][j - 1], copy_matrix[i - 1][j], copy_matrix[i - 1][j - 1])

        result = 0
        for row in copy_matrix:
            result += sum(row)
        return result


# 0(1) space
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        row = len(matrix)
        col = len(matrix[0])
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j]:
                    matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])

        result = 0
        for row in matrix:
            result += sum(row)
        return result