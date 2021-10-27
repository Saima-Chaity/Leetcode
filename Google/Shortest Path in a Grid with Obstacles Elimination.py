'''Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner
(m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:

Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6.
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
'''

from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        row = len(grid)
        col = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        target = (row - 1, col - 1)
        q = deque([(0, 0, 0, k)])
        visited = set()
        visited.add((0, 0, k))
        while q:
            steps, i, j, k = q.popleft()
            if (i, j) == target:
                return steps

            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < row and 0 <= y < col:
                    new_k = k - grid[x][y]
                    if (x, y, new_k) not in visited and new_k >= 0:
                        visited.add((x, y, new_k))
                        q.append((steps + 1, x, y, new_k))
        return -1
