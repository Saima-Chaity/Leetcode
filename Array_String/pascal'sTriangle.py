# Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/
'''Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        triangle = []
        prevRow = []
        for i in range(0, numRows):
            currentRow = [1] * (i + 1)
            for j in range(1, len(currentRow) - 1):
                currentRow[j] = prevRow[j - 1] + prevRow[j]
            triangle.append(currentRow)
            prevRow = currentRow
        return triangle


# Pascal's Triangle II - https://leetcode.com/problems/pascals-triangle-ii/
'''Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 3
Output: [1,3,3,1]'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        triangle = []
        prevRow = []
        for i in range(0, rowIndex + 1):
            currentRow = [1] * (i + 1)
            for j in range(1, len(currentRow) - 1):
                currentRow[j] = prevRow[j - 1] + prevRow[j]
            triangle.append(currentRow)
            prevRow = currentRow
        return triangle[rowIndex]


# Recursive approach
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        memo = {}

        def getNums(rowIndex, colIndex):
            rowCol = (rowIndex, colIndex)
            if rowCol in memo:
                return memo[rowCol]

            if rowIndex == 0 or colIndex == 0 or rowIndex == colIndex:
                memo[rowCol] = 1
                return 1

            memo[rowCol] = getNums(rowIndex - 1, colIndex - 1) + getNums(rowIndex - 1, colIndex)
            return memo[rowCol]

        output = []
        for i in range(rowIndex + 1):
            output.append(getNums(rowIndex, i))
        return output