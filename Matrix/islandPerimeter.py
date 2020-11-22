# Island Perimeter - https://leetcode.com/problems/island-perimeter/
'''You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and
there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square
with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
'''


# BFS
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        q = []
        visited = set()
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
        while q:
            i, j = q.pop(0)
            for dx, dy in direction:
                xi = dx + i
                yj = dy + j
                if 0 <= xi < row and 0 <= yj < col and (xi, yj) not in visited:
                    if grid[xi][yj] != 1:
                        perimeter += 1
                if xi == -1 or yj == -1 or xi == row or yj == col:
                    perimeter += 1
        return perimeter


# DFS
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [(0, 1), (1, 0), (0,-1), (-1, 0)]
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for dx, dy in direction:
                        x = dx + i
                        y = dy + j
                        if 0 <= x < row and 0 <= y < col and grid[x][y] != 1:
                            perimeter += 1
                        if x < 0 or y < 0 or x == row or y == col:
                            perimeter += 1
        return perimeter