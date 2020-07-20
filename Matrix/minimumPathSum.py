# Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/
'''Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j != cols - 1:
                    grid[i][j] = grid[i][j] + grid[i][j + 1]
                if i != rows - 1 and j == cols - 1:
                    grid[i][j] = grid[i][j] + grid[i + 1][j]
                elif i != rows - 1 and j != cols - 1:
                    grid[i][j] = grid[i][j] + min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]

# Top-down approach
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if (grid == [[]]):
            return 0
        # traverse the first column
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        # traverse the first row
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]
        # Calculate minimun sum
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]