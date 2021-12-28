'''Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''

from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        summation = defaultdict(list)
        result = list()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                summation[i + j].append(mat[i][j])

        for key, value in summation.items():
            if key % 2 == 0:
                result.extend(value[::-1])
            else:
                result.extend(value)
        return result