# Unique Paths - https://leetcode.com/problems/unique-paths/

'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?'''

# Input: m = 3, n = 2
# Output: 3

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:

    grid = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          grid[i][j] = 1
        elif i == 0 and j != 0:
          grid[i][j] += grid[i][j - 1]
        elif i != 0 and j == 0:
          grid[i][j] += grid[i - 1][j]
        else:
          grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m - 1][n - 1]


# Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?'''

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    for i in range(rows - 1, -1, -1):
      for j in range(cols - 1, -1, -1):
        if obstacleGrid[i][j] == 1:
          obstacleGrid[i][j] = 0
        elif i != rows - 1 and j == cols - 1:
          obstacleGrid[i][j] += obstacleGrid[i + 1][j]
        elif i == rows - 1 and j != cols - 1:
          obstacleGrid[i][j] += obstacleGrid[i][j + 1]
        elif i == rows - 1 and j == cols - 1:
          obstacleGrid[i][j] = 1
        else:
          obstacleGrid[i][j] = obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]
    return obstacleGrid[0][0]


# Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

'''On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.'''

# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2

class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    self.paths = 0
    (x, y) = (0, 0)
    end = (0, 0)
    emptySquares = 1

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == 1:
          (x, y) = (i, j)
        elif grid[i][j] == 2:
          end = (i, j)
        elif grid[i][j] == 0:
          emptySquares += 1

    def dfs(i, j, empty):
      if not (0 <= i < rows and 0 <= j < cols and grid[i][j] >= 0):
        return

      if (i, j) == end:
        if empty == 0:
          self.paths += 1
          return

      grid[i][j] = -2
      dfs(i - 1, j, empty - 1)
      dfs(i + 1, j, empty - 1)
      dfs(i, j - 1, empty - 1)
      dfs(i, j + 1, empty - 1)
      grid[i][j] = 0

    dfs(x, y, emptySquares)
    return self.paths