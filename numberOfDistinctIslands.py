# Number of Distinct Islands - https://leetcode.com/problems/number-of-distinct-islands/
'''Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if
one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
'''


class Solution(object):

    # "X" - start
    # "O" - out of bounce
    # "L" - left
    # "R" - right
    # "U" - up
    # "D" - down

    def numDistinctIslands(self, grid):

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        distinctIslands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = self.computePath(grid, i, j, "X")
                    distinctIslands.add(path)
        return len(distinctIslands)

    def computePath(self, grid, i, j, direction):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return "O"
        grid[i][j] = 0
        left = self.computePath(grid, i, j - 1, '"L"')
        right = self.computePath(grid, i, j + 1, "R")
        up = self.computePath(grid, i - 1, j, "U")
        down = self.computePath(grid, i + 1, j, "D")
        return direction + left + right + up + down



