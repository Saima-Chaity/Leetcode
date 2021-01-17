# Cut Off Trees for Golf Event - https://leetcode.com/problems/cut-off-trees-for-golf-event/
'''You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix.
In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell
with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell
becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you
cannot cut off all the trees, return -1.

You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.
Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
'''

from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        def bfs(sr, sc, tr, tc):
            q = deque([(sr, sc, 0)])
            visited = set()
            while q:
                sr, sc, step = q.popleft()
                if sr == tr and sc == tc:
                    return step
                for dx, dy in direction:
                    next_x = dx + sr
                    next_y = dy + sc
                    if 0 <= next_x < row and 0 <= next_y < col and (next_x, next_y) not in visited and forest[next_x][
                        next_y]:
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y, step + 1))

            return -1

        if not forest or forest[0][0] == 0:
            return -1

        row = len(forest)
        col = len(forest[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        trees = []

        for i in range(row):
            for j in range(col):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort()
        source_row = 0
        source_col = 0
        totalStep = 0
        for height, i, j in trees:
            distance = bfs(source_row, source_col, i, j)
            if distance < 0:
                return -1
            totalStep += distance
            source_row, source_col = i, j
        return totalStep
