'''Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate
that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
'''


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        row = len(matrix)
        col = len(matrix[0])
        count = 0
        for i in range(row):
            sums = [0] * col
            for j in range(i, row):
                mapping = {}
                mapping[0] = 1
                prefixSum = 0
                for k in range(col):
                    sums[k] += matrix[j][k]
                    prefixSum += sums[k]
                    count += mapping.get(prefixSum - target, 0)
                    mapping[prefixSum] = mapping.get(prefixSum, 0) + 1
        return count