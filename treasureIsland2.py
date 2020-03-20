'''You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest
route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the
starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island
is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any
of the treasure islands.'''

# Input:
# [['S', 'O', 'O', 'S', 'S'],
#  ['D', 'O', 'D', 'O', 'D'],
#  ['O', 'O', 'O', 'O', 'X'],
#  ['X', 'D', 'D', 'O', 'O'],
#  ['X', 'D', 'D', 'D', 'O']]
#
# Output: 3
# Explanation:
# You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
# **/

from collections import deque
import sys
class Solution:
    def treasureIsland(grid):

        def findTreasure(i, j, grid):
            q = deque()
            q.append((i, j, 0))
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visited = set()

            while q:
                for i in range(len(q)):
                    x, y, steps = q.popleft()
                    if grid[x][y] == 'X':
                        return steps

                    for x1, y1 in direction:
                        xi = x + x1
                        yj = y + y1
                        if xi >= 0 and yj >= 0 and xi < len(grid) and yj < len(grid[0]) and grid[xi][yj] != 'D':
                            visited.add((xi, yj))
                            q.append((xi, yj, steps + 1))
            return sys.maxsize


        result = sys.maxsize

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    temp = findTreasure(i, j, grid)
                    result = min(temp, result)
        return result

grid = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]
print(Solution.treasureIsland(grid))

