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

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(mat)
        col = len(mat[0])
        visited = set()
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for dx, dy in direction:
                x = i + dx
                y = j + dy
                if 0 <= x < row and 0 <= y < col and (x, y) not in visited:
                    mat[x][y] = mat[i][j] + 1
                    visited.add((x, y))
                    q.append((x, y))
        return mat