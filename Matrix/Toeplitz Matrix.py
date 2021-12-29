'''Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
'''

from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        summation = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                summation[i - j].append(matrix[i][j])
                values = summation[i - j]
                if len(values) > 1 and values[-1] != values[-2]:
                    return False
        return True


# Another approach
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        result = True
        i = len(matrix) - 1
        j = 0

        while i >= 0 and j < len(matrix):
            cell = []
            temp_i = i
            while temp_i < len(matrix) and j < len(matrix[0]):
                cell.append(matrix[temp_i][j])
                temp_i += 1
                j += 1
                if len(cell) > 1 and cell[-1] != cell[-2]:
                    result = False
                    break
            i -= 1
            j = 0

        if result:
            i = 0
            j = len(matrix[0]) - 1
            while i < len(matrix) and j > 0:
                cell = []
                temp_j = j
                while i < len(matrix) and temp_j < len(matrix[0]):
                    cell.append(matrix[i][temp_j])
                    i += 1
                    temp_j += 1
                    if len(cell) > 1 and cell[-1] != cell[-2]:
                        result = False
                        break
                i = 0
                j -= 1
        else:
            return result
        return result
