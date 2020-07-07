# Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/
'''Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        def binerySearchRow(matrix, low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if matrix[mid][0] <= target and matrix[mid][len(matrix[mid]) - 1] >= target:
                    return mid
                elif matrix[mid][0] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        def binerySearchCol(matrix, low, high, row):
            while low <= high:
                mid = low + (high - low) // 2
                if matrix[row][mid] == target:
                    return mid
                elif matrix[row][mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        row = binerySearchRow(matrix, 0, len(matrix) - 1)
        if row == -1:
            return False
        col = binerySearchCol(matrix, 0, len(matrix[row]) - 1, row)
        return col != -1


# Search a 2D Matrix II - https://leetcode.com/problems/search-a-2d-matrix-ii/
'''Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        for row in matrix:
            if row[0] > target:
                return False
            if row[-1] < target:
                continue

            low = 0
            high = col
            while low <= high:
                mid = low + (high - low) // 2
                if row[mid] > target:
                    high = mid - 1
                elif row[mid] < target:
                    low = mid + 1
                else:
                    return True
        return False