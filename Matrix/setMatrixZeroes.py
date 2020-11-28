# Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/
'''Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowSet = set()
        colSet = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)

        for i in range(row):
            for j in range(col):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0

# Without extra space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        is_Col = False

        for i in range(row):
            if matrix[i][0] == 0:
                is_Col = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update the elements using the first row and first col
        for i in range(1, row):
            for j in range(1, col):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # Update first row
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0

        # Update first col
        if is_Col:
            for i in range(row):
                matrix[i][0] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def setRowToZero(rowIndex, colIndex):
            if rowIndex > 0:
                rowIndex = 0
            for i in range(rowIndex, row):
                if matrix[i][colIndex] != 0:
                    matrix[i][colIndex] = 0
                    visited.add((i, colIndex))

        def setColToZero(rowIndex, colIndex):
            if colIndex > 0:
                colIndex = 0
            for j in range(colIndex, col):
                if matrix[rowIndex][j] != 0:
                    matrix[rowIndex][j] = 0
                    visited.add((rowIndex, j))

        row = len(matrix)
        col = len(matrix[0])
        visited = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 and (i, j) not in visited:
                    visited.add((i, j))
                    setRowToZero(i, j)
                    setColToZero(i, j)

