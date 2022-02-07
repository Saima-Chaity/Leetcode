# Leftmost Column with at Least a One - https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
'''(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted
in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it.
If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols],
which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions
that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not have access
to the binary matrix directly.

Example 1:

Input: mat = [[0,0],[1,1]]
Output: 0'''


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# Start at Top Right, Move Only Left and Down
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        current_row = 0
        current_col = col - 1

        while current_row < row and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1
        return current_col + 1 if current_col != col - 1 else -1


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# Binary Search
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        leftMostIndex = float('inf')
        for row in range(rows):
            low = 0
            high = cols - 1
            while low < high:
                mid = low + (high - low) // 2
                if binaryMatrix.get(row, mid) == 0:
                    low = mid + 1
                else:
                    high = mid
            if binaryMatrix.get(row, low) == 1:
                leftMostIndex = min(leftMostIndex, low)
        return leftMostIndex if leftMostIndex != float('inf') else -1
