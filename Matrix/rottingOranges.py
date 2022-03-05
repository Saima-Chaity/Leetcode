# Rotting Oranges - https://leetcode.com/problems/rotting-oranges/
'''In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4'''

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(grid)
        col = len(grid[0])
        q = deque()
        minuteRequired = 0
        freshOrange = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                    grid[i][j] = -1  # Visited cell
                if grid[i][j] == 1:
                    freshOrange += 1

        while q:
            updated = False
            for i in range(len(q)):
                i, j = q.popleft()
                for dx, dy in direction:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                        q.append((x, y))
                        grid[x][y] = -1  # Visited cell
                        freshOrange -= 1
                        if not updated:
                            minuteRequired += 1
                            updated = True

        return minuteRequired if freshOrange == 0 else -1