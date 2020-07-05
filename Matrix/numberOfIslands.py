# Number of Islands - https://leetcode.com/problems/number-of-islands/
'''Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input:
11110
11010
11000
00000

Output: 1'''

# BFS
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (len(grid)) == 0:
            return 0

        row = len(grid)
        col = len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    island += 1
                    q.append((i, j))
                    grid[i][j] = '0'

                    while len(q):
                        x, y = q.popleft()
                        for dx, dy in direction:
                            xi = dx + x
                            yj = dy + y
                            if 0 <= xi < row and 0 <= yj < col and grid[xi][yj] == "1":
                                q.append((xi, yj))
                                grid[xi][yj] = "0"
        return island

# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (len(grid)) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        self.direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island += 1
                    self.toggleIsland(grid, i, j)
        return island

    def toggleIsland(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        elif grid[i][j] == "1":
            grid[i][j] = "0"
        for (x, y) in self.direction:
            xi = x + i
            yj = y + j
            if xi >= 0 and xi < len(grid) and yj >= 0 and yj < len(grid[0]):
                self.toggleIsland(grid, xi, yj)


