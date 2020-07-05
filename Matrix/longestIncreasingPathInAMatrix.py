# Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].'''

# DFS
from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0

        self.row = len(matrix)
        self.col = len(matrix[0])
        self.neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cache = [[None for _ in range(self.col)] for _ in range(self.row)]
        result = 0
        for i in range(self.row):
            for j in range(self.col):
                longestPathSoFar = self.dfs(i, j, matrix, cache)
                result = max(result, longestPathSoFar)
        return result

    def dfs(self, i, j, matrix, cache):
        if cache[i][j]:
            return cache[i][j]
        longestPath = 0
        for dx, dy in self.neighbors:
            x = i + dx
            y = j + dy
            if x >= 0 and x < self.row and y >= 0 and y < self.col and matrix[x][y] > matrix[i][j]:
                longestPath = max(longestPath, self.dfs(x, y, matrix, cache))
        cache[i][j] = longestPath + 1
        return cache[i][j]

# Topologyical sort - BFS
from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mapping = {}
        q = deque([])
        for i in range(row):
            for j in range(col):
                count = 0
                for dx, dy in directions:
                    x = dx + i
                    y = dy + j
                    if 0 <= x <= row-1 and 0 <= y <= col-1 and matrix[i][j] > matrix[x][y]:
                        count += 1
                mapping[(i, j)] = count
                if count == 0:
                    q.append((i, j))
        output = 0
        while q:
            qLength = len(q)
            for _ in range(qLength):
                i, j = q.popleft()
                for dx, dy in directions:
                    x = dx + i
                    y = dy + j
                    if 0 <= x <= row - 1 and 0 <= y <= col - 1 and matrix[i][j] < matrix[x][y] and (x, y) in mapping:
                        mapping[(x, y)] -= 1
                        if mapping[(x, y)] == 0:
                            q.append((x, y))
            output += 1
        return output
