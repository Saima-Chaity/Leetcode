'''Making A Large Island - https://leetcode.com/problems/making-a-large-island/

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
'''

'''Time complexity is O(n*m), because we traverse our graph twice: 
one with dfs and another when we were looking for empty cells. 
Two Sum II - Input array is sortedSpace complxity is potentially O(n*m) as well.'''
class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def dfs(index, x, y):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] != 1:
                return
            islands[index] += 1
            grid[x][y] = index
            for dx, dy in direction:
                xi = dx + x
                yj = dy + y
                dfs(index, xi, yj)

        row = len(grid)
        col = len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = collections.Counter()
        index = 2
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(index, i, j)
                    index += 1

        result = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] != 0:
                    continue
                neighbours = set()
                for dx, dy in direction:
                    xi = dx + x
                    yj = dy + y
                    if 0 <= xi < row and 0 <= yj < col and grid[xi][yj] != 0:
                        neighbours.add((grid[xi][yj]))
                result = max(result, sum(islands[i] for i in neighbours) + 1)
        return result if result else row * col

