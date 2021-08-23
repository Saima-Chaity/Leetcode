'''Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean
touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south,
east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can
flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from
cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]'''

from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs(q):
            reachable = set()
            while q:
                i, j = q.popleft()
                reachable.add((i, j))
                for dx, dy in direction:
                    x = dx + i
                    y = dy + j
                    if 0 <= x < row and 0 <= y < col and heights[x][y] >= heights[i][j] and (x, y) not in reachable:
                        reachable.add((x, y))
                        q.append((x, y))
            return reachable

        row = len(heights)
        col = len(heights[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific_queue = deque()
        altantic_queue = deque()
        for i in range(row):
            pacific_queue.append((i, 0))
            altantic_queue.append((i, col - 1))

        for i in range(col):
            pacific_queue.append((0, i))
            altantic_queue.append((row - 1, i))

        pacific_result = bfs(pacific_queue)
        atlantic_result = bfs(altantic_queue)
        return pacific_result.intersection(atlantic_result)
