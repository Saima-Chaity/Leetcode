'''Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally
connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1'''

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def dfs(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != 1:
                return False
            grid[x][y] = "#"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        rows = len(grid)
        cols = len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        isFirstIsland = True
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and isFirstIsland:
                    isFirstIsland = False
                    dfs(i, j)

        visited = set()
        shortest_bridge_distance = 0
        q = deque([(r, c, shortest_bridge_distance) for r in range(rows) for c in range(cols) if grid[r][c] == '#'])

        while q:
            x, y, distance = q.popleft()
            for dx, dy in direction:
                xi = dx + x
                yj = dy + y
                if 0 <= xi < rows and 0 <= yj < cols and (xi, yj) not in visited:
                    if grid[xi][yj] == 1:
                        return distance
                    if grid[xi][yj] == "#":
                        continue
                    visited.add((xi, yj))
                    q.append((xi, yj, distance + 1))



