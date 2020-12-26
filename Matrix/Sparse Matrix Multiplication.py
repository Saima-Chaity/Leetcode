# Sparse Matrix Multiplication - https://leetcode.com/problems/sparse-matrix-multiplication/
'''Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 '''

# Time 0(n3)
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        a_row = len(A)
        a_col = len(A[0])
        b_row = len(B)
        b_col = len(B[0])
        output = [[0] * b_col for _ in range(a_row)]
        for i in range(a_row):
            for j in range(a_col):
                if A[i][j] != 0:
                    for k in range(b_col):
                        output[i][k] += A[i][j] * B[j][k]
                else:
                    continue
        return output


# Time 0(n2)
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        def getNoneZero(matrix):
            none_zero = []
            row = len(matrix)
            col = len(matrix[0])
            for i in range(row):
                for j in range(col):
                    if matrix[i][j] != 0:
                        none_zero.append((i, j, matrix[i][j]))
                    else:
                        continue
            return none_zero

        a_row = len(A)
        a_col = len(A[0])
        b_row = len(B)
        b_col = len(B[0])
        output = [[0] * b_col for _ in range(a_row)]
        a_sparse = getNoneZero(A)
        b_sparse = getNoneZero(B)

        for i, j, a_value in a_sparse:
            for m, n, b_value in b_sparse:
                if j == m:
                    output[i][n] += a_value * b_value
        return output
