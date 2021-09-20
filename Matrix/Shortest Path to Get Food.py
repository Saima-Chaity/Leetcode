'''Shortest Path to Get Food - https://leetcode.com/problems/shortest-path-to-get-food/
You are starving and you want to eat food as quickly as possible. You want to find the shortest
path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food,
return -1.

Example 1:
Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.
'''

from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    q.append((i, j, 1))
                    break

        result = []
        while q:
            qLength = len(q)
            for _ in range(qLength):
                x, y, steps = q.popleft()
                for dx, dy in directions:
                    xi = x + dx
                    yj = y + dy
                    if 0 <= xi < rows and 0 <= yj < cols and grid[xi][yj] != "X":
                        if grid[xi][yj] == 'O':
                            q.append((xi, yj, steps + 1))
                        elif grid[xi][yj] == "#":
                            return steps
                        grid[xi][yj] = 'X'
        return -1


# Using heap
import heapq
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        q = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    heapq.heappush(q, (1, i, j))
                    break

        while q:
            steps, x, y = heapq.heappop(q)
            for dx, dy in directions:
                xi = x + dx
                yj = y + dy
                if 0 <= xi < rows and 0 <= yj < cols and grid[xi][yj] != "X":
                    if grid[xi][yj] == 'O':
                        heapq.heappush(q, (steps + 1, xi, yj))
                    elif grid[xi][yj] == "#":
                        return steps
                    grid[xi][yj] = 'X'
        return -1



