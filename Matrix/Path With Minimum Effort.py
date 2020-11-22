# Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/
'''You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0),
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down,
left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.'''

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heap = [(0, 0, 0)]
        distance_matrix = [[float('inf') for _ in range(col)] for _ in range(row)]
        distance_matrix[0][0] = 0

        while heap:
            difference, i, j = heapq.heappop(heap)
            for dx, dy in direction:
                x = dx + i
                y = dy + j
                if 0 <= x < row and 0 <= y < col:
                    current_difference = abs(heights[x][y] - heights[i][j])
                    maxDifference = max(current_difference, difference)
                    if distance_matrix[x][y] > maxDifference:
                        distance_matrix[x][y] = maxDifference
                        heapq.heappush(heap, (maxDifference, x, y))
        return distance_matrix[-1][-1]
