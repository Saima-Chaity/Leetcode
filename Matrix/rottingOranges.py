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
        if not grid:
            return 
        
        row = len(grid)
        col = len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                    grid[i][j] = -1 #Visited cell
        
        minutedRequired = 0
        while q:
            updated = False
            for i in range(len(q)):
                i, j = q.popleft()
                for (x, y) in direction:
                    xi = x + i
                    yj = y + j
                    if xi >= 0 and xi < len(grid) and yj >= 0 and yj < len(grid[0]) and grid[xi][yj] != -1 and grid[xi][yj] == 1:
                        if not updated:
                            minutedRequired += 1
                            updated = True
                        grid[xi][yj] = 2
                        q.append((xi, yj))
                        grid[xi][yj] = -1 #Visited cell

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return minutedRequired
            