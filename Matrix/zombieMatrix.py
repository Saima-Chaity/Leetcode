'''Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human
beings into zombies every hour. Find out how many hours does it take to infect all humans?'''

class Solution:
    def minHours(self, matrix):
        def visitNeighbours(zombie, matrix):
            neighbours = []
            for i, j in zombie:
                if i > 0 and matrix[i-1][j] == 0:
                    matrix[i - 1][j] = 1
                    neighbours.append((i-1, j))
                if j > 0 and matrix[i][j-1] == 0:
                    matrix[i][j-1] = 1
                    neighbours.append((i, j-1))
                if i < len(matrix) - 1 and matrix[i+1][j] == 0:
                    matrix[i + 1][j] = 1
                    neighbours.append((i+1, j))
                if j < len(matrix[0]) - 1 and matrix[i][j+1] == 0:
                    matrix[i][j+1] = 1
                    neighbours.append((i, j+1))
            return neighbours

        row = len(matrix)
        col = len(matrix[0])
        hoursRequired = 0
        zombie = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    zombie.append((i, j))

        while (1):
            zombie = visitNeighbours(zombie, matrix)
            if len(zombie) == 0:
                break
            hoursRequired += 1
        return hoursRequired if hoursRequired > 0 else -1


##Second Approach
def minHour(self, rows, columns, grid):
    if not rows or not columns:
        return 0

    q = [[i, j] for i in range(rows) for j in range(columns) if grid[i][j] == 1]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    time = 0

    while q:
        new = []
        for [i, j] in q:
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni, nj])
        q = new
        if not q:
            break

        time += 1
    return time



# ```
# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]
#
# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]
# ```
matrix = [[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
print(Solution.minHours((), matrix))
print(Solution.minHour((), len(matrix), len(matrix[0]), matrix))