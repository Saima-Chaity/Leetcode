'''Swim in Rising Water - https://leetcode.com/problems/swim-in-rising-water/

You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim
infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square
(0, 0).

Example 1:

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
'''

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        result = 0
        while heap:
            depth, i, j = heapq.heappop(heap)
            result = max(result, depth)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return result
            for dx, dy in direction:
                x = dx + i
                y = dy + j
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                    heapq.heappush(heap, (grid[x][y], x, y))
                    visited.add((x, y))
