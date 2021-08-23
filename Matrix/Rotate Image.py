'''Rotate Image - https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(i, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(row):
            for j in range(col // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

