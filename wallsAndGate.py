# Walls and Gates - https://leetcode.com/problems/walls-and-gates/

'''You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume
that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be
filled with INF.'''

# Given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

from collections import deque


class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
      return []

    rows = len(rooms)
    cols = len(rooms[0])
    q = []
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(rows):
      for j in range(cols):
        if rooms[i][j] == 0:
          q.append((i, j))
          visited.add((i, j))

    while q:
      x, y = q.pop(0)
      for dx, dy in directions:
        xi = x + dx
        yj = y + dy
        if 0 <= xi < rows and 0 <= yj < cols and (xi, yj) not in visited and rooms[xi][yj] != -1:
          rooms[xi][yj] = rooms[x][y] + 1
          visited.add((xi, yj))
          q.append((xi, yj))
