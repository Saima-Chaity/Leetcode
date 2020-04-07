# Number of Distinct Islands - https://leetcode.com/problems/number-of-distinct-islands/
'''Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if
one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
'''


class Solution(object):

    # "X" - start
    # "O" - out of bounce
    # "L" - left
    # "R" - right
    # "U" - up
    # "D" - down

    def numDistinctIslands(self, grid):

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        distinctIslands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = self.computePath(grid, i, j, "X")
                    distinctIslands.add(path)
        return len(distinctIslands)

    def computePath(self, grid, i, j, direction):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return "O"
        grid[i][j] = 0
        left = self.computePath(grid, i, j - 1, '"L"')
        right = self.computePath(grid, i, j + 1, "R")
        up = self.computePath(grid, i - 1, j, "U")
        down = self.computePath(grid, i + 1, j, "D")
        return direction + left + right + up + down


# Number of Distinct Islands II - https://leetcode.com/problems/number-of-distinct-islands-ii/
'''Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, 
or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).'''

# Example 1:
# 11000
# 10000
# 00001
# 00011
# Given the above grid map, return 1.

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        distinctIslands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    shape = []
                    self.computePath(grid, i, j, shape)
                    path = self.normalize(shape)
                    distinctIslands.add(path)
        return len(distinctIslands)

    def computePath(self, grid, i, j, shape):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        shape.append((i, j))
        self.computePath(grid, i, j - 1, shape)
        self.computePath(grid, i, j + 1, shape)
        self.computePath(grid, i - 1, j, shape)
        self.computePath(grid, i + 1, j, shape)

    def normalize(self, shape):
        rotated_shapes = [[] for _ in range(8)]
        for x, y in shape:
            rotated_shapes[0].append((x, y))
            rotated_shapes[1].append((x, -y))
            rotated_shapes[2].append((-x, y))
            rotated_shapes[3].append((-x, -y))
            rotated_shapes[4].append((y, x))
            rotated_shapes[5].append((-y, x))
            rotated_shapes[6].append((y, -x))
            rotated_shapes[7].append((-y, -x))

        for rs in rotated_shapes:
            rs.sort()

        normalizedShape = []
        for rotatedShape in rotated_shapes:
            temp = [(0, 0)]
            for i in range(1, len(rotatedShape)):
                temp.append((rotatedShape[i][0] - rotatedShape[0][0], rotatedShape[i][1] - rotatedShape[0][1]))
            normalizedShape.append(temp[:])
        normalizedShape.sort()
        return tuple(normalizedShape[0])


