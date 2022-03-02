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

from collections import Counter
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def dfs(index, i, j):
            islands[index] += 1
            grid[i][j] = index
            for dx, dy in direction:
                next_x = i + dx
                next_y = j + dy
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 1:
                    dfs(index, next_x, next_y)

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(grid)
        col = len(grid[0])
        islands = Counter()
        index = 2  # index is used for grouping island count and keep track of visited island.

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(index, i, j)
                    index += 1

        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    continue
                neighbors = set()
                for dx, dy in direction:
                    next_x = i + dx
                    next_y = j + dy
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                        neighbors.add(grid[next_x][next_y])
                result = max(result, sum(islands[i] for i in neighbors) + 1)

        return result if result else row * col


# TLE
from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            q.append((i, j))
            visited = set()
            visited.add((i, j))
            count = 1
            while q:
                x, y = q.popleft()
                for dx, dy in direction:
                    next_x = x + dx
                    next_y = y + dy
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and (next_x, next_y) not in visited and \
                            grid[next_x][next_y] == 1:
                        count += 1
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))
            return count

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        largestIsland = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    island_count = bfs(i, j)
                    largestIsland = max(largestIsland, island_count)
                    grid[i][j] = 0
        return largestIsland if largestIsland else len(grid) * len(grid[0])