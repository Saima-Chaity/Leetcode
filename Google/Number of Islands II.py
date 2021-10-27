'''Number of Islands II - https://leetcode.com/problems/number-of-islands-ii/

You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's
represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions
where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example 1:

Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
'''

from collections import deque
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        def getIsland(matrix):
            islandCount = 0
            visited = set()

            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == '1' and (i, j) not in visited:
                        q.append((i, j))
                        visited.add((i, j))
                        islandCount += 1

                        while len(q):
                            x, y = q.popleft()
                            for dx, dy in direction:
                                next_x = x + dx
                                next_y = y + dy
                                if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] == '1' and (
                                next_x, next_y) not in visited:
                                    q.append((next_x, next_y))
                                    visited.add((next_x, next_y))
            return islandCount

        matrix = [['0' for _ in range(n)] for _ in range(m)]
        answer = []
        q = deque()
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for position in positions:
            i, j = position[0], position[1]
            matrix[i][j] = '1'
            answer.append(getIsland(matrix))
        return answer