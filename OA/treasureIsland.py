'''You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and
dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure.
So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start
from the top-left corner of the map and can move one block up, down, left or right at a time.
The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe.
Output the minimum number of steps to get to the treasure.'''

#  [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]

# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.


from collections import deque
class Solution:
    def treasureIsland(grid):
        q = deque()
        q.append((0, 0))
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        visited.add((0, 0))
        steps = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                x, y = node[0], node[1]

                if grid[x][y] == 'X':
                    return steps

                for x1, y1 in direction:
                    xi = x + x1
                    yj = y + y1
                    if xi >= 0 and yj >= 0 and xi < len(grid) and yj < len(grid[0])-1:
                        if grid[xi][yj] != 'D':
                            if (xi, yj) not in visited:
                                visited.add((xi, yj))
                                q.append((xi, yj))
            steps += 1
        return -1


grid = [['O', 'O', 'O', 'O'], ['D', 'O', 'D', 'O'], ['O', 'O', 'O', 'O'], ['X', 'D', 'D', 'O']]
print(Solution.treasureIsland((grid)))

