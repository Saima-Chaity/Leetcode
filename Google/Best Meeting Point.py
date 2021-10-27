'''Best Meeting Point - https://leetcode.com/problems/best-meeting-point/

Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:

Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
'''


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        def calculate(i, j):
            totalDistance = 0
            for point in points:
                totalDistance += abs(point[0] - i) + abs(point[1] - j)
            return totalDistance

        row = len(grid)
        col = len(grid[0])
        points = []
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    points.append((i, j))

        minDistance = float('inf')
        for i in range(row):
            for j in range(col):
                distance = calculate(i, j)
                minDistance = min(minDistance, distance)
        return minDistance


# Another approach
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows.append(i)

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i]:
                    cols.append(i)

        best_point = [rows[len(rows) // 2], cols[len(cols) // 2]]

        totalDistance = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    totalDistance += abs(i - best_point[0]) + abs(j - best_point[1])
        return totalDistance