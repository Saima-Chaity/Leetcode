'''Shortest Distance from All Buildings - https://leetcode.com/problems/shortest-distance-from-all-buildings/

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance.
You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according
to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
'''

# space optimized
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        def bfs(i, j, iterationCount):
            q = deque()
            q.append((i, j))
            steps = 0
            min_distance = float('inf')
            while q:
                qLength = len(q)
                steps += 1
                for _ in range(qLength):
                    x, y = q.popleft()
                    for dx, dy in direction:
                        x_dx = x + dx
                        y_dy = y + dy
                        if 0 <= x_dx < row and 0 <= y_dy < col and grid[x_dx][y_dy] == iterationCount:
                            q.append((x_dx, y_dy))
                            grid[x_dx][y_dy] -= 1
                            total_sum_matrix[x_dx][y_dy] += steps
                            min_distance = min(min_distance, total_sum_matrix[x_dx][y_dy])
            return min_distance

        row = len(grid)
        col = len(grid[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        iterationCount = 0
        total_sum_matrix = [[0] * col for _ in range(row)]
        shortest_distance = float('inf')

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    shortest_distance = bfs(i, j, iterationCount)
                    iterationCount -= 1
                    if shortest_distance == float('inf'):
                        return -1

        return shortest_distance


# TLE
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            visited = set()
            q = deque()
            q.append((i, j))
            totalDistance = 0
            houseReached = 0
            steps = 0
            while q and houseReached != totalHouse:
                qLength = len(q)
                for _ in range(qLength):
                    x, y = q.popleft()
                    if grid[x][y] == 1:
                        houseReached += 1
                        totalDistance += steps
                        continue
                    for dx, dy in direction:
                        x_dx = x + dx
                        y_dy = y + dy
                        if 0 <= x_dx < row and 0 <= y_dy < col and grid[x_dx][y_dy] != 2 and (
                        x_dx, y_dy) not in visited:
                            q.append((x_dx, y_dy))
                            visited.add((x_dx, y_dy))
                steps += 1

            if houseReached != totalHouse:
                for i in range(row):
                    for j in range(col):
                        if grid[i][j] == 0 and (i, j) in visited:
                            grid[i][j] = 2
                return float('inf')
            return totalDistance

        row = len(grid)
        col = len(grid[0])
        shortest_distance = float('inf')
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        totalHouse = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    totalHouse += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    current_distance = bfs(i, j)
                    shortest_distance = min(shortest_distance, current_distance)
        return shortest_distance if shortest_distance != float('inf') else -1


# Another aproach
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            visited = set()
            q = deque()
            q.append((i, j))
            steps = 0
            while q:
                qLength = len(q)
                for _ in range(qLength):
                    x, y = q.popleft()
                    if grid[x][y] == 0:
                        if distance_matrix[x][y] != 0:
                            step, house_reached = distance_matrix[x][y][0], distance_matrix[x][y][1]
                            distance_matrix[x][y] = [step + steps, house_reached + 1]
                        else:
                            distance_matrix[x][y] = [steps, 1]

                    for dx, dy in direction:
                        x_dx = x + dx
                        y_dy = y + dy
                        if 0 <= x_dx < row and 0 <= y_dy < col and grid[x_dx][y_dy] == 0 and (
                        x_dx, y_dy) not in visited:
                            q.append((x_dx, y_dy))
                            visited.add((x_dx, y_dy))
                steps += 1

        row = len(grid)
        col = len(grid[0])
        shortest_distance = float('inf')
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        totalHouse = 0
        distance_matrix = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    totalHouse += 1
                    bfs(i, j)

        for i in range(row):
            for j in range(col):
                if distance_matrix[i][j] != 0 and distance_matrix[i][j][1] == totalHouse:
                    shortest_distance = min(shortest_distance, distance_matrix[i][j][0])
        return shortest_distance if shortest_distance != float('inf') else -1

