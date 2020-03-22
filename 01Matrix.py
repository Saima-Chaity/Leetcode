# 01 Matrix - https://leetcode.com/problems/01-matrix/

'''Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.'''

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

class Solution:
  def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

    if not matrix:
      return []
    rows = len(matrix)
    cols = len(matrix[0])
    q = []
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(rows):
      for j in range(cols):
        if matrix[i][j] == 0:
          q.append((i, j))
          visited.add((i, j))
    while q:
      x, y = q.pop(0)
      for dx, dy in directions:
        xi = x + dx
        yj = y + dy
        if 0 <= xi < rows and 0 <= yj < cols and (xi, yj) not in visited:
          matrix[xi][yj] = matrix[x][y] + 1
          q.append((xi, yj))
          visited.add((xi, yj))
    return matrix