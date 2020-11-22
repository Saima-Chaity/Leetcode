# Path With Maximum Minimum Value - https://leetcode.com/problems/path-with-maximum-minimum-value/

'''Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and
ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal
directions (north, east, west, south).
 '''

# Input: [[5,4,5],[1,2,6],[7,4,6]]
# Output: 4

import heapq
class Solution:
  def maximumMinimumPath(self, A: List[List[int]]) -> int:
    rows = len(A)
    cols = len(A[0])
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = [(-A[0][0], 0, 0)]
    result = 1e9

    while q:
      value, x, y = heapq.heappop(q)
      result = min(result, -value)

      for dx, dy in direction:
        xi = x + dx
        yj = y + dy

        if 0 <= xi < rows and 0 <= yj < cols:
          if A[xi][yj] == -1:
            continue
          if xi == rows - 1 and yj == cols - 1:
            return min(result, A[rows - 1][cols - 1])
          heapq.heappush(q, (-A[xi][yj], xi, yj))
          A[xi][yj] = -1


#Binary Search and DFS
class Solution:
  def maximumMinimumPath(self, A: List[List[int]]) -> int:
    rows = len(A)
    cols = len(A[0])
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def check(value):
      memo = [[0 for _ in range(cols)] for _ in range(rows)]

      def dfs(i, j):
        if i == rows - 1 and j == cols - 1:
          return True

        memo[i][j] = 1
        for x, y in direction:
          xi = x + i
          yj = y + j
          if 0 <= xi < rows and 0 <= yj < cols and not memo[xi][yj] and A[xi][yj] >= value and dfs(xi, yj):
            return True
        return False

      return dfs(0, 0)

    minValue = min(A[0][0], A[rows - 1][cols - 1])
    unique = set()
    for i in range(rows):
      for j in range(cols):
        if A[i][j] <= minValue:
          unique.add(A[i][j])

    arr = sorted(unique)
    left = 0
    right = len(arr) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if check(arr[mid]):
        left = mid + 1
      else:
        right = mid - 1
    return arr[right]


