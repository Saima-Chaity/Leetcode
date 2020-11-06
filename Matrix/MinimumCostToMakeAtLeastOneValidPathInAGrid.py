# Minimum Cost to Make at Least One Valid Path in a Grid - 
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
'''Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. 
The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from 
the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. 
The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
'''

import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        directions = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]
        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            cost, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            else:
                visited.add((i, j))
                if i == row - 1 and j == col - 1:
                    return cost
                for dx, dy, distance in directions:
                    x = dx + i
                    y = dy + j
                    if 0 <= x < row and 0 <= y < col:
                        if grid[i][j] == distance:
                            heapq.heappush(heap, (cost, x, y))
                        elif grid[i][j] != distance:
                            heapq.heappush(heap, (cost+1, x, y))
        return 0

        
