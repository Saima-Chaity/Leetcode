# Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:

Input: [[0,1],[1,0]]

Output: 2'''

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] != 0 or grid[-1][-1]:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        q = deque([(0, 0, 1)])
        '''Another way to generate direction
        direction = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                direction.append((i, j))
        '''
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        grid[0][0] = 1

        while q:
            for _ in range(len(q)):
                x, y, distance = q.popleft()
                if x == rows - 1 and y == cols - 1:
                    return distance
                for dx, dy in directions:
                    xi = x + dx
                    yj = y + dy
                    if 0 <= xi < rows and 0 <= yj < cols and grid[xi][yj] == 0:
                        grid[xi][yj] = 1
                        q.append((xi, yj, distance + 1))
        return -1