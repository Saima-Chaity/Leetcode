# The Maze - https://leetcode.com/problems/the-maze/
'''There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down,
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the
borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true'''

from collections import deque
class Solution:
    class Solution:
        def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
            row, col = len(maze), len(maze[0])
            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visited = set()
            q = deque()
            q.append((start[0], start[1]))
            visited.add((start[0], start[1]))
            while q:
                x, y = q.popleft()
                if x == destination[0] and y == destination[1]:
                    return True
                for dx, dy in direction:
                    r, c = x, y
                    while 0 <= r < row and 0 <= c < col and maze[r][c] == 0:
                        r += dx
                        c += dy
                    if r != destination[0] or c != destination[1]:
                        r -= dx
                        c -= dy

                    if (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
            return False


#DFS
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        def dfs(x, y):
            if (x, y) in visited:
                return False
            visited.add((x, y))
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in direction:
                r, c = x, y
                while 0 <= r < row and 0 <= c < col and maze[r][c] == 0:
                    r += dx
                    c += dy
                if r != destination[0] or c != destination[1]:
                    r -= dx
                    c -= dy
                if dfs(r, c):
                    return True
            return False

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(maze)
        col = len(maze[0])
        visited = set()
        return dfs(start[0], start[1])


# The Maze II - https://leetcode.com/problems/the-maze-ii/
'''There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, 
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the 
destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) 
to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the 
borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12'''


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        q.append((start[0], start[1]))
        distance = [[float('inf') for c in range(col)] for r in range(row)]
        distance[start[0]][start[1]] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in direction:
                roll = distance[x][y]
                r, c = x, y
                while 0 <= r < row and 0 <= c < col and maze[r][c] == 0:
                    r += dx
                    c += dy
                if r != destination[0] or c != destination[1]:
                    r -= dx
                    c -= dy
                roll += abs(r - x) + abs(c - y)

                if roll < distance[r][c]:
                    distance[r][c] = roll
                    q.append((r, c))

        if distance[destination[0]][destination[1]] == float('inf'):
            return -1
        return distance[destination[0]][destination[1]]



# The Maze III - https://leetcode.com/problems/the-maze-iii/
'''There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), l
eft (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. 
There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. 
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). 
Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the 
lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
The ball and the hole coordinates are represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"'''


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        row, col = len(maze), len(maze[0])
        direction = [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]
        q = deque()
        q.append((ball[0], ball[1]))
        distance = [[float('inf') for c in range(col)] for r in range(row)]
        distance[ball[0]][ball[1]] = 0
        mapping = {}

        while q:
            x, y = q.popleft()
            for dx, dy, char in direction:
                path = mapping.get((x, y), "")
                roll = distance[x][y]
                r, c = x, y
                while 0 <= r < row and 0 <= c < col and maze[r][c] == 0 and (r != hole[0] or c != hole[1]):
                    r += dx
                    c += dy
                if r != hole[0] or c != hole[1]:
                    r -= dx
                    c -= dy
                roll += abs(r - x) + abs(c - y)
                path += char

                if roll < distance[r][c]:
                    distance[r][c] = roll
                    mapping[(r, c)] = path
                    if r != hole[0] or c != hole[1]:
                        q.append((r, c))
                elif roll == distance[r][c] and path < mapping.get((r, c), ""):
                    mapping[(r, c)] = path
                    if r != hole[0] or c != hole[1]:
                        q.append((r, c))

        if (hole[0], hole[1]) in mapping:
            return mapping[(hole[0], hole[1])]
        else:
            return 'impossible'