# Spiral Matrix - https://leetcode.com/problems/spiral-matrix/
'''Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        top = left = 0
        down = row
        right = col
        output = []
        
        while left < right and top < down:
            # Print the first row from
            # the remaining rows
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            # Print the last column from
            # the remaining columns
            for i in range(top, down):
                output.append(matrix[i][right-1])
            right -= 1

            # Print the last row from
            # the remaining rows
            if top < down:
                for i in range(right-1, left-1, -1):
                    output.append(matrix[down-1][i])
                down -= 1
            
            # Print the first column from
            # the remaining columns
            if left < right:
                for i in range(down-1, top-1, -1):
                    output.append(matrix[i][left])
                left += 1
        return 
        

# Spiral Matrix II - https://leetcode.com/problems/spiral-matrix-ii/
'''Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row = len(matrix)
        col = len(matrix[0])
        top = left = 0
        down = row
        right = col
        currentNumber = 1
        
        while left < right and top < down:
            # Print the first row from
            # the remaining rows
            for i in range(left, right):
                matrix[top][i] = currentNumber
                currentNumber += 1
            top += 1

            # Print the last column from
            # the remaining columns
            for i in range(top, down):
                matrix[i][right-1] = currentNumber
                currentNumber += 1
            right -= 1

            # Print the last row from
            # the remaining rows
            if top < down:
                for i in range(right-1, left-1, -1):
                    matrix[down-1][i] = currentNumber
                    currentNumber += 1
                down -= 1
            
            # Print the first column from
            # the remaining columns
            if left < right:
                for i in range(down-1, top-1, -1):
                    matrix[i][left] = currentNumber
                    currentNumber += 1
                left += 1
        return matrix