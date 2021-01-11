# Maximal Rectangle - https://leetcode.com/problems/maximal-rectangle/
'''Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
'''

from collections import deque


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        def getMaxRect(currentRow):
            q = deque()
            maxArea = float('-inf')
            for i in range(len(currentRow)):
                value = currentRow[i]
                while q and q[-1][1] >= value:
                    height = q.pop()
                    leftIndex = q[-1][0] if q else -1
                    width = i - leftIndex - 1
                    maxArea = max(maxArea, (height[1] * width))
                q.append((i, value))

            while q:
                height = q.pop()
                leftIndex = q[-1][0] if q else -1
                width = len(currentRow) - leftIndex - 1
                maxArea = max(maxArea, (height[1] * width))
            return maxArea

        rows = len(matrix)
        cols = len(matrix[0])
        maxRectangle = float('-inf')
        currentRow = [0] * (cols + 1)
        for i in range(rows):
            for j in range(cols):
                # update the state of this row's histogram using the last row's histogram
                # by keeping track of the number of consecutive ones
                if matrix[i][j] == "1":
                    currentRow[j] += 1
                else:
                    currentRow[j] = 0
            maxRectangle = max(maxRectangle, getMaxRect(currentRow))
        return maxRectangle